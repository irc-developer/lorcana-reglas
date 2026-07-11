# Reglas completas de Disney Lorcana 2.2: todos los cambios respecto a la versión 2.1

## Introducción

Ravensburger ha publicado las **Disney Lorcana TCG Comprehensive Rules, versión 2.2.0**, con fecha de entrada en vigor del **9 de julio de 2026**. Este artículo compara su texto completo con la versión oficial **2.1.0**, vigente desde el 30 de abril de 2026.

El PDF oficial 2.2 es la fuente normativa. Este artículo organiza y explica sus cambios, pero no sustituye las Comprehensive Rules ni una aclaración oficial aplicable a una interacción concreta.

## Resumen ejecutivo

1. **El daño se calcula mediante un proceso único** (1.9.4): daño base, modificadores y cantidad total. El mismo proceso alimenta los desafíos y los efectos.
2. **Una fuente sigue considerándose que inflige daño aunque este se reduzca a 0**, pero el personaje o la localización no reciben daño (1.9.5 y 8.8.2). Esto puede disparar habilidades que comprueban si una acción infligió daño.
3. **Las excepciones de construcción de mazos solo funcionan si su propia carta ya es legal** (1.10.1.3). Una carta no puede legalizarse a sí misma mediante su habilidad.
4. **Jugar una carta encima de otra no impide el último disparo de la carta inferior** cuando su condición comprueba que se juega la carta superior (4.3.4.2).
5. **Preparar al desafiante no lo retira del desafío** (4.6.4.4). Abandonar la zona de juego sigue siendo lo relevante para salir del desafío.
6. **Las cartas inferiores de una pila adquieren el estado de la superior al cambiar de zona** (5.1.1.7). Si la pila va al descarte, todas quedan boca arriba.
7. **Los efectos opcionales con coste no continúan si el coste no se puede pagar** (6.1.4.1), y se precisa cuándo se paga tinta y cuándo se hacen elecciones durante la resolución (6.7.2–6.7.2.2).
8. **Shift se amplía de forma sustancial** con Duo Shift, Combo Shift, Temporary Shift y Potato Shift, además de reglas para dos cartas inferiores, cartas que no son personajes y variantes combinadas (8.10.4.1–8.10.9).

## Cambios detallados

### Daño: reglas 1.9.4–1.9.6

En 2.1, el cálculo del daño estaba repartido entre las reglas de desafío y de resolución de efectos. La 2.2 crea un procedimiento general:

- el texto del efecto o la Fuerza {S} fija el daño base;
- se aplican todos los modificadores;
- el resultado es la cantidad total y los contadores se colocan simultáneamente.

La nueva 1.9.5 separa dos conceptos que antes podían confundirse: que una fuente **inflija daño** y que el objeto afectado **reciba daño**. Si Resist reduce la cantidad a 0, la fuente todavía satisface una condición del tipo «whenever one of your actions deals damage», pero el objeto no recibe daño.

La antigua 1.9.4, sobre la desaparición de contadores al abandonar el juego, pasa a 1.9.6 sin cambio funcional.

### Construcción del mazo: regla 1.10.1.3

Las habilidades que modifican la construcción funcionan fuera de la partida, pero solo después de comprobar que la carta que las contiene puede incluirse legalmente. *Christopher Robin – Hunny Sage* debe pertenecer primero a un mazo Amethyst/Sapphire; después, **Gather the Party** permite añadir otros personajes Hunny de tintas distintas.

Es una regla nueva con efecto práctico para jugadores, organizadores, Lore Guides y herramientas de validación de mazos.

### Jugar cartas y disparos: reglas 4.3.4.2 y 4.3.6

La 4.3.4.2 confirma que una habilidad de la carta inferior puede dispararse mientras la nueva carta entra encima de ella. La condición se cumple en 4.3.3, antes de que la fuente deje de estar en juego por quedar debajo.

El ejemplo de 4.3.6 se reescribe para dejar claro que un modificador aplicable al «siguiente personaje» también se aplica —y se consume— cuando ese personaje se juega gratis. No cambia el principio ya existente.

### Desafíos: reglas 4.6.4.4 y 4.6.6

Preparar al personaje desafiante durante el desafío no lo elimina de él. El cambio aclara una interacción de timing con consecuencias prácticas: el desafío continúa y las reglas de daño se aplican normalmente mientras ambos participantes sigan en la zona de juego.

Las reglas 4.6.6.1 y 4.6.6.2 ya no reproducen el cálculo del daño, sino que remiten al nuevo procedimiento de 1.9.4. Es una centralización, no una nueva fórmula.

### Pilas y estados: regla 5.1.1.7

Cuando la carta superior de una pila cambia de zona, las cartas inferiores se mueven a esa misma zona y adquieren los estados de la carta superior allí. Este cambio permite que efectos posteriores identifiquen correctamente cartas que estaban boca abajo y ahora están boca arriba en el descarte.

### Clasificaciones: reglas 5.3.3.2, 5.5.3 y 5.6.3

Se añaden **Boss**, **Red Panda**, **Team** y **Vineling** a la lista de clasificaciones de personaje. También se explicita que los objetos y las localizaciones pueden tener clasificaciones adicionales. Esto separa con claridad el tipo de carta de las demás clasificaciones impresas.

### Opcionalidad, condiciones y resolución: reglas 6.1.4.1 y 6.7.2–6.7.2.2

Si un efecto opcional incluye un coste y el jugador no puede pagarlo, se trata como si hubiera elegido no hacerlo: ninguna parte de esa opción ocurre.

La secuencia de resolución añade dos precisiones:

- un pago de tinta exigido en un paso se realiza durante ese mismo paso;
- las elecciones necesarias para comprobar una condición secundaria con *if* se hacen antes de comprobar si la condición es verdadera;
- las elecciones relativas al daño se hacen antes de calcular la cantidad total conforme a 1.9.4.

Estas precisiones afectan sobre todo a efectos de reemplazo, requisitos de elección y habilidades con una rama condicional.

### Efectos dependientes de una condición: reglas 6.1.15 y 6.1.16

Las antiguas «conditional static abilities» de 6.4.3–6.4.4 pasan a la sección general como **conditional dependent effects**. Las construcciones con *unless* e *if* conservan su funcionamiento. La regla sobre saltarse un paso o fase pasa de 6.4.5 a 6.4.3.

El traslado amplía el marco terminológico a efectos que no tienen por qué ser habilidades estáticas; la publicación oficial indica que no cambia las interacciones.

### Boost, Resist y Sing Together

- **Boost (8.4.1):** se define como efecto secuencial y se indica que puede resolverse cuando se podría usar una habilidad activada. Su funcionamiento no cambia.
- **Resist (8.8.2):** adopta la terminología de 1.9.5: reducir a 0 implica que el objeto no recibe daño, aunque la fuente siga considerándose que lo inflige.
- **Sing Together (8.12.1):** se ajusta la definición al lenguaje de los costes alternativos de las canciones; no se identifica un cambio de resultado.

### Las nuevas variantes de Shift: reglas 8.10.4.1–8.10.9

La 2.2 introduce el mayor bloque funcional de la actualización:

- **Duo Shift:** usa dos personajes, uno por cada nombre de la carta; las cartas inferiores se ordenan libremente.
- **Combo Shift:** permite usar un personaje que comparta uno de los nombres o dos personajes que aporten ambos.
- **Temporary Shift:** crea un disparo retardado que, al final del turno, retira el daño y devuelve solo la carta superior a la mano si sigue en juego.
- **Potato Shift:** permite desplazar un personaje sobre un objeto llamado Potato.
- **Estados combinados:** secándose prevalece sobre seco y agotado sobre preparado cuando se usan dos cartas.
- **Carta no personaje:** su antigüedad en juego determina si el personaje entra seco o secándose.
- **Variantes combinadas:** deben cumplirse las condiciones de todas las variantes incluidas en una sola habilidad.

## Aclaraciones y cambios editoriales

No toda diferencia modifica una jugada legal:

- **Funcionales:** 1.10.1.3, 4.3.4.2, 5.1.1.7, 6.1.4.1 y las nuevas variantes de Shift.
- **Aclaraciones con impacto práctico:** 1.9.5, 4.6.4.4 y la secuencia de 6.7.2.
- **Traslados o renumeraciones:** 1.9.4 pasa a 1.9.6; 6.4.3–6.4.4 pasan a 6.1.15–6.1.16; 6.4.5 pasa a 6.4.3.
- **Terminología:** *conditional static ability* se sustituye por *conditional dependent effect*; Resist adopta *takes no damage*.
- **Ejemplos y referencias:** 4.3.6, 4.6.6, 5.1.3, 6.1.6, 6.1.10 y 6.7.2.2 reciben correcciones o ejemplos adicionales.

## Comparación con la aproximación de Vine

Las *Set Release Notes: Attack of the Vine!* anticiparon correctamente el nuevo cálculo de daño, el traslado de los efectos condicionales, las reglas de construcción del mazo y el bloque principal de Shift. También acertaron en la combinación de estados al usar dos cartas y en que preparar a un desafiante no lo retira del desafío.

La publicación final aporta la redacción normativa y revela matices que la aproximación no podía cerrar: 1.9.5 mantiene la condición «deals damage» aunque la cantidad se reduzca a 0; 8.10.9 exige cumplir las condiciones de variantes combinadas; y numerosos *rulings* de cartas continúan siendo aclaraciones de las *release notes*, no nuevas reglas generales reproducidas literalmente en CR 2.2.

La tabla completa está en [[CR 2.2 - comparación final con Attack of the Vine]]. Desde el 9 de julio de 2026, ninguna predicción de Vine debe prevalecer sobre el texto 2.2.

## Qué deben tener en cuenta jugadores y Lore Guides

- **Jugadores casuales:** revisad las nuevas variantes de Shift y la diferencia entre infligir y recibir daño.
- **Jugadores competitivos:** comprobad la legalidad del mazo antes de aplicar una excepción de construcción y declarad con precisión las elecciones de efectos condicionales.
- **Lore Guides y jueces:** usad 1.9.4 como proceso único de daño, 4.6.4.4 para desafíos y 6.7.2 para ordenar pagos y elecciones.
- **Organizadores:** actualizad validadores y material de consulta a 2.2.0, pero no mezcléis estos cambios con política de torneos.
- **Creadores de contenido y desarrolladores:** diferenciad reglas generales de *rulings* específicos y actualizad referencias renumeradas.

## Conclusión

CR 2.2 no cambia la estructura básica de Disney Lorcana, pero formaliza interacciones que ya necesitaban una respuesta precisa y amplía Shift para Attack of the Vine. La consecuencia práctica principal es que daño, costes opcionales, pilas y variantes de Shift tienen ahora procesos explícitos y reutilizables.

Para una interacción compleja, consultad siempre el PDF oficial 2.2 y las aclaraciones oficiales aplicables.

## Fuentes

- *Disney Lorcana TCG Comprehensive Rules*, versión 2.2.0, efectiva el 9 de julio de 2026: `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`.
- *Disney Lorcana TCG Comprehensive Rules*, versión 2.1.0, efectiva el 30 de abril de 2026: `CRUpdate_2.1.0_EN.pdf`.
- *Disney Lorcana TCG Set Release Notes: Attack of the Vine!*: `Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf`. Fuente preliminar para el contraste, no sustituto de CR 2.2.
