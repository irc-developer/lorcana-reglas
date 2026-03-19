## ❓ Duda

¿Puedo evitar la restricción de "Do your worst" de [[Cartas de Lorcana#John Smith - Undaunted Protector|John Smith - Undaunted Protector]] jugando un efecto que dice "elige hasta X personajes" (choose up to X characters) e ignorando a John Smith?

---

## ✅ Respuesta

No. La restricción de "Do your worst" **SÍ aplica incluso en efectos de "choose up to X"**.

Si la estructura es "elige hasta N personajes":
- "Hasta" incluye 0 como opción válida
- Puedes elegir 0, 1, 2, ... hasta N personajes
- **PERO la restricción estática de John Smith obliga a incluirlo en la selección si es posible**

Por ejemplo, si juegas "elige hasta 3 personajes": 
- Las opciones legales son: elegir 0, 1, 2 o 3 personajes
- Si John Smith es un objetivo válido, DEBE incluirse
- La cantidad mínima sigue siendo 1 (John Smith), la máxima sigue siendo 3

**La restricción no es derrotada por "choose up to".**

La restricción "Do your worst" es **incondicional en el contexto de elección válida**: mientras haya una opción legal que sea John Smith, debe elegirse.

---

## 📘 Fundamento en reglas

**Diferencia: "Choose X" vs "Choose up to X"**

- **"Choose X"** = Debes elegir exactamente X objetivos. No es opcional.
- **"Choose up to X"** = Puedes elegir 0 hasta X objetivos. Es flexible en cantidad.

**PERO ambas están sujetas a restricciones estáticas.**

La regla oficial (6.1.3) especifica:
_"Si un efecto permite elegir 'hasta N' (up to N): No se puede elegir el mismo objetivo más de una vez. 'Hasta' incluye 0 como elección válida."_

Lo que la regla NO dice es que "hasta" permite evadir restricciones de elección. Las restricciones estáticas prevalecen.

**Ejemplo análogo - Ward:**

Ward dice: "Your opponents can't choose this card when resolving an effect."

Si juegas un efecto "elige hasta 3 cartas de tu mano" y un oponente controla una carta con Ward:
- El oponente **no puede elegir** la carta con Ward
- Pero sigue pudiendo elegir "hasta 3" cartas (las que no tienen Ward)

Del mismo modo, "Do your worst" impone una **restricción positiva** (must choose) que prevalece sobre la flexibilidad de "choose up to X".

**Base normativa:**
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.1. General (General)#6.1.3. Todas las elecciones (choices) se realizan durante la resolución del efecto|6.1.3. Elecciones: "up to N"]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.4. Habilidades Estáticas (Static Abilities)#Restricciones de elección|6.4. Restricciones estáticas de elección]]

---

## 🔄 Secuencia oficial

1. **Efecto activado**: Se juega un efecto que dice "elige hasta 3 personajes".
2. **Opciones legales**: Los personajes en juego son: John Smith, Otro A, Otro B. Todos son objetivos válidos.
3. **Restricción evaluada**: "Do your worst" crea una restricción **positiva** (must choose John Smith if able). Lo opuesto a Ward (can't choose).
4. **Elección obligatoria**: El jugador DEBE incluir a John Smith. Luego puede elegir 0-2 personajes adicionales (máximo 3 total).
5. **Resolución**: El efecto se resuelve con John Smith **incluido obligatoriamente**.
6. **GSC**: Se verifica estado del juego.

---

## 🏷️ Tags

#up-to-N #static-ability #restriction #positive-restriction #must-choose #do-your-worst
