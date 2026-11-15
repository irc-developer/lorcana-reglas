"""Pruebas contra filtraciones; no pretenden validar el motor ni reglas."""
import copy
import gzip
import json
import tempfile
import unittest
from pathlib import Path

from vista_decision import build_view, project, project_player, project_prompts


class ProjectionTests(unittest.TestCase):
    def setUp(self):
        self.card = {"id": "10-1", "fullName": "Visible", "instanceId": "c1",
                     "cost": 1, "deckOrder": ["FORBIDDEN"],
                     "specialAbilities": [{"future": "FORBIDDEN"}]}
        self.snapshot = {
            "viewingAs": 2, "currentPlayer": 2, "turnNumber": 1,
            "firstPlayer": 2, "winner": "FORBIDDEN", "matchView": {"result": "FORBIDDEN"},
            "myPlayer": {"hand": [self.card], "deckOrder": ["FORBIDDEN"], "lore": 0},
            "opponent": {"handCount": 1, "hand": [{"fullName": "FORBIDDEN"}],
                         "deckOrder": ["FORBIDDEN"], "inkwell": [
                             {"hidden": True, "exerted": False, "card": self.card}]},
            "pendingPrompts": [], "futureDraw": "FORBIDDEN",
        }

    def test_allowlist_removes_hidden_and_future_at_every_supported_depth(self):
        view = project(self.snapshot, [], {"gameId": "g"}, {})
        self.assertNotIn("FORBIDDEN", json.dumps(view))
        self.assertNotIn("hand", view["opponent"])
        self.assertNotIn("card", view["opponent"]["inkwell"][0])
        self.assertNotIn("firstPlayer", view["context"])
        self.assertEqual(view["own"]["hand"][0]["fullName"], "Visible")

    def test_prompts_are_perspective_scoped_and_unknown_payload_is_not_copied(self):
        prompts, incomplete = project_prompts([
            {"player": 1, "type": "select_card", "message": "FORBIDDEN"},
            {"player": 2, "type": "unknown", "privateCandidates": ["FORBIDDEN"]},
        ], 2)
        self.assertTrue(incomplete)
        self.assertNotIn("FORBIDDEN", json.dumps(prompts))

    def test_public_reveal_is_memory_not_exact_hidden_hand(self):
        events = [
            {"index": 0, "type": "CARD_REVEALED", "player": 1,
             "data": {"revealDestination": "hand"}, "cardRefs": [{"id": "x", "name": "Known"}]},
            {"index": 1, "type": "INITIAL_HAND", "player": 1,
             "cardRefs": [{"id": "x", "name": "FORBIDDEN"}]},
        ]
        view = project(self.snapshot, events, {"gameId": "g"}, {})
        self.assertEqual(len(view["publicObservationsEarlierThisGame"]), 1)
        self.assertEqual(view["opponent"]["hiddenHand"], "unknown")
        self.assertNotIn("FORBIDDEN", json.dumps(view))

    def test_hidden_card_never_becomes_visible_even_for_own_ink(self):
        result = project_player({"hand": [], "inkwell": [
            {"hidden": True, "card": {"fullName": "FORBIDDEN"}}]}, True)
        self.assertNotIn("FORBIDDEN", json.dumps(result))

    def test_starting_player_can_be_known_from_an_earlier_turn_start(self):
        view = project(self.snapshot, [{"type": "TURN_START", "player": 1}],
                       {"gameId": "g"}, {})
        self.assertEqual(view["context"]["firstPlayer"], 1)
        self.assertFalse(view["limits"]["firstPlayerNotProvenInPrefix"])

    def make_fixture(self, directory):
        prefix = directory / "p"
        actions = [
            {"seq": 1, "player": 2, "actionType": "CHOOSE_STARTING_PLAYER",
             "logsFromInclusive": 0, "logsToExclusive": 1},
            {"seq": 2, "player": 2, "actionType": "MULLIGAN",
             "logsFromInclusive": 1, "logsToExclusive": 2},
        ]
        events = [{"index": 0, "type": "GAME_START"},
                  {"index": 1, "type": "CARD_REVEALED", "data": {"revealDestination": "hand"},
                   "cardRefs": [{"name": "FUTURE"}]}]
        summary = {"gameId": "g", "matchId": "m", "gameNumber": 1,
                   "perspective": 2, "winner": "FUTURE", "decklist": []}
        for suffix, obj in (("-acciones.json", actions), ("-eventos.json", events), ("-resumen.json", summary)):
            Path(str(prefix) + suffix).write_text(json.dumps(obj), encoding="utf-8")
        with gzip.open(str(prefix) + "-estados.jsonl.gz", "wt", encoding="utf-8") as f:
            for seq in range(3):
                s = copy.deepcopy(self.snapshot)
                s["myPlayer"]["hand"][0]["fullName"] = "FUTURE" if seq == 2 else "BEFORE"
                f.write(json.dumps({"seq": seq, "snapshot": s}) + "\n")
        return prefix

    def test_boundary_is_state_n_minus_one_and_logs_exclude_action_n(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = self.make_fixture(Path(tmp))
            view = build_view(p, 2)
            self.assertEqual(view["boundary"]["snapshotSeq"], 1)
            self.assertEqual(view["own"]["hand"][0]["fullName"], "BEFORE")
            self.assertNotIn("FUTURE", json.dumps(view))
            self.assertEqual(view["publicObservationsEarlierThisGame"], [])
            self.assertNotIn("actionType", view["position"])

    def test_future_changes_do_not_change_view_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = self.make_fixture(Path(tmp))
            original = build_view(p, 2)
            path = Path(str(p) + "-eventos.json")
            events = json.loads(path.read_text())
            events[1]["cardRefs"][0]["name"] = "DIFFERENT FUTURE"
            path.write_text(json.dumps(events), encoding="utf-8")
            changed = build_view(p, 2)
            original.pop("inputHashes"); changed.pop("inputHashes")
            self.assertEqual(original, changed)

    def test_rejects_wrong_perspective_or_broken_boundary(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = self.make_fixture(Path(tmp))
            path = Path(str(p) + "-acciones.json")
            a = json.loads(path.read_text()); a[1]["logsFromInclusive"] = 0
            path.write_text(json.dumps(a), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Frontera"):
                build_view(p, 2)
            a[1]["logsFromInclusive"] = 1; a[1]["player"] = 1
            path.write_text(json.dumps(a), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "perspectiva"):
                build_view(p, 2)

    def test_rejects_previous_game_from_another_match_or_future(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = self.make_fixture(Path(tmp))
            with self.assertRaisesRegex(ValueError, "Contexto BO3"):
                build_view(p, 2, [p])

    def previous_fixture(self, directory):
        p = self.make_fixture(directory)
        summary_path = Path(str(p) + "-resumen.json")
        summary = json.loads(summary_path.read_text()); summary["gameNumber"] = 2
        summary_path.write_text(json.dumps(summary), encoding="utf-8")
        prior = directory / "prior"
        summary.update({"gameId": "older", "gameNumber": 1})
        Path(str(prior) + "-resumen.json").write_text(json.dumps(summary), encoding="utf-8")
        Path(str(prior) + "-eventos.json").write_text(json.dumps([
            {"index": 0, "type": "CARD_PLAYED", "player": 1,
             "cardRefs": [{"id": "known", "name": "Earlier public card"}]},
            {"index": 1, "type": "GAME_END", "message": "FORBIDDEN"},
        ]), encoding="utf-8")
        return p, prior

    def test_accepts_prior_public_memory_and_rejects_duplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            p, prior = self.previous_fixture(Path(tmp))
            view = build_view(p, 2, [prior])
            memory = view["publicObservationsFromPreviousGames"]
            self.assertEqual(len(memory), 1)
            self.assertEqual(memory[0]["gameId"], "older")
            self.assertNotIn("FORBIDDEN", json.dumps(view))
            with self.assertRaisesRegex(ValueError, "duplicado"):
                build_view(p, 2, [prior, prior])

    def test_rejects_previous_game_with_different_seat_until_roles_adapted(self):
        with tempfile.TemporaryDirectory() as tmp:
            p, prior = self.previous_fixture(Path(tmp))
            path = Path(str(prior) + "-resumen.json")
            summary = json.loads(path.read_text()); summary["perspective"] = 1
            path.write_text(json.dumps(summary), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Cambio de asiento"):
                build_view(p, 2, [prior])


if __name__ == "__main__":
    unittest.main()
