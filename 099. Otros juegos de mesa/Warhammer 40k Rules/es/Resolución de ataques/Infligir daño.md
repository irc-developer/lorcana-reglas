---
lang: es
translation_of: Inflict Damage
source_lang: en
type: procedure
category: attack-resolution
canonical: true
source: core-rules
surface: article
owner-domain: attack-resolution
tags:
  - warhammer40k
  - attack-resolution
  - procedimiento
aliases:
  - Infligir daño
  - Resolver daño
related:
  - Sistema de ataque
  - Secuencia de ataque
  - Tiradas de salvación
  - Heridas mortales
---

# Infligir daño

## Resumen

Infligir daño es el paso que comprueba las tiradas de salvación, asigna ataques a miniaturas y reduce sus heridas restantes.

## Definición

El jugador oponente resuelve cada tirada de salvación, de menor a mayor, hasta resolver todos los ataques o hasta que todas las miniaturas de la unidad blanco sean eliminadas.

## Reglas

Para cada tirada de salvación:

1. Elige una miniatura del grupo de asignación en curso. Si es posible, debe ser una miniatura que ya haya perdido una o más heridas.
2. Comprueba la tirada de salvación:
   - Un resultado sin modificar de 1 inflige daño.
   - Si el grupo tiene S Inv y el resultado es igual o mayor que ese atributo, el ataque falla.
   - Si, tras aplicar la FP del arma atacante, el resultado es igual o mayor que el atributo S del grupo, el ataque falla.
   - Cualquier otro resultado inflige daño.
3. Si el ataque inflige daño, la miniatura elegida pierde una cantidad de heridas igual al atributo D del ataque.
4. Si sus heridas restantes se reducen a 0 o menos, la miniatura resulta eliminada.

Cuando todas las miniaturas de un grupo de asignación son eliminadas, el siguiente grupo en el orden de asignación se convierte en el grupo en curso.

## Interacciones

- [[Tiradas de salvación]] crea los grupos y el orden de asignación.
- [[Heridas mortales]] usa una secuencia distinta y no se evita mediante tiradas de salvación normales.
- Modificadores de daño pueden cambiar cuántas heridas se pierden, si una regla lo permite.

## Restricciones

- Si todas las miniaturas de la unidad blanco son eliminadas, se pierden los ataques sobrantes.
- La miniatura elegida debe ser una miniatura ya herida si es posible.
- Este artículo no cubre daños que no pasen por tiradas de salvación, como [[Heridas mortales]].

## Dominio

Parte de:
[[Sistema de ataque]]

## Navegación

- Vuelve a [[Tiradas de salvación]] para crear grupos y tirar salvaciones.
- Consulta [[Heridas mortales]] si el daño no usa la secuencia normal de salvación.

## Referencias

- Reglas básicas oficiales: Infligir daño 05.04.
