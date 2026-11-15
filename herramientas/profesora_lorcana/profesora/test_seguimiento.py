"""Pruebas de trazabilidad y seguimiento; posiciones inventadas, sin juicio estratégico."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest

from herramientas.profesora_lorcana import contratos as c
from herramientas.profesora_lorcana.profesora import seguimiento as s


def bundle(label="ejemplo", assessment="acierto", verdict="confirmada", resources=2):
    """Cinco artefactos mínimos sintéticos; la premisa de juego no está certificada."""
    position = {"schema": "lorcana-position-v1", "position_id": f"pos-{label}",
                "game_ref": {"id": f"g-{label}", "perspective": 1, "ordinal": 1},
                "deck_ref": {"version": "sintetica-v1", "composition": []},
                "boundary": {"turn": 4, "before_action": 7,
                             "view_sha256": c.digest({"resources": resources})},
                "available_state": {"resources": resources, "action_cost": 1,
                                    "opponent": {"hiddenHand": "unknown"}},
                "known_information": [], "rules_evidence": [],
                "completeness": {"scope": "Premisas inventadas, no posición legal certificada"}}
    common = {"position_id": position["position_id"], "position_sha256": c.digest(position)}
    choice = {"schema": "lorcana-choice-v1", **common, "observed_action": "acción-A",
              "evidence_ref": "premisa-sintetica", "intention": "desconocida"}
    plan = {"schema": "lorcana-plan-v1", **common, "role": "revisora", "skill_version": "sintetica-0.2",
            "preferred_line": {"steps": ["acción-B"], "cost": 1}, "alternatives": [],
            "assumptions": ["Costes inventados"], "risks": ["Respuesta desconocida"],
            "rules_refs": [], "confidence": "baja", "missing_information": []}
    diagnosis = {"schema": "lorcana-diagnosis-v1", **common, "diagnosis_id": f"d-{label}",
                 "skill_version": "sintetica-0.2", "choice_ref": c.reference(choice),
                 "assessment": assessment, "impact": {"level": "medio", "reason": "Premisa de ejercicio"},
                 "confidence": {"level": "baja", "basis": "Fixture funcional inventada"},
                 "facts": ["Coste declarado 1"], "inferences": [], "alternatives": [], "rules_refs": [],
                 "questions_for_ivan": ["¿Qué función querías conservar?"],
                 "limitations": ["No independencia empírica ni legalidad certificada"], "revision_of": None}
    review = {"schema": "lorcana-review-v1", **common, "review_id": f"r-{label}",
              "independent_plan_ref": c.reference(plan), "diagnosis_ref": c.reference(diagnosis),
              "verdict": verdict, "agreements": [], "objections": [], "alternative_lines": [],
              "rules_refs": [], "confidence": "baja", "unresolved": [], "revision_of": None}
    return {"diagnosis": diagnosis, "review": review, "position": position,
            "choice": choice, "independent_plan": plan}


def row(occasion="n1", outcome="met", eligible=True):
    return {"occasion_id": occasion, "objective_id": "explicar-reserva", "scope": "sintetica-v1/observado",
            "eligible": eligible, "outcome": outcome, "evidence_ref": "respuesta" if outcome in {"met", "unmet"} else None,
            "reason": "Respuesta registrada" if outcome in {"met", "unmet"} else "Sin datos suficientes"}


class TracingTests(unittest.TestCase):
    def setUp(self):
        self.bundle = bundle()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def files(self, values=None):
        values = values or self.bundle
        paths = {}
        for key, value in values.items():
            path = self.root / f"{key}.json"
            path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            paths[key + "_path"] = path
        return paths

    def test_real_position_is_checked_even_when_both_declared_hashes_match(self):
        self.bundle["position"]["available_state"]["resources"] = 99
        with self.assertRaisesRegex(ValueError, "posición recibida"):
            s.check_pair(**self.bundle)

    def test_inner_view_hash_does_not_replace_complete_position_hash(self):
        for key in ("diagnosis", "review", "choice", "independent_plan"):
            self.bundle[key]["position_sha256"] = self.bundle["position"]["boundary"]["view_sha256"]
        with self.assertRaises(ValueError): s.check_pair(**self.bundle)

    def test_mixed_pair_rejected_even_for_same_position(self):
        foreign_diagnosis = deepcopy(self.bundle["diagnosis"])
        foreign_diagnosis["assessment"] = "defendible"
        self.bundle["diagnosis"] = foreign_diagnosis
        with self.assertRaises(ValueError): s.check_pair(**self.bundle)

    def test_mixed_position_rejected(self):
        self.bundle["review"] = bundle("other")["review"]
        with self.assertRaises(ValueError): s.check_pair(**self.bundle)

    def test_choice_and_independent_plan_content_are_verified(self):
        for key, field, value in (("choice", "observed_action", "otra"),
                                   ("independent_plan", "preferred_line", "otra")):
            changed = deepcopy(self.bundle)
            changed[key][field] = value
            with self.assertRaises(ValueError): s.check_pair(**changed)

    def test_refs_are_exact_shared_shape(self):
        for ref in ("d-ejemplo", {"id": "d-ejemplo", "sha256": "0" * 64},
                    {**c.reference(self.bundle["diagnosis"]), "path": "diagnosis.json"}):
            self.bundle["review"]["diagnosis_ref"] = ref
            with self.assertRaises(ValueError): s.check_pair(**self.bundle)

    def test_indentation_only_changes_bytes_receipt(self):
        paths = self.files()
        before = s.check_files(**paths)
        path = paths["diagnosis_path"]
        path.write_text(json.dumps(self.bundle["diagnosis"], ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        after = s.check_files(**paths)
        self.assertEqual(before["input_refs"], after["input_refs"])
        self.assertNotEqual(before["receipts"][0]["sha256_bytes"], after["receipts"][0]["sha256_bytes"])
        self.assertEqual(before["input_refs"], [c.reference(self.bundle["diagnosis"]), c.reference(self.bundle["review"])])

    def test_content_change_with_old_reference_is_rejected(self):
        paths = self.files()
        changed = {**self.bundle["diagnosis"], "facts": ["Hecho cambiado"]}
        paths["diagnosis_path"].write_text(json.dumps(changed), encoding="utf-8")
        with self.assertRaises(ValueError): s.check_files(**paths)

    def test_strict_reader_rejects_duplicates_and_nonfinite(self):
        paths = self.files()
        for text in ('{"schema":"lorcana-diagnosis-v1","schema":"otro"}', '{"confidence":NaN}'):
            paths["diagnosis_path"].write_text(text, encoding="utf-8")
            with self.assertRaises(ValueError): s.check_files(**paths)

    def test_statuses_preserve_abstention_disagreement_and_suspension(self):
        for assessment, verdict, expected in (("acierto", "confirmada", "utilizable"),
                ("defendible", "confirmada", "utilizable"),
                ("indeterminada", "confirmada", "incierta"),
                ("mejora_probable", "no_evaluable", "incierta"),
                ("mejora_probable", "discrepancia", "disputada"),
                ("error_demostrado", "corregir", "suspendida")):
            with self.subTest(assessment=assessment, verdict=verdict):
                self.assertEqual(s.check_pair(**bundle(assessment=assessment, verdict=verdict)), expected)

    def test_confirmation_keeps_assessment_impact_and_confidence(self):
        values = bundle(assessment="defendible")
        checked = s.check_files(**self.files(values))
        self.assertEqual(checked["assessment"], "defendible")
        self.assertEqual(checked["impact"], values["diagnosis"]["impact"])
        self.assertEqual(checked["diagnosis_confidence"], values["diagnosis"]["confidence"])

    def test_revision_requires_and_checks_real_predecessor(self):
        old = deepcopy(self.bundle)
        new = bundle(assessment="defendible")
        new["diagnosis"]["revision_of"] = c.reference(old["diagnosis"])
        new["review"]["revision_of"] = c.reference(old["review"])
        new["review"]["diagnosis_ref"] = c.reference(new["diagnosis"])
        with self.assertRaisesRegex(ValueError, "anterior"): s.check_pair(**new)
        self.assertEqual(s.check_pair(**new, previous_diagnosis=old["diagnosis"],
                                      previous_review=old["review"]), "utilizable")
        old["diagnosis"]["facts"].append("cambio")
        with self.assertRaises(ValueError):
            s.check_pair(**new, previous_diagnosis=old["diagnosis"], previous_review=old["review"])

    def test_predecessor_same_id_but_different_position_state_rejected(self):
        # revision_of sí referencia el antecesor recibido; lo inválido es su estado.
        for kind in ("diagnosis", "review"):
            with self.subTest(kind=kind):
                values = bundle()
                previous = bundle(resources=3)[kind]
                self.assertEqual(previous["position_id"], values[kind]["position_id"])
                values[kind]["revision_of"] = c.reference(previous)
                if kind == "diagnosis":
                    values["review"]["diagnosis_ref"] = c.reference(values["diagnosis"])
                with self.assertRaisesRegex(ValueError, "otro estado"):
                    s.check_pair(**values, **{f"previous_{kind}": previous})

    def test_predecessor_different_choice_rejected_without_changing_position(self):
        values = bundle()
        previous = deepcopy(values["diagnosis"])
        other_choice = {**values["choice"], "observed_action": "otra-acción"}
        previous["choice_ref"] = c.reference(other_choice)
        values["diagnosis"]["revision_of"] = c.reference(previous)
        values["review"]["diagnosis_ref"] = c.reference(values["diagnosis"])
        with self.assertRaisesRegex(ValueError, "otra elección"):
            s.check_pair(**values, previous_diagnosis=previous)

    def test_predecessor_required_fields_and_schema_checked_even_with_correct_ref(self):
        for kind, fields in (("diagnosis", s.DIAGNOSIS_FIELDS), ("review", s.REVIEW_FIELDS)):
            invalids = [{key: value for key, value in bundle()[kind].items() if key != missing}
                        for missing in fields]
            invalids.append({**bundle()[kind], "schema": "lorcana-otro-v1"})
            for previous in invalids:
                with self.subTest(kind=kind, previous_keys=tuple(previous)):
                    values = bundle()
                    values[kind]["revision_of"] = c.reference(previous)
                    if kind == "diagnosis":
                        values["review"]["diagnosis_ref"] = c.reference(values["diagnosis"])
                    with self.assertRaises(ValueError):
                        s.check_pair(**values, **{f"previous_{kind}": previous})


class FollowUpTests(unittest.TestCase):
    def test_missing_data_and_exclusion_are_not_failures(self):
        result = s.measure([row(), row("n2", "unmet"), row("n3", "missing"), row("n4", None, False)])
        self.assertEqual((result["eligible"], result["evaluable"], result["met"],
                          result["unmet"], result["missing"], result["excluded"]), (3, 2, 1, 1, 1, 1))
        self.assertEqual(s.measure([row(outcome="missing")])["unmet"], 0)

    def test_empty_sample_has_no_invented_rate(self):
        result = s.measure([])
        self.assertEqual(result["evaluable"], 0)
        self.assertNotIn("percentage", result)

    def test_duplicates_mixed_scopes_and_no_evidence_rejected(self):
        for rows in ([row(), row()], [row(), {**row("n2"), "scope": "otra-lista"}],
                     [{**row(), "evidence_ref": None}]):
            with self.assertRaises(ValueError): s.measure(rows)

    def memory(self):
        old = bundle()["diagnosis"]
        newer_same_id = {**old, "assessment": "defendible"}
        return old, [
            {"id": "conclusion", "source_refs": [c.reference(old)], "source_ids": [], "status": "active"},
            {"id": "prioridad", "source_refs": [], "source_ids": ["conclusion"], "status": "active"},
            {"id": "ejercicio", "source_refs": [], "source_ids": ["prioridad"], "status": "active"},
            {"id": "metrica", "source_refs": [], "source_ids": ["ejercicio"], "status": "active"},
            {"id": "otra-version-mismo-id", "source_refs": [c.reference(newer_same_id)], "source_ids": [], "status": "active"},
            {"id": "historica", "source_refs": [c.reference(old)], "source_ids": [], "status": "superseded"}]

    def test_correction_is_transitive_version_specific_and_nonmutating(self):
        old, memory = self.memory()
        original = deepcopy(memory)
        revised = s.mark_affected(memory, [c.reference(old)])
        self.assertTrue(all(item["status"] == "requires_review" for item in revised[:4]))
        self.assertEqual(revised[4]["status"], "active")
        self.assertEqual(revised[5]["status"], "superseded")
        self.assertEqual(memory, original)
        self.assertEqual(s.mark_affected(revised, [c.reference(old)]), revised)

    def test_byte_format_does_not_change_revision_target(self):
        old, memory = self.memory()
        reformatted = json.loads(json.dumps(old, indent=8))
        self.assertEqual(s.mark_affected(memory, [c.reference(old)]),
                         s.mark_affected(memory, [c.reference(reformatted)]))

    def test_duplicate_memory_ids_and_legacy_refs_rejected(self):
        old, memory = self.memory()
        for bad in ([memory[0], memory[0]], [{**memory[0], "source_refs": ["d-ejemplo"]}]):
            with self.assertRaises(ValueError): s.mark_affected(bad, [c.reference(old)])

    def test_external_artifact_id_cannot_replace_canonical_source_ref(self):
        old, memory = self.memory()
        memory[0]["source_refs"] = []
        memory[0]["source_ids"] = [old["diagnosis_id"]]
        with self.assertRaisesRegex(ValueError, "source_ids"):
            s.mark_affected(memory, [c.reference(old)])


if __name__ == "__main__":
    unittest.main()
