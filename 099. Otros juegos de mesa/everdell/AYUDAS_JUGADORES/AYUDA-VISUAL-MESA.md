# Everdell — ayuda visual de mesa

**Alcance**: juego base  
**Validado**: 11/09/2026

---

## Flujo de la partida

```text
INVIERNO TARDÍO
      │
      ▼
┌───────────────────────────────────────────────┐
│ En sentido horario, cada jugador hace 1 acción │
│                                               │
│  TRABAJADOR  │  CARTA  │  SIGUIENTE ESTACIÓN  │
└───────────────────────────────────────────────┘
      │
      ├─ trabajador: obtiene el efecto y se queda desplegado
      ├─ carta: paga / coloca / resuelve efectos
      └─ estación: solo con todos los trabajadores desplegados
                    recupera trabajadores + obtiene bonus
      │
      ▼
 PRIMAVERA  →  VERANO  →  OTOÑO  →  TODOS PASAN  →  PUNTUACIÓN
```

Cada jugador avanza por las estaciones de forma independiente. No hay que esperar a que todos estén en la misma estación.

---

## Decisión rápida

```text
¿Tienes un trabajador disponible?
       │
   Sí  ├── ¿Hay un espacio útil libre? ──► Colócalo y resuelve.
       │
       └── ¿Prefieres jugar una carta? ──► Juega una carta.

   No  ──► ¿Puedes o quieres jugar una carta? ──► Juega una carta.
          Si no, prepárate para la siguiente estación.

PREPARAR:
todos tus trabajadores actuales deben estar desplegados.
```

---

## Resolución de una carta

```text
1. Descuento / habilidad previa
              ↓
2. Pagar coste o usar Ocupado
              ↓
3. Si era del Prado, reponer
              ↓
4. Colocar en la ciudad
              ↓
5. Resolver efecto de la carta
              ↓
6. Resolver efectos disparados
```

**Bicho relacionado**: si ya tienes la Construcción indicada, puedes pagar 0 bayas y poner Ocupado sobre ella. Solo una vez por Construcción.

---

## Dónde colocar un trabajador

```text
TABLERO
├─ Espacio básico ........ recursos / cartas / puntos
├─ Carta de Bosque ....... resuelve el texto
├─ Evento ................ requisito + coste → Evento
├─ Refugio ............... 2 cartas descartadas → 1 recurso
└─ Viaje (solo otoño) .... cartas descartadas → puntos finales

CIUDADES
├─ Destino propio ........ resuelve el texto
└─ Destino abierto rival . resuelve + rival gana 1 punto
```

**Anillo cerrado** = exclusivo, 1 trabajador.  
**Anillo abierto** = compartido, varios trabajadores.

---

## Recursos y límites

| Símbolo / concepto | Regla |
|---|---|
| Ramita | Recurso de construcción |
| Resina | Recurso de construcción |
| Piedra | Recurso de construcción |
| Baya | Recurso habitual de Bichos |
| Carta | Del mazo, salvo que diga Prado |
| Ficha de punto | Se guarda para el final |
| Mano | Máximo 8 cartas |
| Ciudad | Máximo 15 espacios |

Si una reserva de recursos se agota, usa un sustituto para representar los recursos restantes. Los costes siguen siendo de tipos concretos: solo un efecto de “cualquier recurso” permite elegir.

---

## Estaciones

| Al preparar… | Recupera | Obtén además |
|---|---:|---|
| Primavera | Todos los desplegados | 1 trabajador + activa verdes |
| Verano | Todos los desplegados | 1 trabajador + hasta 2 cartas del Prado |
| Otoño | Todos los desplegados | 2 trabajadores + activa verdes |

Las cartas verdes se activan al jugarse en cualquier estación. Prepararse en verano no activa las verdes.

---

## Puntuación final

```text
PUNTOS IMPRESOS EN CARTAS DE CIUDAD
+ FICHAS DE PUNTO
+ BONUS DE PROSPERIDAD MORADA
+ TRABAJADORES EN VIAJE
+ EVENTOS CONSEGUIDOS
= TOTAL
```

Empate: más Eventos → más recursos sobrantes → victoria compartida.

---

## Cinco avisos junto al tablero

1. Una persona solo hace una acción por turno.
2. Prepararse no es una fase común: cada jugador lo hace en su propio turno.
3. El Prado se repone al jugar una carta desde él.
4. Un Evento conseguido no se devuelve aunque después pierdas las cartas que lo habilitaron.
5. Después de pasar no recibes cartas ni recursos, aunque los destinos abiertos aún pueden ser visitados según sus reglas.

