# Guía del workspace

## Contrato obligatorio para rulings

- Una tarea que resuelve una duda de reglas de Lorcana no termina con una respuesta de chat: debe completar el flujo de `.github/skills/lorcana-ruling-workflow/SKILL.md`.
- Antes de la respuesta final, verifica las fuentes oficiales, resuelve el ruling, crea o actualiza el artículo canónico, revisa su calidad, sincroniza los índices afectados y, si el artículo cambió materialmente, la fecha visible de `Empecemos.md`, y valida el conjunto.
- Cada duda documentada con cambios debe terminar con un commit de su transacción editorial y un `push` al repositorio remoto. El usuario ha autorizado este paso como parte del workflow; no requiere pedir confirmación de nuevo, salvo que cambie esa instrucción. Sigue los límites y excepciones de la skill del workflow.
- Después del `push`, publica en Obsidian Publish solo los archivos de esa duda incluidos en el commit: artículos e índices, portada o registro de tags que hayan cambiado en esa transacción. El usuario ha autorizado esta publicación selectiva; nunca publiques el conjunto de pendientes de la bóveda. Usa la herramienta `herramientas/publicar_obsidian/publicar.py` y el workflow para comprobar la selección antes de subirla.
- La respuesta final debe incluir el ruling y la ruta del artículo creado, modificado o verificado como canónico.
- Si se publicaron cambios, incluye también el enlace o hash del commit y el enlace del artículo en Obsidian; si el commit, el `push` o Publish falló, indica el bloqueo verificado y lo que queda pendiente.
- Solo se omite la documentación si el usuario pide explícitamente no modificar el repositorio o si se ha comprobado un bloqueo técnico real; en ese caso, indica la excepción y el trabajo que quedó pendiente.
- La incertidumbre, la falta de selección automática de otra skill o una ruta incómoda no son bloqueos técnicos.

## Fuente de verdad de cartas

- Para nombres, texto exacto y enlaces de cartas, usa solo la sección `02. Listado de Cartas` y el archivo del set correspondiente.
- `02. Listado de Cartas/Cartas de Lorcana.md` actúa como índice de entrada; no asumas que el texto exacto vive solo ahí si ya está repartido por sets.
- No uses `02. Habilidades de las cartas_OLD`, `20. Reglas CR 1.X`, `Unifica` ni material derivado o legacy como autoridad para texto de cartas.
- Si una carta o su set no pueden verificarse dentro de `02. Listado de Cartas`, detente y pide precisión antes de cerrar la respuesta.

## Alcance normativo de reglas

- Para reglas base, la autoridad primaria es el PDF inglés seleccionado por `Documentacion Oficial/README.md` y `01.1.a Official English Reference – Unmodified/00. Fuente actual.md`. Los Markdown numerados de la referencia inglesa son transcripciones históricas incompletas; no sustituyen ese PDF para citas vigentes.
- Usa las instrucciones y skills de `.github/instructions/` y `.github/skills/` cuando el trabajo entre en esos flujos.
