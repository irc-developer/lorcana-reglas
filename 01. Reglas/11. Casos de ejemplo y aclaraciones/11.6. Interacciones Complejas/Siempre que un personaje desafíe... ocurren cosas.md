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

## 📘 Fundamento en reglas

- [[01. Reglas/4. Acciones de turno (Turn Actions)/4.6 Desafío (Challenge)|4.6 Desafío]]: la subregla 4.6.4.5 indica que el challenge ocurre y que los efectos "while challenging" empiezan a aplicar en ese momento.
- [[01. Reglas/4. Acciones de turno (Turn Actions)/4.6 Desafío (Challenge)|4.6 Desafío]]: la subregla 4.6.5 establece que las habilidades que dicen "challenges" o "is challenged" se añaden a la bolsa y se resuelven antes del Challenge Damage step.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.1. General (General)|6.1 General]]: la subregla 6.1.3 indica que todas las elecciones se realizan durante la resolución del efecto.
- [[01. Reglas/1. Principios generales/1.8. Chequeo del estado del juego (Game State Check)|1.8 Chequeo del estado del juego]]: la subregla 1.8.1.4 indica que un personaje con daño igual o superior a su Willpower es desterrado en el game state check.
- [[01. Reglas/4. Acciones de turno (Turn Actions)/4.6 Desafío (Challenge)|4.6 Desafío]]: las subreglas 4.6.7 y 4.6.9 aclaran que el challenge solo termina al final del proceso normal o antes si un personaje sale del challenge.
- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|1.9 Daño]]: las subreglas 1.9.1.4 y 1.9.1.5 aclaran que mover daño quita contadores del origen y pone esos mismos contadores en el destino, y que ese destino recibe daño.

## 🔗 Véase también

- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Mover daño no es retirar daño|Mover daño no es retirar daño]]
- [[01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Headless Horseman y Wreck-It Ralph - último valor conocido y bolsa|Headless Horseman y Wreck-It Ralph - último valor conocido y bolsa]]

## 🏷️ Tags

#mother-gothel #challenge #challenging #being-challenged #triggered-ability #bag #move-damage #timing #gsc

