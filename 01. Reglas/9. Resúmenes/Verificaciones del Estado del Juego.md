# Verificaciones del estado del juego

Una verificación del estado del juego (*game state check*) es el proceso automático de la regla 1.8 que comprueba condiciones concretas y aplica sus resultados.

## Cuándo se realiza

La regla 1.8.1 ordena comprobar el estado:

- al final de cada paso de la fase inicial del turno;
- después de la declaración y del daño de un desafío;
- después de completar cada acción de turno;
- después de que se resuelvan todos los efectos de una acción o habilidad;
- cuando termina el turno.

## Condiciones

- **1.8.1.1:** un jugador con 20 o más puntos de lore gana la partida.
- **1.8.1.2:** si el turno de un jugador termina sin cartas en su mazo, pierde la partida.
- **1.8.1.3:** en multijugador, el último jugador que permanece en la partida gana.
- **1.8.1.4:** un personaje o una localización con daño igual o superior a su Voluntad {W} es desterrado.

Un personaje o una localización desterrados por daño de un personaje en un desafío, o por la habilidad de un personaje desde la última verificación, se consideran desterrados por ese personaje.

## Proceso

1. Se aplican simultáneamente todos los resultados que corresponden al mismo jugador; si afectan a varios jugadores, se aplican en orden de turno (1.8.4).
2. Las habilidades que se disparan por la verificación se añaden a la bolsa, pero no se resuelven todavía (1.8.2).
3. La verificación se repite inmediatamente (1.8.3).
4. Cuando ninguna condición se cumple, se resuelven las habilidades de la bolsa. Después se comprueba otra vez el estado antes de continuar.

Una condición solo produce su resultado si sigue cumpliéndose cuando ocurre la verificación (1.8.5). Si durante la resolución un personaje alcanza daño letal, pero antes de terminar el efecto ese daño se mueve o se retira, no es desterrado por esa condición.

> [!NOTE] Error del PDF oficial
> El ejemplo B de 1.8.3 remite a la inexistente 1.8.1.5 para una localización. La regla correcta es 1.8.1.4, que reúne personajes y localizaciones.

#game-state-check #bag #banish #win #lose
