### Pregunta
Si **Lilo - Bundled Up** 

**_EXTRA LAYERS** During each opponent's turn, the first time this character would take damage, she takes no damage instead._

tiene **Resist +2**, y luego:
- Es objetivo de [[Cartas de Lorcana#Fire The Cannons!|Fire the Cannons!]].
- Es desafiada por **[[Cartas de Lorcana#Flounder - Voice Of Reason|Flounder - Voice Of Reason]]**.

¿Se aplica primero el efecto de “escudo” (replacement/prevent) o el **[[8.8. Resistir (Resist)|Resist]]**?  
En concreto: ¿se dispara el “escudo” con el daño del action pero no con el del challenge?
### Respuesta
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

