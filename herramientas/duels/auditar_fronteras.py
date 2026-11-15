"""Diagnóstico offline de contadores de un replay. No repara ni produce vistas docentes."""
import argparse
from collections import Counter
import copy
import gzip
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import traceback

import duels as d

# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo


def audit(data, gamelog):
    logs, frames = data["logs"], data["frames"]
    previous = data["baseSnapshotLogCount"]
    boundaries, future_prefixes = [], []
    for frame in frames:
        count = frame["logCountAfter"]
        problems = []
        if not 0 <= count <= len(logs):
            problems.append("outside_array")
        if count < previous:
            problems.append("decreasing_count")
        if problems:
            boundaries.append({"seq": frame["seq"], "previous_count": previous,
                               "count": count, "array_length": len(logs), "problems": problems})
        future = [i for i, event in enumerate(logs[:count]) if event["timestamp"] > frame["ts"]]
        if future:
            future_prefixes.append({"seq": frame["seq"], "frame_ts": frame["ts"], "count": count,
                                    "events": [{"index": i, "timestamp": logs[i]["timestamp"],
                                                "type": logs[i]["type"]} for i in future]})
        previous = count
    ri, gi = {e["id"]: e for e in logs}, {e["id"]: e for e in gamelog}
    return {
        "frames": len(frames), "logs": len(logs), "base_count": data["baseSnapshotLogCount"],
        "final_count": previous, "final_count_matches_length": previous == len(logs),
        "continuous_seq": [f["seq"] for f in frames] == list(range(1, len(frames) + 1)),
        "boundary_violations": boundaries, "future_prefixes": future_prefixes,
        "gamelog": {"logs": len(gamelog), "shared_ids": len(ri.keys() & gi.keys()),
                    "replay_only_ids_count": len(ri.keys() - gi.keys()),
                    "unique_replay_ids": len(ri) == len(logs), "unique_gamelog_ids": len(gi) == len(gamelog),
                    "common_order_equal": [e["id"] for e in logs if e["id"] in gi] == [e["id"] for e in gamelog if e["id"] in ri],
                    "extra_events": [{"index": i, "type": e["type"], "timestamp": e["timestamp"]}
                                     for i, e in enumerate(gamelog) if e["id"] not in ri]},
    }


def checked(ref):
    path = resolver_ruta(ref["path"])
    raw = path.read_bytes()
    if d.sha(raw) != ref["sha256"] or len(raw) != ref["bytes"]:
        raise d.DuelsError("Hash o tamaño de evidencia incorrectos")
    return raw


def module(path, name):
    # Ejecutar código local de confianza, nunca contenido del replay.
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def investigate(catalog, acquisition, game_id, out):
    catalog, acquisition, out = resolver_ruta(catalog), resolver_ruta(acquisition), resolver_ruta(out)
    row = next(json.loads(line) for line in catalog.read_text(encoding="utf-8").splitlines()
               if json.loads(line)["game_id"] == game_id)
    manifest = json.loads(acquisition.read_bytes())
    entry = manifest["games"][game_id]
    data, inputs, association = {}, {}, {}
    for kind in ("replay", "gamelog"):
        ref = row["files"][kind]
        raw = checked(ref)
        decoded = gzip.decompress(raw) if raw.startswith(b"\x1f\x8b") else raw
        decoded_ref = ref["decoded_json"]
        if decoded != checked(decoded_ref):
            raise d.DuelsError("Copia JSON distinta de los bytes descomprimidos")
        data[kind] = json.loads(decoded)
        inputs[kind] = {k: ref[k] for k in ("path", "sha256", "bytes")}
        inputs[kind]["decoded_json"] = {k: decoded_ref[k] for k in ("path", "sha256", "bytes")}
        asset = entry["assets"][kind]
        if asset["original"]["sha256"] != ref["sha256"]:
            raise d.DuelsError("Catálogo y adquisición no apuntan al mismo original")
        attempt = asset["attempts"][-1]
        obs = attempt["manifest"]
        downloaded_manifest_ref = dict(obs["file"], path=str(acquisition.parent / obs["file"]["path"]))
        body = json.loads(checked(downloaded_manifest_ref))
        association[kind] = {"requested_ids": obs["parameters"]["ids"],
                             "returned_id": attempt["file"]["id"],
                             "returned_id_in_original_manifest": any(f["id"] == asset["id"] for f in body["files"]),
                             "manifest_file": downloaded_manifest_ref}
    replay, gamelog = data["replay"], data["gamelog"]
    identity_ok = (replay["gameId"] == game_id == entry["row"]["game_id"] == entry["row"]["gamelog_id"] and
                   row["your_player"] == replay["perspective"] == replay["baseSnapshot"]["viewingAs"])
    report = {"schema": "duels-log-boundary-incident-v1", "generated_at": d.now(), "game_id": game_id,
              "inputs": inputs, "catalog_sha256": d.sha(catalog.read_bytes()),
              "acquisition_manifest_sha256": d.sha(acquisition.read_bytes()),
              "identity_matches": identity_ok, "association": association, "audit": audit(replay, gamelog)}
    extractor_path = d.ROOT / "herramientas/duels_analisis/extraer_replays.py"
    adapter_path = d.ROOT / "herramientas/duels_analisis/reconstruir_lote.py"
    extractor = module(extractor_path, "incident_previous_extractor")
    adapter = module(adapter_path, "incident_analysis_adapter")
    out.mkdir(parents=True, exist_ok=True)
    failures = {}
    with tempfile.TemporaryDirectory(dir=out) as folder:
        for label, path, run in (
            ("previous_extractor", extractor_path, lambda: extractor.extract(resolver_ruta(inputs["replay"]["decoded_json"]["path"]), 1, resolver_ruta(folder), {})),
            ("analysis_adapter", adapter_path, lambda: adapter.reconstruct(row, resolver_ruta(folder), extractor)),
        ):
            try:
                run()
                failures[label] = {"unexpected_success": True}
            except Exception as exc:
                frame = traceback.extract_tb(exc.__traceback__)[-1]
                failures[label] = {"error_type": type(exc).__name__, "function": frame.name,
                                   "line": frame.lineno, "code_sha256": d.sha(path.read_bytes())}
    report["reproduced_failures"] = failures
    # Prueba diagnóstica distinta: aplicar parches sin asociar logs. No convierte
    # el archivo en una partida íntegra ni genera derivados para decisiones.
    state = copy.deepcopy(replay["baseSnapshot"])
    upserts, missing = Counter(), Counter()
    deck_counts = []
    for frame in replay["frames"]:
        for op in frame["patch"]:
            extractor.apply_operation(state, op, upserts, missing)
        deck_counts.append(len(state["myPlayer"]["deckOrder"]) == state["myPlayer"]["deckCount"])
    report["patch_only_diagnostic"] = {"all_frames_applied": True, "deck_counts_consistent": all(deck_counts),
                                       "finished": state.get("status") == "finished", "winner_matches": state.get("winner") == replay["winner"],
                                       "reason_matches": state.get("victoryReason") == replay["victoryReason"],
                                       "integral_reconstruction_certified": False}
    for ref in inputs.values():
        checked(ref)
        checked(ref["decoded_json"])
    d.atomic(out / "diagnostico.json", d.encode(report))
    return report


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--catalogo", type=resolver_ruta, required=True)
    p.add_argument("--adquisicion", type=resolver_ruta, required=True, help="manifest.json de la adquisición")
    p.add_argument("--game-id", required=True)
    p.add_argument("--out", type=resolver_ruta, required=True, help="Directorio privado de diagnóstico")
    args = p.parse_args()
    try:
        report = investigate(args.catalogo, args.adquisicion, args.game_id, args.out)
        anomalies = len(report["audit"]["boundary_violations"])
        print(json.dumps({"boundary_violations": anomalies, "future_prefixes": len(report["audit"]["future_prefixes"]),
                          "identity_matches": report["identity_matches"], "originals_verified": True}))
        return 2 if anomalies or report["audit"]["future_prefixes"] else 0
    except Exception:
        print("Diagnóstico fallido; revisa entradas y hashes. Originales conservados.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
