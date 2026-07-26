---
name: lorcana-ruling-workflow
description: "Flujo transaccional obligatorio para resolver una duda de reglas de Disney Lorcana, documentarla en el artículo canónico, sincronizar índices y portada, validar el conjunto y solo entonces responder."
argument-hint: "Describe la duda o interacción de Lorcana que debe resolverse y documentarse."
user-invocable: true
---

# Workflow unificado de rulings de Lorcana

## Contrato

Un ruling, su artículo, los índices afectados y la fecha visible de `Empecemos.md` forman una sola transacción editorial. La tarea no está terminada si solo existe una respuesta de chat.

Solo se permite omitir las ediciones cuando el usuario pide explícitamente no modificar el repositorio o cuando una comprobación demuestra que editar es técnicamente imposible. La incertidumbre normativa, la falta de activación automática de otra instrucción o una ubicación incómoda no son bloqueos.

## Fuentes y guías de apoyo

- Reglas primarias: `01.1.a Official English Reference – Unmodified/`.
- Localización y documentación en castellano: `01. Reglas/`.
- Texto exacto de cartas: archivo de set correspondiente dentro de `02. Listado de Cartas/`.
- Artículos: `01. Reglas/11. Casos de ejemplo y aclaraciones/`.
- Índice manual principal: `01. Reglas/11. Casos de ejemplo y aclaraciones/ÍNDICE - Casos de ejemplo y aclaraciones.md`.
- Plantilla vigente: `01. Reglas/11. Casos de ejemplo y aclaraciones/Plantilla - Caso de ejemplo y aclaración.md`.

Aplica directamente, cuando corresponda, las guías reutilizables de [alcance](../../instructions/lorcana-scope.instructions.md), [aclaración](../../instructions/lorcana-question-clarification.instructions.md), [verificación de cartas](../../instructions/lorcana-card-verification.instructions.md), [deduplicación](../../instructions/lorcana-case-dedup.instructions.md), [formato de casos](../../instructions/lorcana-case-writing.instructions.md), [tags](../../instructions/lorcana-case-tags.instructions.md), [enlaces Obsidian](../../instructions/lorcana-obsidian-links.instructions.md) e [higiene Markdown](../../instructions/lorcana-file-hygiene.instructions.md). Estas guías afinan pasos concretos; ninguna sustituye este flujo.

## Flujo obligatorio y ordenado

1. **Determinar la pregunta exacta.** Reconstruye cartas, versiones, estado de mesa, elecciones y secuencia. Si un dato crítico admite resultados distintos, pide solo la aclaración mínima antes de continuar.
2. **Identificar y priorizar fuentes oficiales.** Busca primero la referencia inglesa oficial sin modificar y después la localización castellana equivalente. Los casos existentes sirven para localizar o comparar, nunca para prevalecer sobre la regla primaria.
3. **Verificar el texto de cartas cuando sea relevante.** Confirma nombre, versión y texto completo en el archivo de set de `02. Listado de Cartas/`. No uses carpetas legacy ni inventes texto ausente.
4. **Producir el ruling técnico.** Determina veredicto, fundamento, orden de eventos, disparos, bolsa y GSC aplicables. Conserva las referencias exactas que sostienen cada conclusión.
5. **Buscar artículos duplicados o solapados.** Busca en toda la sección 11 por nombres de cartas, mecánicas, conceptos, tags y conclusión normativa; revisa la subcarpeta probable y el índice manual.
6. **Decidir crear o actualizar.** Actualiza el artículo canónico si ya cubre la misma interacción o concepto. Crea uno nuevo solo cuando la diferencia conceptual sea material. Si varios se solapan, elige el mejor canónico, integra allí lo útil y evita otro duplicado.
7. **Escribir el artículo completo.** Ubícalo en la subcarpeta 11.* adecuada y sigue la plantilla vigente. La duda documentada debe contener los hechos ya confirmados y la respuesta debe coincidir con el ruling técnico.
8. **Aplicar estructura y calidad editorial.** Revisa nombre de archivo, título si lo usa, frontmatter y metadatos según la convención vigente, estado o fechas si existen, headings, ejemplos, tags, enlaces de cartas y reglas, fuentes oficiales, ortografía, gramática, UTF-8 y formato. Actualmente la plantilla de casos no usa frontmatter: valida su ausencia y no inventes campos.
9. **Actualizar todos los índices afectados.** Para cada índice manual, añade, corrige o elimina el enlace exacto; conserva el orden; renumera; actualiza contadores de subsección, total, estadísticas, búsquedas temáticas y fecha del índice cuando existan. Compara las entradas con los archivos reales.
10. **Actualizar `Empecemos.md`.** Si el artículo se creó o cambió materialmente, sustituye la fecha visible por la fecha real del entorno usando el formato existente `*Última actualización dd/mm/aa*`. Si ya coincide, no hagas un cambio artificial. No cambies la fecha en tareas sin modificación material de un artículo de ruling.
11. **Validar la transacción completa.** Inspecciona el diff y comprueba: artículo frente al ruling; plantilla/frontmatter; tags y registro maestro; destinos de enlaces; fuentes citadas; presencia única en índices; contadores; fecha del índice; fecha de `Empecemos.md`; Markdown/YAML; y ausencia de cambios ajenos. Ejecuta los validadores existentes si los hay.
12. **Preparar la respuesta final.** Solo después de editar y validar, responde con el ruling breve, su secuencia o fundamento necesario y la ruta de cada artículo creado, actualizado o verificado como canónico.

## Excepciones

### Petición explícita de no editar

Resuelve con las mejores fuentes disponibles, no modifiques archivos e indica brevemente que se omitió la documentación porque el usuario lo pidió expresamente.

### Bloqueo técnico verificado

Intenta y registra una comprobación concreta del impedimento. Aun así ofrece el mejor ruling sustentado posible e identifica exactamente el bloqueo y qué artículo, índice o fecha no pudo actualizarse. No afirmes que la transacción se completó.

## Criterio de cierre

No cierres mientras artículo, índices y fecha estén desincronizados. Si el artículo existente ya era completo y correcto y no requiere cambio material, no lo edites artificialmente: devuelve su ruta y deja constancia interna de que se verificaron duplicado, índice y fecha.
