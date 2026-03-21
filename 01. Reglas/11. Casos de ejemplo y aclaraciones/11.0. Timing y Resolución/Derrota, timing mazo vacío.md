# ❓ Duda

¿Pierdo por mazo vacío al iniciar mi turno sin cartas, durante el turno si necesito robar, o al finalizar mi turno?

# ✅ Respuesta

**La derrota por mazo vacío ocurre SOLO cuando finalizas tu turno con el mazo vacío.**

| Escenario | Resultado |
|-----------|-----------|
| **1. Inicias tu turno sin cartas en la biblioteca** | ✓ No pierdes. Continúas el turno normalmente. |
| **2. Durante tu turno: necesitas robar pero no hay cartas** | ✓ No pierdes. El robo simplemente no ocurre (no es acción ilegal). |
| **3. Terminas tu turno con la biblioteca vacía** | ✗ **PIERDES.** Este es el único momento de derrota. |

**Conclusión**: La derrota no se evalúa durante el turno, sino en el momento exacto de finalizarlo.

# 📘 Fundamento en reglas

[[1.12 Robo (Drawing)|Robo]] — Regula cómo se roban cartas y qué ocurre cuando no hay cartas disponibles.

[[1.6 Habilidades (Abilities)|Conceptos generales de evaluación de condiciones]] — Especifica cuándo se evalúan las condiciones de derrota.

[[1.8. Chequeo del estado del juego (Game State Check)|Game State Check]] — Define el proceso de verificación de condiciones de victoria/derrota al finalizar turno.

# 🔄 Secuencia

**Escenario 1: Inicias turno sin cartas**
1. Tu turno comienza
2. Tu mazo está vacío
3. Las acciones de turno se resuelven normalmente
4. **No hay verificación de derrota en este punto**
5. Continúas jugando

**Escenario 2: Necesitas robar durante turno sin cartas**
1. Un efecto dice "Draw 1" o la acción de turno es robar
2. Tu mazo está vacío
3. Intentas robar, pero no hay cartas
4. **El robo simplemente no ocurre** (no acción ilegal, no trigger que dependa del robo)
5. Continúas el turno

**Escenario 3: Finalizas turno con mazo vacío**
1. Ya no hay más acciones en tu turno
2. Verificación de condiciones de "finalización de turno"
3. Tu mazo está vacío
4. **Se detecta: Mazo vacío = Derrota**
5. Pierdes inmediatamente

# 🏷️ Tags

#defeat #empty-deck #end-of-turn #gameplay #timing
