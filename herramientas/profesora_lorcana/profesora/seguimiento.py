"""Comprobaciones locales de enseñanza; no evalúa estrategia ni escribe memoria."""

import argparse
from copy import deepcopy
import json
from pathlib import Path
import re
import sys

# Admite CLI por ruta y uso como módulo desde la raíz, sin instalar un paquete.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from herramientas.profesora_lorcana import contratos

VERSION = "0.2.1"


DIAGNOSIS_FIELDS = set("diagnosis_id position_id position_sha256 skill_version choice_ref assessment impact confidence facts inferences alternatives rules_refs questions_for_ivan limitations revision_of".split())
REVIEW_FIELDS = set("review_id position_id position_sha256 independent_plan_ref diagnosis_ref verdict agreements objections alternative_lines rules_refs confidence unresolved revision_of".split())
ASSESSMENTS = {"acierto", "defendible", "mejora_probable", "error_demostrado", "indeterminada"}
VERDICTS = {"confirmada", "corregir", "discrepancia", "no_evaluable"}
POSITION_FIELDS = set("position_id game_ref deck_ref boundary available_state known_information rules_evidence completeness".split())
CHOICE_FIELDS = set("position_id position_sha256 observed_action evidence_ref intention".split())
PLAN_FIELDS = set("position_id position_sha256 role skill_version preferred_line alternatives assumptions risks rules_refs confidence missing_information".split())


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def check_ref_shape(ref):
    require(isinstance(ref, dict) and set(ref) == {"schema", "sha256"},
            "Referencia requiere exactamente schema y sha256 canónico")
    require(nonempty(ref["schema"]) and isinstance(ref["sha256"], str) and
            re.fullmatch(r"[a-f0-9]{64}", ref["sha256"]), "Referencia inválida")


def artifact(record, kind, fields):
    require(isinstance(record, dict), f"{kind}: se esperaba objeto")
    require(record.get("schema") == f"lorcana-{kind}-v1", f"{kind}: schema incompatible")
    require(fields <= record.keys(), f"{kind}: faltan {sorted(fields - record.keys())}")
    require(nonempty(record["position_id"]), f"{kind}: position_id vacío")
    contratos.canonical(record)  # También rechaza no finitos recibidos por la API Python.


def check_revision(record, previous, kind):
    ref = record["revision_of"]
    if ref is None:
        require(previous is None, f"{kind}: antecesor suministrado sin revision_of")
        return
    check_ref_shape(ref)
    require(previous is not None, f"{kind}: falta artefacto anterior para verificar revision_of")
    artifact(previous, kind, DIAGNOSIS_FIELDS if kind == "diagnosis" else REVIEW_FIELDS)
    contratos.check_reference(ref, previous)
    require(previous["position_id"] == record["position_id"], f"{kind}: revisión de otra posición")
    require(previous["position_sha256"] == record["position_sha256"],
            f"{kind}: antecesor de otro estado de posición")
    if kind == "diagnosis":
        check_ref_shape(previous["choice_ref"])
        require(previous["choice_ref"] == record["choice_ref"],
                "diagnosis: antecesor de otra elección observada")
    require(contratos.reference(record) != ref, f"{kind}: autorreferencia")


def check_pair(diagnosis, review, position, choice, independent_plan, *,
               previous_diagnosis=None, previous_review=None):
    """Contrasta referencias con los cinco artefactos reales, sin certificar estrategia."""
    for record, kind, fields in ((position, "position", POSITION_FIELDS),
                                  (choice, "choice", CHOICE_FIELDS),
                                  (independent_plan, "plan", PLAN_FIELDS),
                                  (diagnosis, "diagnosis", DIAGNOSIS_FIELDS),
                                  (review, "review", REVIEW_FIELDS)):
        artifact(record, kind, fields)
        if kind != "position":
            require(record["position_id"] == position["position_id"], f"{kind}: otra posición")
            require(record["position_sha256"] == contratos.digest(position),
                    f"{kind}: hash no coincide con la posición recibida")
    require(nonempty(diagnosis["diagnosis_id"]), "diagnosis_id vacío")
    require(nonempty(review["review_id"]), "review_id vacío")
    require(nonempty(diagnosis["skill_version"]), "skill_version vacío")
    require(isinstance(diagnosis["assessment"], str) and diagnosis["assessment"] in ASSESSMENTS,
            "Assessment desconocido")
    require(isinstance(review["verdict"], str) and review["verdict"] in VERDICTS,
            "Verdict desconocido")
    require(independent_plan["role"] == "revisora", "El plan suministrado no es de revisora")
    for ref, source in ((review["diagnosis_ref"], diagnosis),
                        (diagnosis["choice_ref"], choice),
                        (review["independent_plan_ref"], independent_plan)):
        check_ref_shape(ref)
        contratos.check_reference(ref, source)
    check_revision(diagnosis, previous_diagnosis, "diagnosis")
    check_revision(review, previous_review, "review")
    if review["verdict"] == "corregir":
        return "suspendida"
    if review["verdict"] == "discrepancia":
        return "disputada"
    if review["verdict"] == "no_evaluable" or diagnosis["assessment"] == "indeterminada":
        return "incierta"
    return "utilizable"


def check_files(diagnosis_path, review_path, position_path, choice_path, independent_plan_path,
                *, previous_diagnosis_path=None, previous_review_path=None):
    """Lee JSON estricto; referencias canónicas y recibos de bytes van separados."""
    paths = {"diagnosis": diagnosis_path, "review": review_path, "position": position_path,
             "choice": choice_path, "independent_plan": independent_plan_path}
    if previous_diagnosis_path is not None:
        paths["previous_diagnosis"] = previous_diagnosis_path
    if previous_review_path is not None:
        paths["previous_review"] = previous_review_path
    records = {kind: contratos.read(path) for kind, path in paths.items()}
    status = check_pair(**records)
    receipts = [{"role": kind, "reference": contratos.reference(records[kind]),
                 "sha256_bytes": contratos.file_digest(path)} for kind, path in paths.items()]
    diagnosis, review = records["diagnosis"], records["review"]
    return {"contract_version": contratos.VERSION, "status": status,
            "input_refs": [contratos.reference(diagnosis), contratos.reference(review)],
            "receipts": receipts, "assessment": diagnosis["assessment"],
            "impact": diagnosis["impact"],
            "diagnosis_confidence": diagnosis["confidence"],
            "review_confidence": review["confidence"],
            "limitations": ["No acredita legalidad, estrategia ni temporalidad del plan"]}


def measure(observations):
    """Cuenta un criterio predefinido, preservando datos faltantes y exclusiones."""
    require(isinstance(observations, list), "Se esperaba una lista de observaciones")
    seen, scope = set(), None
    counts = {"observed": 0, "eligible": 0, "evaluable": 0, "met": 0,
              "unmet": 0, "missing": 0, "excluded": 0}
    for row in observations:
        require(isinstance(row, dict), "Observación inválida")
        for field in ("occasion_id", "objective_id", "scope"):
            require(nonempty(row.get(field)), f"Falta {field}")
        key = row["occasion_id"]
        require(key not in seen, f"Ocasión duplicada: {key}")
        seen.add(key)
        current_scope = (row["objective_id"], row["scope"])
        if scope is None:
            scope = current_scope
        require(current_scope == scope, "No mezclar objetivos o ámbitos")
        require(type(row.get("eligible")) is bool, "Elegibilidad debe ser booleana")
        counts["observed"] += 1
        if not row["eligible"]:
            require(row.get("outcome") is None and nonempty(row.get("reason")),
                    "Exclusión requiere motivo y outcome null")
            counts["excluded"] += 1
            continue
        outcome = row.get("outcome")
        require(outcome in {"met", "unmet", "missing"}, "Resultado desconocido")
        if outcome == "missing":
            require(nonempty(row.get("reason")), "Dato faltante requiere motivo")
        else:
            require(bool(row.get("evidence_ref")), "Resultado evaluado requiere evidencia")
            counts["evaluable"] += 1
        counts["eligible"] += 1
        counts[outcome] += 1
    return {"objective_id": scope[0] if scope else None,
            "scope": scope[1] if scope else None, **counts}


def mark_affected(memory, replaced_refs):
    """Devuelve copia; invalida derivados transitivos, preserva fuentes e historial."""
    require(isinstance(memory, list), "Memoria debe ser lista")
    require(isinstance(replaced_refs, list) and replaced_refs, "Faltan referencias sustituidas")
    for ref in replaced_refs:
        check_ref_shape(ref)
    replaced = {(ref["schema"], ref["sha256"]) for ref in replaced_refs}
    items = deepcopy(memory)
    seen = set()
    for item in items:
        require(isinstance(item, dict) and nonempty(item.get("id")), "Conclusión sin ID")
        require(item["id"] not in seen, "IDs de memoria duplicados")
        seen.add(item["id"])
        require(isinstance(item.get("source_ids"), list) and
                all(nonempty(source) for source in item["source_ids"]), "source_ids inválido")
        require(isinstance(item.get("source_refs"), list), "Falta source_refs canónico")
        for ref in item["source_refs"]:
            check_ref_shape(ref)
        require(item.get("status") in {"active", "requires_review", "superseded"},
                "Estado de memoria desconocido")
    require(all(set(item["source_ids"]) <= seen for item in items),
            "source_ids solo admite conclusiones locales presentes; artefactos usan source_refs")
    affected = {item["id"] for item in items if
                {(ref["schema"], ref["sha256"]) for ref in item["source_refs"]} & replaced}
    while True:
        newly_affected = {item["id"] for item in items if set(item["source_ids"]) & affected}
        if newly_affected <= affected:
            break
        affected.update(newly_affected)
    for item in items:
        causes = sorted(set(item["source_ids"]) & affected)
        direct = [ref for ref in item["source_refs"] if (ref["schema"], ref["sha256"]) in replaced]
        if item["id"] in affected:
            if item["status"] != "superseded":
                item["status"] = "requires_review"
            previous = item.get("revision_reasons", {"source_ids": [], "source_refs": []})
            refs = {contratos.canonical(ref): ref for ref in previous["source_refs"] + direct}
            item["revision_reasons"] = {"source_ids": sorted(set(previous["source_ids"]) | set(causes)),
                                        "source_refs": [refs[key] for key in sorted(refs)]}
    return items


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("comprobar")
    check.add_argument("diagnosis")
    check.add_argument("review")
    check.add_argument("position")
    check.add_argument("choice")
    check.add_argument("independent_plan")
    check.add_argument("--previous-diagnosis")
    check.add_argument("--previous-review")
    metrics = commands.add_parser("medir")
    metrics.add_argument("observations")
    revise = commands.add_parser("revisar")
    revise.add_argument("memory")
    revise.add_argument("replaced_artifacts", nargs="+")
    args = parser.parse_args()
    try:
        if args.command == "comprobar":
            result = check_files(args.diagnosis, args.review, args.position, args.choice,
                                 args.independent_plan, previous_diagnosis_path=args.previous_diagnosis,
                                 previous_review_path=args.previous_review)
        elif args.command == "medir":
            result = measure(contratos.read(args.observations))
        else:
            result = mark_affected(contratos.read(args.memory),
                                   [contratos.reference(contratos.read(path)) for path in args.replaced_artifacts])
    except (ValueError, OSError) as error:
        parser.exit(2, f"Error: {error}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
