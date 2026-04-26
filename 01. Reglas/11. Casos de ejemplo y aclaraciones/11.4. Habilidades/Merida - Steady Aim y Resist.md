## ❓ Duda

Si [[Cartas de Lorcana#Merida - Formidable Archer|Merida - Formidable Archer]] tiene la habilidad STEADY AIM ("Whenever one of your actions deals damage to an opposing character, deal 2 damage to that character") y una de tus acciones intenta infligir 1 daño a un personaje rival con Resist +1, ¿se dispara la habilidad?

¿Y qué pasa si esa misma acción fuera a infligir 2 daños antes de aplicar Resist +1?

---

## ✅ Respuesta

No. Si Resist reduce ese daño final a 0, la acción no se considera que haya infligido daño, así que STEADY AIM no se dispara.

Sí se dispara si, tras aplicar Resist y cualquier otro modificador de daño, la acción sigue infligiendo al menos 1 daño. En ese caso, STEADY AIM crea un segundo evento de daño independiente, y Resist se aplica de nuevo a ese segundo daño cuando la habilidad se resuelve.

Con Resist +1:

- Si la acción iba a infligir 1 daño, el daño final es 0 y STEADY AIM no se dispara.
- Si la acción iba a infligir 2 daños, el daño final es 1, STEADY AIM sí se dispara y luego intenta infligir 2 daños más; Resist reduce ese segundo paquete a 1. El total final es 2 daños.

---

## 📘 Fundamento en reglas

- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de cartas y efectos (Resolving Cards and Effects)|6.7.2.3. Cálculo del daño final]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de cartas y efectos (Resolving Cards and Effects)|6.7.2.4. El daño calculado se inflige al resolver el efecto]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de cartas y efectos (Resolving Cards and Effects)|6.7.3. Los triggers se añaden a la bolsa tras ocurrir durante la resolución]]
- [[01. Reglas/8. Palabras clave (Keywords)/8.8. Resistir (Resist)|8.8.2. Si el daño se reduce a 0, no se considera infligido]]

---

## 🔄 Secuencia oficial

1. Juegas y resuelves una acción tuya que va a infligir daño a un personaje rival.
2. En 6.7.2.3 se calcula el daño final de esa acción aplicando los modificadores correspondientes, incluido Resist.
3. Si el resultado es 0, 8.8.2 indica que no se considera que se haya infligido daño, así que la condición de STEADY AIM no se cumple.
4. Si el resultado es 1 o más, ese daño sí se inflige durante la resolución de la acción.
5. La condición de STEADY AIM se cumple y la habilidad disparada se añade a la bolsa según 6.7.3, para resolverse después de que termine la acción.
6. Al resolverse STEADY AIM, sus 2 daños forman un nuevo evento de daño y Resist vuelve a reducir ese evento por separado.

---

## 🏷️ Tags

#merida #steady-aim #resist #triggered-ability #actions #damage #bag #damage-modifier