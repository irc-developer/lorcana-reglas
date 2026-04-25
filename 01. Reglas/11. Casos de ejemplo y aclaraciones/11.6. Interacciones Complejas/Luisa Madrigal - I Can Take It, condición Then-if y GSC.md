## ❓ Duda

**Luisa Madrigal – Confident Climber** (Wilds Unknown) tiene la habilidad activada:

> **I CAN TAKE IT** 1{I} – Move up to 1 damage from chosen character of yours to this character. Then, if this character has 3 or more damage, move all damage from this character to chosen opposing character.

¿Cómo funciona exactamente esta habilidad y qué ocurre en las casuísticas habituales: mover 0 o 1 daño, alcanzar 3 daños, alcanzar daño letal, no tener personaje rival disponible, interactuar con Resist o generar habilidades por daño?

---

## ✅ Respuesta

**I Can Take It** es una única habilidad activada con **dos instrucciones secuenciales** dentro de la misma resolución.

Primero eliges un personaje tuyo y mueves **0 o 1** daño desde ese personaje a Luisa. Después, **solo en ese momento**, compruebas si Luisa tiene **3 o más** daños. Si la condición es verdadera, eliges un personaje rival y mueves **todo** el daño de Luisa a ese personaje.

El **GSC** no ocurre entre ambas instrucciones, sino **después** de que toda la habilidad termina de resolverse. Por eso, si Luisa llega a daño letal en la primera instrucción pero luego mueve todo ese daño fuera de sí en la segunda, **sobrevive**.

**Sí puede usarse aunque no tengas otro personaje en mesa.** La activación de una habilidad activada comprueba **coste y momento de uso**, no la existencia previa de objetivos legales. En ese caso, al resolverse, la primera instrucción no puede realizarse porque Luisa no puede ser su propio origen; después se sigue resolviendo el resto del texto tanto como sea posible.

Además, el daño movido al personaje rival **sí cuenta como daño recibido**, pero **no** como daño infligido a efectos de **Resist**, así que Resist no lo reduce.

El punto clave con **Ward** es este: **Ward no impide activar la habilidad**. Lo único que impide es **elegir** esa carta cuando la segunda instrucción llega a resolverse. Por tanto, puedes anunciar y pagar **I Can Take It** aunque el único personaje rival tenga Ward; simplemente, si Luisa llega a la segunda instrucción y sigue sin existir un personaje rival legal que puedas elegir, esa parte no hará nada.

---

## 🔄 Funcionamiento exacto

1. **Activación de la habilidad**: es una habilidad activada con coste de **1 tinta**. Como no incluye ![[imagenes/exert.svg|20]] en el coste, Luisa puede usarla incluso el turno en que entra en juego.
2. **Primera instrucción**: al resolver, eliges un personaje tuyo. Ese personaje **no tiene que estar dañado**, porque la instrucción dice **up to 1 damage** y “hasta 1” incluye **0**. **Luisa no puede elegirse a sí misma como origen** de ese daño, porque mover daño exige quitarlo de un personaje y ponerlo en **otro** personaje distinto.
3. **Movimiento inicial**: mueves **0 o 1** daño desde ese personaje a Luisa. Si el personaje elegido tiene daño, puedes mover 1 o decidir mover 0. Si no tiene daño, simplemente mueves 0.
4. **Comprobación de la condición**: después de esa primera instrucción miras cuántos daños tiene Luisa **en ese momento exacto**.
5. **Segunda instrucción**: si Luisa tiene **3 o más** daños, eliges entonces un personaje rival y mueves **todo** el daño de Luisa a ese personaje. No se mueve una parte; se mueve **todo**. **Ward solo importa aquí**, porque es aquí donde la habilidad te pide elegir un personaje rival.
6. **Final de la resolución**: cuando ambas instrucciones han terminado, las habilidades disparadas generadas durante el proceso esperan en la bolsa y luego se realiza el **GSC**.

### Cuándo puedes usar la habilidad frente a Ward

Puedes activar **I Can Take It** si puedes anunciarla y pagar su coste. El procedimiento de usar una habilidad activada no exige elegir al personaje rival por adelantado.

Eso significa:

- si el único personaje rival tiene **Ward**, **sí puedes activar** la habilidad igualmente
- si al llegar a la segunda instrucción sigue siendo el único personaje rival legalmente disponible, **no podrás elegirlo**
- como no existe otra elección legal en ese punto, **la segunda instrucción se resuelve sin efecto**
- el resultado final es que Luisa **conserva su daño**

No se deshace la activación porque la ilegalidad no estaba en **usar** la habilidad, sino en que **al resolver la segunda elección no existe objetivo legal disponible**.

---

## 🧪 Casuísticas frecuentes

| Situación | Resultado | Motivo |
|---|---|---|
| Luisa tiene **0 o 1** daños y mueves **1** hacia ella | Luisa se queda en **1 o 2** daños y **no** hay segunda parte | La condición de **3 o más** no se cumple |
| Luisa tiene **2** daños y mueves **1** hacia ella | Luisa llega a **3**, luego mueve **los 3** a un personaje rival | La condición se comprueba después de la primera instrucción |
| Luisa tiene **3** daños y eliges mover **0** | Luisa sigue con **3** y luego mueve **los 3** a un personaje rival | “Up to 1” permite mover **0** y `Then` no exige haber movido 1 |
| Luisa tiene **3** daños de **4** de Willpower y mueves **1** | Luisa pasa a **4**, luego mueve **los 4** fuera de sí y **sobrevive** | El GSC ocurre solo al final de toda la resolución |
| El personaje elegido tiene **0** daños | La primera instrucción mueve **0**; sigue siendo una resolución legal | No hace falta que el origen esté dañado |
| El personaje elegido tiene **más de 1** daño | En la primera instrucción solo puedes mover **1** | El texto limita a **up to 1 damage** |
| Luisa es tu **único personaje** en juego | **Sí puedes usar la habilidad**, pero Luisa **no puede ser el origen** de la primera instrucción | La activación solo exige pagar el coste; mover daño exige un origen y un destino distintos |
| Luisa es tu **único personaje**, pero ya tiene **3 o más** daños | Si hay personaje rival legal, la segunda instrucción **sí puede resolverse** | `Then` ordena la secuencia, pero no exige que la primera parte haya tenido éxito |
| Luisa ya tenía **3 o más** daños antes de activar la habilidad | Aunque la primera instrucción mueva **0**, la segunda puede ocurrir igualmente | La condición mira el estado real de Luisa al llegar a esa parte |
| Hay varios personajes rivales y **uno tiene Ward** | El personaje con Ward **no puede ser elegido**; si hay otro rival legal sin Ward, debes elegir entre esos personajes legales | Ward impide que el oponente elija esa carta al resolver un efecto |
| El **único** personaje rival disponible tiene **Ward** | **Sí puedes activar la habilidad**, pero la segunda instrucción no puede realizarse y Luisa conserva su daño | Ward no impide activar; impide elegir ese personaje cuando llega la segunda instrucción |
| Al llegar a la segunda instrucción **no existe personaje rival legal** | Esa parte no puede realizarse; Luisa conserva su daño | Se resuelve el efecto **tanto como sea posible** en orden |
| El personaje rival tiene **Resist** | El daño movido **no se reduce** | Resist solo reduce daño **infligido**, no daño **movido o puesto** |
| El personaje rival tiene una habilidad del tipo **“whenever this character is damaged”** | Esa habilidad sí puede dispararse | Recibir daño incluye daño **movido** |

---

## 🔄 Secuencia ejemplo con daño letal

| Paso | Acción | Estado de Luisa |
|---|---|---|
| 1 | Pagar **1{I}** | 3 daño |
| 2 | Elegir un personaje tuyo para la primera instrucción | 3 daño |
| 3 | Mover **1** daño a Luisa | **4 daño** (= Willpower) |
| 4 | Comprobar `if this character has 3 or more damage` | 4 daño, condición verdadera |
| 5 | Elegir personaje rival y moverle **todo** el daño de Luisa | **0 daño** |
| 6 | La habilidad termina de resolverse | 0 daño |
| 7 | Se hace el **GSC** | Luisa no se destierra |

---

## 📘 Fundamento en reglas

- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.3. Habilidades Activadas (Activated Abilities)|6.3. Habilidades Activadas]]: la subregla 6.3.1.1 indica que una habilidad activada en un personaje que no tenga el símbolo de exert como parte del coste puede usarse el mismo turno en que ese personaje entra en juego; por tanto, esta restricción no impide usar I Can Take It el turno en que Luisa entra en juego.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.3. Habilidades Activadas (Activated Abilities)|6.3. Habilidades Activadas]]: la subregla 6.3.2 fija el momento general en el que puede usarse una habilidad activada.
- [[01. Reglas/4. Acciones de turno (Turn Actions)/4.4. Usar una habilidad activada (Use an Activated Ability)|4.4. Usar una habilidad activada]]: las subreglas 4.4.3 y 4.4.4 establecen que primero se anuncia la habilidad, se calcula y paga el coste, y solo después se resuelve el efecto; el procedimiento no exige fijar objetivos antes de activar.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.1. General (General)|6.1. General]]: las subreglas 6.1.2 y 6.1.3 indican que las frases se resuelven en orden, que se hace todo lo posible y que las elecciones se realizan durante la resolución; además, “hasta” incluye 0.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)|6.7. Resolución de Cartas y Efectos]]: las subreglas 6.7.2.4 y 6.7.4 establecen que las instrucciones del texto se cumplen en orden y tanto como sea posible, y que el GSC se realiza tras resolverse el efecto.
- [[01. Reglas/1. Principios generales/1.7. Game Actions, Timing, y Illegal Actions|1.7. Game Actions, Timing, y Illegal Actions]]: la subregla 1.7.7 indica que si se hace una elección ilegal durante la resolución, se retrocede hasta ese punto y se elige de nuevo; si no existe ninguna elección legal, esa parte del efecto se resuelve sin efecto.
- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|1.9. Daño]]: las subreglas 1.9.1.4, 1.9.1.5 y 1.9.2 definen qué es mover daño, qué significa recibir daño y cómo se interpretan expresiones como is damaged.
- [[01. Reglas/8. Palabras clave (Keywords)/8.15 Protección (ward)|8.15 Protección (ward)]]: Ward significa que tus oponentes no pueden elegir esa carta al resolver un efecto.
- [[01. Reglas/8. Palabras clave (Keywords)/8.8. Resistir (Resist)|8.8. Resistir]]: la subregla 8.8.3 aclara que Resist no reduce daño movido o puesto.
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Resolución parcial sin objetivo válido|Resolución parcial sin objetivo válido]]: si una primera cláusula no puede realizarse, una segunda cláusula independiente puede resolverse igualmente.

---

## 🔗 Véase también

- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/No tener objetivo legal vs elegir un objetivo inválido|No tener objetivo legal vs elegir un objetivo inválido]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Mover daño no es retirar daño|Mover daño no es retirar daño]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/El uso de Then|El uso de Then]]

---

## 🏷️ Tags

#gsc #activated-ability #move-damage #take-damage #resist #sequential-effect #then-if #resolution #timing #luisa-madrigal
