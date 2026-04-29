## ❓ Duda

Si controlo a [[02. Listado de Cartas/Set 12 - Wilds Unknown#Dale - Ready for His Shot|Dale - Ready for His Shot]], cuya habilidad dice "During challenges, your characters deal damage with their Willpower instead of their Strength", y uno de mis personajes ya tiene daño marcado, ¿ese daño reduce la cantidad de daño que hará en el desafío?

Ejemplo: si mi personaje tiene 4 {W} y ya tiene 2 de daño, ¿hará 2 o 4 de daño durante el challenge?

---

## ✅ Respuesta

No. El daño recibido no reduce ni la Fuerza ni la Willpower del personaje. Con Dale, ese personaje hará daño usando su Willpower actual en lugar de su Strength, así que un personaje con 4 {W} y 2 de daño marcado sigue haciendo 4 de daño durante el challenge, salvo que otro efecto sí modifique su {W}.

El daño marcado solo se cuenta contra la Willpower para comprobar si el personaje es desterrado cuando se haga el game state check.

Esta misma lógica también aclara una duda relacionada: [[02. Listado de Cartas/Set 12 - Wilds Unknown#Dale - Ready for His Shot|Dale - Ready for His Shot]] no hace que tus personajes "tengan Fuerza igual a su Voluntad" ni cambia su característica de {S}. Solo cambia qué valor usan para hacer daño durante desafíos.

Por eso, Dale no altera efectos fuera del desafío que miran la Fuerza real de un personaje, como [[02. Listado de Cartas/Set 4 - Ursula's Return.md#Under the Sea|Under the Sea]], [[02. Listado de Cartas/Set 4 - Ursula's Return.md#Sisu - Empowered Sibling|Sisu - Empowered Sibling]] o [[02. Listado de Cartas/Set 10 - Whispers in the Well.md#The Headless Horseman - Terror of Sleepy Hollow|The Headless Horseman - Terror of Sleepy Hollow]]. Si un personaje tiene 1 {S} y 4 {W}, con Dale seguirá siendo un personaje de 1 {S} para esos efectos, aunque en un desafío haría 4 de daño.

---

## 📘 Fundamento en reglas

- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)#1.9.1. Definición|1.9.1. Definición]]
- [[01. Reglas/4. Acciones de turno (Turn Actions)/4.6 Desafío (Challenge)#4.6.6.1. Calcular daño|4.6.6.1. Calcular daño]]
- [[01. Reglas/1. Principios generales/1.8. Chequeo del estado del juego (Game State Check)#1.8.1.4. Daño sobre personajes o localizaciones|1.8.1.4. Daño sobre personajes o localizaciones]]

La combinación de estas reglas lleva a esta conclusión:

- El daño se representa con contadores de daño; no dice que reduzca características.
- En el paso de cálculo del daño del challenge solo se tienen en cuenta los efectos que modifiquen la característica relevante y el propio daño a infligir.
- La habilidad de Dale cambia qué característica usa tu personaje para hacer daño en el challenge: usa su Willpower en vez de su Strength.
- Eso no modifica la característica de Fuerza del personaje fuera de ese cálculo concreto.
- Por tanto, los efectos que preguntan por personajes con cierta {S} siguen usando la Fuerza normal del personaje, no su Willpower.
- El daño ya marcado no baja esa Willpower; solo hace que sea más fácil alcanzar el umbral para ser desterrado en el game state check.

---

## 🔄 Secuencia oficial

1. Se declara el desafío normalmente.
2. Al llegar a [[01. Reglas/4. Acciones de turno (Turn Actions)/4.6 Desafío (Challenge)#4.6.6.1. Calcular daño|4.6.6.1]], tus personajes usan su Willpower actual en lugar de su Strength por la habilidad estática de Dale.
3. El daño que ya tuviesen marcado no reduce ese valor; solo permanece como contadores sobre el personaje.
4. En [[01. Reglas/4. Acciones de turno (Turn Actions)/4.6 Desafío (Challenge)#4.6.6.2. Se hace el daño|4.6.6.2]], ambos personajes hacen daño simultáneamente.
5. En [[01. Reglas/4. Acciones de turno (Turn Actions)/4.6 Desafío (Challenge)#4.6.6.3. GSC|4.6.6.3]] se comprueba si el daño total acumulado es igual o superior a la Willpower del personaje.
6. Si lo es, se destierra según [[01. Reglas/1. Principios generales/1.8. Chequeo del estado del juego (Game State Check)#1.8.1.4. Daño sobre personajes o localizaciones|1.8.1.4]].
7. Si después otro efecto como [[02. Listado de Cartas/Set 4 - Ursula's Return.md#Under the Sea|Under the Sea]] o [[02. Listado de Cartas/Set 4 - Ursula's Return.md#Sisu - Empowered Sibling|Sisu - Empowered Sibling]] mira la Fuerza de ese personaje, seguirá viendo su {S} real, no la {W} usada por Dale durante el desafío.

---

## 🏷️ Tags

#dale #spikesuit #challenge #damage #willpower #strength #gsc #static-ability #under-the-sea #sisu #headless-horseman