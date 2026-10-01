# Prompts reutilizables

Esta carpeta contiene prompts reutilizables de una sola tarea.

Estado actual:

- [Crear herramientas de consulta rápida de Lorcana](crear-consulta-rapida-lorcana.prompt.md): prompt para construir búsqueda local y una entrada de consulta con fuentes y ejemplos, utilizable desde Codex Remote.
- Las tareas repetibles y multietapa siguen viviendo como skills en `.github/skills/`.

Los prompts deben ser breves, tener una sola responsabilidad y remitir a las skills existentes cuando corresponda. La lógica repetible y multietapa debe permanecer en su skill responsable.
