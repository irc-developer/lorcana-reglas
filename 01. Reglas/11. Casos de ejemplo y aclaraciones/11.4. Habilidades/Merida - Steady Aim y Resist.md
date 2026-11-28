## ❓ Duda

Si [Merida - Formidable Archer](https://cards.lorcast.io/card/digital/large/crd_4811e7317e3149db966bab69151147cc.avif?1777688117) tiene STEADY AIM y una de tus acciones intenta infligir 1 daño a un personaje rival con Resist +1, ¿se dispara la habilidad aunque el personaje reciba 0?

---

## ✅ Respuesta

**Sí.** Si Resist reduce el daño a 0, la acción sigue considerándose que ha infligido daño y STEADY AIM se dispara.

La regla 1.9.5 separa el daño que **inflige la fuente** del daño que **recibe el personaje**. La acción cuenta como que ha infligido daño, mientras que el personaje con Resist no recibe ninguno.

STEADY AIM crea después un segundo evento de daño independiente. Resist vuelve a aplicarse a esos 2 daños cuando la habilidad se resuelve.

Con Resist +1:

- Si la acción intenta infligir 1 daño, el personaje recibe 0, pero STEADY AIM se dispara. Sus 2 daños se reducen después a 1. El total recibido es **1**.
- Si la acción intenta infligir 2 daños, el personaje recibe 1 y STEADY AIM se dispara. Sus 2 daños se reducen después a 1. El total recibido es **2**.
- Si **ACT OF KINDNESS** de Rapunzel reemplaza el daño de la acción, la fuente deja de infligir ese daño al personaje protegido y STEADY AIM no se dispara por él. Con **EXTRA LAYERS** de Lilo, queda por aclarar si la fuente cuenta como que infligió daño después del reemplazo.

No toda acción que coloca daño lo **inflige**. Si una acción **pone** contadores directamente, como [Malicious, Mean, and Scary](https://cards.lorcast.io/card/digital/large/crd_7039c6bce8754b01894d3d1e7868b6b2.avif?1761752397), ese daño es *put damage*, no *deal damage*. STEADY AIM no se dispara en ese caso.

La interacción completa con los dos escudos está desarrollada en [[Merida frente a Lilo y Rapunzel - infligir daño no es recibir daño]].

---

## 📘 Referencias

### Wiki de Lorcana

- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|Distinguir daño infligido, puesto, movido y recibido]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)|Resolver las instrucciones antes de atender los disparos y el estado del juego]]
- [[01. Reglas/8. Palabras clave (Keywords)/8.8. Resistir (Resist)|Reducir el daño infligido y distinguirlo del daño recibido]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.5. Efectos de Reemplazo (Replacement Effects)|Cómo se aplican y se combinan los efectos de reemplazo]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Merida frente a Lilo y Rapunzel - infligir daño no es recibir daño|Comparar Resist con las protecciones de Lilo y Rapunzel]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Hydra - Deadly Serpent y Resist +1|Contraste con una habilidad que exige que su personaje reciba daño]]

### Fuentes oficiales

- Comprehensive Rules, reglas 1.9.2.1, 1.9.2.2, 1.9.5, 6.7.2, 8.8.2, 6.5.4, 6.5.8.

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

#resist #triggered-ability #turn-actions #damage #bag
