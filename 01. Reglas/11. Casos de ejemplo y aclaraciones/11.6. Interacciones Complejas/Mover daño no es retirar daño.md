## ❓ Duda

¿Cuando se mueve un daño de un personaje a otro se considera que estamos eliminando el daño de un personaje para ponérselo a otro?

## ✅ Respuesta

Sí. A la luz de la aclaración pública del diseñador de reglas, **mover daño equivale técnicamente a retirar daño del origen y poner ese mismo daño en el destino**, solo que el término "mover" lo escribe como una acción completa.

La forma más precisa de leerlo es esta:

- **Retirar daño** describe quitar contadores de daño de un personaje o localización.
- **Poner daño** describe colocar contadores de daño sobre un personaje o localización.
- **Mover daño** combina ambas cosas: se retira daño del origen y se pone en el destino dentro de un único efecto de mover daño.

Por eso, cuando se mueve daño:

- el personaje o localización de **origen** pierde contadores de daño;
- el personaje o localización de **destino** recibe daño, porque recibir daño incluye que el daño sea infligido, colocado o movido.

Lo que **no** cambia es el alcance de una instrucción. Si un efecto solo te dice **retirar daño**, eso no te da permiso para escoger un destino y recolocarlo allí; para eso el texto debe decir expresamente que lo **mueves**.

---

## 📘 Fundamento en reglas

**Definición: mover daño está escrito como retirar del origen y poner en el destino**

La definición general del daño distingue los verbos "remove", "put" y "move", pero la propia definición de "move" desarrolla exactamente esas dos operaciones: quitar contadores de daño de un objeto y colocarlos sobre otro.

**Definición: el destino del daño movido recibe daño**

La regla de "take" indica que un personaje o localización recibe daño cuando se le inflige, se le coloca o se le mueve daño.

**Definición: Resist no afecta al daño movido**

Esto confirma que el daño movido no se trata como daño infligido, pero sigue siendo daño puesto sobre el destino.

- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|1.9.1 Definición general del daño]]
- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|1.9.1.2 Put]]
- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|1.9.1.3 Remove/Removed]]
- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|1.9.1.4 Move]]
- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|1.9.1.5 Take]]
- [[01. Reglas/8. Palabras clave (Keywords)/8.8. Resistir (Resist)|8.8.3 Daño movido o puesto]]

---

## 📝 Nota de diseño

En una aclaración pública, RAV_Kyle explicó que la intención editorial era mantener paridad entre definiciones y evitar que "move" se definiera simplemente como "remove + put" sin desarrollar los términos. Precisamente por eso, indicó que **move sí equivale a remove más put, solo que escrito de forma desarrollada**.

---

## 🔄 Secuencia oficial

1. Un efecto indica **mover** una cantidad de daño desde un origen válido a un destino válido.
2. Al resolverse, esa cantidad de contadores de daño se **quita** del origen.
3. Esos mismos contadores se **colocan** sobre el destino.
4. Técnicamente, eso implica **retirar** daño del origen y **poner** daño en el destino dentro de la misma resolución.
5. Cuando el efecto termina de resolverse, se hace el chequeo de estado del juego; si el destino tiene daño letal, será desterrado en ese momento.

---

## 🏷️ Tags

#damage #move-damage #remove-damage #put-damage #take-damage #resist #rules-interpretation #gsc