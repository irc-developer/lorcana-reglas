---
name: lorcana-scope
description: "Usar cuando trabajes con rulings de Lorcana, edición de reglas, documentación normativa, glosario oficial o verificación de texto de cartas. Define alcance permitido, jerarquía de fuentes y criterios de parada."
applyTo:
  - "01. Reglas/**"
  - "01.1.a Official English Reference – Unmodified/**"
  - "02. Listado de Cartas/**"
  - "Documentacion Oficial/**"
---

# Alcance y jerarquía de fuentes de Lorcana

- Para reglas base, usar el original oficial inglés seleccionado por `Documentacion Oficial/README.md` y `01.1.a Official English Reference – Unmodified/00. Fuente actual.md`. Leer su texto mediante `lorcana-rules-engine` o en la extracción paginada registrada. Abrir el original si importa su presentación visual o si hay dudas sobre la fidelidad de la extracción.
- El original es la autoridad normativa primaria según la copia local identificada. Esta selección no autoriza carpetas legacy ni convierte todo el contenido de `Documentacion Oficial` en reglas base.
- `01. Reglas` se usa para localizar, citar y documentar en castellano.
- Para texto exacto y nombres de cartas, usar la sección `02. Listado de Cartas` y el archivo del set correspondiente, conservados como corpus local. Para los enlaces de lectura de cartas, usar imágenes verificadas de Lorcast según `lorcana-obsidian-links.instructions.md`; ese destino comunitario no sustituye la verificación ni la autoridad normativa.
- No usar `02. Habilidades de las cartas_OLD`, `20. Reglas CR 1.X`, `Unifica` ni material derivado o legacy para resolver, documentar o verificar.
- Una búsqueda vacía o evidencia insuficiente del motor no demuestra que la regla no exista ni constituye un bloqueo para investigar. Reformula con sinónimos y términos oficiales ingleses; prueba las capacidades alternativas del motor; revisa artículos existentes solo como pistas; y, cuando sea pertinente y accesible, inspecciona directamente el documento canónico local y su versión. Registra e identifica citas desde el pasaje original. Diagnostica por separado fallos de recuperación, indexación, ingestión e integración. Consulta fuentes oficiales externas solo si la política de acceso lo autoriza.
- La inspección directa de los documentos canónicos locales es un fallback obligatorio siempre que sean pertinentes y accesibles, incluso si el motor falla. Detén la escalada al obtener evidencia oficial suficiente. Si tras agotar los medios autorizados falta una fuente necesaria, describe el vacío concreto; no inventes el ruling ni pidas datos que la evidencia disponible ya resuelve.
- Ante discrepancia entre inglés y castellano, resolver según la referencia oficial inglesa y citar en castellano cuando exista localización equivalente.
- Los casos del bloque 11 y los resúmenes son apoyo interpretativo o docente; nunca prevalecen sobre las reglas base.
- Usar léxico fijo de zonas: `discard = descarte`, `hand = mano`, `play = zona de juego`, `inkwell = pozo de tinta`.

Consulta la referencia extensa en [Premisas agente IA Lorcana](../../Premisas%20agente%20IA%20Lorcana.md) y el diseño de flujo en [Arquitectura de Skills - Agente Lorcana](../../Arquitectura%20de%20Skills%20-%20Agente%20Lorcana.md).
