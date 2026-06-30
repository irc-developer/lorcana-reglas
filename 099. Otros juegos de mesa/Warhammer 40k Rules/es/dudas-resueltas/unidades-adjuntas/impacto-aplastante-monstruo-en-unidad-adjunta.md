---
type: rules-question
category: attached-units
canonical: false
source: core-rules
surface: resolved-question
owner-domain: attached-units
status: verified
rules:
  - 06.02
  - 15.06
  - 19.01
  - 19.03
tags:
  - warhammer40k
  - resolved-question
  - attached-units
  - stratagems
  - mortal-wounds
  - rules-application
aliases:
  - mi monstruo usa impacto aplastante en unidad adjunta
  - impacto aplastante con monstruo en unidad adjunta
  - tank shock con monstruo en unidad adjunta
  - crushing impact con monstruo en unidad adjunta
  - puedo pasar las mortales de impacto aplastante a los guardaespaldas
  - mortales de impacto aplastante a guardaespaldas
  - monstruo personaje con guardaespaldas impacto aplastante
related:
  - Impacto aplastante
  - Heridas mortales
  - Unidad adjunta
  - Formar unidades adjuntas
  - Claves en unidades adjuntas
  - Sistema de carga
---

# Si mi monstruo está en mi unidad adjunta y usa Impacto aplastante, ¿puedo pasar sus mortales a los guardaespaldas?

## Respuesta corta

Sí. Si tu propia unidad adjunta usa [[Impacto aplastante]] gracias a que contiene una miniatura `MONSTRUO` o `VEHÍCULO`, y esa unidad sufre heridas mortales por los resultados de 1, esas heridas mortales se asignan siguiendo la regla normal de [[Heridas mortales]].

Si tu unidad contiene miniaturas que no sean `PERSONAJE`, como guardaespaldas normales, esas miniaturas van antes que las miniaturas `PERSONAJE`. Por tanto, tu monstruosa `PERSONAJE` que forma parte de tu unidad adjunta no tiene por qué sufrir esas mortales mientras queden guardaespaldas no `PERSONAJE` a los que asignarlas legalmente.

## Por qué funciona

Una [[Unidad adjunta]] tiene las claves de sus unidades componentes. Si una de tus unidades componentes aporta `MONSTRUO` o `VEHÍCULO`, tu unidad adjunta puede cumplir el requisito de blanco de [[Impacto aplastante]] como unidad `MONSTRUO` o `VEHÍCULO`.

Después, [[Impacto aplastante]] te pide elegir una miniatura de tu unidad que esté trabada con la unidad enemiga elegida. En esta duda, esa miniatura es tu monstruo dentro de tu unidad adjunta. Esa miniatura sirve para determinar cuántos D6 tiras, usando su atributo de Resistencia.

La parte importante es el resultado de la tirada: por cada 1, **tu unidad** sufre 1 herida mortal. La estratagema no dice que la herida mortal la sufra la miniatura elegida.

## Cómo se asignan esas heridas mortales

Cuando una unidad sufre heridas mortales, se resuelven una a una. Para cada herida mortal, el jugador controlador elige la miniatura aplicando la prioridad normal:

1. Una miniatura que no sea `PERSONAJE` y que ya haya perdido heridas.
2. Si no hay una, otra miniatura que no sea `PERSONAJE`.
3. Si no hay miniaturas que no sean `PERSONAJE`, una miniatura `PERSONAJE` que ya haya perdido heridas.
4. Si no hay una, otra miniatura `PERSONAJE`.

Así que, si la unidad adjunta tiene guardaespaldas no `PERSONAJE`, las mortales de [[Impacto aplastante]] se asignan a esos guardaespaldas antes que a una monstruosa `PERSONAJE`.

## Ejemplo

Tu unidad adjunta contiene una monstruosa `PERSONAJE` con clave `MONSTRUO` y varias miniaturas guardaespaldas que no son `PERSONAJE`. Tu unidad termina un movimiento de carga y usa [[Impacto aplastante]].

La unidad adjunta puede ser el blanco de la estratagema porque tiene la clave `MONSTRUO`. El jugador elige la miniatura monstruosa trabada y tira tantos D6 como su Resistencia.

Si obtiene dos resultados de 1, la unidad propia sufre 2 heridas mortales. Como la unidad contiene guardaespaldas no `PERSONAJE`, esas heridas mortales se asignan a guardaespaldas siguiendo la prioridad normal de [[Heridas mortales]], no automáticamente a la monstruosa elegida para la tirada.

## Límites y matices

- Si ya hay una miniatura no `PERSONAJE` herida en la unidad, las mortales deben seguir asignándose a esa miniatura antes de elegir otra no `PERSONAJE`.
- Si no queda ninguna miniatura no `PERSONAJE`, entonces las heridas mortales pasan a miniaturas `PERSONAJE` según la prioridad normal.
- Las miniaturas de una unidad adjunta no ganan claves de otras miniaturas. La unidad puede tener la clave `MONSTRUO`, pero eso no convierte a los guardaespaldas en miniaturas `MONSTRUO`.
- Esta respuesta no depende de una habilidad propia de la unidad. Es la combinación normal de [[Claves en unidades adjuntas]], [[Impacto aplastante]] y [[Heridas mortales]].

## Errores comunes

- Pensar que la miniatura elegida para calcular los D6 debe sufrir las mortales de los resultados de 1.
- Pensar que los guardaespaldas no pueden recibir esas mortales porque no tienen la clave `MONSTRUO`.
- Confundir "la unidad tiene la clave" con "todas las miniaturas tienen la clave".
- Asignar libremente las mortales sin respetar la prioridad de miniaturas no `PERSONAJE` heridas primero.

## Fundamento de reglas

- [[Claves en unidades adjuntas]]: la unidad adjunta tiene todas las claves de sus unidades componentes, aunque las miniaturas no ganen claves que no tuvieran.
- [[Impacto aplastante]]: el blanco es la unidad `MONSTRUO` o `VEHÍCULO`; se elige una miniatura para determinar la tirada, pero los resultados de 1 hacen que tu unidad sufra heridas mortales.
- [[Heridas mortales]]: cuando una unidad sufre heridas mortales, se asignan por prioridad a miniaturas no `PERSONAJE` antes que a miniaturas `PERSONAJE`.
- Fuente oficial: `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, referencias `06.02`, `15.06`, `19.01` y `19.03`.

## Resumen para arbitraje casual

Sí: si usas [[Impacto aplastante]] con una monstruosa que forma parte de una unidad adjunta, las mortales que te haces con los 1 las sufre la unidad, no necesariamente la miniatura monstruosa. Si quedan guardaespaldas no `PERSONAJE`, se asignan a ellos antes que a la monstruosa `PERSONAJE`, siguiendo la regla normal de [[Heridas mortales]].
