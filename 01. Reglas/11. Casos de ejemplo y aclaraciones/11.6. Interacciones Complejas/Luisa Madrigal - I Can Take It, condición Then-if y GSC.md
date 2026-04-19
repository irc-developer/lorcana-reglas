## ❓ Duda

**Luisa Madrigal – Confident Climber** (Wilds Unknown) tiene la habilidad activada:

> **I CAN TAKE IT** 1{I} – Move up to 1 damage from chosen character of yours to this character. Then, if this character has 3 or more damage, move all damage from this character to chosen opposing character.

Luisa tiene 3 contadores de daño y su Willpower es 4. Se activa *I Can Take It* para moverle 1 daño adicional (pasaría a 4, igual a su Willpower). ¿La segunda parte del efecto se resuelve antes del GSC, permitiéndole sobrevivir?

---

## ✅ Respuesta

**Sí, Luisa sobrevive.**

El GSC ocurre solo *después* de que el efecto se resuelve por completo. La condición `if this character has 3 or more damage` se evalúa en el momento en que se ejecuta esa parte del texto, es decir, una vez que la Parte 1 (`Then`) ya ha colocado el daño sobre Luisa. Al ser verdadera, se mueve todo el daño al personaje rival antes de que llegue el GSC.

---

## 🔄 Secuencia oficial

| Paso | Acción | Estado de Luisa |
|---|---|---|
| 1 | Pagar 1{I} (coste de activación) | 3 daño |
| 2 | Elegir objetivos (personaje aliado origen y personaje rival destino) | 3 daño |
| 3 | **Parte 1**: Mover 1 daño al personaje aliado → a Luisa | **4 daño** (= Willpower) |
| 4 | Evaluar `if this character has 3 or more damage` → 4 ≥ 3 → **VERDADERO** | 4 daño |
| 5 | **Parte 2**: Mover *todo* el daño de Luisa al personaje rival elegido | **0 daño** |
| 6 | Efecto completamente resuelto → **GSC** | 0 daño → no se destierra ✅ |

---

## 📘 Fundamento en reglas

- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)#6.7.4. Comprobación del estado del juego|6.7.4 GSC tras la resolución completa]]: el GSC se realiza *después* de que cada efecto se resuelve, no a mitad.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)#6.7.2.4. Cuarto paso - resolución del texto|6.7.2.4 Resolución del texto en orden]]: las instrucciones se ejecutan en su totalidad y en el orden escrito.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.1. General (General)#6.1.2.|6.1.2 Efectos en una única resolución]]: las frases de una misma habilidad forman una única resolución.
- [[01. Reglas/1. Principios generales (Concepts)/1.9. Verificación del estado de la partida (Game State Check)|1.9 Verificación del estado de la partida (GSC)]]

---

## 💡 Nota sobre la condición `Then, if`

La condición `if this character has 3 or more damage` no es una condición secundaria de tipo disparado (`[Trigger Condition], if [Condition], [Effect]` conforme a 6.2.4) que se evalúe al inicio del efecto. Forma parte de un efecto secuencial separado por `Then`, cuya condición se comprueba cuando se alcanza ese punto de la ejecución del texto (paso 6.7.2.4), por lo que recoge el estado real de Luisa *después* de la Parte 1.

Esto es análogo a cualquier efecto multi-parte donde las condiciones internas reflejan el estado del juego en el momento en que se ejecutan, no al inicio de la resolución.

---

## 🏷️ Tags

#gsc #activated-ability #movedamage #sequential-effect #then-if #resolution #timing #luisa-madrigal
