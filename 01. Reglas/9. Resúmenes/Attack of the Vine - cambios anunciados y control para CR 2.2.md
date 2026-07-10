# Attack of the Vine: cambios anunciados y control para CR 2.2

*Documento de trabajo creado el 10/07/26*

> [!important] Estado del documento
> Este artículo resume las *Set Release Notes: Attack of the Vine!* y prepara su comparación con la futura versión 2.2 de las Comprehensive Rules. La referencia normativa integrada actualmente en el repositorio sigue siendo la **CR 2.1**. Por tanto, lo descrito aquí como «anunciado para 2.2» no debe incorporarse todavía a los archivos de reglas como si se hubiera verificado su redacción definitiva.

## Fuente, alcance y criterio

La fuente analizada es el [[Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf|PDF oficial Attack of the Vine Set Release Notes]], de 30 páginas. Las propias notas indican que acompañan a la versión 2.2 de las Comprehensive Rules y enumeran cambios por número de regla, aunque el texto completo de esa revisión aún no está disponible en este repositorio.

La comparación futura debe hacerse contra la referencia inglesa vigente de la CR 2.1:

- [[01.1.a Official English Reference – Unmodified/1. Concepts|1. Concepts]].
- [[01.1.a Official English Reference – Unmodified/4. Turn Actions|4. Turn Actions]].
- [[01.1.a Official English Reference – Unmodified/5. Cards and Card Types|5. Cards and Card Types]].
- [[01.1.a Official English Reference – Unmodified/6. Abilities, effects, and resolving|6. Abilities, effects, and resolving]].
- [[01.1.a Official English Reference – Unmodified/8. Keywords|8. Keywords]].
- [[01.1.a Official English Reference – Unmodified/99. Glossary|99. Glossary]].

Para evitar falsos positivos, este artículo distingue entre:

1. **mecánicas nuevas**, que necesitan reglas nuevas o ampliadas;
2. **cambios funcionales o aclaraciones con impacto práctico**;
3. **reorganizaciones o cambios de terminología sin cambio funcional**;
4. **ajustes editoriales y ejemplos**;
5. **rulings de cartas**, que explican interacciones pero no equivalen por sí solos a una modificación general de las reglas.

---

## Resumen ejecutivo

Los puntos que más atención requerirán al integrar la CR 2.2 son estos:

- Se formaliza el tratamiento de los **personajes con dos nombres**: cuentan por cada nombre individual y por el nombre conjunto, pero siguen siendo una sola carta y un solo personaje.
- Aparecen nuevas variantes de **Shift**: **Duo Shift**, **Combo Shift**, **Temporary Shift** y variantes que permiten desplazar sobre una clasificación o incluso sobre una carta que no sea personaje, como **Potato Shift**.
- Shift deja de estar limitado en todos los casos a «un personaje sobre otro personaje». Las reglas deben cubrir pilas formadas desde dos personajes y pilas cuyo soporte original sea una carta que no sea personaje.
- Cuando se desplaza sobre dos personajes con estados incompatibles, prevalece el estado más restrictivo: si uno se está secando, la carta superior se está secando; si uno está agotado, la carta superior entra agotada.
- Se añaden reglas para cartas cuyas habilidades modifican la **construcción del mazo**, como Christopher Robin – Hunny Sage.
- Se centraliza y detalla el **cálculo del daño**, sin que las notas anuncien un cambio en su funcionamiento.
- Las antiguas *conditional static abilities* pasan a llamarse **conditional dependent effects** y se trasladan de 6.4 a 6.1 para aplicarse a cualquier tipo de habilidad. Las notas declaran que esto no cambia interacciones.
- Se precisan el momento de pago de tinta al resolver efectos, la combinación de «may» con un coste, los disparos al jugar una carta sobre otra, el estado de una pila al cambiar de zona y qué sucede si un personaje se endereza durante un desafío.
- Se añaden las clasificaciones **Boss**, **Red Panda**, **Team** y **Vineling**; además, objetos y localizaciones podrán tener clasificaciones adicionales.

---

## 1. Personajes con dos nombres

Attack of the Vine amplía considerablemente el número de personajes con dos nombres y presenta **Team** como nueva clasificación asociada a varios de ellos.

### Reglas anunciadas

Tomando *Sulley & Boo – Scare Buddies* como ejemplo:

- Un personaje con dos nombres cuenta como si tuviera **tres nombres relevantes**. Sulley & Boo cuenta como **Sulley**, como **Boo** y como **Sulley & Boo**.
- Si un efecto pide nombrar una carta y se nombra «Sulley», ese efecto alcanza tanto a los personajes llamados solo Sulley como a los personajes con Sulley antes o después del `&`.
- Si se nombra «Sulley & Boo», el efecto solo alcanza a personajes con ese nombre conjunto; no alcanza a un Sulley individual ni a un Boo individual.
- Tener varios nombres no multiplica la entidad: la carta sigue siendo **un solo personaje**.
- La versión de la carta no forma parte de su nombre a estos efectos. Esto se confirma con *One and Only*: dos versiones distintas de Winnie the Pooh comparten el nombre «Winnie the Pooh».

### Consecuencias para Shift

- Un personaje dual satisface una condición de Shift normal que busque cualquiera de sus nombres.
- Un único personaje dual no satisface por sí solo un **Duo Shift**, porque Duo Shift exige dos personajes distintos, uno para cada nombre.
- A efectos de un Duo Shift, el personaje dual puede aportar uno de los nombres requeridos, pero sigue contando como una sola de las dos cartas necesarias.

### Qué comprobar en CR 2.2

- [ ] Dónde se define formalmente el nombre de una carta dual.
- [ ] Si se modifica la definición de *full name* o el glosario.
- [ ] Cómo se expresa la comparación entre nombre individual, nombre conjunto y versión.
- [ ] Si la regla se aplica a cualquier tipo de carta con dos nombres o solo a personajes.
- [ ] Cómo se coordina esta definición con las nuevas variantes de Shift.

---

## 2. Habilidades que modifican la construcción del mazo

*Christopher Robin – Hunny Sage* introduce **Gather the Party**, que permite incluir otros personajes Hunny en el mazo independientemente de su tipo de tinta.

La excepción tiene límites importantes:

- Solo alcanza a **otros personajes** con la clasificación Hunny.
- No permite incluir cualquier carta Hunny si esa carta no es un personaje.
- Christopher Robin debe ser legal en el mazo antes de que su habilidad pueda modificar la construcción.
- Como Christopher Robin es Amethyst/Sapphire, solo puede incluirse en un mazo compatible con esos tipos de tinta. Su propia habilidad no puede utilizarse para introducirlo en un mazo de otros tipos.
- Tener varias copias de Christopher Robin no cambia esa conclusión.

Este comportamiento explica la nueva regla anunciada **1.10.1.3**, destinada a cartas cuyas habilidades ajustan la construcción del mazo.

### Qué comprobar en CR 2.2

- [ ] Texto exacto de 1.10.1.3 y momento en que se aplican las habilidades de construcción.
- [ ] Si la carta que genera la excepción debe cumplir primero todas las restricciones ordinarias.
- [ ] Cómo interactúan varias habilidades de construcción y qué ocurre si una depende de la presencia de otra carta.
- [ ] Si las reglas de formato o la lista de cartas prohibidas prevalecen expresamente sobre estas habilidades.

---

## 3. Nuevas variantes de Shift

### 3.1. Duo Shift

Duo Shift permite jugar una carta sobre **dos personajes**, uno por cada nombre indicado. Para *Mickey Mouse & Minnie Mouse – Adventuring Duo* se necesita un Mickey Mouse y, por separado, una Minnie Mouse.

- La carta con Duo Shift se coloca arriba y las dos cartas desplazadas quedan debajo en el orden que el jugador elija.
- Un solo Mickey Mouse & Minnie Mouse no basta: aunque tenga ambos nombres, sigue siendo un personaje.
- Morph – Little Imitator puede sustituir a uno de los dos personajes requeridos, pero no puede contar como los dos.
- Si uno de los dos personajes se está secando, la carta superior se está secando.
- Si uno de los dos personajes está agotado, la carta superior entra agotada.

### 3.2. Combo Shift

Combo Shift combina Shift normal y Duo Shift. La carta puede jugarse:

- sobre un personaje con cualquiera de los dos nombres; o
- sobre dos personajes, uno con cada nombre.

Si se usan dos personajes, se aplican las mismas reglas de orden de la pila y de combinación de estados que con Duo Shift.

### 3.3. Temporary Shift

Temporary Shift permite desplazar una carta de forma temporal y crea una instrucción para el final del turno:

- al final del turno, se retira todo el daño del personaje representado por la pila;
- solo la carta con Temporary Shift vuelve a la mano;
- el retorno solo ocurre si esa carta sigue formando parte de una pila en la zona de juego;
- si la pila fue desterrada, la carta permanece en el descarte;
- la carta vuelve a la mano incluso si, tras otro Shift, ha quedado en medio o en la parte inferior de la pila;
- aunque la carta temporal ya no esté arriba, se retira el daño de la carta superior que representa al personaje actual.

Las notas también mencionan **Temporary Red Panda Shift**: funciona de la misma forma, pero permite desplazar sobre un personaje con la clasificación Red Panda en lugar de exigir el mismo nombre.

### 3.4. Potato Shift y Shift sobre cartas que no son personajes

*Posey – Vampire Potato* puede desplazarse sobre un objeto llamado Potato. Es la primera mecánica descrita que permite desplazar un personaje sobre una carta que no es personaje.

- Si el Potato estaba en juego al comienzo del turno, Posey se considera seca y puede hacer las acciones normales de un personaje.
- Si el Potato se jugó ese mismo turno, Posey se está secando y no puede irse de aventura, desafiar, cantar ni realizar otras acciones que exijan estar seca.
- Morph – Little Imitator es una elección legal para Potato Shift por su propia habilidad, aunque Morph no sea un objeto ni se llame Potato.

### 3.5. Morph y todas las variantes de Shift

*Morph – Little Imitator* permite que cualquier personaje con una habilidad Shift se desplace sobre él, incluidas todas sus variantes. Morph elimina la exigencia de nombre, clasificación o tipo de carta para ser una elección legal, pero no cambia el **número de cartas** requerido por la variante.

### Qué comprobar en CR 2.2

- [ ] Redacción completa de Duo Shift, Combo Shift, Temporary Shift, Temporary `[Classification]` Shift y Potato Shift.
- [ ] Si Potato Shift se regula como variante específica o mediante una regla general que admite Shift sobre no-personajes.
- [ ] Cómo se formula la herencia de seco/secándose y preparado/agotado al usar dos cartas.
- [ ] Si existen otros estados incompatibles que deban combinarse.
- [ ] Cómo se ordenan las dos cartas inferiores y si ese orden puede tener relevancia posterior.
- [ ] Cómo se identifica una carta Temporary Shift situada en medio de una pila al final del turno.
- [ ] Qué evento exacto devuelve la carta temporal y retira el daño.
- [ ] Cómo se trata una pila cuyo soporte era un objeto cuando cambia de zona.
- [ ] Cómo se codifica la combinación de dos o más variantes en una sola habilidad, anunciada para 8.10.9.

---

## 4. Cambios de reglas anunciados para CR 2.2

Esta es la lista de control principal. La columna «impacto esperado» clasifica el anuncio de las release notes; deberá confirmarse al comparar los dos documentos completos.

| Regla | Cambio anunciado | Impacto esperado / punto de comparación |
| --- | --- | --- |
| 1.10.1.3 | Añade reglas para habilidades que ajustan la construcción del mazo. | Funcional. Comparar con los límites de Constructed de 1.10.1.1 y con Gather the Party. |
| 4.3.4.2 | Los disparos procedentes de la carta que queda debajo al jugar otra encima se tratan en la misma ventana que los disparos *on-play*. | Aclaración de timing con impacto práctico. Confirmar qué fuentes pueden dispararse y cuándo entran en la bolsa. |
| 4.3.6 | Aclara el ejemplo de reducciones de pago: la reducción sigue consumiéndose/aplicándose aunque el personaje se juegue gratis. | El principio ya figura en 2.1; parece aclaración del ejemplo, no cambio funcional. |
| 4.6.4.4 | Explica qué sucede si un personaje de un desafío se endereza durante ese desafío. | Aclaración funcional: enderezarlo no lo retira del desafío. Solo abandonar la zona de juego lo hace antes de completarse. |
| 5.1.1.7 | Las cartas bajo la superior adquieren los estados de la carta superior cuando esta cambia de zona. | Funcional para pilas, especialmente cartas boca abajo que pasan al descarte y se vuelven visibles. |
| 5.3.3.2 | Añade Boss, Red Panda, Team y Vineling. | Actualización de clasificaciones de personaje. |
| 5.5.3 | Un objeto puede tener clasificaciones adicionales. | Necesario para cartas como Potato y para distinguir tipo de carta de otras clasificaciones. |
| 5.6.3 | Una localización puede tener clasificaciones adicionales. | Ampliación paralela a la de objetos. |
| 6.1.4.1 | Si un efecto combina un coste con «may» y el jugador no quiere o no puede pagarlo, se trata como elegir «no». | Funcional. Ninguna parte del efecto opcional ocurre y no se hacen sus elecciones. |
| 6.7.2 | Define el momento exacto en que se paga tinta durante los pasos de resolución de un efecto. | Cambio estructural relevante; comparar toda la secuencia de resolución, no solo una frase. |
| 6.7.2.1 | Define las elecciones que se hacen al comprobar una condición secundaria con «if». | Aclaración de elecciones y condiciones; comprobar su relación con 6.2.4. |
| 8.4.1 | Precisa la definición de Boost. | Las notas declaran que su funcionamiento no cambia. |
| 8.8.2 | Ajusta Resist a la terminología correcta de las reglas de daño. | Terminológico; comprobar si conserva que reducir a 0 significa que no se infligió daño. |
| 8.10.4.1 | Regula un personaje desplazado sobre una carta que no es personaje. | Funcional y necesario para Potato Shift. |
| 8.10.4.2 | Regula un personaje desplazado sobre dos personajes con estados incompatibles. | Funcional y necesario para Duo/Combo Shift. |
| 8.10.9 | Regula una habilidad que combina dos o más variantes de Shift. | Funcional; comprobar cómo se acumulan requisitos y excepciones. |

### Lista de verificación de integración

- [ ] Obtener el PDF oficial completo de CR 2.2 y conservarlo sin modificar.
- [ ] Extraer su texto preservando símbolos, numeración y ejemplos.
- [ ] Comparar CR 2.1 y CR 2.2 por secciones completas, no solo por números aislados.
- [ ] Confirmar los dieciséis cambios de la tabla anterior.
- [ ] Buscar cambios no mencionados en las release notes.
- [ ] Revisar si la renumeración desplaza enlaces internos existentes.
- [ ] Actualizar primero la referencia inglesa sin modificar y después la adaptación castellana.
- [ ] Separar en el resumen final los cambios funcionales, aclaraciones, ejemplos y correcciones editoriales.
- [ ] Verificar si cada ruling de cartas de este artículo queda codificado por una regla general, por un ejemplo o únicamente por las release notes.

---

## 5. Daño: centralización y terminología

Las notas anuncian una nueva sección que define de forma unificada el cálculo del daño tanto en desafíos como durante la resolución de efectos. También se precisa cuándo una fuente **inflige** daño y cuándo un personaje o una localización **recibe** daño.

Ravensburger indica expresamente que **no cambia la forma de calcular el daño**: el objetivo es reunir en un solo lugar reglas antes dispersas y añadir ejemplos.

El ejemplo de *Piercing Attack* confirma la secuencia:

1. Se parte del daño base del efecto: 2.
2. Se aplican los modificadores que puedan aplicarse.
3. Resist +2 normalmente reduciría ese daño a 0.
4. Como Piercing Attack dice que ese daño no puede reducirse mediante Resist, el modificador no se aplica.
5. El daño final infligido es 2 y se colocan 2 contadores de daño.

### Qué comprobar en CR 2.2

- [ ] Ubicación y numeración de la nueva sección de cálculo de daño.
- [ ] Cambios de referencias en 4.6.6.1, 4.6.6.2 y 8.8.2.
- [ ] Diferencia formal entre *deals damage*, *takes damage* y colocar contadores de daño.
- [ ] Orden completo de base, modificadores, prevención/reemplazo, daño final y contadores.
- [ ] Que las diferencias de redacción no se documenten por error como cambios funcionales.

---

## 6. Conditional dependent effects

Las reglas 2.1 contienen las *conditional static abilities* dentro de 6.4. Las release notes explican que esas definiciones pretendían servir para **todos los tipos de habilidades**, no solo para habilidades estáticas.

Para corregir el alcance:

- el término pasa de **conditional static abilities** a **conditional dependent effects**;
- las reglas correspondientes se trasladan de **6.4 a 6.1**;
- la redacción se adapta para no limitar el concepto a habilidades estáticas.

Las notas afirman que esta reorganización **no cambia ninguna interacción entre cartas**. Al integrar 2.2 habrá que tratarla como generalización terminológica y estructural, salvo que el texto completo revele alguna diferencia material no anunciada.

### Qué comprobar en CR 2.2

- [ ] Nuevos subapartados dentro de 6.1 y reglas eliminadas o renumeradas en 6.4.
- [ ] Nueva entrada de glosario y retirada de *conditional static ability*.
- [ ] Actualización de referencias cruzadas y ejemplos.
- [ ] Que los patrones con `if` y `unless` conservan el mismo resultado práctico.

---

## 7. Ajustes de calidad de vida anunciados

Estos cambios se presentan como ajustes de lenguaje, coherencia, referencias o ejemplos. No deben marcarse como cambios funcionales sin comprobar el texto completo.

| Regla | Ajuste anunciado |
| --- | --- |
| 4.6.6.1 | Actualiza referencias a las nuevas reglas de daño. |
| 4.6.6.2 | Actualiza referencias a las nuevas reglas de daño. |
| 5.1.3 | Corrige la referencia numérica del ejemplo. |
| 6.1.6 | Amplía el ejemplo para incluir tanto «another» como «other». |
| 6.1.10 | Añade un ejemplo nuevo. |
| 6.7.2.2 | Ajusta la redacción para coincidir con secciones relacionadas. |
| 8.10 | Sustituye varias apariciones de «character» por «card». |
| 8.10.8 | Añade las nuevas variantes de Shift a la sección. |
| 8.10.8.1 | Añade `[Classification]` a la definición. |
| 8.10.8.2 | Añade Universal a la definición. |
| 8.12.1 | Ajusta Sing Together para que coincida con el lenguaje usado para las canciones. |

> [!note] Recuento
> Las release notes presentan once viñetas de calidad de vida. Algunas contienen varias sustituciones o altas de variantes, por lo que el número real de líneas modificadas en la CR 2.2 será mayor.

---

## 8. Rulings de cartas con enseñanza general

Las release notes contienen **26 preguntas y respuestas**. A continuación se conserva toda su información normativa relevante, agrupada por principio para facilitar su cruce con la CR 2.2.

### 8.1. Orden de efectos, «may», costes y condiciones

#### Woody – Helping a Friend

Si hay otro Toy en juego, «choose one» se sustituye por «choose both», pero no permite cambiar el orden impreso. Primero se devuelve a la mano una carta de personaje de coste 2 o menos desde el descarte y después se puede jugar gratis un personaje de coste 2 o menos. La carta devuelta puede, por tanto, estar disponible para el segundo efecto.

#### Celia Mae – Friendly Receptionist

Si el jugador no puede o no quiere pagar el coste de 1 tinta incluido en el efecto opcional, se trata como haber elegido «no» al `may`. No ocurre ninguna parte del efecto y no se elige personaje; por tanto, nadie queda bajo la restricción de no poder irse de aventura o desafiar.

#### Prophetic Vision

La pérdida y ganancia de lore solo ocurre en la rama en la que no se juega una acción revelada. Sucede si la carta revelada no es una acción o si es una acción y el jugador decide no jugarla. Si se juega la acción gratis, no se aplica la rama de lore.

#### Look What You've Done

La habilidad para jugar la carta desde el descarte solo se dispara cuando la carta es **descartada durante tu turno**. Jugarla normalmente, resolver sus 2 puntos de daño y colocarla después en el descarte como parte del proceso de una acción no equivale a descartarla y no permite volver a jugarla.

### 8.2. Obligaciones y acciones todavía permitidas

#### Woody – Town Sheriff

Un personaje afectado por «can't challenge and must quest if able» todavía puede cantar canciones o pagar costes de agotamiento. La obligación significa que su jugador no puede terminar el turno sin haberlo enviado de aventura si, llegado ese momento, el personaje está preparado y puede hacerlo.

### 8.3. Timing de aventura y desafío

#### Pocahontas & Meeko – Adventurous Friends

En una aventura, primero se gana el lore. Los disparos causados por que el personaje se vaya de aventura se resuelven después. Por ello, Welcome Return devuelve y puede jugar un personaje después de ganar el lore de la aventura.

#### Boo – Energetic Child

El desafío tiene declaración y daño. Kid-Tastrophe! se dispara al completarse la declaración del desafío y se resuelve desde la bolsa antes del paso de daño. Si destierra al personaje desafiado, no se inflige daño en ese desafío.

#### Ming Lee – Giant Red Panda

Enderezar a un personaje durante el desafío no lo retira de él. Una vez declarados el desafiante y el desafiado, solo abandonar la zona de juego antes de que termine el proceso los retira del desafío.

### 8.4. Pilas, cambios de zona y cartas bajo la superior

#### Sulley & Boo – Scare Buddies

Cuando la pila es desterrada, todas las cartas bajo Sulley & Boo van al descarte y pasan a estar boca arriba. Al resolverse The Power of Friendship, el efecto puede comprobar cuáles de esas cartas son personajes y jugarlas gratis, incluidas las que estaban boca abajo mientras se encontraban bajo la carta superior.

Si Combo Shift usa a la vez un personaje seco y otro que se está secando, Sulley & Boo se está secando. Si usa uno preparado y otro agotado, Sulley & Boo queda agotado.

#### Mickey Mouse & Minnie Mouse – Adventuring Duo

Un personaje dual no satisface en solitario la exigencia de dos personajes de Duo Shift. Al usar dos personajes, si uno se está secando el resultado se está secando, y si uno está agotado el resultado queda agotado.

#### Dash Parr & Violet Parr – Super Siblings

Combo Shift aplica la misma combinación de estados: secándose prevalece sobre seco y agotado prevalece sobre preparado.

### 8.5. «Other», «another» y autorreferencia

#### Winnie the Pooh – Hunny Archmage

Dos copias se reconocen mutuamente como «other Hunny characters». `Other` excluye al propio objeto que aplica el efecto, no a todas las cartas con el mismo nombre.

#### Roo – Hunny Rogue

Dos copias se reconocen mutuamente como «another Hunny character». `Another` significa otro personaje distinto de ese objeto, aunque comparta exactamente el mismo nombre.

#### Heihei – Created by the Vine

Heihei reconoce su propia clasificación Floodborn. Cuando se va de aventura, Botanical Remedy se dispara porque es uno de tus personajes Floodborn; la habilidad no exige «otro» Floodborn.

### 8.6. Entrada en juego agotado

#### Merida – Wisp Conjurer

Focused Energy no hace que Merida entre preparada y se agote después. Igual que ocurre con Bodyguard, la elección se hace al ponerla en juego y Merida entra ya agotada; si se elige esa opción, se roba una carta.

### 8.7. Tipos de tinta y valores distintos

#### Winnie the Pooh & Piglet – Hunny Mages

Magical Mix cuenta **tipos de tinta diferentes**, no el número de símbolos impresos ni el número de cartas. El propio personaje aporta Amethyst y Sapphire. Si el resto de cartas solo repite Amethyst, hay dos tipos distintos y el personaje obtiene +2 lore.

#### With a Few Good Friends

El tipo de tinta se identifica mediante los símbolos situados en la línea de clasificaciones. Una carta puede tener uno o dos símbolos y posee cada uno de los tipos indicados. El efecto cuenta tipos diferentes entre los personajes en juego.

### 8.8. Nombre, versión y cantidades máximas

#### One and Only

Al comparar nombres se usa el nombre principal, no la versión. *Winnie the Pooh – Hunny Wizard* y *Winnie the Pooh – Hunny Archmage* se llaman ambos Winnie the Pooh; si se elige uno, el otro puede ser desterrado por compartir nombre.

#### Narrow Escape

«Up to 2 ... with cost 2 or less each» impone el límite de coste a cada carta por separado. Se pueden elegir dos cartas de coste 2; no existe un presupuesto conjunto de coste 2.

### 8.9. Resist y daño no reducible

#### Piercing Attack / Omnidroid – Ultimate Iteration

Piercing Attack parte de 2 de daño. Resist +2 sería un modificador aplicable, pero la propia acción prohíbe que ese daño se reduzca mediante Resist. El resultado final es 2 de daño y se colocan 2 contadores sobre Omnidroid.

### 8.10. Rulings específicos de las variantes de Shift

#### Morph – Little Imitator

- Es una elección legal para cualquier variante de Shift, aunque no tenga el nombre, clasificación o tipo normalmente requerido.
- No satisface por sí solo Duo Shift, porque Duo Shift sigue exigiendo dos personajes.
- Puede ser uno de esos dos personajes junto con otra carta legal.

#### Posey – Vampire Potato / Morph – Little Imitator

Posey puede usar Potato Shift sobre Morph. Advanced Mimicry convierte a Morph en elección legal aunque no sea un objeto llamado Potato.

#### Christopher Robin – Hunny Sage

Ni una ni varias copias pueden incluirse en un mazo incompatible con Amethyst/Sapphire. Gather the Party solo funciona después de que Christopher Robin sea legalmente parte del mazo y solo exceptúa a los otros personajes Hunny.

---

## 9. Matriz para el cruce futuro con CR 2.2

Cuando se publique la nueva revisión, cada bloque debe acabar con uno de estos estados:

- **Confirmado literalmente**: la CR contiene la regla anunciada con el mismo alcance.
- **Confirmado con redacción distinta**: el resultado coincide, pero hay que documentar matices de lenguaje o numeración.
- **Parcialmente codificado**: la CR recoge el principio general, pero el ruling concreto solo aparece en las release notes.
- **Solo ejemplo o aclaración**: no existe una regla nueva; se añadió un ejemplo o una referencia.
- **No localizado**: el anuncio no aparece donde se esperaba y requiere búsqueda global o verificación de versión.
- **Cambio adicional**: la comparación completa descubre una modificación que las release notes no enumeraban.

| Área | Punto de control | Estado inicial |
| --- | --- | --- |
| Nombres duales | Nombres individuales, nombre conjunto, versión y condición de un solo personaje. | Pendiente de CR 2.2 |
| Construcción | 1.10.1.3 y legalidad previa de la fuente de la excepción. | Pendiente de CR 2.2 |
| Jugar cartas | 4.3.4.2 y disparos desde cartas que quedan debajo. | Pendiente de CR 2.2 |
| Desafíos | 4.6.4.4 y efecto de enderezar durante el desafío. | Pendiente de CR 2.2 |
| Pilas | 5.1.1.7 y estados adquiridos al cambiar de zona. | Pendiente de CR 2.2 |
| Clasificaciones | Boss, Red Panda, Team, Vineling; clasificaciones de objetos y localizaciones. | Pendiente de CR 2.2 |
| Resolución | Coste + may, pago de tinta y elecciones de condiciones secundarias. | Pendiente de CR 2.2 |
| Daño | Sección centralizada, terminología y referencias. | Pendiente de CR 2.2 |
| Efectos condicionales | Traslado 6.4 → 6.1 y nuevo término. | Pendiente de CR 2.2 |
| Shift | No-personajes, dos cartas, estados incompatibles y variantes combinadas. | Pendiente de CR 2.2 |
| Keywords | Boost, Resist y Sing Together. | Pendiente de CR 2.2 |
| Rulings | Cobertura de las 26 respuestas específicas del set. | Pendiente de CR 2.2 |

---

## Conclusión

Attack of the Vine no se limita a añadir cartas nuevas. El set obliga a generalizar la arquitectura de Shift, formalizar los nombres duales y admitir pilas construidas desde más de una carta o desde cartas que no son personajes. Además, la CR 2.2 deberá precisar varias ventanas de timing y resolución que ya tenían una respuesta práctica, pero no una redacción suficientemente explícita en 2.1.

Hasta disponer del documento completo, la conclusión prudente es doble:

1. los rulings del PDF sirven como guía oficial para las cartas y mecánicas de Attack of the Vine;
2. la numeración y el alcance definitivo de las reglas generales deben quedar marcados como pendientes de verificación contra la CR 2.2.
