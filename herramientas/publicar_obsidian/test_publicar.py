"""Pruebas de alcance y fallos de publicación; nunca llaman al sitio real."""
import sys
sys.dont_write_bytecode = True
import json
import io
from contextlib import redirect_stdout
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import publicar as p


class PublicacionTests(unittest.TestCase):
    def test_enlace_publico_con_final_que_parece_extension(self):
        base='https://publish.obsidian.md/wiki'
        self.assertEqual(p.enlace_publico(base,'Reglas 2.3 - cambios respecto a 2.2.md'),base+'/Reglas%202.3%20-%20cambios%20respecto%20a%202.2.md')
        self.assertEqual(p.enlace_publico(base,'Caso normal.md'),base+'/Caso%20normal')
        self.assertEqual(p.enlace_publico(base,'09. Recursos/bolsa.svg'),base+'/09.%20Recursos/bolsa.svg')

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="lorcana-publish-")
        self.root = Path(self.tmp.name).resolve()
        self.caso = p.CASOS + "11.0. Timing y Resolución/Duda con acentos y espacios.md"
        self.otro = p.CASOS + "11.0. Timing y Resolución/Otra duda pendiente.md"
        self.indice = p.CASOS + "ÍNDICE - Casos de ejemplo y aclaraciones.md"
        self.escribir(self.caso, "# Caso\nVersión anterior.\n")
        self.escribir(self.otro, "# Otra duda\nCambio ajeno.\n")
        self.escribir(self.indice, "# Índice\n")
        self.escribir("Empecemos.md", "# Portada\n")
        self.escribir(".obsidian/publish.json", json.dumps({"siteId": "test-site"}))
        p.git(self.root, "init", "-b", "main")
        p.git(self.root, "config", "user.name", "Prueba local")
        p.git(self.root, "config", "user.email", "prueba@example.invalid")
        p.git(self.root, "config", "core.autocrlf", "false")
        self.commit()
        self.escribir(self.caso, "# Caso\nDuda documentada.\n")
        self.escribir(self.indice, "# Índice\nEnlace a la duda.\n")
        self.escribir("Empecemos.md", "# Portada\nFecha actualizada.\n")
        self.escribir("herramientas/ejemplo.md", "# Herramienta privada\n")
        self.commit()
        p.git(self.root, "remote", "add", "origin", "https://example.invalid/test.git")
        p.git(self.root, "update-ref", "refs/remotes/origin/main", "HEAD")
        p.git(self.root, "branch", "--set-upstream-to=origin/main", "main")
        self.estado = {self.caso: "changed", self.indice: "changed", "Empecemos.md": "changed",
                       self.otro: "new", "herramientas/ejemplo.md": "new"}
        self.existentes = {self.caso, self.indice, "Empecemos.md"}
        self.llamadas = []
        self.falla = None

    def tearDown(self):
        self.tmp.cleanup()

    def escribir(self, nombre, contenido):
        dest = self.root / nombre
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(contenido, encoding="utf-8")

    def commit(self):
        p.git(self.root, "add", "--all")
        p.git(self.root, "commit", "-m", "Prueba de documentación")

    def cli(self, command, root, *args):
        self.llamadas.append(args)
        if args == ("vault", "info=path"):
            return str(root)
        if args == ("publish:site",):
            return "slug\tprueba\nurl\thttps://publish.obsidian.md/prueba"
        if args == ("publish:status",):
            return "\n".join(f"{estado}\t{nombre}" for nombre, estado in self.estado.items()) or "No changes."
        if args == ("publish:list",):
            return "\n".join(sorted(self.existentes))
        if args[0] == "publish:add":
            nombre = args[1].removeprefix("path=")
            if nombre == self.falla:
                return "Error: fallo de red"
            self.estado.pop(nombre)
            self.existentes.add(nombre)
            return f"Published: {nombre}"
        self.fail(f"Comando no previsto: {args}")

    def test_solo_publica_seleccion_y_conserva_pendientes_ajenos(self):
        plan = p.preparar(self.root, "HEAD", [self.caso, self.indice])
        before = (self.root / self.otro).read_bytes()
        with patch.object(p, "cli", side_effect=self.cli):
            result = p.publicar(self.root, plan, aplicar=True, command="simulado")
        self.assertEqual(result["publicados"], [self.caso, self.indice])
        self.assertEqual(result["pendientes"], [])
        self.assertEqual(result["estado"], "publicado")
        self.assertEqual([args for args in self.llamadas if args[0] == "publish:add"],
                         [("publish:add", f"path={self.caso}"), ("publish:add", f"path={self.indice}")])
        self.assertEqual(self.estado[self.otro], "new")
        self.assertEqual(self.estado["Empecemos.md"], "changed")
        self.assertEqual(self.estado["herramientas/ejemplo.md"], "new")
        self.assertEqual((self.root / self.otro).read_bytes(), before)

    def test_plan_y_comprobacion_no_escriben(self):
        plan = p.preparar(self.root, "HEAD", [self.caso])
        initial = dict(self.estado)
        with patch.object(p, "cli", side_effect=self.cli):
            result = p.publicar(self.root, plan, command="simulado")
        self.assertEqual(result["estado"], "comprobado")
        self.assertEqual(self.estado, initial)
        self.assertFalse(any(args[0] == "publish:add" for args in self.llamadas))

    def test_perfil_reglas_requiere_seleccion_explicita_y_excluye_fuentes(self):
        regla = "01. Reglas/1. Principios generales/Contadores.md"
        self.escribir(regla, "# Contadores\n")
        self.escribir("Documentacion Oficial/README.md", "# Fuente privada\n")
        self.commit()
        with self.assertRaises(p.PublicacionError):
            p.preparar(self.root, "HEAD", [regla])
        self.assertEqual(p.preparar(self.root, "HEAD", [regla], "reglas")["archivos"], [regla])
        for nombre in ("Documentacion Oficial/README.md", "herramientas/ejemplo.md", "../Empecemos.md"):
            with self.subTest(nombre=nombre), self.assertRaises(p.PublicacionError):
                p.preparar(self.root, "HEAD", [nombre], "reglas")

    def test_rechaza_rutas_ajenas_sin_commit_y_recorridos(self):
        for archivos in ([], [self.otro], ["herramientas/ejemplo.md"], ["../Empecemos.md"],
                         ["/Empecemos.md"], [self.caso, self.caso]):
            with self.subTest(archivos=archivos), self.assertRaises(p.PublicacionError):
                p.preparar(self.root, "HEAD", archivos)

    def test_recursos_e_introduccion_solo_en_perfil_reglas(self):
        nombres = ["00. Introducción/Guía.md", "09. Recursos/Diagrama.svg", "09. Recursos/Diagrama.png", "04. Guia de correccion de jugadas/Referencia.md"]
        for n in nombres:
            self.escribir(n, "Contenido de prueba")
        self.escribir("09. Recursos/privado.html", "No permitido")
        self.commit()
        self.assertEqual(p.preparar(self.root, "HEAD", nombres, "reglas")["archivos"], nombres)
        for n in nombres + ["09. Recursos/privado.html"]:
            with self.subTest(n=n), self.assertRaises(p.PublicacionError):
                p.preparar(self.root, "HEAD", [n])
        with self.assertRaises(p.PublicacionError):
            p.preparar(self.root, "HEAD", ["09. Recursos/privado.html"], "reglas")

    def test_entrada_breve_de_cartas_permitida_y_fichas_excluidas(self):
        entrada = "02. Listado de Cartas/Cartas de Lorcana.md"
        ficha = "02. Listado de Cartas/Set 1 - The First Chapter.md"
        self.escribir(entrada, "# Cartas\nConsulta Lorcast.\n")
        self.escribir(ficha, "# Corpus privado de cartas\n")
        self.commit()
        self.assertEqual(p.preparar(self.root, "HEAD", [entrada])["archivos"], [entrada])
        with self.assertRaises(p.PublicacionError):
            p.preparar(self.root, "HEAD", [ficha])

    def test_rechaza_cambios_posteriores_antes_de_publicar_cualquier_archivo(self):
        plan = p.preparar(self.root, "HEAD", [self.caso, self.indice])
        self.escribir(self.indice, "Cambio posterior ajeno.\n")
        with patch.object(p, "cli", side_effect=self.cli), self.assertRaises(p.PublicacionError):
            p.publicar(self.root, plan, aplicar=True, command="simulado")
        self.assertFalse(any(args[0] == "publish:add" for args in self.llamadas))

    def test_fallo_parcial_detiene_el_resto_y_conserva_informe(self):
        plan = p.preparar(self.root, "HEAD", [self.caso, self.indice, "Empecemos.md"])
        self.falla = self.indice
        with patch.object(p, "cli", side_effect=self.cli), self.assertRaises(p.PublicacionError) as exc:
            p.publicar(self.root, plan, aplicar=True, command="simulado")
        self.assertEqual(exc.exception.informe["publicados"], [self.caso])
        self.assertEqual(exc.exception.informe["pendientes"], [self.indice, "Empecemos.md"])
        self.assertEqual(self.estado["Empecemos.md"], "changed")
        self.assertEqual(exc.exception.informe["estado"], "error")

    def test_no_republica_archivo_ya_actualizado(self):
        del self.estado[self.caso]
        plan = p.preparar(self.root, "HEAD", [self.caso])
        with patch.object(p, "cli", side_effect=self.cli):
            result = p.publicar(self.root, plan, aplicar=True, command="simulado")
        self.assertEqual(result["ya_actualizados"], [self.caso])
        self.assertFalse(any(args[0] == "publish:add" for args in self.llamadas))

    def test_boveda_distinta_o_commit_no_subido_no_publican(self):
        plan = p.preparar(self.root, "HEAD", [self.caso])
        with patch.object(p, "cli", return_value=str(self.root / "otra")), self.assertRaises(p.PublicacionError):
            p.publicar(self.root, plan, aplicar=True, command="simulado")
        p.git(self.root, "update-ref", "refs/remotes/origin/main", "HEAD^")
        with patch.object(p, "cli", side_effect=self.cli), self.assertRaises(p.PublicacionError):
            p.publicar(self.root, plan, aplicar=True, command="simulado")
        self.assertEqual(self.llamadas, [])

    def test_identifica_por_ruta_y_envia_id_a_cli_con_nombres_repetidos(self):
        config = self.root / "registro-obsidian.json"
        config.write_text(json.dumps({"vaults": {
            "otra-id": {"path": str(self.root.parent / "otra" / self.root.name)},
            "proyecto-id": {"path": str(self.root)}
        }}), encoding="utf-8")
        self.assertEqual(p.identificar_boveda(self.root, config), "proyecto-id")
        with patch.object(p, "identificar_boveda", return_value="proyecto-id"), \
                patch.object(p, "ejecutar", return_value="respuesta") as run:
            p.cli("obsidian", self.root, "publish:add", f"path={self.caso}")
        self.assertEqual(run.call_args.args[0],
                         ["obsidian", "vault=proyecto-id", "publish:add", f"path={self.caso}"])

    def test_aplicar_exige_hash_fijo_y_no_ejecuta_head_variable(self):
        output = io.StringIO()
        with patch.object(sys, "argv", ["publicar.py", "--commit", "HEAD", "--archivo", self.caso, "--aplicar"]), \
                patch.object(p, "publicar") as publish, redirect_stdout(output):
            code = p.main()
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(output.getvalue())["estado"], "error")
        publish.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
