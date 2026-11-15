# Asistente de reglas de Disney Lorcana

Estamos desarrollando una aplicación en español para aprender a jugar a Disney Lorcana y resolver dudas sobre sus reglas mediante una conversación. Está dirigida a jugadores, jueces y organizadores de torneos que necesitan explicaciones claras, ejemplos prácticos y respuestas apoyadas en fuentes oficiales.

La aplicación conecta el asistente con una biblioteca de reglamentos, textos de cartas, aclaraciones y documentos de torneo. A partir de una pregunta o una situación de partida, busca la información pertinente y explica cómo se aplica, citando las fuentes utilizadas. Tiene en cuenta la versión del reglamento, las cartas implicadas y el formato de juego, y señala cuándo falta información para confirmar una respuesta.

El proyecto combina la consulta de reglas con una guía de referencia en español. Las dudas que se solicita documentar se convierten en artículos con ejemplos y enlaces relacionados, que se incorporan a la guía publicada en Obsidian. Así, las explicaciones pueden consultarse de nuevo y servir a otras personas de la comunidad.

El objetivo es facilitar tanto el aprendizaje como la resolución de situaciones durante una partida y la formación en arbitraje, manteniendo las explicaciones fieles a la documentación oficial de Disney Lorcana.

## Archivos de trabajo fuera de Obsidian

La bóveda y el repositorio siguen en `lorcana-reglas`. Los análisis privados,
partidas, replays, memorias y adquisiciones se guardan en la carpeta hermana
`../lorcana-trabajo/`, fuera de la bóveda y de este repositorio Git.

- Profesorado, datos, planes y revisiones: `../lorcana-trabajo/analisis/profesora-lorcana/`.
- Extracciones de partidas: `../lorcana-trabajo/analisis/duels-2026-10-15/`.
- Análisis de Ancestral Guitar: `../lorcana-trabajo/analisis/ancestral-guitar/`.
- Adquisiciones del cliente: `../lorcana-trabajo/adquisiciones/duels/`.

No recrees esos árboles dentro de la bóveda ni dejes enlaces simbólicos o junctions
que los vuelvan a exponer a Obsidian. El código sigue en `herramientas/`; el
extractor mantenido está en `herramientas/duels_analisis/extraer_replays.py`.
Usa `herramientas/rutas_trabajo.py`: `ruta_trabajo()` para destinos nuevos y
`resolver_ruta()` para referencias archivadas. `LORCANA_TRABAJO` permite configurar
otra raíz absoluta externa. Conserva los bytes de originales, lotes y manifiestos:
sus rutas históricas se traducen al leer, sin reescribirlos ni invalidar hashes.
Las menciones antiguas a esos árboles en documentos trasladados son históricas.

Las capturas históricas de Discord versionadas permanecen en `analisis/` como
referencias. Las notas, fuentes normativas, `.obsidian` y Publish conservan su
ubicación. El MCP y la CLI antiguos se conservan como referencia histórica, pero
el workflow normal usa `lorcana-rules-engine`. Esta separación técnica no autoriza
publicar datos privados.
