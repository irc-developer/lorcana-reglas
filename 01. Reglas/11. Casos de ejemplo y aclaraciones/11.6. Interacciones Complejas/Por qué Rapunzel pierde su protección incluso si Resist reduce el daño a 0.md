## ❓ Duda

¿Por qué Rapunzel pierde su protección incluso si Resist reduce el daño a 0?

---

## ✅ Respuesta

La protección de Rapunzel **no** se desactiva si Resist reduce el daño final a 0.

Primero se calcula el daño aplicando los modificadores correspondientes, incluido Resist. Solo si el daño final es al menos 1 se considera que Rapunzel ha recibido daño a estos efectos. Si Resist lo reduce a 0, [[01. Reglas/8. Palabras clave (Keywords)/8.8. Resistir (Resist)|8.8.2]] aclara que no se considera que se haya infligido daño alguno, así que la protección no se consume.

La secuencia correcta es:

1. Declaración del daño
2. Aplicación de efectos de modificación (Resist primero)
3. Solo si el daño final es 1 o más, la protección puede consumirse por haber daño realmente infligido

---

## 📘 Fundamento en reglas

- [[6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)#6.7.2. Resolución|6.7.2. Resolución]]
- [[01. Reglas/8. Palabras clave (Keywords)/8.8. Resistir (Resist)|8.8.2. Daño reducido a 0]]
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