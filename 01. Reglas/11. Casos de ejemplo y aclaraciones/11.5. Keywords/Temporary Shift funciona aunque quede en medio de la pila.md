## ❓ Duda

Juego un personaje usando **Temporary Shift** y, durante ese mismo turno, hago otro **Shift** encima. La carta con Temporary Shift queda en medio de la pila.

Al final del turno, ¿la habilidad retardada se resuelve igualmente? ¿Qué carta vuelve a la mano y de qué personaje se retira el daño?

---

## ✅ Respuesta

**Sí. Temporary Shift se resuelve igualmente aunque su carta haya quedado en medio o en la parte inferior de una pila que continúa en juego.**

Al final del turno:

1. Se retira todo el daño del personaje que representa actualmente la pila, es decir, de la **carta superior actual**.
2. Vuelve a la mano **únicamente la carta que se jugó usando Temporary Shift**, aunque ya no sea la carta superior.
3. Las demás cartas permanecen en la zona de juego y continúan formando la pila restante.

El resultado solo cambia si la pila ya no sigue en juego. Por ejemplo, si fue desterrada antes del final del turno, la carta con Temporary Shift permanece en el descarte y no vuelve a la mano.

---

## 📘 Fundamento en reglas

- [[01. Reglas/8. Palabras clave (Keywords)/8.10. Cambio (Shift)#8.10.8.5. Temporary Shift|8.10.8.5. Temporary Shift]] crea una habilidad disparada retardada al usar ese coste alternativo. Al final del turno retira el daño y devuelve únicamente la carta jugada mediante Temporary Shift.
- El texto inglés de [[01.1.a Official English Reference – Unmodified/8. Keywords#8.10.8.5.|CR 2.2, 8.10.8.5]] dice **“return only that card”**: “that card” se refiere a la carta con Temporary Shift, no necesariamente a la carta superior de la pila.
- [[01. Reglas/8. Palabras clave (Keywords)/8.10. Cambio (Shift)#8.10.6. Daño|8.10.6. Daño]] establece que el personaje desplazado conserva el daño del personaje o las cartas sobre las que se coloca. Por eso el daño pertenece al personaje representado por la pila y se retira de su carta superior actual.
- [[01. Reglas/5. Cartas y tipos de carta (Cards and Card types)/5.1. Estados de las cartas (Card States)#5.1.1.7. En una pila (In a stack)|5.1.1.7. En una pila]] regula el movimiento ordinario de una pila cuando abandona el juego su carta superior. En este caso la carta superior no abandona el juego: el ruling específico de Temporary Shift retira la carta temporal desde su posición y deja en juego las demás.

La frase de CR 2.2 **“if this card is in play”** puede resultar ambigua al combinarla con la definición general de una carta situada debajo. Las *Attack of the Vine Set Release Notes* resuelven expresamente esa ambigüedad: basta con que la carta temporal siga formando parte de una pila que continúe en juego.

---

## 🔄 Secuencia oficial

1. Juegas un personaje mediante Temporary Shift sobre un personaje legal. En ese momento se crea la habilidad disparada retardada para el final del turno.
2. Antes de terminar el turno, juegas otro personaje mediante Shift encima de esa pila.
3. La carta con Temporary Shift queda debajo de la nueva carta superior, pero continúa formando parte de una pila en la zona de juego.
4. Al final del turno se resuelve la habilidad retardada.
5. Se retira todo el daño de la carta superior actual.
6. Se extrae de la pila únicamente la carta con Temporary Shift y se devuelve a la mano de su jugador.
7. Las demás cartas permanecen en juego en su mismo orden relativo.

---

## 📝 Fuente y estado

Ruling oficial de los diseñadores recogido en las [[Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf#page=7|Attack of the Vine Set Release Notes, página 7]]:

> “If it’s in the middle or on the bottom of a stack of cards in play, it still returns to your hand.”

Las mismas notas añaden el ejemplo exacto de hacer otro Shift encima: se devuelve la carta desde el medio de la pila y también se retira el daño del personaje situado arriba. La regla general de Temporary Shift está codificada en CR 2.2, 8.10.8.5; la aplicación expresa a una carta situada en medio o debajo procede de este ruling oficial.

Véase también [[CR 2.2 - comparación final con Attack of the Vine]].

---

## 🏷️ Tags

#shift #temporary-shift #stack #delayed-trigger #play-zone #timing
