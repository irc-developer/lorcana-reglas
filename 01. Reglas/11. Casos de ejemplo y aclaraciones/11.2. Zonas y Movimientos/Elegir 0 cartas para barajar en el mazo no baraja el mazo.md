## ❓ Duda

Si un efecto sigue el patrón:

> "Choose up to N cards from your discard and shuffle them into your deck."

¿elegir **0** cartas hace que el mazo se baraje igualmente?

Y, por comparación, ¿cambia algo el criterio reciente según el cual jugar una carta **gratis** cuenta como haber pagado **0** para habilidades como **Babyhead** o **Jessie**?

---

## ✅ Respuesta

**No.** Elegir **0** cartas es una elección legal si el texto dice **"up to N"**, pero eso **no implica por sí mismo que el mazo se baraje**.

La razón es que aquí hay dos ideas distintas:

- **"Up to N"** define cuántos objetos puedes elegir, y **0** está dentro de ese rango.
- **"Shuffle"** sigue siendo una acción concreta sobre el mazo. Si el conjunto elegido es vacío, no hay cartas elegidas que barajar **into your deck**, y la instrucción se resuelve haciendo todo lo posible con ese conjunto vacío.

Por tanto, bajo ese patrón de texto, elegir **0** significa:

- la elección es legal
- no se mueve ninguna carta del descarte al mazo
- **no se randomiza el mazo**, salvo que exista otra instrucción independiente del tipo **"Then shuffle your deck"** o equivalente

---

## 🔍 Por qué no es lo mismo que Babyhead o Jessie

La comparación con **Babyhead - Leader of Sid's Toys** y **Jessie - Lively Cowgirl** no cambia esta conclusión.

En esos casos, la habilidad pregunta **cuánta tinta pagaste** para jugar una carta. Si la jugaste gratis, el valor relevante es **0**, y **0 sí cumple** la condición **"2 o menos"**.

Eso funciona porque la habilidad está comprobando una **cantidad numérica efectivamente pagada**.

En cambio, **"choose up to N cards"** no está comprobando una cantidad ya pagada ni una magnitud del juego; solo está definiendo un **rango legal de elección**. Que **0** sea una elección legal no crea automáticamente un evento adicional de **barajar el mazo** si el texto no lo ordena de forma separada.

Dicho de otro modo:

- **"pay 2 or less"** = pregunta numérica; **0** satisface la condición
- **"choose up to N"** = permiso de selección; **0** hace legal la elección vacía, pero no convierte en realizada una acción física posterior que requiere un objeto sobre el que actuar

Así que sí: **Babyhead** y **Jessie** ven jugar gratis como **pagar 0**. Pero no: eso **no obliga** a concluir que elegir **0 cartas** equivalga a **barajar el mazo**.

---

## 🔄 Cómo se resuelve

1. El efecto empieza a resolverse.
2. Si el texto dice **"choose up to N"**, el jugador puede elegir entre **0** y **N** cartas legales.
3. Si elige **0**, el conjunto de cartas elegidas queda vacío.
4. Después se sigue el resto del texto en orden, haciendo todo lo posible.
5. Como no hay cartas elegidas que barajar **into your deck**, no entra ninguna carta en el mazo por esa instrucción.
6. Si el texto no contiene además una orden separada de **barajar el mazo**, el mazo no se randomiza.

---

## 🧪 Contraste útil

### Caso 1. No hay barajado independiente

Texto patrón:

> "Choose up to 3 cards from your discard and shuffle them into your deck."

Si eliges **0**, la elección es legal, pero no hay cartas que entren en el mazo y **no se baraja** el mazo.

### Caso 2. Sí hay barajado independiente

Texto patrón:

> "Choose up to 3 cards from your discard and put them into your deck. Then shuffle your deck."

Aquí, aunque elijas **0**, la segunda instrucción sigue existiendo como mandato autónomo. En ese caso, **sí** barajas el mazo porque el texto lo ordena expresamente.

---

## 📘 Referencias

### Wiki de Lorcana

- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.1. General (General)|Elecciones, opciones y dependencias entre instrucciones de un efecto]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)|Cómo seguir las instrucciones y resolver las habilidades pendientes]]
- [[01. Reglas/1. Principios generales/1.7. Game Actions, Timing, y Illegal Actions|Elecciones legales y corrección de acciones ilegales]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Cantar o jugar gratis cuenta como pagar 0 tinta|Cantar o jugar gratis cuenta como pagar 0 tinta]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Acción jugada debido a un efecto de otra carta|Acción jugada debido a un efecto de otra carta]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Buscar en el mazo y cuándo barajar|Buscar, mirar y cumplir una instrucción independiente de barajar]]

---

## 📝 Nota de alcance

Este caso documenta el **patrón de texto** “choose up to N cards ... and shuffle them into your deck”.

Si una carta concreta usa una redacción distinta, especialmente si incluye una segunda instrucción autónoma de **shuffle your deck**, la conclusión puede cambiar.

---

## 🏷️ Tags

#deck #discard #scope #resolution #alternate-cost
