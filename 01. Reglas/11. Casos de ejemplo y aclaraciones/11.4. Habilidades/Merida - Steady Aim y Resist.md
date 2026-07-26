## ❓ Duda

Si [[02. Listado de Cartas/Set 12 - Wilds Unknown.md#Merida - Formidable Archer|Merida - Formidable Archer]] tiene STEADY AIM y una de tus acciones intenta infligir 1 daño a un personaje rival con Resist +1, ¿se dispara la habilidad aunque el personaje reciba 0?

---

## ✅ Respuesta

**Sí.** Desde las CR 2.2, si Resist reduce el daño a 0, la acción sigue considerándose que ha infligido daño y STEADY AIM se dispara.

La regla 1.9.5 separa el daño que **inflige la fuente** del daño que **recibe el personaje**. La acción cuenta como que ha infligido daño, mientras que el personaje con Resist no recibe ninguno.

STEADY AIM crea después un segundo evento de daño independiente. Resist vuelve a aplicarse a esos 2 daños cuando la habilidad se resuelve.

Con Resist +1:

- Si la acción intenta infligir 1 daño, el personaje recibe 0, pero STEADY AIM se dispara. Sus 2 daños se reducen después a 1. El total recibido es **1**.
- Si la acción intenta infligir 2 daños, el personaje recibe 1 y STEADY AIM se dispara. Sus 2 daños se reducen después a 1. El total recibido es **2**.
- Si un escudo de Lilo o Rapunzel reemplaza el daño recibido de la acción, la acción sigue contando como que ha infligido daño y STEADY AIM también se dispara.

No toda acción que coloca daño lo **inflige**. Si una acción **pone** contadores directamente, como [[02. Listado de Cartas/Set 10 - Whispers in the Well.md#Malicious, Mean, and Scary|Malicious, Mean, and Scary]], ese daño es *put damage*, no *deal damage*. STEADY AIM no se dispara en ese caso.

La interacción completa con los dos escudos está desarrollada en [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Merida frente a Lilo y Rapunzel - infligir daño no es recibir daño|Merida frente a Lilo y Rapunzel - infligir daño no es recibir daño]].

---

## 📘 Fundamento en reglas

- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|1.9.2.1. Deal y 1.9.2.2. Put son operaciones distintas]]
- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)#1.9.5. Daño reducido a 0|1.9.5. La fuente sigue considerándose que inflige daño]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de cartas y efectos (Resolving Cards and Effects)|6.7.2. Cálculo y resolución del daño]]
- [[01. Reglas/8. Palabras clave (Keywords)/8.8. Resistir (Resist)|8.8.2. El objeto no recibe daño si se reduce a 0]]

---

## 🔄 Secuencia

1. La acción intenta infligir daño a un personaje rival.
2. Se calcula el daño aplicando los modificadores correspondientes, incluido Resist.
3. Aunque el resultado sea 0, 1.9.5 mantiene que la acción ha infligido daño; el personaje es quien no lo recibe.
4. STEADY AIM se añade a la bolsa y espera a que termine la acción.
5. Cuando STEADY AIM se resuelve, genera un nuevo evento de 2 daños.
6. Resist y cualquier reemplazo aplicable se evalúan de nuevo para ese evento.

---

## 🏷️ Tags

#merida #steady-aim #resist #triggered-ability #actions #damage #bag #damage-modifier #cr-2-2
