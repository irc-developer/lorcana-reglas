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
  - 19.00
  - 19.01
  - 19.02
  - 24.28
  - 24.34
tags:
  - warhammer40k
  - resolved-question
  - attached-units
  - attack-resolution
  - rules-application
aliases:
  - puedo asignar heridas al líder antes que al apoyo
  - puedo asignar heridas al apoyo antes que al líder
  - asignar heridas con líder y apoyo
  - heridas en unidad con líder y apoyo
  - quién muere primero líder apoyo o guardaespaldas
  - precisión contra líder y apoyo
related:
  - Tiradas de salvación
  - Infligir daño
  - Unidad adjunta
  - Atacar a unidades adjuntas
  - Formar unidades adjuntas
  - Líder
  - Apoyo
  - Precisión
  - precision-con-dos-personajes
---

# ¿Cómo se asignan heridas si una unidad adjunta tiene Líder y Apoyo?

## Respuesta corta

Mientras queden miniaturas guardaespaldas que no sean `PERSONAJE`, no puedes asignar ataques al [[Líder]] ni al [[Apoyo]] por decisión propia. En el orden normal de asignación, los grupos que no son `PERSONAJE` van antes que los grupos `PERSONAJE`.

Cuando ya solo quedan miniaturas `PERSONAJE`, el [[Líder]] y el [[Apoyo]] no tienen una prioridad especial entre sí. Se ordenan como grupos `PERSONAJE`: si uno ya está herido, ese grupo va antes que los `PERSONAJE` sin heridas; si ninguno está herido, puedes elegir el orden aplicable.

## Regla práctica

No pienses en "Líder primero y Apoyo después" ni en "Apoyo como segunda guardaespaldas". La pregunta importante es si cada grupo de asignación es `PERSONAJE` o no.

- Las miniaturas guardaespaldas no `PERSONAJE` van antes.
- Cada miniatura `PERSONAJE` forma su propio grupo de asignación.
- Los grupos `PERSONAJE` no se adelantan a los grupos que no son `PERSONAJE`.
- Entre grupos `PERSONAJE`, un grupo con una miniatura herida va antes que uno sin miniaturas heridas.

## Cómo decidirlo en mesa

1. Comprueba si la unidad adjunta todavía tiene miniaturas guardaespaldas que no sean `PERSONAJE`.
2. Si las tiene, esos grupos no `PERSONAJE` deben ir antes que el [[Líder]] y el [[Apoyo]].
3. Si ya no quedan grupos no `PERSONAJE`, crea un grupo por cada miniatura `PERSONAJE`.
4. Si uno de esos `PERSONAJE` ya ha perdido heridas, ponlo antes que los `PERSONAJE` sin heridas.
5. Si ninguno está herido, el jugador oponente puede ordenar esos grupos `PERSONAJE` de la forma válida que prefiera.

## Ejemplos

Una unidad tiene una guardaespaldas, un [[Líder]] y una unidad con [[Apoyo]], y tanto el Líder como el Apoyo son `PERSONAJE`. Mientras quede alguna miniatura de la guardaespaldas, los ataques se asignan primero a los grupos de guardaespaldas que correspondan. No puedes saltarte la guardaespaldas para matar antes al Líder o al Apoyo por asignación normal.

Si la guardaespaldas ya ha sido destruida y quedan el Líder y el Apoyo, ambos son grupos `PERSONAJE`. Si ninguno está herido, puedes poner primero al Líder o al Apoyo. Si decides asignar primero al Líder y sobrevive con heridas perdidas, ese Líder herido tendrá prioridad frente al Apoyo sin heridas en asignaciones posteriores de esa secuencia.

Si un ataque tiene [[Precisión]], el jugador activo puede elegir un grupo de asignación con miniaturas `PERSONAJE` visibles al inicio del paso de orden de asignación. En ese caso, puede dirigir esos ataques al Líder o al Apoyo visible aunque todavía queden guardaespaldas, siempre que se cumplan las condiciones de [[Precisión]].

## Errores comunes

- Pensar que el [[Apoyo]] cuenta como guardaespaldas para proteger al [[Líder]].
- Pensar que el [[Líder]] siempre debe morir antes que el [[Apoyo]].
- Pensar que el [[Apoyo]] siempre debe morir antes que el [[Líder]].
- Olvidar que cada miniatura `PERSONAJE` forma su propio grupo de asignación.
- Usar [[Precisión]] como si permitiera elegir cualquier miniatura, cuando exige un grupo `PERSONAJE` visible.

## Fundamento de reglas

- [[Tiradas de salvación]]: crea grupos de asignación, separa cada miniatura `PERSONAJE` y establece que los grupos `PERSONAJE` no pueden ir antes que grupos que no son `PERSONAJE`.
- [[Unidad adjunta]]: una unidad adjunta puede estar formada por guardaespaldas y unidades [[Líder]] y/o [[Apoyo]].
- [[Formar unidades adjuntas]]: explica que Líder y Apoyo se unen a la unidad guardaespaldas, no uno al otro.
- [[Atacar a unidades adjuntas]]: mantiene el marco de unidad adjunta al resolver ataques contra ella.
- [[Precisión]]: permite al jugador activo elegir un grupo de asignación `PERSONAJE` visible en el momento indicado.
- Fuente oficial: `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, referencias `05.03`, `19.00`, `19.01`, `19.02`, `24.28` y `24.34`.

## Resumen para arbitraje casual

Primero van los guardaespaldas no `PERSONAJE`. Cuando solo quedan Líder y Apoyo, ambos se tratan como grupos `PERSONAJE`: no hay prioridad especial por ser Líder o Apoyo, salvo que uno ya esté herido. Con [[Precisión]], el atacante puede escoger un grupo `PERSONAJE` visible si la regla se aplica.
