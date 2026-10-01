"""Mediciones separadas de redacción/transporte. Es mantenimiento: escribe un informe."""
import sys
sys.dont_write_bytecode = True
import argparse
from contextlib import closing
from datetime import datetime, timezone
import json
import math
import platform
import statistics
import subprocess
import time
from pathlib import Path
import core as x


def stats(values):
    ordered = sorted(values)
    return {"n": len(values), "median_ms": round(statistics.median(values), 3),
            "p95_ms": round(ordered[math.ceil(.95 * len(ordered)) - 1], 3),
            "min_ms": round(ordered[0], 3), "max_ms": round(ordered[-1], 3)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vueltas", type=int, default=3)
    parser.add_argument("--salida", type=Path, default=x.HERE / ".cache/mediciones.json")
    args = parser.parse_args()
    db = x.HERE / ".cache/indice.sqlite"
    state = x.freshness(x.ROOT, db)
    if not state["current"]:
        raise SystemExit("Ejecuta actualizar antes de medir: no mezclar fallback desactualizado con búsquedas calientes.")
    cases = x.load_json(x.HERE / "evaluacion.json")
    cold, warm, check, cli = [], [], [], []
    for case in cases:
        command = [sys.executable, "-X", "utf8", str(x.HERE / "consulta.py"), "consultar", case["question"], "--json"]
        if case.get("card"):
            command.extend(["--carta", case["card"]])
        start = time.perf_counter()
        result = subprocess.run(command, cwd=x.ROOT, capture_output=True, text=True, encoding="utf-8", check=True)
        cli.append((time.perf_counter() - start) * 1000)
        cold.append(json.loads(result.stdout)["elapsed_ms"])
    print("Frío de proceso completado.", flush=True)
    for _ in range(max(1, args.vueltas)):
        for case in cases:
            r = x.query(x.ROOT, db, case["question"], card_names=[case["card"]] if case.get("card") else [])
            warm.append(r["elapsed_ms"])
            check.append(r["freshness"]["validation_ms"])
    with closing(x.ro_connection(db)) as c:
        coverage = {r[0]: r[1] for r in c.execute("select kind,count(*) from chunks group by kind")}
        rules_qa = json.loads(c.execute("select meta from sources where kind='cr'").fetchone()[0])["extraction"]
        sets = [{"path": r["path"], "coverage": json.loads(r["meta"])["coverage"],
                 "cards": c.execute("select count(*) from chunks where source_id=?",(r["id"],)).fetchone()[0]}
                for r in c.execute("select * from sources where kind='card'")]
    report = {"measured_at_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version,
              "machine": platform.platform(), "backend": state["backend"],
              "cold_process_retrieval": stats(cold), "cold_cli_including_start_and_json": stats(cli),
              "warm_same_process_retrieval": stats(warm), "initial_full_hash_validation": stats(check),
              "definition": "Frío = proceso Python nuevo por pregunta, sin purgar caché del SO. Caliente = mismo proceso, índice persistente y conexión nueva por consulta. Ambos incluyen hashing completo inicial/final y relectura de citas; no incluyen razonamiento, redacción ni transporte remoto.",
              "coverage": coverage, "sets": sets, "pdf_qa": rules_qa,
              "excluded_sources": len(state["selection"]["excluded"]),
              "source_count": state["source_count"], "questions": [c["id"] for c in cases]}
    args.salida.parent.mkdir(parents=True, exist_ok=True)
    args.salida.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("cold_process_retrieval", "cold_cli_including_start_and_json", "warm_same_process_retrieval", "initial_full_hash_validation", "coverage")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
