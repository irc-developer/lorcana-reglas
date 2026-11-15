from pathlib import Path
import hashlib
import tempfile
import unittest
from unittest.mock import patch

from herramientas.profesora_lorcana import coordinar_piloto as coordinator
from herramientas.profesora_lorcana.contratos import digest, file_digest, read, reference
from herramientas.profesora_lorcana.analista import registro as analyst
from herramientas.profesora_lorcana.analista.test_registro import position, plan, choice
from herramientas.profesora_lorcana.revisora import registro as reviewer


class CoordinationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.p = position()
        self.position_path = self.root / 'position.json'
        self.position_path.write_bytes(analyst.encode(self.p))
        self.a, self.r = self.root / 'analyst', self.root / 'reviewer'
        pref = analyst.append(self.a, 'position', self.p)
        self.ap = plan(pref)
        analyst.append(self.a, 'plan', self.ap)
        reviewer.open_session(self.position_path, self.r, 'limitada', 'Synthetic protocol fixture')
        self.rp = {**self.ap, 'role': 'revisora'}
        self.rplan_path = self.root / 'review-plan.json'
        self.rplan_path.write_bytes(analyst.encode(self.rp))

    def test_seal_matches_both_preserved_plans_and_is_not_overwritten(self):
        reviewer.save_plan(self.r, self.rplan_path)
        _, result = coordinator.seal(self.position_path, self.a, self.r, self.root / 'out')
        self.assertEqual(result['analyst_plan_ref'], reference(self.ap))
        self.assertEqual(result['reviewer_plan_ref'], reference(self.rp))
        with self.assertRaises(FileExistsError):
            coordinator.seal(self.position_path, self.a, self.r, self.root / 'out')

    def test_missing_second_plan_does_not_open_reserved_map(self):
        with patch.object(coordinator, 'read', wraps=read) as reads:
            with self.assertRaisesRegex(ValueError, 'revisora debe tener su plan'):
                coordinator.release(self.root, self.position_path, self.a, self.r, self.root / 'out')
        self.assertFalse(any('RESERVADO' in str(call) for call in reads.call_args_list))

    def test_revealed_analyst_stage_is_rejected_before_export(self):
        reviewer.save_plan(self.r, self.rplan_path)
        analyst.append(self.a, 'choice', choice(reference(self.p)))
        with self.assertRaisesRegex(ValueError, 'solo posición y plan'):
            coordinator.seal(self.position_path, self.a, self.r, self.root / 'out')

    def test_mixed_position_is_rejected(self):
        reviewer.save_plan(self.r, self.rplan_path)
        self.position_path.write_bytes(analyst.encode({**self.p, 'position_id': 'different'}))
        with self.assertRaises(ValueError):
            coordinator.seal(self.position_path, self.a, self.r, self.root / 'out')

    def source(self):
        prefix = self.root / 'source'
        path = Path(str(prefix) + '-eventos.json')
        event = {'index': 0, 'type': 'CARD_QUEST', 'player': 1,
                 'cardRefs': [{'id': 'A', 'name': 'Synthetic A'}, {'id': 'future', 'name': 'Hidden future'}],
                 'data': {'cardId': 'A', 'loreGained': 2, 'newLoreTotal': 20},
                 'winner': 1, 'deckOrder': ['future']}
        path.write_bytes(analyst.encode([event]))
        return {'prefix': str(prefix), 'source_input_hashes': {path.name: file_digest(path)},
                'observed_action_record': {'seq': 1, 'actionType': 'QUEST',
                                           'logsFromInclusive': 0, 'logsToExclusive': 1}}

    def test_only_choice_is_exported_and_source_change_is_detected(self):
        source = self.source()
        selected, evidence = coordinator.extract_choice(self.p, source)
        self.assertEqual(selected['observed_action']['cards_recorded'], [{'id': 'A', 'name': 'Synthetic A'}])
        self.assertNotIn('loreGained', str(selected) + str(evidence))
        self.assertNotIn('Hidden future', str(selected) + str(evidence))
        self.assertNotIn('winner', str(selected) + str(evidence))
        path = Path(source['prefix'] + '-eventos.json')
        path.write_text('[]', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'cambiaron'):
            coordinator.extract_choice(self.p, source)

    def test_release_seals_first_and_exports_linked_limited_choice(self):
        reviewer.save_plan(self.r, self.rplan_path)
        source = {**self.source(), 'position_id': self.p['position_id']}
        (self.root / 'RESERVADO-COORDINACION.json').write_bytes(
            analyst.encode({'positions': [source]}))
        result = coordinator.release(self.root, self.position_path, self.a, self.r, self.root / 'out')
        selected = read(self.root / 'out/eleccion.json')
        evidence = read(self.root / 'out/evidencia-eleccion.json')
        self.assertEqual(result['choice_ref'], reference(selected))
        self.assertEqual(selected['evidence_ref'], reference(evidence))
        self.assertEqual(selected['position_sha256'], digest(self.p))
        self.assertTrue((self.root / 'out/SELLO-PLANES.json').is_file())

    def test_mulligan_excludes_redraws_even_if_refs_are_interleaved(self):
        source = self.source()
        source['observed_action_record']['actionType'] = 'MULLIGAN'
        event = {'index': 0, 'type': 'MULLIGAN', 'player': 1,
                 'message': 'You mulliganed 2 cards: {card:1}, {card:3}. Drew: {card:0}, {card:2}',
                 'data': {'mulliganCount': 2},
                 'cardRefs': [{'id': 'future-x', 'name': 'Future X'}, {'id': 'a', 'name': 'A'},
                              {'id': 'future-y', 'name': 'Future Y'}, {'id': 'b', 'name': 'B'}]}
        path = Path(source['prefix'] + '-eventos.json')
        path.write_bytes(analyst.encode([event]))
        source['source_input_hashes'][path.name] = file_digest(path)
        selected, evidence = coordinator.extract_choice(self.p, source)
        self.assertEqual(selected['observed_action']['cards_recorded'], [{'id': 'a', 'name': 'A'}, {'id': 'b', 'name': 'B'}])
        self.assertNotIn('future-', str(selected) + str(evidence))
        event['message'] = 'Unknown template with the same returned/drawn refs'
        path.write_bytes(analyst.encode([event]))
        source['source_input_hashes'][path.name] = file_digest(path)
        with self.assertRaisesRegex(ValueError, 'Plantilla de mulligan desconocida'):
            coordinator.extract_choice(self.p, source)

    def pending_source(self, *, actor=1, source_instance='instance-a', extra_patch=False):
        source = self.source()
        source['observed_action_record'] = {'seq': 1, 'actionType': 'PLAY_CARD', 'player': 1,
                                           'turnNumber': 6, 'timestamp': 123,
                                           'logsFromInclusive': 0, 'logsToExclusive': 0}
        self.p['available_state'] = {'own': {'hand': [
            {'instanceId': 'instance-a', 'id': 'A', 'fullName': 'Synthetic A'}]}}
        prompt = {'type': 'boolean', 'message': 'bodyguardExertChoice', 'player': actor,
                  'sourceCardInstanceId': source_instance}
        operations = [{'op': 'add', 'path': '/pendingPrompts/0', 'value': prompt}]
        if extra_patch:
            operations.append({'op': 'add', 'path': '/myPlayer/hand/-', 'value': 'Future draw'})
        frame = {'seq': 1, 'actionType': 'PLAY_CARD', 'player': 1, 'turnNumber': 6,
                 'ts': 123, 'logCountAfter': 0, 'patch': operations}
        raw = analyst.encode({'format': 'duels-replay-v1', 'frames': [frame,
            {'seq': 2, 'answer': True, 'future': 'Hidden future'}], 'winner': 2})
        replay_path = self.root / 'replay.json'
        replay_path.write_bytes(raw)
        summary_path = Path(source['prefix'] + '-resumen.json')
        summary_path.write_bytes(analyst.encode({'source': str(replay_path),
            'sourceSha256': hashlib.sha256(raw).hexdigest(),
            'decodedSha256': hashlib.sha256(raw).hexdigest()}))
        source['source_input_hashes'][summary_path.name] = file_digest(summary_path)
        return source

    def test_pending_play_excludes_answer_and_does_not_claim_resolution(self):
        selected, evidence = coordinator.extract_choice(self.p, self.pending_source())
        self.assertEqual(selected['observed_action']['cards_recorded'], [{'id': 'A', 'name': 'Synthetic A'}])
        self.assertFalse(selected['observed_action']['resolution_observed'])
        self.assertNotIn('Hidden future', str(selected) + str(evidence))
        self.assertNotIn('winner', str(selected) + str(evidence))
        self.assertNotIn('answer', str(selected) + str(evidence))

    def test_pending_play_rejects_foreign_prompt_unknown_card_and_effect_patch(self):
        for kwargs in ({'actor': 2}, {'source_instance': 'unknown'}, {'extra_patch': True}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                coordinator.extract_choice(self.p, self.pending_source(**kwargs))

    def test_pending_play_rejects_changed_summary_or_replay(self):
        source = self.pending_source()
        Path(source['prefix'] + '-resumen.json').write_text('{}', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Resumen original'):
            coordinator.extract_choice(self.p, source)
        source = self.pending_source()
        (self.root / 'replay.json').write_text('{}', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Replay original'):
            coordinator.extract_choice(self.p, source)


if __name__ == '__main__':
    unittest.main()
