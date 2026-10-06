# Plan de limpieza editorial de las dudas de Lorcana

Fecha del barrido y ejecución: 06/10/2026. Estado editorial: limpieza aplicada y validada; tres variantes requieren revisión normativa.

Objetivo: que un lector novato encuentre la respuesta y entienda la jugada sin tener que leer el registro de investigación del asistente. Mantener el fundamento necesario y las limitaciones que cambien cómo debe usar la respuesta.

El usuario autorizó inicialmente ejecutar el plan en local y después indicó en esta conversación «Súbelo al repo y publica». Se autoriza el commit y push de esta tarea y la publicación selectiva de los artículos y el índice. Las instrucciones, planes y notas internas se incluyen en el repositorio, sin publicarlos en Obsidian. La limpieza editorial no constituye una nueva comprobación de vigencia o corrección de todos los rulings.

## Resultado de la ejecución local

- **237 registros revisados:** 236 artículos públicos editados y una nota de mantenimiento trasladada a documentación interna. El índice público queda en 236 casos (37 de timing).
- **232 artículos con limpieza aplicada** y cuatro artículos con limpieza aplicada y una revisión normativa pendiente, correspondientes a tres variantes. Ningún registro editorial queda pendiente.
- Relatos técnicos y de verificación retirados; referencias de fuentes condensadas; ejemplos y secuencias conservados cuando aportan una consecuencia propia. Las ampliaciones están antes del único bloque final de tags.
- Los encabezados de secuencia pasan de 203 bloques de «Secuencia oficial» a 116 de «Cómo se resuelve». El resto se retiró por ser relleno o repetir la respuesta.
- Longitud comparable de los 236 artículos: **112,511 → 97,522 palabras Markdown** (−13.3 %). Es una medida del resultado, no una cuota de recorte.
- Tod y The Horseman Strikes!: **856 → 278 palabras**, manteniendo ambas elecciones y el orden de resolución.
- Plantilla, guía de escritura, workflow y consulta rápida ajustados para evitar que la investigación se vuelque de nuevo en los artículos. La verificación completa de fuentes sigue siendo obligatoria al resolver dudas.
- Reparados enlaces históricos sin destino, un ancla retirada, texto con codificación dañada y estructuras vacías o repetidas. No se actualizaron índices de búsqueda ni cachés.

### Revisiones normativas separadas de la limpieza

| Variante | Hallazgo y tratamiento local |
|---|---|
| Luisa como único personaje | El cuerpo excluía a Luisa como origen del daño y una ampliación afirmaba que podía mover su propio daño. Se retiraron esas afirmaciones incompatibles y se conservó una advertencia breve. El resto de la explicación y los resultados de GSC se mantienen. |
| Potato Shift sobre Morph | El cuerpo afirmaba que era legal y una ampliación pedía aclaración oficial. La combinación queda pendiente; se conserva su pregunta y fuentes sin un «sí» confirmado. El artículo general de Morph contiene un aviso cruzado a esta variante. |
| Hans y Anna al jugar cartas para ambos jugadores | La variante citaba una numeración retirada y afirmaba que una condición secundaria impedía añadir el disparo a la bolsa; la guía local actual describe otra comprobación. Se conserva el escenario con aviso pendiente, sin adjudicar un resultado nuevo. |

También se retiró de Webby's Diary un ejemplo ajeno al resultado principal que afirmaba que poner una carta debajo de The Black Cauldron disparaba el objeto: la ficha de Webby's Diary limita el evento a personajes o localizaciones. Se verificaron ambas fichas completas en el set 10 y se conserva el ejemplo pertinente de Boost.

La nota sobre Touch the Sky que estaba añadida a una duda de efectos simultáneos se conserva en [documentación interna](nota-retirada-touch-the-sky.md), pendiente de decidir su destino tras revisar el contenido. La [nota de mantenimiento del TXT](CR%202.1%20-%20artefactos%20tipográficos%20del%20TXT%20y%20criterio%20de%20integración.md) también queda fuera del índice público.

### Validación y estado de entrega

Comprobaciones editoriales del conjunto: destinos de enlaces locales, enlaces nuevos a epígrafes, ausencia de frontmatter en casos, un bloque de tags al final, encabezados no vacíos, referencias e índice principal coherentes con los archivos reales. Revisado el diff y la ausencia de errores de whitespace. Las verificaciones no certifican todos los rulings ni sustituyen las tres revisiones normativas descritas.

Se preservan los cambios de configuración de Obsidian ajenos a esta tarea. La primera entrega se mantuvo sin commit, push ni publicación; el usuario autorizó después subir y publicar. El inventario conserva las medidas y señales del barrido inicial y registra el resultado por archivo.

Los apartados siguientes conservan los criterios y lotes del plan inicial como referencia de la ejecución; sus cifras de barrido describen el corpus antes del traslado.

## 1. Alcance y resultados del barrido inicial

Se han examinado el texto y la estructura de los 237 archivos Markdown de las subcarpetas 11.*, excluyendo la plantilla y el índice. El total coincide con el índice manual. Se ha realizado lectura dirigida de los bloques de fuentes y de casos representativos para distinguir ruido editorial, contenido didáctico y límites relevantes. Durante la ejecución se completó el barrido editorial del conjunto. Una señal automática no acredita que un párrafo sobre.

El [inventario completo](inventario-limpieza-editorial.tsv) recoge una fila por artículo, su categoría, longitud inicial, señales, decisión editorial, ruta actual y longitud tras la limpieza. La longitud se calcula por separación de espacios sobre el Markdown, incluidos enlaces; sirve para priorizar, no como límite de publicación.

| Categoría | Archivos |
|---|---:|
| 11.0. Timing y Resolución | 38 |
| 11.2. Zonas y Movimientos | 24 |
| 11.3. Costes y Requisitos | 21 |
| 11.4. Habilidades | 35 |
| 11.5. Keywords | 21 |
| 11.6. Interacciones Complejas | 67 |
| 11.7. Dudas por desarrollar | 5 |
| 11.8. Correcciones de jugadas | 26 |
| **Total** | **237** |

Hallazgos comprobados:

- **5 artículos** mencionan el índice de búsqueda, el MCP, hashes o recuperación en memoria. Es información del proceso de documentación que puede retirarse del artículo público.
- **31 artículos** tienen un bloque de fuentes o estado. Algunos contienen verificaciones extensas; otros solo una referencia breve y útil. No se propone borrar todos esos bloques por su título.
- **201 artículos** usan el encabezado «Secuencia oficial» (203 bloques, porque Bodyguard lo repite). La plantilla impone una secuencia fija de seis componentes, aunque no todos ayuden a resolver cada duda.
- **14 artículos** tienen otros encabezados después del primer bloque de tags. Es una señal de ampliaciones acumuladas que deben integrarse donde corresponda, no eliminarse sin leerlas.
- **27 artículos** superan 800 palabras y **7** superan 1.200. Se revisarán por repeticiones y amplitud del tema; la longitud por sí sola no justifica recortes.

## 2. Criterio para decidir qué sobra

Cada frase debe cumplir alguna función: describir un hecho necesario de la duda, dar la respuesta, explicar el motivo, mostrar una consecuencia distinta, permitir consultar una fuente o advertir de una limitación material. Si no cumple ninguna, es candidata a salir del artículo.

| Contenido | Tratamiento propuesto |
|---|---|
| Fechas de búsqueda, comprobación de enlaces, apertura del PDF, comparación de hashes, errores HTTP, estado del índice o del MCP | Retirar del artículo. Comunicar incidencias relevantes en la transacción de trabajo; si se necesita conservarlas, usar un registro interno separado. |
| Fecha y título del hilo, captura aportada, autorización para incorporar una imagen, relato de cómo se verificaron fichas | Retirar cuando solo expliquen cómo llegó la pregunta. Conservar el estado de mesa reconstruido. |
| «No es una FAQ oficial», «es una inferencia editorial», «el ejemplo es didáctico», repetidos como descargo | Sustituir por una explicación directa sustentada en las reglas. Conservar una nota breve cuando exista incertidumbre material o sea necesario distinguir el alcance de una aclaración oficial concreta. |
| Versión y fecha efectiva del documento repetidas en párrafos largos | Conservar una referencia compacta a la fuente utilizada y los epígrafes o páginas pertinentes. Centralizar la información general de vigencia en las páginas de fuentes ya existentes. |
| Texto completo de cartas | Citar solo la parte que explica la duda y enlazar la ficha completa. Leer y verificar el texto completo sigue siendo obligatorio para el asistente. |
| Misma conclusión en respuesta, ejemplo, secuencia, tabla y errores frecuentes | Elegir la presentación más clara. Mantener ejemplos o variantes adicionales solo si cambian el resultado o evitan una confusión distinta. |
| Pasos «costes: no aplica», bolsa o GSC genéricos, cierre normal del turno | Retirar si no intervienen en la explicación. Conservar el momento de bolsa o GSC cuando sea decisivo para el resultado. |
| Fuente oficial que resuelve una excepción, respuesta provisional, ámbito Coconut, traducción de trabajo o decisión reservada al Lore Guide | Conservar la referencia o advertencia que el lector necesita; condensar el relato de comprobación que la acompaña. |

No transformar una interpretación discutible en una certeza al abreviarla. No atribuir a una FAQ oficial una conclusión que esa FAQ no contiene. Tampoco sustituir un bloque largo de descargos por una etiqueta «confirmado» sin fundamento.

## 3. Cambiar primero el comportamiento de documentación

Antes de limpiar en serie, armonizar estas piezas en una misma edición:

1. [Plantilla de casos](../../01.%20Reglas/11.%20Casos%20de%20ejemplo%20y%20aclaraciones/Plantilla%20-%20Caso%20de%20ejemplo%20y%20aclaración.md): conservar duda y respuesta; sustituir la secuencia obligatoria por un ejemplo o secuencia cuando aporte información. Usar «Cómo se resuelve» en lugar de «Secuencia oficial» para describir una aplicación editorial de reglas. Dejar referencias compactas y tags al final.
2. [Guía de escritura](../instructions/lorcana-case-writing.instructions.md): incorporar el criterio del apartado 2, limitar las citas de cartas a lo relevante y exigir que las variantes tengan una función distinta. Fuentes y estado dejan de ser una invitación a narrar verificaciones.
3. [Workflow de rulings](../skills/lorcana-ruling-workflow/SKILL.md): mantener la comprobación completa de fuentes, cartas, índices y publicación; aclarar en los pasos de escritura y calidad que los resultados de investigación no se vuelcan automáticamente en el artículo. Los avisos técnicos se comunican donde corresponda a la transacción.
4. [Consulta rápida](../../.agents/skills/lorcana-consulta-rapida/SKILL.md): aclarar que declarar una incidencia de búsqueda en la respuesta de trabajo no obliga a incluirla en la documentación pública. Mantener los modos y sus restricciones actuales.

Estructura propuesta para una duda sencilla:

- **Duda:** situación y condiciones necesarias.
- **Respuesta:** resultado y motivo en lenguaje claro.
- **Ejemplo o cómo se resuelve:** solo si ayuda; puede integrarse en la respuesta.
- **Referencias:** reglas y fuente oficial suficientes para sostener lo explicado, sin repetir la demostración entera.
- **Tags.**

No imponer un número rígido de palabras o referencias: un caso complejo puede necesitar más detalle. Mantener los nombres de archivo y los enlaces existentes durante la primera limpieza.

## 4. Lotes de revisión

### Lote piloto: Tod

Empezar por [Tod y The Horseman Strikes!](../../01.%20Reglas/11.%20Casos%20de%20ejemplo%20y%20aclaraciones/11.0.%20Timing%20y%20Resolución/Tod%20y%20The%20Horseman%20Strikes!%20-%20rechazar%20el%20destierro%20no%20elige%20personaje.md).

- Retirar el relato de «Fuentes y alcance» de las líneas 29–33, conservando una referencia compacta al PDF y las reglas que fundamentan las dos ramas.
- Integrar cualquier condición de la habilidad que siga siendo necesaria en la duda o explicación; no perder información útil porque comparta párrafo con el registro de verificación.
- Condensar la respuesta y la secuencia de ocho pasos: el lector necesita distinguir rechazar el destierro de aceptar y elegir a Tod, y entender cuándo puede resolverse su habilidad.
- Presentar una sola demostración clara de esas dos ramas. Evitar repetirla en tres formatos.

Muestra de la respuesta abreviada, basada en la explicación ya documentada:

> **No.** Tras robar, decides si realizar el destierro opcional. Si lo rechazas, no eliges a Tod y su habilidad no se dispara. Si aceptas y lo eliges, su habilidad espera en la bolsa mientras la acción lo destierra. Cuando puede resolverse, Tod ya está en el descarte y no puede prepararse. No puedes resolver su habilidad entre elegirlo y desterrarlo.

La muestra no reemplaza todavía el artículo. Sus enlaces, condiciones iniciales y referencias se conservarán al preparar la edición completa.

### Lote 1: otros artículos con información del proceso técnico

| Artículo | Bloque a revisar | Precaución editorial |
|---|---|---|
| Derrota, timing mazo vacío | «Fuente y estado», líneas 54–60 | Conservar el momento de derrota y lo necesario para entender FOOLS!; retirar comparaciones de fichas, captura y aviso del índice. |
| Remember Me permite jugar personajes desde la mano y el descarte | «Fuentes y alcance», líneas 52–58 | Conservar los distintos permisos y restricciones; retirar la historia de incorporación, verificaciones y recuperación. |
| Look What You've Done no se dispara al terminar de resolverse | «Fuente y estado», líneas 50–56 | Conservar la FAQ oficial concreta y su página. Retirar HTTP 403, hashes y circunstancias de lectura. |
| Strange Things y This Growing Pressure | «Fuente y estado», líneas 80–88, y finales de secuencia genéricos | Conservar las condiciones de juego y, cuando siga siendo relevante, el carácter de traducción de trabajo de Baloo. Retirar el relato del MCP y de incorporación. |

Las líneas corresponden al estado auditado y se desplazarán al editar. El inventario contiene las rutas completas.

### Lote 2: verificaciones, procedencia y atribuciones repetidas

Revisar después Boo con Scrooge; Mulan con Hercules; Fergus con Sleepy Hollow; Bambi con Dr. Bushroot; Descartar como requisito para resolver una habilidad; Ancestral Guitar; Bodyguard; y Wasabi.

Acciones: sustituir las verificaciones fechadas por referencias compactas, retirar el origen de capturas que solo contextualiza la pregunta y condensar las declaraciones de autoría editorial. En Boo, Mulan y Wasabi, conservar las distinciones sobre qué aclara una fuente oficial y qué conclusión requiere aplicar otras reglas, cuando sean necesarias para entender el grado de certeza.

Los bloques breves de «Fuente y estado» de Narrow Escape, Morph o Temporary Shift requieren otro tratamiento: integrar o abreviar su referencia, conservando las aclaraciones oficiales sobre excepciones. No presentan el mismo exceso que Tod.

### Lote 3: repetición y ampliaciones acumuladas

Prioridad de lectura: One and Only; Luisa Madrigal — I Can Take It; No tener objetivo legal vs elegir un objetivo inválido; Boost olvidado al poner carta debajo en torneo; Bodyguard; Remember Me.

Revisar respuestas que se repiten en tablas y secuencias, variantes periféricas y los 14 artículos con contenido posterior a tags. Integrar cada ampliación bajo su pregunta o enlace relacionado. En One and Only, valorar reducir la tabla de doce comparaciones y el catálogo de interacciones; en Luisa, conservar las condiciones que producen resultados diferentes y evitar repetir Ward en varios bloques.

Hay dos hallazgos que deben tratarse aparte:

- «CR 2.1 - artefactos tipográficos del TXT y criterio de integración» es una nota de mantenimiento dentro del índice de dudas. Proponer su traslado a documentación interna, conservando lo útil y actualizando enlaces y recuentos si se ejecuta el traslado.
- «The Queen - Conceited Ruler y descarte sin retorno» conserva una pregunta al usuario en «Dato faltante». Integrar las condiciones en el caso definitivo y retirar ese residuo de conversación; si cambia el fallo, hacer revisión normativa antes de editarlo.

### Lote 4: completar todas las categorías

Seguir el orden 11.0 → 11.2 → 11.3 → 11.4 → 11.5 → 11.6 → 11.7 → 11.8, saltando los artículos ya cerrados en lotes anteriores. Trabajar en grupos de 5–10 artículos para que los cambios sean fáciles de revisar.

Revisar también los artículos sin señales automáticas. Marcar cada fila como «limpiado», «revisado sin cambios» o «pendiente de revisión normativa», con una nota breve. La categoría de dudas por desarrollar y los casos de torneo merecen conservar los límites que afectan al uso de la respuesta.

## 5. Validación y publicación de cada lote

- Comparar antes y después: mismo resultado, mismos supuestos críticos y mismas diferencias entre variantes; explicación más breve y clara.
- Comprobar que cada referencia conservada respalda la conclusión y que no se pierde una excepción. Si se detecta una duda normativa, aislarla para una revisión específica y verificar las fuentes antes de cambiar el resultado.
- Mantener enlaces de cartas y reglas, ausencia de frontmatter, tags pertinentes y referencias sin duplicados. Corregir restos de plantilla, encabezados vacíos y codificación dañada en los archivos editados.
- Sincronizar índices si cambian títulos, enlaces, ubicación o número de artículos; mantener las fechas exigidas por el workflow cuando corresponda. No modificar contadores por un simple recorte de texto.
- Validar el diff y conservar los cambios previos del usuario. En el estado inicial solo figura como modificado `.obsidian/workspace.json`, que queda fuera de esta tarea.
- Subir solo los archivos de esta tarea al repositorio y publicar solo los 236 artículos y el índice principal, conforme a la autorización posterior del usuario. Conservar fuera los cambios de Obsidian y cualquier otro pendiente de la bóveda.

## 6. Criterio de finalización

La limpieza local termina cuando los 237 registros originales tengan decisión editorial, se hayan revisado las señales técnicas y estructurales, las instrucciones produzcan el nuevo formato y los cambios estén validados. La publicación fue aplazada en la primera entrega y está autorizada por la instrucción posterior del usuario. Los casos que realmente necesiten revisión normativa deben quedar identificados; no se resuelven por una supresión automática de texto.

El éxito se mide por la utilidad de lo que queda, no por alcanzar un porcentaje de palabras borradas: respuesta fácil de localizar, motivo comprensible, ejemplo con función propia y fuentes consultables sin el relato de investigación.
