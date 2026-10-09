## ❓ Duda

En una partida multijugador, si una habilidad dice que "cada oponente" hace algo, ¿todos los oponentes realizan esa instrucción simultáneamente o la resuelven en orden de turno?

La duda práctica es si el resultado del primer oponente puede cambiar lo que hacen después los demás cuando todos están actuando como parte del mismo efecto.

---

## ✅ Respuesta

No se resuelve de forma simultánea física. En multijugador, cuando un mismo efecto exige que varios jugadores hagan algo, esos jugadores lo hacen uno por uno en orden de turno.

Si el texto dice "cada oponente" y el controlador del efecto es el jugador activo, normalmente el jugador activo no tiene ninguna parte que resolver en esa instrucción. En ese caso, empiezan a actuar los oponentes en orden de turno, comenzando por el jugador situado a la izquierda del activo y siguiendo alrededor de la mesa.

Eso significa que el resultado del primer oponente sí puede cambiar la información pública disponible para el siguiente. Lo que no ocurre es una resolución intermedia de bolsa o una comprobación del estado del juego entre uno y otro: todos siguen formando parte de la misma resolución del efecto.

En resumen:

- los oponentes no actúan a la vez
- actúan uno por uno en orden de turno
- las habilidades disparadas que nazcan durante esa secuencia esperan en la bolsa hasta que el efecto entero termine

---

### Efectos con varias partes, desde el 16/10/2026

Cada jugador afectado completa **la primera parte**, en orden de turno; después todos completan la segunda, y así sucesivamente. No se resuelve el efecto entero para un jugador antes de pasar al siguiente. No se intercalan bolsa ni chequeos de estado entre partes.

Por ejemplo, [[Thomas O'Malley - Savvy Vagabond, revelaciones y costes empatados|Thomas O’Malley]] hace que todos revelen antes de comparar el coste más alto. [CR 2.3, 6.7.6.1, p.37](https://files.disneylorcana.com/CRUpdate_EN_Oct-2026.pdf#page=37) y [notas de Hyperia City](https://www.disneylorcana.com/en-US/news/2026/10/hyperia-city-set-release-notes) aclaran ese orden.

---

## 📘 Referencias

- [[6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)|6.7.6. Si varios jugadores actúan, lo hacen en orden de turno dentro de la misma resolución]]
- [[9.2. Reglas adicionales de multijugador (Multiplayer Rules)|9.2.2. En multijugador se procede hacia la izquierda, un jugador cada vez]]
- [[2.1. General|2.1.3. El orden de turno en multijugador va hacia la izquierda]]
- [[6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)|6.7.4. Los triggers creados durante esa resolución esperan]]

---

## 🔄 Cómo se resuelve

1. Empieza a resolverse una habilidad o acción que dice que cada oponente haga algo.
2. Como más de un jugador debe actuar durante ese mismo efecto, se aplica el orden de turno multijugador.
3. El primer oponente en orden de turno realiza su parte de la instrucción actual.
4. Si durante esa parte se generan habilidades disparadas, se añaden a la bolsa pero no se resuelven todavía.
5. Después realiza su parte el siguiente oponente en orden de turno, con la información pública actualizada que exista en ese momento.
6. Cuando todos han completado esa parte, se pasa a la siguiente parte en orden de turno, si la hay. Solo al terminar todas las partes queda resuelto el efecto.
7. Solo entonces se hace la comprobación del estado del juego y pueden empezar a resolverse habilidades desde la bolsa.

---

## 🏷️ Tags

#turn-structure #resolution #timing
