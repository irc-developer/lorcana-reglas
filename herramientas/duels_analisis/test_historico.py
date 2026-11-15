import unittest

from historico import grouped, summarize


def row(game_id, result="win", number=1, printing="a", match="m"):
    return {"game_id": game_id, "account_scope": "account:test", "match_id": match,
            "match_game_number": number, "match_format": "bo3" if match else "bo1",
            "result": result, "started_at": f"2026-10-{number:02}T00:00:00Z",
            "selection": {"status": "safe", "scope": "deck_object_identity", "historical_name_verified": False},
            "deck": {"printing_sha256": printing, "printing_counts": {printing: 60},
                     "composition_sha256": "unverified:" + printing,
                     "identity_complete": False, "unresolved_ids": [printing]},
            "absent_fields": [], "conflicts": [], "opp_deck_colors": "Amber/Sapphire"}


class HistoryTests(unittest.TestCase):
    def test_counts_games_and_complete_matches_separately(self):
        result = summarize([row("1"), row("2", number=2), row("3", result="loss", match=None)])
        self.assertEqual(result["selected"], {"games": 3, "results": {"win": 2, "loss": 1}})
        self.assertEqual(result["matchDerivedResults"], {"win": 1})
        self.assertEqual(result["gamesWithoutMatchId"], 1)
        self.assertEqual(result["catalogIdentityCompleteRows"], 0)

    def test_color_string_is_kept_whole_and_unknown_first_player_separate(self):
        result = summarize([row("1")])
        self.assertEqual(list(result["byOpponentColorsOnly"]), ["Amber/Sapphire"])
        self.assertEqual(result["byFirstPlayer"]["unknown"]["games"], 1)

    def test_partial_or_cross_selected_match_does_not_get_winner(self):
        a, b, c = row("1"), row("2", number=2), row("3", "loss", number=3)
        c["selection"]["status"] = "pending"
        self.assertEqual(summarize([a])["matchDerivedResults"], {"undetermined": 1})
        self.assertEqual(summarize([a, b, c])["matchDerivedResults"], {"undetermined": 1})

    def test_observed_return_to_list_is_another_episode_not_new_composition(self):
        result = summarize([row("1"), row("2", number=2, printing="b"), row("3", number=3)])
        self.assertEqual(len(result["versionsByPrinting"]), 2)
        self.assertEqual([e["label"] for e in result["episodes"]], ["V01", "V02", "V01"])
        self.assertEqual(result["transitionsObserved"][0]["deltaByPrintingId"], {"a": -60, "b": 60})
        self.assertEqual(result["historicalNameVerifiedRows"], 0)

    def test_duplicate_game_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicada"):
            summarize([row("1"), row("1")])

    def test_actual_list_size_is_preserved_instead_of_forcing_sixty(self):
        a = row("1"); a["deck"]["printing_counts"] = {"a": 61}
        result = summarize([a])
        self.assertEqual(result["versionsByPrinting"][0]["totalCards"], 61)
        self.assertEqual(result["listSizes"], {61: 1})

    def test_structural_derivatives_are_counted_separately_from_pending(self):
        a, b = row("1"), row("2", number=2)
        a["derived"] = [{"status": "verified_structure"}]
        b["derived"] = [{"status": "pending"}]
        self.assertEqual(summarize([a, b])["gamesWithDerived"], 1)


if __name__ == "__main__":
    unittest.main()
