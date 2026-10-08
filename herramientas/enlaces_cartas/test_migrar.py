"""Pruebas de identidad de cartas y conservación de texto en la migración."""
import sys
sys.dont_write_bytecode = True
import json
from pathlib import Path
import tempfile
import unittest

import migrar as m


class MigracionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.local = "02. Listado de Cartas/Set 7 - Archazia''s Island.md"
        path = self.root / self.local
        path.parent.mkdir()
        path.write_bytes(b"# Set\r\n\r\n## Elsa - Ice Maker\r\n\r\n**Coste:** 7\r\nTexto completo.\r\n\r\n## Bolt - Superdog\r\nOtra ficha.\r\n")
        self.card = {"name": "Elsa", "version": "Ice Maker", "lang": "en",
                     "id": "crd_elsa", "collector_number": "69", "cost": 7,
                     "image_uris": {"digital": {"large": "https://cards.lorcast.io/elsa.avif?123"}}}
        (self.root / "set-7.json").write_text(json.dumps([self.card]), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_fichas_no_mezclan_cartas_y_conservan_crlf(self):
        fichas = m.fichas_locales(self.root)
        self.assertEqual(len(fichas), 2)
        self.assertIn("Texto completo.", fichas[(self.local, "Elsa - Ice Maker")])
        self.assertNotIn("Otra ficha.", fichas[(self.local, "Elsa - Ice Maker")])
        self.assertIn("\r\n", m.leer(self.root / self.local))

    def test_conserva_etiqueta_reglas_y_texto_ajeno_y_es_idempotente(self):
        text = f"Duda: [[{self.local}#Elsa - Ice Maker|Elsa – Ice Maker]].\r\n[[6.1. General|Reglas]] ![[imagen.svg|20]]\r\n"
        key = self.local + "#Elsa - Ice Maker"
        mapa = {key: m.elegir(self.local, "Elsa - Ice Maker", "Elsa", m.fichas_locales(self.root), self.root)}
        result, count = m.sustituir(text, mapa, self.root)
        self.assertEqual(count, 1)
        self.assertEqual(result, "Duda: [Elsa – Ice Maker](https://cards.lorcast.io/elsa.avif?123).\r\n[[6.1. General|Reglas]] ![[imagen.svg|20]]\r\n")
        self.assertEqual(m.sustituir(result, mapa, self.root), (result, 0))

    def test_rechaza_coincidencias_ambiguas_y_coste_distinto(self):
        fichas = m.fichas_locales(self.root)
        second = dict(self.card, id="crd_otra", collector_number="70")
        (self.root / "set-7.json").write_text(json.dumps([self.card, second]), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "ambigua"):
            m.elegir(self.local, "Elsa - Ice Maker", "Elsa", fichas, self.root)
        (self.root / "set-7.json").write_text(json.dumps([dict(self.card, cost=8)]), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Coste distinto"):
            m.elegir(self.local, "Elsa - Ice Maker", "Elsa", fichas, self.root)

    def test_ancla_de_linea_exige_ficha_de_la_etiqueta(self):
        fichas = m.fichas_locales(self.root)
        good = m.elegir(self.local, "L999", "Elsa - Ice Maker", fichas, self.root)
        self.assertEqual(good["ficha_verificada"], "Elsa - Ice Maker")
        with self.assertRaisesRegex(ValueError, "No existe ficha exacta"):
            m.elegir(self.local, "L999", "Otra carta", fichas, self.root)

    def test_reimpresion_no_se_elige_por_orden_o_rareza(self):
        extra = dict(self.card, id="crd_variante", collector_number="224")
        (self.root / "set-7.json").write_text(json.dumps([extra, self.card]), encoding="utf-8")
        selected = m.elegir(self.local, "Elsa - Ice Maker", "Elsa", m.fichas_locales(self.root), self.root)
        self.assertEqual(selected["numero"], "69")


if __name__ == "__main__":
    unittest.main(verbosity=2)
