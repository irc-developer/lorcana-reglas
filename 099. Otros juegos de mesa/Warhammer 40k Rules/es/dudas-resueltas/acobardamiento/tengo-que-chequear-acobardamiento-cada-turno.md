---
type: rules-question
category: battle-shock
canonical: false
source: core-rules
surface: resolved-question
owner-domain: battle-shock
status: verified
rules:
  - 01.07
  - 08.03
tags:
  - warhammer40k
  - resolved-question
  - battle-shock
  - command-phase
  - half-strength
  - rules-application
aliases:
  - tengo que chequear acobardamiento cada turno
  - se repite la tirada de acobardamiento
  - unidad por debajo del 50 por ciento
  - unidad a mitad de efectivos
  - superar acobardamiento evita futuras tiradas
related:
  - Acobardamiento en fase de mando
  - Tiradas de acobardamiento
  - Acobardada
  - Efectivos iniciales y mitad de efectivos
  - Fase de mando
  - Control de objetivos (CO)
  - Usar estratagemas
  - Sistema de acciones
  - Retroceder
---

# Si una unidad está por debajo del 50 % de efectivos, ¿tengo que chequear acobardamiento cada turno?

## Respuesta corta

**Sí, en cada una de tus fases de mando** debes hacer una [[Tiradas de acobardamiento|tirada de acobardamiento]] por esa unidad mientras siga **a mitad de efectivos o por debajo**, aunque superase la tirada anterior y no esté acobardada.

No se comprueba al inicio de cada turno de ambos jugadores. La tirada se hace en el paso de [[Acobardamiento en fase de mando|Acobardamiento]] de la fase de mando del jugador activo, solamente para las unidades de ese jugador.

## Cómo funciona

En tu paso de Acobardamiento, cada una de tus unidades debe hacer una tirada si cumple una o ambas condiciones:

- Está acobardada.
- Está a mitad de efectivos o por debajo.

Por tanto, superar una tirada no concede inmunidad para los turnos posteriores. Si en tu siguiente fase de mando la unidad sigue a mitad de efectivos o por debajo, vuelve a tirar.

Si la unidad ya estaba acobardada y supera la tirada realizada durante este paso, deja de estar acobardada. Si falla una tirada, la unidad y todas sus miniaturas pasan a estar acobardadas.

## Resumen de los efectos de estar acobardada

Mientras una unidad esté [[Acobardada|acobardada]]:

- El atributo [[Control de objetivos (CO)|CO]] de todas sus miniaturas se modifica a “-”. La raya no equivale a 0 ni representa un valor numérico: esas miniaturas son incapaces de controlar objetivos.
- Su jugador controlador no puede tomarla como blanco de sus propias [[Usar estratagemas|estratagemas]].
- No puede iniciar [[Sistema de acciones|acciones]] y no puede completar una acción que ya hubiese iniciado.
- Si está trabada y quiere [[Retroceder|retroceder]], no puede elegir Retirada ordenada: debe usar Huida desesperada y hacer una tirada de riesgo por cada miniatura de la unidad.

Por tanto, mientras la unidad siga acobardada, un modificador numérico como `+1 CO` no convierte “-” en 1. Para que esas miniaturas puedan controlar un objetivo, la unidad debe dejar de estar acobardada o una regla debe anular expresamente este efecto.

Estar acobardada no impide por sí solo que la unidad mueva, dispare, declare una carga o combata. Esas actividades solo quedan restringidas si otra regla aplicable lo indica.

## ¿Hay otros casos que se comprueben cada turno?

Para las tiradas de acobardamiento de la fase de mando hay **dos condiciones recurrentes**. En cada una de tus fases de mando, una unidad tira si:

- Está acobardada, aunque ya no esté a mitad de efectivos o por debajo.
- Está a mitad de efectivos o por debajo, aunque no esté acobardada.

Cumplir ambas condiciones no provoca dos tiradas: se hace **una sola tirada por unidad** en ese paso.

Fuera de estas condiciones no existe una comprobación general que debas hacer automáticamente al inicio de todos los turnos. Una misión, habilidad, estratagema u otra regla puede ordenar una tirada o efecto adicional, pero se resuelve únicamente en el momento indicado por esa regla.

Por ejemplo, después de una [[Retroceder|Huida desesperada]], una unidad que no esté acobardada debe hacer una tirada de acobardamiento. Esa es una tirada adicional provocada por el movimiento, no una comprobación que se repita al inicio de cada turno.

Del mismo modo, las reglas que duran «hasta el inicio de la siguiente fase de mando» simplemente terminan en ese momento, salvo que su propio texto exija realizar una tirada o comprobación.

## Ejemplo

Una unidad empezó la batalla con 10 miniaturas y ahora tiene 5:

1. Está a mitad de efectivos, por lo que tira por acobardamiento en tu fase de mando.
2. Supera la tirada y no queda acobardada.
3. En tu siguiente fase de mando sigue teniendo 5 miniaturas.
4. Debe volver a tirar, aunque superase la comprobación anterior.

Durante la fase de mando del oponente no hace esta tirada por el mero hecho de estar a mitad de efectivos, porque no es una unidad del jugador activo.

## Matiz sobre el 50 %

La condición no es únicamente estar por debajo del 50 %. También se hace la tirada cuando la unidad está **exactamente a mitad de efectivos**.

Por ejemplo:

- Una unidad con efectivos iniciales de 10 tira cuando le quedan 5 miniaturas o menos.
- Una unidad con efectivos iniciales de 9 no puede estar exactamente a mitad de efectivos; está bajo mitad cuando le quedan 4 miniaturas o menos.
- Una unidad de una sola miniatura usa sus heridas restantes respecto a su atributo H para determinar si está a mitad de efectivos o por debajo.

## Vehículos y otras unidades de una sola miniatura

Sí: un vehículo que sea una unidad de una sola miniatura debe tirar por acobardamiento cuando le quede la mitad o menos de su atributo H.

Esto no depende de la clave `VEHÍCULO`. La misma regla se aplica a cualquier unidad de una sola miniatura, como un monstruo o un personaje que opere por separado.

Por ejemplo:

- Un vehículo con H 12 está a mitad de efectivos con 6 heridas restantes y tira con 6 o menos.
- Un vehículo con H 11 no puede estar exactamente a mitad de efectivos; está bajo mitad con 5 heridas restantes y tira con 5 o menos.

Si una unidad contiene varias miniaturas vehículo, se compara el número de miniaturas restantes con sus efectivos iniciales. No se suman las heridas perdidas de todos sus vehículos para calcular el 50 %.

## Errores comunes

- Hacer la tirada una sola vez, al cruzar por primera vez el umbral.
- Pensar que superar una tirada evita las comprobaciones posteriores.
- Hacer dos tiradas porque la unidad está acobardada y también a mitad de efectivos o por debajo.
- Tirar al inicio de cada turno en vez de hacerlo en el paso de Acobardamiento de la fase de mando.
- Olvidar que estar exactamente al 50 % también obliga a tirar.
- Hacer la tirada durante la fase de mando del oponente por una unidad que no pertenece al jugador activo.
- Tratar cualquier efecto que termina al inicio de una fase como si exigiese una tirada.
- Sumar las heridas perdidas de una unidad con varios vehículos en vez de contar sus miniaturas restantes.

## Fundamento de reglas

- [[Acobardamiento en fase de mando]]: el jugador activo hace una tirada por cada una de sus unidades que esté acobardada y/o a mitad de efectivos o por debajo.
- [[Tiradas de acobardamiento]]: una tirada fallida hace que la unidad pase a estar acobardada.
- [[Efectivos iniciales y mitad de efectivos]]: define cuándo una unidad está a mitad de efectivos o bajo mitad de efectivos.
- [[Retroceder]]: Huida desesperada puede provocar una tirada adicional fuera del paso normal de Acobardamiento.
- Fuente oficial: `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, referencias `08.03` Battle-shock, `01.07` Battle-shock Rolls, y Rules Appendix, Starting Strength.

## Resumen para arbitraje casual

Mientras una unidad siga a mitad de efectivos o por debajo, tira por acobardamiento en cada una de sus propias fases de mando. En una unidad de una sola miniatura, incluidos muchos vehículos, el umbral se calcula mediante sus heridas restantes. Haber superado la tirada anterior no evita la siguiente. No se tira automáticamente durante el turno del oponente.
