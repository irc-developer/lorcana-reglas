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
- Sigue `01. Reglas/11. Casos de ejemplo y aclaraciones/Plantilla - Caso de ejemplo y aclaración.md`: duda, respuesta, referencias y tags. Añade un ejemplo o «Cómo se resuelve» solo si ayuda a entender el resultado; no rellenes una secuencia fija de costes, elecciones, bolsa y GSC.
- La convención vigente de los casos no usa frontmatter YAML. Valida esa ausencia contra la plantilla; no inventes frontmatter, estados ni fechas. Si la plantilla cambia, aplica su frontmatter exacto.
- Integra en la duda final cualquier dato crítico confirmado al usuario; no dejes bloques separados de aclaración previa en el documento final.
- Vincula las cartas y reglas a destinos existentes, cita las fuentes oficiales utilizadas y conserva UTF-8, ortografía española y Markdown limpio.

## Escribir para quien está aprendiendo

- Abre con el resultado y explica el motivo en lenguaje claro. Cada párrafo debe aportar una condición necesaria, una consecuencia distinta, una explicación o una referencia consultable.
- Verifica cartas y reglas completas durante el trabajo; en el artículo cita solo el texto relevante y enlaza la imagen exacta de Lorcast y la fuente oficial. Las fichas de set se conservan localmente para evidencia; no son destinos públicos. Conserva los epígrafes o páginas necesarios sin repetirlos en varios bloques.
- El artículo no es un registro de investigación: excluye fechas de búsqueda, comprobaciones de enlaces, hashes, estado del índice o del MCP, errores de recuperación, autorizaciones y la historia de las capturas que originaron la pregunta. Las incidencias de trabajo se comunican en la conversación o en un registro interno cuando corresponda.
- Evita repetir la misma conclusión en respuesta, tabla, secuencia y errores frecuentes. Conserva ejemplos o variantes que cambien el resultado o resuelvan una confusión distinta. Los costes, disparos y GSC se explican cuando son decisivos, no como cierre genérico.
- No añadas descargos repetidos de «inferencia editorial», «ejemplo didáctico» o «no es una FAQ oficial». Explica la aplicación de las reglas sin atribuirla a una aclaración oficial que no existe. Conserva una nota breve si hay incertidumbre material, conflicto de fuentes, traducción de trabajo o un ámbito limitado que el lector deba conocer.
- Mantén las advertencias que afectan al uso de la respuesta, especialmente las decisiones reservadas al Lore Guide. Abreviar nunca convierte un fallo provisional en confirmado.
- Integra las ampliaciones bajo la duda correspondiente y agrupa los tags al final. No impongas una longitud máxima: elimina repeticiones y contenido periférico, conservando las condiciones relevantes.

Complementa esta instrucción con [lorcana-case-dedup.instructions.md](lorcana-case-dedup.instructions.md), [lorcana-case-tags.instructions.md](lorcana-case-tags.instructions.md) y [lorcana-file-hygiene.instructions.md](lorcana-file-hygiene.instructions.md).
