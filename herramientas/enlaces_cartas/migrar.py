"""Resuelve y migra enlaces de cartas con datos de Lorcast descargados previamente.

No descarga datos ni publica. Conserva etiquetas, saltos de línea y todo el texto
ajeno al enlace. El modo predeterminado prepara el mapa sin editar artículos.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import csv
import hashlib
import json
import re
import subprocess
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[2]
CATALOGO = "02. Listado de Cartas/"
MAPA = ROOT / ".github/planes/mapa-cartas-lorcast.json"
INVENTARIO = ROOT / ".github/planes/inventario-enlaces-cartas.tsv"
WIKI = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
MD = re.compile(r"(?<!!)\[([^\]\n]+)\]\((<[^>]+>|[^\n)]*)\)")
ACTIVAS = ("00. Introducción/", "01. Reglas/", "01.1.a Official English Reference",
           "03. Reglas de Torneo/", "04. Guia de correccion de jugadas/",
           "05. Consejos de jueces/", "06. Reviews de jueces en torneos/",
           "07. Gestión de Aplicación Carde.io/", "08. Consejos para jugadores/",
           "09. Recursos/", "10. Comunidad y actividades/")


def leer(path):
    return path.read_bytes().decode("utf-8-sig")


def normalizar(nombre):
    nombre = unicodedata.normalize("NFKD", nombre)
    nombre = "".join(c for c in nombre if not unicodedata.combining(c))
    nombre = nombre.translate(str.maketrans({"’": "'", "‘": "'", "–": "-", "—": "-"}))
    return re.sub(r"\s+", " ", nombre).strip().casefold()


def nombre_carta(carta):
    return carta["name"] + (" - " + carta["version"] if carta.get("version") else "")


def archivos_activos(root=ROOT):
    files = subprocess.check_output(["git", "-c", f"safe.directory={root.as_posix()}",
                                     "ls-files", "-z"], cwd=root).decode("utf-8").split("\0")
    return [p for p in files if p.endswith(".md") and p.startswith(ACTIVAS)
            and "Plantilla" not in Path(p).name]


def fichas_locales(root=ROOT):
    result = {}
    for path in (root / CATALOGO).glob("*.md"):
        content = leer(path)
        for m in re.finditer(r"^## ([^\r\n]+)\r?$\n(.*?)(?=^## |\Z)", content, re.M | re.S):
            result[(path.relative_to(root).as_posix(), m[1].strip())] = m[2]
    return result


def ocurrencias(texto, root=ROOT):
    nombres = {p.name: p.relative_to(root).as_posix() for p in (root / CATALOGO).glob("*.md")}
    nombres.update({Path(k).stem: v for k, v in list(nombres.items())})
    matches = [(m, m[1].split("|", 1)[0], m[1].split("|", 1)[-1], "wiki") for m in WIKI.finditer(texto)]
    matches += [(m, m[2].strip("<>"), m[1], "markdown") for m in MD.finditer(texto)]
    for m, target, label, syntax in sorted(matches, key=lambda x: x[0].start()):
        target = unquote(target).replace("\\", "/")
        path, sep, heading = target.partition("#")
        if CATALOGO in path:
            path = path[path.index(CATALOGO):]
            if not path.endswith(".md"):
                path += ".md"
        elif path in nombres:
            path = nombres[path]
        else:
            continue
        if not sep:
            raise ValueError(f"Enlace al catálogo o set que requiere decisión editorial: {target}")
        yield m, path, heading, label, syntax


def elegir(path, heading, label, fichas, cache):
    # Las anclas de línea históricas no identifican cartas; resolver por la etiqueta.
    local_heading = label if re.fullmatch(r"L\d+", heading) else heading
    if local_heading == "Baloo - Pilote de livraison" and "Set 14 - " in path:
        # La ficha local conserva ambas lenguas e identifica la misma carta #188.
        local_heading = "Baloo - Delivery Pilot"
    body = fichas.get((path, local_heading))
    if body is None:
        raise ValueError(f"No existe ficha exacta: {path}#{local_heading}")
    number = re.match(r"Set (\d+) - ", Path(path).stem)
    if number is None:
        raise ValueError(f"Set especial pendiente: {path}#{local_heading}")
    setcode = number[1]
    data = json.loads((cache / f"set-{setcode}.json").read_text(encoding="utf-8"))
    cards = data.get("results", []) if isinstance(data, dict) else data
    candidates = [c for c in cards if c.get("lang") == "en"
                  and normalizar(nombre_carta(c)) == normalizar(local_heading)]
    image_id = re.search(r"crd_[a-z0-9]+", body)
    exact = [c for c in candidates if image_id and c["id"] == image_id[0]]
    if exact:
        candidates = exact
    else:
        # Elegir una impresión base solo si es inequívoca; nunca el primer resultado.
        base = [c for c in candidates if c["collector_number"].isdigit()
                and 1 <= int(c["collector_number"]) <= 204]
        if len(base) == 1:
            candidates = base
    if len(candidates) != 1:
        raise ValueError(f"Coincidencia ambigua/ausente: {path}#{local_heading}: "
                         + ", ".join(nombre_carta(c) + " #" + c["collector_number"] for c in candidates))
    card = candidates[0]
    cost = re.search(r"\*\*Coste:\*\* (\d+)", body)
    if cost and int(cost[1]) != card["cost"]:
        raise ValueError(f"Coste distinto: {path}#{local_heading}")
    uri = card.get("image_uris", {}).get("digital", {}).get("large")
    if not uri or urlparse(uri).scheme != "https":
        raise ValueError(f"Imagen HTTPS ausente: {path}#{local_heading}")
    return {"archivo_local": path, "epigrafe": heading, "ficha_verificada": local_heading,
            "nombre": card["name"], "version": card.get("version"), "set": setcode,
            "numero": card["collector_number"], "idioma": card["lang"], "id": card["id"],
            "imagen": uri, "obtenido": "2026-10-08", "estado": "resuelto"}


def sustituir(texto, mapa, root=ROOT):
    result = texto
    occurrences = list(ocurrencias(texto, root))
    for m, path, heading, label, _ in reversed(occurrences):
        key = path + "#" + heading
        result = result[:m.start()] + f"[{label}]({mapa[key]['imagen']})" + result[m.end():]
    return result, len(occurrences)


def enlace_verificado(set_name, heading, label=None):
    mapa = json.loads(MAPA.read_text(encoding="utf-8"))["cartas"]
    key = CATALOGO + set_name.removesuffix(".md") + ".md#" + heading
    if key not in mapa:
        raise ValueError("Carta sin URL verificada en el mapa de Lorcast: " + key)
    return f"[{label or heading}]({mapa[key]['imagen']})"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=ROOT / ".codex_tmp/lorcast-2026-10-08")
    parser.add_argument("--aplicar", action="store_true")
    args = parser.parse_args()
    fichas = fichas_locales()
    mapa = json.loads(MAPA.read_text(encoding="utf-8"))["cartas"] if MAPA.exists() else {}
    errors = []
    paths = archivos_activos()
    for p in paths:
        for _, local, heading, label, _ in ocurrencias(leer(ROOT / p)):
            key = local + "#" + heading
            if key in mapa:
                continue
            try:
                mapa[key] = elegir(local, heading, label, fichas, args.cache)
            except ValueError as exc:
                errors.append(str(exc))
    MAPA.write_text(json.dumps({"fecha": "2026-10-08", "cartas": mapa}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if errors:
        print(json.dumps({"errores": sorted(set(errors)), "resueltos": len(mapa)}, ensure_ascii=False, indent=2))
        return 1
    cambios, total = [], 0
    for p in paths:
        path = ROOT / p
        before = leer(path)
        after, count = sustituir(before, mapa)
        if before == after:
            continue
        total += count
        cambios.append({"archivo": p, "enlaces": count,
                        "antes_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                        "despues_sha256": hashlib.sha256(after.encode("utf-8")).hexdigest()})
        if args.aplicar:
            path.write_bytes(after.encode("utf-8"))
    informe = {"estado": "aplicado" if args.aplicar else "preparado", "enlaces": total,
               "archivos": len(cambios), "cambios": cambios}
    if cambios:
        (ROOT / ".github/planes/manifiesto-migracion-cartas.json").write_text(
            json.dumps(informe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in informe.items() if k != "cambios"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
