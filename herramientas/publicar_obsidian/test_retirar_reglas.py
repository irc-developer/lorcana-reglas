"""Pruebas de retirada de reglas con sitio simulado; nunca llaman a Publish real."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import unittest
from unittest.mock import patch
import publicar as p
import retirar_reglas as r
import test_publicar as fixtures


class RetiradaReglasTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.PublicacionTests()
        self.f.setUp()
        self.root = self.f.root
        self.hist = sorted(r.PERMITIDAS)[0]
        self.f.escribir(self.hist, "Se conserva como registro histórico.\n")
        self.f.escribir(r.ENTRADA, "# CR 2.3\nFecha efectiva: 16/10/2026.\n")
        self.f.escribir("Empecemos.md", "# Portada de la migración\n")
        self.f.commit()
        p.git(self.root, "update-ref", "refs/remotes/origin/main", "HEAD")
        self.sha = p.git(self.root, "rev-parse", "HEAD")
        self.pub = dict(p.preparar(self.root, self.sha, [r.ENTRADA, "Empecemos.md"], "reglas"), estado="publicado", pendientes=[])
        self.f.existentes.update({self.hist, r.ENTRADA})
        self.f.estado.pop("Empecemos.md", None)
        self.fail_remove = False

    def tearDown(self):
        self.f.tearDown()

    def cli(self, command, root, *args):
        if args[0] == "publish:remove":
            self.f.llamadas.append(args)
            if not self.fail_remove:
                self.f.existentes.remove(args[1].removeprefix("path="))
            return "Simulado"
        return self.f.cli(command, root, *args)

    def ejecutar(self, aplicar=False):
        with patch.object(p, "cli", side_effect=self.cli):
            return r.retirar(self.root, self.sha, [self.hist], self.pub, aplicar, "simulado")

    def test_prepara_sin_mutar_y_retira_solo_elegidas(self):
        original = (self.root / self.hist).read_bytes()
        self.assertEqual(self.ejecutar()["estado"], "preparado")
        self.assertIn(self.hist, self.f.existentes)
        pending = dict(self.f.estado)
        result = self.ejecutar(True)
        self.assertEqual(result["retiradas"], [self.hist])
        self.assertNotIn(self.hist, self.f.existentes)
        self.assertIn(r.ENTRADA, self.f.existentes)
        self.assertEqual(self.f.estado, pending)
        self.assertEqual((self.root / self.hist).read_bytes(), original)

    def test_rechaza_fuera_de_lista_duplicados_y_sin_aviso(self):
        for names in ([], ["Empecemos.md"], [self.hist, self.hist], ["../" + self.hist]):
            with self.subTest(names=names), self.assertRaises(p.PublicacionError):
                r.preparar_retirada(self.root, names, self.f.existentes)
        self.f.escribir(self.hist, "# Sin aviso\n")
        with self.assertRaises(p.PublicacionError):
            r.preparar_retirada(self.root, [self.hist], self.f.existentes)

    def test_publicacion_pendiente_y_enlaces_bloquean_retirada(self):
        self.pub["estado"] = "error"
        with self.assertRaises(p.PublicacionError):
            self.ejecutar(True)
        self.pub["estado"] = "publicado"
        self.f.escribir(self.f.otro, "[[" + Path(self.hist).stem + "]]\n")
        self.f.existentes.add(self.f.otro)
        with self.assertRaises(p.PublicacionError):
            self.ejecutar(True)
        self.assertFalse(any(a[0] == "publish:remove" for a in self.f.llamadas))

    def test_fallo_conserva_informe_parcial_y_original(self):
        self.fail_remove = True
        with self.assertRaises(p.PublicacionError) as exc:
            self.ejecutar(True)
        self.assertEqual(exc.exception.informe["estado"], "error")
        self.assertEqual(exc.exception.informe["retiradas"], [])
        self.assertTrue((self.root / self.hist).is_file())


if __name__ == "__main__":
    unittest.main(verbosity=2)
