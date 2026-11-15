"""Comprueba ambos planes antes de exportar una elección limitada del piloto."""
import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import re

from herramientas.profesora_lorcana.contratos import (
    check_reference, digest, file_digest, read, reference,
)
from herramientas.profesora_lorcana.analista import registro as analyst
from herramientas.profesora_lorcana.revisora import registro as reviewer

import sys
# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo


def write_new(path, value):
    path = resolver_ruta(path)
    content = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode('utf-8')
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as handle:
        handle.write(content)


def seal(position_path, analyst_session, reviewer_session, out):
    """No consulta acciones originales ni elecciones durante la comprobación."""
    position = read(position_path)
    a, r = resolver_ruta(analyst_session), resolver_ruta(reviewer_session)
    state = analyst.verify(a)
    if state['kinds'] != ['position', 'plan']:
        raise ValueError('La analista debe tener solo posición y plan antes de revelar')
    check_reference(reference(read(a / 'position.json')), position)
    ap = read(a / 'plan-0001.json')
    rrefs = reviewer.references(r)
    if 'independent_plan_ref' not in rrefs or 'choice_ref' in rrefs or (r / 'revelacion.json').exists():
        raise ValueError('La revisora debe tener su plan y ninguna revelación')
    check_reference(rrefs['position'], position)
    rp = read(r / 'plan.json')['artifact']
    check_reference(rrefs['independent_plan_ref'], rp)
    if (ap['position_sha256'] != digest(position) or rp['position_sha256'] != digest(position)
            or ap['role'] != 'analista' or rp['role'] != 'revisora'):
        raise ValueError('Los dos planes no corresponden a la misma posición y papeles')
    record = {'schema': 'lorcana-dual-plan-seal-v1', 'position_id': position['position_id'],
              'checked_at': datetime.now(timezone.utc).isoformat(), 'position_ref': reference(position),
              'analyst_plan_ref': reference(ap), 'reviewer_plan_ref': reference(rp),
              'analyst_record_receipt': state['last_record'],
              'reviewer_plan_receipt_sha256_bytes': file_digest(r / 'plan.json'),
              'reviewer_exposure_declaration': rrefs['exposure_declaration'],
              'recorded_stages_precede_choice_export': True,
              'limits': ['Comprobación de artefactos y orden registrado; no prueba conocimiento previo, aislamiento o legalidad.',
                         'La declaración de exposición del contexto se conserva sin convertirla en independencia demostrada.']}
    write_new(resolver_ruta(out) / 'SELLO-PLANES.json', record)
    return position, record


def extract_choice(position, source):
    """Incluye acción registrada; omite robos, daño, sabiduría ganada y continuación."""
    action = source['observed_action_record']
    source_path = resolver_ruta(source['prefix'] + '-eventos.json')
    expected = source['source_input_hashes'].get(source_path.name)
    if not expected or file_digest(source_path) != expected:
        raise ValueError('Los eventos originales cambiaron desde la preparación')
    events = read(source_path)[action['logsFromInclusive']:action['logsToExclusive']]
    if action['actionType'] == 'PLAY_CARD' and not events and action['logsFromInclusive'] == action['logsToExclusive']:
        return extract_pending_bodyguard_play(position, source)
    event_type = {'MULLIGAN': 'MULLIGAN', 'PLAY_CARD': 'CARD_PLAYED',
                  'ADD_TO_INK': 'CARD_INKED', 'QUEST': 'CARD_QUEST'}.get(action['actionType'])
    if event_type is None:
        raise ValueError('Acción todavía sin proyección limitada implementada; revisar su evidencia')
    primary = [e for e in events if e.get('type') == event_type
               and e.get('player') == position['game_ref']['perspective']]
    if len(primary) != 1:
        raise ValueError('No hay un evento único de elección asociado a la perspectiva')
    event = primary[0]
    chosen_refs = event.get('cardRefs', [])
    mulligan_count = None
    if event_type == 'MULLIGAN':
        mulligan_count = event.get('data', {}).get('mulliganCount')
        if type(mulligan_count) is not int or mulligan_count < 0:
            raise ValueError('Mulligan sin cantidad válida')
        # The event's cardRefs contains BOTH returned and drawn cards. Export
        # only placeholders explicitly in the returned portion of the template.
        if mulligan_count == 0:
            chosen_refs = []
        else:
            prefix, separator, _ = event.get('message', '').partition('. Drew:')
            match = re.search(r'\bmulliganed (\d+) cards?:\s*(.*)$', prefix)
            if not separator or not match or int(match[1]) != mulligan_count:
                raise ValueError('Plantilla de mulligan desconocida: no inferir cartas elegidas')
            returned = match[2]
            if not re.fullmatch(r'\{card:\d+\}(?:,\s*\{card:\d+\})*', returned):
                raise ValueError('Referencias del mulligan ambiguas')
            indices = [int(index) for index in re.findall(r'\{card:(\d+)\}', returned)]
            if (len(indices) != mulligan_count or len(set(indices)) != len(indices)
                    or any(index >= len(chosen_refs) for index in indices)):
                raise ValueError('Referencias del mulligan inconsistentes')
            chosen_refs = [chosen_refs[index] for index in indices]
    cards = [{k: card[k] for k in ('id', 'name') if k in card}
             for card in chosen_refs]
    if event_type != 'MULLIGAN':
        chosen_id = event.get('data', {}).get('cardId')
        cards = [card for card in cards if chosen_id and card.get('id') == chosen_id]
        if len(cards) != 1:
            raise ValueError('Carta elegida ausente o ambigua en el evento')
    observed = {'action_type': action['actionType'], 'cards_recorded': cards}
    if event_type == 'MULLIGAN':
        if len(cards) != mulligan_count:
            raise ValueError('Mulligan sin cantidades/referencias consistentes')
        observed['cards_changed_count'] = mulligan_count
    elif not cards:
        raise ValueError('Elección sin carta identificada')
    evidence = {'schema': 'lorcana-action-evidence-v1', 'position_id': position['position_id'],
                'position_sha256': digest(position), 'action_seq': action['seq'],
                'event_index': event['index'], 'event_type': event_type,
                'recorded_choice': observed,
                'source_sha256_bytes': expected,
                'limits': ['Acción observada por Duels; no certifica legalidad ni intención del jugador.',
                           'No incluye los efectos posteriores de la acción ni la continuación.']}
    choice = {'schema': 'lorcana-choice-v1', 'position_id': position['position_id'],
              'position_sha256': digest(position), 'observed_action': observed,
              'evidence_ref': reference(evidence), 'intention': 'desconocida'}
    analyst.validate('choice', choice)
    reviewer.validate(choice, 'choice', position)
    return choice, evidence


def extract_pending_bodyguard_play(position, source):
    """Identify only an initiated play from its immediate prompt, never its answer."""
    action = source['observed_action_record']
    summary_path = resolver_ruta(source['prefix'] + '-resumen.json')
    expected_summary = source['source_input_hashes'].get(summary_path.name)
    if not expected_summary or file_digest(summary_path) != expected_summary:
        raise ValueError('Resumen original alterado o sin recibo')
    summary = read(summary_path)
    raw = resolver_ruta(summary['source']).read_bytes()
    raw_hash = hashlib.sha256(raw).hexdigest()
    if raw_hash != summary['sourceSha256']:
        raise ValueError('Replay original alterado')
    decoded = gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw
    if hashlib.sha256(decoded).hexdigest() != summary['decodedSha256']:
        raise ValueError('Replay descomprimido alterado')
    replay = json.loads(decoded.decode('utf-8-sig'))
    frames = [f for f in replay['frames'] if f.get('seq') == action['seq']]
    if len(frames) != 1 or replay.get('format') != 'duels-replay-v1':
        raise ValueError('Frame inmediato ausente o ambiguo')
    frame = frames[0]
    if (action['actionType'] != 'PLAY_CARD' or action['player'] != position['game_ref']['perspective']
            or action['logsFromInclusive'] != action['logsToExclusive']
            or any(frame.get(k) != action.get(k) for k in ('seq', 'actionType', 'player', 'turnNumber'))
            or frame.get('logCountAfter') != action['logsToExclusive']
            or frame.get('ts') != action.get('timestamp')):
        raise ValueError('Frame inmediato de otra acción o perspectiva')
    # Narrow supported shape: opening this prompt creates no card movements,
    # effects, draws or results. Unknown patches fail closed.
    prompts = []
    for operation in frame['patch']:
        if operation.get('path') == '/canRequestUndo' and operation.get('op') == 'replace' and type(operation.get('value')) is bool:
            continue
        if operation.get('path') == '/pendingPrompts/0' and operation.get('op') == 'add':
            prompts.append(operation['value'])
        else:
            raise ValueError('Patch no soportado para juego pendiente')
    if len(prompts) != 1:
        raise ValueError('Prompt inmediato ausente o ambiguo')
    prompt = prompts[0]
    if (prompt.get('type') != 'boolean' or prompt.get('message') != 'bodyguardExertChoice'
            or prompt.get('player') != action['player'] or not prompt.get('sourceCardInstanceId')):
        raise ValueError('Prompt inmediato no soportado')
    cards = [card for card in position['available_state']['own']['hand']
             if card.get('instanceId') == prompt['sourceCardInstanceId']]
    if len(cards) != 1 or not cards[0].get('id') or not cards[0].get('fullName'):
        raise ValueError('Fuente del prompt no identifica una carta propia previa')
    observed = {'action_type': 'PLAY_CARD',
                'stage': 'initiated_pending_bodyguard_choice',
                'cards_recorded': [{'id': cards[0]['id'], 'name': cards[0]['fullName']}],
                'resolution_observed': False}
    evidence = {'schema': 'lorcana-action-evidence-v1', 'position_id': position['position_id'],
                'position_sha256': digest(position), 'action_seq': action['seq'],
                'event_index': None, 'event_type': 'PLAY_INITIATED_PENDING_PROMPT',
                'recorded_choice': observed, 'source_sha256_bytes': raw_hash,
                'summary_sha256_bytes': expected_summary,
                'limits': ['Selección iniciada identificada por el prompt inmediato y una instancia de la mano previa.',
                           'No acredita pago, carta en juego, respuesta de Guardaespaldas ni resolución.',
                           'No incluye otro frame, efectos, robos, resultado ni continuación.']}
    choice = {'schema': 'lorcana-choice-v1', 'position_id': position['position_id'],
              'position_sha256': digest(position), 'observed_action': observed,
              'evidence_ref': reference(evidence), 'intention': 'desconocida'}
    analyst.validate('choice', choice)
    reviewer.validate(choice, 'choice', position)
    return choice, evidence


def release(pilot_root, position_path, analyst_session, reviewer_session, out):
    # Intentionally perform BOTH stage checks before opening the reserved map.
    position, record = seal(position_path, analyst_session, reviewer_session, out)
    reserved = read(resolver_ruta(pilot_root) / 'RESERVADO-COORDINACION.json')
    matches = [item for item in reserved['positions'] if item['position_id'] == position['position_id']]
    if len(matches) != 1:
        raise ValueError('Mapa de posición ausente o ambiguo')
    choice, evidence = extract_choice(position, matches[0])
    write_new(resolver_ruta(out) / 'evidencia-eleccion.json', evidence)
    write_new(resolver_ruta(out) / 'eleccion.json', choice)
    return {'position_id': position['position_id'], 'choice_ref': reference(choice),
            'dual_plan_seal_ref': reference(record), 'directory': str(resolver_ruta(out).resolve())}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pilot-root', type=resolver_ruta, required=True)
    parser.add_argument('--position', type=resolver_ruta, required=True)
    parser.add_argument('--analyst-session', type=resolver_ruta, required=True)
    parser.add_argument('--reviewer-session', type=resolver_ruta, required=True)
    parser.add_argument('--out', type=resolver_ruta, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(release(args.pilot_root, args.position, args.analyst_session,
                                 args.reviewer_session, args.out), ensure_ascii=True))
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f'No se publica la elección: {error}\n')
