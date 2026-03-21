## ❓ Duda

Colors of the Wind dice "Each player reveals the top card of their deck. Draw a card for each different ink type of cards revealed this way."

- ¿Se resuelve todo el efecto de golpe o por partes?
- ¿El robo ocurre como un único evento o múltiples?
- ¿Cuándo se disparan triggers durante el robo?

---

## ✅ Respuesta

**Pregunta 1: ¿Se resuelve todo el efecto de golpe o por partes?**

El efecto se resuelve en **dos pasos secuenciales dentro de una única resolución**:

1. **Paso 1 (Simultáneo)**: Todos los jugadores revelan la carta superior de su mazo al mismo tiempo
2. **Paso 2 (Resolución)**: Se cuenta el número de tipos de tinta diferentes entre TODAS las cartas reveladas, y el que jugó la carta roba esa cantidad de cartas

**NO se resuelve "de golpe"**: hay que completar Paso 1 antes de Paso 2.

---

**Pregunta 2: ¿El robo ocurre como un único evento o múltiples?**

El robo ocurre como **X eventos individuales separados**. Aunque dice "Draw a card for each different ink type", esto significa:
- Cuentas X tipos de tinta diferentes
- Robas X cartas como **X actos separados de robo**, uno por cada carta
- Cada robo es un evento completo y individual

**Regla oficial (CR 1.12.2):** "Las cartas se roban de una en una. Si un efecto dice que robes varias, se roban en orden, una tras otra."

**Ejemplo**: Si se revelan 3 tipos de tinta (Amber, Ruby, Emerald), robas 3 cartas EN 3 EVENTOS DE ROBO SEPARADOS, no como 1 evento de robo unitario.

---

**Pregunta 3: ¿Cuándo se disparan triggers durante el robo?**

Los triggers que monitorean "whenever you draw" se disparan **una vez POR CADA CARTA ROBADA**, porque cada carta robada es un evento de robo individual y completo.

**Secuencia completa**:
1. Revelan cartas
2. Se resuelve el robo: **Carta 1 es robada (evento 1)**
3. **Triggers de "whenever you draw" se disparan POR CARTA 1**
4. **Carta 2 es robada (evento 2)**
5. **Triggers de "whenever you draw" se disparan POR CARTA 2**
6. **Carta 3 es robada (evento 3)**
7. **Triggers de "whenever you draw" se disparan POR CARTA 3**

---

## 📘 Fundamento

**Criterio: Eventos de Robo Individuales**

De [[01. Reglas/1. Principios generales/1.12 Robo (Drawing)|1.12. Robo]]:

- **Cada carta se roba individualmente**: "Las cartas se roban de una en una. Si un efecto dice que robes varias, se roban en orden, una tras otra."
- **Cada robo es un evento completo**: "Si una carta o efecto hace robar varias cartas, **cada carta se roba y se resuelve de forma individual**, siguiendo el mismo procedimiento."
- **Los triggers se disparan por cada evento**: "Abilities that trigger when a card is drawn are added to the bag after the draw is completed" — esto ocurre por CADA carta robada, no por el lote completo.

**Structure de Colors of the Wind**:

El efecto tiene estructura explícita con dos pasos:
1. "Each player reveals" = acción de revelación (simultánea, NO robo)
2. "Draw a card for each" = cálculo de cantidad (X) + resolución de X eventos de robo individuales

**Diferencia con "Draw all at once" vs "Draw one by one"**:

En Lorcana, "Draw X cards" SIEMPRE es "uno por uno", no "todos a la vez":

❌ INCORRECTO: "Robas 3 cartas como 1 evento"

✅ CORRECTO: "Robas 3 cartas = 3 eventos de robo individuales que se resuelven uno tras otro"

**Consecuencia para Color of the Wind**:

Colors of the Wind calcula X (número de tipos de tinta), luego roba esas X cartas de forma individual = **X eventos de robo separados** = **X disparos de "whenever you draw"**

**Caso de uso real: Jafar – Striking Illusionist**

En el GSC case histórico:
- Jafar tiene "Gain 1 lore whenever you draw a card"
- Efecto roba 3 cartas
- Resultado: trigger dispara 3 veces → **ganas 3 lore** (no 1)

---

## 🔄 Secuencia

**Escenario: 3 jugadores revelan cartas con tinta Amber, Ruby, Emerald + tienes "Whenever you draw, gain 1 lore"**

1. **Acción Principal**: Se juega Colors of the Wind
2. **Paso 1 - Revelación Simultánea**:
   - Jugador A revela: Cinderella (Sapphire)
   - Jugador B revela: Aurora (Ruby)
   - Jugador C revela: Mulan (Amber)
3. **Conteo de Tipos de Tinta**: Sapphire, Ruby, Amber = **3 tipos diferentes**
4. **Paso 2 - Robo Individual 1**:
   - Robas la 1ª carta de tu mazo (evento de robo 1)
   - Trigger se añade a la bolsa
5. **Paso 2 - Robo Individual 2**:
   - Robas la 2ª carta de tu mazo (evento de robo 2)
   - Trigger se añade a la bolsa
6. **Paso 2 - Robo Individual 3**:
   - Robas la 3ª carta de tu mazo (evento de robo 3)
   - Trigger se añade a la bolsa
7. **Resolución de Triggers desde la Bolsa**:
   - Trigger 1: Ganas 1 lore
   - Trigger 2: Ganas 1 lore
   - Trigger 3: Ganas 1 lore
   - **Total: ganas 3 lore**

**Contraste incorrecto (para evitar confusión)**:

❌ FALSO: "Triggers se disparan una sola vez porque es un único efecto"

✅ CORRECTO: "Triggers se disparan 3 veces porque hay 3 eventos de robo individuales, aunque procedan del mismo efecto"

**Caso comparativo: Multiple Effects vs Multiple Robberies**:

Si en tuRN los siguiente ocurre:
- Efecto A: "Draw a card" (evento 1)
- Efecto B: "Draw a card" (evento 2)
- Tienes: "Whenever you draw, gain 1 lore"

Resultado: ganas 2 lore (1 por cada evento)

Colors of the Wind con 3 tipos tinta:
- Un efecto: "Draw a card for each different ink type"
- Resultado: roba 3 cartas = 3 eventos = **ganas 3 lore**

No hay diferencia en cómo se cuentan los disparos.

---

## 🏷️ Tags

#multiple-draws #event-resolution #triggered-abilities #timing #draw-mechanics #single-event #colors-of-the-wind

