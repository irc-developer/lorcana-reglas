# Guía del workspace

## Contrato obligatorio para rulings

- Una tarea que resuelve una duda de reglas de Lorcana no termina con una respuesta de chat: debe completar el flujo de `.github/skills/lorcana-ruling-workflow/SKILL.md`.
- Antes de la respuesta final, verifica las fuentes oficiales, resuelve el ruling, crea o actualiza el artículo canónico, revisa su calidad, sincroniza los índices afectados y, si el artículo cambió materialmente, la fecha visible de `Empecemos.md`, y valida el conjunto.
- La respuesta final debe incluir el ruling y la ruta del artículo creado, modificado o verificado como canónico.
- Solo se omite la documentación si el usuario pide explícitamente no modificar el repositorio o si se ha comprobado un bloqueo técnico real; en ese caso, indica la excepción y el trabajo que quedó pendiente.
- La incertidumbre, la falta de selección automática de otra skill o una ruta incómoda no son bloqueos técnicos.

## Fuente de verdad de cartas

- Para nombres, texto exacto y enlaces de cartas, usa solo la sección `02. Listado de Cartas` y el archivo del set correspondiente.
- `02. Listado de Cartas/Cartas de Lorcana.md` actúa como índice de entrada; no asumas que el texto exacto vive solo ahí si ya está repartido por sets.
- No uses `02. Habilidades de las cartas_OLD`, `20. Reglas CR 1.X`, `Unifica` ni material derivado o legacy como autoridad para texto de cartas.
- Si una carta o su set no pueden verificarse dentro de `02. Listado de Cartas`, detente y pide precisión antes de cerrar la respuesta.

## Alcance normativo de reglas

- Para reglas base, la autoridad primaria sigue siendo `01.1.a Official English Reference – Unmodified`.
- Usa las instrucciones y skills de `.github/instructions/` y `.github/skills/` cuando el trabajo entre en esos flujos.
