---
type: rules-question
category: attached-units
canonical: false
source: core-rules
surface: resolved-question
owner-domain: attached-units
status: verified
rules:
  - 19.03
  - 02.05
  - 01.02
  - 19.01
  - 24.03
tags:
  - warhammer40k
  - resolved-question
  - attached-units
  - rules-application
aliases:
  - las keywords se pasan a la unidad adjunta
  - las claves se comparten entre lider y escolta
  - un lider da sus keywords a la unidad
  - una unidad adjunta gana las keywords del personaje
related:
  - Claves en unidades adjuntas
  - Formar unidades adjuntas
  - Unidad adjunta
  - Claves
  - Claves diversas en unidades
  - Unidades y miniaturas
  - Anti
  - Líder
---

# ¿Las keywords se pasan de un personaje a la unidad que se ha unido y al revés?

## Respuesta corta

Sí, a nivel de unidad: una [[Unidad adjunta]] tiene todas las keywords de sus unidades componentes. No, a nivel de miniatura: el personaje, la Escolta y cualquier otra miniatura no ganan las keywords de las demás miniaturas.

## Regla práctica

Si una regla comprueba si una unidad tiene una keyword, mira el conjunto completo de keywords de la unidad adjunta. Si una regla comprueba si una miniatura tiene una keyword, mira solo las keywords propias de esa miniatura.

## Cómo decidirlo en mesa

1. Identifica si la regla habla de una unidad o de una miniatura.
2. Si habla de una unidad, trata la unidad adjunta como una sola unidad con todas las keywords de sus partes.
3. Si habla de una miniatura concreta, usa solo las keywords de esa miniatura.
4. No traslades keywords entre miniaturas salvo que una regla lo diga expresamente.

## Ejemplos

Un [[Líder]] con la keyword `PSYKER` se une a una unidad de Escolta que no tiene `PSYKER`. La unidad adjunta cuenta como una unidad `PSYKER`, así que un arma con `[ANTI-PSYKER 4+]` puede aplicar [[Anti]] contra esa unidad.

Eso no convierte a las miniaturas de Escolta en miniaturas `PSYKER`. Si otra regla exige elegir o afectar a una miniatura `PSYKER`, esas miniaturas de Escolta no cumplen esa condición.

También funciona en el otro sentido a nivel de unidad: si la Escolta aporta una keyword que el Líder no tiene, la unidad adjunta tiene esa keyword. El modelo Líder no gana esa keyword como miniatura individual.

## Errores comunes

- Pensar que el personaje reparte sus keywords a todas las miniaturas de la Escolta.
- Pensar que la Escolta reparte sus keywords al modelo Líder.
- Usar una keyword agregada de la unidad para cumplir una regla que exige que una miniatura tenga esa keyword.
- Olvidar que los ataques eligen unidades como blanco, por lo que muchas reglas con keywords se resuelven contra la keyword de la unidad blanco.

## Fundamento de reglas

- [[Claves en unidades adjuntas]]: la unidad adjunta tiene todas las keywords de sus unidades componentes, pero sus miniaturas no ganan keywords que no tuvieran.
- [[Claves]] y [[Claves diversas en unidades]]: una regla que nombra una keyword se aplica a unidades con esa keyword, y una unidad con keywords mezcladas reúne las keywords de sus miniaturas sin transferirlas entre miniaturas.
- [[Unidad adjunta]] y [[Formar unidades adjuntas]]: explican cuándo una unidad de Escolta y un Líder o Apoyo pasan a ser una sola unidad adjunta.
- [[Unidades y miniaturas]]: separa las comprobaciones sobre unidades de las comprobaciones sobre miniaturas.
- [[Anti]]: ejemplo de regla que comprueba la keyword de la unidad blanco.
- Fuente oficial: `doc/fuentes_oficiales/eng_01-06_warhammer40k_new40k_core_rules.pdf`, referencias `19.03`, `02.05`, `01.02`, `19.01` y `24.03`.

## Resumen para arbitraje casual

La unidad adjunta reúne las keywords de sus partes para reglas que miran a la unidad. Ninguna miniatura gana keywords ajenas por estar en esa unidad.
