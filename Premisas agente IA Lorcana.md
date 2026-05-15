# Premisas del agente IA de reglas Lorcana

Estado: Índice histórico  
Fecha de reorganización: 2026-05-13  
Fecha de congelación de criterio original: 2026-03-18

> Este archivo ya no es la fuente operativa del workspace. Las customizaciones activas viven en `.github/instructions/` y `.github/skills/`.

## Qué es este archivo ahora

Este documento queda como:

1. índice de la capa activa del repositorio;
2. resumen histórico de la reorganización;
3. punto de entrada para entender dónde vive cada responsabilidad.

No debe volver a convertirse en un bloque monolítico de reglas operativas.

## Dónde vive hoy cada responsabilidad

### Instrucciones activas

- Alcance, jerarquía de fuentes y criterio de parada: [.github/instructions/lorcana-scope.instructions.md](.github/instructions/lorcana-scope.instructions.md)
- Aclaración mínima de dudas ambiguas: [.github/instructions/lorcana-question-clarification.instructions.md](.github/instructions/lorcana-question-clarification.instructions.md)
- Verificación exacta de cartas: [.github/instructions/lorcana-card-verification.instructions.md](.github/instructions/lorcana-card-verification.instructions.md)
- Timing de disparos frente a reemplazos: [.github/instructions/lorcana-trigger-vs-replacement.instructions.md](.github/instructions/lorcana-trigger-vs-replacement.instructions.md)
- Robos múltiples como eventos separados: [.github/instructions/lorcana-draw-events.instructions.md](.github/instructions/lorcana-draw-events.instructions.md)
- Escritura y ubicación de casos: [.github/instructions/lorcana-case-writing.instructions.md](.github/instructions/lorcana-case-writing.instructions.md)
- Deduplificación de casos: [.github/instructions/lorcana-case-dedup.instructions.md](.github/instructions/lorcana-case-dedup.instructions.md)
- Tags de casos: [.github/instructions/lorcana-case-tags.instructions.md](.github/instructions/lorcana-case-tags.instructions.md)
- Enlaces Obsidian y citas internas: [.github/instructions/lorcana-obsidian-links.instructions.md](.github/instructions/lorcana-obsidian-links.instructions.md)
- Higiene de archivos Markdown: [.github/instructions/lorcana-file-hygiene.instructions.md](.github/instructions/lorcana-file-hygiene.instructions.md)

### Skills activas del workspace

- Importación de sets desde la API: [.github/skills/lorcana-api-set-import/SKILL.md](.github/skills/lorcana-api-set-import/SKILL.md)
- Seeds SQL de preguntas: [.github/skills/lorcana-sql-question-pools/SKILL.md](.github/skills/lorcana-sql-question-pools/SKILL.md)
- Actualización de portada e índices manuales: [.github/skills/update-empecemos-date/SKILL.md](.github/skills/update-empecemos-date/SKILL.md)

### Diseño y contexto

- Estructura actual de customizaciones: [.github/README.md](.github/README.md)
- Diseño objetivo del flujo de rulings: [Arquitectura de Skills - Agente Lorcana.md](Arquitectura%20de%20Skills%20-%20Agente%20Lorcana.md)

## Decisiones meta que siguen vigentes

- Lo específico de Lorcana debe vivir en el workspace, no en customizaciones globales del perfil.
- Las reglas operativas deben modificarse en la instrucción o skill responsable, no aquí.
- Si aparece una nueva responsabilidad reusable, debe añadirse como instrucción o skill pequeña, no como apéndice de este archivo.
- Si una regla vieja entra en conflicto con la capa activa, prevalece la capa activa de `.github/`.

## Qué se retiró de la capa activa

La versión anterior de este archivo mezclaba en un solo texto:

- alcance y jerarquía de fuentes,
- resolución de ambigüedades,
- verificación de cartas,
- timing,
- robos múltiples,
- documentación de casos,
- tags,
- enlaces de Obsidian,
- saneado de archivos,
- reglas de interacción del agente y bloques de prompt.

Ese modelo ya no se usa porque generaba duplicidad, contradicciones internas y una superficie difícil de mantener.

## Material que queda solo como histórico

- Bloques de prompt listos para copiar.
- Reglas antiguas que obligaban a documentar todos los rulings por defecto.
- Guías de optimización de requests o de ejecución dependientes del agente del momento.
- Cualquier formulación detallada que ya haya sido absorbida por una instrucción modular.

Si en el futuro hace falta recuperar el texto exacto previo a esta reorganización, la referencia correcta es el historial del repositorio, no este archivo.

## Cuándo editar este archivo

Edita este archivo solo si ocurre una de estas cosas:

1. se crea, renombra o elimina una instrucción o una skill relevante;
2. cambia la regla de reparto entre customización local y global;
3. necesitas dejar constancia histórica de una reorganización importante.

No añadas aquí reglas operativas nuevas. Si una regla debe influir en el comportamiento del agente, colócala en `.github/instructions/` o `.github/skills/`.