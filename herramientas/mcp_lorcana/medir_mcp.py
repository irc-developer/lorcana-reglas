"""Medición reproducible de desarrollo; nunca ejecutar durante consulta:."""
import sys
sys.dont_write_bytecode = True
import argparse
import json
from pathlib import Path
import statistics
import time

import anyio
from test_mcp import cliente, snapshot
from adaptador import REPO, core
from servidor import VERSION
from presentacion import GROUPS, expandir_fuentes


def resumen(values):
    return {"n": len(values), "min_ms": round(min(values), 3),
            "p50_ms": round(statistics.median(values), 3),
            "p95_ms": round(statistics.quantiles(values, n=100, method="inclusive")[94], 3),
            "max_ms": round(max(values), 3)}


async def medir():
    before = snapshot(REPO)
    starts, cold = [], []
    for _ in range(3):
        start = time.perf_counter()
        async with cliente() as client:
            await client.list_tools()
            starts.append((time.perf_counter() - start) * 1000)
            start = time.perf_counter()
            result = await client.call_tool("obtener_regla", {"numero": "1.12.2"})
            assert not result.is_error
            cold.append((time.perf_counter() - start) * 1000)
    samples = []
    async with cliente() as client:
        for case in core.load_json(core.HERE / "evaluacion.json"):
            args = {"pregunta": case["question"], "modo": "consulta"}
            if case.get("card"):
                args["cartas"] = [case["card"]]
            full_result = await client.call_tool("buscar_evidencia", dict(args, formato="completo"))
            assert not full_result.is_error
            full = full_result.structured_content
            full_chars = len(full_result.content[0].text)
            for repeat in range(3):
                start = time.perf_counter()
                result = await client.call_tool("buscar_evidencia", args)
                ms = (time.perf_counter() - start) * 1000
                assert not result.is_error
                expanded = expandir_fuentes(result.structured_content)
                assert all(expanded[group] == full[group] for group in GROUPS), "La vista alteró evidencia"
                samples.append({"id": case["id"], "repeat": repeat, "roundtrip_ms": round(ms, 3),
                                "core_ms": result.structured_content["elapsed_ms"],
                                "envelope_bytes": len(result.model_dump_json(by_alias=True).encode("utf-8")),
                                "text_chars": len(result.content[0].text), "full_text_chars": full_chars,
                                "text_reduction_percent": round(100 * (1 - len(result.content[0].text) / full_chars), 2)})
        audit = []
        for args in (
            {"pregunta": 'resist previene del daño puesto por acciones que ponen "put" en su texto?', "modo": "consulta"},
            {"pregunta": 'el resist previene el daño de acciones que digan "put counter damage"?', "modo": "consulta", "reglas": ["9.2"]},
        ):
            full = await client.call_tool("buscar_evidencia", dict(args, formato="completo"))
            compact = await client.call_tool("buscar_evidencia", args)
            assert not full.is_error and not compact.is_error
            assert all(expandir_fuentes(compact.structured_content)[g] == full.structured_content[g] for g in GROUPS)
            audit.append({"question": args["pregunta"], "rules_requested": args.get("reglas", []),
                          "current": compact.structured_content["freshness"]["current"],
                          "full_text_chars": len(full.content[0].text), "read_text_chars": len(compact.content[0].text),
                          "reduction_percent": round(100 * (1 - len(compact.content[0].text) / len(full.content[0].text)), 2),
                          "all_evidence_preserved": True})
    assert before == snapshot(REPO), "Las operaciones de lectura modificaron archivos"
    return {"date": "2026-09-30", "server_version": VERSION, "python": sys.version.split()[0],
            "sdk": __import__("importlib.metadata", fromlist=["version"]).version("mcp"),
            "protocol": "legacy stdio", "readonly_verified": True,
            "note": "Proceso nuevo sin vaciar caché del SO. Overhead: roundtrip menos tiempo del motor; incluye adaptación, presentación, serialización, transporte y cliente. 60 lecturas, 20 llamadas completas para comparar textos y 4 para reproducir los casos auditados. Sin modelo ni red; no mide el tiempo del chat.",
            "startup": resumen(starts), "first_call_new_process": resumen(cold),
            "roundtrip": resumen([s["roundtrip_ms"] for s in samples]),
            "core": resumen([s["core_ms"] for s in samples]),
            "overhead": resumen([s["roundtrip_ms"]-s["core_ms"] for s in samples]),
            "max_envelope_bytes": max(s["envelope_bytes"] for s in samples),
            "max_text_chars": max(s["text_chars"] for s in samples),
            "text_reduction_percent": {"min": min(s["text_reduction_percent"] for s in samples),
                                       "median": statistics.median(s["text_reduction_percent"] for s in samples)},
            "audit_cases": audit, "samples": samples}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--salida", type=Path, help="Informe; se escribe después de comprobar la lectura.")
    args = parser.parse_args()
    result = anyio.run(medir)
    if args.salida:
        args.salida.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "samples"}, ensure_ascii=False, indent=2))
