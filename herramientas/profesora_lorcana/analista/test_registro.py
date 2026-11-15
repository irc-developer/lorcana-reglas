"""Invariantes del registro con símbolos sintéticos, sin datos de partidas."""
import copy
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from .registro import append, balance, encode, main, read, validate, verify
from herramientas.profesora_lorcana.contratos import digest, reference, file_digest


def position():
    return {
        "schema": "lorcana-position-v1", "position_id": "synthetic-p1",
        "game_ref": {"id": "synthetic-g1", "perspective": 1, "ordinal": 1},
        "deck_ref": {"version": "synthetic-v1", "composition": {"A": 4, "B": 4}, "complete": False},
        "boundary": {"turn": 3, "previous_action": 8, "limited_view_sha256": "0" * 64},
        "available_state": {"ink": 5, "hand": ["A", "B"], "synthetic": True},
        "known_information": [], "rules_evidence": [{"ref": "axioms", "status": "synthetic"}],
        "completeness": {"missing": ["resto de lista"], "contradictions": [], "scope": "synthetic"},
    }


def line():
    return {"label": "A y B", "status": "realizable", "resources": {"ink": 5, "A": 1, "B": 1},
            "steps": [
                {"action": "A", "spend": {"ink": 2, "A": 1}, "gain": {}, "evidence_refs": ["axioms"]},
                {"action": "B", "spend": {"ink": 3, "B": 1}, "gain": {}, "evidence_refs": ["axioms"]}],
            "conditions": [], "benefit": "Dos piezas", "risk": "Sin tinta restante", "rules_refs": ["axioms"]}


def plan(receipt):
    return {"schema": "lorcana-plan-v1", "position_id": "synthetic-p1", "position_sha256": receipt["sha256"],
            "role": "analista", "skill_version": "0.2.0", "preferred_line": line(), "alternatives": [],
            "alternatives_note": "Ensayo restringido; no se afirma acción forzada real.",
            "assumptions": ["axiomas sintéticos"], "risks": ["sin reserva"], "rules_refs": ["axioms"],
            "confidence": {"level": "media", "basis": "solo ejercicio"}, "missing_information": ["resto de lista"]}


def choice(receipt):
    return {"schema": "lorcana-choice-v1", "position_id": "synthetic-p1", "position_sha256": receipt["sha256"],
            "observed_action": ["A"], "evidence_ref": "synthetic-choice", "intention": "desconocida"}


def diagnosis(position_receipt, choice_receipt):
    return {"schema": "lorcana-diagnosis-v1", "diagnosis_id": "synthetic-d1", "position_id": "synthetic-p1",
            "position_sha256": position_receipt["sha256"], "skill_version": "0.2.0", "choice_ref": choice_receipt,
            "assessment": "defendible", "impact": {"level": "medio", "reason": "Reserva recursos"},
            "confidence": {"level": "baja", "basis": "Intención pendiente"},
            "facts": ["Juega A"], "inferences": ["Quizá reserva B"], "alternatives": [line()],
            "rules_refs": ["axioms"], "questions_for_ivan": ["¿Qué función reservabas para B?"],
            "limitations": ["Ejercicio, sin reglas de cartas reales"], "revision_of": None}


class RegistroTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.session = Path(self.temp.name) / "sesion"
        self.position_ref = append(self.session, "position", position())

    def advance(self):
        append(self.session, "plan", plan(self.position_ref))
        return append(self.session, "choice", choice(self.position_ref))

    def test_full_flow_and_intention_revision(self):
        c = self.advance()
        d = diagnosis(self.position_ref, c)
        first = append(self.session, "diagnosis", d)
        old_bytes = (self.session / "diagnosis-0003.json").read_bytes()
        revised = copy.deepcopy(d)
        revised.update(diagnosis_id="synthetic-d2", assessment="acierto", revision_of=first)
        revised["facts"].append("Nueva evidencia posterior atribuida de intención; no resultado")
        append(self.session, "diagnosis", revised)
        self.assertEqual(verify(self.session)["kinds"], ["position", "plan", "choice", "diagnosis", "diagnosis"])
        self.assertEqual((self.session / "diagnosis-0003.json").read_bytes(), old_bytes)

    def test_choice_before_plan_rejected_without_new_files(self):
        before = set(self.session.iterdir())
        with self.assertRaisesRegex(ValueError, "plan previo"):
            append(self.session, "choice", choice(self.position_ref))
        self.assertEqual(set(self.session.iterdir()), before)

    def test_diagnosis_before_choice_rejected(self):
        append(self.session, "plan", plan(self.position_ref))
        with self.assertRaisesRegex(ValueError, "elección revelada"):
            append(self.session, "diagnosis", diagnosis(self.position_ref, {}))

    def test_position_hash_mismatch_rejected(self):
        p = plan({"sha256": "f" * 64})
        with self.assertRaisesRegex(ValueError, "Identidad/hash"):
            append(self.session, "plan", p)

    def test_position_id_mismatch_rejected(self):
        p = plan(self.position_ref)
        p["position_id"] = "other"
        with self.assertRaisesRegex(ValueError, "Identidad/hash"):
            append(self.session, "plan", p)

    def test_double_spend_ink_and_card_rejected(self):
        for resource in ("ink", "A"):
            with self.subTest(resource=resource):
                l = line()
                l["steps"].append({"action": "Doble gasto", "spend": {resource: 1}, "gain": {}, "evidence_refs": ["axioms"]})
                with self.assertRaisesRegex(ValueError, "no financiada"):
                    balance(l)

    def test_gain_cannot_fund_same_step_spend(self):
        l = line()
        l["resources"]["ink"] = 1
        l["steps"][0]["gain"] = {"ink": 2}
        with self.assertRaisesRegex(ValueError, "no financiada"):
            balance(l)

    def test_financed_line_retains_exact_balance(self):
        self.assertEqual(balance(line()), {"ink": 0, "A": 0, "B": 0})

    def test_conditional_line_requires_condition(self):
        l = line()
        l["status"] = "condicionada"
        with self.assertRaisesRegex(ValueError, "sin condición"):
            balance(l)

    def test_tamper_position_detected(self):
        p = read(self.session / "position.json")
        p["available_state"]["ink"] = 99
        (self.session / "position.json").write_bytes(encode(p))
        with self.assertRaisesRegex(ValueError, "alterado"):
            verify(self.session)

    def test_retroactive_plan_rejected(self):
        self.advance()
        with self.assertRaisesRegex(ValueError, "preceder"):
            append(self.session, "plan", plan(self.position_ref))

    def test_revision_requires_predecessor_and_new_id(self):
        c = self.advance()
        d = diagnosis(self.position_ref, c)
        first = append(self.session, "diagnosis", d)
        with self.assertRaisesRegex(ValueError, "anterior"):
            append(self.session, "diagnosis", d)
        d["revision_of"] = first
        with self.assertRaisesRegex(ValueError, "ID nuevo"):
            append(self.session, "diagnosis", d)

    def test_obvious_future_rejected(self):
        p = position()
        p["available_state"]["deckOrder"] = ["SECRET"]
        with self.assertRaisesRegex(ValueError, "futuro"):
            validate("position", p)

    def test_opponent_hand_rejected(self):
        p = position()
        p["available_state"]["opponent"] = {"hand": ["SECRET"]}
        with self.assertRaisesRegex(ValueError, "Mano rival"):
            validate("position", p)

    def test_wrong_choice_ref_and_path_escape_rejected(self):
        c = self.advance()
        d = diagnosis(self.position_ref, c)
        d["choice_ref"] = {"path": "../choice.json", "sha256": c["sha256"]}
        with self.assertRaisesRegex(ValueError, "otra elección"):
            append(self.session, "diagnosis", d)
        record_path = self.session / "0002-choice.json"
        record = read(record_path)
        record["artifact_receipt"]["path"] = "../choice.json"
        record_path.write_bytes(encode(record))
        with self.assertRaisesRegex(ValueError, "fuera de sesión"):
            verify(self.session)

    def test_missing_data_can_remain_indeterminate(self):
        p = plan(self.position_ref)
        p["preferred_line"] = None
        append(self.session, "plan", p)
        c = append(self.session, "choice", choice(self.position_ref))
        d = diagnosis(self.position_ref, c)
        d.update(assessment="indeterminada", alternatives=[])
        d["limitations"].append("Contradicción conservada; no hay comparación resuelta")
        append(self.session, "diagnosis", d)
        self.assertEqual(verify(self.session)["kinds"][-1], "diagnosis")

    def test_wrong_initial_balance_is_not_certified(self):
        # Límite deliberado: pasa aritmética, pero debe objetarse semánticamente.
        l = line()
        l["resources"]["ink"] = 999
        self.assertEqual(balance(l)["ink"], 994)

    def test_shared_canonical_ref_is_separate_from_bytes(self):
        stored = read(self.session / "position.json")
        self.assertEqual(self.position_ref, reference(stored))
        self.assertEqual(set(self.position_ref), {"schema", "sha256"})
        self.assertNotEqual(self.position_ref["sha256"], file_digest(self.session / "position.json"))
        compact = Path(self.temp.name) / "compact.json"
        compact.write_text(json.dumps(stored, ensure_ascii=False), encoding="utf-8")
        self.assertEqual(digest(read(compact)), self.position_ref["sha256"])
        self.assertNotEqual(file_digest(compact), file_digest(self.session / "position.json"))

    def test_strict_shared_read_rejects_duplicates_and_nonfinite(self):
        path = Path(self.temp.name) / "bad.json"
        for text in ('{"a":1,"a":2}', '{"a":NaN}', '{"a":Infinity}'):
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    read(path)

    def test_nonfinite_via_python_api_rejected_without_session(self):
        bad = position()
        bad["available_state"]["ink"] = float('nan')
        destination = Path(self.temp.name) / "bad-session"
        with self.assertRaises(ValueError):
            append(destination, "position", bad)
        self.assertFalse(destination.exists())

    def test_local_receipt_cannot_be_exchange_choice_ref(self):
        self.advance()
        record = read(self.session / "0002-choice.json")
        d = diagnosis(self.position_ref, record["artifact_receipt"])
        with self.assertRaisesRegex(ValueError, "otra elección"):
            append(self.session, "diagnosis", d)

    def test_cli_later_stage_rejected_before_reading_input(self):
        secret = Path(self.temp.name) / "later-input.json"
        def guarded_read(path):
            if Path(path) == secret:
                self.fail("La entrada posterior se abrió antes de comprobar la etapa")
            return read(path)
        for kind in ("choice", "diagnosis"):
            with self.subTest(kind=kind), patch('sys.argv', ['registro', kind, str(secret), '--session', str(self.session)]), \
                    patch('herramientas.profesora_lorcana.analista.registro.read', side_effect=guarded_read), \
                    contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as stopped:
                main()
            self.assertEqual(stopped.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
