"""Registro local de la analista: secuencia y cuentas declaradas, no reglas de juego."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from herramientas.profesora_lorcana.contratos import (
    canonical, check_reference, digest, file_digest, read, reference,
)

from herramientas.rutas_trabajo import resolver_ruta

VERSION = "0.2.0"
REQUIRED = {
    "position": "position_id game_ref deck_ref boundary available_state known_information rules_evidence completeness",
    "plan": "position_id position_sha256 role skill_version preferred_line alternatives assumptions risks rules_refs confidence missing_information",
    "choice": "position_id position_sha256 observed_action evidence_ref intention",
    "diagnosis": "diagnosis_id position_id position_sha256 skill_version choice_ref assessment impact confidence facts inferences alternatives rules_refs questions_for_ivan limitations revision_of",
}
SCHEMAS = {kind: f"lorcana-{kind}-v1" for kind in REQUIRED}
ASSESSMENTS = {"acierto", "defendible", "mejora_probable", "error_demostrado", "indeterminada"}
FUTURE_KEYS = {"deckOrder", "deck_order", "future_draws", "winner", "result", "outcome",
               "observed_action", "diagnosis", "assessment", "opponent_hand"}


def encode(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def scan_future(value):
    if isinstance(value, dict):
        require(not FUTURE_KEYS.intersection(value), "Posición con clave de futuro/elección/diagnóstico")
        opponent = value.get("opponent")
        require(not isinstance(opponent, dict) or not opponent.get("hand"), "Mano rival no admitida como estado conocido")
        for item in value.values():
            scan_future(item)
    elif isinstance(value, list):
        for item in value:
            scan_future(item)


def balance(line):
    """Comprueba financiación declarada; no acredita saldo, coste, objetivo o efecto."""
    require(isinstance(line, dict), "Línea sin estructura")
    for key in ("label", "status", "resources", "steps", "conditions", "benefit", "risk", "rules_refs"):
        require(key in line, f"Línea sin {key}")
    require(line["status"] in {"realizable", "condicionada"}, "Estado de línea inválido")
    require(isinstance(line["conditions"], list), "Condiciones deben ser lista")
    require(line["status"] != "condicionada" or line["conditions"], "Línea condicionada sin condición")
    require(all(nonempty(line[k]) for k in ("label", "benefit", "risk")), "Línea sin explicación")
    require(isinstance(line["rules_refs"], list), "Referencias de línea deben ser lista")
    require(isinstance(line["resources"], dict), "Recursos deben ser objeto")
    remaining = dict(line["resources"])
    require(all(nonempty(k) and type(v) is int and v >= 0 for k, v in remaining.items()), "Saldo inicial inválido")
    require(isinstance(line["steps"], list) and line["steps"], "Línea sin pasos")
    for step in line["steps"]:
        require(isinstance(step, dict) and nonempty(step.get("action")), "Paso sin acción")
        require(isinstance(step.get("evidence_refs"), list) and step["evidence_refs"], "Paso sin evidencia")
        for key, sign in (("spend", -1), ("gain", 1)):
            movements = step.get(key)
            require(isinstance(movements, dict), f"Paso sin {key}")
            for resource, amount in movements.items():
                require(resource in remaining and type(amount) is int and amount >= 0, "Movimiento de recurso inválido")
                remaining[resource] += sign * amount
                require(remaining[resource] >= 0, f"Línea no financiada: {resource}")
    return remaining


def validate(kind, value):
    require(isinstance(value, dict), "Artefacto debe ser objeto")
    canonical(value)  # También rechaza valores no finitos desde la API Python.
    require(value.get("schema") == SCHEMAS[kind], "Schema incorrecto")
    missing = set(REQUIRED[kind].split()) - value.keys()
    require(not missing, f"Faltan campos: {sorted(missing)}")
    require(nonempty(value["position_id"]), "position_id vacío")
    if kind == "position":
        scan_future(value)
        for key in ("game_ref", "deck_ref", "boundary", "available_state", "completeness"):
            require(isinstance(value[key], dict) and value[key], f"Posición sin {key}")
        return
    require(nonempty(value["position_sha256"]), "Falta hash de posición")
    if kind in {"plan", "diagnosis"}:
        require(nonempty(value["skill_version"]), "Falta versión de skill")
        confidence = value["confidence"]
        require(isinstance(confidence, dict) and confidence.get("level") in {"baja", "media", "alta", "no_evaluable"}
                and nonempty(confidence.get("basis")), "Confianza inválida")
        list_fields = ("alternatives", "rules_refs", "assumptions", "risks", "missing_information") if kind == "plan" else (
            "alternatives", "rules_refs", "facts", "inferences", "questions_for_ivan", "limitations")
        for key in list_fields:
            require(isinstance(value[key], list), f"{key} debe ser lista")
        for line in value["alternatives"]:
            balance(line)
    if kind == "plan":
        require(value["role"] == "analista", "Este registro solo sella planes de analista")
        if value["preferred_line"] is not None:
            balance(value["preferred_line"])
        else:
            require(value["missing_information"], "Plan sin línea ni información pendiente")
        require(value["alternatives"] or nonempty(value.get("alternatives_note")), "Explica ausencia de alternativas")
    elif kind == "choice":
        require(bool(value["observed_action"]) and bool(value["evidence_ref"]), "Elección sin acción/evidencia")
        require(value["intention"] is not None, "Intención debe indicar desconocida si no consta")
    elif kind == "diagnosis":
        require(nonempty(value["diagnosis_id"]), "diagnosis_id vacío")
        require(value["assessment"] in ASSESSMENTS, "Evaluación inválida")
        impact = value["impact"]
        require(isinstance(impact, dict) and impact.get("level") in {"bajo", "medio", "alto", "indeterminado"}
                and nonempty(impact.get("reason")), "Impacto inválido")


def local_receipt(path):
    """Integridad local de bytes: nunca se intercambia como referencia de artefacto."""
    return {"path": Path(path).name, "sha256_bytes": file_digest(path)}


def resolve_ref(session, receipt):
    require(isinstance(receipt, dict) and set(receipt) == {"path", "sha256_bytes"}, "Recibo local inválido")
    name = receipt["path"]
    require(nonempty(name) and Path(name).name == name and "/" not in name and "\\" not in name, "Referencia fuera de sesión")
    path = session / name
    require(path.is_file() and file_digest(path) == receipt["sha256_bytes"], "Hash/recibo alterado")
    return path


def verify(session):
    """Relee cadena; no interpreta acciones ni comprueba la semántica del texto libre."""
    session = resolver_ruta(session)
    entries = sorted(session.glob("[0-9][0-9][0-9][0-9]-*.json"))
    require(entries, "Sesión sin posición")
    kinds, previous, position_hash, position_id, choice_value = [], None, None, None, None
    diagnoses = []
    for index, path in enumerate(entries):
        require(path.name.startswith(f"{index:04d}-"), "Cadena incompleta")
        record = read(path)
        require(set(record) == {"schema", "kind", "artifact_receipt", "previous_record"}
                and record["schema"] == "lorcana-analyst-record-v2", "Recibo inválido; no migrar ensayos v0.1")
        require(record["previous_record"] == previous, "Cadena de recibos alterada")
        kind = record["kind"]
        require(kind in REQUIRED, "Tipo desconocido")
        artifact = resolve_ref(session, record["artifact_receipt"])
        value = read(artifact)
        validate(kind, value)
        if kind == "position":
            require(not kinds and artifact.name == "position.json", "Posición fuera de orden")
            position_hash, position_id = digest(value), value["position_id"]
        else:
            require(value["position_id"] == position_id and value["position_sha256"] == position_hash, "Identidad/hash de posición no coinciden")
            if kind == "plan":
                require(kinds == ["position"], "Plan debe preceder a la elección")
            elif kind == "choice":
                require(kinds == ["position", "plan"], "Elección requiere plan previo")
                choice_value = value
            else:
                require(kinds[:3] == ["position", "plan", "choice"], "Diagnóstico requiere elección revelada")
                try:
                    check_reference(value["choice_ref"], choice_value)
                except ValueError as error:
                    raise ValueError("Diagnóstico refiere otra elección") from error
                expected_revision = diagnoses[-1][0] if diagnoses else None
                require(value["revision_of"] == expected_revision, "Revisión debe conservar diagnóstico anterior")
                require(value["diagnosis_id"] not in [d[1] for d in diagnoses], "Revisión debe tener ID nuevo")
                diagnoses.append((reference(value), value["diagnosis_id"]))
        kinds.append(kind)
        previous = local_receipt(path)
    return {"kinds": kinds, "last_record": previous, "position_sha256": position_hash}


def next_state(session, kind):
    """Precomprobar antes de abrir una entrada posterior desde la CLI."""
    session = resolver_ruta(session)
    if kind == "position":
        require(not session.exists(), "La sesión debe ser nueva")
        return {"kinds": [], "last_record": None}
    state = verify(session)
    if kind == "plan":
        require(state["kinds"] == ["position"], "Plan debe preceder a la elección")
    elif kind == "choice":
        require(state["kinds"] == ["position", "plan"], "Elección requiere plan previo")
    else:
        require(state["kinds"][:3] == ["position", "plan", "choice"], "Diagnóstico requiere elección revelada")
    return state


def append(session, kind, value):
    """Una sesión por posición. API: el llamador controla lo ya leído."""
    session = resolver_ruta(session)
    state = next_state(session, kind)
    validate(kind, value)
    index = len(state["kinds"])
    artifact_name = "position.json" if kind == "position" else f"{kind}-{index:04d}.json"
    # Prevalidar la transición en un directorio temporal evita dejar un registro
    # utilizable si falla una comprobación. No se presenta como transacción multiusuario.
    import tempfile
    import shutil
    with tempfile.TemporaryDirectory() as temporary:
        staged = Path(temporary) / "session"
        if session.exists():
            shutil.copytree(session, staged)
        else:
            staged.mkdir()
        (staged / artifact_name).write_bytes(encode(value))
        record = {"schema": "lorcana-analyst-record-v2", "kind": kind,
                  "artifact_receipt": local_receipt(staged / artifact_name), "previous_record": state["last_record"]}
        record_name = f"{index:04d}-{kind}.json"
        (staged / record_name).write_bytes(encode(record))
        verify(staged)
        if kind == "position":
            session.mkdir(parents=True, exist_ok=False)
        for name in (artifact_name, record_name):
            with (session / name).open("xb") as target:
                target.write((staged / name).read_bytes())
    return reference(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=[*REQUIRED, "verify"])
    parser.add_argument("input", nargs="?", type=resolver_ruta)
    parser.add_argument("--session", required=True, type=resolver_ruta)
    args = parser.parse_args()
    try:
        require(args.kind == "verify" or args.input is not None, "Falta archivo de entrada")
        if args.kind == "verify":
            result = verify(args.session)
        else:
            next_state(args.session, args.kind)  # Antes de leer la entrada.
            result = append(args.session, args.kind, read(args.input))
        print(json.dumps(result, ensure_ascii=False))
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"Registro rechazado: {error}\n")


if __name__ == "__main__":
    main()
