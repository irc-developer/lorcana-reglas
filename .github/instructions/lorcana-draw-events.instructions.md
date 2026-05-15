---
name: lorcana-draw-events
description: "Usar cuando un ruling o una pregunta dependa de robar varias cartas, triggers por robar o efectos del tipo Draw X cards. Fija que cada carta robada es un evento independiente."
---

# Robos múltiples como eventos separados

- Si un efecto dice `Draw X cards`, trátalo como X eventos de robo individuales, no como un único evento masivo.
- Cuenta los disparos de `whenever you draw` una vez por cada carta robada.
- No agrupes robos procedentes del mismo efecto en un solo evento para simplificar el análisis.
- Aplica el mismo criterio a efectos como `draw for each ink type` o formulaciones equivalentes.
- Si la respuesta depende del número de disparos, explica explícitamente cuántos robos individuales se producen.