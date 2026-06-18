---
lang: es
translation_of: Battle Sequence System
source_lang: en
type: system
category: game-sequence
canonical: true
source: core-rules
surface: system
owner-domain: game-sequence
tags:
  - warhammer40k
  - game-sequence
  - system
aliases:
  - Sistema de secuencia de juego
  - Sistema de secuencia de batalla
  - Secuencia de juego
related:
  - La ronda de batalla
  - Estructura del turno
  - Fase de mando
  - Fase de movimiento
  - Fase de disparo
  - Fase de carga
  - Fase de combate
---

# Sistema de secuencia de juego

## Resumen

El sistema de secuencia de juego es el mapa de dominio para el orden principal de la batalla: rondas de batalla, turnos de los jugadores y fases del turno.

## Alcance

Este dominio cubre el esqueleto temporal de la partida en vivo: la ronda de batalla, la estructura de cada turno y las fases principales que contienen los procedimientos de juego.

Sirve para responder preguntas de **cuándo** ocurre algo. Cuando la pregunta pasa a ser **cómo** se resuelve una mecánica concreta, la respuesta debe saltar al dominio correspondiente.

## Responsabilidad del dominio

Secuencia de juego mantiene:

- [[La ronda de batalla]] como bucle externo de la partida.
- [[Estructura del turno]] como orden interno de cada turno de jugador.
- [[Fase de mando]], [[Fase de movimiento]], [[Fase de disparo]], [[Fase de carga]] y [[Fase de combate]] como contenedores temporales.
- [[Turnos de los jugadores]] como entrada de alias respaldada por la fuente oficial.

Secuencia de juego no mantiene:

- Las reglas de movimiento, disparo, carga, combate o ataques.
- La preparación previa a la batalla.
- Las reglas de datasheets, claves, habilidades o estratagemas salvo como ventanas temporales.
- La puntuación o resolución específica de misión.

## Artículos publicados

- [[La ronda de batalla]]
- [[Estructura del turno]]
- [[Turnos de los jugadores]]
- [[Fase de mando]]
- [[Fase de movimiento]]
- [[Fase de disparo]]
- [[Fase de carga]]
- [[Fase de combate]]

## Navegación

- Empieza aquí cuando la duda sea el orden temporal de la partida.
- Lee [[La ronda de batalla]] si la duda es el bucle de rondas o qué jugador actúa primero.
- Lee [[Estructura del turno]] si la duda es el orden de un turno de jugador.
- Lee una fase concreta cuando la duda esté dentro de esa ventana temporal.
- Pasa a [[Sistema de movimiento]] cuando la pregunta sea cómo mueve una unidad.
- Pasa a [[Sistema de ataque]] cuando la pregunta entre en impactar, herir, salvar o infligir daño.

## Referencias

- Reglas básicas oficiales: La ronda de batalla 07.00.
- Reglas básicas oficiales: Fase de mando 08.00.
- Reglas básicas oficiales: Fase de movimiento 09.00.
- Reglas básicas oficiales: Fase de disparo 10.00.
- Reglas básicas oficiales: Fase de carga 11.00.
- Reglas básicas oficiales: Fase de combate 12.00.
