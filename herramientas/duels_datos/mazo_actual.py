"""Extrae la última lista jugada de ROTOR y la compara con la anterior distinta."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import tempfile

from herramientas.duels.duels import Client, DuelsError, Importer, Lock, atomic, load_token, now
from .catalogo import (consolidate, digest, encode, file_hash, importer_observations,
                       normalize_list, read_json, utc, verify_batch)

# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo

ROOT = Path(__file__).resolve().parents[2]
PRIVATE = ruta_trabajo('analisis/profesora-lorcana/datos/privado')
HANDOFF = PRIVATE / 'entrega-historico-final.json'


def relation(left, right):
    if not left.get('printing_sha256') or not right.get('printing_sha256'):
        raise ValueError('Una lista está ausente o es inválida; no se salta esa partida')
    if left['printing_sha256'] == right['printing_sha256']:
        return 'same'
    if not left['identity_complete'] or not right['identity_complete']:
        return 'unresolved_identity'
    if left['composition_sha256'] == right['composition_sha256']:
        return 'printing_only'
    return 'composition_change'


def select_versions(rows, account, deck_id):
    selected = [r for r in rows if r['account_id'] == account and r['your_deck_id'] == deck_id]
    if not selected:
        raise ValueError('No hay partidas del objeto de mazo seleccionado')
    for row in selected:
        if not row.get('started_at'):
            raise ValueError('Falta fecha de inicio: no se puede establecer la última partida')
    selected.sort(key=lambda r: utc(r['started_at']), reverse=True)
    current = selected[0]
    # Un empate temporal con listas distintas no permite ordenar versiones.
    for a, b in zip(selected, selected[1:]):
        if utc(a['started_at']) == utc(b['started_at']) and relation(a['deck'], b['deck']) != 'same':
            raise ValueError('Empate temporal entre listas distintas: orden de versiones ambiguo')
    relation(current['deck'], current['deck'])
    skipped = 0
    for row in selected[1:]:
        kind = relation(current['deck'], row['deck'])
        if kind in ('same', 'printing_only'):
            skipped += 1
            continue
        return current, row, kind, skipped
    return current, None, 'no_previous_distinct', skipped


def label(identity):
    return identity.removeprefix('full-name:')


def differences(current, previous):
    before = previous['composition_counts'] if previous else {}
    after = current['composition_counts']
    return [{'identity': key, 'name': label(key), 'before': before.get(key, 0),
             'after': after.get(key, 0), 'delta': after.get(key, 0) - before.get(key, 0)}
            for key in sorted(set(before) | set(after)) if before.get(key, 0) != after.get(key, 0)]


def replay_check(row, identities):
    asset = row.get('files', {}).get('replay', {})
    if asset.get('status') != 'verified_json':
        return {'status': 'not_available', 'acquisition_status': asset.get('status')}
    ref = asset.get('decoded_json') or asset
    path = resolver_ruta(ref['path'])
    if file_hash(path) != ref['sha256']:
        raise ValueError('Replay alterado: comprobación de integridad fallida')
    raw = path.read_bytes()
    replay = json.loads(gzip.decompress(raw) if raw.startswith(b'\x1f\x8b') else raw)
    if (replay.get('gameId') != row['game_id'] or replay.get('perspective') != row['your_player']
            or replay.get('baseSnapshot', {}).get('viewingAs') != row['your_player']):
        raise ValueError('El replay no corresponde a la partida/perspectiva')
    header = normalize_list(replay.get('decklist'), identities)
    kind = relation(row['deck'], header)
    return {'status': 'agreement' if kind in ('same', 'printing_only') else 'conflict',
            'comparison': kind, 'source': {'path': str(path.resolve()), 'sha256': ref['sha256']},
            'header_list': header,
            'changes_from_header_to_history': differences(row['deck'], header)}


def snapshot(row, identities, sources):
    evidence = []
    for entry in row.get('sources', []):
        ref = sources[entry['source']]
        if file_hash(ref['path']) != ref['sha256']:
            raise ValueError('Fuente original de la lista alterada')
        if ref not in evidence:
            evidence.append(ref)
    deck = normalize_list(row['deck']['original'], identities)
    own = dict(row, deck=deck)
    return {'game_id': row['game_id'], 'started_at': row['started_at'], 'ended_at': row.get('ended_at'),
            'your_player': row['your_player'], 'deck': deck, 'sources': evidence,
            'replay_check': replay_check(own, identities),
            'observed_list_hashes': sorted({d['printing_sha256'] for d in row.get('deck_observations', [])
                                            if d.get('printing_sha256')})}


def render(report):
    current, previous = report['current'], report['previous']
    lines = ['# Último mazo jugado — ROTOR Investigaorets', '',
             f"Consulta: {report['data_as_of']}. Fuente de la lista: historial de Duels.",
             f"Partida: `{current['game_id']}`. Inicio (UTC): {current['started_at']}.",
             f"Total: **{current['deck']['total_cards']} cartas**.", '']
    for title, item in (('actual', current), ('anterior', previous)):
        if item:
            state = {'agreement': 'coincide', 'conflict': 'discrepa',
                     'not_available': 'sin replay disponible'}[item['replay_check']['status']]
            lines.append(f'Contraste con el encabezado del replay ({title}): {state}.')
    lines.append('')
    for warning in report['warnings']:
        lines += [f'**Aviso:** {warning}', '']
    lines += ['## Lista actual', '']
    for identity, count in sorted(current['deck']['composition_counts'].items()):
        lines.append(f'- {count} × {label(identity)}')
    lines += ['', '## Cambios respecto a la anterior distinta', '']
    if previous:
        lines += [f"Referencia: `{previous['game_id']}`, {previous['started_at']} (UTC), "
                  f"{previous['deck']['total_cards']} cartas.", '',
                  '| Carta | Antes | Ahora | Cambio |', '| --- | ---: | ---: | ---: |']
        for change in report['changes']:
            name = change['name'].replace('|', '\\|')
            lines.append(f"| {name} | {change['before']} | {change['after']} | {change['delta']:+d} |")
    else:
        lines.append('No se ha encontrado una composición anterior distinta en las partidas disponibles.')
    lines += ['', f"Partidas intermedias con la misma composición: {report['same_composition_games_skipped']}.", '',
              'La lista corresponde a una partida jugada; no acredita ediciones guardadas después en el constructor.',
              'Los nombres son identidades observadas en Duels; este informe no verifica texto ni reglas de cartas.', '']
    return '\n'.join(lines)


def publish_report(report, out):
    report_id = digest({'report': report, 'renderer_version': 1})
    directory = resolver_ruta(out) / report_id
    files = {'comparacion.json': encode(report), 'INFORME.md': render(report).encode('utf-8'),
             'mazo-actual.txt': ('\n'.join(f'{count} {label(identity)}' for identity, count in
                                         sorted(report['current']['deck']['composition_counts'].items())) + '\n').encode('utf-8')}
    files['manifiesto.json'] = encode({'schema': 'duels-deck-report-manifest-v1', 'report_id': report_id,
                                     'artifacts': {name: hashlib.sha256(data).hexdigest()
                                                   for name, data in files.items()}})
    if directory.exists():
        if any(not (directory / name).is_file() or (directory / name).read_bytes() != data for name, data in files.items()):
            raise ValueError('Informe existente alterado; no se sobrescribe')
        return directory
    directory.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=directory.parent) as temp:
        staged = resolver_ruta(temp) / 'informe'
        staged.mkdir()
        for name, data in files.items():
            (staged / name).write_bytes(data)
        staged.rename(directory)
    return directory


def build(handoff=HANDOFF, out=PRIVATE / 'mazo-actual', refresh=False, manifest=None):
    handoff = resolver_ruta(handoff)
    hand = read_json(handoff)
    batch = resolver_ruta(hand['batch'])
    if verify_batch(batch, originals=False):
        raise ValueError('Lote de referencia alterado')
    selection = read_json(batch / 'seleccion.json')
    if selection.get('schema') != 'duels-selection-evidence-v1' or selection.get('target_name') != 'ROTOR Investigaorets':
        raise ValueError('La selección de referencia no identifica ROTOR Investigaorets')
    account, deck_id = selection['account_id'], selection['target_deck_id']
    identities = read_json(batch / 'normalizacion.json')['identities']
    base_rows = [json.loads(line) for line in (batch / 'catalogo.jsonl').read_text(encoding='utf-8').splitlines()]
    sources = {s['sha256']: s for s in read_json(batch / 'fuentes.json')}
    batch_coverage = read_json(batch / 'cobertura.json')
    coverage = {key: batch_coverage[key] for key in ('games', 'input_history', 'limits')}
    rows = base_rows
    data_as_of = 'Lote histórico local; sin consulta nueva'
    acquisition, request_count = None, 0
    if refresh:
        # Ventana nueva completa de metadatos: no presupone orden de la API,
        # ni que la fecha de actualización sea la fecha de la partida.
        acquisition = resolver_ruta(out) / 'adquisiciones' / now().replace(':', '').replace('.', '-')
        client = Client(load_token())
        with Lock(acquisition):
            importer = Importer(acquisition, client)
            params = {'format': 'json', 'limit': 250, 'to': now()}
            importer.run(params, max_pages=0, download_games=0)
            if importer.m['account']['id'] != account:
                raise ValueError('La cuenta autenticada difiere del histórico')
            observations, refs, _, fresh_coverage = importer_observations(importer.path)
            if not fresh_coverage['enumeration_complete_verified']:
                raise ValueError('Historial nuevo incompleto: no se acredita la última partida')
            rows, _ = consolidate(observations, identities, selection_evidence=selection)
            # Reutiliza archivos únicamente para el mismo replay y perspectiva.
            by_game = {r['game_id']: r for r in base_rows if r['account_id'] == account}
            for row in rows:
                old = by_game.get(row['game_id'])
                if old and old['replay_id'] == row['replay_id'] and old['your_player'] == row['your_player']:
                    row['files'] = old['files']
            current, previous, _, _ = select_versions(rows, account, deck_id)
            needed = [r['game_id'] for r in (current, previous) if r and
                      r['files']['replay'].get('status') != 'verified_json' and r.get('replay_id')]
            if needed:
                importer.run(params, skip_history=True, download_games=len(needed), game_ids=needed)
                acquired, _, _, _ = importer_observations(importer.path)
                assets = {o['row']['game_id']: o['files'] for o in acquired}
                for row in rows:
                    if row['game_id'] in needed:
                        row['files'] = assets[row['game_id']]
            sources.update({s['sha256']: s for s in refs})
            data_as_of = params['to']
            coverage = fresh_coverage
            request_count = client.requests
    elif manifest:
        observations, refs, _, coverage = importer_observations(manifest)
        parameters = coverage['parameters']
        if (not coverage['enumeration_complete_verified'] or parameters.get('from')
                or parameters.get('queue') or parameters.get('source') not in (None, 'all')):
            raise ValueError('Se requiere una enumeración completa sin filtro inferior, cola ni fuente')
        if any(o['account_id'] != account for o in observations):
            raise ValueError('El manifiesto pertenece a otra cuenta')
        rows, _ = consolidate(observations, identities, selection_evidence=selection)
        old_rows = {r['game_id']: r for r in base_rows if r['account_id'] == account}
        for row in rows:
            old = old_rows.get(row['game_id'])
            if (old and old['replay_id'] == row['replay_id'] and old['your_player'] == row['your_player']
                    and row['files']['replay'].get('status') != 'verified_json'):
                row['files'] = old['files']
        sources.update({s['sha256']: s for s in refs})
        data_as_of = parameters.get('to') or read_json(manifest)['updated_at']
        acquisition = resolver_ruta(manifest).resolve().parent
    current, previous, kind, skipped = select_versions(rows, account, deck_id)
    current = snapshot(current, identities, sources)
    previous = snapshot(previous, identities, sources) if previous else None
    warnings = []
    for title, item in (('actual', current), ('anterior', previous)):
        if not item:
            continue
        if item['replay_check']['status'] == 'conflict':
            warnings.append(f'La lista {title} del historial difiere del encabezado del replay. Se conservan ambas; el cambio es entre declaraciones del historial.')
        elif item['replay_check']['status'] == 'not_available':
            warnings.append(f'La lista {title} no se ha contrastado con un replay disponible.')
        if len(item['observed_list_hashes']) > 1:
            warnings.append(f'Hay observaciones históricas contradictorias para la partida {title}.')
        if not item['deck']['identity_complete']:
            warnings.append(f'Hay identidades sin resolver en la lista {title}; las diferencias de IDs son provisionales.')
        if item['deck']['total_cards'] < 60:
            warnings.append(f'La lista declarada {title} tiene menos de 60 cartas; no se ha completado.')
    latest_account = max((r for r in rows if r['account_id'] == account and r.get('started_at')),
                         key=lambda r: utc(r['started_at']))
    if latest_account['your_deck_id'] != deck_id:
        warnings.append('La última partida de la cuenta usa otro mazo: se muestra la última de ROTOR.')
    frozen_manifest = None
    if acquisition:
        content = (acquisition / 'manifest.json').read_bytes()
        frozen_manifest = resolver_ruta(out) / 'entradas' / (hashlib.sha256(content).hexdigest() + '.json')
        if frozen_manifest.exists() and frozen_manifest.read_bytes() != content:
            raise ValueError('Copia de manifiesto alterada')
        if not frozen_manifest.exists():
            atomic(frozen_manifest, content)
    report = {'schema': 'duels-current-deck-v1', 'account_id': account, 'deck_id': deck_id,
              'base_batch': str(batch.resolve()), 'base_batch_id': batch.name,
              'data_as_of': data_as_of, 'refreshed': refresh or bool(manifest), 'coverage': coverage,
              'acquisition_manifest': str((acquisition / 'manifest.json').resolve()) if acquisition else None,
              'acquisition_manifest_sha256': file_hash(frozen_manifest) if frozen_manifest else None,
              'acquisition_manifest_snapshot': str(frozen_manifest.resolve()) if frozen_manifest else None,
              'http_requests': request_count, 'current': current, 'previous': previous,
              'comparison': kind, 'same_composition_games_skipped': skipped,
              'latest_account_game_id': latest_account['game_id'],
              'changes': differences(current['deck'], previous['deck']) if previous else [],
              'warnings': warnings}
    return publish_report(report, out), report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--handoff', type=resolver_ruta, default=HANDOFF)
    parser.add_argument('--out', type=resolver_ruta, default=PRIVATE / 'mazo-actual')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--actualizar', action='store_true', help='Consulta metadatos completos; reutiliza archivos y adquiere los de hasta dos partidas comparadas si faltan')
    mode.add_argument('--manifest', type=resolver_ruta, help='Usa un historial completo ya adquirido por el cliente, sin red')
    args = parser.parse_args(argv)
    try:
        directory, report = build(args.handoff, args.out, args.actualizar, args.manifest)
        print(json.dumps({'report': str(directory), 'total_cards': report['current']['deck']['total_cards'],
                          'comparison': report['comparison'], 'warnings': len(report['warnings']),
                          'http_requests': report['http_requests']}, ensure_ascii=True))
        return 0
    except (ValueError, DuelsError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except Exception:
        print('Error local al extraer el mazo; revisa formato e integridad. No se publican resultados parciales.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
