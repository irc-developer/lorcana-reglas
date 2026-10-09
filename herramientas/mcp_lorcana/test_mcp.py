"""Pruebas con transporte stdio real y oráculos de fuente. Solo desarrollo/mantenimiento."""
import sys
sys.dont_write_bytecode = True
import asyncio
from contextlib import asynccontextmanager
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from jsonschema import Draft202012Validator
from mcp import Client, StdioServerParameters
from adaptador import Adaptador, REPO, core
from presentacion import expandir_fuentes

HERE = Path(__file__).resolve().parent
SERVER = HERE / "servidor.py"
GROUPS = ("primary_rules", "cards", "official_policy", "official_notes", "special_format", "spanish", "case", "support")


def snapshot(root):
    result = {}
    for directory, dirs, files in os.walk(root):
        # Incluir dependencias y bytecode preparados antes del ensayo; excluir solo Git.
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in files:
            p = Path(directory) / name
            stat = p.stat()
            result[p.relative_to(root).as_posix()] = (stat.st_size, stat.st_mtime_ns, core.digest(p.read_bytes()))
    return result


@asynccontextmanager
async def cliente(root=REPO, db=None, mode="legacy", script=None):
    args = ["-B", "-X", "utf8"] + (["-c", script] if script else [str(SERVER)]) + ["--root", str(root)]
    if db is not None:
        args += ["--db", str(db)]
    params = StdioServerParameters(command=sys.executable, args=args, cwd=str(REPO.parent))
    # cwd distinto, rutas con espacios y handshake legacy usado por clientes existentes.
    async with Client(params, mode=mode, cache=None, read_timeout_seconds=120) as client:
        yield client


def estable(data):
    """Eliminar únicamente mediciones; preservar todas las citas, hashes y limitaciones."""
    if isinstance(data, dict):
        return {k: estable(v) for k, v in data.items() if k not in ("elapsed_ms", "validation_ms")}
    if isinstance(data, list):
        return [estable(v) for v in data]
    return data


class ProtocoloTests(unittest.IsolatedAsyncioTestCase):
    async def test_cr23_fecha_futura_sin_escrituras(self):
        script = f"""import sys
sys.dont_write_bytecode=True
sys.path.insert(0,{str(HERE)!r})
from adaptador import core
from datetime import date
core.fecha_local=lambda: date(2026,10,16)
from servidor import main
main()
"""
        before = snapshot(REPO)
        async with cliente(script=script) as client:
            state = (await client.call_tool("estado_fuentes", {})).structured_content
            self.assertEqual(state["selection"]["version"], "2.3.0")
            for rid in ("1.13", "6.1.4.2", "6.7.6.1", "8.1.2", "8.16"):
                result = await client.call_tool("obtener_regla", {"numero": rid})
                self.assertFalse(result.is_error)
                data = expandir_fuentes(result.structured_content)
                self.assertTrue(data["primary_rules"])
                self.assertTrue(all(p["version"] == "2.3.0" for p in data["primary_rules"]))
            result = await client.call_tool("obtener_regla", {"numero": "7.1.6.1"})
            self.assertEqual(result.structured_content["missing_rule_numbers"], ["7.1.6.1"])
        self.assertEqual(before, snapshot(REPO))

    async def test_descubrimiento_y_20_oraculos_sin_escrituras(self):
        before = snapshot(REPO)
        async with cliente() as client:
            listing = await client.list_tools()
            tools = {t.name: t for t in listing.tools}
            self.assertEqual(set(tools), {"estado_fuentes", "obtener_carta", "obtener_regla", "buscar_evidencia"})
            self.assertEqual(client.server_info.name, "lorcana")
            self.assertIn("sin señal", client.instructions)
            for tool in tools.values():
                self.assertTrue(tool.annotations.read_only_hint)
                self.assertFalse(tool.annotations.destructive_hint)
                self.assertFalse(tool.annotations.open_world_hint)
                Draft202012Validator.check_schema(tool.input_schema)
                Draft202012Validator.check_schema(tool.output_schema)
            self.assertIn("modo", tools["buscar_evidencia"].input_schema["required"])
            state = await client.call_tool("estado_fuentes", {})
            self.assertTrue(state.structured_content["freshness"]["current"])
            for case in core.load_json(core.HERE / ("evaluacion-2.3.json" if core.pick_primary(core.ROOT)[1] == "2.3.0" else "evaluacion.json")):
                with self.subTest(id=case["id"]):
                    args = {"pregunta": case["question"], "modo": "consulta"}
                    if case.get("card"):
                        args["cartas"] = [case["card"]]
                    result = await client.call_tool("buscar_evidencia", args)
                    self.assertFalse(result.is_error, result.content)
                    r = result.structured_content
                    Draft202012Validator(tools["buscar_evidencia"].output_schema).validate(r)
                    self.assertEqual(json.loads(result.content[0].text), r)
                    expanded = expandir_fuentes(r)
                    primary = {p["rule"]: p for p in expanded["primary_rules"] if p["rule"]}
                    for rid in case.get("rules", []):
                        self.assertIn(rid, primary)
                        self.assertEqual(primary[rid]["version"], core.pick_primary(core.ROOT)[1])
                        self.assertEqual(primary[rid]["path"], core.pick_primary(core.ROOT)[0])
                    for rid, text in case.get("decisive", {}).items():
                        self.assertIn(text, primary[rid]["text"])
                    for rid, pages in case.get("pages", {}).items():
                        self.assertEqual(primary[rid]["pages"], pages)
                    if case.get("card"):
                        resolution = next(c for c in r["card_resolution"] if c["requested"] == case["card"])
                        self.assertEqual(resolution["status"], case["card_status"])
                        if resolution["status"] != "exacta":
                            self.assertFalse(resolution["matches"])
                            self.assertIn("insuficiente", r["status"])
                        if case.get("card_text"):
                            self.assertIn(case["card_text"], next(p["text"] for p in r["cards"] if p["id"] == resolution["matches"][0]["id"]))
                    if case.get("warning"):
                        self.assertTrue(any(case["warning"] in w for w in r["warnings"]))
                    if case.get("scope"):
                        self.assertEqual(r["scope"], case["scope"])
                    if case.get("special_path"):
                        self.assertTrue(any(case["special_path"] in p["path"] for p in expanded["special_format"]))
                    if case.get("policy_section"):
                        self.assertTrue(any(p.get("policy_section", "").startswith(case["policy_section"]) for p in r["official_policy"]))
                    if case.get("case_contains"):
                        self.assertTrue(any(case["case_contains"] in p["path"] for p in expanded["case"]))
                    if case.get("excluded_contains"):
                        self.assertTrue(any(case["excluded_contains"] in p["path"] for p in r["excluded_related"]))
                        self.assertFalse(any(case["excluded_contains"] in p["path"] for p in expanded["case"]))
                    for group in GROUPS:
                        for packet in expanded[group]:
                            self.assertTrue(packet["citation_verified"])
                            self.assertEqual(len(packet["source_hash"]), 64)
                            self.assertTrue(packet["authority"])
                            self.assertTrue(packet["local_link"])
        self.assertEqual(before, snapshot(REPO))

    async def test_cli_equivalente_y_modos(self):
        async with cliente() as client:
            requests = [("obtener_carta", {"nombre": "Minnie Mouse - Practical Traveler"}, ["carta", "Minnie Mouse - Practical Traveler"]),
                        ("obtener_regla", {"numero": "6.1.6"}, ["regla", "6.1.6"]),
                        ("buscar_evidencia", {"pregunta": "consulta: CR 1.12.2", "modo": "consulta"}, ["consultar", "consulta: CR 1.12.2"]),
                        ("buscar_evidencia", {"pregunta": "documenta: CR 1.12.2", "modo": "documenta"}, ["consultar", "documenta: CR 1.12.2"])]
            for name, args, cli_args in requests:
                r = (await client.call_tool(name, dict(args, formato="completo"))).structured_content
                cli = await asyncio.to_thread(subprocess.run, [sys.executable, "-B", "-X", "utf8", str(core.HERE / "consulta.py"), *cli_args, "--json"], capture_output=True, text=True, encoding="utf-8")
                self.assertEqual(cli.returncode, 0, cli.stderr)
                expected = json.loads(cli.stdout)
                if name.startswith("obtener_"):
                    expected.update(mode="auxiliar", editorial_required=None)
                self.assertEqual(estable(r), estable(expected))
            ordinary = await client.call_tool("buscar_evidencia", {"pregunta": "CR 1.12.2", "modo": "documenta"})
            self.assertTrue(ordinary.structured_content["editorial_required"])
            missing = await client.call_tool("obtener_regla", {"numero": "1.8.1.5"})
            self.assertFalse(missing.is_error)
            self.assertEqual(missing.structured_content["missing_rule_numbers"], ["1.8.1.5"])

    async def test_entradas_invalidas_y_recuperacion_del_proceso(self):
        async with cliente() as client:
            bad = [("buscar_evidencia", {"pregunta": "CR 1.12.2"}),
                   ("buscar_evidencia", {"pregunta": "documenta: robo", "modo": "consulta"}),
                   ("buscar_evidencia", {"pregunta": "actualiza:", "modo": "consulta"}),
                   ("buscar_evidencia", {"pregunta": "consulta: documenta: robo", "modo": "consulta"}),
                   ("buscar_evidencia", {"pregunta": " ", "modo": "consulta"}),
                   ("obtener_regla", {"numero": "../../secretos"}),
                   ("obtener_carta", {"nombre": ""}),
                   ("estado_fuentes", {"root": "C:/"}),
                   ("inventada", {})]
            for limit in (0, 13, True, "2"):
                bad.append(("buscar_evidencia", {"pregunta": "robo", "modo": "consulta", "limite": limit}))
            bad.append(("obtener_regla", {"numero": "8.8", "formato": "resumido"}))
            for name, args in bad:
                with self.subTest(name=name, args=args):
                    result = await client.call_tool(name, args)
                    self.assertTrue(result.is_error)
                    self.assertTrue(json.loads(result.content[0].text)["no_ruling"])
            good = await client.call_tool("obtener_regla", {"numero": "1.12.2"})
            self.assertFalse(good.is_error)

    async def test_protocolo_moderno_y_llamadas_concurrentes(self):
        async with cliente(mode="auto") as client:
            results = await asyncio.gather(*(client.call_tool("obtener_regla", {"numero": n}) for n in ("1.12.2", "6.1.6", "8.8.3")))
            self.assertTrue(all(not r.is_error for r in results))
            self.assertTrue(all(r.structured_content["evidence_only"] for r in results))

    async def test_fichas_repetidas_y_campos_ausentes(self):
        async with cliente() as client:
            r = expandir_fuentes((await client.call_tool("obtener_carta", {"nombre": "Cinderella - Gentle and Kind"})).structured_content)
            self.assertEqual(r["card_resolution"][0]["status"], "multiples_fichas_comprobar")
            self.assertEqual({p["path"] for p in r["cards"]}, {"02. Listado de Cartas/Set 1 - The First Chapter.md", "02. Listado de Cartas/Set 9 - Fabled.md"})
            self.assertIn("insuficiente", r["status"])
            r = (await client.call_tool("obtener_carta", {"nombre": "Thomas - Wide-Eyed Recruit"})).structured_content
            p = r["cards"][0]
            self.assertNotIn("Fuerza", p["documented_fields"])
            self.assertFalse(p["ability_section_present"])
            self.assertEqual(p["coverage"], "completitud_no_acreditada")
            self.assertIn("**Voluntad:** 4", p["text"])

    async def test_lectura_conserva_evidencia_y_reduce_los_dos_casos_auditados(self):
        before = snapshot(REPO)
        requests = [
            ("buscar_evidencia", {"pregunta": 'resist previene del daño puesto por acciones que ponen "put" en su texto?', "modo": "consulta"}),
            ("buscar_evidencia", {"pregunta": 'el resist previene el daño de acciones que digan "put counter damage"?', "modo": "consulta", "reglas": ["9.2"]}),
            ("obtener_regla", {"numero": "8.8"}),
            ("obtener_carta", {"nombre": "Cinderella - Gentle and Kind"}),
            ("obtener_carta", {"nombre": "Thomas - Wide-Eyed Recruit"}),
            ("obtener_regla", {"numero": "1.8.1.5"}),
            ("estado_fuentes", {}),
        ]
        async with cliente() as client:
            for name, args in requests:
                with self.subTest(name=name, args=args):
                    full = (await client.call_tool(name, dict(args, formato="completo"))).structured_content
                    compact = await client.call_tool(name, args)
                    self.assertFalse(compact.is_error)
                    r = compact.structured_content
                    self.assertEqual(r["delivery"]["format"], "lectura")
                    self.assertTrue(r["delivery"]["complete_texts"])
                    self.assertEqual(json.loads(compact.content[0].text), r)
                    expanded = expandir_fuentes(r)
                    for group in GROUPS:
                        # Incluye textos, condiciones, referencias, enlaces, hashes y limitaciones.
                        self.assertEqual(expanded.get(group), full.get(group))
                    for field in ("warnings", "card_resolution", "missing_rule_numbers", "excluded_related", "mode", "editorial_required"):
                        self.assertEqual(r.get(field), full.get(field))
                    self.assertEqual(r["freshness"]["changes"], full["freshness"]["changes"])
                    self.assertEqual(r["selection"], full["selection"])
                    self.assertEqual(r["freshness"]["selection"]["excluded_count"], len(full["freshness"]["selection"]["excluded"]))
                    old_chars = len(json.dumps(full, ensure_ascii=False))
                    self.assertLess(len(compact.content[0].text), old_chars)
                    if name == "buscar_evidencia":
                        self.assertLess(len(compact.content[0].text), old_chars * .8)
        self.assertEqual(before, snapshot(REPO))


class FixturesTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="test-mcp-", dir=HERE / ".cache")
        self.root = Path(self.temp.name).resolve()
        assert self.root.is_relative_to((HERE / ".cache").resolve())
        for rel in core.CONTROL + ["Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf",
                                "Documentacion Oficial/CRUpdate_EN_Oct-2026.pdf",
                                   "02. Listado de Cartas/Set 14 - Hyperia City.md",
                                   "01. Reglas/1. Principios generales/1.12 Robo (Drawing).md"]:
            dest = self.root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / rel, dest)
        self.db = self.root / "cache/indice.sqlite"
        core.update(self.root, self.db)

    def tearDown(self):
        self.temp.cleanup()

    async def solo_lectura(self, client, name, args):
        before = snapshot(self.root)
        r = await client.call_tool(name, args)
        self.assertEqual(before, snapshot(self.root))
        return r

    async def test_indice_ausente_y_obsoleto_sin_cache(self):
        missing = self.root / "sin-cache/indice.sqlite"
        async with cliente(self.root, missing) as client:
            r = await self.solo_lectura(client, "obtener_regla", {"numero": "1.12.2"})
            self.assertFalse(r.is_error)
            self.assertFalse(r.structured_content["freshness"]["usable"])
        path = self.root / "01. Reglas/1. Principios generales/1.12 Robo (Drawing).md"
        stat = path.stat()
        path.write_text(path.read_text(encoding="utf-8").replace("una en una", "UNA EN UNA"), encoding="utf-8")
        os.utime(path, ns=(stat.st_atime_ns, stat.st_mtime_ns))
        async with cliente(self.root, self.db) as client:
            r = await self.solo_lectura(client, "buscar_evidencia", {"pregunta": "robar cartas una en una", "modo": "consulta"})
            self.assertFalse(r.is_error)
            self.assertFalse(r.structured_content["freshness"]["current"])
            self.assertTrue(any("UNA EN UNA" in p["text"] for p in r.structured_content["spanish"]))

    async def test_sustitucion_atomica_entre_llamadas_y_actualiza_separado(self):
        async with cliente(self.root, self.db) as client:
            r = await self.solo_lectura(client, "obtener_regla", {"numero": "1.12.2"})
            self.assertTrue(r.structured_content["freshness"]["current"])
            path = self.root / "09. Recursos/prueba.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Prueba\nCambio de inventario durante un servidor abierto.\n", encoding="utf-8")
            stale = await self.solo_lectura(client, "estado_fuentes", {})
            self.assertFalse(stale.structured_content["freshness"]["current"])
            # Vía de mantenimiento CLI, nunca herramienta MCP.
            run = subprocess.run([sys.executable, "-B", "-X", "utf8", str(core.HERE / "consulta.py"), "--root", str(self.root), "--db", str(self.db), "actualizar", "--json"], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertIn("09. Recursos/prueba.md", json.loads(run.stdout)["changes"]["added"])
            current = await self.solo_lectura(client, "estado_fuentes", {})
            self.assertTrue(current.structured_content["freshness"]["current"])

    async def test_pdf_corrupto_y_seleccion_discrepante_fallan(self):
        async with cliente(self.root, self.db) as client:
            pdf = self.root / "Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf"
            data = pdf.read_bytes()
            pdf.write_bytes(b"not a readable PDF")
            r = await self.solo_lectura(client, "obtener_regla", {"numero": "1.12.2"})
            self.assertTrue(r.is_error)
            self.assertTrue(json.loads(r.content[0].text)["no_ruling"])
            pdf.write_bytes(data)
            pointer = self.root / core.CONTROL[0]
            pointer.write_text(pointer.read_text(encoding="utf-8").replace("2.2.0", "8.9.0"), encoding="utf-8")
            r = await self.solo_lectura(client, "estado_fuentes", {})
            self.assertTrue(r.is_error)

    async def test_cambio_durante_consulta_rechaza_evidencia(self):
        path = self.root / "01. Reglas/1. Principios generales/1.12 Robo (Drawing).md"
        # Inyección solo en el proceso de ensayo; el servidor de producción no tiene interruptores de prueba.
        script = f"""import sys
sys.dont_write_bytecode=True
sys.path.insert(0,{str(HERE)!r})
from adaptador import core
from pathlib import Path
original=core.verify_fragments
def changed(*args, **kwargs):
    original(*args, **kwargs)
    p=Path({str(path)!r})
    p.write_bytes(p.read_bytes()+b'\\nCambio concurrente de prueba.\\n')
core.verify_fragments=changed
from servidor import main
main()
"""
        async with cliente(self.root, self.db, script=script) as client:
            result = await client.call_tool("obtener_regla", {"numero": "1.12.2"})
            self.assertTrue(result.is_error)
            self.assertIn("Fuentes cambiaron", json.loads(result.content[0].text)["error"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
