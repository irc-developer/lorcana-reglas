## ❓ Duda

Con Mother Gothel bicolor, si la habilidad que mueve daño se dispara cuando un personaje desafía o es desafiado, ¿hay que esperar a que el challenge termine o esa habilidad se resuelve en mitad del challenge? Y, si hay que elegir cómo mover el daño, ¿esa decisión se toma mientras el personaje sigue estando "challenging" o "being challenged"?

## ✅ Respuesta

No hay que esperar a que el challenge termine. Si la habilidad usa un disparador del tipo "when/whenever ... challenges" o "when/whenever ... is challenged", entra en la bolsa durante el Challenge Declaration step y se resuelve antes del Challenge Damage step.

Eso significa que la elección de cómo mover el daño se hace mientras el challenge sigue en curso. En ese momento los personajes implicados todavía están en el challenge, porque el challenge no termina hasta después del paso de daño y de vaciar la bolsa, salvo que uno de esos personajes salga antes del challenge por otro efecto o por un game state check.

La consecuencia práctica es importante: si el daño movido deja al personaje desafiado con daño letal, ese personaje puede ser desterrado antes del Challenge Damage step. Si eso ocurre, el challenge termina por salida de un personaje del challenge y no se llega a hacer el intercambio normal de daño del desafío.

## 🔄 Secuencia correcta

1. Se declara el challenge y se elige qué personaje desafía y cuál es desafiado.
2. El challenge ocurre y empiezan a aplicar los efectos "while challenging".
3. Las habilidades que dicen "challenges" o "is challenged" se añaden a la bolsa.
4. La habilidad de Mother Gothel se resuelve desde la bolsa antes del paso de daño.
5. Las elecciones del efecto se hacen al resolverlo, así que se toman con los personajes todavía dentro del challenge.
6. Si después de resolver la habilidad un personaje tiene daño letal, el game state check lo destierra.
7. Si uno de los personajes sale del challenge, el challenge termina ahí; si no, se pasa al Challenge Damage step.

## 🧪 Caso límite relevante

Si Mother Gothel mueve daño al personaje desafiado y eso hace que alcance o supere su Willpower, ese personaje es desterrado en el game state check inmediatamente posterior a la resolución de la habilidad. Como uno de los personajes ya no está en el challenge, se aplica la regla de salida del challenge y no se llega al daño normal del desafío.

## 📘 Referencias

### Wiki de Lorcana

- [[01. Reglas/4. Acciones de turno (Turn Actions)/4.6 Desafío (Challenge)|Declaración, habilidades y daño del desafío]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.1. General (General)|Elecciones y resolución de instrucciones]]
- [[01. Reglas/1. Principios generales/1.8. Chequeo del estado del juego (Game State Check)|Cuándo se comprueba el estado del juego]]
- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|Infligir, poner, mover y recibir daño]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Mover daño no es retirar daño|Cómo mover daño retira contadores y puede generar disparos]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Headless Horseman y Wreck-It Ralph - último valor conocido y bolsa|Headless Horseman y Wreck-It Ralph - último valor conocido y bolsa]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Boo - Energetic Child destierra antes del daño del desafío|Boo - Energetic Child destierra antes del daño del desafío]]

---

## 🏷️ Tags

#challenge #triggered-ability #bag #move-damage #timing #gsc
