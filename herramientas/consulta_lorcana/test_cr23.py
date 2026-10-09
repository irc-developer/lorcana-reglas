"""Transición fechada, glosarios y extracción de ambos originales oficiales."""
import sys
sys.dont_write_bytecode = True
from contextlib import closing
from datetime import date
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import core as x


class CR23Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.previous = x.load_json(x.HERE / "fuentes.json")["primary_transition"]
        cls.pdfs = {}
        for key in ("previous", "published"):
            pages, qa = x.extract_pdf(x.ROOT / cls.previous[key + "_path"])
            cls.pdfs[key] = (pages, qa, {r["rule"]: r for r in x.cr_chunks(pages)}, x.glossary_chunks(pages))

    def test_limite_de_fecha_y_hashes(self):
        for day, key in ((15, "previous"), (16, "published"), (17, "published")):
            with self.subTest(day=day), patch.object(x, "fecha_local", return_value=date(2026, 10, day)):
                self.assertEqual(x.pick_primary(x.ROOT), (self.previous[key + "_path"], self.previous[key + "_version"]))

    def test_simbolos_identidad_y_glosarios_completos(self):
        for key, expected in (("previous", 55), ("published", 56)):
            pages, qa, rules, glossary = self.pdfs[key]
            self.assertEqual(qa["pages"], expected)
            self.assertIn("{INKWELL}", rules["5.2.3"]["text"])
            self.assertNotIn("{M}", rules["5.2.3"]["text"])
            terms = {r["glossary_term"] for r in glossary}
            self.assertTrue({"action, turn", "Set step", "move cost", "Willpower", "inkwell symbol"} <= terms)
            self.assertFalse(any("Update Summary" in r["text"] for r in glossary))
        self.assertTrue({"counter", "ink drop"} <= {g["glossary_term"] for g in self.pdfs["published"][3]})

    def test_lectura_futura_recupera_nuevas_reglas_y_excluye_historicos(self):
        with patch.object(x, "fecha_local", return_value=date(2026, 10, 16)), tempfile.TemporaryDirectory(dir=x.ROOT / ".codex_tmp") as tmp:
            db = Path(tmp) / "futuro.sqlite"
            x.update(x.ROOT, db)
            with closing(x.ro_connection(db)) as c:
                for rid in ("1.13", "6.1.4.2", "6.7.6.1", "8.1.2", "8.16"):
                    rows = x.exact_rules(c, rid)
                    self.assertTrue(rows, rid)
                    self.assertTrue(all(r["path"].endswith("CRUpdate_EN_Oct-2026.pdf") for r in rows))
                self.assertEqual(x.exact_rules(c, "7.1.6.1"), [])
                cases = {r[0] for r in c.execute("select path from sources where kind not in ('control','excluded')")}
                self.assertFalse(any("CR 2.2 -" in r for r in cases))
            before = {p: (p.stat().st_mtime_ns, x.digest(p.read_bytes())) for p in Path(tmp).rglob("*") if p.is_file()}
            result = x.query(x.ROOT, db, "consulta: CR 8.16", rule_numbers=["8.16"])
            self.assertEqual(result["selection"]["version"], "2.3.0")
            self.assertEqual(before, {p: (p.stat().st_mtime_ns, x.digest(p.read_bytes())) for p in Path(tmp).rglob("*") if p.is_file()})

    def test_anticipos_no_son_evidencia_vigente(self):
        rel = "01. Reglas/8. Palabras clave (Keywords)/8.16. Aventurero (Adventurous).md"
        with patch.object(x, "fecha_local", return_value=date(2026, 10, 15)):
            entries, selection = x.inventory(x.ROOT)
            self.assertEqual(selection["version"], "2.2.0")
            self.assertEqual(entries[rel]["kind"], "excluded")
        with patch.object(x, "fecha_local", return_value=date(2026, 10, 16)):
            entries, selection = x.inventory(x.ROOT)
            self.assertEqual(entries[rel]["kind"], "local")


if __name__ == "__main__":
    unittest.main(verbosity=2)
