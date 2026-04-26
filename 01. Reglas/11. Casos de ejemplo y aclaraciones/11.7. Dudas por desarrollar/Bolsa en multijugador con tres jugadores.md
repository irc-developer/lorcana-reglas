## ❓ Duda

En una partida multijugador de tres jugadores, si al mismo tiempo se disparan habilidades del jugador activo y de los otros dos jugadores, ¿cómo se resuelven exactamente desde la bolsa?

La duda concreta es si el jugador activo resuelve todas las suyas antes de que la bolsa pase al siguiente jugador en orden de turno, y si ese siguiente jugador hace lo mismo antes de pasar al tercero.

---

## ✅ Respuesta

Sí. En multijugador, las habilidades disparadas que ocurren al mismo tiempo se añaden a la bolsa simultáneamente, pero no se resuelven todas mezcladas.

Primero resuelve el jugador activo una de sus habilidades y, mientras siga teniendo habilidades propias en la bolsa, continúa resolviéndolas una a una. Cuando ya no le queden, la bolsa pasa al siguiente jugador en orden de turno, que hace exactamente lo mismo. Después pasa al tercer jugador.

La consecuencia práctica es esta:

- el jugador activo vacía su parte de la bolsa antes de que el siguiente jugador empiece a resolver la suya
- el segundo jugador hace lo mismo antes de que la bolsa pase al tercero
- si durante ese proceso un jugador añade nuevas habilidades propias a la bolsa, esas nuevas habilidades pueden entrar en su siguiente comprobación de bolsa
- si la habilidad nueva pertenece a otro jugador, espera a que llegue el turno de ese jugador para resolver desde la bolsa

En una mesa de tres jugadores, por tanto, no hay una resolución alterna tipo A-B-A-C. La bolsa avanza por bloques de control en orden de turno.

---

## 📘 Fundamento en reglas

- [[01. Reglas/7. Zonas (Zones)/7.7. Bolsa (Bag)#7.7.3.1. Añadir a la bolsa un efecto|7.7.3.1. Los triggers simultáneos se añaden a la bolsa simultáneamente]]
- [[01. Reglas/7. Zonas (Zones)/7.7. Bolsa (Bag)#7.7.4.2. El jugador activo escoge|7.7.4.2. El jugador activo empieza resolviendo una de las suyas]]
- [[01. Reglas/7. Zonas (Zones)/7.7. Bolsa (Bag)#7.7.4.3. Escoger siguiente habilidad|7.7.4.3. El mismo jugador sigue mientras aún tenga habilidades propias]]
- [[01. Reglas/7. Zonas (Zones)/7.7. Bolsa (Bag)#7.7.4.4. Pasar la bolsa (passing the bag)|7.7.4.4. La bolsa pasa al siguiente jugador en orden de turno]]
- [[01. Reglas/7. Zonas (Zones)/7.7. Bolsa (Bag)#7.7.4.5. Continúa la resolución|7.7.4.5. El proceso continúa por todos los jugadores]]
- [[01. Reglas/2. Juego (Gameplay)/2.1. General#2.1.3. Jugador inicial y jugador no inicial|2.1.3. En multijugador el orden sigue hacia la izquierda]]

---

## 🔄 Secuencia oficial

1. Ocurre un evento que dispara habilidades de los tres jugadores al mismo tiempo.
2. Todas esas habilidades se añaden a la bolsa simultáneamente.
3. La bolsa comprueba qué jugadores tienen habilidades pendientes.
4. Si el jugador activo tiene alguna, elige una suya y la resuelve por completo.
5. Tras la comprobación posterior, si ese mismo jugador aún tiene habilidades propias en la bolsa, sigue resolviendo las suyas.
6. Cuando ya no tenga más, la bolsa pasa al siguiente jugador en orden de turno.
7. Ese jugador resuelve sus habilidades siguiendo el mismo patrón, y después la bolsa pasa al tercer jugador si aún tiene habilidades pendientes.
8. Cuando ningún jugador tenga más habilidades en la bolsa, la partida continúa con el jugador activo.

---

## 🏷️ Tags

#multijugador #bag #triggered-abilities #turn-order #active-player