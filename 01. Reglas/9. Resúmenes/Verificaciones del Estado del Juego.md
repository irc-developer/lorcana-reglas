La verificación del estado del juego es un proceso automático que el juego realiza para comprobar un conjunto de condiciones específicas y ejecutar las *acciones requeridas* cuando se cumplen una o más de esas condiciones [CR-1.9.1, CR-351].

## **¿Cuándo se realiza una verificación del estado del juego?** [CR-1.9.2, CR-352]:

La verificación del estado del juego se realiza en los siguientes momentos clave:

- **Al final de cada paso** del turno.
- **Después de que cualquier acción o habilidad haya terminado de resolverse.**
- **Después de que cada efecto en la bolsa (bag) haya terminado de resolverse.**

## **Condiciones que evalúan una verificación del estado del juego** [CR-1.9.1, CR-351-352]:

- Si un jugador tiene **20 o más puntos de lore**, ese jugador gana la partida [CR-1.9.1.1, CR-352].
- Si un jugador intentó robar de un mazo sin cartas **desde la última verificación del estado del juego**, ese jugador **pierde la partida** [CR-1.9.1.2, CR-352].
- Si un **personaje o ubicación tiene daño igual o superior a su Voluntad ({W})**, ese personaje o ubicación es **desterrado** [CR-1.9.1.3, CR-352]. Se considera que un personaje desterró a otro personaje o ubicación si el destierro fue resultado de daño infligido en un desafío o por una habilidad de personaje como, por ejemplo, mover daños, [CR-1.9.1.3, CR-186].

### **Proceso de la verificación del estado del juego** [CR-1.9.2, CR-352-353]:

Durante una verificación del estado del juego, se sigue este orden:

1. Primero, se comprueban y completan todas las **condiciones de victoria y derrota** y las acciones requeridas.
2. Si no se cumplen condiciones de victoria o derrota, se comprueban y completan todas las demás condiciones y acciones requeridas (como el destierro de personajes/ubicaciones por daño).
3. Una vez que se completan todas las acciones requeridas, **la verificación del estado del juego se repite** hasta que no haya más acciones requeridas que completar [CR-1.9.3, CR-188].
4. Las habilidades disparadas que ocurrieron durante este proceso se añaden a la bolsa para resolverse **después** de que la verificación del estado del juego y todas las acciones requeridas hayan finalizado por completo [CR-1.9.2, CR-1.9.4, CR-187-188] como, por ejemplo, las que dependen de desterrar un personaje.
5. Cualquier acción requerida generada por una verificación del estado del juego ocurre en el **orden de turno** [CR-1.9.2.1, CR-188]. Si un jugador ganaría y perdería al mismo tiempo debido a la misma verificación, ese jugador gana la partida [CR-1.9.2.1, CR-188]. Si varias acciones requeridas ocurren a la vez, se consideran una única acción combinada que sucede simultáneamente [CR-1.9.5, CR-188-189].
