import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import headless


class HeadlessTests(unittest.TestCase):
    articulo = "01. Reglas/Regla.md"

    def setUp(self):
        temporal = tempfile.TemporaryDirectory()
        self.addCleanup(temporal.cleanup)
        self.root = Path(temporal.name).resolve()
        self.escritorio = {"siteId": "sitio-de-prueba", "host": "host-de-prueba"}
        self.config = dict(self.escritorio, vaultPath=str(self.root), includes=[], excludes=[])
        self.cuenta = {
            "sites": [{"id": self.config["siteId"], "host": self.config["host"], "slug": headless.SITIO}],
            "shared": [],
        }

    def crear(self, ruta, texto):
        archivo = self.root / ruta
        archivo.parent.mkdir(parents=True, exist_ok=True)
        archivo.write_text(texto, encoding="utf-8")

    def test_marca_publica_y_nota_existente_sin_marca(self):
        self.crear(self.articulo, "---\n\npublish: true\n---\n# Regla\n")
        self.assertEqual(headless.elegibilidad(self.root, self.articulo, []), "publish: true")
        self.crear(self.articulo, "# Regla\n")
        self.assertEqual(
            headless.elegibilidad(self.root, self.articulo, []), "solo si ya está publicada"
        )

    def test_bloquea_archivos_internos_aunque_tengan_marca_publica(self):
        marca = "---\npublish: true\n---\n"
        for ruta, texto, exclusiones in (
            ("herramientas/README.md", marca, []),
            ("01. Reglas/.interno/Regla.md", marca, []),
            ("01. Reglas/Dudas por desarrollar/Regla.md", marca, []),
            (self.articulo, marca, ["01. Reglas"]),
            (self.articulo, marca.replace("true", "false"), []),
            (self.articulo, marca.replace("true", "true\ndraft: true"), []),
        ):
            with self.subTest(ruta=ruta, texto=texto, exclusiones=exclusiones):
                self.crear(ruta, texto)
                with self.assertRaises(headless.PublicacionError):
                    headless.elegibilidad(self.root, ruta, exclusiones)

    def test_informa_todas_las_retiradas_y_cambios_fuera_de_seleccion(self):
        cambios = {
            "published": False,
            "changes": [
                {"type": "new", "path": self.articulo},
                {"type": "changed", "path": "herramientas/README.md"},
                {"type": "deleted", "path": "09. Recursos/Diagrama.svg"},
            ],
        }
        salida = io.StringIO()
        with patch.object(headless, "leer_json", side_effect=[self.config, self.cuenta, cambios]) as leer:
            with contextlib.redirect_stdout(salida):
                self.assertTrue(headless.simular(
                    self.root, ["ob"], self.escritorio, {self.articulo: "solo si ya está publicada"}
                ))
        self.assertEqual(
            leer.call_args.args[0], ["ob", "publish", "--path", str(self.root), "--dry-run", "--json"]
        )
        for texto in ("Alta", "Actualizaciones", "Retiradas", "fuera de la selección",
                      "retirada remota", "alta de nota sin publish: true"):
            self.assertIn(texto, salida.getvalue())

    def test_permite_actualizacion_preexistente_sin_marca(self):
        cambios = {"published": False, "changes": [{"type": "changed", "path": self.articulo}]}
        with patch.object(headless, "leer_json", side_effect=[self.config, self.cuenta, cambios]):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertFalse(headless.simular(
                    self.root, ["ob"], self.escritorio, {self.articulo: "solo si ya está publicada"}
                ))

    def test_rechaza_otra_boveda_otro_sitio_o_una_exclusion(self):
        for config, cuenta in (
            (dict(self.config, vaultPath=str(self.root / "otra")), self.cuenta),
            (dict(self.config, siteId="otro"), self.cuenta),
            (dict(self.config, excludes=["01. Reglas"]), self.cuenta),
            (self.config, {"sites": [], "shared": []}),
        ):
            with self.subTest(config=config, cuenta=cuenta):
                with patch.object(headless, "leer_json", side_effect=[config, cuenta]) as leer:
                    with contextlib.redirect_stdout(io.StringIO()):
                        with self.assertRaises(headless.PublicacionError):
                            headless.simular(
                                self.root, ["ob"], self.escritorio, {self.articulo: "publish: true"}
                            )
                self.assertTrue(all("publish" not in llamada.args[0] for llamada in leer.call_args_list))


if __name__ == "__main__":
    unittest.main()
