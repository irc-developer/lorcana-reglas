---
name: lorcana-consulta-rapida
description: "Recupera evidencia local para dudas puntuales de Disney Lorcana mediante Lorcana Rules Engine y remite la documentación al workflow editorial de la wiki."
---

# Consulta rápida de Lorcana

En cada tarea nueva, lee explícitamente `.github/copilot-instructions.md`, `.github/README.md`, `.github/instructions/lorcana-scope.instructions.md` y `.github/lorcana-rules-engine.md`. Si intervienen cartas, lee también `lorcana-card-verification.instructions.md`; carga las guías de timing, robos, aclaración o correcciones solo cuando correspondan.

## Elegir el modo antes de recuperar evidencia

- `consulta: [pregunta]` o invocación expresa de esta skill: **solo lectura**. No edites la bóveda ni generes índices, cachés o borradores. No documentes el ruling.
- `documenta: [pregunta]`: lee `.github/skills/lorcana-ruling-workflow/SKILL.md`, recupera y valida evidencia con el motor y aplica el workflow editorial completo de la wiki.
- `actualiza:`: usa la skill `manage-lorcana-sources` del motor. Autoriza el mantenimiento de fuentes o índices y no la edición de artículos.
- Una pregunta ordinaria sin señal sigue el workflow editorial completo de la wiki, salvo que Iván pida explícitamente solo lectura.

El motor no recibe estos modos. No conviertas la llamada CLI en una escritura ni interpretes una consulta fallida como permiso para usar otro motor.

## Recuperación

Lee `.github/lorcana-rules-engine.md` para localizar y ejecutar el motor. Usa su skill `query-lorcana` para buscar reglas y torneo, comprobar cartas/erratas y validar citas. La CLI no devuelve un paquete único de evidencia: compón consultas breves a `rules`, `cards`, `wiki` y `cases`, lee los registros completos pertinentes y conserva los metadatos de procedencia y localizador.

Si una búsqueda no devuelve resultados, no infieras que la regla no existe ni abandones la investigación. Reformula con conceptos alternativos, sinónimos y terminología oficial inglesa; usa modos y familias/tipos de fuente alternativos del motor; recupera registros relacionados o conocidos; y comprueba versiones, cobertura e integridad. Revisa artículos existentes y sus referencias únicamente para descubrir fuentes. Inspecciona obligatoriamente el documento canónico oficial local pertinente cuando esté accesible, aunque el motor siga fallando. Registra versión, identificador de regla, página y cita desde el original/transcripción. Diagnostica retrieval, indexación, ingestión o integración en una línea de trabajo separada del ruling y de la edición. Fuentes oficiales externas solo cuando lo autorice la política de acceso. Detén la escalada al obtener respaldo oficial suficiente.

`citations validate SOURCE:VERSION:RECORD` confirma identidad, versión, contenido y localizador frente a las fuentes locales. Revisa el pasaje completo para determinar si apoya la conclusión. `sources check-versions` audita el conjunto local y puede detectar cambios; una discrepancia impide afirmar frescura global. No actualices ni reconstruyas índices durante una `consulta:`. En cualquier modo, una avería del motor no impide completar el ruling o artículo si el documento canónico local aporta evidencia suficiente.

Las fuentes oficiales tienen la autoridad descrita por el repositorio. La vigencia de la copia local no implica verificación externa en vivo. Si el motor falla, sigue el protocolo de recuperación anterior y separa el defecto técnico de la pregunta normativa. Solo informa un bloqueo normativo tras inspeccionar las fuentes locales pertinentes accesibles y agotar las alternativas autorizadas; nunca inventes el resultado.

## Cartas, reglas y salida

Para cartas concretas, confirma la impresión completa en los archivos de set de `02. Listado de Cartas/` según `lorcana-card-verification.instructions.md`. El catálogo del motor sirve para buscar y contrastar texto oficial y erratas; no reemplaza los requisitos editoriales de la wiki ni la URL verificada de Lorcast.

Responde en castellano, con la conclusión, la secuencia relevante y referencias con versión y localizador. Enlaza la regla castellana de `01. Reglas/` cuando exista; conserva página y edición. Distingue reglas de torneo de la CR y señala cualquier dato o fuente que falte.

En Codex Remote selecciona el PC donde están disponibles el repositorio y el proyecto hermano `lorcana-rules-engine`. La vía remota utiliza esos archivos mediante la CLI local; no requiere el MCP. La ejecución en un proceso local no acredita por sí sola una sesión remota real.
