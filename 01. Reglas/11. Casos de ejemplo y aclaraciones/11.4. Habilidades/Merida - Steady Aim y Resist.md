## ❓ Duda

Si [[02. Listado de Cartas/Set 12 - Wilds Unknown#Merida - Formidable Archer|Merida - Formidable Archer]] tiene la habilidad STEADY AIM ("Whenever one of your actions deals damage to an opposing character, deal 2 damage to that character") y una de tus acciones intenta infligir 1 daño a un personaje rival con Resist +1, ¿se dispara la habilidad?

¿Y qué pasa si esa misma acción fuera a infligir 2 daños antes de aplicar Resist +1?

---

## ✅ Respuesta

No. Si Resist reduce ese daño final a 0, la acción no se considera que haya infligido daño, así que STEADY AIM no se dispara.

Sí se dispara si, tras aplicar Resist y cualquier otro modificador de daño, la acción sigue infligiendo al menos 1 daño. En ese caso, STEADY AIM crea un segundo evento de daño independiente, y Resist se aplica de nuevo a ese segundo daño cuando la habilidad se resuelve.

Con escudos de reemplazo como los de [[02. Listado de Cartas/Set 11 - Winterspell.md#Lilo - Bundled Up|Lilo - Bundled Up]] o [[02. Listado de Cartas/Set 10 - Whispers in the Well.md#Rapunzel - Ready for Adventure|Rapunzel - Ready for Adventure]], ocurre lo mismo en el punto decisivo: si ese escudo reemplaza el daño de la acción original por “no damage”, la acción no llega a infligir daño y STEADY AIM no se dispara.

Si la acción original sí llegó a infligir daño y STEADY AIM ya se disparó, los 2 daños de STEADY AIM forman un nuevo evento de daño. Ese segundo evento puede ser reducido por Resist o reemplazado por un escudo si ese efecto de reemplazo sigue disponible cuando la habilidad se resuelva.

Excepción importante: no toda acción que acaba con daño sobre un personaje lo inflige. Si una acción **pone** contadores de daño directamente, como [[02. Listado de Cartas/Set 10 - Whispers in the Well.md#Malicious, Mean, and Scary|Malicious, Mean, and Scary]] (“Put 1 damage counter on each opposing character”), ese daño es **daño puesto**, no **daño infligido**. En ese caso, STEADY AIM no se dispara, aunque los personajes rivales sí hayan recibido daño.

Con Resist +1:

- Si la acción iba a infligir 1 daño, el daño final es 0 y STEADY AIM no se dispara.
- Si la acción iba a infligir 2 daños, el daño final es 1, STEADY AIM sí se dispara y luego intenta infligir 2 daños más; Resist reduce ese segundo paquete a 1. El total final es 2 daños.
- Si la acción original es reemplazada por un escudo tipo Lilo o Rapunzel, el daño final de esa acción es 0, no se considera infligido daño y STEADY AIM no se dispara.
- Si la acción original hizo daño y luego el objetivo conserva un escudo aplicable para el siguiente evento, ese escudo puede evitar por separado los 2 daños de STEADY AIM.
- Si la acción pone daño en vez de infligirlo, como [[02. Listado de Cartas/Set 10 - Whispers in the Well.md#Malicious, Mean, and Scary|Malicious, Mean, and Scary]], STEADY AIM no se dispara.

---

## 📘 Fundamento en reglas

- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|1.9.1.1. Deal/Dealt y 1.9.1.2. Put son categorías distintas de daño]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.5. Efectos de Reemplazo (Replacement Effects)|6.5. Los efectos de reemplazo modifican o sustituyen el evento cuando va a ocurrir]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de cartas y efectos (Resolving Cards and Effects)|6.7.2.3. Cálculo del daño final]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de cartas y efectos (Resolving Cards and Effects)|6.7.2.3. El daño calculado se inflige al resolver el efecto]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de cartas y efectos (Resolving Cards and Effects)|6.7.3. Los triggers se añaden a la bolsa tras ocurrir durante la resolución]]
- [[01. Reglas/8. Palabras clave (Keywords)/8.8. Resistir (Resist)|8.8.2. Si el daño se reduce a 0, no se considera infligido]]

---

## 🔄 Secuencia oficial

1. Juegas y resuelves una acción tuya que va a infligir daño a un personaje rival.
2. En 6.7.2.3 se calcula el daño final de esa acción aplicando los modificadores correspondientes, incluido Resist.
3. Si el resultado es 0, 8.8.2 indica que no se considera que se haya infligido daño, así que la condición de STEADY AIM no se cumple.
4. Si el resultado es 1 o más, ese daño sí se inflige durante la resolución de la acción.
5. La condición de STEADY AIM se cumple y la habilidad disparada se añade a la bolsa según 6.7.4, para resolverse después de que termine la acción.
6. Al resolverse STEADY AIM, sus 2 daños forman un nuevo evento de daño y Resist vuelve a reducir ese evento por separado.
7. Si el objetivo tiene un escudo de reemplazo disponible, ese escudo puede hacer que el evento original o el evento creado por STEADY AIM pase a “no damage”; en el evento que quede en 0, no se considera que se haya infligido daño.

---

## 🏷️ Tags

#merida #steady-aim #resist #replacement-effect #shield #triggered-ability #actions #damage #bag #damage-modifier