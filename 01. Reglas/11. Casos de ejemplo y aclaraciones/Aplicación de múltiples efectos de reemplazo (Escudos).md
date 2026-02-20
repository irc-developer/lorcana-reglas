Cuando un personaje tiene **varios efectos de reemplazo aplicables al mismo evento de daño**, el controlador del personaje afectado decide cuál aplicar primero.

Ejemplo típico:

- Un efecto reemplaza el daño que el personaje **recibiría**.
- Otro efecto reemplaza el daño que el personaje **haría**.

Ambos son **efectos de reemplazo** según las reglas en la [[6.5. Efectos de Reemplazo (Replacement Effects)||sección de 6.5 - Efectos de Reemplazo]].

---
## Procedimiento cuando hay varios efectos aplicables

Si varios efectos de reemplazo pueden aplicarse al mismo evento:

1. Se identifica el evento original  
   > Ej: “Este personaje va a recibir 3 de daño”.

2. Se determinan todos los efectos de reemplazo aplicables.

3. El controlador del personaje afectado elige cuál aplicar primero.

4. El evento se modifica.

5. Se comprueba si algún otro efecto sigue siendo aplicable al nuevo evento.

6. Se repite el proceso hasta que ningún efecto pueda aplicarse.

Este marco deriva de la estructura general de resolución de efectos en [[6.5. Efectos de Reemplazo (Replacement Effects)|sección de 6.5 - Efectos de Reemplazo]] y [[6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)|sección de 6.7 - Resolución de Cartas y Efectos]].

---

##  Aplicación práctica

### Escenario: aplicar primero el efecto que evita el daño

Evento original:
> “El personaje recibe 3 de daño”.

Se aplica el efecto que reemplaza ese daño por:
> “El personaje no recibe daño”.

Ahora:

- El evento de daño ya no existe.
- Se revisa si el otro efecto puede aplicarse.
- Como ya no hay daño que modificar, no puede aplicarse.

Resultado: solo se aplicó un efecto.

## Importante: no se “activan”

Evita usar el término *activar*. Los efectos de reemplazo:

- ❌ No se activan.
- ❌ No usan la bolsa.
- ❌ No generan un evento posterior.
- ✅ Modifican el evento directamente antes de que ocurra.

---
### Regla práctica

> Si un efecto convierte el daño en 0 o lo elimina completamente, los demás efectos que modifican ese daño dejan de ser aplicables.