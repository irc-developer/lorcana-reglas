"""Retirada selectiva del catálogo de cartas; nunca elimina las fichas locales.

Operación separada del workflow de dudas. Exige autorización expresa para
retirar el catálogo, un commit subido y un informe de publicación completa.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
from pathlib import Path

import publicar as p

ROOT = p.ROOT
ENTRADA = "02. Listado de Cartas/Cartas de Lorcana.md"


def preparar_retirada(root, archivos, publicados):
    root = Path(root).resolve()
    result = {}
    for nombre in archivos:
        rel = Path(nombre)
        if (any(c in nombre for c in "\r\n\t\0:") or rel.as_posix() != nombre or rel.is_absolute() or rel.parent.as_posix() != "02. Listado de Cartas"
                or rel.suffix != ".md" or nombre == ENTRADA
                or not (rel.name.startswith("Set ") or rel.name == "Illumineer's Quest - Palace Heist.md")):
            raise p.PublicacionError(f"Fuera de las fichas del catálogo: {nombre}")
        path = root / rel
        if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(root):
            raise p.PublicacionError(f"Ficha local ausente o insegura: {nombre}")
        if nombre in result:
            raise p.PublicacionError(f"Ficha repetida: {nombre}")
        result[nombre] = {"sha256_local": hashlib.sha256(path.read_bytes()).hexdigest(),
                          "publicada": nombre in publicados}
    if not result:
        raise p.PublicacionError("Indica las fichas explícitas que se van a retirar.")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--archivo", action="append", required=True)
    parser.add_argument("--informe-publicacion", type=Path, required=True)
    parser.add_argument("--aplicar", action="store_true")
    args = parser.parse_args()
    root = ROOT.resolve()
    sha = p.git(root, "rev-parse", "HEAD")
    if args.commit != sha:
        raise p.PublicacionError("La retirada requiere el hash exacto del commit actual.")
    p.git(root, "merge-base", "--is-ancestor", sha, "@{upstream}")
    publication = json.loads(args.informe_publicacion.read_text(encoding="utf-8"))
    if publication.get("estado") != "publicado" or publication.get("commit") != sha or publication.get("pendientes"):
        raise p.PublicacionError("Publica y verifica primero la migración de artículos y la entrada breve.")
    if ENTRADA not in publication["archivos"] or "Empecemos.md" not in publication["archivos"]:
        raise p.PublicacionError("La entrada breve y la portada deben formar parte de la publicación.")
    for nombre in publication["archivos"]:
        if p.comprobar_archivo(root, sha, nombre) != publication["sha256"][nombre]:
            raise p.PublicacionError("Un artículo cambió después de su publicación: " + nombre)
    command = p.encontrar_cli()
    if Path(p.cli(command, root, "vault", "info=path")).resolve() != root:
        raise p.PublicacionError("La CLI apunta a otra bóveda.")
    config = (root / ".obsidian/publish.json").read_bytes()
    site = json.loads(config)
    published = set(p.cli(command, root, "publish:list").splitlines())
    selection = preparar_retirada(root, args.archivo, published)
    if not set(selection).issubset(site.get("excluded", [])):
        raise p.PublicacionError("Excluye primero las fichas de futuras publicaciones.")
    if ENTRADA not in published:
        raise p.PublicacionError("Falta la entrada breve del catálogo público.")
    pending = p.pendientes(p.cli(command, root, "publish:status"))
    if any(n in pending for n in publication["archivos"]):
        raise p.PublicacionError("La publicación de la migración sigue pendiente.")
    # No despublicar si quedan enlaces locales a estas fichas en notas publicadas.
    targets = set(selection)
    stems = {Path(n).stem for n in targets}
    import re
    from urllib.parse import unquote
    for nombre in published - targets:
        path = root / nombre
        if not path.is_file() or path.suffix != ".md":
            continue
        content = path.read_text(encoding="utf-8-sig")
        for target in re.findall(r"\[\[([^\]\n]+)\]\]", content):
            dest = unquote(target.split("|", 1)[0].split("#", 1)[0]).removesuffix(".md")
            if dest in stems or dest + ".md" in targets:
                raise p.PublicacionError(f"Queda un enlace a la ficha retirada en {nombre}: {target}")
        if any(n in unquote(content) or n.removesuffix(".md") + "#" in unquote(content) for n in targets):
            raise p.PublicacionError("Queda una referencia explícita al catálogo en " + nombre)
    report = {"estado": "preparado", "commit_migracion": sha, "fichas": selection,
              "retiradas": [], "ya_ausentes": [n for n, r in selection.items() if not r["publicada"]]}
    dest = root / ".github/planes/retirada-catalogo-lorcast.json"
    def guardar():
        dest.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    guardar()
    if args.aplicar:
        report["estado"] = "en_curso"
        guardar()
        for nombre, record in selection.items():
            if (root / ".obsidian/publish.json").read_bytes() != config:
                raise p.PublicacionError("La configuración del sitio cambió.")
            if hashlib.sha256((root / nombre).read_bytes()).hexdigest() != record["sha256_local"]:
                raise p.PublicacionError("La ficha local cambió durante la retirada: " + nombre)
            if record["publicada"]:
                output = p.cli(command, root, "publish:remove", "path=" + nombre)
                if nombre in set(p.cli(command, root, "publish:list").splitlines()):
                    raise p.PublicacionError("Publish no retiró la ficha: " + nombre + ": " + output)
                report["retiradas"].append(nombre)
                guardar()
                print("Retirada: " + nombre, flush=True)
        final = set(p.cli(command, root, "publish:list").splitlines())
        if targets & final or ENTRADA not in final:
            raise p.PublicacionError("Estado final del catálogo inesperado.")
        for nombre, record in selection.items():
            if hashlib.sha256((root / nombre).read_bytes()).hexdigest() != record["sha256_local"]:
                raise p.PublicacionError("La ficha local no se conservó: " + nombre)
        report["estado"] = "retirado"
    guardar()
    print(json.dumps({"estado": report["estado"], "fichas": len(selection),
                      "publicadas": sum(r["publicada"] for r in selection.values()),
                      "retiradas": len(report["retiradas"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
