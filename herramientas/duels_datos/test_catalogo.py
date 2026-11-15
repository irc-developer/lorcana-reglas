import gzip
import json
from pathlib import Path
import tempfile
import unittest

from herramientas.duels_datos.catalogo import (
    consolidate, contract_observations, coverage, file_hash, make_batch,
    importer_observations, manual_observations, normalize_list, verified_file, verify_batch,
)
from herramientas.rutas_trabajo import ruta_trabajo


ROOT = Path(__file__).resolve().parents[2]


def observation(game='g1', scope='account1', source_id='a', **fields):
    return {'account_id': scope, 'account_scope': scope,
            'row': {'game_id': game, **fields},
            'source': {'kind': 'history_page', 'sha256': source_id, 'path': source_id},
            'source_row': 0, 'files': {}}


class CompositionTests(unittest.TestCase):
    def test_aggregation_order_and_original_are_preserved(self):
        original = [{'cardId': 'foil', 'count': 2}, {'cardId': 'base', 'count': 3}]
        alias = {'foil': 'card:identity', 'base': 'card:identity'}
        a = normalize_list(original, alias)
        b = normalize_list([{'cardId': 'base', 'count': 5}], alias)
        self.assertEqual(a['composition_sha256'], b['composition_sha256'])
        self.assertNotEqual(a['printing_sha256'], b['printing_sha256'])
        self.assertEqual(a['original'], original)
        self.assertEqual(normalize_list(original[::-1], alias)['printing_sha256'], a['printing_sha256'])

    def test_unknown_printings_are_not_guessed(self):
        a = normalize_list(['10-1'])
        b = normalize_list(['10-201'])
        self.assertFalse(a['identity_complete'])
        self.assertNotEqual(a['composition_sha256'], b['composition_sha256'])

    def test_missing_invalid_empty_and_counts(self):
        self.assertIsNone(normalize_list(None)['composition_sha256'])
        self.assertIn('decklist_invalid', normalize_list({})['issues'])
        for count in (True, 0, -1, 1.5, '4'):
            self.assertIsNone(normalize_list([{'cardId': 'x', 'count': count}])['composition_sha256'])
        self.assertIn('deck_below_60', normalize_list([])['issues'])


class ConsolidationTests(unittest.TestCase):
    def test_account_game_dedup_and_historical_changes(self):
        old = observation(updated_at='2026-10-14T00:00:00Z', result='loss', your_decklist=['a'])
        new = observation(source_id='b', updated_at='2026-10-15T00:00:00Z', result='win', your_decklist=['b'])
        third = observation(scope='other-account')
        rows, issues = consolidate([new, old, old, third])
        self.assertEqual(len(rows), 2)
        row = rows[0]
        self.assertEqual(row['result'], 'win')
        self.assertEqual(row['observation_count'], 3)
        self.assertEqual(len(row['deck_observations']), 3)
        self.assertTrue(row['conflicts'])
        self.assertTrue(any(i['issue'] == 'conflicting_historical_decklists' for i in issues))

    def test_missing_latest_list_is_not_replaced_with_old_list(self):
        rows, _ = consolidate([observation(your_decklist=['x']), observation(source_id='b', your_decklist=None)])
        self.assertIsNone(rows[0]['deck']['original'])
        self.assertEqual(rows[0]['deck_observations'][0]['original'], ['x'])

    def test_selection_does_not_equate_colors_or_deck_id_with_name(self):
        rows, _ = consolidate([
            observation(game='named', your_deck_name='ROTOR Investigaorets', your_deck_id='deck'),
            observation(game='historical', your_deck_id='deck', your_decklist=['changed']),
            observation(game='other', your_deck_colors='sapphire/steel'),
        ])
        self.assertEqual({r['game_id']: r['selection']['status'] for r in rows},
                         {'historical': 'candidate', 'named': 'safe', 'other': 'pending'})

    def test_duplicate_match_slot_and_invalid_date(self):
        rows, issues = consolidate([observation(match_id='m', match_game_number=1, updated_at='bad'),
                                   observation(game='g2', match_id='m', match_game_number=1)])
        self.assertEqual(len(rows), 2)
        self.assertTrue({'invalid_timestamp', 'duplicate_match_slot'} <= {i['issue'] for i in issues})

    def test_coverage_uses_games_and_matches_separately(self):
        rows, issues = consolidate([observation(match_id='m'), observation(game='g2', match_id='m')])
        c = coverage(rows, issues, {})
        self.assertEqual((c['games'], c['matches_with_id']), (2, 1))
        self.assertEqual(c['file_statuses']['replay'], {'not_requested': 2})

    def test_current_ui_selects_deck_object_without_asserting_historical_name(self):
        evidence = {'schema': 'duels-selection-evidence-v1', 'basis': 'current_ui_deck_object_plus_explicit_name',
                    'account_id': 'account1', 'target_name': 'ROTOR Investigaorets', 'target_deck_id': 'target'}
        rows, _ = consolidate([observation(game='target', your_deck_id='target', your_decklist=['x']),
                               observation(game='different-id', your_deck_id='other', your_decklist=['x']),
                               observation(game='different-account', scope='account2', your_deck_id='target', your_decklist=['x'])], selection_evidence=evidence)
        by_id = {r['game_id']: r for r in rows}
        self.assertEqual(by_id['target']['selection']['status'], 'safe')
        self.assertFalse(by_id['target']['selection']['historical_name_verified'])
        self.assertEqual(by_id['different-id']['selection']['status'], 'candidate')
        self.assertEqual(by_id['different-account']['selection']['status'], 'pending')


class FileTests(unittest.TestCase):
    def test_corruption_hash_identity_and_gzip(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'replay.gz'
            replay = {'format': 'duels-replay-v1', 'gameId': 'g', 'perspective': 2,
                      'baseSnapshot': {'viewingAs': 2}, 'frames': [], 'logs': []}
            path.write_bytes(gzip.compress(json.dumps(replay).encode()))
            self.assertEqual(verified_file(path, file_hash(path), game_id='g')['status'], 'verified_json')
            self.assertEqual(verified_file(path, game_id='wrong')['status'], 'game_id_mismatch')
            self.assertEqual(verified_file(path, perspective=1)['status'], 'perspective_mismatch')
            self.assertEqual(verified_file(path, 'wrong')['status'], 'hash_mismatch')
            path.write_bytes(b'\x1f\x8btruncated')
            self.assertEqual(verified_file(path)['status'], 'corrupt_or_unsupported')
            self.assertEqual(verified_file(path.parent / 'absent')['status'], 'absent_local')

    def test_contract_preserves_raw_pages_while_catalog_omits_private_urls(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            raw = {'games': [{'game_id': 'g', 'replay_url': 'https://private.invalid/secret', 'your_decklist': None}], 'next_cursor': None}
            (root / 'page.json').write_text(json.dumps(raw), encoding='utf-8')
            contract = {'schema': 'duels-datos-input-v1', 'account_id': 'account1',
                        'pages': [{'path': 'page.json', 'sha256': file_hash(root / 'page.json')}],
                        'coverage': {'enumeration_complete': True},
                        'files': [{'game_id': 'g', 'kind': 'replay', 'status': 'unavailable', 'reason': 'manifest_missing'}]}
            (root / 'contract.json').write_text(json.dumps(contract), encoding='utf-8')
            obs, sources, identities, meta = contract_observations(root / 'contract.json')
            batch = make_batch(root / 'batches', obs, sources, identities, input_coverage=meta)
            self.assertNotIn('private.invalid', (batch / 'catalogo.jsonl').read_text())
            self.assertEqual(json.loads((batch / 'cobertura.json').read_text())['file_statuses']['replay'], {'unavailable': 1})
            self.assertEqual(json.loads((root / 'page.json').read_text()), raw)

    def test_batches_are_idempotent_and_modified_batch_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            obs = [observation()]
            first = make_batch(temp, obs, [])
            second = make_batch(temp, obs, [])
            self.assertEqual(first, second)
            (first / 'catalogo.jsonl').write_bytes(b'corrupted')
            with self.assertRaisesRegex(ValueError, 'alterado'):
                make_batch(temp, obs, [])

    def test_infrastructure_adapter_checks_account_hash_chain_and_coverage(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            page = root / 'page.json'
            page.write_text(json.dumps({'games': [{'game_id': 'g', 'your_user_id': 'a'}], 'next_cursor': None}))
            manifest = {'schema_version': 1, 'source': 'https://duels.ink', 'account': {'id': 'a'},
                        'state': {'enumeration_complete': True}, 'parameters': {'limit': 250},
                        'observations': [{'endpoint': '/api/me/match-history', 'file': {'path': 'page.json', 'sha256': file_hash(page)}, 'parameters': {}}],
                        'games': {'g': {'assets': {'replay': {'status': 'unavailable', 'error': {'code': 'manifest_missing'}}}}}}
            path = root / 'manifest.json'
            path.write_text(json.dumps(manifest))
            observations, _, _, meta = importer_observations(path)
            self.assertTrue(meta['enumeration_complete_verified'])
            self.assertEqual(observations[0]['files']['replay']['status'], 'unavailable')
            manifest['observations'][0]['parameters']['cursor'] = 'unexpected-private-cursor'
            path.write_text(json.dumps(manifest))
            _, _, _, meta = importer_observations(path)
            self.assertFalse(meta['enumeration_complete_verified'])
            self.assertNotIn('unexpected-private-cursor', json.dumps(meta))
            page.write_text(json.dumps({'games': [{'game_id': 'g', 'your_user_id': 'WRONG'}], 'next_cursor': None}))
            manifest['observations'][0]['file']['sha256'] = file_hash(page)
            path.write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, 'cuenta incompatible'):
                importer_observations(path)
            page.write_bytes(b'corrupted')
            with self.assertRaisesRegex(ValueError, 'alterada'):
                importer_observations(path)

    def test_checkpoint_snapshot_remains_valid_after_client_updates(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            checkpoint = root / 'checkpoint.json'
            checkpoint.write_text('{"state":1}')
            from herramientas.duels_datos.catalogo import source
            batch = make_batch(root / 'private/lotes', [observation()], [source(checkpoint, 'infrastructure_manifest')])
            checkpoint.write_text('{"state":2}')
            self.assertEqual(verify_batch(batch), [])
            (batch / 'catalogo.jsonl').write_text('corrupted')
            self.assertIn('artifact_modified:catalogo.jsonl', verify_batch(batch))

    def test_reference_cannot_escape_acquisition_folder(self):
        from herramientas.duels_datos.catalogo import contained_ref
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, 'fuera'):
                contained_ref(Path(temp), '../outside.json')

    def test_identity_collection_keeps_conflicts_and_exact_full_names(self):
        from herramientas.duels_datos.identidades import observed_names
        from collections import defaultdict
        names = defaultdict(set)
        observed_names([{'id': '10-1', 'fullName': ' Judy - Title '},
                        {'id': '10-201', 'fullName': 'Judy - Title'},
                        {'id': '11-1', 'fullName': 'Judy - Different Title'},
                        {'id': '10-1', 'fullName': 'Conflicting Name'},
                        {'id': '10-2', 'name': 'Name without fullName'}], names)
        self.assertEqual(names['10-1'], {'Judy - Title', 'Conflicting Name'})
        self.assertEqual(names['10-201'], {'Judy - Title'})
        self.assertNotIn('10-2', names)

    def test_real_manual_fixtures(self):
        directory = ruta_trabajo('analisis/duels-2026-10-15')
        if not (directory / 'partida-01-resumen.json').exists():
            self.skipTest('Fixtures personales no distribuidos')
        obs, sources, ids = manual_observations(directory)
        self.assertEqual(len(obs), 2)
        self.assertEqual(len(sources), 2)
        self.assertTrue(all(o['derived']['status'] == 'verified_structure' for o in obs))
        for item in obs:
            self.assertIsNone(item['account_id'])
            self.assertEqual(sum(c['copies'] for c in item['row']['your_decklist']), 60)
        rows, _ = consolidate(obs, ids)
        self.assertEqual(len({r['deck']['composition_sha256'] for r in rows}), 1)
        self.assertEqual(len({r['match_id'] for r in rows}), 1)
        self.assertEqual({r['went_first'] for r in rows}, {False, True})


if __name__ == '__main__':
    unittest.main()
