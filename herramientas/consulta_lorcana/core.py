"""Recuperación local de evidencia. No redacta rulings ni ejecuta contenido fuente."""
from __future__ import annotations

import argparse
import collections
from contextlib import closing
import difflib
import fnmatch
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sqlite3
import sys
import time
import unicodedata
import uuid
from urllib.parse import unquote
from datetime import date, datetime, timezone

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SCHEMA = 1
FOLDERS = {
    "00. Introducción": ("recursos", "didactico_no_normativo", "support"),
    "01. Reglas": ("estandar", "localizacion", "local"),
    "02. Listado de Cartas": ("estandar", "ficha_local_set", "card"),
    "03. Reglas de Torneo": ("torneo", "explicacion_local_politica", "local"),
    "04. Guia de correccion de jugadas": ("correcciones", "explicacion_local_politica", "local"),
    "05. Consejos de jueces": ("consejos", "consejo_no_normativo", "support"),
    "06. Reviews de jueces en torneos": ("experiencias", "experiencia_no_normativa", "support"),
    "07. Gestión de Aplicación Carde.io": ("carde", "operativo_no_normativo", "support"),
    "08. Consejos para jugadores": ("consejos", "consejo_no_normativo", "support"),
    "09. Recursos": ("recursos", "didactico_no_normativo", "support"),
    "10. Comunidad y actividades": ("comunidad", "explicacion_local_comunidad", "support"),
}
CONTROL = ["Documentacion Oficial/README.md",
           "01.1.a Official English Reference – Unmodified/00. Fuente actual.md"]
RULE = re.compile(r"^(\d+(?:\.\d+)*)\.\s+(.*)")
REFS = re.compile(r"\b\d+(?:\.\d+){1,4}\b")
OFFICIAL = re.compile(r"https://(?:files|cards|www)\.disneylorcana\.com/[^\s)\]>]+")
STOP = set("a al algo ante como con de del el en es esta este estos hay la las lo los me mi no o para por puedo que se si sin su sus un una y you your the this that of to in is it can do does if on with whenever during character personaje characters turn turno regla reglas cr consulta documenta".split())


def norm(s):
    s = unicodedata.normalize("NFKD", s.translate(str.maketrans({"–": "-", "—": "-", "’": "'", "‘": "'"})))
    return " ".join(re.findall(r"[a-z0-9]+", "".join(c for c in s.lower() if not unicodedata.combining(c))))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_text(path):
    return path.read_text(encoding="utf-8-sig")


def mode_of(question, explicit=False):
    m = re.match(r"^\s*(consulta|documenta|actualiza)\s*:\s*(.*)$", question, re.I | re.S)
    return (m.group(1).lower(), m.group(2)) if m else ("consulta" if explicit else "documenta", question)


def fecha_local():
    return date.today()


def pick_primary(root):
    """Los dos punteros activos deben acordar PDF y versión; no se elige por nombre/mtime."""
    pointer = read_text(root / CONTROL[1])
    m = re.search(r"Documentacion Oficial/([^`\]\n]+\.pdf)", pointer)
    if not m:
        raise ValueError("El puntero de fuente actual no identifica un PDF en Documentacion Oficial.")
    rel = "Documentacion Oficial/" + m.group(1)
    path = (root / rel).resolve()
    if path.parent != (root / "Documentacion Oficial").resolve() or not path.is_file():
        raise ValueError("PDF primario ausente o fuera de Documentacion Oficial: " + rel)
    readme = read_text(root / CONTROL[0])
    blocks = re.split(r"(?im)^## ", readme)
    active = next((b for b in blocks if path.name in b and re.search(r"\b\d+\.\d+\.\d+\b", b)), "")
    versions = re.findall(r"\b\d+\.\d+\.\d+\b", active)
    if path.name not in active or not versions or versions[0] not in pointer:
        raise ValueError("Los dos documentos de fuente actual discrepan. Corrígelos antes de indexar.")
    transition = load_json(HERE / "fuentes.json").get("primary_transition", {})
    if rel in (transition.get("previous_path"), transition.get("published_path")):
        # Los punteros mantienen primero el original previo para clientes ya abiertos.
        # La selección fechada se valida contra ambos documentos y los dos originales.
        for key in ("previous", "published"):
            candidate = transition[key + "_path"]
            original = (root / candidate).resolve()
            if original.parent != (root / "Documentacion Oficial").resolve() or not original.is_file():
                raise ValueError("Falta el original de la transición: " + candidate)
            if digest(original.read_bytes()) != transition[key + "_sha256"]:
                raise ValueError("El original de la transición ha cambiado: " + candidate)
            if original.name not in pointer or original.name not in readme or transition[key + "_version"] not in pointer or transition[key + "_version"] not in readme:
                raise ValueError("Los dos selectores deben documentar ambas versiones de la transición.")
        key = "previous" if fecha_local() < date.fromisoformat(transition["effective_on"]) else "published"
        return transition[key + "_path"], transition[key + "_version"]
    return rel, versions[0]


def inventory(root):
    config = load_json(HERE / "fuentes.json")
    primary, version = pick_primary(root)
    entries, excluded = {}, []
    discord_paths = set()
    # La procedencia de casos migrados puede constar solo en el índice manual.
    for idx in (root / "01. Reglas").rglob("ÍNDICE*.md"):
        for line in read_text(idx).splitlines():
            if "DISCORD" in line.upper():
                for target in re.findall(r"\]\(<([^>]+)>\)", line):
                    discord_paths.add((idx.parent / unquote(target)).as_posix())

    def add(path, scope, authority, kind, data=None):
        rel = path.relative_to(root).as_posix()
        data = path.read_bytes() if data is None else data
        entries[rel] = {"hash": digest(data), "size": len(data), "scope": scope,
                        "authority": authority, "kind": kind}

    for folder, (scope, authority, kind) in FOLDERS.items():
        for path in sorted((root / folder).rglob("*.md")):
            rel = path.relative_to(root).as_posix()
            data = path.read_bytes()
            text = data.decode("utf-8-sig")
            future = re.search(r"<!-- CR-ACTIVA-DESDE: (\d{4}-\d{2}-\d{2}) -->", text)
            if future and fecha_local() < date.fromisoformat(future.group(1)):
                excluded.append({"path": rel, "reason": "adaptación publicada con vigencia futura: " + future.group(1)})
                add(path, scope, "adaptacion_futura", "excluded", data)
                continue
            # Se excluye todo archivo que declare procedencia Discord, incluso un caso activo.
            if re.search(r"discord", text, re.I) or path.as_posix() in discord_paths:
                excluded.append({"path": rel, "reason": "procedencia Discord en texto o índice"})
                add(path, scope, authority, "excluded", data)
                continue
            if re.search(r"ya no debe utilizarse|se conserva como registro histórico", text, re.I):
                excluded.append({"path": rel, "reason": "documento declarado histórico"})
                add(path, scope, authority, "excluded", data)
                continue
            if path.name.startswith(("ÍNDICE", "Índice", "Plantilla")) or path.name == "Cartas de Lorcana.md":
                add(path, scope, authority, "control", data)
                continue
            if kind == "card" and not (path.name.startswith("Set ") or path.name.startswith("Illumineer")):
                excluded.append({"path": rel, "reason": "no es archivo de set"})
                continue
            if folder == "01. Reglas" and "/11. " in rel:
                authority, kind_here = "caso_interpretativo", "case"
            else:
                kind_here = kind
                authority = FOLDERS[folder][1]
            if folder == "01. Reglas" and ("/9. Resúmenes/" in rel or "/10. Artículos/" in rel):
                authority, kind_here = "resumen_interpretativo", "support"
            if "coconut" in norm(rel):
                scope_here = "coconut"
            elif "pack rush" in norm(rel):
                scope_here = "pack_rush"
            elif "multijugador" in norm(rel) or "multiplayer" in norm(rel):
                scope_here = "multijugador"
            else:
                scope_here = scope
            if "Protocolos personales" in rel:
                authority, kind_here = "consejo_no_normativo", "support"
            add(path, scope_here, authority, kind_here, data)
    for rel in CONTROL:
        add(root / rel, "seleccion_fuentes", "control", "control")
    add(root / primary, "estandar", "regla_oficial", "cr")
    for path in sorted((root / "Documentacion Oficial").glob("*.pdf")):
        if path.relative_to(root).as_posix() == primary:
            continue
        if path.name in config.get("superseded_pdfs", []):
            rel = path.relative_to(root).as_posix()
            excluded.append({"path": rel, "reason": "política sustituida por un original posterior"})
            add(path, "torneo", "historico", "excluded")
            continue
        for spec in config["pdfs"]:
            if fnmatch.fnmatch(path.name, spec["pattern"]):
                add(path, spec["scope"], spec["authority"], spec["kind"])
                break
    for spec in config.get("official_markdown", []):
        # Una transcripción identificada no convierte otros Markdown en fuentes oficiales.
        for key, hash_key in (("path", "sha256"), ("raw_path", "raw_sha256")):
            path = (root / spec[key]).resolve()
            if path.parent != (root / "Documentacion Oficial").resolve() or not path.is_file():
                raise ValueError("Fuente oficial ausente o fuera de su carpeta: " + spec[key])
            if digest(path.read_bytes()) != spec[hash_key]:
                raise ValueError("Fuente oficial modificada sin verificar: " + spec[key])
        path = root / spec["path"]
        add(path, spec["scope"], spec["authority"], spec["kind"])
    # Las herramientas/configuración no son evidencia, pero invalidan un índice de otra implementación.
    signature = digest(b"".join((HERE / x).read_bytes() for x in ("core.py", "fuentes.json", "sinonimos.json")))
    # El texto operativo de las erratas cambia por fecha aunque la ficha impresa
    # no cambie. Impide reutilizar esos fragmentos al cruzar su fecha de aplicación.
    applicability = [(s["path"], s["name"], fecha_local() >= date.fromisoformat(s["effective_on"]))
                     for s in config.get("card_errata", [])]
    if applicability:
        signature = digest((signature + json.dumps(applicability, ensure_ascii=False)).encode())
    return entries, {"primary": primary, "version": version, "signature": signature, "excluded": excluded}


def delta(old, current):
    added = sorted(current.keys() - old.keys())
    removed = sorted(old.keys() - current.keys())
    modified = sorted(p for p in current.keys() & old.keys() if current[p]["hash"] != old[p]["hash"])
    renames = []
    for p in added[:]:
        previous = next((q for q in removed if old[q]["hash"] == current[p]["hash"]), None)
        if previous:
            renames.append({"from": previous, "to": p})
            removed.remove(previous)
            added.remove(p)
    return {"added": added, "modified": modified, "removed": removed, "renamed": renames}


def extract_pdf(path):
    """Conserva texto bruto y texto con símbolos mapeados por fuente (nunca reemplazo global)."""
    try:
        import fitz
    except ImportError as exc:
        raise RuntimeError("Falta PyMuPDF: python -m pip install -r herramientas/consulta_lorcana/requirements.txt") from exc
    profile_hash = digest(path.read_bytes())
    # La codificación de las fuentes subset cambia entre PDF; ! no significa siempre agotamiento.
    profile = load_json(HERE / "fuentes.json").get("glyph_maps", {}).get(profile_hash)
    glyphs = profile["symbols"] if profile else {}
    result, counts = [], collections.Counter()
    with fitz.open(path) as doc:
        if doc.is_encrypted:
            raise ValueError("PDF cifrado: " + str(path))
        for n, page in enumerate(doc, 1):
            lines = []
            for block in page.get_text("dict", sort=True)["blocks"]:
                for line in block.get("lines", []):
                    if line["bbox"][1] > page.rect.height - 48:
                        continue  # pie recurrente, copyright y número de página
                    raw, mapped = "", ""
                    for span in line["spans"]:
                        raw += span["text"]
                        if "Glyph" in span["font"]:
                            if profile is None and span["text"].strip():
                                raise ValueError(f"Símbolos sin perfil verificado: {path.name}, SHA256 {profile_hash}. Inspecciona el PDF y añade glyph_maps en fuentes.json; no se deduce el símbolo por su código.")
                            for c in span["text"]:
                                if c not in glyphs and not c.isspace():
                                    raise ValueError(f"Símbolo desconocido {c!r}, página {n}: {path.name}")
                                counts[c] += 1
                                mapped += glyphs.get(c, c)
                        else:
                            mapped += unicodedata.normalize("NFKC", span["text"])
                    lines.append((line["bbox"][1], line["bbox"][0], raw.strip(), mapped.strip()))
            lines.sort(key=lambda x: (round(x[0], 1), x[1]))
            lines = [x for x in lines if not (x[0] > page.rect.height - 110 and
                     (x[2].startswith(("©", "Based on")) or x[2] == "disneylorcana.com" or x[2].isdigit()))]
            raw = "\n".join(x[2] for x in lines if x[2])
            mapped = "\n".join(x[3] for x in lines if x[3])
            if len(mapped) < 80 or "\ufffd" in mapped or "\x00" in mapped:
                raise ValueError(f"Extracción ilegible o página sin texto: {path.name}, p. {n}. Requiere revisión/OCR.")
            result.append({"page": n, "raw": raw, "text": mapped})
    return result, {"pages": len(result), "glyphs": dict(counts), "glyph_profile": profile_hash if counts else None,
                    "glyph_verification": profile.get("verified") if profile else None, "extractor": "PyMuPDF/font-aware"}


def chunk_base(title, text, raw=None, **fields):
    return {"title": title, "text": text, "raw_text": raw if raw is not None else text,
            "rule": None, "lines": None, "pages": None, "context": [],
            "references": sorted(set(REFS.findall(text))), **fields}


def cr_chunks(pages):
    out, current, headings = [], None, {}
    last = ()
    for page in pages[2:]:  # portada e índice no contienen reglas
        for raw, text in zip(page["raw"].splitlines(), page["text"].splitlines()):
            if re.match(r"^(GLOSSARY|UPDATE SUMMARY|PREVIOUS UPDATE)", text, re.I):
                if current:
                    out.append(current)
                    current = None
                return out
            m = RULE.match(text)
            heading = re.match(r"^(\d+(?:\.\d+)?)\.\s+([A-Z].*)", text)
            if m:
                rid = m.group(1)
                depth = len(rid.split("."))
                if depth <= 2:
                    headings[depth] = text
                    if depth == 1:
                        headings.pop(2, None)
                order = tuple(map(int, rid.split(".")))
                if order <= last:
                    raise ValueError("Orden de extracción/identificador duplicado en CR: " + rid)
                last = order
                if current:
                    out.append(current)
                current = chunk_base("CR " + rid, text, raw, rule=rid, pages=[page["page"], page["page"]],
                                     context=list(headings.values()))
            elif heading:
                headings[len(heading.group(1).split("."))] = text
                if len(heading.group(1).split(".")) == 1:
                    headings.pop(2, None)
            elif current:
                current["text"] += "\n" + text
                current["raw_text"] += "\n" + raw
                current["pages"][1] = page["page"]
    if current:
        out.append(current)
    return out


def markdown_chunks(text, kind, default_title=""):
    lines = text.splitlines()
    title = next((x.lstrip("# ") for x in lines if x.startswith("# ")), default_title)
    if kind == "card":
        starts = [i for i, line in enumerate(lines) if line.startswith("## ")]
    elif kind == "case":
        starts = [0]  # caso completo: duda, respuesta, fundamento y estado no se separan
    else:
        starts = [0] + [i for i, line in enumerate(lines) if i and re.match(r"^#{2,3} ", line)]
    result = []
    for j, start in enumerate(starts):
        end = starts[j + 1] if j + 1 < len(starts) else len(lines)
        section = "\n".join(lines[start:end]).strip()
        if not section:
            continue
        heading = lines[start].lstrip("# ") if lines[start].startswith("#") else title
        if kind == "case":
            heading = default_title
        result.append(chunk_base(heading or title, section, lines=[start + 1, end], context=[title]))
    return result


def pdf_sections(pages, title):
    """Secciones completas de políticas; no corta un remedio al cambiar de página."""
    output, current = [], None
    for page in pages:
        if "CONTENTS" in page["text"]:
            continue
        lines = list(zip(page["raw"].splitlines(), page["text"].splitlines()))
        skip = False
        for i, (raw, text) in enumerate(lines):
            if skip:
                skip = False
                continue
            heading = text
            # Algunos encabezados tienen número y título en cajas PDF distintas.
            if re.fullmatch(r"\d+(?:\.\d+)+\.?", text) and i + 1 < len(lines):
                next_raw, next_text = lines[i + 1]
                if re.fullmatch(r"[A-Z][A-Za-z /&–()\-]+", next_text):
                    heading = text + " " + next_text
                    raw += "\n" + next_raw
                    text += "\n" + next_text
                    skip = True
            m = re.match(r"^(\d+(?:\.\d+)+)\.?\s+([A-Z][A-Za-z /&–()\-]+)$", heading)
            if m:
                if current:
                    output.append(current)
                current = chunk_base(title + " · " + heading, text, raw,
                                     policy_section=m.group(1), pages=[page["page"], page["page"]])
            elif current:
                current["text"] += "\n" + text
                current["raw_text"] += "\n" + raw
                current["pages"][1] = page["page"]
    if current:
        output.append(current)
    return output


def glossary_chunks(pages):
    output, current, active, inline_format = [], None, False, None
    for page in pages[2:]:
        for raw, text in zip(page["raw"].splitlines(), page["text"].splitlines()):
            if text.upper() == "GLOSSARY":
                active = True
                continue
            if active and re.match(r"^(UPDATE SUMMARY|PREVIOUS UPDATE)", text, re.I):
                if current:
                    output.append(current)
                return output
            if not active:
                continue
            if inline_format is None:
                inline_format = bool(re.match(r"^[A-Za-z][A-Za-z ,/()'’\-]+?:\s", text))
            # Entradas cortas del glosario, separadas de sus párrafos por el PDF original.
            inline = re.match(r"^([A-Za-z][A-Za-z ,/()'’\-]+?)(?:\s+\{[A-Z]+\})?:\s+(.+)$", text)
            heading = not inline_format and len(text) < 75 and re.fullmatch(r"[A-Za-z][A-Za-z ,/()'’\-]+(?:\s+\{[A-Z]+\})?", text) and not text.endswith((".", ":"))
            if inline and inline_format:
                if current:
                    output.append(current)
                term = inline.group(1)
                current = chunk_base("Glosario CR · " + term, text, raw,
                                     glossary_term=term, pages=[page["page"], page["page"]])
                continue
            if heading:
                if current:
                    output.append(current)
                term = re.sub(r"\s+\{[A-Z]+\}$", "", text)
                current = chunk_base("Glosario CR · " + term, text, raw,
                                     glossary_term=term, pages=[page["page"], page["page"]])
            elif current:
                current["text"] += "\n" + text
                current["raw_text"] += "\n" + raw
                current["pages"][1] = page["page"]
    if current:
        output.append(current)
    return output


def parse_source(root, rel, spec, selection):
    path = root / rel
    kind = spec["kind"]
    meta = dict(spec, version=None, effective_date=None, documented_urls=[], limitations=[], coverage=None)
    if kind in ("control", "excluded"):
        return [], meta
    if path.suffix == ".pdf":
        pages, qa = extract_pdf(path)
        meta["extraction"] = qa
        first = pages[0]["text"]
        v = re.search(r"Version\s+([\d.]+)", first, re.I)
        dt = re.search(r"Effective\s+([^\n]+)", first, re.I)
        meta["version"] = v.group(1) if v else None
        meta["effective_date"] = dt.group(1).strip() if dt else None
        if kind == "cr":
            if meta["version"] != selection["version"]:
                raise ValueError("Versión interior del PDF distinta de la selección documentada.")
            chunks = cr_chunks(pages)
            if len(chunks) < 200:
                raise ValueError("Extracción CR incompleta: menos de 200 reglas.")
            ids = {c["rule"] for c in chunks}
            for c in chunks:
                c["references"] = sorted(set(REFS.findall(c["text"])) - {c["rule"]})
            meta["extraction"]["rules"] = len(ids)
            meta["extraction"]["cross_page_rules"] = [c["rule"] for c in chunks if c["pages"][0] != c["pages"][1]]
            meta["extraction"]["unresolved_references"] = sorted({r for c in chunks for r in c["references"]
                if len(r.split(".")) >= 3 and r not in ids})
            chunks.extend(glossary_chunks(pages))
        else:
            chunks = pdf_sections(pages, path.stem) if kind in ("tournament", "correction") else []
            if not chunks:
                chunks = [chunk_base(path.stem + f" · p. {p['page']}", p["text"], p["raw"], pages=[p["page"], p["page"]]) for p in pages]
        meta["documented_urls"] = sorted(set(OFFICIAL.findall("\n".join(p["text"] for p in pages))))
        config_url = load_json(HERE / "fuentes.json")["verified_urls"].get(path.name)
        meta["official_link"] = config_url
        observation = load_json(HERE / "fuentes.json").get("maintenance_observations", {}).get(path.name)
        if observation:
            meta["maintenance_observation"] = observation
            meta["limitations"].append(observation["limitation"])
        if not meta["version"] and not meta["effective_date"]:
            meta["limitations"].append("El original no declara versión/fecha identificables; no se deducen del nombre.")
    else:
        text = read_text(path)
        chunks = markdown_chunks(text, kind, path.stem)
        meta["documented_urls"] = sorted(set(OFFICIAL.findall(text)))
        official = next((s for s in load_json(HERE / "fuentes.json").get("official_markdown", [])
                         if s["path"] == rel), None)
        if official:
            meta["effective_date"] = official["effective_on"]
            meta["official_link"] = {"url": official["url"], "verified_on": official.get("verified_on")}
            meta["limitations"].extend(official.get("limitations", []))
        if kind == "card":
            intro = text.split("\n## ", 1)[0]
            meta["coverage"] = "parcial_declarado" if "parcial" in norm(intro) else "completitud_no_acreditada"
            meta["limitations"].append("Ficha local del set; integridad del listado no garantizada salvo declaración comprobada.")
            for c in chunks:
                c["card_name"] = c["title"]
                c["card_status"] = "ficha_disponible" if "**Tipo:**" in c["text"] and "**Set:**" in c["text"] else "ficha_incompleta"
                if c["card_status"] == "ficha_incompleta":
                    c["limitations"] = ["Faltan campos básicos de la ficha; no cerrar ruling."]
                c["documented_fields"] = re.findall(r"\*\*([^*]+):\*\*", c["text"])
                c["ability_section_present"] = "**Habilidades:**" in c["text"]
                errata = next((s for s in load_json(HERE / "fuentes.json").get("card_errata", [])
                               if s["path"] == rel and s["name"] == c["title"]), None)
                if errata:
                    if errata["printed"] not in c["text"] or errata.get("corrected", "") not in c["text"]:
                        raise ValueError("Errata no coincide con ficha literal: " + c["title"])
                    active = fecha_local() >= date.fromisoformat(errata["effective_on"])
                    c["errata"] = {"effective_on": errata["effective_on"], "official_url": errata["url"],
                                   "state": "vigente" if active else "anunciada; aún no vigente"}
                    # El fragmento literal conserva líneas y prueba de integridad. La vista
                    # operativa se entrega aparte para no confundir el impreso con la errata.
                    c["operative_ability"] = (errata.get("corrected") if active else errata["printed"])
                    c["operative_text_status"] = ("corregido_oficial" if errata.get("corrected") else
                                                    "nueva_redaccion_completa_no_publicada") if active else "impreso_previo"
                    if active and not errata.get("corrected"):
                        c["operative_clarification"] = errata["clarification"]
                    c["errata_warning"] = ("Errata vigente: usar texto corregido o aclaración oficial, no el impreso histórico."
                                            if active else "Errata anunciada para " + errata["effective_on"] + "; conservar el texto vigente anterior hasta esa fecha.")
            meta["card_count"] = len(chunks)
            numbers = [int(n) for n in re.findall(r"\*\*Set:\*\*[^\n]*#(\d+)", text)]
            # Algunos sets usan #N para el número del set, otros para la carta; no deducir huecos de colección.
            meta["numbers_documented_in_set_field"] = sorted(set(numbers)) if numbers else None
            meta["duplicate_full_names"] = sorted(name for name, n in collections.Counter(c["title"] for c in chunks).items() if n > 1)
        elif kind == "local" and spec["scope"] in ("torneo", "correcciones"):
            meta["limitations"].append("Explicación local; contrastar la sección con el original antes de aplicar política.")
        if kind == "case":
            meta["limitations"].append("Caso interpretativo local, no FAQ oficial; contrastar cartas y reglas primarias.")
        observations = load_json(HERE / "fuentes.json").get("local_observations", {})
        if rel in observations:
            meta["limitations"].append(observations[rel])
    return chunks, meta


def ro_connection(db):
    c = sqlite3.connect(db.resolve().as_uri() + "?mode=ro&immutable=1", uri=True)
    c.row_factory = sqlite3.Row
    return c


def metadata(c):
    return {r[0]: json.loads(r[1]) for r in c.execute("select key,value from meta")}


def old_sources(c):
    return {r["path"]: dict(json.loads(r["meta"]), id=r["id"]) for r in c.execute("select * from sources")}


def freshness(root, db, current=None, selection=None):
    start = time.perf_counter()
    if current is None:
        current, selection = inventory(root)
    result = {"usable": False, "current": False, "changes": None, "selection": selection}
    if db.is_file():
        try:
            with closing(ro_connection(db)) as c:
                meta = metadata(c)
                changes = delta(old_sources(c), current)
                result.update(usable=meta.get("schema") == SCHEMA, changes=changes, built_at=meta.get("built_at"),
                              backend=meta.get("backend"), source_count=c.execute("select count(*) from sources where kind not in ('control','excluded')").fetchone()[0],
                              chunk_count=c.execute("select count(*) from chunks").fetchone()[0])
                result["current"] = result["usable"] and not any(changes.values()) and meta.get("selection", {}).get("signature") == selection["signature"] and meta.get("selection", {}).get("primary") == selection["primary"]
        except (sqlite3.Error, ValueError) as exc:
            result["error"] = str(exc)
    failure = db.parent / "last_failure.json"
    if failure.is_file():
        result["last_failed_update"] = load_json(failure)
    result["validation_ms"] = round((time.perf_counter() - start) * 1000, 3)
    return result


def create_schema(c, force_scan=False):
    c.executescript("""
        create table meta(key text primary key,value text not null);
        create table sources(id text primary key,path text unique,kind text,meta text);
        create table chunks(id text primary key,source_id text,kind text,scope text,authority text,
                            rule text,card_key text,payload text,search text);
        create index by_rule on chunks(rule); create index by_card on chunks(card_key);
        create index by_source on chunks(source_id);
    """)
    backend = "scan"
    if not force_scan:
        try:
            c.execute("create virtual table search_fts using fts5(id UNINDEXED, title, body, tokenize='unicode61 remove_diacritics 2')")
            backend = "fts5"
        except sqlite3.OperationalError:
            pass
    return backend


def populate(c, root, entries, selection, previous=None, force_scan=False):
    backend = create_schema(c, force_scan)
    old = old_sources(previous) if previous else {}
    unused = set(old) - set(entries)
    reused, extracted = 0, 0
    for rel, spec in entries.items():
        prior = old.get(rel)
        if prior is None:
            renamed = next((q for q in sorted(unused) if old[q]["hash"] == spec["hash"]), None)
            if renamed:
                prior = old[renamed]
                unused.remove(renamed)
        sid = prior["id"] if prior else str(uuid.uuid5(uuid.NAMESPACE_URL, rel))
        if prior and prior["hash"] == spec["hash"] and prior["kind"] == spec["kind"] and metadata(previous)["selection"]["signature"] == selection["signature"]:
            source_meta = {k: v for k, v in prior.items() if k != "id"}
            chunks = [json.loads(r[0]) for r in previous.execute("select payload from chunks where source_id=?", (sid,))]
            reused += 1
        else:
            chunks, source_meta = parse_source(root, rel, spec, selection)
            extracted += 1
        c.execute("insert into sources values(?,?,?,?)", (sid, rel, spec["kind"], json.dumps(source_meta, ensure_ascii=False)))
        for i, payload in enumerate(chunks):
            scope = spec["scope"]
            if spec["kind"] == "cr":
                if (payload.get("rule") or "").startswith("9.") or payload.get("rule") == "9":
                    scope = "multijugador"
                elif (payload.get("rule") or "").startswith("10.2"):
                    scope = "pack_rush"
            cid = digest((sid + ":" + (payload.get("rule") or payload["title"] + ":" + str(i))).encode())[:24]
            payload.update(id=cid, source_id=sid, path=rel, kind=spec["kind"], scope=scope, authority=spec["authority"])
            search = norm(payload["title"] + " " + payload["text"] + " " + rel)
            c.execute("insert into chunks values(?,?,?,?,?,?,?,?,?)", (cid, sid, spec["kind"], scope, spec["authority"], payload.get("rule"), norm(payload.get("card_name", "")), json.dumps(payload, ensure_ascii=False), search))
            if backend == "fts5":
                c.execute("insert into search_fts values(?,?,?)", (cid, norm(payload["title"]), search))
    for key, value in {"schema": SCHEMA, "selection": selection, "backend": backend,
                       "built_at": datetime.now(timezone.utc).isoformat(), "update": {"reused": reused, "parsed": extracted}}.items():
        c.execute("insert into meta values(?,?)", (key, json.dumps(value, ensure_ascii=False)))
    c.commit()
    return {"backend": backend, "reused": reused, "parsed": extracted}


def update(root, db, force_scan=False):
    """Construcción en fichero separado, publicación atómica; nunca pisa un índice fallido."""
    db.parent.mkdir(parents=True, exist_ok=True)
    temp = db.parent / ("build-" + uuid.uuid4().hex + ".sqlite")
    previous = None
    try:
        entries, selection = inventory(root)
        before = freshness(root, db, entries, selection)
        if before["current"] and before.get("backend") == ("scan" if force_scan else "fts5"):
            return dict(before, update={"reused": len(entries), "parsed": 0}, unchanged=True)
        if before["usable"]:
            previous = ro_connection(db)
        with closing(sqlite3.connect(temp)) as c:
            report = populate(c, root, entries, selection, previous, force_scan)
            if c.execute("pragma integrity_check").fetchone()[0] != "ok":
                raise ValueError("Integridad SQLite fallida")
        # Detecta ediciones concurrentes durante la construcción antes de publicarla.
        final_entries, final_selection = inventory(root)
        if entries != final_entries or selection != final_selection:
            raise ValueError("Fuentes cambiaron durante la actualización. Reintenta.")
        if previous:
            previous.close()
            previous = None
        os.replace(temp, db)
        (db.parent / "last_failure.json").unlink(missing_ok=True)
        return {"ok": True, "update": report, "changes": before.get("changes"), "selection": selection}
    except Exception as exc:
        (db.parent / "last_failure.json").write_text(json.dumps({"error": str(exc), "at": datetime.now(timezone.utc).isoformat(), "preserved_last_index": db.exists()}, ensure_ascii=False), encoding="utf-8")
        raise
    finally:
        if previous:
            previous.close()
        temp.unlink(missing_ok=True)


def expand_query(question):
    q = norm(question)
    config = load_json(HERE / "sinonimos.json")
    tokens = [t for t in q.split() if t not in STOP and len(t) > 1]
    expanded = set(tokens)
    for group in config["groups"]:
        if any(re.search(r"\b" + re.escape(norm(t)) + r"\b", q) for t in group):
            expanded.update(t for phrase in group for t in norm(phrase).split() if t not in STOP)
    hints = []
    for hint in config["rule_hints"]:
        if any(re.search(r"\b" + re.escape(norm(t)) + r"\b", q) for t in hint["terms"]):
            hints.extend(hint["rules"])
    return tokens, sorted(expanded), list(dict.fromkeys(hints))


def search(c, question, kinds, scopes, limit=8):
    tokens, expanded, _ = expand_query(question)
    if not expanded:
        return []
    kinds_sql = ",".join("?" for _ in kinds)
    scope_sql = ",".join("?" for _ in scopes)
    filters = f"c.kind in ({kinds_sql}) and c.scope in ({scope_sql})"
    if metadata(c)["backend"] == "fts5":
        expression = " OR ".join('"' + t + '"' for t in expanded[:70])
        rows = c.execute(f"select c.payload,c.search from search_fts join chunks c on c.id=search_fts.id where search_fts match ? and {filters} order by bm25(search_fts,0,5,1) limit 120", [expression, *kinds, *scopes]).fetchall()
    else:
        rows = c.execute(f"select c.payload,c.search from chunks c where {filters}", [*kinds, *scopes]).fetchall()
    ranked = []
    for row in rows:
        p = json.loads(row["payload"])
        title, body = norm(p["title"]), row["search"]
        words = set(body.split())
        score = sum(5 if t in title.split() else 1 for t in tokens if t in words)
        score += sum(.2 for t in expanded if t in words)
        if norm(question) in body:
            score += 8
        if score:
            ranked.append((score, p))
    ranked.sort(key=lambda x: (-x[0], x[1]["path"], x[1]["id"]))
    return [dict(p, retrieval_score=round(s, 2)) for s, p in ranked[:limit]]


def exact_rules(c, number, scope=None):
    number = number.strip().removeprefix("CR ").rstrip(".")
    rows = c.execute("select payload from chunks where kind='cr' and (rule=? or rule like ?) order by rowid", (number, number + ".%")).fetchall()
    return [json.loads(r[0]) for r in rows if scope is None or json.loads(r[0])["scope"] == scope]


def cards(c, name):
    key = norm(name)
    exact = [json.loads(r[0]) for r in c.execute("select payload from chunks where kind='card' and card_key=? order by id", (key,))]
    if exact:
        # Reimpresiones idénticas no son versiones distintas; conserva todas las procedencias.
        distinct = {norm(p["text"].split("**Habilidades:**", 1)[-1].split("**Flavor text:**", 1)[0]) for p in exact}
        status = "incompleta" if any(p.get("card_status") == "ficha_incompleta" for p in exact) else "exacta" if len(distinct) == 1 else "multiples_fichas_comprobar"
        return {"status": status, "matches": exact, "candidates": []}
    prefix = [json.loads(r[0]) for r in c.execute("select payload from chunks where kind='card' and card_key like ? order by card_key,id", (key + " %",))]
    if prefix:
        return {"status": "ambigua", "matches": [], "candidates": prefix}
    keys = {r[0] for r in c.execute("select distinct card_key from chunks where kind='card'")}
    near = difflib.get_close_matches(key, sorted(keys), n=6, cutoff=.55)
    candidates = [json.loads(r[0]) for k in near for r in c.execute("select payload from chunks where kind='card' and card_key=?", (k,))]
    return {"status": "ausente", "matches": [], "candidates": candidates}


def decorate(c, root, payload):
    meta = json.loads(c.execute("select meta from sources where id=?", (payload["source_id"],)).fetchone()[0])
    absolute = (root / payload["path"]).resolve().as_posix()
    location = f":{payload['lines'][0]}" if payload["lines"] else ""
    p = dict(payload, absolute_path=absolute, source_hash=meta["hash"], version=meta.get("version"),
             effective_date=meta.get("effective_date"), source_limitations=meta.get("limitations", []),
             coverage=meta.get("coverage"), documented_urls=meta.get("documented_urls", []),
             maintenance_observation=meta.get("maintenance_observation"),
             local_link=f"[{payload['title']}](<{absolute}{location}>)", citation_verified=True)
    # El bruto sigue íntegro en el índice; evita duplicar todo el texto en la respuesta al agente.
    p.pop("raw_text", None)
    p["raw_text_preserved_in_index"] = True
    link = meta.get("official_link")
    p["official_url"] = link["url"] if link else None
    p["official_url_verified_on"] = link.get("verified_on") if link else None
    if link and link.get("verified_on") and payload["pages"]:
        p["official_page_link"] = link["url"] + "#page=" + str(payload["pages"][0])
    # Integridad normativa != score. No se añade confianza estadística.
    return p


def policy_context(c, results):
    output = list(results)
    for p in results[:2]:
        if p["kind"] not in ("tournament", "correction") or p.get("policy_section"):
            continue
        page = p["pages"][0]
        for row in c.execute("select payload from chunks where source_id=?", (p["source_id"],)):
            extra = json.loads(row[0])
            if abs(extra["pages"][0] - page) <= 1 and extra["id"] not in {x["id"] for x in output}:
                output.append(extra)
    return output


def verify_fragments(c, root, packets):
    """Relee fuentes citadas (hash), y texto exacto de líneas MD. PDF se contrasta por hash completo."""
    seen = {}
    for p in packets:
        path = root / p["path"]
        if p["path"] not in seen:
            seen[p["path"]] = path.read_bytes()
        if digest(seen[p["path"]]) != p["source_hash"]:
            raise ValueError("Fuente cambió durante la consulta: " + p["path"])
        if p["lines"]:
            start, end = p["lines"]
            direct = "\n".join(seen[p["path"]].decode("utf-8-sig").splitlines()[start-1:end]).strip()
            if direct != p["text"]:
                raise ValueError("Fragmento no coincide con líneas actuales: " + p["path"])


def query(root, db, question, card_names=(), rule_numbers=(), scope=None, explicit=True, limit=5):
    start = time.perf_counter()
    mode, question = mode_of(question, explicit)
    if mode == "actualiza":
        return {"mode": mode, "action_required": "Ejecutar actualizar; consultar nunca escribe."}
    entries, selection = inventory(root)
    state = freshness(root, db, entries, selection)
    state["validation_ms"] = round((time.perf_counter() - start) * 1000, 3)
    temporary = not state["current"]
    if temporary:
        c = sqlite3.connect(":memory:")
        c.row_factory = sqlite3.Row
        populate(c, root, entries, selection)
    else:
        c = ro_connection(db)
    try:
        q = norm(question)
        scope = scope or ("coconut" if "coconut" in q else "pack_rush" if "pack rush" in q else "multijugador" if "multijugador" in q or "multiplayer" in q else "estandar")
        scopes = ["estandar", scope]
        tokens, _, hints = expand_query(question)
        explicit_rules = list(rule_numbers) + re.findall(r"(?<!\d)\d+(?:\.\d+){1,4}(?!\d)", question)
        detected = []
        catalog = c.execute("select distinct card_key,json_extract(payload,'$.card_name') as name from chunks where kind='card'").fetchall()
        for row in catalog:
            if re.search(r"\b" + re.escape(row["card_key"]) + r"\b", q):
                detected.append(row["name"])
        # Nombre explícito de versión ausente: nunca sustituir por una carta parecida.
        absent = re.findall(r"([A-Z][\w'’]+(?:\s+[A-Z][\w'’]+){0,3}\s*[-–]\s*[A-Z][\w'’]+(?:\s+(?:[A-Z][\w'’]+|into|the|of|a|in|for)){0,4})", question)
        names = list(dict.fromkeys([*card_names, *detected, *absent]))
        if not names:
            bare = [r["name"].split(" - ")[0] for r in catalog if " - " in r["name"]]
            names = sorted({n for n in bare if re.search(r"\b" + re.escape(norm(n)) + r"\b", q)})
        resolutions = [{"requested": n, **cards(c, n)} for n in names]
        card_packets = [p for res in resolutions for p in res["matches"]]
        missing_rule_numbers = [n for n in dict.fromkeys(explicit_rules) if not exact_rules(c, n)]
        primary = []
        for rid in list(dict.fromkeys(explicit_rules + hints)):
            primary.extend(exact_rules(c, rid) if rid in explicit_rules else exact_rules(c, rid, "estandar"))
        primary.extend(search(c, question, ["cr"], scopes, limit))
        primary = list({p["id"]: p for p in primary}.values())
        # Referencias inmediatas de las reglas solicitadas; las secciones amplias se expanden con regla.
        referenced = []
        unresolved = []
        for p in primary[:8]:
            for number in p.get("references", []):
                if len(number.split(".")) < 3:
                    continue
                linked = c.execute("select payload from chunks where kind='cr' and rule=?", (number,)).fetchone()
                if linked:
                    referenced.append(json.loads(linked[0]))
                else:
                    unresolved.append(number)
        primary = list({p["id"]: p for p in primary + referenced}.values())
        is_policy = scope in ("torneo", "correcciones") or any(t in q for t in ("torneo", "tournament", "missed", "olvid", "omitid", "sancion", "warning", "correccion", "caution", "takeback", "slow play", "juego lento", "dispositivos electronicos", "minnie mouse practical traveler"))
        policy = policy_context(c, search(c, question, ["tournament", "correction"], ["torneo", "correcciones"], 2)) if is_policy else []
        # Los originales de políticas están en inglés. Una pregunta en español
        # sobre un disparo perdido debe recuperar su sección, no solo Lore Guides.
        missed_trigger = any(t in q for t in ("missed trigger", "lore olvidad", "efecto disparado perdido")) or (
            any(t in q for t in ("disparo", "habilidad disparada", "trigger")) and
            any(t in q for t in ("olvid", "perdid", "omitid")))
        if is_policy and missed_trigger:
            decisive_policy = search(c, "Missed Trigger", ["correction"], ["correcciones"], 2)
            policy = list({p["id"]: p for p in decisive_policy + policy}.values())
        special = search(c, question, ["special"], [scope], 2) if scope == "coconut" else []
        official_notes = search(c, question, ["release"], ["estandar"], 1)
        spanish = search(c, question, ["local"], [*scopes, "torneo", "correcciones"] if is_policy else scopes, limit)
        local_numbers = list(dict.fromkeys(explicit_rules + [p["rule"] for p in primary[:8] if p.get("rule")]))
        localized = []
        for row in c.execute("select payload from chunks where kind='local'"):
            p = json.loads(row[0])
            if p["scope"] not in scopes:
                continue
            # Número exacto, no una coincidencia de tokens separados (1, 12, 2).
            if any(re.search(r"(?<![\d.])" + re.escape(n) + r"(?![\d.])", p["text"]) for n in local_numbers):
                localized.append(p)
        spanish = list({p["id"]: p for p in localized + spanish}.values())[:limit]
        # Amplía con localización por identificadores, sin convertirla en autoridad primaria.
        if explicit_rules:
            spanish = search(c, " ".join(explicit_rules), ["local"], scopes, limit) + spanish
            spanish = list({p["id"]: p for p in spanish}.values())[:limit]
        case_candidates = search(c, question, ["case"], [scope] if scope != "estandar" else scopes, 15)
        case = next(([p] for p in case_candidates if not names or any(norm(n) in norm(p["text"] + p["path"]) for n in names)), [])
        support = search(c, question, ["support"], ["consejos", "experiencias", "carde", "recursos", "comunidad"], 2)
        warnings = []
        if missing_rule_numbers:
            warnings.append("Regla exacta ausente en la CR seleccionada: " + ", ".join(missing_rule_numbers) + ". Los resultados relacionados no la sustituyen.")
        if re.search(r"\b(old|legacy|antigua|antiguas|historica|historicas)\b|cr 1 x|cr 2 1 0", q):
            warnings.append("Las fuentes históricas/legacy están excluidas. Este paquete usa exclusivamente la CR local identificada, no recupera versiones antiguas.")
        if unresolved:
            warnings.append("Referencias internas del PDF sin destino: " + ", ".join(sorted(set(unresolved))) + ". No corregirlas por suposición.")
        if temporary:
            warnings.append("Índice ausente/desactualizado: lectura directa y recuperación en memoria; no se escribió ningún archivo.")
        if any(res["status"] != "exacta" for res in resolutions):
            warnings.append("Carta ausente, ambigua o con fichas distintas: confirmar nombre/versión y texto completo antes del ruling.")
        if is_policy and not c.execute("select 1 from sources where kind='correction'").fetchone():
            warnings.append("Sin original local de Play Correction Guidelines: las correcciones locales no acreditan la política oficial ni su vigencia.")
        if is_policy:
            for row in c.execute("select meta from sources where kind='tournament'"):
                warnings.extend(json.loads(row[0]).get("limitations", []))
        for res in resolutions:
            for candidate in res["matches"]:
                meta = json.loads(c.execute("select meta from sources where id=?", (candidate["source_id"],)).fetchone()[0])
                if meta.get("coverage") == "parcial_declarado":
                    warnings.append("El set de " + candidate["card_name"] + " es un listado parcial declarado.")
        relevant_exclusions = [e for e in selection["excluded"] if any(norm(n) in norm(e["path"]) for n in names)]
        if relevant_exclusions:
            warnings.append("Caso relacionado excluido por procedencia Discord; usar carta y PDF primario, sin presentar la interpretación como ruling oficial.")
        grouped = {"primary_rules": primary, "cards": card_packets, "official_policy": policy,
                   "official_notes": official_notes, "special_format": special, "spanish": spanish, "case": case, "support": support}
        grouped = {k: [decorate(c, root, p) for p in vals] for k, vals in grouped.items()}
        for p in grouped["spanish"]:
            warnings.extend(w for w in p["source_limitations"] if w.startswith("Discrepancia comprobada"))
        warnings.extend(p["errata_warning"] for p in grouped["cards"] if p.get("errata_warning"))
        # Los candidatos no se omiten/truncan antes de ofrecer versiones; tampoco se usan para razonar.
        for res in resolutions:
            for key in ("matches", "candidates"):
                res[key] = [decorate(c, root, p) for p in res[key]]
        all_packets = [p for vals in grouped.values() for p in vals] + [p for r in resolutions for p in r["candidates"]]
        verify_fragments(c, root, all_packets)
        for res in resolutions:
            # El texto completo de coincidencias está en cards; los candidatos nunca se usan como cartas confirmadas.
            for key in ("matches", "candidates"):
                res[key] = [{k: p.get(k) for k in ("id", "card_name", "path", "lines", "local_link", "coverage", "source_hash", "card_status")} for p in res[key]]
        # Segunda comprobación completa cubre adiciones y cambios concurrentes, sin escribir.
        entries_after, selection_after = inventory(root)
        if entries_after != entries or selection_after != selection:
            raise ValueError("Fuentes cambiaron durante la recuperación. Repetir la consulta.")
        ok = bool(primary or policy or special) and not missing_rule_numbers and all(r["status"] == "exacta" for r in resolutions)
        return {"mode": mode, "editorial_required": mode == "documenta", "question": question,
                "status": ("evidencia_recuperada_con_limitaciones" if warnings else "evidencia_recuperada") if ok else "evidencia_insuficiente_o_ambigua",
                "evidence_only": True, "content_is_untrusted_data": True,
                "freshness": state, "selection": {"primary": selection["primary"], "version": selection["version"]},
                "scope": scope, "card_resolution": resolutions, "missing_rule_numbers": missing_rule_numbers, "excluded_related": relevant_exclusions,
                "warnings": list(dict.fromkeys(warnings)), **grouped,
                "elapsed_ms": round((time.perf_counter() - start) * 1000, 3)}
    finally:
        c.close()


def readable(result):
    if "question" not in result:
        return json.dumps(result, ensure_ascii=False, indent=2)
    lines = [f"{result['status']} · {result['elapsed_ms']} ms · CR {result['selection']['version']}",
             f"Modo: {result['mode']} · ámbito: {result['scope']}", *result["warnings"]]
    for res in result["card_resolution"]:
        lines.append(f"Carta {res['requested']}: {res['status']}")
        lines.extend("  Candidato: " + p["card_name"] + " · " + p["local_link"] for p in res["candidates"])
    for group in ("primary_rules", "cards", "official_policy", "official_notes", "special_format", "spanish", "case", "support"):
        if result[group]:
            lines.append("\n" + group)
        for p in result[group]:
            lines.extend([p["local_link"] + f" · {p['authority']} · páginas {p['pages']} · líneas {p['lines']}", p["text"]])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--db", type=Path, default=HERE / ".cache" / "indice.sqlite")
    subs = parser.add_subparsers(dest="command", required=True)
    for name in ("indexar", "actualizar", "estado"):
        sub = subs.add_parser(name)
        sub.add_argument("--json", action="store_true")
        if name != "estado":
            sub.add_argument("--sin-fts", action="store_true", help="Alternativa SQLite con búsqueda local por tokens")
    sub = subs.add_parser("consultar")
    sub.add_argument("question")
    sub.add_argument("--carta", action="append", default=[])
    sub.add_argument("--regla", action="append", default=[])
    sub.add_argument("--ambito", choices=["estandar", "coconut", "multijugador", "pack_rush", "torneo", "correcciones", "consejos", "experiencias", "carde", "recursos", "comunidad"])
    sub.add_argument("--limite", type=int, default=5)
    sub.add_argument("--json", action="store_true")
    for name in ("regla", "carta"):
        sub = subs.add_parser(name)
        sub.add_argument("name")
        sub.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command in ("indexar", "actualizar"):
            result = update(args.root.resolve(), args.db.resolve(), args.sin_fts)
        elif args.command == "estado":
            result = freshness(args.root.resolve(), args.db.resolve())
        else:
            kwargs = {}
            if args.command == "consultar":
                question = args.question
                kwargs = dict(card_names=args.carta, rule_numbers=args.regla, scope=args.ambito, limit=max(1, min(args.limite, 12)))
            else:
                question = args.name
                kwargs["card_names" if args.command == "carta" else "rule_numbers"] = [args.name]
            result = query(args.root.resolve(), args.db.resolve(), question, **kwargs)
        print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else readable(result))
        return 0
    except Exception as exc:
        print(json.dumps({"status": "error", "error": str(exc), "no_ruling": True}, ensure_ascii=False), file=sys.stderr)
        return 2
