---
type: rules-question
category: attached-units
canonical: false
source: core-rules
surface: resolved-question
owner-domain: attack-resolution
status: verified
rules:
  - 05.03
  - 05.04
  - 19.02
  - 24.28
tags:
  - warhammer40k
  - resolved-question
  - attached-units
  - attack-resolution
  - precision
  - rules-application
aliases:
  - cómo se asignan las heridas con precisión y dos personajes
  - precisión contra una unidad con dos personajes
  - puedo elegir entre dos personajes con precisión
  - puedo repartir precisión entre dos personajes
  - qué personaje recibe los ataques de precisión
related:
  - Precisión
  - Tiradas de salvación
  - Infligir daño
  - Atacar a unidades adjuntas
  - Unidad adjunta
  - asignar-heridas-a-lider-y-apoyo
---

# ¿Cómo se asignan las heridas si tengo Precisión y dos personajes en la unidad?

## Respuesta corta

Cada miniatura `PERSONAJE` forma su propio grupo de asignación. Al resolver ataques con [[Precisión]], el jugador activo puede elegir uno de los grupos `PERSONAJE` visibles para convertirlo en el grupo de asignación en curso.

Si los dos personajes son visibles, el atacante elige a cuál de los dos se asignan primero esos ataques. Si solo uno es visible, únicamente puede elegir a ese. Si ninguno es visible, [[Precisión]] no permite seleccionar sus grupos.

## Regla práctica

[[Precisión]] permite escoger un grupo `PERSONAJE` visible, pero no permite repartir libremente las tiradas de salvación entre varios personajes.

Una vez elegido el personaje:

- su grupo se convierte en el grupo de asignación en curso;
- los ataques se resuelven contra ese grupo;
- el jugador oponente no puede cambiar a otro personaje mientras el grupo elegido siga siendo el grupo en curso;
- si todas las miniaturas del grupo son eliminadas, se pasa al siguiente grupo del orden de asignación.

Como cada miniatura `PERSONAJE` tiene su propio grupo, normalmente eliminar al personaje elegido significa eliminar todo ese grupo.

## Cómo decidirlo en mesa

1. Separa cada miniatura `PERSONAJE` en su propio grupo de asignación.
2. Comprueba cuáles de esos personajes son visibles para el atacante.
3. Al inicio del paso de orden de asignación, el jugador activo decide si usa [[Precisión]].
4. Si la usa, elige uno de los grupos `PERSONAJE` visibles como grupo en curso.
5. Resuelve las tiradas de salvación y el daño contra ese grupo.
6. Si el personaje elegido es eliminado y quedan ataques por resolver, continúa con el siguiente grupo del orden de asignación.

## Ejemplo

Una unidad adjunta contiene una unidad guardaespaldas, un Líder y un Apoyo. Tanto el Líder como el Apoyo tienen la clave `PERSONAJE`.

El atacante consigue cuatro heridas con un arma con [[Precisión]] y puede ver a ambos personajes. Al inicio del orden de asignación, elige el grupo del Líder. Las salvaciones correspondientes se resuelven contra el Líder; el jugador defensor no puede decidir que algunas se asignen al Líder y otras al Apoyo para repartir el daño.

Si el Líder es eliminado antes de resolver todos los ataques, los ataques restantes pasan al siguiente grupo establecido en el orden de asignación. No pasan automáticamente al Apoyo salvo que su grupo sea el siguiente en ese orden.

Si, en cambio, el atacante solo puede ver al Apoyo, no puede elegir al Líder mediante [[Precisión]], aunque el Líder forme parte de la misma unidad adjunta.

## Resistencia y salvación

[[Precisión]] modifica la asignación de los ataques, pero no cambia la Resistencia utilizada en la tirada para herir.

Mientras la unidad adjunta incluya miniaturas guardaespaldas, los ataques se resuelven usando la Resistencia más alta de esas miniaturas guardaespaldas, incluso si después se asignan a un personaje mediante [[Precisión]].

Las tiradas de salvación y el daño sí se resuelven usando el grupo del personaje elegido.

## Errores comunes

- Permitir que el defensor elija cuál de los dos personajes recibe los ataques de [[Precisión]].
- Repartir libremente las salvaciones de un mismo grupo de ataques entre ambos personajes.
- Elegir mediante [[Precisión]] un personaje que no sea visible.
- Pensar que todos los personajes forman un único grupo porque tienen los mismos atributos.
- Usar la Resistencia del personaje elegido para la tirada para herir mientras todavía quedan guardaespaldas.
- Suponer que los ataques sobrantes pasan automáticamente al segundo personaje cuando el primero es eliminado.

## Fundamento de reglas

- [[Tiradas de salvación]]: cada miniatura `PERSONAJE` forma su propio grupo de asignación.
- [[Precisión]]: el jugador activo puede elegir un grupo de asignación `PERSONAJE` visible al inicio del paso de orden de asignación.
- [[Infligir daño]]: los ataques se asignan a miniaturas del grupo en curso y, cuando ese grupo es eliminado, se continúa con el siguiente grupo del orden de asignación.
- [[Atacar a unidades adjuntas]]: mientras queden guardaespaldas, se usa la Resistencia más alta de esas miniaturas para resolver los ataques.
- Referencias oficiales: `05.03`, `05.04`, `19.02` y `24.28`.

## Resumen para arbitraje casual

Con dos personajes visibles, el atacante elige uno de sus grupos al usar [[Precisión]]. Los ataques se resuelven contra ese personaje y no se pueden repartir libremente entre ambos. Si el grupo elegido es eliminado, los ataques restantes siguen el orden de asignación ya establecido.
