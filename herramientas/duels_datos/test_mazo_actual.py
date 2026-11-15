import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from herramientas.duels_datos.catalogo import encode, file_hash, make_batch, normalize_list, source
from herramientas.duels_datos.mazo_actual import (
    build, differences, publish_report, relation, replay_check, select_versions, snapshot,
)


IDENTITIES = {'a': 'full-name:Card A', 'foil-a': 'full-name:Card A',
              'b': 'full-name:Card B'}


def row(game, date, cards, **fields):
    return {'game_id': game, 'started_at': date, 'ended_at': date, 'your_player': 1,
            'account_id': 'account', 'your_deck_id': 'deck',
            'deck': normalize_list(cards, IDENTITIES), 'files': {}, 'sources': [],
            **fields}


def copies(card, count=60):
    return [{'cardId': card, 'count': count}]


class VersionTests(unittest.TestCase):
    def test_skips_same_composition_and_printings_and_uses_play_time(self):
        rows = [row('new', '2026-10-15T12:00:00Z', copies('a')),
                row('foil', '2026-10-15T11:00:00Z', copies('foil-a')),
                row('same', '2026-10-15T10:00:00Z', copies('a')),
                row('different', '2026-10-14T12:00:00Z', copies('b'),
                    updated_at='2026-10-16T00:00:00Z')]
        current, previous, kind, skipped = select_versions(rows[::-1], 'account', 'deck')
        self.assertEqual((current['game_id'], previous['game_id'], kind, skipped),
                         ('new', 'different', 'composition_change', 2))

    def test_reversion_compares_with_immediately_preceding_distinct_version(self):
        rows = [row('new-a', '2026-10-15T12:00:00Z', copies('a')),
                row('recent-b', '2026-10-15T11:00:00Z', copies('b')),
                row('old-a', '2026-10-15T10:00:00Z', copies('a'))]
        self.assertEqual(select_versions(rows, 'account', 'deck')[1]['game_id'], 'recent-b')

    def test_filters_account_and_deck_object_even_for_identical_lists(self):
        rows = [row('correct', '2026-10-15T10:00:00Z', copies('a')),
                row('other-account', '2026-10-15T12:00:00Z', copies('a'), account_id='other'),
                row('other-object', '2026-10-15T11:00:00Z', copies('a'), your_deck_id='other')]
        current, previous, kind, _ = select_versions(rows, 'account', 'deck')
        self.assertEqual((current['game_id'], previous, kind), ('correct', None, 'no_previous_distinct'))

    def test_normalizes_timezones_before_ordering(self):
        rows = [row('older', '2026-10-15T13:00:00+02:00', copies('a')),
                row('newer', '2026-10-15T12:00:00Z', copies('b'))]
        self.assertEqual(select_versions(rows, 'account', 'deck')[0]['game_id'], 'newer')

    def test_missing_list_between_versions_is_not_silently_skipped(self):
        rows = [row('new', '2026-10-15T12:00:00Z', copies('a')),
                row('missing', '2026-10-15T11:00:00Z', None),
                row('old', '2026-10-15T10:00:00Z', copies('b'))]
        with self.assertRaisesRegex(ValueError, 'ausente'):
            select_versions(rows, 'account', 'deck')

    def test_ambiguous_dates_and_missing_dates_are_rejected(self):
        for date in (None, 'bad', '2026-10-15T12:00:00'):
            with self.subTest(date=date), self.assertRaises(ValueError):
                select_versions([row('g', date, copies('a'))], 'account', 'deck')
        with self.assertRaisesRegex(ValueError, 'ambiguo'):
            select_versions([row('a', '2026-10-15T12:00:00Z', copies('a')),
                             row('b', '2026-10-15T12:00:00Z', copies('b'))], 'account', 'deck')

    def test_unresolved_ids_are_provisional_and_counts_are_preserved(self):
        a, b = normalize_list(copies('unknown', 61)), normalize_list(copies('other', 60))
        self.assertEqual(relation(a, b), 'unresolved_identity')
        self.assertEqual(a['total_cards'], 61)
        self.assertEqual(normalize_list(copies('a', 59), IDENTITIES)['total_cards'], 59)

    def test_quantity_change_is_not_a_printing_change(self):
        a = normalize_list(copies('a', 61), IDENTITIES)
        b = normalize_list(copies('foil-a'), IDENTITIES)
        self.assertEqual(relation(a, b), 'composition_change')
        self.assertEqual(differences(a, b)[0]['delta'], 1)


class EvidenceTests(unittest.TestCase):
    def replay_fixture(self, directory, cards=None):
        path = Path(directory) / 'replay.json'
        path.write_text(json.dumps({'gameId': 'game', 'perspective': 1,
                                    'baseSnapshot': {'viewingAs': 1},
                                    'decklist': cards or copies('a')}), encoding='utf-8')
        game = row('game', '2026-10-15T12:00:00Z', copies('a'))
        game['files'] = {'replay': {'status': 'verified_json', 'path': str(path), 'sha256': file_hash(path)}}
        return game, path

    def test_conflicting_replay_is_preserved_without_replacing_history(self):
        with tempfile.TemporaryDirectory() as temp:
            game, _ = self.replay_fixture(temp, copies('b', 57))
            check = replay_check(game, IDENTITIES)
            self.assertEqual(check['status'], 'conflict')
            self.assertEqual(check['header_list']['total_cards'], 57)
            self.assertEqual(game['deck']['total_cards'], 60)

    def test_modified_replay_and_wrong_perspective_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            game, path = self.replay_fixture(temp)
            path.write_text('{}', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'integridad'):
                replay_check(game, IDENTITIES)
            game, _ = self.replay_fixture(temp)
            game['your_player'] = 2
            with self.assertRaisesRegex(ValueError, 'perspectiva'):
                replay_check(game, IDENTITIES)

    def test_modified_original_page_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            game, path = self.replay_fixture(temp)
            ref = {'path': str(path), 'sha256': file_hash(path)}
            game['sources'] = [{'source': ref['sha256']}]
            path.write_text('{}', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Fuente original'):
                snapshot(game, IDENTITIES, {ref['sha256']: ref})

    def test_export_is_idempotent_and_detects_modified_artifact(self):
        with tempfile.TemporaryDirectory() as temp:
            game, _ = self.replay_fixture(temp)
            current = snapshot(game, IDENTITIES, {})
            report = {'current': current, 'previous': None, 'data_as_of': 'local',
                      'warnings': [], 'same_composition_games_skipped': 0}
            out = Path(temp) / 'reports'
            first = publish_report(report, out)
            self.assertEqual(first, publish_report(report, out))
            self.assertEqual((first / 'mazo-actual.txt').read_text(), '60 Card A\n')
            (first / 'mazo-actual.txt').write_text('modified', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'alterado'):
                publish_report(report, out)


class PipelineTests(unittest.TestCase):
    def fixture(self, root):
        games = [{'game_id': 'new', 'your_user_id': 'account', 'your_deck_id': 'deck',
                  'your_player': 1, 'started_at': '2026-10-15T12:00:00Z', 'your_decklist': copies('a')},
                 {'game_id': 'old', 'your_user_id': 'account', 'your_deck_id': 'deck',
                  'your_player': 1, 'started_at': '2026-10-14T12:00:00Z', 'your_decklist': copies('b')}]
        page = root / 'page.json'
        page.write_bytes(encode({'games': games, 'next_cursor': None}))
        evidence = source(page, 'history_page')
        observations = [{'account_id': 'account', 'account_scope': 'account', 'row': r,
                         'source': evidence, 'source_row': i, 'files': {}} for i, r in enumerate(games)]
        batch = make_batch(root / 'batches', observations, [evidence], IDENTITIES,
                           selection_evidence={'schema': 'duels-selection-evidence-v1',
                                               'account_id': 'account', 'target_deck_id': 'deck',
                                               'target_name': 'ROTOR Investigaorets',
                                               'basis': 'current_ui_deck_object_plus_explicit_name'})
        handoff = root / 'handoff.json'
        handoff.write_bytes(encode({'batch': str(batch)}))
        return handoff, games

    def test_authenticated_pipeline_and_offline_manifest_reuse(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            handoff, games = self.fixture(root)

            class FakeClient:
                def __init__(self, token):
                    self.requests = 0

                def api(self, endpoint, params=None):
                    self.requests += 1
                    value = {'id': 'account'} if endpoint == '/api/me' else {'games': games, 'next_cursor': None}
                    return value, encode(value), {}

            with patch('herramientas.duels_datos.mazo_actual.Client', FakeClient), \
                    patch('herramientas.duels_datos.mazo_actual.load_token', return_value='fixture'):
                _, report = build(handoff, root / 'reports', refresh=True)
            self.assertEqual(report['http_requests'], 2)
            self.assertEqual(report['current']['game_id'], 'new')
            self.assertEqual(report['previous']['game_id'], 'old')
            frozen = Path(report['acquisition_manifest_snapshot'])
            self.assertEqual(file_hash(frozen), report['acquisition_manifest_sha256'])
            _, reused = build(handoff, root / 'reports', manifest=report['acquisition_manifest'])
            self.assertEqual(report['current']['deck'], reused['current']['deck'])
            self.assertEqual(reused['http_requests'], 0)
            # El checkpoint puede cambiar; la evidencia del informe permanece.
            manifest = Path(report['acquisition_manifest'])
            data = json.loads(manifest.read_text(encoding='utf-8'))
            data['state']['enumeration_complete'] = False
            manifest.write_bytes(encode(data))
            self.assertEqual(file_hash(frozen), report['acquisition_manifest_sha256'])
            with self.assertRaisesRegex(ValueError, 'enumeración completa'):
                build(handoff, root / 'reports', manifest=manifest)


if __name__ == '__main__':
    unittest.main()
