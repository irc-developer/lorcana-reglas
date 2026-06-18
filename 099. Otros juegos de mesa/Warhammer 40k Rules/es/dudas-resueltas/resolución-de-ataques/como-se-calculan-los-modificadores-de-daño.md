---
type: rules-question
category: attack-resolution
canonical: false
source: core-rules-and-missing-digital-reference
surface: resolved-question
owner-domain: attack-resolution
status: needs-official-clarification
rules:
  - 02.04
  - 05.04
  - 06.02
  - 24.10
  - 24.25
tags:
  - warhammer40k
  - resolved-question
  - attack-resolution
  - damage
  - modifiers
  - melta
  - devastating-wounds
  - rules-application
aliases:
  - cómo se calcula ahora el daño
  - orden de los modificadores de daño
  - reducir el daño a cero
  - reducir el daño a la mitad
  - daño cero y fusión
  - dividir y restar daño
related:
  - Daño (D)
  - Infligir daño
  - Fusión
  - Heridas devastadoras
  - Heridas mortales
---

# ¿Cómo se calcula el Daño con reducciones a 0, a la mitad y otros modificadores?

## Respuesta corta

Las Reglas básicas de 2026 remiten expresamente a una entrada llamada **Characteristic Modifiers** en la página 11, pero esa entrada no está desarrollada en las 88 páginas del PDF y, a fecha de 15 de junio de 2026, tampoco aparece en el manual de la app.

Por tanto, **el orden general de los modificadores de atributos no está actualmente disponible en una fuente oficial consultable**. El PDF parece contener una referencia a contenido digital omitido o todavía no publicado.

La fórmula usada en la edición anterior era:

`cambiar o sustituir → dividir → multiplicar → sumar → restar → redondear al alza`

Es el precedente más razonable para un arbitraje provisional, pero no debe presentarse como texto verificado de las reglas de 2026 hasta que Games Workshop publique la entrada ausente o una FAQ equivalente.

## Lo que sí está confirmado

- [[Daño (D)|Daño]] es el atributo `D` del arma.
- Cuando un ataque inflige daño, la miniatura elegida pierde una cantidad de heridas igual a `D`.
- [[Fusión|[FUSIÓN X]]] suma `X` al atributo `D` si se cumple su condición de alcance.
- El ejemplo oficial de Fusión convierte un atributo `D6` en `D6+2`.
- [[Heridas devastadoras|[HERIDAS DEVASTADORAS]]] usa el atributo `D` para determinar las heridas mortales causadas por una herida crítica.

## Heridas devastadoras

Si una regla modifica válidamente el atributo `D`, [[Heridas devastadoras]] usa el valor que tenga ese atributo al resolverse la habilidad.

Cada herida crítica solo puede dañar a una miniatura y se pierde cualquier exceso de heridas mortales de ese ataque.

## Criterio provisional de arbitraje

Hasta que aparezca **Characteristic Modifiers**, una mesa o evento puede adoptar expresamente la fórmula de la edición anterior:

1. Determinar primero el atributo aleatorio.
2. Cambiar o sustituir valores.
3. Dividir.
4. Multiplicar.
5. Sumar.
6. Restar.
7. Redondear al alza al final.

Con ese criterio provisional, cambiar el Daño a 0 se aplicaría antes que `[FUSIÓN 2]`, dando como resultado Daño 2. Este resultado era una FAQ expresa de la edición anterior, pero todavía no está confirmado por una fuente publicada para la edición de 2026.

## Fundamento de reglas

- [[Daño (D)]]: Reglas básicas, Armas `02.04`, página 10.
- Modificadores de atributos: la página 11 incluye **Characteristic Modifiers** entre las referencias aplicables a perfiles y armas, pero no contiene su definición.
- Soporte digital: la página 86 explica que la app oficial contiene definiciones ampliadas, interacciones poco frecuentes y FAQ. Sin embargo, **Characteristic Modifiers** no figura actualmente en el manual de la app.
- [[Infligir daño]]: Reglas básicas, Infligir daño `05.04`.
- [[Heridas mortales]]: Reglas básicas, Heridas mortales `06.02`.
- [[Heridas devastadoras]]: Reglas básicas, `[HERIDAS DEVASTADORAS]` `24.10`, página 80.
- [[Fusión]]: Reglas básicas, `[FUSIÓN]` `24.25`, página 83. Su ejemplo convierte un atributo `D6` en `D6+2`.
- PDF oficial de las Reglas básicas de 2026: https://assets.warhammer-community.com/eng_01-06_warhammer40k_new40k_core_rules-was6fbu1ix-hfewhmxyiy.pdf
- Descargas oficiales de Warhammer 40,000: https://www.warhammer-community.com/en-gb/downloads/warhammer-40000/
- Precedente histórico: *Core Rules Updates* versión 1.8 con *Rules Commentary* versión 1.7 de la edición anterior.

## Resumen para arbitraje casual

El PDF de 2026 remite a **Characteristic Modifiers**, pero la definición no está publicada ni en sus 88 páginas ni actualmente en el manual de la app. La fórmula de la edición anterior puede usarse como criterio provisional acordado, no como una regla de 2026 ya verificada.
