## ❓ Duda

Con la mecánica Boost, cuando una carta queda debajo de otra en la zona de juego, ¿qué pasa con esas cartas “under” cuando la carta superior abandona la zona de juego?

---

## ✅ Respuesta

Todas las cartas de la pila se mueven a la misma zona que la carta superior.  
Mientras están en pila, las cartas de debajo no se consideran en juego como cartas independientes. Si la carta superior sale de la zona de juego, toda la pila la acompaña a la nueva zona.

---

## 📘 Fundamento en reglas

- [[5.1. Estados de las cartas (Card States)#5.1.1.5. Debajo (Under)|5.1.1.5. Debajo (Under)]]
- [[5.1. Estados de las cartas (Card States)#5.1.1.7. En una pila (In a stack)|5.1.1.7. En una pila (In a stack)]]
- [[5.1. Estados de las cartas (Card States)#5.1.1.10. Boca abajo (Facedown)|5.1.1.10. Boca abajo (Facedown)]]

---

## 🔄 Secuencia oficial

1. **Coste**: se resuelve el efecto que coloca cartas debajo (por ejemplo, Boost).
2. **Objetivos**: se define la carta superior que recibe cartas debajo.
3. **Resolución**: las cartas pasan a estado “debajo” formando una pila.
4. **Disparos**: se añaden a la bolsa los triggers que se generen por esa colocación.
5. **GSC**: si la carta superior abandona la zona de juego, toda la pila se mueve a la misma zona y se verifica estado del juego.

---

## 🏷️ Tags

#boost #facedown #stack #under #zonas