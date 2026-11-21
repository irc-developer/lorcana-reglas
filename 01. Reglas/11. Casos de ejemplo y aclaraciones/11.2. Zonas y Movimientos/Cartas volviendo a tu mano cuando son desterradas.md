## ❓ Duda

Cuando una carta dice que “al ser desterrada” vuelve a tu mano (por ejemplo, [HeiHei - Persistent Presence](https://cards.lorcast.io/card/digital/large/crd_907f9d8972fd47b6903590bd53f1e662.avif?1709690747) o [Gale - Wind Spirit](https://cards.lorcast.io/card/digital/large/crd_a9888f3a8e1845588922ff69068e6f78.avif?1723917209)), ¿pasa primero por el descarte o vuelve directamente?  
Y si esa carta estaba debajo de otra en una pila (por Boost), ¿se considera desterrada para disparar esa habilidad?

---

## ✅ Respuesta

Pasa primero por el descarte y luego vuelve a la mano cuando se resuelve su habilidad.  
No es un cambio funcional nuevo: la redacción que especifica “desde el descarte” aclara una secuencia que ya seguía el flujo de zonas.

Si la carta estaba debajo de otra en una pila, no se considera en juego como carta independiente. Cuando la carta superior sale de la zona de juego, toda la pila se mueve a la misma zona; por tanto, la carta “under” no dispara por sí sola un “cuando este personaje sea desterrado” como si estuviera en juego independiente.

Esto también puede cumplir una condición que comprueba si una carta ha salido del descarte este turno. Por ejemplo, si [Will o' the Wisp - Forest Spirit](https://cards.lorcast.io/card/digital/large/crd_4d61ccc401a942719bfcafde3a132578.avif?1777687337) es desterrado en un desafío, su habilidad *Come On Out* se dispara. Si al resolverla eliges devolverlo a tu mano, Will o' the Wisp habrá salido del descarte. En consecuencia, [Anna - Soothing Sister](https://cards.lorcast.io/card/digital/large/crd_be89cf4d06b54426801f296b3cbf751d.avif?1770259425) obtiene *Shift* 0 {I} durante ese turno.

La habilidad de Anna no se dispara: *Shift* es una habilidad estática, y el regreso de Will o' the Wisp hace que se cumpla su condición. La habilidad de Will se resuelve dentro de la bolsa del desafío; podrás usar el *Shift* de Anna cuando el desafío termine si eres el jugador activo, sigues en ese turno y tienes otro personaje llamado Anna en juego.

---

## 📘 Referencias

- [[7.4. Juego (Play)|7.4.3. Cartas abandonando la zona de Juego]]
- [[7.6. Pila de descarte (Discard pile)|7.6.1. Definición de descarte]]
- [[5.1. Estados de las cartas (Card States)|5.1.1.5. Debajo (Under)]]
- [[5.1. Estados de las cartas (Card States)|5.1.1.7. En una pila (In a stack)]]
- [[1.8. Chequeo del estado del juego (Game State Check)|1.8.3. Evaluación cíclica]]: los disparos por el destierro se resuelven en la bolsa antes de continuar.
- [[4.6 Desafío (Challenge)]]: el efecto de Will o' the Wisp se resuelve durante la bolsa del desafío.
- [[8.10. Cambio (Shift)|8.10.1. Definición]]: *Shift* es una habilidad estática que permite jugar la carta pagando un coste alternativo.
- [CR 2.3.0, 4.6.7, p. 15](https://files.disneylorcana.com/CRUpdate_EN_Oct-2026.pdf#page=15): cierre normal del desafío. [CR 2.3.0, 4.6.9–4.6.9.2, pp. 16–18](https://files.disneylorcana.com/CRUpdate_EN_Oct-2026.pdf#page=16): si un participante sale del desafío, se resuelven los disparos pendientes antes de cerrarlo. El ejemplo B muestra una devolución a la mano como la de Will o' the Wisp.
- [CR 2.3.0, 8.10.1, p. 42](https://files.disneylorcana.com/CRUpdate_EN_Oct-2026.pdf#page=42).

---

## 🔄 Cómo se resuelve

1. **Evento de inicio**: ocurre el evento que destierra al personaje.
2. **Costes y requisitos (si aplica)**: no hay pago de coste adicional en este caso.
3. **Elecciones y objetivos**: no aplica objetivo adicional para el propio evento de destierro.
4. **Resolución**: la carta abandona zona de juego y entra en descarte; si su texto tiene trigger de retorno, queda preparado para bolsa.
5. **Disparos y bolsa**: la habilidad de retorno entra en la bolsa y, al resolverse, mueve la carta del descarte a la mano.

---

## 🏷️ Tags

#bag #banish #boost #discard #shift #static-ability #under
