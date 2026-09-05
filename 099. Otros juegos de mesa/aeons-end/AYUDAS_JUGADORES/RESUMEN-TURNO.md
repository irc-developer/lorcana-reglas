# Aeon's End — Resumen de turno

**Edición**: primera edición, juego base de 2016  
**Uso**: consulta rápida durante la partida  
**Documento completo**: [Aeons-End.md](../Aeons-End.md)  
**Última validación**: 10/08/2026

---

## Victoria y derrota

**Victoria inmediata si:**

- la némesis llega a 0 de vida; o
- el mazo de némesis está vacío y no quedan minions ni poderes en juego.

**Derrota inmediata si:**

- Gravehold llega a 0 de vida;
- todos los jugadores están agotados; o
- se cumple una condición específica del tablero de la némesis.

---

## Orden de turno

Después de cada turno, revela una carta del mazo de orden:

| Jugadores | Cartas |
|-----------|--------|
| Solitario verdadero | 3 jugador + 2 némesis |
| 2 | J1 ×2, J2 ×2, némesis ×2 |
| 3 | J1, J2, J3, comodín, némesis ×2 |
| 4 | J1, J2, J3, J4, némesis ×2 |

Cuando se agota, baraja el descarte de orden para formar un nuevo mazo.

---

## Turno de jugador

### 1. Fase de lanzamiento

- Lanza opcionalmente los hechizos de brechas abiertas.
- Lanza obligatoriamente todos los hechizos de brechas cerradas.
- Elige el orden de lanzamiento.
- Descarta cada hechizo antes de resolver su `Cast:`.
- Una brecha abierta con `+1 Damage` añade ese daño al hechizo lanzado desde ella.

### 2. Fase principal

Haz estas acciones en cualquier orden y tantas veces como quieras:

- jugar gema o reliquia;
- ganar carta del suministro;
- ganar carga: 2 aether;
- enfocar brecha cerrada;
- abrir brecha cerrada;
- preparar hechizo;
- resolver `While prepped`;
- cumplir `TO DISCARD:` de un poder.

### 3. Fase de robo

1. Pon las gemas y reliquias jugadas encima del descarte, en el orden elegido.
2. Conserva las cartas no jugadas en la mano.
3. Roba hasta tener 5 cartas.
4. Si el mazo se agota, voltea el descarte sin barajar y continúa.

---

## Aether

- Se obtiene principalmente con gemas.
- Se gasta en cartas, cargas y brechas.
- Solo dura durante el turno actual.
- No se acumula ni se entrega a aliados.
- Las cartas ganadas van inmediatamente al descarte.

---

## Brechas

| Estado | Preparar hechizo | Lanzamiento |
|--------|------------------|-------------|
| Abierta | Sí | Opcional en la fase de lanzamiento |
| Cerrada enfocada este turno | Sí | Obligatorio en la siguiente fase de lanzamiento |
| Cerrada no enfocada | No | — |

**Enfocar:** paga el coste, gira 90°, puedes preparar ese turno.  
**Abrir:** paga el coste actual, dale la vuelta; queda abierta para siempre.  
**Límite:** una brecha solo puede tener 1 hechizo preparado.

---

## Turno de la némesis

### 1. Fase principal

Resuelve de más antigua a más reciente:

- `PERSISTENT` de minions;
- quita 1 ficha de cada poder;
- si un poder queda sin fichas, resuelve `POWER X:` y descártalo.

### 2. Fase de robo

- **Ataque**: resuelve ahora y descarta.
- **Minion**: `IMMEDIATELY:`, fichas de vida y entra en juego.
- **Poder**: `IMMEDIATELY:`, fichas de poder y entra en juego.
- Si el mazo está vacío: `Unleash` ×3.

El `PERSISTENT` de un minion o el poder de una carta recién entrada no se resuelve hasta el siguiente turno de némesis.

---

## Agotamiento

Al llegar a 0 de vida:

1. `Unleash` ×2.
2. Destruye 1 brecha y descarta su hechizo preparado.
3. Descarta todas tus cargas.

Después:

- no puedes ganar vida;
- el daño que recibas se convierte en el doble de daño a Gravehold;
- si un efecto busca al jugador con menos vida, elige al jugador no agotado con menos vida.

---

## Recordatorios críticos

- El mazo **nunca se baraja**.
- No descartes la mano al final del turno.
- El aether sobrante se pierde.
- `Destroy` retira de la partida; `discard` solo descarta.
- Un hechizo de brecha cerrada se lanza obligatoriamente.
- Un minion recién robado espera para resolver su persistente.
- Vaciar el mazo de némesis no basta si quedan minions o poderes.
- La vida inicial normal es 10 por mago y 30 para Gravehold.

