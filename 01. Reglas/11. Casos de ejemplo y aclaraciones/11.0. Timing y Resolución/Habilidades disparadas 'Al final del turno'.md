## ❓ Duda

¿Una habilidad que se dispara al final del turno vuelve a dispararse si, durante esa misma fase, otra habilidad cambia el estado que la habilidad comprueba?

---

## ✅ Respuesta

**No.** Una habilidad disparada al final del turno se añade a la bolsa una vez cuando se cumple su condición de disparo. Si además tiene una condición secundaria, esa condición se comprueba al resolverla.

Por ejemplo, [[02. Listado de Cartas/Set 5 - Shimmering Skies.md#Clarabelle - Light on Her Hooves|Clarabelle - Light on Her Hooves]] entra en la bolsa al final del turno aunque tenga el mismo número de cartas que el oponente. Si al resolverla sigue empatada, no roba. Si otra habilidad cambia después el tamaño de las manos, Clarabelle no vuelve a entrar en la bolsa.

Esto no impide que otras habilidades distintas se disparen por los eventos que ocurran durante la resolución; simplemente no crea una segunda instancia de la misma condición de final de turno.

---

## 📘 Fundamento en reglas

- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.2. Habilidades Disparadas (Triggered Abilities)#6.2.1. Definición|6.2.1. Definición]]: una instancia se dispara por cada vez que se cumple su condición.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.2. Habilidades Disparadas (Triggered Abilities)#6.2.4. Estructura Condicional 1, si Condicional 2, efecto|6.2.4. Condición secundaria]]: la condición secundaria se verifica al resolver.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)#6.7.4. Habilidades disparadas durante la resolución|6.7.4. Habilidades durante la resolución]]: los disparos nuevos esperan en la bolsa, pero son eventos nuevos.
- [[Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf|Comprehensive Rules 2.2.0]], reglas 6.2.1, 6.2.4 y 7.7.3.

---

## 🔄 Secuencia oficial

1. Comienza el final del turno y se comprueban las condiciones de disparo.
2. Clarabelle se añade a la bolsa, sin comprobar todavía la diferencia de cartas.
3. Se resuelven las habilidades en el orden correspondiente.
4. Al resolver Clarabelle, se comprueba la condición secundaria con el número actual de cartas.
5. Si es falsa, esa instancia se resuelve sin efecto.
6. Cambios posteriores no reabren la condición de final de turno.

---

## 🏷️ Tags

#end-of-turn #triggered-ability #bag-priority #timing #resolution
