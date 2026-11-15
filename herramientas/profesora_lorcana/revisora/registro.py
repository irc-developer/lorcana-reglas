"""Registro local de posición → plan previo → elección/diagnóstico → revisiones.

No es un motor estratégico ni una barrera de permisos. Solo biblioteca estándar.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from herramientas.profesora_lorcana.contratos import (
    canonical, digest, reference, check_reference, read,
)


from herramientas.rutas_trabajo import resolver_ruta

VERSION = "0.2.1"
FIELDS = {
    "position": "position_id game_ref deck_ref boundary available_state known_information rules_evidence completeness",
    "plan": "position_id position_sha256 role skill_version preferred_line alternatives assumptions risks rules_refs confidence missing_information",
    "choice": "position_id position_sha256 observed_action evidence_ref intention",
    "diagnosis": "diagnosis_id position_id position_sha256 skill_version choice_ref assessment impact confidence facts inferences alternatives rules_refs questions_for_ivan limitations revision_of",
    "review": "review_id position_id position_sha256 independent_plan_ref diagnosis_ref verdict agreements objections alternative_lines rules_refs confidence unresolved revision_of",
}
ARRAYS = {
    "plan": "alternatives assumptions risks rules_refs missing_information",
    "diagnosis": "facts inferences alternatives rules_refs questions_for_ivan limitations",
    "review": "agreements objections alternative_lines rules_refs unresolved",
}
ASSESSMENTS = {"acierto", "defendible", "mejora_probable", "error_demostrado", "indeterminada"}
VERDICTS = {"confirmada", "corregir", "discrepancia", "no_evaluable"}
EXPOSURES = {"limitada", "contaminada", "desconocida"}
# Targeted alarms, deliberately not a semantic independence certificate.
FORBIDDEN = {
    "winner", "result", "outcome", "gameoutcome", "gameresult", "deckorder",
    "futuredraws", "nextdraw", "opponenthand", "observedaction", "diagnosis",
    "diagnosisid", "assessment", "selectedaction", "chosenaction", "replayurl",
    "replaypath", "fullreplay", "continuation", "futureevents",
}


def _json_shape(value):
    if isinstance(value, dict):
        if not all(isinstance(k, str) for k in value):
            raise ValueError("Las claves JSON deben ser strings")
        for item in value.values():
            _json_shape(item)
    elif isinstance(value, list):
        for item in value:
            _json_shape(item)
    elif value is not None and type(value) not in (str, int, float, bool):
        raise ValueError("Valor ajeno a JSON")


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _leak_guard(value, opponent=False):
    if isinstance(value, dict):
        for key, item in value.items():
            normalized = re.sub(r"[^a-z0-9]", "", key.lower())
            if normalized in FORBIDDEN:
                raise ValueError("Posible información posterior/oculta en un campo")
            # Existing projected views legitimately carry hiddenHand: unknown.
            if normalized == "hiddenhand" and item != "unknown":
                raise ValueError("Mano oculta con contenido")
            if opponent and normalized in {"hand", "deck", "deckcards"}:
                raise ValueError("Zona rival desconocida con contenido")
            _leak_guard(item, opponent or normalized in {"opponent", "rival"})
    elif isinstance(value, list):
        for item in value:
            _leak_guard(item, opponent)


def validate(artifact, kind, position=None):
    if not isinstance(artifact, dict):
        raise ValueError("Artefacto sin objeto JSON")
    _json_shape(artifact)
    canonical(artifact)  # Reject NaN passed through the Python API too.
    if artifact.get("schema") != f"lorcana-{kind}-v1":
        raise ValueError("Schema incompatible")
    missing = set(FIELDS[kind].split()) - artifact.keys()
    if missing:
        raise ValueError("Campos obligatorios ausentes: " + ", ".join(sorted(missing)))
    if not _text(artifact["position_id"]):
        raise ValueError("position_id vacío")
    if kind in ("position", "plan"):
        _leak_guard(artifact)
    if kind == "position":
        for key in ("game_ref", "deck_ref", "boundary", "available_state", "completeness"):
            if not isinstance(artifact[key], dict) or not artifact[key]:
                raise ValueError("Objeto de posición vacío o incompatible: " + key)
        for key in ("known_information", "rules_evidence"):
            if not isinstance(artifact[key], (list, dict)):
                raise ValueError("Evidencia incompatible: " + key)
    else:
        if position is None:
            raise ValueError("Falta posición para contrastar identidad/hash")
        if (artifact["position_id"] != position["position_id"]
                or artifact["position_sha256"] != digest(position)):
            raise ValueError("Identidad/hash de posición no coincide")
    for key in ARRAYS.get(kind, "").split():
        if not isinstance(artifact[key], list):
            raise ValueError("Campo debe ser lista: " + key)
    if kind in ("plan", "diagnosis") and not _text(artifact["skill_version"]):
        raise ValueError("Falta versión de skill")
    if kind in ("plan", "diagnosis", "review"):
        if not isinstance(artifact["confidence"], (str, dict)) or not artifact["confidence"]:
            raise ValueError("Falta confianza explícita")
    if kind == "plan" and (artifact["role"] != "revisora" or not artifact["preferred_line"]):
        raise ValueError("Plan sin papel revisora o línea preferida")
    if kind == "choice" and (not artifact["observed_action"] or not artifact["evidence_ref"]):
        raise ValueError("Elección sin acción o procedencia")
    if kind == "diagnosis":
        if not _text(artifact["diagnosis_id"]) or artifact["assessment"] not in ASSESSMENTS:
            raise ValueError("Identidad/evaluación del diagnóstico incompatible")
    if kind == "review":
        if not _text(artifact["review_id"]) or artifact["verdict"] not in VERDICTS:
            raise ValueError("Identidad/veredicto de revisión incompatible")


def _write_new(path, value):
    # Serialize completely before exclusive creation. Existing files stay intact.
    content = canonical(value).decode("utf-8") + "\n"
    with Path(path).open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(content)


def _receipt(kind, artifact, parent):
    payload = {"schema": "lorcana-review-receipt-v1", "stage": kind,
               "parent_sha256": parent, "artifact": artifact}
    return {**payload, "receipt_sha256": digest(payload)}


def _load_receipt(path, kind, parent):
    receipt = read(path)
    if not isinstance(receipt, dict):
        raise ValueError("Recibo sin objeto JSON")
    payload = {k: v for k, v in receipt.items() if k != "receipt_sha256"}
    if (receipt.get("schema") != "lorcana-review-receipt-v1"
            or receipt.get("stage") != kind
            or receipt.get("parent_sha256") != parent
            or receipt.get("receipt_sha256") != digest(payload)):
        raise ValueError("Recibo alterado o cadena incorrecta")
    return receipt


def open_session(position_path, session, exposure, note):
    if exposure not in EXPOSURES or not _text(note):
        raise ValueError("Declara exposición y nota de contexto")
    position = read(position_path)
    validate(position, "position")
    session = resolver_ruta(session)
    session.mkdir(parents=True, exist_ok=False)
    data = {"schema": "lorcana-review-session-v1", "helper_version": VERSION,
            "exposure_declaration": exposure, "context_note": note,
            "position_sha256": digest(position), "position": position}
    _write_new(session / "sesion.json", _receipt("position", data, None))
    return reference(position)


def _session(session):
    receipt = _load_receipt(resolver_ruta(session) / "sesion.json", "position", None)
    data = receipt["artifact"]
    if (data.get("schema") != "lorcana-review-session-v1"
            or data.get("helper_version") not in {"0.1.0", "0.2.0", VERSION}
            or data.get("exposure_declaration") not in EXPOSURES
            or not _text(data.get("context_note"))):
        raise ValueError("Sesión incompatible")
    validate(data["position"], "position")
    if data["position_sha256"] != digest(data["position"]):
        raise ValueError("Hash de posición guardada incorrecto")
    return receipt


def _plan(session):
    start = _session(session)
    receipt = _load_receipt(resolver_ruta(session) / "plan.json", "plan", start["receipt_sha256"])
    validate(receipt["artifact"], "plan", start["artifact"]["position"])
    return start, receipt


def save_plan(session, plan_path):
    start = _session(session)
    if (resolver_ruta(session) / "revelacion.json").exists():
        raise ValueError("La revelación ya ocurrió")
    plan = read(plan_path)
    validate(plan, "plan", start["artifact"]["position"])
    _write_new(resolver_ruta(session) / "plan.json", _receipt("plan", plan, start["receipt_sha256"]))
    return reference(plan)


def reveal(session, choice_path, diagnosis_path):
    # This gate deliberately precedes ALL reads of the two later artifacts.
    start, plan = _plan(session)
    choice, diagnosis = read(choice_path), read(diagnosis_path)
    position = start["artifact"]["position"]
    validate(choice, "choice", position)
    validate(diagnosis, "diagnosis", position)
    check_reference(diagnosis["choice_ref"], choice)
    if diagnosis["revision_of"] is not None:
        raise ValueError("El diagnóstico inicial no puede omitir un antecesor de la sesión")
    data = {"choice": choice, "diagnosis": diagnosis}
    _write_new(resolver_ruta(session) / "revelacion.json", _receipt("reveal", data, plan["receipt_sha256"]))
    return {"choice_ref": reference(choice), "diagnosis_ref": reference(diagnosis)}


def _revealed(session):
    start, plan = _plan(session)
    receipt = _load_receipt(resolver_ruta(session) / "revelacion.json", "reveal", plan["receipt_sha256"])
    data = receipt["artifact"]
    position = start["artifact"]["position"]
    validate(data["choice"], "choice", position)
    validate(data["diagnosis"], "diagnosis", position)
    check_reference(data["diagnosis"]["choice_ref"], data["choice"])
    return start, plan, receipt


def references(session):
    start = _session(session)
    result = {"position": reference(start["artifact"]["position"]),
              "exposure_declaration": start["artifact"]["exposure_declaration"]}
    if (resolver_ruta(session) / "plan.json").exists():
        _, plan = _plan(session)
        result["independent_plan_ref"] = reference(plan["artifact"])
    if (resolver_ruta(session) / "revelacion.json").exists():
        start, plan, original, contexts = _diagnoses(session)
        reviews = _reviews(session, start, plan, contexts)
        result["choice_ref"] = reference(original["artifact"]["choice"])
        result["diagnosis_ref"] = reference(contexts[-1]["diagnosis"])
        result["diagnosis_history"] = [reference(row["diagnosis"]) for row in contexts]
        result["reviews"] = [reference(row["artifact"]) for row in reviews]
    return result


def _review_path(session, review_id):
    if not isinstance(review_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{1,100}", review_id):
        raise ValueError("review_id requiere 1–100 letras ASCII, dígitos, _ o -")
    return resolver_ruta(session) / ("revision-" + review_id + ".json")


def _diagnoses(session):
    """Keep the original revelation and append diagnoses without recreating a plan."""
    start, plan, original = _revealed(session)
    position = start["artifact"]["position"]
    choice = original["artifact"]["choice"]
    first = original["artifact"]["diagnosis"]
    if first["revision_of"] is not None:
        raise ValueError("Diagnóstico inicial con antecesor omitido")
    contexts = [{"receipt": original, "diagnosis": first}]
    seen_ids = {first["diagnosis_id"]}
    paths = sorted(resolver_ruta(session).glob("diagnostico-*.json"))
    for index, path in enumerate(paths, 1):
        if path.name != f"diagnostico-{index:04}.json":
            raise ValueError("Secuencia de diagnósticos discontinua")
        previous = contexts[-1]
        receipt = _load_receipt(path, "diagnosis", previous["receipt"]["receipt_sha256"])
        diagnosis = receipt["artifact"]
        validate(diagnosis, "diagnosis", position)
        check_reference(diagnosis["choice_ref"], choice)
        check_reference(diagnosis["revision_of"], previous["diagnosis"])
        if diagnosis["diagnosis_id"] in seen_ids:
            raise ValueError("Identificador de diagnóstico ya conservado")
        seen_ids.add(diagnosis["diagnosis_id"])
        contexts.append({"receipt": receipt, "diagnosis": diagnosis})
    return start, plan, original, contexts


def _reviews(session, start, plan, contexts):
    """Validate reviews against the exact diagnosis receipt they were saved on."""
    parents = {row["receipt"]["receipt_sha256"]: (index, row)
               for index, row in enumerate(contexts)}
    rows = []
    for path in sorted(resolver_ruta(session).glob("revision-*.json")):
        raw = read(path)
        parent = raw.get("parent_sha256") if isinstance(raw, dict) else None
        if not isinstance(parent, str) or parent not in parents:
            raise ValueError("Revisión enlazada a una revelación/diagnóstico desconocido")
        index, context = parents[parent]
        receipt = _load_receipt(path, "review", context["receipt"]["receipt_sha256"])
        review = receipt["artifact"]
        validate(review, "review", start["artifact"]["position"])
        check_reference(review["independent_plan_ref"], plan["artifact"])
        check_reference(review["diagnosis_ref"], context["diagnosis"])
        if path != _review_path(session, review["review_id"]):
            raise ValueError("Archivo/identidad de revisión incompatibles")
        rows.append({"artifact": review, "diagnosis_index": index})
    by_hash = {digest(row["artifact"]): row for row in rows}
    for row in rows:
        cursor, seen = row, set()
        while cursor["artifact"]["revision_of"] is not None:
            current_hash = digest(cursor["artifact"])
            if current_hash in seen:
                raise ValueError("Ciclo entre revisiones")
            seen.add(current_hash)
            previous_ref = cursor["artifact"]["revision_of"]
            previous = by_hash.get(previous_ref.get("sha256")) if isinstance(previous_ref, dict) else None
            if previous is None or previous["diagnosis_index"] > cursor["diagnosis_index"]:
                raise ValueError("Antecesor de revisión ausente o posterior")
            check_reference(previous_ref, previous["artifact"])
            cursor = previous
    return rows


def save_diagnosis_successor(session, diagnosis_path):
    start, plan, original, contexts = _diagnoses(session)
    # Validate already conserved reviews too; tampering must not be bypassed by
    # adding a new diagnosis. No old receipt is modified.
    _reviews(session, start, plan, contexts)
    diagnosis = read(diagnosis_path)
    validate(diagnosis, "diagnosis", start["artifact"]["position"])
    check_reference(diagnosis["choice_ref"], original["artifact"]["choice"])
    previous = contexts[-1]
    check_reference(diagnosis["revision_of"], previous["diagnosis"])
    if diagnosis["diagnosis_id"] in {row["diagnosis"]["diagnosis_id"] for row in contexts}:
        raise ValueError("El sucesor necesita identidad nueva")
    if len(contexts) > 9999:
        raise ValueError("Límite de versiones de esta sesión")
    path = resolver_ruta(session) / f"diagnostico-{len(contexts):04}.json"
    _write_new(path, _receipt("diagnosis", diagnosis, previous["receipt"]["receipt_sha256"]))
    return reference(diagnosis)


def save_review(session, review_path):
    start, plan, original, contexts = _diagnoses(session)
    stored_reviews = _reviews(session, start, plan, contexts)
    current = contexts[-1]
    review = read(review_path)
    validate(review, "review", start["artifact"]["position"])
    check_reference(review["independent_plan_ref"], plan["artifact"])
    check_reference(review["diagnosis_ref"], current["diagnosis"])
    previous = review["revision_of"]
    if previous is not None:
        if not any(reference(row["artifact"]) == previous for row in stored_reviews):
            raise ValueError("La revisión anterior no está conservada en esta sesión")
    elif len(contexts) > 1 and stored_reviews:
        raise ValueError("La revisión del sucesor debe enlazar la revisión anterior")
    _write_new(_review_path(session, review["review_id"]),
               _receipt("review", review, current["receipt"]["receipt_sha256"]))
    return reference(review)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("abrir")
    p.add_argument("--posicion", required=True, type=resolver_ruta)
    p.add_argument("--sesion", required=True, type=resolver_ruta)
    p.add_argument("--exposicion", choices=sorted(EXPOSURES), required=True)
    p.add_argument("--nota", required=True)
    for command in ("plan", "revision", "referencias", "revelar", "diagnostico-sucesor"):
        p = commands.add_parser(command)
        p.add_argument("--sesion", required=True, type=resolver_ruta)
        if command in ("plan", "revision", "diagnostico-sucesor"):
            p.add_argument("--entrada", required=True, type=resolver_ruta)
        elif command == "revelar":
            p.add_argument("--eleccion", required=True, type=resolver_ruta)
            p.add_argument("--diagnostico", required=True, type=resolver_ruta)
    args = parser.parse_args()
    try:
        if args.command == "abrir":
            result = open_session(args.posicion, args.sesion, args.exposicion, args.nota)
        elif args.command == "plan":
            result = save_plan(args.sesion, args.entrada)
        elif args.command == "revelar":
            result = reveal(args.sesion, args.eleccion, args.diagnostico)
        elif args.command == "revision":
            result = save_review(args.sesion, args.entrada)
        elif args.command == "diagnostico-sucesor":
            result = save_diagnosis_successor(args.sesion, args.entrada)
        else:
            result = references(args.sesion)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        # Do not print paths or arbitrary values from personal artifacts.
        parser.exit(2, f"Registro rechazado ({type(exc).__name__}); revisar etapa, campos y referencias.\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
