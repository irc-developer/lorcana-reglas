---
name: lorcana-analista-jugadas
description: Analiza decisiones de Disney Lorcana desde una posición limitada, guarda un plan anterior a la elección y entrega un diagnóstico trazable. Para mulligan, tinta, secuencia y cierre; no prepara replays ni sustituye el workflow de rulings.
---

# Analista de jugadas de Lorcana

Esta entrada activa la implementación del repositorio, actualmente en fase piloto.
Desde la raíz de `lorcana-reglas`, lee y aplica `.github/skills/lorcana-analista-jugadas/SKILL.md`.
Esa es la fuente mantenida de las instrucciones; resuelve sus referencias relativas desde su propia carpeta.
Si no puedes leerla, informa de la dependencia ausente antes de emitir un diagnóstico.

La coordinación y las fronteras de integración siguen `../lorcana-trabajo/analisis/profesora-lorcana/INTEGRACION-AGENTES.md`.
La memoria y las partidas personales quedan fuera de esta entrada. No crea conversaciones ni publica datos.
