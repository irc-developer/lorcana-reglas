## ❓ Duda

Tengo [Cursed Merfolk](https://cards.lorcast.io/card/digital/large/crd_25aa34175eeb4f30bbb9199f46040395.avif?1709690747) en juego (habilidad: *"Whenever this character is challenged, each opponent chooses and discards a card."*). Mi oponente desafía a Cursed Merfolk y recibe daño suficiente para ser desterrado (banished). También controlo [Emerald Chromicon](https://cards.lorcast.io/card/digital/large/crd_693273eeac4846a39a3539fc6ded617d.avif?1723917209) con habilidad *"During opponents' turns, whenever one of your characters is banished, you may return chosen character to their player's hand."*

**¿En qué orden se resuelven los triggers: primero descarte o primero retorno a mano?**

---

## ✅ Respuesta

**El descarte ocurre primero, luego se puede devolver a mano.**

Los disparadores **ocurren en momentos secuenciales distintos**, no simultáneamente:

### Análisis del timing:

**PRIMER TRIGGER - Cursed Merfolk:**
- Momento de disparo: **Mientras se resuelve el desafío**, antes de que el daño se aplique
- Oponente descarta una carta
    
2. Esa habilidad se dispara **durante el paso del desafío**, antes de que se resuelva el daño.
    
3. Por lo tanto, **la habilidad de Cursed Merfolk se resuelve primero**, obligando al oponente a descartar una carta.
    

Después de que el daño del desafío se aplique y el personaje sea desterrado, ocurre lo siguiente:

4. **Emerald Chromicon se dispara cuando el personaje es desterrado**.
    
5. En ese momento su habilidad se añade a la resolución y puede devolver un personaje a la mano.
    

Por tanto, **siempre se descarta primero y después puede ocurrir el “bounce” del Chromicon**.

---

#### Regla general relevante

Cuando **varios jugadores tienen habilidades disparadas al mismo tiempo**, se aplican en este orden:

1. **El jugador activo resuelve primero las habilidades que controla**, en el orden que prefiera.
    
2. Después **cada otro jugador resuelve las suyas**, también en el orden que prefiera.
    

Esto se debe a que las habilidades disparadas se añaden a la **bag** y se resuelven siguiendo el orden de prioridad de jugadores.

En el caso hipotético de que ambas habilidades **se disparasen al mismo tiempo**, el jugador activo resolvería primero las suyas y luego el oponente las suyas. Pero **en este ejemplo concreto no ocurre**, porque los disparadores son distintos.

---

## 📘 Referencias

- [[6.2. Habilidades Disparadas (Triggered Abilities)|6.2.3. Cuándo se cocinan los disparos]] – Los disparos se cocinan cuando su condición se cumple de forma secuencial.
- [[7.7. Bolsa (Bag)|7.7.4. Orden de resolución]] – En la bolsa, los disparos se resuelven en orden de prioridad de jugadores por cada disparo generado.
- [[4.6 Desafío (Challenge)|Declaración y resolución del desafío]] – Un desafío se resuelve: se compara fuerza/voluntad, se aplica daño, se desterran si corresponde.

---

## 🔄 Cómo se resuelve

1. El oponente declara un desafío legal contra Cursed Merfolk agotado; agota a su atacante.
2. Al ocurrir el desafío, se añade el disparo de Cursed Merfolk a la bolsa.
3. Antes del daño, se resuelve la bolsa de la declaración. Cada oponente de su controlador elige y descarta una carta.
4. Se hace el daño simultáneo del desafío y después el chequeo de estado. Si Cursed Merfolk tiene daño letal, queda desterrado.
5. Emerald Chromicon se dispara por ese destierro durante el turno rival. Tras completar los chequeos, su controlador puede resolverlo para devolver un personaje elegido legal.
6. Se completa la bolsa restante y termina el desafío.

---

## 🏷️ Tags

#triggered-ability #timing #banish #discard #bag #resolution
