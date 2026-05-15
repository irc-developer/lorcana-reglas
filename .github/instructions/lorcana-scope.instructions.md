---
name: lorcana-scope
description: "Usar cuando trabajes con rulings de Lorcana, edición de reglas, documentación normativa, glosario oficial o verificación de texto de cartas. Define alcance permitido, jerarquía de fuentes y criterios de parada."
applyTo:
  - "01. Reglas/**"
  - "01.1.a Official English Reference – Unmodified/**"
  - "02. Listado de Cartas/**"
---

# Alcance y jerarquía de fuentes de Lorcana

- Para reglas, usar solo `01. Reglas` y `01.1.a Official English Reference – Unmodified`.
- La autoridad normativa primaria es `01.1.a Official English Reference – Unmodified`.
- `01. Reglas` se usa para localizar, citar y documentar en castellano.
- Para texto exacto de cartas, nombres y enlaces de cartas, usar solo `02. Listado de Cartas/Cartas de Lorcana.md`.
- No usar `02. Habilidades de las cartas_OLD`, `20. Reglas CR 1.X`, `Unifica` ni material derivado o legacy para resolver, documentar o verificar.
- Si una regla o una carta no puede sostenerse con esas fuentes, detenerse y pedir al usuario el dato exacto o una ampliación explícita del alcance.
- Ante discrepancia entre inglés y castellano, resolver según la referencia oficial inglesa y citar en castellano cuando exista localización equivalente.
- Los casos del bloque 11 y los resúmenes son apoyo interpretativo o docente; nunca prevalecen sobre las reglas base.
- Usar léxico fijo de zonas: `discard = descarte`, `hand = mano`, `play = zona de juego`, `inkwell = pozo de tinta`.

Consulta la referencia extensa en [Premisas agente IA Lorcana](../../Premisas%20agente%20IA%20Lorcana.md) y el diseño de flujo en [Arquitectura de Skills - Agente Lorcana](../../Arquitectura%20de%20Skills%20-%20Agente%20Lorcana.md).