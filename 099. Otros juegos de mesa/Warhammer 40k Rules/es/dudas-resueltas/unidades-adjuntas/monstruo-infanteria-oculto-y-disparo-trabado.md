---
type: rules-question
category: attached-units
canonical: false
source: core-rules
surface: resolved-question
owner-domain: attached-units
status: verified
rules:
  - 10.06
  - 13.08
  - 13.09
  - 17.03
  - 19.03
tags:
  - warhammer40k
  - resolved-question
  - attached-units
  - terrain
  - shooting
  - rules-application
aliases:
  - monstruo en unidad de infanteria oculto
  - hidden con monstruo en unidad adjunta
  - unidad adjunta monstruo infanteria cobertura
  - zoantropos con monstruo oculto
  - disparar trabado con monstruo y guardaespaldas
  - monster attached unit hidden
related:
  - Claves en unidades adjuntas
  - Claves diversas en unidades
  - Unidad adjunta
  - Oculto
  - Beneficiarse de cobertura
  - Disparo a quemarropa
  - Disparar contra Monstruos y Vehículos trabados
---

# Si una unidad adjunta mezcla un monstruo con infantería, ¿cómo funcionan Oculto, cobertura y disparar trabado?

## Respuesta corta

La [[Unidad adjunta]] tiene todas las claves de sus componentes a nivel de unidad, pero sus miniaturas no ganan las claves de las demás. Por tanto, una unidad que contiene un monstruo y miniaturas de infantería puede ser una unidad `MONSTRUO` e `INFANTERÍA`, pero el monstruo no se convierte en miniatura `INFANTERÍA` y las miniaturas de infantería no se convierten en miniaturas `MONSTRUO`.

Para [[Oculto]], se mira cada miniatura: solo pueden estar ocultas las miniaturas `INFANTERÍA`, `BESTIAS` o `ENJAMBRE` que cumplan los requisitos. El monstruo no se beneficia de Oculto por estar en una unidad que también tiene `INFANTERÍA`.

Además, si cualquier miniatura de esa unidad realiza ataques a distancia, incluido el monstruo, la unidad ha realizado ataques a distancia. Eso impide que sus miniaturas estén ocultas durante ese turno y el turno siguiente.

## Regla práctica

1. Si una regla pregunta si la unidad tiene una clave, usa el conjunto completo de claves de la unidad adjunta.
2. Si una regla pregunta si una miniatura tiene una clave, mira solo las claves propias de esa miniatura.
3. Si una condición habla de lo que ha hecho la unidad, cualquier miniatura que actúe puede hacer que la unidad cumpla o incumpla esa condición.

## Oculto

[[Oculto]] exige que la miniatura tenga la clave `INFANTERÍA`, `BESTIAS` o `ENJAMBRE`, que esté en el área de terreno correspondiente y que su unidad no haya realizado ataques a distancia durante este turno ni durante el anterior.

En una unidad adjunta mixta:

- Las miniaturas `INFANTERÍA`, `BESTIAS` o `ENJAMBRE` pueden estar ocultas si cumplen el resto de requisitos.
- El monstruo no está oculto salvo que él mismo tenga una de esas claves.
- Si dispara el monstruo, la unidad ha realizado ataques a distancia; por tanto, las miniaturas de infantería tampoco estarán ocultas durante ese turno ni durante el turno siguiente.
- Si disparan las miniaturas de infantería, ocurre lo mismo: la unidad ha realizado ataques a distancia y se pierde la condición de Oculto para las miniaturas que pudieran beneficiarse.

## Cobertura

[[Beneficiarse de cobertura]] se comprueba contra el ataque a distancia y exige que todas las miniaturas de la unidad blanco cumplan al menos una de las condiciones de cobertura.

Esto significa que no basta con que las miniaturas de infantería estén en un área de terreno. Si el monstruo de la misma unidad no cumple ninguna condición de cobertura contra ese ataque, la unidad no se beneficia de cobertura contra ese ataque.

## Disparar estando trabado

Una unidad trabada que no avanzó puede usar [[Disparo a quemarropa]] si tiene alguna arma `[A QUEMARROPA]` o si es una unidad `MONSTRUO` o `VEHÍCULO`.

En una unidad adjunta que tiene la clave `MONSTRUO` por contener un monstruo, la unidad puede cumplir esa condición como unidad `MONSTRUO`. Pero las restricciones posteriores se aplican por miniatura:

- Las miniaturas `MONSTRUO` o `VEHÍCULO` pueden disparar estando trabadas con las restricciones normales de [[Disparo a quemarropa]].
- Las miniaturas que no sean `MONSTRUO` ni `VEHÍCULO` solo pueden disparar armas `[A QUEMARROPA]` y solo contra unidades enemigas trabadas con su unidad.
- Las armas `[ÁREA]` no pueden tomar como blanco una unidad con la que la unidad atacante esté trabada.

## Que el enemigo dispare contra esa unidad trabada

[[Disparar contra Monstruos y Vehículos trabados]] permite elegir como blanco a una unidad enemiga `MONSTRUO` o `VEHÍCULO` que esté trabada.

Si la unidad adjunta tiene la clave `MONSTRUO` por contener un monstruo, el enemigo puede elegir esa unidad como blanco aunque también contenga miniaturas que no sean monstruo. El blanco es la unidad. Después, los ataques se asignan siguiendo las reglas normales para atacar a unidades adjuntas; la regla de disparar contra monstruos trabados no obliga a que las heridas vayan al monstruo.

## Ejemplo

Una unidad adjunta contiene un monstruo `PERSONAJE` y varias miniaturas `INFANTERÍA`, como un caso de monstruo unido a Zoántropos u otra escolta similar.

Mientras no hayan disparado en este turno ni en el anterior, las miniaturas `INFANTERÍA` pueden estar [[Oculto|ocultas]] si están en el terreno adecuado. El monstruo no está oculto solo por acompañarlas.

Si el monstruo dispara, la unidad ha realizado ataques a distancia. Desde ese momento, las miniaturas de infantería de esa unidad dejan de cumplir la condición de Oculto para ese turno y tampoco podrán estar ocultas durante el turno siguiente.

Si la unidad está trabada y no avanzó, puede usar [[Disparo a quemarropa]] porque la unidad tiene `MONSTRUO`. El monstruo podrá disparar como miniatura `MONSTRUO`; las miniaturas de infantería solo podrán disparar armas `[A QUEMARROPA]` si las tienen.

## Errores comunes

- Pensar que la clave `INFANTERÍA` de la unidad convierte al monstruo en miniatura `INFANTERÍA`.
- Pensar que la clave `MONSTRUO` de la unidad convierte a los guardaespaldas en miniaturas `MONSTRUO`.
- Aplicar [[Oculto]] a toda la unidad en vez de a las miniaturas que cumplen sus requisitos.
- Mantener Oculto en la infantería después de que haya disparado otra miniatura de la misma unidad.
- Pensar que, si el enemigo dispara contra una unidad `MONSTRUO` trabada, las heridas deben asignarse obligatoriamente al monstruo.

## Fundamento de reglas

- [[Claves en unidades adjuntas]] y [[Claves diversas en unidades]]: la unidad reúne las claves de sus componentes, pero las miniaturas no ganan claves ajenas.
- [[Oculto]]: el requisito de clave se comprueba en la miniatura, y la condición de no haber disparado se comprueba en la unidad.
- [[Beneficiarse de cobertura]]: todas las miniaturas de la unidad blanco deben cumplir una condición de cobertura.
- [[Disparo a quemarropa]]: permite disparar a unidades trabadas en casos concretos y distingue entre miniaturas `MONSTRUO`/`VEHÍCULO` y las que no lo son.
- [[Disparar contra Monstruos y Vehículos trabados]]: permite elegir como blanco una unidad enemiga `MONSTRUO`/`VEHÍCULO` trabada, sin cambiar la asignación normal de ataques.
- Fuente oficial: `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, referencias `10.06`, `13.08`, `13.09`, `17.03` y `19.03`.

## Resumen para arbitraje casual

La unidad comparte claves solo a nivel de unidad. Para Oculto miras miniaturas: la infantería puede estar oculta, el monstruo no por esa razón. Pero si dispara cualquier miniatura de la unidad, incluido el monstruo, la unidad ha disparado y las miniaturas de esa unidad no pueden estar ocultas durante ese turno ni el siguiente.
