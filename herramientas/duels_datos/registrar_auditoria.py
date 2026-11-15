"""Registra auditorías de reconstrucción como suplementos inmutables, sin tocar lotes."""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path

from .catalogo import digest, encode, file_hash, normalize_list, read_json, verify_batch

import sys
# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo


def compare_replay(row, identities, source_by_hash=None):
    asset = row['files']['replay']
    ref = asset.get('decoded_json') or asset
    path = resolver_ruta(ref['path'])
    if file_hash(path) != ref['sha256']:
        raise ValueError('Replay alterado al registrar auditoría')
    raw = path.read_bytes()
    data = json.loads(gzip.decompress(raw) if raw.startswith(b'\x1f\x8b') else raw)
    if data.get('gameId') != row['game_id'] or data.get('perspective') != row['your_player']:
        raise ValueError('Identidad del replay no coincide')
    replay = normalize_list(data.get('decklist'), identities)
    history = row['deck']
    keys = sorted(set(history.get('printing_counts', {})) | set(replay.get('printing_counts', {})))
    differences = {key: {'history': history['printing_counts'].get(key, 0), 'replay_header': replay['printing_counts'].get(key, 0)}
                   for key in keys if history['printing_counts'].get(key, 0) != replay['printing_counts'].get(key, 0)}
    boundary_problems, previous = [], data.get('baseSnapshotLogCount')
    for frame in data['frames']:
        current = frame.get('logCountAfter')
        if type(previous) is not int or type(current) is not int or not previous <= current <= len(data['logs']):
            boundary_problems.append({'seq': frame.get('seq'), 'previous': previous, 'current': current, 'logs': len(data['logs'])})
        previous = current
    api_observations = []
    for observation in row.get('sources', []):
        if observation['kind'] != 'history_page':
            continue
        evidence = (source_by_hash or {})[observation['source']]
        page_path = resolver_ruta(evidence['path'])
        if file_hash(page_path) != evidence['sha256']:
            raise ValueError('Página API alterada al registrar auditoría')
        original_row = read_json(page_path)['games'][observation['row']]
        if original_row['game_id'] != row['game_id'] or original_row['your_user_id'] != row['account_id']:
            raise ValueError('Referencia API apunta a otra partida o cuenta')
        original_list = normalize_list(original_row.get('your_decklist'), identities)
        api_observations.append({'page_path': str(page_path.resolve()), 'page_sha256': evidence['sha256'],
                                 'row_index': observation['row'], 'game_id': original_row['game_id'],
                                 'your_player': original_row.get('your_player'), 'your_deck_id': original_row.get('your_deck_id'),
                                 'list': original_list,
                                 'same_printing_as_catalog': original_list['printing_sha256'] == history['printing_sha256'],
                                 'same_perspective_as_catalog_and_replay': original_row.get('your_player') == row['your_player'] == data['perspective'],
                                 'same_deck_id_as_catalog': original_row.get('your_deck_id') == row['your_deck_id']})
    return {'replay_source': {'path': str(path.resolve()), 'sha256': ref['sha256']},
            'replay_original': {key: asset[key] for key in ('path', 'sha256', 'bytes') if key in asset},
            'same_printing_list': history['printing_sha256'] == replay['printing_sha256'],
            'same_composition': history['composition_sha256'] == replay['composition_sha256'],
            'history_list': history, 'replay_header_list': replay,
            'printing_differences': differences, 'log_boundary_problems': boundary_problems,
            'api_observations': api_observations,
            'all_api_observations_match_catalog': bool(api_observations) and all(o['same_printing_as_catalog'] for o in api_observations),
            'replay_explicit_your_deck_id': data.get('your_deck_id'),
            'replay_match_id': data.get('baseSnapshot', {}).get('matchView', {}).get('id'),
            'catalog_match_id': row['match_id'],
            'resolution': 'unresolved_preserve_both_sources_no_list_replacement'}


def register(batch, audit_path, out):
    batch, audit_path, out = resolver_ruta(batch), resolver_ruta(audit_path), resolver_ruta(out)
    if verify_batch(batch):
        raise ValueError('Lote de origen alterado')
    raw_audit = audit_path.read_bytes()
    audit = json.loads(raw_audit.decode('utf-8-sig'))
    manifest = read_json(batch / 'manifiesto.json')
    if audit.get('schema') != 'duels-reconstruction-audit-v1' or audit.get('batchId') != manifest['batch_id']:
        raise ValueError('Auditoría incompatible con el lote')
    rows = {row['game_id']: row for row in map(json.loads, (batch / 'catalogo.jsonl').read_text(encoding='utf-8').splitlines())}
    games = audit['games']
    if len({game['gameId'] for game in games}) != len(games):
        raise ValueError('Auditoría con partidas duplicadas')
    safe = {key for key, row in rows.items() if row['selection']['status'] == 'safe'}
    if {game['gameId'] for game in games} != safe:
        raise ValueError('La auditoría no cubre exactamente la selección segura')
    statuses = dict(Counter(game['status'] for game in games))
    if statuses != audit.get('statuses'):
        raise ValueError('Resumen de auditoría incoherente')
    identities = read_json(batch / 'normalizacion.json')['identities']
    source_by_hash = {evidence['sha256']: evidence for evidence in read_json(batch / 'fuentes.json')}
    details = []
    for game in games:
        item = {key: game[key] for key in ('gameId', 'matchId', 'yourPlayer', 'status', 'errorType', 'error', 'sourceStatus') if key in game}
        if game['status'] == 'failed':
            item['independent_data_checks'] = compare_replay(rows[game['gameId']], identities, source_by_hash)
        details.append(item)
    report = {'schema': 'duels-data-audit-supplement-v1', 'base_batch_id': manifest['batch_id'],
              'base_batch_path': str(batch.resolve()),
              'audit_source': {'original_path': str(audit_path.resolve()), 'sha256': hashlib.sha256(raw_audit).hexdigest()},
              'statuses': statuses, 'games': details,
              'limits': ['Reconstruction statuses are supplied by the analysis audit and preserved by hash.',
                         'Independent checks compare replay headers and event boundaries, not engine execution.',
                         'verified_json acquisition coverage remains distinct from reconstruction coverage.',
                         'No disputed list is silently replaced and no missing content is fabricated.']}
    payload = encode(report)
    artifact_hashes = {'informe.json': hashlib.sha256(payload).hexdigest(),
                       'auditoria-original.json': hashlib.sha256(raw_audit).hexdigest()}
    supplement_id = digest({'base_batch_id': manifest['batch_id'], 'artifacts': artifact_hashes})
    directory = out / supplement_id
    directory.mkdir(parents=True, exist_ok=True)
    artifacts = {'informe.json': payload, 'auditoria-original.json': raw_audit,
                 'manifiesto.json': encode({'schema': 'duels-data-audit-supplement-manifest-v1',
                                           'supplement_id': supplement_id, 'artifacts': artifact_hashes})}
    for name, data in artifacts.items():
        path = directory / name
        if path.exists() and path.read_bytes() != data:
            raise ValueError('Suplemento existente alterado')
        if not path.exists():
            path.write_bytes(data)
    return directory, statuses


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch', type=resolver_ruta, required=True)
    parser.add_argument('--audit', type=resolver_ruta, required=True)
    parser.add_argument('--out', type=resolver_ruta, required=True)
    args = parser.parse_args()
    directory, statuses = register(args.batch, args.audit, args.out)
    print(json.dumps({'supplement': str(directory.resolve()), 'reconstruction': statuses}))


if __name__ == '__main__':
    main()
