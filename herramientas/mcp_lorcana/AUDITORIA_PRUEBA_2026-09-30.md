# Auditoría de las consultas de prueba — 30/09/2026

Se revisaron dos chats recientes mediante `read_thread` y sus registros completos. No se iniciaron turnos ni se enviaron mensajes a esos chats. Esta revisión no modifica servidor, instrucciones, configuración o esfuerzo del modelo.

| Chat | Duración del turno | Llamadas MCP | Tiempo MCP sumado | Tiempo de pared de bloques de herramientas |
|---|---:|---:|---:|---:|
| Consultar Resist y el daño de Put | 70,024 s | 2 | 2,115 s | 5,021 s |
| Aclarar Resist y daño de contadores | 77,883 s | 3 | 3,784 s | 8,247 s |

El tiempo MCP sumado incluye llamadas en paralelo en la segunda prueba y está incluido en el tiempo de pared de los bloques. Este último se calculó entre llamada `exec` y resultado; incluye comandos, MCP y, donde corresponde, apertura web. El resto transcurre fuera de esos bloques: generación/consumo de contexto, coordinación y posibles esperas del cliente/proveedor. No se puede asignar todo ese tiempo exclusivamente a razonamiento o a un conflicto. Ambos chats usaron `gpt-6.1-sol` con esfuerzo `high`; no se demuestra cuánto explica de la duración.

## Funcionamiento confirmado

Las cinco llamadas a `lorcana` terminaron correctamente: `isError=false`, índice actual/utilizable, CR 2.2.0, sin advertencias ni reglas solicitadas ausentes. La búsqueda usó `modo="consulta"` y la regla fue auxiliar. No aparecieron CLI de consulta/mantenimiento, llamadas de edición, indexación, creación de artículos o ejecución del flujo editorial. Las respuestas incluyeron fundamento CR 8.8.3, ejemplo y versión local.

No hay evidencia de colisión funcional MCP/CLI, dos índices diferentes o fallo del servidor que explique el minuto. Está observado el uso del MCP por el asistente en chats nuevos para una consulta sencilla.

## Desajustes observados

**Salida recortada por la herramienta que presenta los datos.** El servidor devolvió `structuredContent` completo: 46.934 y 44.860 caracteres al serializarlo para la auditoría. El código imprimió el paquete entero con `text()`, sin ampliar el presupuesto predeterminado de 10.000 tokens de `functions.exec`. Los registros muestran:

```text
Warning: truncated output (original token count: 11601)
Warning: truncated output (original token count: 11096)
```

`tool_output_token_limit=100000` del proyecto no modifica el presupuesto del contenedor `exec`. El recorte apareció al mostrar la evidencia al asistente; MCP conservó el resultado completo. Después se pidieron reglas adicionales. Esto puede aumentar las rondas para completar contexto, pero la secuencia no demuestra que sea la única causa de las llamadas ni de la duración total.

**Carga amplia de instrucciones/manual.** La prueba de 70 s leyó siete archivos: skill rápida, contrato Copilot, README de `.github`, alcance, verificación de cartas, workflow editorial y README MCP completo. Sus comandos imprimieron 28.493 caracteres, además del catálogo de herramientas. La skill exige actualmente cargar esas instrucciones; el manual MCP añade instalación y diagnóstico a una consulta con herramientas ya disponibles. Los comandos tardaron solo 0,731 s, pero su contenido entra en las siguientes solicitudes al modelo.

**Varias rondas.** La prueba de 70 s contiene cuatro bloques: instrucciones iniciales, instrucciones restantes/manual, búsqueda y regla completa. Entre bloques hubo intervalos de unos 10–11 s; después del último resultado transcurrieron unos 20 s hasta terminar. Esto localiza el tiempo fuera de las herramientas sin identificar el proceso interno del proveedor.

**Comprobaciones adicionales en la prueba anterior.** La prueba de 78 s añadió cuatro documentos, una segunda búsqueda y la apertura web del PDF, que devolvió `Internal Error`. Se ejecutaron en paralelo dentro de un bloque de 2,574 s. El fallo web no bloqueó la recuperación local ni fue un fallo MCP. La primera búsqueda solicitó expresamente la sección 9.2; después se recuperó la sección 8.8 de Resist.

**Redacción antigua del alcance.** `.github/instructions/lorcana-scope.instructions.md` todavía restringe las reglas a `01. Reglas` y `01.1.a Official English Reference – Unmodified`. El puntero `00. Fuente actual.md` de esa carpeta remite al PDF vigente de `Documentacion Oficial` y declara históricos los Markdown. La skill y MCP utilizan ese PDF. Conviene explicitar la selección en contrato y alcance; estas pruebas no demuestran que esa ambigüedad haya causado retraso.

## Prioridad sugerida

Primero ajustar la presentación en `exec`: conservar el resultado estructurado completo, mostrar la evidencia pertinente con citas y condiciones completas y evitar JSON truncado. Después reducir la lectura del manual de instalación en consultas normales y alinear el alcance con el puntero oficial actual. Mantener los modos y el workflow editorial. Repetir la misma consulta y comparar rondas, tamaño de contexto y duración total.

Referencias oficiales para distinguir las capas: [diagnóstico de servidor y cliente](https://developers.openai.com/plugins/deploy/troubleshooting) y [configuración/instrucciones MCP en Codex](https://learn.chatgpt.com/docs/extend/mcp).

## Registros revisados

- [Consultar Resist y el daño de Put](<C:/Users/plata/.codex/sessions/2026/09/30/rollout-2026-09-30T14-28-29-01a0f249-acd4-7f22-bf7d-f8ceae208df8.jsonl>): llamadas MCP completas en líneas 28 y 35; recorte en 29; duración en 42.
- [Aclarar Resist y daño de contadores](<C:/Users/plata/.codex/sessions/2026/09/30/rollout-2026-09-30T14-24-14-01a0f245-c661-7e63-8f98-912f7225a342.jsonl>): llamadas MCP completas en líneas 31, 39 y 40; recorte en 32; duración en 50.

Pendientes: evaluación editorial completa en una copia, consultas de ambigüedad/limitaciones con el asistente y observación del MCP desde el acceso móvil existente.

## Cambios aplicados después de esta auditoría — 0.2.0

La recomendación sobre recortes y lecturas se implementó el 30/09/2026. `lectura` comparte metadatos de fuente y conserva íntegros todos los fragmentos; `completo` mantiene el paquete plano de diagnóstico. AGENTS.md, la skill y las instrucciones MCP especifican una sola copia de salida, presupuesto explícito de `functions.exec` y lectura por grupos desde memoria si el resultado todavía es demasiado grande. Se evita repetir MCP para suplir un recorte.

La skill ya no exige guías de cartas sin cartas concretas, workflow editorial para una petición explícita de solo lectura ni manual de instalación en una consulta normal. El núcleo `.github` se sigue cargando y los modos editoriales conservan el workflow completo. Contrato, alcance y workflow remiten al PDF oficial seleccionado por los dos punteros locales.

Al reproducir los dos conjuntos de argumentos por transporte MCP real, la vista entregó 28,74 % y 26,22 % menos caracteres que el formato completo sobre las mismas fuentes actuales; todos los fragmentos reconstruidos fueron idénticos. La carga inicial prescrita para la consulta sin cartas es de cuatro archivos y 13.508 caracteres, frente a los siete y 28.493 observados antes. El índice se actualizó como mantenimiento porque tres fuentes habían cambiado; las llamadas de lectura posteriores no escribieron archivos.

Pasaron las 10 pruebas MCP y los 20 oráculos de fuente. El cliente Codex acepta la configuración estricta y descubre `lorcana` 0.2.0 con sus cuatro herramientas. Véanse [resultados](RESULTADOS.md) y [mediciones actuales](mediciones-0.2.0-2026-09-30.json). Las secciones anteriores describen el estado durante las pruebas originales; no son defectos pendientes sin tratar.

Falta repetir la consulta en un chat nuevo tras reiniciar el servidor para observar rondas y latencia total con el asistente. La reproducción de transporte no demuestra por sí sola que el minuto observado haya disminuido.
