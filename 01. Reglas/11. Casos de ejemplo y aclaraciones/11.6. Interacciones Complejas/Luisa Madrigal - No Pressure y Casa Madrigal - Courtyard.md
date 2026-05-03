## ❓ Duda

**Luisa Madrigal - No Pressure** tiene:

> **SHOULDER THE BURDEN** Whenever this character quests, you may move up to 3 damage from chosen character to this character.

Y **Casa Madrigal - Courtyard** tiene:

> **HEALING HOME** Whenever a character quests while here, you may remove up to 2 damage from them. Then, you may remove up to 2 damage from this location.

Si Luisa questea mientras está en esa localización y su habilidad le mueve daño encima, ¿la casa la cura después por ese mismo quest? ¿Se resuelve primero la acción completa de Luisa y luego salta el trigger de la casa?

---

## ✅ Respuesta

El mismo quest de Luisa hace que **ambas habilidades se disparen a la vez**: la de Luisa por "Whenever this character quests" y la de la Casa por "Whenever a character quests while here".

Las dos habilidades se añaden **simultáneamente a la bolsa**, pero **no** se resuelven a la vez. Como normalmente ambas pertenecen al jugador activo, ese jugador elige cuál resuelve primero.

La parte importante es esta: **entre resolver una habilidad disparada y resolver la siguiente sí hay comprobación del estado del juego**. Por eso, si resuelves primero a Luisa y al mover daño sobre ella queda con daño letal, Luisa será desterrada antes de que puedas resolver después la curación de la Casa.

Así que la Casa **sí puede curar por ese mismo quest**, pero solo si cuando su habilidad vaya a resolverse la carta sigue en juego y sigue siendo un objetivo legal. No existe una "resolución conjunta" en la que la Casa espere dentro de la misma resolución de Luisa para salvarla del GSC.

---

## 🔄 Funcionamiento exacto

1. **Luisa hace quest** mientras está en **Casa Madrigal - Courtyard**.
2. Ese mismo evento cumple a la vez la condición de disparo de **Shoulder the Burden** y de **Healing Home**.
3. Ambas habilidades se añaden a la **bolsa** al mismo tiempo.
4. Como son habilidades del jugador activo, ese jugador elige cuál resuelve primero.
5. Se resuelve por completo la primera habilidad elegida.
6. Después de esa resolución, se hace el **GSC**.
7. Si siguen quedando habilidades tuyas en la bolsa, eliges la siguiente y la resuelves.

La consecuencia práctica es que el orden importa mucho.

---

## 🧪 Casuísticas frecuentes

| Situación | Resultado | Motivo |
|---|---|---|
| Luisa tiene **1 daño** y mueves **2** con su habilidad; después resuelves la Casa | La Casa puede curar hasta **2** a Luisa | Luisa no llega a daño letal tras resolver su propia habilidad |
| Luisa tiene **4 de Voluntad**, ya tiene **2 daños** y mueves **2** con su habilidad; resuelves primero a Luisa | Luisa llega a **4 daños**, se hace GSC y es desterrada antes de la Casa | El GSC ocurre tras cada resolución desde la bolsa |
| Mismo caso anterior, pero resuelves primero la Casa | La Casa puede curar primero hasta **2** a Luisa o a otro personaje; luego resuelves la habilidad de Luisa | El jugador activo elige el orden entre triggers simultáneos propios |
| Luisa sobrevive a su propia habilidad y luego resuelves la Casa | La Casa puede curar a **Luisa** hasta **2** daños y luego hasta **2** a la localización | Luisa sigue en juego cuando Healing Home se resuelve |
| Luisa es desterrada por GSC tras su habilidad | La Casa ya no puede curar a **Luisa**; solo podrá curar la localización si su texto sigue pudiendo aplicarse | Luisa ya no está en juego al llegar esa resolución |

---

## 🔄 Ejemplo con números

Supón esta situación:

- **Luisa Madrigal - No Pressure** está en **Casa Madrigal - Courtyard**.
- Luisa tiene **2 daños** y **4 de Voluntad**.
- Otro de tus personajes tiene **2 daños**.

Si Luisa questea, se disparan a la vez ambas habilidades.

Si eliges resolver primero **Shoulder the Burden**, puedes mover hasta **2** daños desde tu otro personaje a Luisa. Luisa pasa de **2** a **4** daños. La habilidad termina de resolverse y, antes de tocar el trigger de la Casa, se hace el **GSC**. Como Luisa tiene daño igual a su Voluntad, es desterrada. Cuando después quieras resolver **Healing Home**, la parte de "remove up to 2 damage from them" ya no podrá aplicarse sobre Luisa porque ya no está en juego.

Si, en cambio, eliges resolver primero **Healing Home**, puedes quitar hasta **2** daños a Luisa y luego hasta **2** daños a la Casa. Solo después resolverías **Shoulder the Burden**.

---

## 📘 Fundamento en reglas

- [[01. Reglas/7. Zonas (Zones)/7.7. Bolsa (Bag)|7.7. Bolsa (Bag)]]: la subregla **7.7.3.1** indica que si varias habilidades disparadas ocurren al mismo tiempo, se añaden a la bolsa simultáneamente.
- [[01. Reglas/7. Zonas (Zones)/7.7. Bolsa (Bag)|7.7. Bolsa (Bag)]]: las subreglas **7.7.4.2** y **7.7.4.3** indican que el jugador activo elige una de sus habilidades disparadas en la bolsa y la resuelve por completo antes de elegir la siguiente.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)|6.7. Resolución de Cartas y Efectos]]: la subregla **6.7.4** aclara que las habilidades disparadas creadas durante una resolución esperan a la bolsa y no se mezclan dentro de esa misma resolución.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)|6.7. Resolución de Cartas y Efectos]]: la subregla **6.7.5** establece que la comprobación del estado del juego se realiza después de que se resuelvan todos los efectos de una acción o habilidad.
- [[01. Reglas/1. Principios generales/1.8. Chequeo del estado del juego (Game State Check).md|1.8. Chequeo del estado del juego (Game State Check)]]: un personaje con daño igual o superior a su Voluntad es desterrado en esa comprobación.
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Múltiples habilidades a la vez|Múltiples habilidades a la vez]]: resume que los triggers simultáneos no se resuelven a la vez, sino uno por uno desde la bolsa.

---

## 🔗 Véase también

- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Luisa Madrigal - I Can Take It, condición Then-if y GSC|Luisa Madrigal - I Can Take It, condición Then-if y GSC]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Mover daño no es retirar daño|Mover daño no es retirar daño]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Múltiples habilidades a la vez|Múltiples habilidades a la vez]]

---

## 🏷️ Tags

#bag #triggered-abilities #resolution-order #gsc #quest #move-damage #remove-damage #luisa-madrigal #casa-madrigal