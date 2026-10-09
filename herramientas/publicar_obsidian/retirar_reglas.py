"""Retirada explícita de las seis páginas históricas CR 2.2; conserva los originales."""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote
import publicar as p

ENTRADA = "01. Reglas/9. Resúmenes/Reglas completas de Disney Lorcana 2.3 - cambios respecto a 2.2.md"
CARPETA = "01. Reglas/9. Resúmenes/"
PERMITIDAS = {CARPETA + n + ".md" for n in (
    "Reglas completas de Disney Lorcana 2.2 - cambios respecto a 2.1",
    "CR 2.2 - matriz de diferencias respecto a CR 2.1",
    "CR 2.2 - comparación final con Attack of the Vine",
    "CR 2.2 - revisión editorial del PDF oficial",
    "CR 2.2 - resumen de implementación",
    "Attack of the Vine - cambios anunciados y control para CR 2.2")}


def preparar_retirada(root, archivos, publicados):
    seleccion = {}
    root = Path(root).resolve()
    for nombre in archivos:
        if nombre not in PERMITIDAS or nombre in seleccion:
            raise p.PublicacionError("Retirada fuera de la lista CR 2.2 o repetida: " + nombre)
        p.ruta_editorial(root, nombre, "reglas")
        path = root / nombre
        if "se conserva como registro histórico" not in path.read_text(encoding="utf-8-sig").lower():
            raise p.PublicacionError("Falta el aviso histórico: " + nombre)
        seleccion[nombre] = {"sha256_local": hashlib.sha256(path.read_bytes()).hexdigest(), "publicada": nombre in publicados}
    if not seleccion:
        raise p.PublicacionError("Indica las rutas exactas que deben retirarse.")
    return seleccion


def comprobar_enlaces(root, publicados, targets):
    stems = {Path(n).stem for n in targets}
    for nombre in publicados - targets:
        path = root / nombre
        if path.suffix != ".md" or not path.is_file():
            continue
        text = unquote(path.read_text(encoding="utf-8-sig"))
        for link in re.findall(r"\[\[([^\]\n]+)\]\]", text):
            dest = link.split("|", 1)[0].split("#", 1)[0].removesuffix(".md")
            if dest in stems or dest + ".md" in targets:
                raise p.PublicacionError("Queda un enlace a una página retirada en " + nombre)
        if any(n in text or n.removesuffix(".md") in text for n in targets):
            raise p.PublicacionError("Queda una referencia a una página retirada en " + nombre)


def retirar(root, commit, archivos, publication, aplicar=False, command=None, informe=None):
    root = Path(root).resolve()
    if not re.fullmatch(r"[0-9a-f]{40,64}", commit) or p.git(root, "rev-parse", "HEAD") != commit:
        raise p.PublicacionError("Usa el hash concreto del commit actual subido.")
    p.git(root, "merge-base", "--is-ancestor", commit, "@{upstream}")
    if publication.get("estado") != "publicado" or publication.get("commit") != commit or publication.get("pendientes"):
        raise p.PublicacionError("La publicación de reemplazo debe estar completa antes de retirar.")
    if not {ENTRADA, "Empecemos.md"} <= set(publication.get("archivos", [])):
        raise p.PublicacionError("Publica primero la entrada de cambios y la portada.")
    for nombre in publication["archivos"]:
        p.ruta_editorial(root, nombre, "reglas")
        if p.comprobar_archivo(root, commit, nombre) != publication["sha256"][nombre]:
            raise p.PublicacionError("Un archivo publicado cambió: " + nombre)
    command = command or p.encontrar_cli()
    if Path(p.cli(command, root, "vault", "info=path")).resolve() != root:
        raise p.PublicacionError("La CLI apunta a otra bóveda.")
    config = (root / ".obsidian/publish.json").read_bytes()
    if not json.loads(config).get("siteId"):
        raise p.PublicacionError("Falta el sitio configurado.")
    published = set(p.cli(command, root, "publish:list").splitlines())
    pending = p.pendientes(p.cli(command, root, "publish:status"))
    if any(n in pending or n not in published for n in publication["archivos"]):
        raise p.PublicacionError("La publicación de reemplazo sigue pendiente.")
    selection = preparar_retirada(root, archivos, published)
    targets = set(selection)
    comprobar_enlaces(root, published, targets)
    for nombre in targets:
        p.comprobar_archivo(root, commit, nombre)
    report = {"estado": "preparado", "commit": commit, "paginas": selection, "retiradas": [],
              "ya_ausentes": [n for n, r in selection.items() if not r["publicada"]]}
    def guardar():
        if informe:
            Path(informe).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    guardar()
    if not aplicar:
        return report
    try:
        for nombre, record in selection.items():
            if (root / ".obsidian/publish.json").read_bytes() != config:
                raise p.PublicacionError("La configuración del sitio cambió.")
            if hashlib.sha256((root / nombre).read_bytes()).hexdigest() != record["sha256_local"]:
                raise p.PublicacionError("El histórico local cambió: " + nombre)
            if record["publicada"]:
                result = p.cli(command, root, "publish:remove", "path=" + nombre)
                if nombre in set(p.cli(command, root, "publish:list").splitlines()):
                    raise p.PublicacionError("Publish no confirmó la retirada: " + nombre + ": " + result)
                report["retiradas"].append(nombre)
                guardar()
        final = set(p.cli(command, root, "publish:list").splitlines())
        if targets & final or not set(publication["archivos"]) <= final:
            raise p.PublicacionError("Estado final de Publish inesperado.")
        for nombre, record in selection.items():
            if hashlib.sha256((root / nombre).read_bytes()).hexdigest() != record["sha256_local"]:
                raise p.PublicacionError("El histórico local no se conservó: " + nombre)
        report["estado"] = "retirado"
    except Exception as exc:
        report.update(estado="error", error=str(exc))
        guardar()
        raise p.PublicacionError(str(exc), report) from exc
    guardar()
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--archivo", action="append", required=True)
    parser.add_argument("--informe-publicacion", type=Path, required=True)
    parser.add_argument("--informe", type=Path, required=True)
    parser.add_argument("--aplicar", action="store_true")
    args = parser.parse_args()
    try:
        result = retirar(p.ROOT, args.commit, args.archivo,
                         json.loads(args.informe_publicacion.read_text(encoding="utf-8-sig")),
                         args.aplicar, informe=args.informe)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except p.PublicacionError as exc:
        print(json.dumps(dict(exc.informe, estado="error", error=str(exc)), ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    sys.exit(main())
