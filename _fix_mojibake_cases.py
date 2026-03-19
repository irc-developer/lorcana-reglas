from pathlib import Path

root = Path(r"c:\Users\plata\OneDrive\Documentos\Proyectos\lorcana-reglas\01. Reglas\11. Casos de ejemplo y aclaraciones")

exclude = {
    "Plantilla - Caso de ejemplo y aclaración.md",
    "Glosario.md",
}

markers = ["Ã", "â", "ðŸ", "Â", "â€”", "â€œ", "â€", "â€™"]

fixed = 0
scanned = 0

for p in root.glob("*.md"):
    if p.name in exclude or p.name.startswith("_backup_migracion"):
        continue
    scanned += 1
    text = p.read_text(encoding="utf-8", errors="replace")
    if not any(m in text for m in markers):
        continue

    candidate = text
    try:
        candidate = text.encode("latin-1", errors="ignore").decode("utf-8", errors="ignore")
    except Exception:
        continue

    old_score = sum(text.count(m) for m in markers)
    new_score = sum(candidate.count(m) for m in markers)

    if new_score < old_score and candidate.strip():
        p.write_text(candidate, encoding="utf-8")
        fixed += 1

print(f"SCANNED={scanned}")
print(f"FIXED={fixed}")
