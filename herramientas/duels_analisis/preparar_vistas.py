"""Genera posiciones concretas tras reconstrucción; no imprime sus cartas."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

from vista_decision import build_view

import sys
# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo


def enrich_registered_list(view, identities, source_hash):
    """Only already registered own IDs; never export the global card map."""
    unresolved = False
    for card in view["ownRegisteredList"]:
        identity = identities.get(card["id"], "")
        if identity.startswith("full-name:"):
            card["name"] = identity[len("full-name:"):]
        else:
            unresolved = True
    view["registeredListIdentityMapSha256"] = source_hash
    view["limits"]["registeredListIdentityIncomplete"] = unresolved


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("audit", type=resolver_ruta)
    p.add_argument("batch", type=resolver_ruta)
    p.add_argument("--out", type=resolver_ruta, required=True)
    args = p.parse_args()
    audit = json.loads(args.audit.read_text(encoding="utf-8"))
    identity_path = args.batch / "normalizacion.json"
    identities = json.loads(identity_path.read_text(encoding="utf-8"))["identities"]
    identity_hash = hashlib.sha256(identity_path.read_bytes()).hexdigest()
    rows = [json.loads(l) for l in (args.batch / "catalogo.jsonl").read_text(encoding="utf-8").splitlines()]
    rows = {r["game_id"]: r for r in rows if r["selection"]["status"] == "safe"}
    available = {g["gameId"]: g for g in audit["games"] if g["status"] == "reconstructed"}
    records = []
    for game_id, rec in available.items():
        row = rows[game_id]
        prefix = resolver_ruta(rec["prefix"])
        actions = json.loads(resolver_ruta(str(prefix) + "-acciones.json").read_text(encoding="utf-8"))
        previous_rows = sorted((r for r in rows.values() if row.get("match_id")
                                and r.get("match_id") == row["match_id"]
                                and (r.get("match_game_number") or 0) < (row.get("match_game_number") or 0)),
                               key=lambda r: r.get("match_game_number") or 0)
        # Strict projector rejects seat changes. Missing memory is stated,
        # never replaced with private/future information.
        previous = [resolver_ruta(available[r["game_id"]]["prefix"]) for r in previous_rows
                    if r["game_id"] in available and r["your_player"] == row["your_player"]]
        omitted_previous = [r["game_id"] for r in previous_rows
                            if r["game_id"] not in available or r["your_player"] != row["your_player"]]
        candidates = {
            "mulligan": lambda a: a["actionType"] == "MULLIGAN",
            "tinta-inicial": lambda a: a["actionType"] == "ADD_TO_INK",
            "transicion": lambda a: a["actionType"] == "ADD_TO_INK" and a["turnNumber"] >= 6,
        }
        for kind, predicate in candidates.items():
            action = next((a for a in actions if a["player"] == row["your_player"] and predicate(a)), None)
            record = {"gameId": game_id, "kind": kind}
            if action is None:
                record["status"] = "no_matching_action"
            else:
                try:
                    v = build_view(prefix, action["seq"], previous)
                    enrich_registered_list(v, identities, identity_hash)
                    v["limits"]["previousGameMemoryIncomplete"] = bool(omitted_previous)
                    v["omittedPreviousGameIds"] = omitted_previous
                    destination = args.out / game_id / f"{kind}-antes-{action['seq']:03}.json"
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                    record.update(status="created", beforeSeq=action["seq"], path=str(destination),
                                  incompletePrompt=v["limits"]["pendingPromptIncomplete"],
                                  incompletePreviousMemory=bool(omitted_previous))
                except Exception as exc:
                    record.update(status="failed", errorType=type(exc).__name__, error=str(exc))
            records.append(record)
    result = {"schema": "duels-position-availability-v1", "batchId": args.batch.name,
              "reconstructedGames": len(available), "counts": dict(Counter(r["status"] for r in records)),
              "positions": records}
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "catalogo-vistas.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"reconstructedGames": len(available), "counts": result["counts"]}))


if __name__ == "__main__":
    main()
