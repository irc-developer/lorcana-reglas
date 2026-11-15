"""Medidas descriptivas de un lote local; no infiere arquetipos ni decisiones."""
import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import sys
# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo


def utc(value):
    if not value:
        return datetime.max.replace(tzinfo=timezone.utc)
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def outcomes(rows):
    return {"games": len(rows), "results": dict(sorted(Counter(r.get("result", "unknown") for r in rows).items()))}


def grouped(rows, field):
    groups = defaultdict(list)
    for row in rows:
        # Colors are an opaque API string, never an iterable of color letters
        # and never an archetype label.
        key = row.get(field)
        if not isinstance(key, (str, bool, int, float, type(None))):
            raise ValueError(f"Tipo no soportado para {field}")
        groups["unknown" if key is None else str(key)].append(row)
    return {k: outcomes(v) for k, v in sorted(groups.items())}


def value_range(rows, field):
    values = [r[field] for r in rows if type(r.get(field)) in (int, float)]
    return {"known": len(values), "missing": len(rows) - len(values),
            "min": min(values) if values else None, "max": max(values) if values else None}


def summarize(rows):
    selected = [r for r in rows if r.get("selection", {}).get("status") == "safe"]
    keys = [(r["account_scope"], r["game_id"]) for r in selected]
    if len(keys) != len(set(keys)):
        raise ValueError("Partida duplicada en la selección")
    if len(set(r["account_scope"] for r in selected)) > 1:
        raise ValueError("No mezclar cuentas en un análisis personal")
    selected.sort(key=lambda r: (utc(r.get("started_at")), r.get("match_game_number") or 0, r["game_id"]))
    printing = defaultdict(list)
    for r in selected:
        d = r.get("deck")
        if not d or not d.get("printing_sha256"):
            raise ValueError("Falta lista/huella de impresión")
        if not d["printing_counts"] or any(type(q) is not int or q <= 0 for q in d["printing_counts"].values()):
            raise ValueError("Cantidades de lista inválidas")
        printing[d["printing_sha256"]].append(r)
    versions = []
    labels = {}
    for index, (fingerprint, group) in enumerate(printing.items(), 1):
        counts = group[0]["deck"]["printing_counts"]
        if any(r["deck"]["printing_counts"] != counts for r in group):
            raise ValueError("Huella compartida por listas diferentes")
        label = f"V{index:02}"
        labels[fingerprint] = label
        versions.append({
            "label": label, "printing_sha256": fingerprint,
            "catalogCompositionHashes": sorted(set(r["deck"]["composition_sha256"] for r in group)),
            "printingCounts": counts, "totalCards": sum(counts.values()),
            "firstObserved": group[0].get("started_at"),
            "lastObserved": group[-1].get("started_at"), **outcomes(group),
            "gameIds": [r["game_id"] for r in group],
            "unresolvedIds": sorted(set(c for r in group for c in r["deck"]["unresolved_ids"])),
            "byQueue": grouped(group, "queue_name"),
        })
    episodes = []
    for r in selected:
        label = labels[r["deck"]["printing_sha256"]]
        if not episodes or episodes[-1]["label"] != label:
            episodes.append({"label": label, "firstObserved": r.get("started_at"),
                             "lastObserved": r.get("started_at"), "gameIds": []})
        episodes[-1]["gameIds"].append(r["game_id"])
        episodes[-1]["lastObserved"] = r.get("started_at")
    counts_by_label = {v["label"]: v["printingCounts"] for v in versions}
    transitions = []
    for previous, current in zip(episodes, episodes[1:]):
        a, b = counts_by_label[previous["label"]], counts_by_label[current["label"]]
        delta = {c: b.get(c, 0) - a.get(c, 0) for c in sorted(set(a) | set(b)) if a.get(c, 0) != b.get(c, 0)}
        transitions.append({"from": previous["label"], "to": current["label"],
                            "afterObserved": previous["lastObserved"],
                            "byObserved": current["firstObserved"], "deltaByPrintingId": delta,
                            "copiesAdded": sum(v for v in delta.values() if v > 0),
                            "copiesRemoved": -sum(v for v in delta.values() if v < 0)})
    matches, global_matches = defaultdict(list), defaultdict(list)
    for r in rows:
        if r.get("match_id"):
            global_matches[(r["account_scope"], r["match_id"])].append(r)
    for r in selected:
        if r.get("match_id"):
            matches[(r["account_scope"], r["match_id"])].append(r)
    match_reports = []
    for key, group in matches.items():
        score = Counter(r.get("result") for r in group)
        numbers = sorted(r.get("match_game_number") or -1 for r in group)
        same_rows = {r["game_id"] for r in group} == {r["game_id"] for r in global_matches[key]}
        sequence_complete = numbers in ([1, 2], [1, 2, 3])
        decided = ((score["win"] == 2 and score["loss"] <= 1) or
                   (score["loss"] == 2 and score["win"] <= 1)) and score["win"] + score["loss"] == len(group)
        complete = same_rows and sequence_complete and decided and all(r.get("match_format") == "bo3" for r in group)
        mmr_rows = [r for r in group if r.get("mmr_before") is not None]
        match_reports.append({
            "matchId": key[1], "gameIds": [r["game_id"] for r in group],
            "observedScore": dict(score), "completeWithinReturnedCatalog": complete,
            "derivedResult": ("win" if score["win"] == 2 else "loss") if complete else "undetermined",
            "printingLabels": sorted(set(labels[r["deck"]["printing_sha256"]] for r in group)),
            "mmrObservationCount": len(mmr_rows),
        })
    known_dates = [r.get("started_at") for r in selected if r.get("started_at")]
    return {
        "schema": "duels-history-analysis-v1", "selected": outcomes(selected),
        "selectionScopes": dict(Counter(r["selection"].get("scope", "unspecified") for r in selected)),
        "historicalNameVerifiedRows": sum(r["selection"].get("historical_name_verified") is True for r in selected),
        "firstObserved": min(known_dates, key=utc) if known_dates else None,
        "lastObserved": max(known_dates, key=utc) if known_dates else None,
        "byQueue": grouped(selected, "queue_name"), "byFormat": grouped(selected, "match_format"),
        "byFirstPlayer": grouped(selected, "went_first"), "bySeason": grouped(selected, "season_name"),
        "byOpponentColorsOnly": grouped(selected, "opp_deck_colors"),
        "endReasons": grouped(selected, "end_reason"),
        "opponentDisplayNames": len(set(r.get("opp_display_name") for r in selected if r.get("opp_display_name"))),
        "mmrBefore": value_range(selected, "mmr_before"),
        "mmrAfter": value_range(selected, "mmr_after"),
        "opponentMmrBefore": value_range(selected, "opp_mmr_before"),
        "durationSeconds": value_range(selected, "duration_seconds"),
        "missingFields": dict(sorted(Counter(k for r in selected for k in r.get("absent_fields", [])).items())),
        "rowsWithConflicts": [{"gameId": r["game_id"], "fields": sorted(set(c["field"] for c in r["conflicts"]))}
                              for r in selected if r.get("conflicts")],
        "fileStatuses": {kind: dict(Counter(r.get("files", {}).get(kind, {}).get("status", "unknown") for r in selected))
                         for kind in ("replay", "gamelog")},
        "gamesWithDerived": sum(any(d.get("status") == "verified_structure" for d in r.get("derived", [])) for r in selected),
        "listSizes": dict(Counter(sum(r["deck"]["printing_counts"].values()) for r in selected)),
        "catalogIdentityCompleteRows": sum(r["deck"]["identity_complete"] is True for r in selected),
        "catalogUnresolvedIds": sorted(set(c for r in selected for c in r["deck"]["unresolved_ids"])),
        "versionsByPrinting": versions, "episodes": episodes, "transitionsObserved": transitions,
        "matches": match_reports,
        "matchDerivedResults": dict(Counter(m["derivedResult"] for m in match_reports)),
        "gamesWithoutMatchId": sum(not r.get("match_id") for r in selected),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("batch", type=resolver_ruta)
    p.add_argument("--out", type=resolver_ruta, required=True)
    args = p.parse_args()
    source = args.batch / "catalogo.jsonl"
    rows = [json.loads(line) for line in source.read_text(encoding="utf-8").splitlines()]
    result = summarize(rows)
    result["batchId"] = args.batch.name
    result["sourceHashes"] = {name: hashlib.sha256((args.batch / name).read_bytes()).hexdigest()
                              for name in ("catalogo.jsonl", "normalizacion.json", "seleccion.json")}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"written": str(args.out), "selected": result["selected"],
                      "printingGroups": len(result["versionsByPrinting"]),
                      "matchDerivedResults": result["matchDerivedResults"]}))


if __name__ == "__main__":
    main()
