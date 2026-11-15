import unittest

from auditar_fronteras import audit


class BoundaryAuditTests(unittest.TestCase):
    def data(self):
        return {"baseSnapshotLogCount": 0,
                "logs": [{"id": str(i), "timestamp": i * 10, "type": "event"} for i in range(4)],
                "frames": [{"seq": 1, "logCountAfter": 3, "ts": 20},
                           {"seq": 2, "logCountAfter": 2, "ts": 25},
                           {"seq": 3, "logCountAfter": 4, "ts": 40}]}

    def test_decreasing_count_inside_array_is_distinct_from_out_of_bounds(self):
        data = self.data()
        result = audit(data, data["logs"])
        self.assertTrue(result["final_count_matches_length"])
        self.assertEqual(result["boundary_violations"], [{"seq": 2, "previous_count": 3, "count": 2,
                                                        "array_length": 4, "problems": ["decreasing_count"]}])

    def test_future_prefix_detected_without_mutation(self):
        data = self.data()
        data["frames"][0]["ts"] = 5
        result = audit(data, data["logs"])
        self.assertEqual([e["index"] for e in result["future_prefixes"][0]["events"]], [1, 2])
        self.assertEqual(data["frames"][0]["logCountAfter"], 3)
        self.assertEqual(len(data["logs"]), 4)

    def test_extra_gamelog_events_not_substituted_into_replay(self):
        data = self.data()
        extra = {"id": "extra", "timestamp": 0, "type": "INITIAL_HAND"}
        result = audit(data, [extra, *data["logs"]])
        self.assertEqual(result["gamelog"]["shared_ids"], 4)
        self.assertEqual(len(result["gamelog"]["extra_events"]), 1)
        self.assertTrue(result["gamelog"]["common_order_equal"])
        self.assertEqual(result["logs"], 4)

    def test_no_anomaly_when_monotonic_and_no_future_events(self):
        data = self.data()
        data["frames"][1]["logCountAfter"] = 3
        result = audit(data, data["logs"])
        self.assertEqual(result["boundary_violations"], [])
        self.assertEqual(result["future_prefixes"], [])


if __name__ == "__main__":
    unittest.main()
