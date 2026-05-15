# Customizaciones de Copilot del workspace

Este directorio concentra las customizaciones versionadas del repositorio.

## Estructura

- `instructions/`: instrucciones específicas cargables bajo demanda o por patrón.
- `skills/`: flujos especializados reutilizables e invocables.
- `prompts/`: reservado para prompts reutilizables de una sola tarea.
- `agents/`: reservado para agentes personalizados cuando exista un flujo que lo justifique.

## Estado actual

- Las skills activas del workspace siguen en `skills/`.
- Las instrucciones activas de Lorcana viven en `instructions/` y están troceadas por responsabilidad.
- El primer agente real del workspace vive en `.github/agents/lorcana-ruling.agent.md`.
- La skill de preguntas de Lorcana del workspace es la autoridad frente a cualquier copia equivalente del perfil de usuario.
- [Premisas agente IA Lorcana](../Premisas%20agente%20IA%20Lorcana.md) queda como referencia extensa de criterio.
- [Arquitectura de Skills - Agente Lorcana](../Arquitectura%20de%20Skills%20-%20Agente%20Lorcana.md) queda como documento de diseño, no como agente activo.

## Criterio de organización

- Lo específico de Lorcana y de este repositorio debe vivir aquí.
- Lo genérico y reutilizable entre proyectos puede seguir viviendo en skills o prompts del perfil de usuario.
- No se crean agentes personalizados hasta que exista un flujo real que los justifique.