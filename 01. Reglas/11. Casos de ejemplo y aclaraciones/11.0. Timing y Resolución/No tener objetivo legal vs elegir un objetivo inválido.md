## ❓ Duda

¿Qué diferencia hay entre que un efecto no tenga ningún objetivo legal y que sí exista alguno, pero el jugador intente elegir un objetivo inválido? ¿Se pierde el efecto, se deshace la carta o solo se corrige la elección?

---

## ✅ Respuesta

La diferencia práctica es esta:

- **Si no existe ningún objetivo legal** en el momento de hacer la elección, esa parte del efecto **se resuelve sin efecto**, siempre que esa elección pertenezca a la **resolución** del efecto.
- **Si sí existe al menos un objetivo legal**, pero el jugador elige uno que no cumple las restricciones, la elección es **ilegal** y se **retrocede solo hasta ese momento de la elección** para escoger de nuevo un objetivo válido.
- **Si la legalidad del objetivo era requisito para poder iniciar o completar la acción de turno**, entonces ya no estamos ante una simple elección fallida dentro de la resolución, sino ante una **acción ilegal** y corresponde deshacerla según 1.7.6 en la medida de lo posible.

En Lorcana esto importa mucho porque las elecciones de tipo **choose / chosen** se hacen **durante la resolución**, no al anunciar la carta o habilidad. Por eso, la pregunta correcta no es “¿hay una carta en mesa?”, sino “¿hay al menos una elección legal en este punto exacto de la resolución?”.

Además, **que un objetivo produzca poco o ningún efecto no lo vuelve inválido**. Si el texto permite elegirlo legalmente, sigue siendo un objetivo válido aunque el resultado práctico sea mover 0, retirar 0 o modificar algo que ya estaba en ese estado.

La frontera real, por tanto, no es solo “hay objetivo / no hay objetivo”, sino **en qué momento del procedimiento hacía falta que ese objetivo fuese legal**.

---

## 🔍 La diferencia real

| Situación | Qué significa | Qué pasa en reglas |
|---|---|---|
| **No hay objetivo legal durante la resolución** | Ningún objeto del juego cumple todas las restricciones del texto en el momento de elegir durante la resolución | Esa parte del efecto se resuelve sin efecto; si hay otras partes independientes, se hace todo lo posible |
| **Se elige un objetivo inválido** | Sí había al menos una opción legal, pero la elección concreta hecha por el jugador no lo era | Se deshace hasta el momento de la elección y se elige otra vez |
| **La acción exigía un objetivo legal para poder iniciarse o completarse** | La ilegalidad no está en una elección interna del efecto, sino en haber intentado una acción que no podía llevarse a cabo correctamente | La acción es ilegal y se deshace según 1.7.6, tanto como sea posible |
| **El objetivo es legal, pero el efecto hará 0** | El objeto cumple las restricciones, aunque el resultado material sea nulo o mínimo | La elección sigue siendo legal y el efecto se resuelve normalmente |

La clave no es si “hay algo” en mesa, sino si ese algo **cumple exactamente** los criterios del efecto: controlador correcto, tipo correcto, estado correcto, restricciones como Ward, Fuerza, daño previo, etc.

Y antes de aplicar 1.7.7 conviene hacer una pregunta previa: **¿estamos corrigiendo una elección tomada durante la resolución, o una acción que nunca pudo iniciarse legalmente así?**

---

## 🧪 Ejemplos formativos

### 1. No hay ningún objetivo legal

Una acción dice: “Destierra chosen character with 2 {S} or less.”

Si el único personaje rival tiene **3 {S}**, no existe ningún objetivo legal para esa elección. No se retrocede el hecho de haber jugado la acción; simplemente, al llegar a la elección, esa parte **no puede hacerse** y el efecto se resuelve sin efecto.

Lo mismo ocurre si el único personaje rival disponible tiene **Ward** y eres tú quien debe elegirlo: ese personaje existe en mesa, pero **no es una elección legal** para ti.

Aquí no se retrocede toda la carta porque el problema aparece en una **elección de resolución**, no en el hecho de haber jugado la carta.

### 2. Sí había objetivo legal, pero se eligió uno inválido

Una acción dice: “Deal 2 damage to chosen character. Draw a card.”

Hay dos personajes rivales en mesa:

- uno sin Ward
- uno con Ward

Si el jugador intenta elegir el personaje con Ward, la jugada no vuelve atrás por completo. Según la regla de corrección de elecciones ilegales, se **retrocede solo hasta el momento de esa elección** y el jugador debe escoger un objetivo legal, en este caso el personaje sin Ward.

La carta ya fue jugada; lo incorrecto fue únicamente la elección.

### 3. Hay objetivo legal aunque el efecto haga 0

Una acción dice: “Remove all damage from chosen character of yours. Draw a card for each damage removed this way.”

Si controlas un personaje sin daño, ese personaje **sigue siendo un objetivo legal** si el texto no exige “damaged character”. El efecto retirará **0** daño y luego robarás **0** cartas.

Esto no es “no tener objetivo”. Es **tener un objetivo legal con resultado nulo**.

### 4. Diferencia aplicada a un efecto secuencial

En [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Luisa Madrigal - I Can Take It, condición Then-if y GSC|Luisa Madrigal - I Can Take It, condición Then-if y GSC]], la segunda instrucción pide elegir un personaje rival.

- Si no existe ningún personaje rival elegible en ese momento, esa segunda instrucción no puede realizarse y Luisa conserva el daño.
- Si sí existe uno legal pero el jugador intenta elegir uno con Ward habiendo otro legal sin Ward, se corrige la elección y se sigue resolviendo desde ahí.

La diferencia no está en el texto de Luisa, sino en **si había o no había una elección legal disponible cuando llegó ese punto de la resolución**.

### 5. Cuándo sí sería una acción ilegal

Si una acción de turno exige desde su propio inicio un objetivo o destino legal para poder declararse correctamente, y ese requisito no existe, entonces no estamos ante un caso de “resolver sin efecto”, sino ante una **acción ilegal** en el sentido de [[01. Reglas/1. Principios generales/1.7. Game Actions, Timing, y Illegal Actions#1.7.6. Acción ilegal|1.7.6]].

En otras palabras:

- si el fallo aparece **al iniciar la acción**, se deshace la acción
- si el fallo aparece **al hacer una elección dentro de la resolución**, se aplica 1.7.7

Por eso, si solo hay una carta en mesa y no es legal, la respuesta correcta no es automáticamente “retrocede todo” ni automáticamente “resuelve sin efecto”. Primero hay que identificar **en qué paso del procedimiento se requería la legalidad**.

---

## 🧭 Cómo distinguirlo en mesa

1. Lee la restricción completa del efecto, no solo el tipo de carta que parece querer elegir.
2. Determina si la legalidad se exige para **iniciar la acción** o para **resolver una elección interna**.
3. Si era un requisito para iniciar o completar la acción y no existía, la acción es ilegal y se deshace tanto como sea posible.
4. Si la elección ocurre durante la resolución y **no existe ninguna opción legal**, esa parte se resuelve sin efecto.
5. Si sí había opción legal pero el jugador eligió una ilegal, se corrige desde ese punto.
6. Si la elección era legal aunque el efecto haga poco o nada, no hay error que corregir.

Esta distinción evita dos errores comunes:

- pensar que “hay una carta en mesa” equivale a “hay objetivo legal”
- pensar que “el efecto no hará casi nada” equivale a “el objetivo es inválido”

---

## 📘 Fundamento en reglas

- [[01. Reglas/1. Principios generales/1.7. Game Actions, Timing, y Illegal Actions#1.7.6. Acción ilegal|1.7.6. Acción ilegal]]: si un jugador intenta hacer una game action que no puede hacer o empieza una turn action que no puede llevar a cabo al completo, se deshace hasta donde sea razonable.
- [[01. Reglas/1. Principios generales/1.7. Game Actions, Timing, y Illegal Actions#1.7.3. Elecciones durante la resolución|1.7.3. Elecciones durante la resolución]]: las elecciones de tipo choose/chosen se hacen cuando el efecto se está resolviendo.
- [[01. Reglas/1. Principios generales/1.7. Game Actions, Timing, y Illegal Actions#1.7.7. Corrección de jugadas|1.7.7. Corrección de jugadas]]: si la elección fue ilegal, se deshace hasta ese momento; si no existe ninguna elección legal, el efecto se resuelve sin efecto y se hace todo lo posible con lo demás.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.1. General (General)#6.1.2. Las habilidades y efectos de una carta están formados por una o más frases separadas por puntos.|6.1.2. Resolver en orden y hacer todo lo posible]]: los efectos se siguen en orden y se resuelven tanto como sea posible.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.1. General (General)#6.1.3. Todas las elecciones (choices) se realizan durante la resolución del efecto.|6.1.3. Las elecciones se hacen al resolver]]: confirma que la legalidad de la elección se comprueba en ese punto de la resolución.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)#6.7.2.4. Cuarto paso - resolución del texto|6.7.2.4. Resolución del texto]]: el jugador cumple las instrucciones y toma las decisiones requeridas en el orden escrito, haciendo todo lo posible.

---

## 🔗 Véase también

- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Ohana Means Family y Brawl sin objetivo válido o con objetivo inválido|Ohana Means Family y Brawl sin objetivo válido o con objetivo inválido]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Resolución parcial sin objetivo válido|Resolución parcial sin objetivo válido]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/El uso de Then|El uso de Then]]

---

## 🏷️ Tags

#targeting #legal-target #illegal-choice #resolution #timing #ward #choose #chosen