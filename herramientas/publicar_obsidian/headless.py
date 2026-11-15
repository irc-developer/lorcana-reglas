"""Revisa una selección editorial y, opcionalmente, simula Publish con ob."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

from publicar import ROOT, PublicacionError, ruta_editorial


VERSION_OB = "0.0.14"
SITIO = "reglas-lorcana"
ETIQUETAS = {"new": "Altas", "changed": "Actualizaciones", "deleted": "Retiradas"}
RESERVADO = re.compile(
    r"(?<!\w)(?:borrador(?:es)?|drafts?|wip|intern[oa]s?|privad[oa]s?|"
    r"pendientes?|por desarrollar|temporales?|plantillas?|tmp)(?!\w)", re.I
)


def lista_rutas(config, clave):
    valor = config.get(clave)
    if not isinstance(valor, list) or any(not isinstance(ruta, str) for ruta in valor):
        raise PublicacionError("La configuración de filtros no tiene el formato esperado.")
    return valor


def en_filtro(ruta, filtros):
    nombre = ruta.casefold()
    for filtro in filtros:
        prefijo = filtro.replace("\\", "/").rstrip("/").casefold()
        if nombre == prefijo or nombre.startswith(prefijo + "/"):
            return True
    return False


def elegibilidad(root, nombre, excluidos):
    nombre = ruta_editorial(root, nombre, "reglas")
    ruta = Path(nombre)
    if any(p.startswith(".") or RESERVADO.search(p) for p in ruta.parts):
        raise PublicacionError(f"Ruta reservada o de trabajo: {nombre}")
    if en_filtro(nombre, excluidos):
        raise PublicacionError(f"Excluido en la configuración de escritorio: {nombre}")
    archivo = root / ruta
    if archivo.resolve() != archivo:
        raise PublicacionError(f"Ruta redirigida: {nombre}")
    if archivo.stat().st_size > 50 * 1024 * 1024:
        raise PublicacionError(f"Supera el límite de 50 MiB: {nombre}")
    if ruta.suffix != ".md":
        return "adjunto explícito"
    with archivo.open(encoding="utf-8") as flujo:
        if flujo.readline().rstrip("\r\n") != "---":
            return "solo si ya está publicada"
        lineas = []
        for linea in flujo:
            if linea.rstrip("\r\n") == "---":
                break
            lineas.append(linea)
        else:
            raise PublicacionError(f"Frontmatter sin cerrar: {nombre}")
    metadatos = "".join(lineas)
    if re.search(
        r"^\s*(?:draft|wip|private|status|estado)\s*:\s*"
        r"""['"]?(?:true|yes|draft|wip|private|borrador|pendiente|privado)\b""",
        metadatos, re.I | re.M,
    ):
        raise PublicacionError(f"Metadatos de borrador o contenido privado: {nombre}")
    banderas = re.findall(r"^[ \t]*publish[ \t]*:.*$", metadatos, re.I | re.M)
    if banderas == ["publish: true"]:
        return "publish: true"
    if banderas:
        raise PublicacionError(f"Marca publish desactivada o distinta de 'publish: true': {nombre}")
    return "solo si ya está publicada"


def ejecutar(args, root, mensaje):
    try:
        resultado = subprocess.run(
            args, cwd=root, stdin=subprocess.DEVNULL, capture_output=True,
            text=True, encoding="utf-8", check=True, timeout=120,
        )
    except (OSError, UnicodeError, subprocess.SubprocessError):
        # Los errores del proveedor pueden contener detalles de la sesión.
        raise PublicacionError(mensaje) from None
    return resultado.stdout.strip()


def entorno(root):
    node = shutil.which("node")
    if not node:
        return "falta Node.js 22 o superior", None
    version = ejecutar([node, "--version"], root, "No se pudo verificar Node.js.")
    match = re.fullmatch(r"v(\d+)\.\d+\.\d+", version)
    if not match or int(match[1]) < 22:
        return "se requiere Node.js 22 o superior", None
    if sys.platform == "win32":
        shim = shutil.which("ob.cmd")
        cli = Path(shim).parent / "node_modules/obsidian-headless/cli.js" if shim else None
        comando = [node, str(cli)] if cli and cli.is_file() else None
    else:
        ob = shutil.which("ob")
        comando = [ob] if ob else None
    if not comando:
        return f"Node.js {version}, falta la CLI oficial ob {VERSION_OB}", None
    if ejecutar([*comando, "--version"], root, "No se pudo verificar ob.") != VERSION_OB:
        return f"Node.js {version}, se requiere ob {VERSION_OB} para este piloto", None
    return f"Node.js {version}, ob {VERSION_OB}", comando


def leer_json(comando, root, mensaje):
    texto = ejecutar(comando, root, mensaje)
    try:
        datos = json.loads(texto)
    except ValueError:
        raise PublicacionError(mensaje) from None
    if not isinstance(datos, dict):
        raise PublicacionError(mensaje)
    return datos


def simular(root, comando, escritorio, seleccion):
    config = leer_json(
        [*comando, "publish-config", "--path", str(root), "--json"], root,
        "No se pudo leer la vinculación local de Headless Publish.",
    )
    ruta = config.get("vaultPath")
    if (not isinstance(ruta, str) or Path(ruta).resolve() != root
            or config.get("siteId") != escritorio["siteId"] or config.get("host") != escritorio["host"]):
        raise PublicacionError("La vinculación Headless no coincide con la bóveda y el sitio de escritorio.")
    incluidos = lista_rutas(config, "includes")
    excluidos = lista_rutas(config, "excludes")
    print(f"Filtros Headless: {len(incluidos)} inclusiones, {len(excluidos)} exclusiones.")
    for nombre in seleccion:
        if en_filtro(nombre, excluidos):
            raise PublicacionError(f"La selección incluye una ruta excluida en Headless: {nombre}")
    cuenta = leer_json(
        [*comando, "publish-list-sites", "--json"], root,
        "No se pudo verificar el acceso al sitio. Revisa la sesión Headless y la conexión.",
    )
    sitios = cuenta.get("sites"), cuenta.get("shared")
    if not all(isinstance(grupo, list) for grupo in sitios) or not any(
        isinstance(sitio, dict) and sitio.get("id") == config["siteId"]
        and sitio.get("host") == config["host"] and sitio.get("slug") == SITIO
        for grupo in sitios for sitio in grupo
    ):
        raise PublicacionError("La cuenta Headless no ha confirmado el sitio esperado.")
    datos = leer_json(
        [*comando, "publish", "--path", str(root), "--dry-run", "--json"], root,
        "Falló la simulación. Revisa el acceso al sitio y la conexión.",
    )
    cambios = datos.get("changes")
    if datos.get("published") is not False or not isinstance(cambios, list):
        raise PublicacionError("La respuesta no confirma una simulación válida.")
    grupos = {tipo: [] for tipo in ETIQUETAS}
    vistas = set()
    bloqueos = []
    for cambio in cambios:
        if not isinstance(cambio, dict):
            raise PublicacionError("La simulación contiene un cambio sin formato reconocido.")
        tipo, nombre = cambio.get("type"), cambio.get("path")
        if (not isinstance(tipo, str) or tipo not in grupos or not isinstance(nombre, str)
                or not nombre or not nombre.isprintable() or nombre in vistas):
            raise PublicacionError("La simulación contiene un tipo o una ruta sin formato reconocido.")
        vistas.add(nombre)
        grupos[tipo].append(nombre)
        if tipo == "deleted":
            bloqueos.append((nombre, "retirada remota"))
        elif nombre not in seleccion:
            bloqueos.append((nombre, "fuera de la selección"))
        elif tipo == "new" and seleccion[nombre] == "solo si ya está publicada":
            bloqueos.append((nombre, "alta de nota sin publish: true"))
    for tipo, rutas in grupos.items():
        print(f"{ETIQUETAS[tipo]} ({len(rutas)})")
        for ruta in sorted(rutas):
            print(f"  {ruta}")
    sin_cambio = seleccion.keys() - vistas
    if sin_cambio:
        print("Selección sin cambio informado (puede estar al día o no ser elegible)")
        for ruta in sorted(sin_cambio):
            print(f"  {ruta}")
    for ruta, motivo in bloqueos:
        print(f"BLOQUEO: {ruta} ({motivo})")
    return bool(bloqueos)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archivo", action="append", required=True, help="Ruta editorial explícita.")
    parser.add_argument("--simular", action="store_true", help="Compara con el sitio sin publicar.")
    args = parser.parse_args()
    try:
        escritorio = json.loads((ROOT / ".obsidian/publish.json").read_text(encoding="utf-8-sig"))
        if not isinstance(escritorio, dict) or not escritorio.get("siteId") or not escritorio.get("host"):
            raise PublicacionError("No hay un sitio Publish identificado en la configuración de escritorio.")
        incluidos = lista_rutas(escritorio, "included")
        excluidos = lista_rutas(escritorio, "excluded")
        print(f"Sitio esperado: {SITIO}. Configuración de escritorio presente.")
        print(f"Filtros de escritorio: {len(incluidos)} inclusiones, {len(excluidos)} exclusiones.")
        seleccion = {}
        for nombre in args.archivo:
            nombre = nombre.replace("\\", "/")
            if nombre in seleccion:
                raise PublicacionError(f"Ruta repetida: {nombre}")
            seleccion[nombre] = elegibilidad(ROOT, nombre, excluidos)
            print(f"  {nombre} ({seleccion[nombre]})")
        estado, comando = entorno(ROOT)
        print(f"Entorno: {estado}.")
        if not args.simular:
            print("Revisión local completada. Pendientes remotos sin consultar.")
            return 0
        if not comando:
            raise PublicacionError("Headless no está disponible para simular.")
        return int(simular(ROOT, comando, escritorio, seleccion))
    except PublicacionError as exc:
        print(f"BLOQUEO: {exc}", file=sys.stderr)
    except (OSError, ValueError):
        print("BLOQUEO: no se pudo leer la configuración o un archivo local.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
