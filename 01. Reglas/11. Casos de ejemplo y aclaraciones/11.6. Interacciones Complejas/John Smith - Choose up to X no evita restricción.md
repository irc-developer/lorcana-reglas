## ❓ Duda

¿Puedo evitar la restricción de "Do your worst" de [John Smith - Undaunted Protector](https://cards.lorcast.io/card/digital/large/crd_26b1e9d58acf429aa2d77f89f6534c16.avif?1770260064) jugando un efecto que dice "elige hasta X personajes" (choose up to X characters) e ignorando a John Smith?

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

## 📘 Referencias

**Diferencia: "Choose X" vs "Choose up to X"**

- **"Choose X"** = Debes elegir exactamente X objetivos. No es opcional.
- **"Choose up to X"** = Puedes elegir 0 hasta X objetivos. Es flexible en cantidad.

**PERO ambas están sujetas a restricciones estáticas.**

La regla oficial (6.1.3) especifica:
_"Si un efecto permite elegir 'hasta N' (up to N): No se puede elegir el mismo objetivo más de una vez. 'Hasta' incluye 0 como elección válida."_

Lo que la regla NO dice es que "hasta" permite evadir restricciones de elección. Las restricciones estáticas prevalecen.

Una prohibición como Ward puede volver ilegal elegir a John Smith. «If able» exige que cumpla todos los requisitos y no elimina prohibiciones. Ward en juego no afecta a cartas de personaje que estén en una mano o descarte.

**Base normativa:**
- [[6.1. General (General)|6.1.3. Elecciones: "up to N"]]
- [[6.4. Habilidades Estáticas (Static Abilities)|6.4. Restricciones estáticas de elección]]

---

## 🏷️ Tags

#static-ability #restriction
