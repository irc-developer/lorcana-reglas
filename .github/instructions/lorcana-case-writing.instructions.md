---
name: lorcana-case-writing
description: "Guía de estructura y calidad para archivos de 01. Reglas/11. Casos de ejemplo y aclaraciones. No activa por sí sola la creación inicial del artículo."
applyTo:
  - "01. Reglas/11. Casos de ejemplo y aclaraciones/**"
---

# Formato de casos y aclaraciones de Lorcana

- La obligación de crear o actualizar un artículo nace del contrato global y de `.github/skills/lorcana-ruling-workflow/SKILL.md`; esta instrucción solo controla la calidad de archivos ya seleccionados por ese flujo.
- Elige la subcarpeta 11.* existente que mejor encaje con la duda. Si ninguna encaja, crea una categoría justificada y sincroniza el índice en la misma transacción; no difieras la documentación solo por la ubicación.
- Usa un nombre descriptivo, específico y distinto de los artículos canónicos existentes.
- Sigue `01. Reglas/11. Casos de ejemplo y aclaraciones/Plantilla - Caso de ejemplo y aclaración.md`: duda, respuesta, fundamento en reglas, secuencia oficial y tags. Añade fuente y estado cuando el origen oficial o el grado de certeza lo requieran.
- La convención vigente de los casos no usa frontmatter YAML. Valida esa ausencia contra la plantilla; no inventes frontmatter, estados ni fechas. Si la plantilla cambia, aplica su frontmatter exacto.
- Integra en la duda final cualquier dato crítico confirmado al usuario; no dejes bloques separados de aclaración previa en el documento final.
- Vincula las cartas y reglas a destinos existentes, cita las fuentes oficiales utilizadas y conserva UTF-8, ortografía española y Markdown limpio.

Complementa esta instrucción con [lorcana-case-dedup.instructions.md](lorcana-case-dedup.instructions.md), [lorcana-case-tags.instructions.md](lorcana-case-tags.instructions.md) y [lorcana-file-hygiene.instructions.md](lorcana-file-hygiene.instructions.md).
