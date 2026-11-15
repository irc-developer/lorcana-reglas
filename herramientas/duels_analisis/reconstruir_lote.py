"""Reconstruye secuencialmente originales locales. Sin HTTP ni credenciales."""
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
import re
import tempfile
from collections import Counter
from pathlib import Path

import sys
# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo


def load_extractor():
    path = Path(__file__).resolve().parents[2] / "herramientas/duels_analisis/extraer_replays.py"
    spec = importlib.util.spec_from_file_location("extractor_duels_existente", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_json(path):
    return json.loads(resolver_ruta(path).read_text(encoding="utf-8-sig"))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def checked_bytes(file):
    path = resolver_ruta(file["path"])
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != file["sha256"]:
        raise ValueError("Hash del archivo de entrada distinto del lote")
    return path, raw


def card_weight(card):
    if not isinstance(card, dict):
        return 1
    if "card" in card:
        return card_weight(card["card"])
    return 1 + sum(card_weight(c) for c in card.get("cardsUnder", []))


class BoundaryError(ValueError):
    def __init__(self, code, seq, previous, current, total):
        self.code = code
        self.details = {"code": code, "seq": seq, "previous": previous,
                        "current": current, "totalLogs": total}
        super().__init__(f"Frontera de logs {code}: seq={seq}, previous={previous}, current={current}, total={total}")


def validate_boundaries(data):
    """Preflight the whole array before applying patches or writing states."""
    total = len(data["logs"])
    previous = data["baseSnapshotLogCount"]
    if type(previous) is not int or not 0 <= previous <= total:
        raise BoundaryError("outside_array", 0, None, previous, total)
    for frame in data["frames"]:
        count = frame["logCountAfter"]
        if type(count) is not int or not 0 <= count <= total:
            raise BoundaryError("outside_array", frame["seq"], previous, count, total)
        if count < previous:
            raise BoundaryError("decreasing_count", frame["seq"], previous, count, total)
        previous = count
    if previous != total:
        raise BoundaryError("unaccounted_logs", data["frames"][-1]["seq"] if data["frames"] else 0,
                            previous, previous, total)


def reconstruct(row, directory, extractor):
    directory = resolver_ruta(directory)
    if directory.exists():
        raise FileExistsError("Destino de derivados ya existe: usar una ruta nueva y conservar la auditoría anterior")
    directory.parent.mkdir(parents=True, exist_ok=True)
    # Failed patching, end-state checks, or event rendering must not publish a
    # partially written states file as the requested output directory.
    with tempfile.TemporaryDirectory(prefix=".duels-pending-", dir=directory.parent) as temporary:
        staging = resolver_ruta(temporary) / "ready"
        result = _reconstruct(row, staging, extractor)
        staging.rename(directory)
    result["prefix"] = str(directory / "partida-01")
    return result


def _reconstruct(row, directory, extractor):
    file = row["files"]["replay"]
    path, raw = checked_bytes(file)
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    decoded_sha = hashlib.sha256(raw).hexdigest()
    if file.get("decoded_json") and decoded_sha != file["decoded_json"]["sha256"]:
        raise ValueError("Hash descomprimido distinto del contrato")
    data = json.loads(raw.decode("utf-8-sig"))
    if data["format"] != "duels-replay-v1" or data["gameId"] != row["game_id"]:
        raise ValueError("Formato o identidad de replay distintos")
    if data["perspective"] != row["your_player"] or data["perspective"] != data["baseSnapshot"]["viewingAs"]:
        raise ValueError("Perspectiva distinta del catálogo")
    frames, logs = data["frames"], data["logs"]
    if not frames or [f["seq"] for f in frames] != list(range(1, len(frames) + 1)):
        raise ValueError("Frames ausentes/discontinuos")
    validate_boundaries(data)
    if Counter(data["decklist"]) != Counter(row["deck"]["printing_counts"]):
        # Counter(dict) preserves quantities, unlike Counter(dict.keys()).
        raise ValueError("Lista del replay distinta de la partida catalogada")
    catalog = {}
    extractor.collect_catalog(data, catalog)
    state = copy.deepcopy(data["baseSnapshot"])
    initial = Counter(c["id"] for c in state["myPlayer"]["hand"])
    initial.update(state["myPlayer"]["deckOrder"])
    if initial != Counter(data["decklist"]):
        raise ValueError("Mano+mazo iniciales no conservan la lista")
    directory.mkdir(parents=True, exist_ok=True)
    prefix = directory / "partida-01"
    upserts, missing = Counter(), Counter()
    previous_count = data["baseSnapshotLogCount"]
    actions = []
    with gzip.open(str(prefix) + "-estados.jsonl.gz", "wt", encoding="utf-8") as handle:
        handle.write(json.dumps({"seq": 0, "snapshot": state}, ensure_ascii=False) + "\n")
        for frame in frames:
            for operation in frame["patch"]:
                extractor.apply_operation(state, operation, upserts, missing)
            count = frame["logCountAfter"]
            if len(state["myPlayer"]["deckOrder"]) != state["myPlayer"]["deckCount"]:
                raise ValueError("Tamaño del mazo incoherente")
            actions.append({
                "seq": frame["seq"], "actionType": frame["actionType"], "player": frame["player"],
                "turnNumber": frame["turnNumber"], "timestamp": frame.get("ts"),
                "logsFromInclusive": previous_count, "logsToExclusive": count,
            })
            handle.write(json.dumps({"seq": frame["seq"], "snapshot": state}, ensure_ascii=False) + "\n")
            previous_count = count
    if previous_count != len(logs):
        raise ValueError("Quedan logs sin asociar")
    if state.get("status") != "finished" or state.get("winner") != data.get("winner") or state.get("victoryReason") != data.get("victoryReason"):
        raise ValueError("Final reconstruido no coincide con encabezado")
    final_weight = state["myPlayer"]["deckCount"] + sum(
        card_weight(c) for zone in ("hand", "field", "items", "inkwell", "discard")
        for c in state["myPlayer"].get(zone, []))
    if final_weight != len(data["decklist"]):
        raise ValueError("No se conservan las cartas propias al final")
    events = [dict(e, index=i, resolvedMessage=extractor.render_message(e)) for i, e in enumerate(logs)]
    if len({e["id"] for e in events}) != len(events):
        raise ValueError("IDs de eventos duplicados")
    summary = {
        "format": data["format"], "gameId": data["gameId"], "matchId": row.get("match_id"),
        "gameNumber": row.get("match_game_number") or 1, "perspective": data["perspective"],
        "firstPlayer": state.get("firstPlayer"), "source": str(path),
        "sourceSha256": file["sha256"], "decodedSha256": decoded_sha,
        "decklist": [{"id": c, "name": catalog.get(c, "[nombre no localizado]"), "copies": n}
                     for c, n in sorted(Counter(data["decklist"]).items())],
        "frames": len(frames), "logs": len(logs),
        "replaceCreatingPropertiesCount": sum(upserts.values()), "removeMissingPropertiesCount": sum(missing.values()),
        "validation": {"allFramesApplied": True, "allLogsAccountedFor": True,
                       "initialDeckConservation": True, "finalCardCount": final_weight,
                       "resultMatchesHeader": True},
    }
    write_json(resolver_ruta(str(prefix) + "-resumen.json"), summary)
    write_json(resolver_ruta(str(prefix) + "-acciones.json"), actions)
    write_json(resolver_ruta(str(prefix) + "-eventos.json"), events)
    return {"status": "reconstructed", "prefix": str(prefix), "frames": len(frames),
            "logs": len(logs), "finalCardCount": final_weight,
            "upserts": sum(upserts.values()), "missingRemovals": sum(missing.values())}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("batch", type=resolver_ruta)
    p.add_argument("--out", type=resolver_ruta, required=True)
    args = p.parse_args()
    if (args.out / "reconstruccion.json").exists():
        p.error("Ya existe una auditoría en destino; usar una ruta/version nueva")
    rows = [json.loads(l) for l in (args.batch / "catalogo.jsonl").read_text(encoding="utf-8").splitlines()]
    rows = sorted((r for r in rows if r["selection"]["status"] == "safe"), key=lambda r: (r.get("started_at") or "", r["game_id"]))
    extractor = load_extractor()
    records = []
    for index, row in enumerate(rows, 1):
        game_id = row["game_id"]
        if not re.fullmatch(r"[A-Za-z0-9_-]+", game_id):
            raise ValueError("ID no apto como nombre de archivo")
        record = {"gameId": game_id, "matchId": row.get("match_id"), "yourPlayer": row["your_player"]}
        if row["files"]["replay"]["status"] != "verified_json":
            record.update(status="not_available", sourceStatus=row["files"]["replay"]["status"])
        else:
            try:
                record.update(reconstruct(row, args.out / "reconstruidos" / game_id, extractor))
            except Exception as exc:
                # Error details stay local and are never decision input.
                record.update(status="failed", errorType=type(exc).__name__, error=str(exc))
                if isinstance(exc, BoundaryError):
                    record["boundaryDetails"] = exc.details
        records.append(record)
        if index % 25 == 0:
            print(json.dumps({"processed": index, "statuses": dict(Counter(r["status"] for r in records))}), flush=True)
    result = {"schema": "duels-reconstruction-audit-v2", "batchId": args.batch.name,
              "extractorPath": "herramientas/duels_analisis/extraer_replays.py",
              "extractorSha256": hashlib.sha256(resolver_ruta(extractor.__file__).read_bytes()).hexdigest(),
              "statuses": dict(Counter(r["status"] for r in records)), "games": records,
              "rulesOrUiSemanticsCertified": False}
    args.out.mkdir(parents=True, exist_ok=True)
    write_json(args.out / "reconstruccion.json", result)
    print(json.dumps({"finished": True, "statuses": result["statuses"]}), flush=True)


if __name__ == "__main__":
    main()
