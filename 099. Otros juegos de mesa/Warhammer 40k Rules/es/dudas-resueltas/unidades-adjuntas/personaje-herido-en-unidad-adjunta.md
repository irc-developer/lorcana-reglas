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
  - personaje herido en unidad adjunta
  - personaje herido recibe las heridas antes que la guardaespaldas
  - lider herido recibe futuros ataques
  - lider herido y guardaespaldas
  - si un personaje esta herido hay que asignarle heridas
related:
  - Tiradas de salvación
  - Infligir daño
  - Atacar a unidades adjuntas
  - Unidad adjunta
  - Precisión
  - asignar-heridas-a-lider-y-apoyo
  - precision-con-dos-personajes
---

# ¿Un personaje herido en una unidad adjunta debe recibir primero las heridas de futuros ataques?

## Respuesta corta

No, no por asignación normal. Si una unidad adjunta todavía tiene miniaturas que no son `PERSONAJE`, los grupos que no son `PERSONAJE` van antes que los grupos `PERSONAJE`. Que el personaje ya haya perdido heridas no le permite saltarse esa prioridad.

La regla de elegir una miniatura ya herida se aplica dentro del grupo de asignación en curso. Si el grupo en curso es la guardaespaldas, eliges una miniatura herida de ese grupo si es posible. No cambias al grupo del personaje solo porque ese personaje esté herido.

## Regla práctica

Primero determina el orden de grupos en [[Tiradas de salvación]]:

- cada miniatura `PERSONAJE` forma su propio grupo;
- las demás miniaturas se agrupan por atributos de H, S y S Inv;
- los grupos que no son `PERSONAJE` van antes que los grupos `PERSONAJE`;
- entre grupos del mismo tipo, los grupos heridos se adelantan cuando la regla lo exige.

Después, en [[Infligir daño]], para cada ataque eliges una miniatura del grupo de asignación en curso. Si dentro de ese grupo hay una miniatura que ya ha perdido heridas, debes elegirla si es posible.

La clave es "dentro de ese grupo". Un `PERSONAJE` herido no adelanta a una guardaespaldas no `PERSONAJE`.

## Cómo decidirlo en mesa

1. Comprueba si la unidad adjunta todavía tiene grupos que no son `PERSONAJE`.
2. Si los tiene, esos grupos van antes que el personaje, aunque el personaje esté herido.
3. Resuelve los ataques contra el grupo en curso.
4. Dentro de ese grupo, asigna a una miniatura ya herida si es posible.
5. Cuando todas las miniaturas de ese grupo sean eliminadas, pasa al siguiente grupo del orden de asignación.
6. Cuando solo queden grupos `PERSONAJE`, un grupo `PERSONAJE` herido va antes que los grupos `PERSONAJE` sin heridas.

## Ejemplo

Una unidad adjunta contiene cinco guardaespaldas y un Líder `PERSONAJE`. En una activación anterior, un arma con [[Precisión]] hirió al Líder y le dejó con heridas perdidas.

Más tarde, la misma unidad adjunta recibe ataques normales sin [[Precisión]]. Aunque el Líder esté herido, el jugador oponente no asigna esos ataques al Líder mientras sigan quedando guardaespaldas que no son `PERSONAJE`. Los ataques se resuelven primero contra el grupo de guardaespaldas correspondiente.

Si todas las guardaespaldas son eliminadas y el Líder sigue vivo, entonces el grupo del Líder pasa a ser relevante. Si hay otros personajes en la unidad, el personaje herido irá antes que los personajes sin heridas.

## Qué pasa con Precisión

[[Precisión]] sí puede cambiar esta respuesta para los ataques que tengan esa habilidad.

Al inicio del paso de orden de asignación de esos ataques, el jugador activo puede elegir un grupo de asignación `PERSONAJE` visible. Si el personaje herido es visible y se cumplen las condiciones de [[Precisión]], el atacante puede hacer que ese grupo sea el grupo en curso aunque todavía queden guardaespaldas.

Eso no es porque el personaje esté herido, sino porque [[Precisión]] permite elegir un grupo `PERSONAJE` visible.

## Errores comunes

- Pensar que "la miniatura herida va primero" ignora el orden de grupos.
- Asignar ataques normales al Líder herido mientras todavía quedan guardaespaldas no `PERSONAJE`.
- Tratar a todos los personajes y guardaespaldas como un único grupo de heridas.
- Olvidar que cada miniatura `PERSONAJE` forma su propio grupo de asignación.
- Aplicar [[Precisión]] a ataques que no tienen esa habilidad.
- Usar la Resistencia del personaje mientras todavía quedan guardaespaldas en la unidad adjunta.

## Fundamento de reglas

- [[Tiradas de salvación]]: crea grupos de asignación, separa cada miniatura `PERSONAJE` y establece que los grupos no `PERSONAJE` van antes que los grupos `PERSONAJE`.
- [[Infligir daño]]: al resolver cada ataque se elige una miniatura del grupo en curso, y si es posible debe ser una miniatura de ese grupo que ya haya perdido heridas.
- [[Atacar a unidades adjuntas]]: mientras la unidad adjunta incluya miniaturas guardaespaldas, la tirada para herir usa la Resistencia más alta de esas miniaturas guardaespaldas.
- [[Precisión]]: permite al jugador activo elegir un grupo `PERSONAJE` visible en el momento indicado.
- Fuente oficial: `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, referencias `05.03`, `05.04`, `19.02` y `24.28`.

## Resumen para arbitraje casual

Un personaje herido no atrae automáticamente los ataques normales. Mientras queden guardaespaldas no `PERSONAJE`, van primero. Solo cuando el grupo del personaje sea el grupo en curso, o cuando un ataque con [[Precisión]] lo elija legalmente, las heridas posteriores pueden seguir entrando en ese personaje.
