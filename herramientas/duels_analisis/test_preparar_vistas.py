import json
import unittest

from preparar_vistas import enrich_registered_list


class KnownListTests(unittest.TestCase):
    def test_only_registered_own_ids_are_named_not_the_global_map(self):
        view = {"ownRegisteredList": [{"id": "own", "copies": 4, "name": "missing"}], "limits": {}}
        enrich_registered_list(view, {"own": "full-name:Known own card", "other": "full-name:HIDDEN"}, "source-hash")
        self.assertEqual(view["ownRegisteredList"][0]["name"], "Known own card")
        self.assertEqual(view["ownRegisteredList"][0]["copies"], 4)
        self.assertNotIn("HIDDEN", json.dumps(view))
        self.assertFalse(view["limits"]["registeredListIdentityIncomplete"])

    def test_unresolved_registered_id_remains_explicit(self):
        view = {"ownRegisteredList": [{"id": "unknown", "copies": 1}], "limits": {}}
        enrich_registered_list(view, {}, "hash")
        self.assertTrue(view["limits"]["registeredListIdentityIncomplete"])


if __name__ == "__main__":
    unittest.main()
