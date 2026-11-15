"""Invariantes del registro, con fixtures sintéticas; sin reglas/cartas reales."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import registro as r
from herramientas.profesora_lorcana import contratos


def position():
    return {
        "schema": "lorcana-position-v1", "position_id": "synthetic-p1",
        "game_ref": {"id": "synthetic-g1", "perspective": 1, "ordinal": 1},
        "deck_ref": {"version": "synthetic-v1", "composition": []},
        "boundary": {"turn": 4, "before_action": 7, "view_sha256": "synthetic-only"},
        "available_state": {"ink_ready": 4, "opponent": {"hiddenHand": "unknown"}},
        "known_information": [], "rules_evidence": [],
        "completeness": {"scope": "synthetic protocol fixture, no rules authority"},
    }


def plan(p):
    return {
        "schema": "lorcana-plan-v1", "position_id": p["position_id"],
        "position_sha256": r.digest(p), "role": "revisora", "skill_version": r.VERSION,
        "preferred_line": {"steps": ["synthetic-A"], "cost": 4},
        "alternatives": [], "assumptions": [], "risks": [], "rules_refs": [],
        "confidence": "limitada por fixture sintética", "missing_information": [],
    }


def choice(p):
    return {
        "schema": "lorcana-choice-v1", "position_id": p["position_id"],
        "position_sha256": r.digest(p), "observed_action": "synthetic-B",
        "evidence_ref": "synthetic-manual-choice-v1", "intention": "desconocida",
    }


def diagnosis(p, c):
    return {
        "schema": "lorcana-diagnosis-v1", "diagnosis_id": "synthetic-d1",
        "position_id": p["position_id"], "position_sha256": r.digest(p),
        "skill_version": "synthetic-analyst-0.1", "choice_ref": r.reference(c),
        "assessment": "defendible", "impact": "medio", "confidence": "baja",
        "facts": [], "inferences": [], "alternatives": [], "rules_refs": [],
        "questions_for_ivan": [], "limitations": ["synthetic"], "revision_of": None,
    }


def review(p, pl, d):
    return {
        "schema": "lorcana-review-v1", "review_id": "synthetic-r1",
        "position_id": p["position_id"], "position_sha256": r.digest(p),
        "independent_plan_ref": r.reference(pl), "diagnosis_ref": r.reference(d),
        "verdict": "discrepancia", "agreements": [],
        "objections": [{"claim": "synthetic disagreement", "reason": "cost/benefit premise differs"}],
        "alternative_lines": [], "rules_refs": [], "confidence": "baja",
        "unresolved": ["rival response unknown"], "revision_of": None,
    }


class RegistryTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.session = self.root / "session"
        self.p = position()
        self.pl = plan(self.p)
        self.c = choice(self.p)
        self.d = diagnosis(self.p, self.c)
        self.rv = review(self.p, self.pl, self.d)

    def put(self, name, data):
        path = self.root / name
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        return path

    def start(self, exposure="limitada"):
        r.open_session(self.put("position.json", self.p), self.session, exposure, "synthetic test")

    def planned(self):
        self.start()
        r.save_plan(self.session, self.put("plan-in.json", self.pl))

    def revealed(self):
        self.planned()
        r.reveal(self.session, self.put("choice.json", self.c), self.put("diagnosis.json", self.d))

    def test_no_reads_of_choice_or_diagnosis_before_saved_plan(self):
        self.start()
        choice_path = self.root / "DO-NOT-READ-choice.json"
        diag_path = self.root / "DO-NOT-READ-diagnosis.json"
        actual_read = r.read
        seen = []

        def spy(path):
            seen.append(Path(path))
            return actual_read(path)

        with patch.object(r, "read", side_effect=spy):
            with self.assertRaises(FileNotFoundError):
                r.reveal(self.session, choice_path, diag_path)
        self.assertNotIn(choice_path, seen)
        self.assertNotIn(diag_path, seen)
        self.assertFalse((self.session / "revelacion.json").exists())

    def test_plan_saved_before_reveal_and_never_overwritten(self):
        self.revealed()
        old = (self.session / "plan.json").read_bytes()
        self.pl["preferred_line"]["cost"] = 3
        with self.assertRaises(ValueError):
            r.save_plan(self.session, self.put("plan-v2.json", self.pl))
        self.assertEqual(old, (self.session / "plan.json").read_bytes())

    def test_same_id_different_hash_or_different_id_are_rejected(self):
        self.planned()
        for field, value in (("position_id", "different-position"), ("position_sha256", "0" * 64)):
            with self.subTest(field=field):
                wrong = {**self.c, field: value}
                with self.assertRaises(ValueError):
                    r.reveal(self.session, self.put("wrong.json", wrong), self.put("d.json", self.d))
                self.assertFalse((self.session / "revelacion.json").exists())

    def test_changed_position_requires_a_new_hash(self):
        self.p["available_state"]["ink_ready"] = 3
        self.start()
        with self.assertRaises(ValueError):
            r.save_plan(self.session, self.put("stale-plan.json", self.pl))

    def test_wrong_choice_version_rejected(self):
        self.planned()
        self.c["intention"] = "synthetic new attributed evidence"
        with self.assertRaises(ValueError):
            r.reveal(self.session, self.put("c.json", self.c), self.put("d.json", self.d))

    def test_position_and_plan_known_leak_fields_rejected(self):
        leaks = [
            {"future_draws": ["SENTINEL"]}, {"deckOrder": ["SENTINEL"]},
            {"winner": 1}, {"observed_action": "SENTINEL"},
            {"diagnosis": {"assessment": "SENTINEL"}},
            {"opponent": {"hand": ["SENTINEL"]}},
            {"opponent": {"hiddenHand": ["SENTINEL"]}},
        ]
        for leak in leaks:
            for artifact, kind in ((self.p, "position"), (self.pl, "plan")):
                with self.subTest(leak=leak, kind=kind):
                    bad = {**copy.deepcopy(artifact), "nested": [leak]}
                    with self.assertRaises(ValueError):
                        r.validate(bad, kind, self.p if kind == "plan" else None)

    def test_receipt_tampering_rejected_before_reveal(self):
        self.planned()
        path = self.session / "plan.json"
        changed = r.read(path)
        changed["artifact"]["preferred_line"]["cost"] = 1
        path.write_text(json.dumps(changed), encoding="utf-8")
        with self.assertRaises(ValueError):
            r.reveal(self.session, self.root / "never-choice", self.root / "never-diagnosis")

    def test_disagreement_and_previous_revision_preserved(self):
        self.revealed()
        first_ref = r.save_review(self.session, self.put("r1.json", self.rv))
        first_path = self.session / "revision-synthetic-r1.json"
        original = first_path.read_bytes()
        newer = {**self.rv, "review_id": "synthetic-r2", "revision_of": first_ref,
                 "unresolved": ["new attributed explanation; follow-up pending"]}
        r.save_review(self.session, self.put("r2.json", newer))
        self.assertEqual(first_path.read_bytes(), original)
        saved = r.read(self.session / "revision-synthetic-r2.json")["artifact"]
        self.assertEqual(saved["verdict"], "discrepancia")
        self.assertEqual(saved["objections"], self.rv["objections"])
        self.assertEqual(saved["revision_of"], first_ref)
        with self.assertRaises(FileExistsError):
            r.save_review(self.session, self.put("r2.json", newer))

    def test_review_cannot_mix_plan_or_diagnosis_version(self):
        self.revealed()
        for field in ("independent_plan_ref", "diagnosis_ref"):
            with self.subTest(field=field):
                bad = {**self.rv, field: {"schema": "other", "sha256": "0" * 64}}
                with self.assertRaises(ValueError):
                    r.save_review(self.session, self.put("bad-review.json", bad))

    def test_unknown_previous_revision_rejected(self):
        self.revealed()
        self.rv["revision_of"] = {"schema": "lorcana-review-v1", "sha256": "0" * 64}
        with self.assertRaises(ValueError):
            r.save_review(self.session, self.put("revision.json", self.rv))

    def test_contamination_declaration_is_conserved_not_certified(self):
        self.start("contaminada")
        self.assertEqual(r.references(self.session)["exposure_declaration"], "contaminada")
        with self.assertRaises(FileExistsError):
            r.open_session(self.root / "position.json", self.session, "limitada", "cannot reset context")

    def test_canonical_hash_stable_and_duplicate_keys_nonfinite_rejected(self):
        self.assertEqual(r.digest({"b": 2, "a": "á"}), r.digest({"a": "á", "b": 2}))
        for bad in ('{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}'):
            path = self.root / "bad.json"
            path.write_text(bad, encoding="utf-8")
            with self.assertRaises(ValueError):
                r.read(path)
        with self.assertRaises(ValueError):
            r.digest({"x": float("nan")})

    def test_path_escape_in_review_id_rejected(self):
        self.revealed()
        self.rv["review_id"] = "../outside"
        with self.assertRaises(ValueError):
            r.save_review(self.session, self.put("revision.json", self.rv))

    def test_identity_functions_are_shared_not_reimplemented(self):
        for name in ("canonical", "digest", "reference", "read", "check_reference"):
            self.assertIs(getattr(r, name), getattr(contratos, name))

    def test_interchanged_reference_is_exact_and_whitespace_independent(self):
        self.planned()
        path = self.put("choice.json", self.c)
        path.write_text(json.dumps(self.c, indent=6, ensure_ascii=True), encoding="utf-8")
        self.assertEqual(contratos.reference(contratos.read(path)), self.d["choice_ref"])
        self.d["choice_ref"]["path"] = "unsupported-extra-field"
        with self.assertRaises(ValueError):
            r.reveal(self.session, path, self.put("diagnosis.json", self.d))

    def successor(self):
        return {**copy.deepcopy(self.d), "diagnosis_id": "synthetic-d2",
                "revision_of": r.reference(self.d), "assessment": "indeterminada"}

    def test_successor_preserves_plan_revelation_and_review_and_links_across_contexts(self):
        self.revealed()
        first_review_ref = r.save_review(self.session, self.put("r1.json", self.rv))
        conserved = {path: path.read_bytes() for path in self.session.iterdir()}
        successor = self.successor()
        ref = r.save_diagnosis_successor(self.session, self.put("d2.json", successor))
        newer = {**self.rv, "review_id": "synthetic-r2", "diagnosis_ref": ref,
                 "revision_of": first_review_ref, "verdict": "confirmada"}
        r.save_review(self.session, self.put("r2.json", newer))
        for path, original in conserved.items():
            self.assertEqual(path.read_bytes(), original)
        refs = r.references(self.session)
        self.assertEqual(refs["diagnosis_ref"], r.reference(successor))
        self.assertEqual(refs["diagnosis_history"], [r.reference(self.d), ref])
        self.assertEqual(len(refs["reviews"]), 2)
        saved = r.read(self.session / "revision-synthetic-r2.json")
        context = r.read(self.session / "diagnostico-0001.json")
        self.assertEqual(saved["parent_sha256"], context["receipt_sha256"])
        self.assertEqual(saved["artifact"]["revision_of"], first_review_ref)
        self.assertEqual(saved["artifact"]["independent_plan_ref"], r.reference(self.pl))

    def test_successor_rejects_wrong_or_skipped_ancestor(self):
        self.revealed()
        successor = self.successor()
        bad = {**successor, "revision_of": {"schema": "lorcana-diagnosis-v1", "sha256": "0" * 64}}
        with self.assertRaises(ValueError):
            r.save_diagnosis_successor(self.session, self.put("bad.json", bad))
        self.assertFalse((self.session / "diagnostico-0001.json").exists())
        r.save_diagnosis_successor(self.session, self.put("d2.json", successor))
        # A subsequent revision must point to the latest diagnosis, not its grandparent.
        bad = {**successor, "diagnosis_id": "synthetic-d3"}
        with self.assertRaises(ValueError):
            r.save_diagnosis_successor(self.session, self.put("skipped.json", bad))
        self.assertFalse((self.session / "diagnostico-0002.json").exists())

    def test_successor_rejects_different_choice_or_position(self):
        self.revealed()
        changed_choice = {**self.c, "observed_action": "synthetic-C"}
        for changes in ({"choice_ref": r.reference(changed_choice)},
                        {"position_id": "other-position"},
                        {"position_sha256": "0" * 64}):
            with self.subTest(changes=changes):
                bad = {**self.successor(), **changes}
                with self.assertRaises(ValueError):
                    r.save_diagnosis_successor(self.session, self.put("bad.json", bad))
        self.assertFalse((self.session / "diagnostico-0001.json").exists())

    def test_successor_rejects_altered_revelation_receipt(self):
        self.revealed()
        path = self.session / "revelacion.json"
        data = r.read(path)
        data["artifact"]["diagnosis"]["assessment"] = "acierto"
        path.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaises(ValueError):
            r.save_diagnosis_successor(self.session, self.put("d2.json", self.successor()))

    def test_successor_rejects_altered_previous_review(self):
        self.revealed()
        r.save_review(self.session, self.put("r1.json", self.rv))
        path = self.session / "revision-synthetic-r1.json"
        data = r.read(path)
        data["artifact"]["verdict"] = "confirmada"
        path.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaises(ValueError):
            r.save_diagnosis_successor(self.session, self.put("d2.json", self.successor()))

    def test_review_rejects_altered_successor_receipt(self):
        self.revealed()
        successor = self.successor()
        ref = r.save_diagnosis_successor(self.session, self.put("d2.json", successor))
        path = self.session / "diagnostico-0001.json"
        data = r.read(path)
        data["artifact"]["confidence"] = "altered"
        path.write_text(json.dumps(data), encoding="utf-8")
        newer = {**self.rv, "review_id": "r2", "diagnosis_ref": ref}
        with self.assertRaises(ValueError):
            r.save_review(self.session, self.put("r2.json", newer))

    def test_successor_review_must_link_previous_review_and_current_diagnosis(self):
        self.revealed()
        previous_ref = r.save_review(self.session, self.put("r1.json", self.rv))
        successor = self.successor()
        ref = r.save_diagnosis_successor(self.session, self.put("d2.json", successor))
        unlinked = {**self.rv, "review_id": "r2", "diagnosis_ref": ref}
        with self.assertRaises(ValueError):
            r.save_review(self.session, self.put("unlinked.json", unlinked))
        stale = {**self.rv, "review_id": "r2", "revision_of": previous_ref}
        with self.assertRaises(ValueError):
            r.save_review(self.session, self.put("stale.json", stale))

    def test_successor_cannot_replace_initial_revelation_or_reuse_diagnosis_id(self):
        self.planned()
        with self.assertRaises(ValueError):
            r.reveal(self.session, self.put("c.json", self.c), self.put("d2.json", self.successor()))
        r.reveal(self.session, self.put("c.json", self.c), self.put("d1.json", self.d))
        bad = {**self.successor(), "diagnosis_id": self.d["diagnosis_id"]}
        with self.assertRaises(ValueError):
            r.save_diagnosis_successor(self.session, self.put("reuse.json", bad))


if __name__ == "__main__":
    unittest.main()
