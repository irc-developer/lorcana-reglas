## ❓ Duda

¿Por qué Rapunzel pierde su protección incluso si Resist reduce el daño a 0?

---

## ✅ Respuesta

La protección de Rapunzel se desactiva cuando recibe daño, independientemente de cuánto daño sea finalmente aplicado. La estática de resist se aplica primero y si, el daño se reduce a 0, no se pierde el escudo. La secuencia es:

1. Declaración del daño
2. Aplicación de efectos de modificación (Resist primero)
3. Desactivación de protecciones si el daño ≥ 1 (antes de aplicarse)

---

## 📘 Fundamento en reglas

- [[6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)#6.7.2. Resolución|6.7.2. Resolución]]
- [[7.7. Bolsa (Bag)#7.7.4. Orden|7.7.4. Orden]]
- ---

---

## 🔄 Secuencia oficial

1. **Coste**: determinar el coste de la acción o habilidad que inicia la jugada.
2. **Objetivos**: fijar objetivos legales según el texto.
3. **Resolución**: resolver el texto en orden.
4. **Disparos**: añadir a la bolsa los triggers generados y resolver por prioridad.
5. **GSC**: realizar chequeo del estado del juego tras cada resolución.

---

## 🏷️ Tags

#rapunzel #replacement-effects #resist #static-abilities #timing