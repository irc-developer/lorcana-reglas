## ❓ Duda

¿Cuál tiene prioridad al resolver daño: un efecto de reemplazo (escudo de una carta) o una reducción de daño (Resist keyword)?

## ✅ Respuesta

- **[[Cartas de Lorcana#Fire The Cannons!|Fire the Cannons!]]** genera un evento de “deal damage”.  
  Los **[[6.5. Efectos de Reemplazo (Replacement Effects)|Efectos de Reemplazo]]** se aplican cuando el evento *iba a ocurrir* y lo reemplazan antes de que el daño sea **hecho**.  
  Por eso, si el “escudo” de Lilo reemplaza/previene el daño, el daño nunca se llega a “hecho” y **Resist no llega a importar**.

- **[[4.6 Desafío (Challenge)#4.6.6.1. Calcular daño|Desafío: en el paso de daño]]**, primero se **calcula** el daño con modificadores (como **Resist**) y luego el daño se **hace** simultáneamente.  
  Si el reemplazo de Lilo reemplaza/previenen el daño “que fuera a ser hecho”, este se aplica **antes** de que el daño se coloque.  
  *Resultado*: el daño del challenge se calcula con Resist; si el efecto de reemplazo lo reemplaza/previene, entonces **no se considera que se haya hecho** (y el “escudo” no queda “gastado” antes).

### Conclusión rápida

- **Fire the Cannons!**→ el “escudo” se aplica primero, **Resist no entra**.
- **Desafío** → **Resist se aplica primero**; el “escudo” solo se aplica si aún queda daño por infligir.
- La interacción con resist es aplicable también a habilidades como las de [[Cartas de Lorcana#Rapunzel - Ready for Adventure|Rapunzel - Ready for Adventure]] y [[Cartas de Lorcana#Hercules - Mighty Leader|Hercules - Mighty Leader]] en lo que refiere a perder el escudo si tienen resist.
#Resist #Replacement-Effect #challenge

---

## 📘 Fundamento en reglas

- [[1.9. DaÃƒ±o (Damage)#1.9.1.5. Take|take]]
- [[8.8. Resistir (Resist)|Resist]]
- [[6.5. Efectos de Reemplazo (Replacement Effects)|Efectos de Reemplazo]]
- [[4.6 DesafÃƒ­o (Challenge)#4.6.6.1. Calcular daÃƒ±o|DesafÃƒ­o: en el paso de daÃƒ±o]]
- ---

---

## 🔄 Secuencia oficial

1. **Coste**: determinar el coste de la acción o habilidad que inicia la jugada.
2. **Objetivos**: fijar objetivos legales según el texto.
3. **Resolución**: resolver el texto en orden.
4. **Disparos**: añadir a la bolsa los triggers generados y resolver por prioridad.
5. **GSC**: realizar chequeo del estado del juego tras cada resolución.

---

## 🏷️ Tags

#replacement-effects #resist #damage #priority