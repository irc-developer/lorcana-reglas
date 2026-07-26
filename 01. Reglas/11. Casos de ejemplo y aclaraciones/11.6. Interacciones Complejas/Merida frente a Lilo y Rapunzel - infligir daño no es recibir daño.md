## ❓ Duda

Si una acción intenta infligir daño a un personaje protegido por [[02. Listado de Cartas/Set 11 - Winterspell.md#Lilo - Bundled Up|Lilo - Bundled Up]] o por [[02. Listado de Cartas/Set 10 - Whispers in the Well.md#Rapunzel - Ready for Adventure|Rapunzel - Ready for Adventure]], ese personaje no recibe el daño.

¿Se dispara aun así **STEADY AIM** de [[02. Listado de Cartas/Set 12 - Wilds Unknown.md#Merida - Formidable Archer|Merida - Formidable Archer]]?

---

## ✅ Respuesta

**Sí. Merida se dispara tanto frente a la protección de Lilo como frente a la de Rapunzel.**

Las reglas actuales separan dos hechos:

1. El daño que **inflige la fuente** (*damage dealt by the source*).
2. El daño que **recibe la carta afectada** (*damage taken by the affected card*).

Los efectos de reemplazo de Lilo y Rapunzel modifican el segundo hecho: el personaje protegido **no recibe daño**. No reemplazan el hecho de que la acción fue la fuente que **infligió daño**.

Por tanto, la condición de STEADY AIM se cumple:

> “Whenever one of your actions **deals damage** to an opposing character [...]”

La habilidad de Merida se añade a la bolsa y, cuando se resuelva, intentará infligir 2 daños a ese mismo personaje.

---

## 🧠 La distinción decisiva: la fuente y el receptor

En lenguaje cotidiano solemos tratar estas dos frases como equivalentes:

- «La acción inflige 3 daños».
- «El personaje recibe 3 daños».

Mecánicamente no tienen por qué producir el mismo valor. Una fuente puede seguir contando como que ha infligido daño aunque un modificador o un efecto de reemplazo haga que el personaje no reciba ninguno.

La regla [[01. Reglas/1. Principios generales/1.9. Daño (Damage)#1.9.5. Daño reducido a 0|1.9.5]] lo muestra expresamente para el daño reducido a 0: la fuente continúa considerándose que ha infligido daño, pero la carta afectada no lo recibe. Los efectos de Lilo y Rapunzel no son reducciones de daño, pero aplican la misma separación funcional: reemplazan el daño que recibiría la carta, no el daño originado por la acción.

Esto también explica por qué la regla [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.5. Efectos de Reemplazo (Replacement Effects)#6.5.4. Qué pasa cuando es reemplazado|6.5.4]] no impide el disparo de Merida. El hecho reemplazado —que el personaje reciba el daño— no sucede. En su lugar ocurre un evento modificado en el que:

- la acción sigue siendo una fuente que ha infligido daño; y
- el personaje protegido no recibe ese daño.

STEADY AIM observa el primer hecho, no el segundo.

---

## 🔄 Secuencia con Lilo - Bundled Up

Supongamos que un jugador controla a Merida y juega una acción que inflige 3 daños a la Lilo rival. Es la primera vez durante ese turno que Lilo fuera a recibir daño.

1. Se calcula el daño de la acción.
2. La acción va a infligir daño a Lilo.
3. **EXTRA LAYERS** reemplaza la primera vez que Lilo fuera a recibirlo.
4. La acción sigue contando como que ha infligido daño, pero Lilo recibe **0**.
5. La protección de Lilo queda utilizada para ese turno.
6. STEADY AIM se dispara y se añade a la bolsa.
7. Una vez resuelta completamente la acción, se resuelve STEADY AIM.
8. Merida intenta infligir 2 daños a Lilo.
9. Como EXTRA LAYERS ya se utilizó, Lilo recibe normalmente esos 2 daños, salvo que otro modificador o reemplazo se lo impida.

### Resultado

- Daño recibido por Lilo de la acción: **0**.
- Daño posterior de STEADY AIM: normalmente **2**.
- STEADY AIM no vuelve a dispararse por sus propios 2 daños, porque esos daños proceden de la habilidad de Merida, no de una acción.

---

## 🔄 Secuencia con Rapunzel - Ready for Adventure

Ahora el personaje rival tiene una protección creada por **ACT OF KINDNESS**:

> “The next time they would be dealt damage they take no damage instead.”

La secuencia práctica es la misma:

1. La acción va a infligir daño al personaje protegido.
2. ACT OF KINDNESS reemplaza el daño que ese personaje fuera a recibir.
3. La acción sigue contando como que ha infligido daño, pero el personaje recibe **0**.
4. La protección de Rapunzel queda consumida.
5. STEADY AIM se dispara.
6. Cuando STEADY AIM intenta infligir 2 daños, la protección ya no está disponible y el personaje normalmente recibe esos 2.

Rapunzel no contradice el caso de Lilo. La diferencia entre ambas protecciones está en **qué formas de colocar daño pueden interceptar**, no en si Merida se dispara.

---

## 🔎 «Daño infligido por» frente a «daño infligido a»

La redacción de Rapunzel puede parecer más problemática porque su condición dice **would be dealt damage**, mientras que Lilo dice **would take damage**. Sin embargo, eso no cambia la comprobación que hace Merida:

- Rapunzel observa el daño que fuera a ser **infligido al personaje protegido**.
- Merida observa el daño **infligido por la acción**.

ACT OF KINDNESS reemplaza el lado receptor: el personaje no recibe el daño que iba a serle infligido. El valor del daño originado por la acción —el que consulta STEADY AIM— no queda reemplazado.

El ejemplo de Rapunzel incluido en la regla 6.5.8 describe el evento modificado desde el punto de vista del personaje protegido: el personaje rival no le hace daño. Su finalidad es explicar qué ocurre con varias instancias idénticas de ACT OF KINDNESS. No convierte el reemplazo en una anulación del hecho separado de que la acción que inició el evento haya infligido daño a efectos de habilidades como STEADY AIM.

> [!IMPORTANT] Regla práctica
> «La acción ha infligido daño» y «el personaje ha recibido daño» son comprobaciones distintas. Lilo y Rapunzel pueden hacer falsa la segunda sin hacer falsa la primera.

---

## 🆚 Lilo y Rapunzel no protegen exactamente de lo mismo

| Operación que colocaría daño | ¿Lilo la reemplaza? | ¿Rapunzel la reemplaza? | ¿Puede disparar a Merida? |
|---|---:|---:|---:|
| Una acción **inflige** daño (*deal*) | Sí | Sí | Sí |
| Una habilidad **inflige** daño (*deal*) | Sí | Sí | No, porque no es una acción |
| Una acción **pone** daño (*put*) | Sí | No | No, porque poner no es infligir |
| Una acción **mueve** daño (*move*) | Sí | No | No, porque mover no es infligir |

La protección de Lilo usa **take damage**, el concepto general que comprende cualquier daño colocado sobre ella. Por eso puede reemplazar daño infligido, puesto o movido.

La protección de Rapunzel usa **would be dealt damage**, de modo que solo interviene ante daño que fuera a ser **infligido**. Esto incluye tanto el daño de un desafío como el de un efecto que diga *deal damage*. No está limitada a los desafíos.

---

## 🛡️ ¿Qué ocurre si también hay Resist?

Los modificadores de daño se aplican antes que los efectos de reemplazo.

### Resist reduce el daño a 0

- La fuente sigue considerándose que ha infligido daño conforme a 1.9.5.
- El personaje no fuera a recibir daño.
- La protección de Lilo o Rapunzel no necesita aplicarse y se conserva.
- STEADY AIM se dispara si la fuente era una acción.
- Cuando STEADY AIM intente infligir sus 2 daños, la protección aún disponible podrá reemplazar ese nuevo daño si, después de aplicar Resist, quedara al menos 1.

### Resist deja al menos 1 daño

- El personaje todavía fuera a recibir daño.
- La protección aplicable de Lilo o Rapunzel reemplaza ese daño y se consume.
- La acción continúa contando como que ha infligido daño.
- STEADY AIM se dispara.
- Los 2 daños posteriores constituyen un evento independiente y vuelven a verse afectados por Resist.

---

## ⚠️ Errores frecuentes

### «Si el personaje recibe 0, la acción no ha infligido daño»

Incorrecto con las CR 2.2. El daño infligido por la fuente y el daño recibido por la carta se comprueban por separado.

### «La regla 6.5.4 elimina todo el evento de la acción»

No necesariamente. Un efecto puede quedar reemplazado solo parcialmente. Lilo y Rapunzel sustituyen el resultado que afectaría al receptor, mientras el evento modificado conserva a la acción como fuente del daño.

### «Rapunzel solo protege durante desafíos»

Incorrecto. *Deal damage* comprende el daño de los desafíos y el de los efectos que expresamente infligen daño.

### «Los 2 daños de Merida son una ampliación de los daños de la acción»

Incorrecto. STEADY AIM crea una habilidad disparada y un nuevo evento de daño. Resist y los efectos de reemplazo se vuelven a evaluar cuando esa habilidad se resuelve.

---

## 📘 Fundamento en reglas

- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)|1.9. Daño]]: distingue infligir, poner, mover y recibir daño.
- [[01. Reglas/1. Principios generales/1.9. Daño (Damage)#1.9.5. Daño reducido a 0|1.9.5]]: una fuente puede seguir considerándose que ha infligido daño aunque el receptor no reciba ninguno.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.5. Efectos de Reemplazo (Replacement Effects)|6.5. Efectos de reemplazo]]: el evento original es sustituido por un evento modificado, que sí puede disparar habilidades.
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de cartas y efectos (Resolving Cards and Effects)|6.7.2. Resolución de efectos]]: primero se calcula el daño, después se ejecutan las instrucciones y se aplican los reemplazos.
- [[01. Reglas/8. Palabras clave (Keywords)/8.8. Resistir (Resist)|8.8. Resist]]: Resist modifica el daño infligido, pero la fuente sigue considerándose que lo inflige si queda reducido a 0.
- [Disney Lorcana Comprehensive Rules 2.2.0](https://files.disneylorcana.com/Comprehensive-Rules_2.2.0-EN.pdf), vigentes desde el 9 de julio de 2026.

> [!NOTE] Alcance de la conclusión
> La aplicación concreta a Lilo, Rapunzel y Merida se obtiene combinando el texto actualizado de las cartas con la separación entre daño infligido por la fuente y daño recibido por la carta que establecen las CR 2.2.

---

## 🏷️ Tags

#merida #lilo #rapunzel #steady-aim #extra-layers #act-of-kindness #deal-damage #take-damage #put-damage #move-damage #replacement-effect #resist #damage #triggered-ability #bag #cr-2-2
