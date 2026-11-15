"""Catálogo local inmutable de partidas, listas y archivos de Duels (sin HTTP)."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unicodedata
import zlib

import sys
# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo

VERSION = 1
TARGET = 'ROTOR Investigaorets'
FIELDS = ('game_id', 'match_id', 'match_game_number', 'match_format', 'result',
          'end_reason', 'went_first', 'your_player', 'started_at', 'ended_at',
          'updated_at', 'mode', 'queue_id', 'ranked', 'season_id', 'season_name',
          'your_deck_id', 'your_deck_name', 'your_deck_colors', 'queue_name',
          'duration_seconds', 'turns', 'your_lore', 'opp_lore', 'opp_display_name',
          'opp_guest', 'opp_is_bot', 'opp_deck_colors', 'opp_mmr_before',
          'mmr_before', 'mmr_after', 'mmr_delta', 'is_placement', 'placement_number',
          'replay_id', 'gamelog_id')


def encode(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')) + '\n').encode('utf-8')


def digest(value):
    return hashlib.sha256(encode(value)).hexdigest()


def file_hash(path):
    h = hashlib.sha256()
    with resolver_ruta(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def read_json(path):
    return json.loads(resolver_ruta(path).read_text(encoding='utf-8-sig'))


def source(path, kind):
    path = resolver_ruta(path).resolve()
    return {'path': str(path), 'sha256': file_hash(path), 'bytes': path.stat().st_size, 'kind': kind}


def contained_ref(base, relative):
    base = resolver_ruta(base)
    path = (base / relative).resolve()
    if not path.is_relative_to(base.resolve()):
        raise ValueError('Referencia fuera del directorio de adquisición')
    return path


def utc(value):
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError('Fecha no textual')
    date = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if date.tzinfo is None:
        raise ValueError('Fecha sin zona horaria')
    return date.astimezone(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')


def date_order(value):
    try:
        return utc(value) or ''
    except (TypeError, ValueError, AttributeError):
        return ''


def normalize_list(original, identities=None):
    """Nunca deduce variantes por prefijos de ID ni por parecido entre nombres."""
    if original is None:
        return {'original': None, 'printing_sha256': None, 'composition_sha256': None,
                'identity_complete': False, 'issues': ['decklist_missing']}
    identities = identities or {}
    counts = Counter()
    issues = []
    if not isinstance(original, list):
        return {'original': original, 'printing_sha256': None, 'composition_sha256': None,
                'identity_complete': False, 'issues': ['decklist_invalid']}
    for item in original:
        if isinstance(item, str):
            card, count = item, 1
        elif isinstance(item, dict):
            card = item.get('cardId', item.get('id'))
            count = item.get('count', item.get('copies'))
        else:
            card, count = None, None
        if not isinstance(card, str) or not card or type(count) is not int or count < 1:
            issues.append('deck_entry_invalid')
            continue
        counts[card] += count
    if issues:
        return {'original': original, 'printing_sha256': None, 'composition_sha256': None,
                'identity_complete': False, 'issues': sorted(set(issues))}
    strategic = Counter()
    unresolved = []
    for card, count in counts.items():
        identity = identities.get(card)
        if identity is None:
            identity = 'unresolved-id:' + card
            unresolved.append(card)
        strategic[identity] += count
    if sum(counts.values()) < 60:
        issues.append('deck_below_60')
    if unresolved:
        issues.append('printing_identity_unresolved')
    return {'original': original, 'printing_counts': dict(sorted(counts.items())),
            'composition_counts': dict(sorted(strategic.items())), 'total_cards': sum(counts.values()),
            'printing_sha256': digest(dict(sorted(counts.items()))),
            'composition_sha256': digest(dict(sorted(strategic.items()))),
            'identity_complete': not unresolved, 'unresolved_ids': sorted(unresolved), 'issues': issues}


def verified_file(path, expected=None, kind='replay', game_id=None, perspective=None):
    path = resolver_ruta(path)
    result = {'path': str(resolver_ruta(path).resolve()), 'expected_sha256': expected, 'status': 'absent_local'}
    if not resolver_ruta(path).is_file():
        return result
    result.update(sha256=file_hash(path), bytes=resolver_ruta(path).stat().st_size)
    if expected and expected != result['sha256']:
        result['status'] = 'hash_mismatch'
        return result
    try:
        with resolver_ruta(path).open('rb') as handle:
            compressed = handle.read(2) == b'\x1f\x8b'
        opener = gzip.open if compressed else open
        with opener(path, 'rt', encoding='utf-8-sig') as handle:
            data = json.load(handle)
        if kind == 'replay':
            if not isinstance(data, dict) or data.get('format') != 'duels-replay-v1':
                raise ValueError('unexpected replay format')
            if game_id and data.get('gameId') != game_id:
                result['status'] = 'game_id_mismatch'
                return result
            if perspective is not None and data.get('perspective') != perspective:
                result['status'] = 'perspective_mismatch'
                return result
            if not isinstance(data.get('baseSnapshot'), dict) or not isinstance(data.get('frames'), list) or not isinstance(data.get('logs'), list):
                raise ValueError('invalid replay structure')
            if data['baseSnapshot'].get('viewingAs') != data.get('perspective'):
                raise ValueError('inconsistent perspective')
        result['status'] = 'verified_json'
        result['validation_scope'] = 'hash_and_json_and_identity' if kind == 'replay' else 'hash_and_json_only'
    except (ValueError, OSError, UnicodeError, EOFError, zlib.error):
        result['status'] = 'corrupt_or_unsupported'
    return result


def manual_derived(summary_path, summary):
    """Audita asociación y secuencias de derivados; no vuelve a interpretar jugadas."""
    prefix = summary_path.name.removesuffix('-resumen.json')
    files, errors = {}, []
    suffixes = {'states': '-estados.jsonl.gz', 'actions': '-acciones.json',
                'events': '-eventos.json', 'final_state': '-estado-final.json', 'readable_log': '-registro.md'}
    for kind, suffix in suffixes.items():
        path = summary_path.parent / (prefix + suffix)
        if path.exists():
            files[kind] = source(path, 'manual_derived_' + kind)
        else:
            errors.append('missing_' + kind)
    if errors:
        return {'files': files, 'status': 'incomplete', 'errors': errors}
    try:
        actions = read_json(files['actions']['path'])
        events = read_json(files['events']['path'])
        final = read_json(files['final_state']['path'])
        previous_end, state_count, last = 0, 0, None
        with gzip.open(files['states']['path'], 'rt', encoding='utf-8') as handle:
            for index, line in enumerate(handle):
                last = json.loads(line)
                if last.get('seq') != index:
                    errors.append('state_sequence_gap')
                state_count += 1
        if state_count != len(actions) + 1 or len(actions) != summary.get('frames'):
            errors.append('frame_count_mismatch')
        if not last or last['snapshot'] != final:
            errors.append('final_state_mismatch')
        for index, action in enumerate(actions, 1):
            start, end = action.get('logsFromInclusive'), action.get('logsToExclusive')
            if action.get('seq') != index or start != previous_end or type(end) is not int or not start <= end <= len(events):
                errors.append('action_event_range_mismatch')
                break
            previous_end = end
        if previous_end != len(events) or len(events) != summary.get('logs'):
            errors.append('event_count_mismatch')
        if len({event.get('id') for event in events}) != len(events):
            errors.append('duplicate_event_id')
        if final.get('winner') != summary.get('winner') or final.get('viewingAs') != summary.get('perspective'):
            errors.append('summary_final_identity_mismatch')
    except (ValueError, OSError, EOFError, KeyError, TypeError):
        errors.append('corrupt_or_inconsistent_derived')
    return {'files': files, 'status': 'verified_structure' if not errors else 'inconsistent',
            'errors': sorted(set(errors)), 'validation_scope': 'hashes_sequences_ranges_final_state_not_patch_reexecution',
            'semantics': {'state_before_action_seq_n': 'states.seq=n-1',
                          'state_after_action_seq_n': 'states.seq=n',
                          'event_interval': '[logsFromInclusive,logsToExclusive), zero based',
                          'contains_hidden_future_information': True}}


def manual_observations(directory, account_id=None):
    observations, sources, identities = [], [], {}
    for path in sorted(resolver_ruta(directory).glob('partida-*-resumen.json')):
        summary = read_json(path)
        evidence = source(path, 'manual_summary')
        sources.append(evidence)
        for card in summary.get('decklist', []):
            if card.get('name') and card['name'] != '[nombre no localizado]':
                identities[card['id']] = 'full-name:' + unicodedata.normalize('NFKC', card['name']).strip()
        row = {key: None for key in FIELDS}
        row.update(game_id=summary['gameId'], match_id=summary.get('matchId'),
                   match_game_number=summary.get('gameNumber'), match_format=summary.get('formatMatch'),
                   your_player=summary.get('perspective'), end_reason=summary.get('victoryReason'),
                   started_at=summary.get('startedAtMadrid'), ended_at=summary.get('endedAtMadrid'),
                   duration_seconds=summary.get('durationSeconds'), turns=summary.get('exportedTurnCount'))
        other_player = '1' if summary.get('perspective') == 2 else '2'
        row['opp_display_name'] = summary.get('playerNames', {}).get(other_player)
        row['your_lore'] = summary.get('loreAfter', {}).get(str(summary.get('perspective')))
        row['opp_lore'] = summary.get('loreAfter', {}).get(other_player)
        if summary.get('winner') is not None and summary.get('perspective') is not None:
            row['result'] = 'win' if summary['winner'] == summary['perspective'] else 'loss'
        if summary.get('firstPlayer') is not None and summary.get('perspective') is not None:
            row['went_first'] = summary['firstPlayer'] == summary['perspective']
        row['your_decklist'] = summary.get('decklist')
        player_name = summary.get('playerNames', {}).get(str(summary.get('perspective')))
        replay = verified_file(summary['source'], summary.get('sourceSha256'), game_id=row['game_id'], perspective=row['your_player'])
        if replay['status'] == 'verified_json':
            original_data = read_json(summary['source'])
            if normalize_list(original_data.get('decklist'))['printing_sha256'] != normalize_list(row['your_decklist'])['printing_sha256']:
                replay['status'] = 'summary_decklist_mismatch'
        observations.append({'account_id': account_id, 'account_scope': account_id or 'manual-name:' + str(player_name),
                             'row': row, 'source': evidence, 'source_row': None,
                             'files': {'replay': replay},
                             'derived': manual_derived(path, summary),
                             'extraction_validation': summary.get('validation')})
    return observations, sources, identities


def contract_observations(path):
    """Adaptador explícito v1: las páginas y descargas originales permanecen fuera del catálogo."""
    contract = read_json(path)
    if contract.get('schema') != 'duels-datos-input-v1':
        raise ValueError('Contrato de entrada desconocido')
    account = contract.get('account_id')
    if not account:
        raise ValueError('Contrato sin account_id verificado')
    base = resolver_ruta(path).resolve().parent
    observations, sources = [], [source(path, 'input_contract')]
    assets = defaultdict(dict)
    for asset in contract.get('files', []):
        kind = asset['kind']
        if kind not in ('replay', 'gamelog'):
            raise ValueError('Tipo de archivo desconocido')
        clean = {k: asset.get(k) for k in ('status', 'reason') if k in asset}
        if asset.get('path'):
            clean = {**clean, **verified_file(base / asset['path'], asset.get('sha256'), kind, asset['game_id'])}
        assets[asset['game_id']][kind] = clean
    for page in contract.get('pages', []):
        page_path = base / page['path']
        evidence = source(page_path, 'history_page')
        if page.get('sha256') and evidence['sha256'] != page['sha256']:
            raise ValueError('Hash de página de historial no coincide')
        sources.append(evidence)
        data = read_json(page_path)
        for index, row in enumerate(data['games']):
            if not row.get('game_id'):
                raise ValueError('Fila de historial sin game_id')
            observations.append({'account_id': account, 'account_scope': account, 'row': row,
                                 'source': evidence, 'source_row': index, 'files': assets[row['game_id']],
                                 'fetched_at': page.get('fetched_at')})
    return observations, sources, contract.get('identities', {}), contract.get('coverage', {})


def importer_observations(path):
    """Lee directamente el manifest.json v1 de herramientas/duels/duels.py."""
    manifest_bytes = resolver_ruta(path).read_bytes()
    manifest = json.loads(manifest_bytes.decode('utf-8-sig'))
    if manifest.get('schema_version') != 1 or manifest.get('source') != 'https://duels.ink':
        raise ValueError('Manifiesto de infraestructura incompatible')
    account = manifest.get('account', {}).get('id')
    if not account:
        raise ValueError('Manifiesto sin identidad de cuenta')
    base = resolver_ruta(path).resolve().parent
    manifest_source = {'path': str(resolver_ruta(path).resolve()), 'sha256': hashlib.sha256(manifest_bytes).hexdigest(),
                       'bytes': len(manifest_bytes), 'kind': 'infrastructure_manifest'}
    observations, sources, page_meta = [], [manifest_source], []
    page_issues, expected_cursor = [], None
    for page in manifest.get('observations', []):
        if page.get('endpoint') != '/api/me/match-history':
            continue
        ref = page['file']
        page_path = contained_ref(base, ref['path'])
        evidence = source(page_path, 'history_page')
        if evidence['sha256'] != ref['sha256']:
            raise ValueError('Página original de infraestructura alterada')
        data = read_json(page_path)
        if not isinstance(data, dict) or not isinstance(data.get('games'), list) or 'next_cursor' not in data:
            raise ValueError('Página de historial incompleta')
        parameters = page.get('parameters', {})
        if parameters.get('cursor') != expected_cursor:
            # Una respuesta ya capturada antes de fallar el checkpoint puede repetirse.
            page_issues.append('cursor_chain_overlap_or_gap')
        expected_cursor = data['next_cursor']
        sources.append(evidence)
        page_meta.append({'sha256': evidence['sha256'], 'rows': len(data['games']),
                          'fetched_at': page.get('acquired_at'), 'next_cursor_present': expected_cursor is not None})
        for index, row in enumerate(data['games']):
            if not isinstance(row, dict) or not row.get('game_id') or row.get('your_user_id') != account:
                raise ValueError('Fila sin identificador o con cuenta incompatible')
            files = {}
            game = manifest.get('games', {}).get(row['game_id'], {})
            for kind in ('replay', 'gamelog'):
                asset = game.get('assets', {}).get(kind, {})
                clean = {'status': asset.get('status', 'not_requested'),
                         'infrastructure_status': asset.get('status', 'not_requested')}
                if asset.get('error'):
                    clean['reason'] = asset['error'].get('code')
                if asset.get('original'):
                    ref_asset = asset['original']
                    clean.update(verified_file(contained_ref(base, ref_asset['path']), ref_asset['sha256'], kind,
                                               row['game_id'], row.get('your_player')))
                if asset.get('json'):
                    decoded = asset['json']
                    clean['decoded_json'] = verified_file(contained_ref(base, decoded['path']), decoded['sha256'], kind,
                                                          row['game_id'], row.get('your_player'))
                files[kind] = clean
            observations.append({'account_id': account, 'account_scope': account, 'row': row,
                                 'source': evidence, 'source_row': index, 'files': files,
                                 'fetched_at': page.get('acquired_at')})
    complete = bool(manifest.get('state', {}).get('enumeration_complete'))
    completion_verified = complete and bool(page_meta) and expected_cursor is None and not page_issues
    input_coverage = {'enumeration_complete_claimed': complete,
                      'enumeration_complete_verified': completion_verified,
                      'page_chain_issues': sorted(set(page_issues)), 'pages': page_meta,
                      'parameters': {k: v for k, v in manifest.get('parameters', {}).items()
                                     if k in ('format', 'limit', 'from', 'to', 'source', 'queue')},
                      'scope': 'history_returned_for_recorded_filters_not_all_lifetime_activity'}
    return observations, sources, {}, input_coverage


def consolidate(observations, identities=None, seed_hashes=(), selection_evidence=None):
    groups = defaultdict(list)
    for observation in observations:
        groups[(observation['account_scope'], observation['row']['game_id'])].append(observation)
    catalog, issues = [], []
    for (scope, game), group in sorted(groups.items()):
        group = sorted(group, key=lambda o: (o['source']['kind'] == 'history_page',
                         date_order(o['row'].get('updated_at')), o.get('fetched_at') or '', o['source']['sha256'], o.get('source_row') or 0))
        row = {key: None for key in FIELDS}
        history_lists, files, provenance, conflicts, derived, field_sources, file_observations = [], {}, [], [], [], {}, []
        for observation in group:
            raw = observation['row']
            provenance.append({'source': observation['source']['sha256'], 'row': observation.get('source_row'),
                               'kind': observation['source']['kind'], 'updated_at': raw.get('updated_at'),
                               'absent_fields': [key for key in FIELDS if raw.get(key) is None]})
            for key in FIELDS:
                if raw.get(key) is not None:
                    if row[key] is not None and row[key] != raw[key]:
                        conflicts.append({'field': key, 'previous': row[key], 'value': raw[key], 'source': observation['source']['sha256']})
                    row[key] = raw[key]
                    field_sources[key] = {'source': observation['source']['sha256'], 'row': observation.get('source_row')}
            history_lists.append({'source': observation['source']['sha256'],
                                  **normalize_list(raw.get('your_decklist'), identities)})
            if observation.get('derived'):
                derived.append(observation['derived'])
            for kind, entry in observation.get('files', {}).items():
                file_observations.append({'kind': kind, 'source': observation['source']['sha256'], **entry})
                if files.get(kind, {}).get('status') != 'verified_json' or entry.get('status') == 'verified_json':
                    files[kind] = entry
        for key in ('started_at', 'ended_at', 'updated_at'):
            try:
                row[key] = utc(row[key])
            except (TypeError, ValueError):
                issues.append({'game_id': game, 'issue': 'invalid_timestamp', 'field': key})
                row[key] = None
        deck = history_lists[-1] if history_lists else normalize_list(None, identities)
        for field in ('went_first', 'ranked', 'opp_guest', 'opp_is_bot', 'is_placement'):
            if row[field] is not None and type(row[field]) is not bool:
                issues.append({'game_id': game, 'issue': 'invalid_boolean', 'field': field})
        if row['your_player'] is not None and (type(row['your_player']) is not int or row['your_player'] not in (1, 2)):
            issues.append({'game_id': game, 'issue': 'invalid_perspective'})
        if row['result'] is not None and row['result'] not in ('win', 'loss', 'draw', 'abandoned'):
            issues.append({'game_id': game, 'issue': 'unknown_result'})
        if row['started_at'] and row['ended_at'] and row['ended_at'] < row['started_at']:
            issues.append({'game_id': game, 'issue': 'negative_duration'})
        if row['match_game_number'] is not None and (type(row['match_game_number']) is not int or row['match_game_number'] < 1):
            issues.append({'game_id': game, 'issue': 'invalid_match_game_number'})
        for deck_issue in deck['issues']:
            issues.append({'game_id': game, 'issue': deck_issue})
        selection = {'status': 'pending', 'reasons': ['no_target_identity_evidence']}
        if row['your_deck_name'] == TARGET:
            selection = {'status': 'safe', 'reasons': ['exact_historical_deck_name']}
        elif deck.get('composition_sha256') in seed_hashes:
            selection = {'status': 'candidate', 'reasons': ['same_composition_as_manual_pilot_name_unverified']}
        elif row['your_deck_name']:
            selection = {'status': 'pending', 'reasons': ['different_recorded_name_not_automatically_excluded']}
        row.update(account_id=group[-1]['account_id'], account_scope=scope, deck=deck,
                   deck_observations=history_lists, selection=selection, sources=provenance, derived=derived,
                   observation_count=len(group), conflicts=conflicts,
                   field_sources=field_sources,
                   file_observations=file_observations,
                   absent_fields=[key for key in FIELDS if row[key] is None],
                   files={kind: files.get(kind, {'status': 'not_requested'}) for kind in ('replay', 'gamelog')})
        if len({d.get('composition_sha256') for d in history_lists if d.get('composition_sha256')}) > 1:
            issues.append({'game_id': game, 'issue': 'conflicting_historical_decklists'})
        catalog.append(row)
    # Un mismo identificador puede haber cambiado de composición o de nombre.
    named_ids = {(r['account_scope'], r['your_deck_id']) for r in catalog
                 if r['selection']['status'] == 'safe' and r['your_deck_id']}
    pilot_ids = {(r['account_scope'], r['your_deck_id']) for r in catalog
                 if r['your_deck_id'] and any(s['kind'] == 'manual_summary' for s in r['sources'])
                 and any(d.get('composition_sha256') in seed_hashes for d in r['deck_observations'])}
    for row in catalog:
        if row['selection']['status'] != 'safe' and (row['account_scope'], row['your_deck_id']) in named_ids:
            row['selection'] = {'status': 'candidate', 'reasons': ['deck_id_linked_to_named_row_historical_name_unverified']}
        elif row['selection']['status'] != 'safe' and (row['account_scope'], row['your_deck_id']) in pilot_ids:
            row['selection'] = {'status': 'candidate', 'reasons': ['deck_id_linked_to_verified_manual_pilot_nominal_name_unverified']}
        evidence = selection_evidence or {}
        if (evidence.get('schema') == 'duels-selection-evidence-v1'
                and evidence.get('basis') == 'current_ui_deck_object_plus_explicit_name'
                and evidence.get('target_name') == TARGET
                and row['account_id'] == evidence.get('account_id')
                and row['your_deck_id'] and row['your_deck_id'] == evidence.get('target_deck_id')):
            row['selection'] = {'status': 'safe', 'reasons': ['same_deck_object_as_verified_current_ui_selection'],
                                'scope': 'deck_object_identity', 'historical_name_verified': False,
                                'evidence_sha256': digest(evidence)}
    target_printings = {(r['account_scope'], r['deck']['printing_sha256']) for r in catalog
                        if r['selection']['status'] == 'safe' and r['deck']['printing_sha256']}
    target_known_compositions = {(r['account_scope'], r['deck']['composition_sha256']) for r in catalog
                                if r['selection']['status'] == 'safe' and r['deck']['identity_complete']}
    for row in catalog:
        if row['selection']['status'] != 'pending':
            continue
        if row['deck']['printing_sha256'] and (row['account_scope'], row['deck']['printing_sha256']) in target_printings:
            row['selection'] = {'status': 'candidate', 'reasons': ['same_printing_composition_as_selected_deck_object_other_id']}
        elif row['deck']['identity_complete'] and (row['account_scope'], row['deck']['composition_sha256']) in target_known_compositions:
            row['selection'] = {'status': 'candidate', 'reasons': ['same_known_composition_as_selected_deck_object_other_id']}
    slots = defaultdict(list)
    for row in catalog:
        if row['match_id'] and row['match_game_number'] is not None:
            slots[(row['account_scope'], row['match_id'], row['match_game_number'])].append(row['game_id'])
    for (_, match, number), games in slots.items():
        if len(games) > 1:
            issues.append({'issue': 'duplicate_match_slot', 'match_id': match, 'number': number, 'games': games})
    return catalog, issues


def coverage(catalog, issues, input_coverage):
    matches = {(r['account_scope'], r['match_id']) for r in catalog if r['match_id']}
    return {'games': len(catalog), 'matches_with_id': len(matches),
            'games_without_match_id': sum(r['match_id'] is None for r in catalog),
            'selection': dict(Counter(r['selection']['status'] for r in catalog)),
            'decklists_absent': sum(r['deck']['original'] is None for r in catalog),
            'distinct_compositions': len({r['deck']['composition_sha256'] for r in catalog if r['deck']['composition_sha256']}),
            'unresolved_composition_identities': sum(not r['deck']['identity_complete'] for r in catalog),
            'file_statuses': {kind: dict(Counter(r['files'][kind]['status'] for r in catalog)) for kind in ('replay', 'gamelog')},
            'selected_file_statuses': {kind: dict(Counter(r['files'][kind]['status'] for r in catalog if r['selection']['status'] in ('safe', 'candidate'))) for kind in ('replay', 'gamelog')},
            'file_statuses_by_selection': {status: {kind: dict(Counter(r['files'][kind]['status'] for r in catalog if r['selection']['status'] == status))
                                                  for kind in ('replay', 'gamelog')} for status in ('safe', 'candidate', 'pending')},
            'input_history': input_coverage, 'issues': issues,
            'limits': ['No acredita integridad semántica de estados de replay ni suficiencia docente.',
                       'Sin registro de final de paginación no acredita historial completo.',
                       'No se deduce fecha de retención de archivos ausentes.']}


def make_batch(out, observations, sources, identities=None, seeds=(), input_coverage=None, selection_evidence=None):
    out = resolver_ruta(out)
    # El checkpoint de infraestructura cambia al descargar/reanudar; conservar
    # una copia de su estado de entrada para que los lotes anteriores sigan auditables.
    frozen_sources = []
    for evidence in sources:
        if evidence['kind'] == 'infrastructure_manifest':
            content = resolver_ruta(evidence['path']).read_bytes()
            if hashlib.sha256(content).hexdigest() != evidence['sha256']:
                raise ValueError('Manifiesto cambió durante la consolidación; reintenta')
            destination = out.parent / 'entradas' / (evidence['sha256'] + '.json')
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists() and destination.read_bytes() != content:
                raise ValueError('Snapshot de entrada alterado')
            if not destination.exists():
                destination.write_bytes(content)
            evidence = {**evidence, 'path': str(destination.resolve()),
                        'original_input_path': evidence.get('original_input_path', evidence['path'])}
        frozen_sources.append(evidence)
    sources = frozen_sources
    catalog, issues = consolidate(observations, identities, seeds, selection_evidence)
    matches = defaultdict(list)
    versions = defaultdict(list)
    for row in catalog:
        if row['match_id']:
            matches[(row['account_scope'], row['match_id'])].append(row['game_id'])
        if row['deck'].get('composition_sha256'):
            versions[(row['account_scope'], row['deck']['composition_sha256'])].append(row['game_id'])
    artifacts = {
        'catalogo.jsonl': b''.join(encode(row) for row in catalog),
        'encuentros.jsonl': b''.join(encode({'account_scope': k[0], 'match_id': k[1], 'game_ids': sorted(v)}) for k, v in sorted(matches.items())),
        'composiciones.jsonl': b''.join(encode({'account_scope': k[0], 'composition_sha256': k[1], 'game_ids': sorted(v)}) for k, v in sorted(versions.items())),
        'fuentes.json': encode(sorted({s['sha256'] + s['path']: s for s in sources}.values(), key=lambda s: (s['path'], s['sha256']))),
        'cobertura.json': encode(coverage(catalog, issues, input_coverage or {})),
        'normalizacion.json': encode({'schema_version': VERSION, 'identities': identities or {}, 'seed_compositions': sorted(seeds)})}
    if selection_evidence:
        artifacts['seleccion.json'] = encode(selection_evidence)
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in artifacts.items()}
    batch_id = digest({'schema_version': VERSION, 'artifacts': hashes})
    manifest = {'schema': 'duels-datos-batch-v1', 'batch_id': batch_id, 'artifacts': hashes}
    artifacts['manifiesto.json'] = encode(manifest)
    out = resolver_ruta(out)
    out.mkdir(parents=True, exist_ok=True)
    destination = out / batch_id
    if destination.exists():
        for name, data in artifacts.items():
            if not (destination / name).exists() or (destination / name).read_bytes() != data:
                raise ValueError('Lote existente alterado; no se sobrescribe')
        return destination
    staging = resolver_ruta(tempfile.mkdtemp(prefix='.lote-', dir=out))
    try:
        for name, data in artifacts.items():
            (staging / name).write_bytes(data)
        staging.rename(destination)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return destination


def verify_batch(batch, originals=True):
    batch = resolver_ruta(batch)
    manifest = read_json(batch / 'manifiesto.json')
    failures = []
    if manifest.get('schema') != 'duels-datos-batch-v1':
        raise ValueError('Versión de lote desconocida')
    expected_id = digest({'schema_version': VERSION, 'artifacts': manifest['artifacts']})
    if expected_id != manifest.get('batch_id') or batch.name != expected_id:
        failures.append('batch_id_mismatch')
    for name, expected in manifest['artifacts'].items():
        path = batch / name
        if Path(name).name != name or not path.is_file() or file_hash(path) != expected:
            failures.append('artifact_modified:' + Path(name).name)
    if failures or not originals:
        return failures
    for evidence in read_json(batch / 'fuentes.json'):
        path = resolver_ruta(evidence['path'])
        if not path.is_file() or file_hash(path) != evidence['sha256']:
            failures.append('source_changed:' + evidence['kind'])
    for line in (batch / 'catalogo.jsonl').read_text(encoding='utf-8').splitlines():
        row = json.loads(line)
        assets = list(row['files'].items()) + [(a['kind'], a) for a in row.get('file_observations', [])]
        for kind, asset in assets:
            if asset.get('path') and asset.get('sha256'):
                path = resolver_ruta(asset['path'])
                if not path.is_file() or file_hash(path) != asset['sha256']:
                    failures.append('original_changed:' + row['game_id'] + ':' + kind)
            decoded = asset.get('decoded_json')
            if decoded and decoded.get('path') and decoded.get('sha256'):
                path = resolver_ruta(decoded['path'])
                if not path.is_file() or file_hash(path) != decoded['sha256']:
                    failures.append('decoded_changed:' + row['game_id'] + ':' + kind)
        for derived in row.get('derived', []):
            for kind, evidence in derived['files'].items():
                path = resolver_ruta(evidence['path'])
                if not path.is_file() or file_hash(path) != evidence['sha256']:
                    failures.append('derived_changed:' + row['game_id'] + ':' + kind)
    return sorted(set(failures))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    build = sub.add_parser('build')
    build.add_argument('--manual', type=resolver_ruta)
    build.add_argument('--contract', type=resolver_ruta)
    build.add_argument('--manifest', type=resolver_ruta, action='append', help='manifest.json v1 de herramientas/duels; repetible')
    build.add_argument('--account-id', help='Solo tras verificar correspondencia de la cuenta con los originales manuales')
    build.add_argument('--selection-evidence', type=resolver_ruta, help='Evidencia local de identidad del objeto de mazo seleccionado por Iván')
    build.add_argument('--observed-identities', type=resolver_ruta, help='Mapa versionado de fullName observados por identidades.py')
    build.add_argument('--link-manual-account', action='store_true', help='Vincula solo tras contrastar partida, perspectiva y lista exacta con API')
    build.add_argument('--out', type=resolver_ruta, required=True)
    query = sub.add_parser('query')
    query.add_argument('batch', type=resolver_ruta)
    query.add_argument('--selection', choices=('safe', 'candidate', 'pending'))
    query.add_argument('--game-id')
    query.add_argument('--match-id')
    query.add_argument('--full', action='store_true')
    verify = sub.add_parser('verify')
    verify.add_argument('batch', type=resolver_ruta)
    args = parser.parse_args()
    if args.command == 'verify':
        failures = verify_batch(args.batch)
        print(json.dumps({'valid': not failures, 'failures': failures}))
        if failures:
            raise SystemExit(1)
        return
    if args.command == 'query':
        if verify_batch(args.batch, originals=False):
            raise ValueError('Lote alterado; ejecuta verify')
        for line in (args.batch / 'catalogo.jsonl').read_text(encoding='utf-8').splitlines():
            row = json.loads(line)
            if args.selection and row['selection']['status'] != args.selection:
                continue
            if args.game_id and row['game_id'] != args.game_id:
                continue
            if args.match_id and row['match_id'] != args.match_id:
                continue
            print(encode(row if args.full else {k: row[k] for k in ('game_id', 'match_id', 'match_game_number', 'result', 'started_at', 'selection')}).decode().strip())
        return
    observations, sources, identities, seeds, input_coverage = [], [], {}, [], {}
    if args.manual:
        obs, src, ids = manual_observations(args.manual, args.account_id)
        observations += obs
        sources += src
        identities.update(ids)
    if args.contract:
        obs, src, ids, input_coverage = contract_observations(args.contract)
        observations += obs
        sources += src
        identities.update(ids)
    manifest_coverage = []
    for manifest_path in args.manifest or []:
        obs, src, ids, current_coverage = importer_observations(manifest_path)
        observations += obs
        sources += src
        identities.update(ids)
        manifest_coverage.append({'manifest_sha256': file_hash(manifest_path), **current_coverage})
    if manifest_coverage:
        input_coverage = {'acquisitions': manifest_coverage}
    if args.link_manual_account:
        for observation in observations:
            if observation['source']['kind'] != 'manual_summary':
                continue
            manual_row = observation['row']
            matches = [o for o in observations if o['source']['kind'] == 'history_page'
                       and o['row']['game_id'] == manual_row['game_id']
                       and o['row'].get('your_player') == manual_row['your_player']
                       and normalize_list(o['row'].get('your_decklist'))['printing_sha256'] is not None
                       and normalize_list(o['row'].get('your_decklist'))['printing_sha256'] == normalize_list(manual_row.get('your_decklist'))['printing_sha256']]
            accounts = {o['account_id'] for o in matches}
            if len(accounts) != 1:
                raise ValueError('No se puede vincular manual con una única cuenta mediante partida, perspectiva y lista')
            account = next(iter(accounts))
            if args.account_id and args.account_id != account:
                raise ValueError('La cuenta manual indicada contradice la evidencia API')
            observation['account_id'], observation['account_scope'] = account, account
    if args.observed_identities:
        mapping = read_json(args.observed_identities)
        if mapping.get('schema') != 'duels-observed-identities-v1':
            raise ValueError('Mapa de identidades incompatible')
        for card, identity in mapping['identities'].items():
            if card in identities and identities[card] != identity:
                raise ValueError('Nombre completo observado contradice el piloto')
            identities[card] = identity
        for card in mapping.get('conflicts', {}):
            identities.pop(card, None)
        sources.append(source(args.observed_identities, 'observed_identity_map'))
        for evidence in mapping.get('sources', []):
            current = source(evidence['path'], 'replay_card_identity_evidence')
            if current['sha256'] != evidence['sha256']:
                raise ValueError('Replay de identidades alterado')
            sources.append(current)
    for observation in observations:
        if (observation['source']['kind'] == 'manual_summary'
                and observation['files']['replay']['status'] == 'verified_json'
                and observation['derived']['status'] == 'verified_structure'):
            value = normalize_list(observation['row'].get('your_decklist'), identities).get('composition_sha256')
            if value:
                seeds.append(value)
    if not observations:
        parser.error('No hay observaciones; facilita --manual o --contract')
    selection_evidence = None
    if args.selection_evidence:
        selection_evidence = read_json(args.selection_evidence)
        if selection_evidence.get('schema') != 'duels-selection-evidence-v1':
            raise ValueError('Evidencia de selección incompatible')
        sources.append(source(args.selection_evidence, 'selection_evidence'))
        for ref in selection_evidence.get('evidence_files', []):
            current = source(ref['path'], 'selection_external_evidence')
            if current['sha256'] != ref['sha256']:
                raise ValueError('Archivo de evidencia de selección alterado')
            sources.append(current)
    batch = make_batch(args.out, observations, sources, identities, sorted(set(seeds)), input_coverage, selection_evidence)
    report = read_json(batch / 'cobertura.json')
    brief = {key: report[key] for key in ('games', 'matches_with_id', 'selection', 'decklists_absent', 'file_statuses')}
    brief['issues_count'] = len(report['issues'])
    print(json.dumps({'batch': str(batch.resolve()), 'coverage': brief}, ensure_ascii=False))


if __name__ == '__main__':
    main()
