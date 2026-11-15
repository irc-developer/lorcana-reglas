import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from reconstruir_lote import BoundaryError, load_extractor, reconstruct


class ReconstructionTests(unittest.TestCase):
    def fixture(self, directory):
        card = {"id": "x", "fullName": "Fixture", "instanceId": "c"}
        own = {"hand": [card], "deckOrder": ["x"] * 60, "deckCount": 60,
               "field": [], "items": [], "inkwell": [], "discard": [], "lore": 0}
        state = {"id": "game", "viewingAs": 2, "myPlayer": own,
                 "opponent": {"handCount": 7}, "status": "playing", "winner": None,
                 "victoryReason": None, "firstPlayer": 2}
        data = {"format": "duels-replay-v1", "gameId": "game", "perspective": 2,
                "baseSnapshot": state, "decklist": ["x"] * 61, "baseSnapshotLogCount": 0,
                "logs": [], "winner": 2, "victoryReason": "concede",
                "frames": [{"seq": 1, "actionType": "CONCEDE", "player": 1,
                            "turnNumber": 1, "logCountAfter": 0, "patch": [
                                {"op": "replace", "path": "/status", "value": "finished"},
                                {"op": "replace", "path": "/winner", "value": 2},
                                {"op": "replace", "path": "/victoryReason", "value": "concede"},
                            ]}]}
        path = directory / "input.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        row = {"game_id": "game", "your_player": 2, "match_id": None,
               "deck": {"printing_counts": {"x": 61}},
               "files": {"replay": {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}}}
        return data, path, row

    def test_bo1_without_matchview_and_sixty_one_cards_is_reconstructed(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            _, _, row = self.fixture(directory)
            result = reconstruct(row, directory / "out", load_extractor())
            self.assertEqual(result["status"], "reconstructed")
            self.assertEqual(result["finalCardCount"], 61)
            summary = json.loads((directory / "out/partida-01-resumen.json").read_text())
            self.assertIsNone(summary["matchId"])

    def test_list_disagreement_is_not_silently_repaired(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            _, _, row = self.fixture(directory)
            row["deck"]["printing_counts"] = {"x": 60}
            with self.assertRaisesRegex(ValueError, "Lista del replay distinta"):
                reconstruct(row, directory / "out", load_extractor())

    def test_outside_array_counter_is_identified(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            data, path, row = self.fixture(directory)
            data["baseSnapshotLogCount"] = 1
            path.write_text(json.dumps(data), encoding="utf-8")
            row["files"]["replay"]["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            with self.assertRaisesRegex(BoundaryError, "outside_array"):
                reconstruct(row, directory / "out", load_extractor())
            self.assertFalse((directory / "out").exists())

    def test_decrease_inside_array_is_prevalidated_without_publishing_derivatives(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            data, path, row = self.fixture(directory)
            data["logs"] = [{"id": str(i), "message": "", "cardRefs": []} for i in range(3)]
            data["frames"][0]["logCountAfter"] = 3
            second = dict(data["frames"][0], seq=2, logCountAfter=2)
            data["frames"].append(second)
            path.write_text(json.dumps(data), encoding="utf-8")
            row["files"]["replay"]["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            with self.assertRaises(BoundaryError) as ctx:
                reconstruct(row, directory / "out", load_extractor())
            self.assertEqual(ctx.exception.code, "decreasing_count")
            self.assertEqual(ctx.exception.details["seq"], 2)
            self.assertFalse((directory / "out").exists())
            self.assertEqual(list(directory.glob(".duels-pending-*")), [])

    def test_late_validation_failure_does_not_publish_partial_states(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            data, path, row = self.fixture(directory)
            data["winner"] = 1  # The final patch still sets winner 2.
            path.write_text(json.dumps(data), encoding="utf-8")
            row["files"]["replay"]["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            with self.assertRaisesRegex(ValueError, "Final reconstruido"):
                reconstruct(row, directory / "out", load_extractor())
            self.assertFalse((directory / "out").exists())
            self.assertEqual(list(directory.glob(".duels-pending-*")), [])


if __name__ == "__main__":
    unittest.main()
