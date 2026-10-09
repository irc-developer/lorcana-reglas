"""Publica solo las rutas editoriales explícitas de un commit de una duda."""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
CASOS = "01. Reglas/11. Casos de ejemplo y aclaraciones/"
RAIZ_EDITORIAL = {"Empecemos.md", "Registro de Tags - Master List.md",
                  "02. Listado de Cartas/Cartas de Lorcana.md"}


class PublicacionError(RuntimeError):
    def __init__(self, mensaje, informe=None):
        super().__init__(mensaje)
        self.informe = informe or {}


def ejecutar(args, root):
    run = subprocess.run(args, cwd=root, capture_output=True, text=True,
                         encoding="utf-8", errors="replace", timeout=120)
    if run.returncode:
        raise PublicacionError((run.stderr or run.stdout).strip() or f"Falló {args[0]}")
    return run.stdout.strip()


def git(root, *args):
    return ejecutar(["git", "-c", f"safe.directory={root.as_posix()}", *args], root)


def ruta_editorial(root, nombre, perfil="dudas"):
    nombre = nombre.replace("\\", "/")
    parts = nombre.split("/")
    if any(c in nombre for c in "\r\n\t\0:") or any(p in ("", ".", "..") for p in parts):
        raise PublicacionError(f"Ruta no válida: {nombre!r}")
    rel = PurePosixPath(nombre)
    permitida = nombre in RAIZ_EDITORIAL or nombre.startswith(CASOS) and rel.suffix == ".md"
    if perfil == "reglas":
        texto_editorial = nombre.startswith(("00. Introducción/", "01. Reglas/", "03. Reglas de Torneo/", "04. Guia de correccion de jugadas/", "05. Consejos de jueces/", "09. Recursos/", "10. Comunidad y actividades/")) and rel.suffix == ".md" and not rel.name.startswith("Plantilla")
        recurso = nombre.startswith(("09. Recursos/", "imagenes/recursos/")) and rel.suffix in (".svg", ".png")
        permitida = permitida or texto_editorial or recurso
    elif perfil != "dudas":
        raise PublicacionError("Perfil de publicación desconocido: " + perfil)
    if rel.is_absolute() or not permitida:
        raise PublicacionError(f"Fuera de la documentación de dudas: {nombre}")
    path = root / nombre
    if not path.resolve().is_relative_to(root) or not path.is_file():
        raise PublicacionError(f"Archivo ausente o fuera de la bóveda: {nombre}")
    if any(p.is_symlink() for p in (path, *path.parents) if p != root and p.is_relative_to(root)):
        raise PublicacionError(f"No se publican enlaces simbólicos: {nombre}")
    return nombre


def comprobar_archivo(root, sha, nombre):
    blob = git(root, "rev-parse", f"{sha}:{nombre}")
    actual = git(root, "hash-object", f"--path={nombre}", "--", nombre)
    if actual != blob:
        raise PublicacionError(f"El archivo tiene cambios posteriores o ajenos al commit: {nombre}")
    return hashlib.sha256((root / nombre).read_bytes()).hexdigest()


def preparar(root, commit, archivos, perfil="dudas"):
    root = Path(root).resolve()
    if not re.fullmatch(r"HEAD|[0-9a-fA-F]{7,64}", commit):
        raise PublicacionError("Usa HEAD o el hash del commit de esta duda.")
    sha = git(root, "rev-parse", "--verify", f"{commit}^{{commit}}")
    cambios = git(root, "diff-tree", "--root", "--no-commit-id", "--no-renames", "-r",
                  "--name-status", "-z", sha).split("\0")
    estados = dict(zip(cambios[1::2], cambios[0::2]))
    if not archivos:
        raise PublicacionError("Indica al menos un --archivo; nunca se selecciona toda la bóveda.")
    elegidos = []
    for archivo in archivos:
        nombre = ruta_editorial(root, archivo, perfil)
        if nombre in elegidos:
            raise PublicacionError(f"Ruta repetida: {nombre}")
        if estados.get(nombre) not in ("A", "M"):
            raise PublicacionError(f"La ruta no fue añadida o modificada en este commit: {nombre}")
        elegidos.append(nombre)
    hashes = {nombre: comprobar_archivo(root, sha, nombre) for nombre in elegidos}
    return {"estado": "plan", "commit": sha, "perfil": perfil, "archivos": elegidos, "sha256": hashes}


def encontrar_cli():
    command = shutil.which("obsidian")
    if command:
        return command
    if sys.platform == "win32" and os.environ.get("LOCALAPPDATA"):
        candidate = Path(os.environ["LOCALAPPDATA"]) / "Programs/obsidian/Obsidian.com"
        if candidate.is_file():
            return str(candidate)
    raise PublicacionError("No se encuentra la CLI oficial de Obsidian; requiere instalador 1.12.7+ y CLI habilitada.")


def identificar_boveda(root, config=None):
    if config is None:
        if sys.platform == "win32":
            config = Path(os.environ["APPDATA"]) / "obsidian/obsidian.json"
        elif sys.platform == "darwin":
            config = Path.home() / "Library/Application Support/obsidian/obsidian.json"
        else:
            config = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config")) / "obsidian/obsidian.json"
    vaults = json.loads(Path(config).read_text(encoding="utf-8-sig")).get("vaults", {})
    matches = [key for key, value in vaults.items() if Path(value["path"]).resolve() == root]
    if len(matches) != 1:
        raise PublicacionError("La bóveda no tiene un identificador único registrado en Obsidian.")
    return matches[0]


def cli(command, root, *args):
    # Nombres iguales o que difieren solo en mayúsculas pueden apuntar a otra bóveda.
    return ejecutar([command, f"vault={identificar_boveda(root)}", *args], root)


def pendientes(texto):
    if texto == "No changes.":
        return {}
    result = {}
    for line in texto.splitlines():
        campos = line.split("\t", 1)
        if len(campos) != 2 or campos[0] not in ("new", "changed", "deleted"):
            raise PublicacionError(f"Respuesta inesperada de publish:status: {line}")
        result[campos[1]] = campos[0]
    if not result:
        raise PublicacionError("Publish no devolvió un estado verificable.")
    return result


def publicar(root, plan, aplicar=False, command=None):
    root = Path(root).resolve()
    command = command or encontrar_cli()
    informe = dict(plan, estado="comprobando", publicados=[], ya_actualizados=[], pendientes=list(plan["archivos"]))
    try:
        if aplicar:
            if git(root, "rev-parse", "HEAD") != plan["commit"]:
                raise PublicacionError("Solo se publica el commit actual de la duda, no un commit histórico.")
            git(root, "merge-base", "--is-ancestor", plan["commit"], "@{upstream}")
        real = cli(command, root, "vault", "info=path")
        if Path(real).resolve() != root:
            raise PublicacionError("La CLI apunta a otra bóveda o no está habilitada.")
        config = (root / ".obsidian/publish.json").read_bytes()
        if not json.loads(config).get("siteId"):
            raise PublicacionError("La bóveda no tiene un sitio Publish configurado.")
        site = dict(line.split("\t", 1) for line in cli(command, root, "publish:site").splitlines())
        base = site.get("url", "")
        if not base.startswith("https://publish.obsidian.md/"):
            raise PublicacionError("Publish no devolvió la URL del sitio configurado.")
        estado = pendientes(cli(command, root, "publish:status"))
        existentes = set(cli(command, root, "publish:list").splitlines())
        elegidos = plan["archivos"]
        informe.update(url_base=base, pendientes=[p for p in elegidos if p in estado],
                       otros_pendientes=len(set(estado) - set(elegidos)))
        # Validar toda la selección antes de la primera subida.
        for nombre in elegidos:
            if comprobar_archivo(root, plan["commit"], nombre) != plan["sha256"][nombre]:
                raise PublicacionError(f"El archivo cambió desde la preparación: {nombre}")
            if estado.get(nombre) == "deleted" or nombre not in estado and nombre not in existentes:
                raise PublicacionError(f"Ruta no publicable o no verificable: {nombre}")
        if not aplicar:
            return dict(informe, estado="comprobado")
        for nombre in elegidos:
            if (root / ".obsidian/publish.json").read_bytes() != config:
                raise PublicacionError("La configuración del sitio cambió durante la publicación.")
            if comprobar_archivo(root, plan["commit"], nombre) != plan["sha256"][nombre]:
                raise PublicacionError(f"El archivo cambió durante la publicación: {nombre}")
            if nombre not in estado:
                informe["ya_actualizados"].append(nombre)
                continue
            result = cli(command, root, "publish:add", f"path={nombre}")
            if result != f"Published: {nombre}":
                raise PublicacionError(f"Publish no confirmó la subida de {nombre}: {result}")
            informe["publicados"].append(nombre)
            informe["pendientes"].remove(nombre)
        final = pendientes(cli(command, root, "publish:status"))
        informe["pendientes"] = [p for p in elegidos if p in final]
        if informe["pendientes"]:
            raise PublicacionError("Siguen pendientes archivos de esta duda; la publicación no está completa.")
        for nombre in elegidos:
            if comprobar_archivo(root, plan["commit"], nombre) != plan["sha256"][nombre]:
                raise PublicacionError(f"El archivo cambió antes de verificar el resultado: {nombre}")
        informe.update(estado="publicado", enlaces={p: base + "/" + quote(p[:-3] if p.endswith(".md") else p, safe="/") for p in elegidos})
        return informe
    except (PublicacionError, OSError, ValueError, subprocess.TimeoutExpired) as exc:
        informe.update(estado="error", error=str(exc))
        raise PublicacionError(str(exc), informe) from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--archivo", action="append", required=True)
    parser.add_argument("--perfil", choices=("dudas", "reglas"), default="dudas")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--comprobar", action="store_true", help="Leer el sitio y los pendientes sin subir archivos.")
    mode.add_argument("--aplicar", action="store_true", help="Publicar solo las rutas explícitas del commit actual ya subido.")
    args = parser.parse_args()
    try:
        if args.aplicar and args.commit == "HEAD":
            raise PublicacionError("Para publicar usa el hash concreto del plan revisado, no HEAD.")
        result = preparar(args.root, args.commit, args.archivo, args.perfil)
        if args.comprobar or args.aplicar:
            result = publicar(args.root, result, args.aplicar)
        code = 0
    except (PublicacionError, OSError, subprocess.TimeoutExpired) as exc:
        result = dict(getattr(exc, "informe", {}), estado="error", error=str(exc))
        code = 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
