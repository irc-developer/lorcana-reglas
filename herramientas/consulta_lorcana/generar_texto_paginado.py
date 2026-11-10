"""Extrae PDF oficiales a Markdown paginado y muestra sus hashes de registro."""
import argparse
import json
from pathlib import Path

from core import ROOT, digest, extract_pdf, read_paged_pdf_text


def generate(pdf):
    original_hash = digest(pdf.read_bytes())
    pages, extraction = extract_pdf(pdf)
    if digest(pdf.read_bytes()) != original_hash:
        raise ValueError("El PDF cambió durante la extracción: " + str(pdf))
    meta = {"pdf_sha256": original_hash, "extraction": extraction}
    output = [
        f"# {pdf.stem} · Texto paginado",
        "",
        f"Extracción de `{pdf.name}`. Los encabezados indican las páginas del original.",
        f"<!-- {json.dumps(meta, ensure_ascii=False)} -->",
    ]
    for page in pages:
        lines = zip(page["text"].splitlines(), page["raw"].splitlines(), strict=True)
        overrides = [(i, raw) for i, (text, raw) in enumerate(lines) if text != raw]
        output.extend(["", f"## Página {page['page']}", f"<!-- {json.dumps(overrides, ensure_ascii=False)} -->",
                       "```text", page["text"], "```"])
    data = ("\n".join(output) + "\n").encode("utf-8")
    target = pdf.with_suffix(".paginas.md")
    return target, data, original_hash, pages, extraction


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdfs", nargs="+", type=Path)
    args = parser.parse_args()
    registered = {}
    for pdf in args.pdfs:
        pdf = pdf.resolve()
        if pdf.parent != (ROOT / "Documentacion Oficial").resolve() or pdf.suffix != ".pdf":
            parser.error("Indica un PDF de Documentacion Oficial: " + str(pdf))
        target, data, original_hash, pages, extraction = generate(pdf)
        reading_hash = digest(data)
        target.write_bytes(data)
        if read_paged_pdf_text(target, {"hash": original_hash, "reading_hash": reading_hash}) != (pages, extraction):
            raise ValueError("La transcripción no reproduce la extracción: " + str(target))
        registered[original_hash] = {"file": target.name, "sha256": reading_hash}
    print(json.dumps(registered, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
