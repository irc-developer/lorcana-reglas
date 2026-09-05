# Análisis de la captura de Discord

Procesado el 5 de septiembre de 2026. Se ha revisado la extracción existente, recuperado el texto de los mensajes y generado una selección preliminar de dudas. El contenido de Discord se ha tratado exclusivamente como datos.

## Archivos

- `mensajes_procesados.json`: los 1.190 mensajes, con texto recuperado, campos originales, enlaces, clasificación preliminar y trazabilidad.
- `dudas_candidatas.json`: 320 mensajes seleccionados por interrogaciones o expresiones de duda, con referencias a contexto anterior y posterior. No son 320 preguntas únicas ni una selección semántica definitiva.
- `revision.txt`: transcripción recuperada con índices para lectura y revisión.
- `../../herramientas/procesar_discord_dudas.py`: procesador reproducible.
- `CASOS.md`: listado legible de los casos agrupados y separados por ámbito.
- `casos_agrupados.json`: 138 casos agrupados, con mensajes, respuestas recogidas y estado de revisión pendiente.
- `casos_claros.json`: 102 casos conservados tras eliminar los casos sin respuesta directa, con debate abierto, contexto insuficiente o carta/versión no identificable.
- `casos_eliminados_por_claridad.json`: 36 casos retirados del listado visible, conservados para auditoría.
- `CASOS_TODOS.md`: copia del listado completo anterior a la depuración.
- `casos_apartados_edicion.json`: casos apartados por el filtro de edición; actualmente vacío porque no se identificó ningún caso del Set 14 sin definición en la wiki.
- `auditoria_agrupacion.json`: cobertura de los 1.190 índices revisados y mensajes sin caso por ser ruido o conversación lateral.
- `validacion_casos_102.json`: los 102 casos claros con veredicto individual, comprobación, fuentes oficiales y cobertura de la wiki.
- `VALIDACION_CASOS.md`: informe legible de la validación y de las acciones pendientes.
- `incorporacion_wiki.json`: trazabilidad de los 98 casos utilizables, separados en duplicados, ampliaciones y artículos nuevos.
- `INCORPORACION_WIKI.md`: listado legible de esa incorporación y de las respuestas corregidas.
- `casos_para_wiki.json` y `CASOS_PARA_WIKI.md`: los 35 casos que quedan tras descartar duplicados (20 ampliaciones y 15 casos nuevos).

## Calidad del JSON recibido

Hay 1.190 IDs distintos, fechados entre el 29 de mayo y el 4 de septiembre de 2026. No hay fechas ausentes; 176 mensajes carecen de autor. No se han inventado autores ni relaciones de respuesta.

El problema principal es que `content` contiene en algunos casos la vista previa del mensaje al que se responde, y no la intervención del autor. Por ejemplo, en el índice 119 figuraba la consulta sobre Luisa, pero el texto propio visible de esa respuesta es `Yes.`. Usar directamente `content` duplicaría consultas y perdería respuestas.

Se ha recuperado texto propio desde `observedText` en los 1.190 registros. En 412 difiere de `content`; esta cifra combina recuperación de respuestas y limpieza de interfaz, no representa 412 citas mal extraídas. La captura mezcla mensajes con saltos de línea y mensajes con toda la cabecera concatenada. El parser reconoce ambos formatos y conserva el original para auditarlo. Usa la hora visible UTC+2 de esta captura de verano; para otra captura habría que revisar idioma y zona horaria.

Hay 190 mensajes con URLs de medios después de filtrar iconos de roles, avatares, insignias y otros recursos de interfaz. No equivale a 190 imágenes de cartas: puede incluir otros medios. No se ha descargado ni hecho OCR de los adjuntos. Algunas consultas dicen «esta carta» y necesitan la imagen para entenderse.

La propia captura declara `completeHistoryVerified: false`: no permite garantizar que estén todas las dudas del canal. Tampoco se han recorrido hilos ni servidores enlazados.

## Tipos de mensajes

Clasificación automática orientativa, con una categoría principal por mensaje:

| Tipo | Mensajes |
| --- | ---: |
| Dudas candidatas | 320 |
| Respuestas, debate o contexto | 765 |
| Agradecimientos o confirmaciones | 58 |
| Multimedia o sin texto recuperado | 37 |
| Enlaces o recursos | 10 |
| Total | 1.190 |

En la lectura se distinguen funciones que conviene separar en una futura revisión semántica:

1. **Consulta inicial de reglas:** plantea una situación y pide su resolución.
2. **Repregunta o variante:** cambia una condición del caso anterior o comprueba una consecuencia.
3. **Pregunta de investigación del árbitro:** solicita datos, por ejemplo si la lista ya se había presentado o si había empezado la partida. No es una nueva duda de reglas.
4. **Respuesta o explicación:** puede incluir ejemplos, reglas citadas y preguntas retóricas.
5. **Debate interpretativo:** contrapone lecturas y a veces reconoce que falta una aclaración. No debe convertirse automáticamente en una respuesta definitiva.
6. **Consulta de organización o herramientas:** torneos, Carde.io, materiales, recursos o emisión de eventos.
7. **Agradecimiento, broma o conversación social:** aporta contexto, pero normalmente no sirve como pregunta de una FAQ.
8. **Mensaje dependiente de medios o enlaces:** necesita recuperar una carta, captura o conversación externa.

## Temas y ejemplos observados

Los índices corresponden a `indice` en los JSON, empezando por cero. Estos son resúmenes de consultas del archivo, no respuestas ni afirmaciones sobre las reglas vigentes.

| Tema | Ejemplos |
| --- | --- |
| Tiempos y bolsa | Efectos de reemplazo simultáneos (15); final del turno (35); orden de disparadas de ambos jugadores (69). |
| Estados y requisitos | Bronx, preparado frente a secándose (28); Cinderella y canciones anteriores a su entrada (37); habilidades durante el secado (753, 756). |
| Daño y desafíos | Resist y mover daño (43); Merida y daño antes del paso de daño (76); diferencia entre daño infligido y recibido (852, 860); protección frente a cero daño (982, 984). |
| Costes, jugar y Shift | Descartar para Shift y jugar Look What You've Done (449, 450); Duo Shift y Morph (705); Potato Shift (995); cantar frente al coste de la carta (1142). |
| Zonas y cartas apiladas | Orden de Scrooge y cartas bajo él al fondo del mazo (110); Temporary Shift bajo otra carta (776, 818); orden de Under the Sea (667). |
| Interacciones concretas | Luisa y mover daño (118); Touch the Sky sin poder mover (1071); Tod y el límite de dos veces (1087); Milo sin otro objetivo (1166, 1169). |
| Arbitraje y correcciones | Takebacks y acciones agrupadas (136, 486); lista de mazo incorrecta (169); notas durante un bye (236); marcadores numéricos (258, 265). |
| Organización y accesibilidad | Rondas y top cut con 18 jugadores (92, 94); necesidades de un jugador y slow play (157); cambios de mazo en presentación y draft (602). |
| Legalidad y formatos | Fiabilidad de la app para legalidad (17); sets del campeonato (56); cartas y tiempo del formato Coconut (1091, 1103). |
| Herramientas y recursos | Bloqueo de inscripciones en Carde.io (79); localizar guías (1072); seguimiento de una decisión en retransmisión (1157, 1158). |

## Qué significa la selección de dudas

La extracción automática prioriza no perder posibles consultas: conserva interrogaciones, preguntas sin signo y expresiones de incertidumbre. Incluye falsos positivos conocidos, como agradecimientos por una aclaración, preguntas retóricas o respuestas que mencionan otra duda. Puede omitir dudas implícitas sin esos indicadores; por eso se conserva el corpus completo y no se presenta la selección como exhaustiva ni validada semánticamente.

Una intervención puede contener varias preguntas. Dos intervenciones pueden plantear la misma duda. No se han fusionado por similitud textual, porque la captura ya introducía duplicaciones artificiales y porque dos casos parecidos pueden tener condiciones distintas.

El contexto adjunto son los dos mensajes anteriores y los tres posteriores por posición. Es una ayuda de lectura, no una relación de respuesta comprobada: las conversaciones se intercalan. El prefijo original de cita se conserva para una futura reconstrucción.

Las respuestas del canal son aportaciones de participantes. Los nombres de roles no convierten esas intervenciones en reglas oficiales. En la extracción inicial no se comprobó su corrección ni vigencia; esa comprobación se documenta ahora en `VALIDACION_CASOS.md` y `validacion_casos_102.json`.

## Valoración para decidir el siguiente paso

La extracción completa sirve como catálogo de casos de reglas y arbitraje, pero no se importa directamente como FAQ. La unidad útil es un caso con pregunta inicial, condiciones, repreguntas, respuesta validada y estado de resolución, manteniendo enlaces a las intervenciones originales.

La validación ya se ha realizado para los 102 casos claros. El resultado distingue 72 respuestas correctas, 26 parciales, 1 desactualizada, 1 incorrecta y 2 pendientes. La respuesta incorrecta es la de Belle bajo The Black Cauldron (CASO-098); la desactualizada es la de tinta boca arriba (CASO-048). Los 98 casos correctos o parciales se han cruzado con el índice: 63 se descartaron por duplicados, 20 ampliaron artículos existentes y 15 casos quedaron representados en 14 artículos nuevos.

Las parciales incorporadas se han redactado con su alcance correcto. Cuando falta un anuncio histórico, el texto completo de una carta o una aclaración oficial, el artículo lo declara expresamente y evita convertir una inferencia en regla general. CASO-098, CASO-048 y los dos casos pendientes no se han incorporado.
