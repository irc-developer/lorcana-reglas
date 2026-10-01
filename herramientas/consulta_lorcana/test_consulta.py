"""Oráculos de fuente primaria + fallos de mantenimiento. Ejecutar fuera del modo consulta."""
import sys
sys.dont_write_bytecode = True
from contextlib import closing
import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import core as x

DB = x.HERE / ".cache/indice.sqlite"


def snapshot(root):
    return {p.relative_to(root).as_posix(): (p.stat().st_size, p.stat().st_mtime_ns, x.digest(p.read_bytes()))
            for p in root.rglob("*") if p.is_file() and ".git" not in p.parts}


class CorpusTests(unittest.TestCase):
    def test_release_notes_recovered_as_rules_support(self):
        r = x.query(x.ROOT, DB, "consulta: Woody - Town Sheriff puede cantar canciones")
        self.assertTrue(r["official_notes"])
        note = r["official_notes"][0]
        self.assertEqual(note["authority"], "notas_oficiales")
        self.assertIn("Woody", note["text"])
        self.assertTrue(note["citation_verified"])
        self.assertTrue(all(p["path"].startswith("02. Listado de Cartas/") for p in r["cards"]))

    def test_missing_exact_rule_is_insufficient(self):
        r = x.query(x.ROOT, DB, "consulta: CR 1.8.1.5", rule_numbers=["1.8.1.5"])
        self.assertEqual(r["missing_rule_numbers"], ["1.8.1.5"])
        self.assertIn("insuficiente", r["status"])
        self.assertFalse(any(p["rule"] == "1.8.1.5" for p in r["primary_rules"]))

    def test_20_verified_questions(self):
        self.assertTrue(x.freshness(x.ROOT, DB)["current"], "Ejecuta actualizar antes de las pruebas")
        for case in x.load_json(x.HERE / "evaluacion.json"):
            with self.subTest(id=case["id"]):
                r = x.query(x.ROOT, DB, case["question"], card_names=[case["card"]] if case.get("card") else [])
                primary = {p["rule"]: p for p in r["primary_rules"] if p["rule"]}
                for rid in case.get("rules", []):
                    self.assertIn(rid, primary)
                    self.assertEqual(primary[rid]["version"], "2.2.0")
                    self.assertEqual(primary[rid]["path"], "Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf")
                for rid, text in case.get("decisive", {}).items():
                    self.assertIn(text, primary[rid]["text"])
                for rid, pages in case.get("pages", {}).items():
                    self.assertEqual(primary[rid]["pages"], pages)
                if "card" in case:
                    res = next(z for z in r["card_resolution"] if z["requested"] == case["card"])
                    self.assertEqual(res["status"], case["card_status"])
                    if res["status"] != "exacta":
                        self.assertFalse(res["matches"])
                        self.assertIn("insuficiente", r["status"])
                    if case.get("card_text"):
                        self.assertIn(case["card_text"], next(p["text"] for p in r["cards"] if p["id"] == res["matches"][0]["id"]))
                if case.get("warning"):
                    self.assertTrue(any(case["warning"] in w for w in r["warnings"]))
                if case.get("case_contains"):
                    self.assertTrue(any(case["case_contains"] in p["path"] for p in r["case"]))
                if case.get("excluded_contains"):
                    self.assertTrue(any(case["excluded_contains"] in p["path"] for p in r["excluded_related"]))
                    self.assertFalse(any(case["excluded_contains"] in p["path"] for p in r["case"]))
                if case.get("special_path"):
                    self.assertTrue(any(case["special_path"] in p["path"] for p in r["special_format"]))
                if case.get("policy_section"):
                    self.assertTrue(any(p.get("policy_section", "").startswith(case["policy_section"]) for p in r["official_policy"]))
                if case.get("scope"):
                    self.assertEqual(r["scope"], case["scope"])
                for group in ("primary_rules", "cards", "spanish", "case", "official_policy", "special_format"):
                    self.assertTrue(all(p["citation_verified"] for p in r[group]))

    def test_cli_readonly_all_commands(self):
        before = snapshot(x.ROOT)
        for args in (["estado"], ["regla", "6.1.6"], ["carta", "Wasabi - Called into Battle"],
                     ["consultar", "consulta: ¿Si robo tres cartas, son tres robos?"]):
            run = subprocess.run([sys.executable, "-B", "-X", "utf8", str(x.HERE / "consulta.py"), *args, "--json"], cwd=x.ROOT, capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertIsInstance(json.loads(run.stdout), dict)
        self.assertEqual(before, snapshot(x.ROOT))

    def test_symbols_and_order_against_pdf(self):
        import fitz
        with fitz.open(x.ROOT / "Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf") as doc:
            # Oráculo independiente: los identificadores que aparecen al inicio de línea del PDF.
            body = "\n".join(p.get_text(sort=True) for p in list(doc)[2:45])
            expected = set(__import__("re").findall(r"(?m)^\s*(\d+(?:\.\d+){2,})\.\s", body))
        with closing(x.ro_connection(DB)) as c:
            actual = {r[0] for r in c.execute("select rule from chunks where kind='cr' and rule is not null")}
            self.assertTrue(expected <= actual, expected - actual)
            ink = x.exact_rules(c, "4.3.6")[0]
            strength = x.exact_rules(c, "6.5.1.1")[0]
            self.assertIn("{I}", ink["text"])
            self.assertIn("{E}", strength["text"])
            self.assertIn("{S}", strength["text"])
            self.assertIn('"', ink["raw_text"])
            self.assertNotIn("disneylorcana.com", ink["text"])
            glossary_titles = {json.loads(r[0])["title"] for r in c.execute("select payload from chunks where rule is null and kind='cr'")}
            self.assertIn("Glosario CR · action, game", glossary_titles)
            self.assertIn("Glosario CR · action, turn", glossary_titles)
            cards = c.execute("select payload from chunks where kind='card'").fetchall()
            self.assertTrue(cards)
            self.assertTrue(all(json.loads(r[0])["path"].startswith("02. Listado de Cartas/") for r in cards))
            coconut = [json.loads(r[0]) for r in c.execute("select payload from chunks where kind='special'")]
            self.assertTrue(any("gain lore equal to her {L}" in p["text"] for p in coconut))
            self.assertTrue(any('the {E} abilities' in p["text"] for p in coconut))
            release = [json.loads(r[0]) for r in c.execute("select payload from chunks where kind='release'")]
            self.assertTrue(any("have 2 {L}" in p["text"] for p in release))
            self.assertTrue(any("with 2 {S}" in p["text"] for p in release))

    def test_forbidden_sources(self):
        with closing(x.ro_connection(DB)) as c:
            paths = [r[0] for r in c.execute("select path from sources where kind not in ('control','excluded')")]
            self.assertFalse(any(p.startswith(("20.", "02. Habilidades", "Unifica", "01.1.a", "099.")) for p in paths))
            excluded = x.metadata(c)["selection"]["excluded"]
            self.assertGreater(len(excluded), 25)
            self.assertFalse(any(p["path"] in paths for p in excluded))


class MaintenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = x.HERE / ".cache"
        cls.temp = tempfile.TemporaryDirectory(prefix="test-corpus-", dir=base)
        cls.root = Path(cls.temp.name).resolve()
        assert cls.root.is_relative_to(base.resolve())
        for rel in x.CONTROL + ["Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf",
                                "02. Listado de Cartas/Set 14 - Hyperia City.md",
                                "01. Reglas/1. Principios generales/1.12 Robo (Drawing).md"]:
            target = cls.root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(x.ROOT / rel, target)
        cls.db = cls.root / "cache/indice.sqlite"
        x.update(cls.root, cls.db)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_01_stale_same_mtime_readonly_current_text(self):
        path = self.root / "01. Reglas/1. Principios generales/1.12 Robo (Drawing).md"
        original, stat = path.read_bytes(), path.stat()
        try:
            text = original.decode("utf-8").replace("una en una", "UNA EN UNA")
            path.write_text(text, encoding="utf-8")
            os.utime(path, ns=(stat.st_atime_ns, stat.st_mtime_ns))
            self.assertFalse(x.freshness(self.root, self.db)["current"])
            before = snapshot(self.root)
            r = x.query(self.root, self.db, "robar cartas una en una")
            self.assertFalse(r["freshness"]["current"])
            self.assertTrue(any("UNA EN UNA" in p["text"] for p in r["spanish"]))
            self.assertEqual(before, snapshot(self.root))
        finally:
            path.write_bytes(original)

    def test_02_incremental_add_modify_rename_remove(self):
        path = self.root / "09. Recursos/prueba.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# Prueba\nEvidencia de prueba para robar.\n", encoding="utf-8")
        added = x.update(self.root, self.db)
        self.assertIn("09. Recursos/prueba.md", added["changes"]["added"])
        self.assertEqual(added["update"]["parsed"], 1)
        with closing(x.ro_connection(self.db)) as c:
            sid = c.execute("select id from sources where path=?", ("09. Recursos/prueba.md",)).fetchone()[0]
        moved = path.with_name("renombrada.md")
        path.rename(moved)
        renamed = x.update(self.root, self.db)
        self.assertEqual(renamed["update"]["parsed"], 0)
        self.assertEqual(len(renamed["changes"]["renamed"]), 1)
        with closing(x.ro_connection(self.db)) as c:
            self.assertEqual(c.execute("select id from sources where path=?", ("09. Recursos/renombrada.md",)).fetchone()[0], sid)
        moved.write_text("# Prueba\nOtra evidencia de robar.\n", encoding="utf-8")
        self.assertEqual(x.update(self.root, self.db)["update"]["parsed"], 1)
        moved.unlink()
        removed = x.update(self.root, self.db)
        self.assertIn("09. Recursos/renombrada.md", removed["changes"]["removed"])

    def test_03_failed_update_preserves_index_and_declares_failure(self):
        path = self.root / "Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf"
        original = path.read_bytes()
        before_hash = x.digest(self.db.read_bytes())
        try:
            path.write_bytes(b"not a readable PDF")
            with self.assertRaises(Exception):
                x.update(self.root, self.db)
            self.assertEqual(before_hash, x.digest(self.db.read_bytes()))
            with self.assertRaises(Exception):
                x.query(self.root, self.db, "robo")
            self.assertTrue((self.db.parent / "last_failure.json").is_file())
        finally:
            path.write_bytes(original)
        state = x.freshness(self.root, self.db)
        self.assertTrue(state["current"])
        self.assertTrue(state["last_failed_update"]["preserved_last_index"])

    def test_04_fallback_without_fts(self):
        db = self.root / "fallback/indice.sqlite"
        result = x.update(self.root, db, force_scan=True)
        self.assertEqual(result["update"]["backend"], "scan")
        r = x.query(self.root, db, "draw three cards")
        self.assertIn("1.12.2", [p["rule"] for p in r["primary_rules"]])
        self.assertTrue(all(p["citation_verified"] for p in r["primary_rules"]))

    def test_05_future_pdf_filename_without_code_change(self):
        # Renombrar un PDF con el mismo interior y actualizar ambos punteros basta.
        old = "Comprehensive-Rules_2.2.0-EN.pdf"
        new = "CR-current-renamed.pdf"
        pdf = self.root / "Documentacion Oficial" / old
        target = pdf.with_name(new)
        controls = [(self.root / r, (self.root / r).read_bytes()) for r in x.CONTROL]
        try:
            pdf.rename(target)
            for p, data in controls:
                p.write_text(data.decode("utf-8").replace(old, new), encoding="utf-8")
            result = x.update(self.root, self.db)
            self.assertEqual(result["selection"]["primary"], "Documentacion Oficial/" + new)
            r = x.query(self.root, self.db, "CR 1.12.2")
            self.assertTrue(all(p["path"].endswith(new) for p in r["primary_rules"]))
        finally:
            target.rename(pdf)
            for p, data in controls:
                p.write_bytes(data)
            x.update(self.root, self.db)

    def test_06_missing_index_readonly(self):
        db = self.root / "does-not-exist/indice.sqlite"
        before = snapshot(self.root)
        r = x.query(self.root, db, "consulta: CR 1.12.2")
        self.assertFalse(r["freshness"]["usable"])
        self.assertIn("1.12.2", [p["rule"] for p in r["primary_rules"]])
        self.assertEqual(before, snapshot(self.root))

    def test_07_selection_disagreement_is_error(self):
        path = self.root / x.CONTROL[0]
        data = path.read_bytes()
        try:
            path.write_text(data.decode("utf-8").replace("2.2.0", "8.9.0"), encoding="utf-8")
            with self.assertRaises(ValueError):
                x.inventory(self.root)
        finally:
            path.write_bytes(data)

    def test_08_modes_in_fresh_process(self):
        for text, mode in [("consulta: x", "consulta"), ("documenta: x", "documenta"), ("actualiza:", "actualiza")]:
            self.assertEqual(x.mode_of(text)[0], mode)
        self.assertEqual(x.mode_of("pregunta ordinaria")[0], "documenta")
        self.assertEqual(x.mode_of("pregunta con invocación", explicit=True)[0], "consulta")
        run = subprocess.run([sys.executable, "-B", "-X", "utf8", str(x.HERE / "consulta.py"), "--root", str(self.root), "--db", str(self.db), "consultar", "documenta: CR 1.12.2", "--json"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertTrue(json.loads(run.stdout)["editorial_required"])
        self.assertEqual(x.query(self.root,self.db,"actualiza:")["action_required"], "Ejecutar actualizar; consultar nunca escribe.")

    def test_09_unknown_pdf_symbol_encoding_fails_closed(self):
        source = self.root / "Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf"
        target = self.root / "unverified-symbols.pdf"
        try:
            target.write_bytes(source.read_bytes() + b"\n")
            with self.assertRaisesRegex(ValueError, "Símbolos sin perfil verificado"):
                x.extract_pdf(target)
        finally:
            target.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
