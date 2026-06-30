---
type: rules-question
category: attack-resolution
canonical: false
source: core-rules-app
surface: resolved-question
owner-domain: attack-resolution
status: verified
rules:
  - 02.02.01
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
  - daño reducido a cero y fusión
  - no se suma fusión si el daño es cero
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

La app oficial sí contiene la regla general de modificadores. Para calcular el [[Daño (D)|Daño]] final de un ataque, aplica los modificadores en este orden:

1. Cambiar o reemplazar el valor por un valor especificado, por ejemplo cambiar el Daño a `0`.
2. Multiplicar.
3. Sumar, por ejemplo [[Fusión|[FUSIÓN X]]].
4. Dividir, por ejemplo reducir el Daño a la mitad.
5. Restar.
6. Redondear al alza cualquier fracción, después de aplicar todos los modificadores.

Pero antes de hacer esa cuenta hay una comprobación más importante: **solo puedes sumar, restar, multiplicar o dividir si el ataque conserva un atributo D numérico modificable**.

Si una regla reduce el Daño a `0`, lo cambia a `-`, indica que el ataque no inflige daño o deja el Daño sin valor numérico, no le sumas nada después. No añades [[Fusión|[FUSIÓN X]]], no aplicas otros `+1 al Daño` y no intentas reconstruir un Daño a partir de `0`, `-` o "nada".

La parte fácil de olvidar en los casos que sí tienen Daño numérico es que **la suma va antes que la división**.

## Regla práctica

Cuando una regla cambia o reemplaza un atributo por un valor concreto, ese cambio se resuelve antes que los modificadores matemáticos. A partir de ese nuevo valor, aplicas multiplicaciones, sumas, divisiones y restas.

Sin embargo, si esa regla deja el Daño en `0`, `-` o sin infligir daño, la secuencia se detiene para ese ataque: no hay un atributo D válido sobre el que aplicar sumas posteriores.

Si el atributo ya incluye un operador, ese operador forma parte del atributo y no es un modificador externo. Por ejemplo, si el arma tiene Daño `D6+1`, primero determinas ese valor completo y después aplicas los modificadores.

Las fracciones no se redondean en mitad del cálculo. Se redondea al alza solamente al final, después de todos los modificadores.

## Ejemplos

### Daño reducido a 0

Un ataque de Daño 6 está sujeto a una regla que reduce su Daño a `0`.

Ese ataque queda en Daño 0. Si también tendría `[FUSIÓN 2]`, no le sumas ese `+2`: sigue siendo Daño 0.

### Daño `-`, sin Daño o sin infligir daño

Si una regla cambia el atributo D del ataque a `-`, hace que el ataque no inflija daño o dice que su Daño se reduce a nada, no hay un valor numérico que modificar.

En esos casos, no añades `[FUSIÓN X]`, no aplicas `+1 al Daño` y no pasas a dividir o restar. El ataque no recupera Daño por modificadores posteriores.

### Fusión y reducción a la mitad con Daño numérico

Un ataque de Daño 4 recibe `[FUSIÓN 2]` y después otra regla reduce su Daño a la mitad.

Como el ataque sí conserva un Daño numérico, se aplica el orden normal:

`(4 + 2) ÷ 2 = 3`

El resultado es Daño 3.

### Sumar y reducir a la mitad

Un ataque de Daño 5 recibe `+1 al Daño` y después se reduce a la mitad.

`(5 + 1) ÷ 2 = 3`

El resultado es Daño 3. No es `5 ÷ 2 + 1`.

### Reducir a la mitad y restar

Un ataque de Daño 5 se reduce a la mitad y además recibe `-1 al Daño`.

`5 ÷ 2 - 1 = 1,5`

Después de aplicar todos los modificadores, se redondea al alza:

`1,5 → 2`

El resultado es Daño 2.

### Daño aleatorio

Un arma tiene Daño `D6+1`. Sacas un `4`, así que su Daño es `5`. Si luego recibe `+1 al Daño` y se reduce a la mitad:

`(5 + 1) ÷ 2 = 3`

El `+1` del perfil `D6+1` no es el mismo modificador que el `+1 al Daño` aplicado después.

## Heridas devastadoras

[[Heridas devastadoras]] usa el atributo D del ataque para determinar cuántas heridas mortales se infligen cuando se obtiene una herida crítica.

Por tanto, si el atributo D está modificado, primero calcula el Daño final con el orden anterior. Después usa ese valor final para determinar las heridas mortales de Heridas devastadoras.

Esto no convierte cualquier herida mortal adicional del arma en Daño modificable. Si una regla causa heridas mortales por otro medio, solo se modifican si esa propia regla lo permite.

## Errores comunes

- Aplicar la división antes que la suma.
- Redondear inmediatamente después de dividir.
- Tratar el `+1` de `D6+1` como si fuera un modificador externo.
- Resolver `[FUSIÓN]` antes de cambiar el Daño a 0.
- Sumar `[FUSIÓN]` a un ataque cuyo Daño fue reducido a `0`, cambiado a `-` o anulado.
- Pensar que un ataque que no inflige daño puede recuperar Daño mediante modificadores posteriores.
- Aplicar modificadores al Daño de Heridas devastadoras después de convertirlo en heridas mortales.

## Fuentes oficiales

- App oficial de Warhammer 40,000, Reglas básicas, `02. Hojas de datos`, `02.02 Perfiles`, `02.02.01 Modificadores`: orden para aplicar modificadores.
- `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, `02.04` Profiles and Weapons: atributo `D` y referencia no desarrollada a `Characteristic Modifiers`.
- `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, `05.04` Inflict Damage: pérdida de heridas igual al atributo `D`.
- `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, `06.02` Mortal Wounds: resolución de heridas mortales.
- `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, `24.10` `[DEVASTATING WOUNDS]`.
- `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, `24.25` `[MELTA]`.

## Resumen para arbitraje casual

Para calcular Daño: cambia o reemplaza valores, multiplica, suma, divide, resta y redondea al alza al final. Pero si una regla reduce el Daño a `0`, lo cambia a `-` o hace que el ataque no inflija daño, paras ahí: no se le suma `[FUSIÓN]` ni ningún otro bono posterior.
