## ❓ Duda

Si controlo Headless Horseman y Wreck-It Ralph, y Ralph es desterrado mientras tiene cartas debajo que aumentan su Fuerza, ¿la habilidad de Headless Horseman puede ir aumentando la Fuerza de mis personajes a medida que Ralph va desterrando personajes rivales con su trigger? ¿Eso puede salvar a algunos personajes del efecto de Ralph, o Ralph destierra de una vez a todos los personajes rivales con Fuerza igual o menor que la suya antes de que Headless Horseman haga nada?

---

## ✅ Respuesta

No. Headless Horseman no puede salvar personajes del mismo efecto disparado de Wreck-It Ralph.

Cuando se resuelve la habilidad de Ralph, el juego mira la Fuerza que Ralph tenía justo antes de abandonar el juego usando su último valor conocido. Con ese valor se determina qué personajes rivales tienen Fuerza igual o menor y esos personajes se destierran como parte de esa misma resolución. Los disparos de Headless Horseman provocados por esos destierros se añaden a la bolsa, pero esperan a resolverse hasta que la habilidad de Ralph haya terminado por completo. Para entonces, los personajes ya han sido desterrados.

En la línea concreta donde primero destierras un personaje rival con Headless Horseman y luego Ralph desafía a otro personaje rival haciendo que ambos sean desterrados en ese challenge, el resultado correcto es este:

- Ralph sí conserva para su trigger el +1 {S} que ya había ganado antes ese turno, así que usa su último valor conocido de 4 {S}.
- Cuando Ralph y el personaje rival son desterrados a la vez, se disparan simultáneamente la habilidad de Ralph y la de Headless Horseman.
- Puedes elegir en qué orden resolver esas dos habilidades porque ambas son tuyas.
- Pero aunque resuelvas primero la de Headless Horseman, ese +1 no cambia retroactivamente la Fuerza que Ralph tenía antes de abandonar el juego.
- Por tanto, Ralph destierra a los personajes rivales con 4 {S} o menos, no con 5 {S} o menos.
- Si Headless Horseman no estaba en ese challenge, puede seguir en juego y luego recibir su +1, quedándose con 6 {S} hasta el final del turno.

La consecuencia práctica es esta:

- Sí cuentan los aumentos de Fuerza que Ralph ya tenía antes de ser desterrado.
- No cuentan los nuevos disparos de Headless Horseman creados por los personajes que Ralph acaba de desterrar.

---

## 📘 Fundamento en reglas

- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)#6.7.6. Último valor conocido|6.7.6. Último valor conocido]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.4. Habilidades Estáticas (Static Abilities)#6.4.2.3. Habilidades estáticas continuas generadas por cartas en juego|6.4.2.3. Fin inmediato del efecto al salir del juego]]
- [[01. Reglas/7. Zonas (Zones)/7.4. Juego (Play)#7.4.3. Cartas abandonando la zona de Juego.|7.4.3. Las habilidades disparadas ven a las cartas que abandonan el juego simultáneamente]]
- [[01. Reglas/7. Zonas (Zones)/7.7. Bolsa (Bag)#7.7.3.1. Añadir a la bolsa un efecto|7.7.3.1. Los triggers creados durante una resolución esperan a que el efecto actual termine]]
- [[01. Reglas/1. Principios generales/1.8. Chequeo del estado del juego (Game State Check)#1.8.3. Evaluación cíclica|1.8.3. La bolsa se resuelve después de completar las comprobaciones y resoluciones en curso]]

---

## 🔄 Secuencia oficial

1. **Primer destierro previo**: Headless Horseman destierra a un personaje rival durante tu turno y su trigger se resuelve. Ralph pasa de 3 {S} a 4 {S} este turno.
2. **Challenge**: Ralph desafía a otro personaje rival y ambos reciben daño letal.
3. **GSC**: Ralph y el personaje rival son desterrados simultáneamente.
4. **Triggers simultáneos**: se disparan a la vez la habilidad de Ralph y la de Headless Horseman, porque Headless Horseman ve al personaje rival abandonar el juego en ese mismo evento.
5. **Orden en la bolsa**: como ambas habilidades son tuyas, eliges cuál resolver primero.
6. **Resolución de Ralph**: cuando resuelves la habilidad de Ralph, usa su último valor conocido antes de abandonar el juego, que en este ejemplo es 4 {S}.
7. **Aplicación del efecto**: Ralph destierra a todos los personajes rivales con 4 {S} o menos.
8. **Resolución posterior de Horseman**: después puede resolverse la habilidad de Headless Horseman y dar +1 {S} a tus personajes que sigan en juego, pero eso ya no cambia el barrido de Ralph.

---

## 🏷️ Tags

#headlesshorseman #wreckitralph #last-known-value #bag #triggered-abilities #static-abilities #strength #banish #resolution-order