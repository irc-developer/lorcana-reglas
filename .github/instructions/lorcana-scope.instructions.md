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

- Para reglas base, usar el PDF oficial inglés seleccionado por `Documentacion Oficial/README.md` y `01.1.a Official English Reference – Unmodified/00. Fuente actual.md`, con `01. Reglas` como localización castellana.
- Ese PDF es la autoridad normativa primaria según la copia local identificada. Los Markdown numerados de la referencia inglesa son transcripciones históricas incompletas, no texto consolidado vigente. Esta selección no autoriza carpetas legacy ni convierte todo el contenido de `Documentacion Oficial` en reglas base.
- `01. Reglas` se usa para localizar, citar y documentar en castellano.
- Para texto exacto y nombres de cartas, usar la sección `02. Listado de Cartas` y el archivo del set correspondiente, conservados como corpus local. Para los enlaces de lectura de cartas, usar imágenes verificadas de Lorcast según `lorcana-obsidian-links.instructions.md`; ese destino comunitario no sustituye la verificación ni la autoridad normativa.
- No usar `02. Habilidades de las cartas_OLD`, `20. Reglas CR 1.X`, `Unifica` ni material derivado o legacy para resolver, documentar o verificar.
- Si una regla o una carta no puede sostenerse con esas fuentes, detenerse y pedir al usuario el dato exacto o una ampliación explícita del alcance.
- Ante discrepancia entre inglés y castellano, resolver según la referencia oficial inglesa y citar en castellano cuando exista localización equivalente.
- Los casos del bloque 11 y los resúmenes son apoyo interpretativo o docente; nunca prevalecen sobre las reglas base.
- Usar léxico fijo de zonas: `discard = descarte`, `hand = mano`, `play = zona de juego`, `inkwell = pozo de tinta`.

Consulta la referencia extensa en [Premisas agente IA Lorcana](../../Premisas%20agente%20IA%20Lorcana.md) y el diseño de flujo en [Arquitectura de Skills - Agente Lorcana](../../Arquitectura%20de%20Skills%20-%20Agente%20Lorcana.md).
