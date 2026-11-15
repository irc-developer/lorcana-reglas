"""Prepara posiciones reales limitadas; no evalúa jugadas ni revela elecciones."""
import argparse
import importlib.util
import json
from pathlib import Path

from herramientas.profesora_lorcana.contratos import digest, file_digest, read

import sys
# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo

ROOT = Path(__file__).resolve().parents[2]
HISTORICAL = ruta_trabajo('analisis/profesora-lorcana/analisis-rotor/historico-7332')
DEFAULT_OUT = ruta_trabajo('analisis/profesora-lorcana/desarrollo/coordinacion/piloto-v02')


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    content = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode('utf-8')
    if path.exists() and path.read_bytes() != content:
        raise ValueError('Destino distinto existente: usar un directorio nuevo')
    if not path.exists():
        path.write_bytes(content)


def projector():
    path = ROOT / 'herramientas/duels_analisis/vista_decision.py'
    spec = importlib.util.spec_from_file_location('limited_view_for_pilot', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.build_view


def redact_ids(value, game, opaque):
    if isinstance(value, dict):
        return {key: redact_ids(item, game, opaque) for key, item in value.items()}
    if isinstance(value, list):
        return [redact_ids(item, game, opaque) for item in value]
    return opaque if value == game else value


def prepare(out=DEFAULT_OUT):
    out = resolver_ruta(out)
    audit = read(HISTORICAL / 'reconstruccion.json')
    handoff = read(ruta_trabajo('analisis/profesora-lorcana/datos/privado/entrega-historico-final.json'))
    batch = resolver_ruta(handoff['batch'])
    from herramientas.duels_datos.catalogo import verify_batch
    if verify_batch(batch, originals=False):
        raise ValueError('Lote de origen alterado')
    rows = {row['game_id']: row for row in
            map(json.loads, (batch / 'catalogo.jsonl').read_text(encoding='utf-8').splitlines())}
    identities = read(batch / 'normalizacion.json')['identities']
    excluded = {game['gameId'] for game in read(HISTORICAL / 'muestra.json')['games']}
    for path in (ruta_trabajo('analisis/duels-2026-10-15')).glob('partida-*-resumen.json'):
        excluded.add(read(path)['gameId'])
    games = [g for g in audit['games'] if g['status'] == 'reconstructed'
             and g['gameId'] not in excluded
             and (not rows[g['gameId']].get('match_id') or rows[g['gameId']].get('match_game_number') == 1)]
    games.sort(key=lambda g: g['gameId'])
    build_view = projector()
    used, records, private = set(), [], []
    for phase in ('apertura', 'desarrollo', 'cierre'):
        count = 0
        for game in games:
            if count == 4:
                break
            game_id = game['gameId']
            if game_id in used:
                continue
            prefix = resolver_ruta(game['prefix'])
            actions = read(str(prefix) + '-acciones.json')
            own = rows[game_id]['your_player']
            # Sampling depends on prior public state/phase, never win/loss.
            candidates = [a for a in actions if a['player'] == own and
                          ((phase == 'apertura' and a['actionType'] == 'MULLIGAN') or
                           (phase != 'apertura' and a['turnNumber'] >= 6 and
                            a['actionType'] in ('ADD_TO_INK', 'PLAY_CARD', 'QUEST', 'CHALLENGE', 'ATTACK')))]
            for action in candidates:
                view = build_view(prefix, action['seq'])
                if view['limits']['pendingPromptIncomplete']:
                    continue
                if phase == 'cierre' and view['own']['lore'] < 12:
                    continue
                if phase == 'desarrollo' and view['own']['lore'] >= 12:
                    continue
                opaque = f'g-{len(records) + 1:02}'
                original_refs = view.pop('inputHashes')
                view['position']['matchId'] = None  # Eligible games are first game/BO1.
                view = redact_ids(view, game_id, opaque)
                for card in view['ownRegisteredList']:
                    identity = identities.get(card['id'], '')
                    if identity.startswith('full-name:'):
                        card['name'] = identity.removeprefix('full-name:')
                position_id = f'pilot-{len(records) + 1:02}'
                position = {'schema': 'lorcana-position-v1', 'position_id': position_id,
                            'game_ref': {'id': opaque, 'perspective': own, 'game_number': 1},
                            'deck_ref': {'printing_sha256': rows[game_id]['deck']['printing_sha256'],
                                         'composition_sha256': rows[game_id]['deck']['composition_sha256'],
                                         'own_registered_list': view['ownRegisteredList']},
                            'boundary': {**view['boundary'], 'limited_view_sha256': digest(view)},
                            'available_state': view, 'known_information': [],
                            'rules_evidence': {'status': 'requires_verification',
                                               'engine_fields_are_not_authority': True},
                            'completeness': {'pending_prompt_incomplete': False,
                                             'prior_game_memory_required': False,
                                             'rules_evidence_incomplete': True}}
                # Stage only the limited artifact. No choice or original path beside it.
                destination = out / 'posiciones' / f'{position_id}.json'
                write(destination, position)
                records.append({'position_id': position_id, 'phase_for_sampling': phase,
                                'path': str(destination.resolve()), 'position_sha256': digest(position)})
                private.append({'position_id': position_id, 'game_id': game_id,
                                'prefix': str(prefix), 'before_seq': action['seq'],
                                'source_input_hashes': original_refs,
                                'observed_action_record': action})
                used.add(game_id)
                count += 1
                break
        if count != 4:
            raise ValueError('Muestra insuficiente para una fase; no presentar selección parcial como piloto completo')
    write(out / 'RESERVADO-COORDINACION.json', {
        'schema': 'lorcana-pilot-private-mapping-v1', 'batch_id': batch.name,
        'reconstruction_audit_sha256_bytes': file_digest(HISTORICAL / 'reconstruccion.json'),
        'excluded_previously_reviewed_games': sorted(excluded), 'positions': private})
    write(out / 'MANIFIESTO.json', {
        'schema': 'lorcana-pilot-position-manifest-v1', 'contract_version': '0.2',
        'positions_prepared': len(records), 'positions_strategically_reviewed': 0,
        'selection': 'Four per phase; first eligible unused game by ID; first game or BO1; no outcome strata.',
        'limits': ['Limited positions prepared, not strategic diagnoses.',
                   'Closure sample means own lore >=12, not a proven lethal.',
                   'Card text/engine attributes require corpus verification for dependent judgments.',
                   'Sampling coordinator has access to original metadata; evaluators must declare their own context exposure.',
                   'Keep RESERVADO-COORDINACION.json out of evaluator context.'],
        'positions': records})
    return out, records


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=resolver_ruta, default=DEFAULT_OUT)
    args = parser.parse_args()
    directory, positions = prepare(args.out)
    print(json.dumps({'directory': str(directory), 'prepared': len(positions), 'reviewed': 0}))
