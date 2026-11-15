import json
from pathlib import Path
import tempfile
import unittest

from .catalogo import file_hash, normalize_list, source
from .registrar_auditoria import compare_replay


class AuditComparisonTests(unittest.TestCase):
    def fixture(self, root, history, replay, frames=None, identities=None):
        page = root / 'page.json'
        api_row = {'game_id': 'g', 'your_user_id': 'account', 'your_player': 2,
                   'your_deck_id': 'deck', 'your_decklist': history}
        page.write_text(json.dumps({'games': [api_row], 'next_cursor': None}), encoding='utf-8')
        page_ref = source(page, 'history_page')
        path = root / 'replay.json'
        path.write_text(json.dumps({'gameId': 'g', 'perspective': 2, 'decklist': replay,
                                   'baseSnapshotLogCount': 0, 'frames': frames or [],
                                   'logs': [{}, {}, {}, {}, {}], 'baseSnapshot': {'matchView': {'id': 'm'}}}), encoding='utf-8')
        row = {'game_id': 'g', 'account_id': 'account', 'your_player': 2,
               'match_id': 'm', 'your_deck_id': 'deck', 'deck': normalize_list(history, identities),
               'files': {'replay': {'path': str(path), 'sha256': file_hash(path)}},
               'sources': [{'kind': 'history_page', 'source': page_ref['sha256'], 'row': 0}]}
        return row, {page_ref['sha256']: page_ref}

    def test_quantity_conflict_preserves_both_originals_and_provenance(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            row, sources = self.fixture(root, ['x', 'x'], ['x'])
            original_hashes = {p: file_hash(p) for p in root.iterdir()}
            report = compare_replay(row, {'x': 'full-name:X'}, sources)
            self.assertFalse(report['same_composition'])
            self.assertEqual(report['printing_differences'], {'x': {'history': 2, 'replay_header': 1}})
            self.assertTrue(report['all_api_observations_match_catalog'])
            self.assertEqual(report['history_list']['original'], ['x', 'x'])
            self.assertEqual(report['replay_header_list']['original'], ['x'])
            self.assertTrue(report['api_observations'][0]['same_deck_id_as_catalog'])
            self.assertEqual(original_hashes, {p: file_hash(p) for p in root.iterdir()})

    def test_printing_difference_can_share_composition(self):
        with tempfile.TemporaryDirectory() as temp:
            identities = {'regular': 'full-name:X', 'foil': 'full-name:X'}
            row, sources = self.fixture(Path(temp), ['regular'], ['foil'], identities=identities)
            report = compare_replay(row, identities, sources)
            self.assertFalse(report['same_printing_list'])
            self.assertTrue(report['same_composition'])

    def test_nonmonotone_boundary_is_recorded_without_repair(self):
        with tempfile.TemporaryDirectory() as temp:
            frames = [{'seq': 1, 'logCountAfter': 3}, {'seq': 2, 'logCountAfter': 2}]
            row, sources = self.fixture(Path(temp), ['x'], ['x'], frames=frames)
            report = compare_replay(row, {}, sources)
            self.assertEqual(report['log_boundary_problems'], [{'seq': 2, 'previous': 3, 'current': 2, 'logs': 5}])

    def test_wrong_account_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            row, sources = self.fixture(Path(temp), ['x'], ['x'])
            row['account_id'] = 'other-account'
            with self.assertRaisesRegex(ValueError, 'otra partida o cuenta'):
                compare_replay(row, {}, sources)


if __name__ == '__main__':
    unittest.main()
