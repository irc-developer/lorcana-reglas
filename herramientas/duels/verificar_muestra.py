"""Valida adquisiciones localmente con el extractor existente; no hace peticiones HTTP."""
import argparse
from collections import Counter
import gzip
import importlib.util
import json
from pathlib import Path
import sys
import traceback

import duels as d

# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo


def verify(out, extractor_path=None):
    out = resolver_ruta(out)
    manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    extractor_path = extractor_path or d.ROOT / "herramientas/duels_analisis/extraer_replays.py"
    spec = importlib.util.spec_from_file_location("duels_existing_extractor", extractor_path)
    extractor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(extractor)
    report = {"schema_version": 1, "verified_at": d.now(), "account_id": manifest["account"]["id"],
              "manifest_sha256": d.sha((out / "manifest.json").read_bytes()),
              "extractor": str(extractor_path), "extractor_sha256": d.sha(extractor_path.read_bytes()),
              "original_refs_checked": 0, "games": []}

    def read(ref):
        path = (out / ref["path"]).resolve()
        if not path.is_relative_to(out.resolve()):
            raise d.DuelsError("Referencia fuera del directorio de adquisición")
        raw = path.read_bytes()
        if d.sha(raw) != ref["sha256"] or len(raw) != ref["bytes"]:
            raise d.DuelsError("Integridad local fallida")
        report["original_refs_checked"] += 1
        return raw

    for observation in manifest["observations"]:
        read(observation["file"])
    for entry in manifest["games"].values():
        source = entry["row_source"]
        current_page = json.loads(read(source["file"]))
        canonical = current_page["games"][source["index"]]
        if canonical != entry["row"] or d.sha(d.encode(canonical)) != source["row_sha256"]:
            raise d.DuelsError("Fila canónica y procedencia no coinciden")
        if entry["row"]["game_id"] != entry["game_id"] or entry["row"]["your_user_id"] != manifest["account"]["id"]:
            raise d.DuelsError("Identidad de fila inconsistente")
        for source in entry["row_versions"]:
            page = json.loads(read(source["file"]))
            if d.sha(d.encode(page["games"][source["index"]])) != source["row_sha256"]:
                raise d.DuelsError("Procedencia de fila no coincide")
        assets = entry["assets"]
        r = assets["replay"]
        if r["status"] != "downloaded":
            continue
        raw = read(r["original"])
        decoded = gzip.decompress(raw) if raw.startswith(b"\x1f\x8b") else raw
        if decoded != read(r["json"]):
            raise d.DuelsError("JSON descomprimido no coincide con original")
        replay = json.loads(decoded)
        d.validate_asset("replay", replay, entry["row"])
        folder = out / "verification" / d.sha(entry["game_id"].encode())
        folder.mkdir(parents=True, exist_ok=True)
        catalog = {}
        extractor.collect_catalog(replay, catalog)
        # Invocar extract(), no main(): main() exige que todos los archivos sean
        # del mismo encuentro y misma lista, una restricción ajena al importador.
        summary = extractor.extract(out / r["json"]["path"], 1, folder, catalog)
        if entry["row"].get("your_decklist") is not None:
            history_deck = Counter()
            for card in entry["row"]["your_decklist"]:
                history_deck[card["cardId"]] += card["count"]
            if history_deck != Counter(replay["decklist"]):
                raise d.DuelsError("Lista histórica y replay no coinciden")
        result = {"game_id": entry["game_id"], "replay_validation": summary["validation"],
                  "frames": summary["frames"], "replay_logs": summary["logs"],
                  "history_decklist_checked": entry["row"].get("your_decklist") is not None}
        g = assets["gamelog"]
        if g["status"] == "downloaded":
            raw_g = read(g["original"])
            decoded_g = gzip.decompress(raw_g) if raw_g.startswith(b"\x1f\x8b") else raw_g
            if decoded_g != read(g["json"]):
                raise d.DuelsError("Gamelog JSON no coincide con original")
            logs = json.loads(decoded_g)
            if not isinstance(logs, list) or not all(isinstance(x, dict) and "id" in x for x in logs):
                raise d.DuelsError("Esquema del gamelog no reconocido por el verificador de muestra")
            ids = {x["id"] for x in logs}
            replay_ids = {x["id"] for x in replay["logs"]}
            result.update(gamelog_logs=len(logs), shared_log_ids=len(ids & replay_ids),
                          all_replay_logs_in_gamelog=replay_ids <= ids,
                          gamelog_only_event_types=[x.get("type") for x in logs if x["id"] not in replay_ids])
        # Contrastar datos estructurales con la extracción manual anterior, si es
        # la misma partida. No es una prueba de texto idéntico entre exportaciones.
        for previous in (ruta_trabajo("analisis/duels-2026-10-15")).glob("partida-*-resumen.json"):
            old = json.loads(previous.read_text(encoding="utf-8"))
            if old["gameId"] == entry["game_id"]:
                fields = ("gameId", "matchId", "gameNumber", "perspective", "winner", "frames", "logs")
                composition = lambda value: [(x["id"], x["copies"]) for x in value["decklist"]]
                result["previous_extraction_matches"] = (all(old[k] == summary[k] for k in fields) and
                                                         composition(old) == composition(summary))
                if not result["previous_extraction_matches"]:
                    raise d.DuelsError("La adquisición no coincide con la extracción previa")
        report["games"].append(result)
    d.atomic(out / "verification/report.json", d.encode(report))
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=resolver_ruta, default=ruta_trabajo("adquisiciones/duels/sample"))
    args = parser.parse_args()
    try:
        report = verify(args.out)
        print(json.dumps({"verified_games": len(report["games"]), "references_checked": report["original_refs_checked"],
                          "report": str((args.out / "verification/report.json").resolve())}, ensure_ascii=False))
        return 0
    except Exception as exc:
        frame = traceback.extract_tb(exc.__traceback__)[-1]
        detail = str(exc) if isinstance(exc, d.DuelsError) else f"{type(exc).__name__} en {frame.name}:{frame.lineno}"
        print("Verificación fallida: " + detail + ". Originales conservados.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
