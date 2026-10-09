# Plan de revisión de artículos: CR 2.3 y Hyperia City

**Preparado:** 09/10/2026. **Estado:** revisión individual y edición ejecutadas; commit subido y publicación verificada. Recarga de la conexión MCP persistente pendiente.

**Petición de Iván:** ampliar la revisión que anteriormente se limitó a los artículos relacionados con cambios detectados y decidir qué aclaraciones de Hyperia City necesitan documentación. Este plan complementa la migración ya publicada; no sustituye su informe ni declara realizada una revisión normativa integral de toda la wiki.

## Alcance comprobado y trabajo restante

Se ha inventariado y cribado el texto de **495 documentos**, incluidos **239 casos**, en introducción, reglas, referencia inglesa, torneo, correcciones, consejos, recursos, comunidad y portada. Los **15 documentos históricos** se distinguen de la referencia activa: nueve transcripciones inglesas numeradas y seis notas retiradas. «00. Fuente actual» sigue siendo un selector activo y no se clasifica como transcripción histórica. El catálogo de cartas se ha consultado como evidencia adicional; sus fichas no están incluidas en los 495 documentos ni se publicarán como artículos.

El cribado señala **231 documentos no históricos** por conceptos potencialmente afectados. Es una selección de lectura, no una lista de 231 errores. Se han leído y contrastado casos y derivados seleccionados, las reglas relevantes de ambos PDF y las notas oficiales de Hyperia City, incluidas sus aclaraciones por carta. Los documentos sin coincidencias también necesitan decisión individual de revisión; no se darán por correctos automáticamente.

Se han preparado **41 actuaciones iniciales**: 26 sobre documentos existentes, 8 altas propuestas y 7 sobre corpus, recursos o sincronización. Algunas exigen una corrección confirmada; otras son ampliaciones o comprobaciones que pueden cerrarse sin editar. Los ocho títulos son propuestas editoriales, sujetas a una última comparación conceptual antes de crear los archivos.

Entregables de planificación:

- [Inventario de los 495 documentos](auditoria-cr-2.3-inventario.tsv): ruta, tipo, hash, cambios previos, prioridad, hallazgos y estado de cierre.
- [Actuaciones y fundamentos](auditoria-cr-2.3-hallazgos.tsv): trabajo concreto, evidencia y distinción entre defecto confirmado y revisión pendiente.
- [Decisiones sobre 34 temas de Hyperia](hyperia-city-decisiones-editoriales.tsv): crear, ampliar, reutilizar o comprobar, con destino explícito.
- [Cribado de enlaces](auditoria-cr-2.3-enlaces.tsv): candidatos sin destino local; dos son marcadores de la plantilla y no defectos de una página para lectores. No certifica anclas ni enlaces públicos.
- [Manifiesto de preparación](auditoria-cr-2.3-plan.json): alcance, base de Git, hashes de fuentes y archivos previos que deben conservarse.

## Fuentes y aplicación temporal

La autoridad para la adaptación es el [PDF oficial inglés de CR 2.3](https://files.disneylorcana.com/CRUpdate_EN_Oct-2026.pdf), efectivo el **16/10/2026**, comparado con el original local 2.2. Las [notas oficiales de Hyperia City](https://www.disneylorcana.com/en-US/news/2026/10/hyperia-city-set-release-notes), publicadas el 08/10/2026 y consultadas el 09/10, aportan aclaraciones y erratas. Las cartas se verifican en los archivos de set y se contrastan con la fuente oficial cuando existe una corrección.

La publicación podrá hacerse **en cuanto esté completado y validado cada lote**, siguiendo la decisión previa de Iván. Todo anticipo debe indicar la vigencia del 16/10. Publicar ahora no convierte 2.3 en el reglamento vigente antes de esa fecha. Se conserva la selección 2.2 para consultas anteriores y el original histórico para comparaciones. Las seis notas antiguas ya retiradas de Publish no necesitan una segunda retirada.

Las transcripciones inglesas históricas no se utilizarán como autoridad primaria. Las políticas de torneo y de corrección no cambian por actualizar CR: solo se revisan sus dependencias de reglas y enlaces, salvo evidencia oficial específica de una modificación de política.

## Lote 1 — Correcciones prioritarias y corpus

1. **Resumen «Declarar un desafío» (A01).** Reconstruirlo desde CR 4.6: contiene dos versiones, numeración CR 1.X, referencias antiguas, «pila» para resolver disparos y la contradicción «agotado, preparado». Incluir los limitadores de las palabras clave aplicables, las ventanas de bolsa/GSC y las diferencias de localizaciones. Revisar todos los enlaces que lo utilizan como explicación.
2. **Jukebox (C01/H02).** El MCP devuelve la ficha con el texto impreso anterior a la errata. Registrar texto impreso y texto corregido con procedencia y aplicación; evitar que la búsqueda presente el impreso como operativo. Preparar su caso canónico antes de sincronizar el índice.
3. **Erratas de Adventurous en cartas anteriores (C02).** Actualizar las cinco fichas afectadas en sets 10–13 y buscar sus dependencias. Preservar las condiciones y duraciones de cada carta. Si la fuente solo informa de la modificación, documentar ese alcance sin inventar una transcripción oficial completa. Integrar Woody y This Growing Pressure en A10/A11.
4. **«Next Stop Olympus, dos copias y lores» (A02).** La secuencia coloca habilidades todavía no disparadas en la bolsa. Separar creación del efecto, evento que lo dispara y resolución. Verificar la terminología flotante/retardada y aprovechar la revisión para incorporar Yama, evitando otro artículo sobre acumulación del mismo concepto.

**Cierre del lote:** texto operativo del catálogo identificado sin ambigüedad, procedimientos corregidos y referencias verificadas. Ningún archivo previo ajeno se incluye íntegro en la publicación de este lote.

## Lote 2 — Casos y explicaciones que dependen de CR 2.3

| Familia | Trabajo y documentos iniciales | Referencia para el contraste |
| --- | --- | --- |
| Palabras clave repetidas | Support, Ancestral Guitar y el borrador Peter Pan’s Shadow/Pegasus. Explicar duración; conservar la acumulación de modificadores numéricos. No cambiar un veredicto solo por actualizar la explicación. | 8.1.2, p.41; 6.4 |
| Efectos entre jugadores | «Cada oponente», casos de revelación y dependencias del artículo «No hay bolsa». Resolver por partes sin intercalar bolsa. | 6.7.6–6.7.6.1, p.37 |
| Decisiones opcionales y secuencias | Minnie, Milo, Madame Medusa, «El uso de Then» y descarte como requisito. Comparar el texto exacto; varios may no eliminan condiciones A to B/if you do. | 6.1.4.2 y 6.1.5.1, p.26 |
| Requisitos y otras acciones legales | Copper/Reckless, Woody, Adventurous y el borrador Strange Things. Corregir prohibiciones demasiado amplias y comprobar localizaciones como objetivos de desafío. | 8.7, p.42; 8.16, p.44; 1.2.2 |
| Juego y entrada | Belle/Caldero, Remember Me, Bodyguard y casos de jugar desde otras zonas. Distinguir permiso, oportunidad, coste, carta jugada y entrada real. | 4.3.2–4.3.3, p.13; 6.7.9, p.38 |
| Contadores y pagos | Revisar afirmaciones genéricas que equiparan pagar tinta con agotar cartas; añadir escenarios sin gotas y pagos mixtos cuando sean necesarios. | 1.13.1.2, p.9; 4.3.2.4; 4.4.3.4; 4.7.3.4 |
| Elecciones y características | Revisar cartas reveladas por cada efecto, nombres, comparaciones de coste y movimiento por efecto, incluida elección aunque no llegue a ocurrir el movimiento. | 6.1.14.3, p.29; 6.7.7, p.37; 4.7, p.18 |

La inversión A/B en la explicación de Madame Medusa está confirmada; el veredicto completo de ese caso y la exigencia de objetivo en Milo quedan pendientes de resolución técnica. No se aplicará una sustitución masiva de textos con may o de conclusiones existentes.

## Lote 3 — Artículos nuevos de Hyperia City

Las rutas propuestas y los artículos comparados están en H01–H08 de la matriz de actuaciones. La tabla organiza las preguntas que documentaremos; el ruling completo, las imágenes verificadas y sus referencias se prepararán durante la ejecución.

| ID | Artículo propuesto | Motivo editorial frente a los casos existentes |
| --- | --- | --- |
| H01 | Belle - Apprentice Inventor puede jugarse al desterrar The Black Cauldron | Cambio de zona durante el pago; Scrooge cubre otro coste y no esa continuidad. |
| H02 | Jukebox requiere otra canción con el mismo nombre en el descarte | Errata y comprobación del disparo posterior; enlazar «Acciones en el descarte». |
| H03 | Minnie Mouse - Urban Visionary y las dos decisiones opcionales | Caso concreto de opciones independientes con consecuencia compartida; contrastar las cuatro combinaciones y enlazar Milo. |
| H04 | Baymax - Amped Up, retirar gotas y pagar tinta | Diferenciar un coste expresado en contadores de un coste de tinta pagado mediante contadores. |
| H05 | Madam Mim - Resourceful Trickster y las gotas usadas antes de entrar | Distinguir disparos que comprueban un pago previo de habilidades que necesitan estar presentes al ocurrir el evento. |
| H06 | Thomas O’Malley - Savvy Vagabond, revelaciones y costes empatados | Comparación global tras revelar; el artículo general de bolsa no desarrolla el empate ni los destinos. |
| H07 | Flippant Taunt mantiene su efecto cuando su jugador abandona la partida | Separar salida de una carta y salida de un jugador. Precisar la duración sin inventar un turno posterior de un jugador eliminado. |
| H08 | Clawhauser - Safety Officer no ignora su condición al jugarse gratis | Restricción para poder jugar, distinta de elegir un coste alternativo. |

Antes de cada alta: comparar nombres, mecánica, conclusión y tags en toda la sección 11. Si la misma duda ya queda resuelta en un canónico, ampliar ese documento y retirar el alta prevista de la matriz. El número ocho es una previsión, no una cuota de artículos.

## Lote 4 — Aclaraciones que aprovecharemos en documentos existentes

- **Ancestral Guitar, Remember Me y Belle - Exceptional Writer:** ampliar sus artículos ya identificados.
- **Port Authority/Russell:** ampliar el caso de once/whenever; distinguir número de disparos y número de resoluciones con efecto.
- **Mr. Manchas:** añadir a reducciones de coste; verificar también los ejemplos originales.
- **Everyone Knows Juanita:** integrar en «Acciones en el descarte».
- **Merlin’s Wand/equipo, Rapunzel, Spyglass Hat/Ariel:** comparar y ampliar los canónicos de nombres múltiples, another y nombre sin versión.
- **Yama:** integrar en la revisión de Next Stop Olympus.
- **Stone by Day:** comparar el caso «Enderezar un personaje» y añadir una variante útil si falta.
- Los ejemplos sobre lore cero, contar cartas jugadas, habilidades estáticas, reemplazos y resolución de canciones se asignan a reglas generales o keywords. La matriz incluye todos los temas; no se generará un artículo por cada pregunta oficial.

## Lote 5 — Cobertura del resto de la wiki y recursos

1. Recorrer cada fila no histórica del inventario y leer el documento completo. Empezar por los 231 candidatos y continuar con los restantes, incluidos torneo/corrección y consejos cuando dependan de CR. Registrar **sin cambios**, **actualizado**, **histórico** o **pendiente con motivo**, junto a la fuente y regla contrastadas. El hash permite detectar cambios posteriores y repetir solo la revisión afectada.
2. Reconciliar introducción, etiquetas, registro maestro y glosario. Hay errores anteriores a 2.3 en la guía de búsqueda, entre ellos la definición de Alert como preparación al jugar (Alert es oficial en CR 8.2) y la descripción de Support como habilidad de desafío. Reutilizar los tags canónicos.
3. Inspeccionar visualmente los recursos enlazados, incluidos PNG y SVG. El texto extraído señala problemas en `tiposdehabilidades.svg` y `resolucionHabilidades.svg`; el esquema de jugar necesita representar entrada y continuidad. Actualizar fuentes editables, exportaciones y páginas que los incorporan conjuntamente. No presentar la extracción de etiquetas como revisión visual completada.
4. Revisar rutas completas, anclas, referencias públicas y enlaces al catálogo o a CR 1.X. El cribado inicial de wikilinks solo identifica nombres sin destino; puede pasar por alto una ruta antigua cuyo nombre siga existiendo en otra carpeta. Excluir marcadores de plantilla y mantener históricos identificados.
5. Comprobar todas las citas de la selección anterior de 44 páginas publicadas, no solo las nuevas. Ya están confirmadas páginas erróneas en el resumen CR 2.3 y Colors of the Wind: **CR 2.2, 6.7.6 está en p.37 y 8.1.2 en p.41**. Corregir también cualquier informe que repita esas referencias, conservando la trazabilidad de la corrección.

**Criterio de cobertura:** todas las filas tienen decisión justificada. Una búsqueda sin coincidencias no cierra una fila ni demuestra vigencia de su contenido. La revisión de políticas conserva su autoridad propia y no fabrica nuevas penalizaciones a partir de CR.

## Lote 6 — Conocimiento del MCP

El original CR 2.3 y la transición por fecha ya están incorporados al proyecto. El MCP conectado sigue seleccionando CR 2.2 el 09/10, lo que corresponde a la fecha vigente. Esto no acredita por sí solo que su proceso haya cargado todos los cambios de código de la migración.

Faltan en el corpus oficial local las notas de Hyperia como fuente recuperable, y la ficha de Jukebox conserva el impreso sin errata. Para completar la actualización:

1. Incorporar las notas oficiales como evidencia identificable con URL, fecha de publicación/consulta, hash, alcance y limitaciones. Usar el mecanismo de fuentes existente y comprobar qué formato admite antes de elegir la copia local.
2. Incorporar las correcciones de cartas con procedencia y aplicación temporal; evitar duplicados de texto operativo e impreso en consultas.
3. Actualizar el índice mediante la CLI de mantenimiento después de terminar cada lote de corpus/artículos. Las herramientas MCP de lectura no realizan esta operación.
4. Verificar búsqueda de Jukebox, las cinco erratas, los ocho temas nuevos y los casos ampliados. Comprobar fuentes, resolución exacta de cartas y advertencias; el set 14 declara variantes parciales y no se presentará como catálogo íntegro sin acreditarlo.
5. Probar un proceso nuevo y comprobar una conexión persistente tras recarga. Mantener 2.2 hasta el 15/10 y comprobar selección 2.3 desde el 16/10 con los mecanismos de fecha existentes. No terminar procesos de otros chats ni afirmar que se reiniciaron conexiones que no se han comprobado.

## Ejecución editorial y publicación

Ejecutar en el orden de los lotes, con transacciones pequeñas y selecciones explícitas. Para cada transacción que modifica artículos: resolver, escribir, sincronizar índices/tags y fecha visible si corresponde, validar, crear commit, hacer push y publicar solo sus rutas mediante `herramientas/publicar_obsidian/publicar.py`. Usar primero el plan de publicación y `--comprobar`, después `--aplicar`, y verificar el contenido público frente a lo aprobado en el commit. Los planes, herramientas y fichas de set quedan fuera de Publish.

Conservar los cambios previos registrados: Bodyguard, Strange Things/This Growing Pressure, Empates intencionales, índice, registro de tags y el borrador Peter Pan’s Shadow/Pegasus. Si un archivo comparte trabajo previo, aislar la transacción antes de commit/Publish o completar coordinadamente la anterior; no subir el archivo completo por comodidad. Mantener aparte `.obsidian/workspace.json` y los archivos temporales.

Validación ajustada a los cambios: texto exacto de cartas, regla/página original, coherencia de veredicto y secuencia, plantilla, tags, enlaces, índices y contadores, fecha, avisos de vigencia y selección de publicación. Repetir pruebas del motor solo si cambia su código, selección o extracción; para cambios de corpus, comprobar indexación y recuperación de los escenarios afectados.

El cierre final entregará un inventario sin pendientes no explicados, altas y actualizaciones realmente realizadas, comprobaciones del MCP, commits y enlaces públicos. Hasta entonces, este documento es un plan de ejecución y no un informe de actualización terminada.

## Ejecución del 09/10/2026

Se completó la lectura individual de los 495 documentos y las decisiones sobre 34 temas de Hyperia; se crearon las ocho entradas previstas. El inventario conserva hashes iniciales y finales, y el registro de lectura documenta el contraste. También se corrigieron dependencias adicionales detectadas en la lectura, enlaces públicos, diagramas y políticas desde sus originales. Los 15 documentos históricos y los cambios previos protegidos se conservan.

El MCP incorpora las notas y erratas fechadas; los procesos nuevos se prueban con CR 2.2 antes del 16/10 y CR 2.3 desde esa fecha. La conexión persistente abierta conserva el código anterior: su recarga no se ha realizado, porque no hay una herramienta de reconexión disponible y no se terminan procesos de otros chats. Véase el informe de cierre para resultados de Git y publicación.

Publicación completada: **317 rutas**, sin pendientes de esta selección, en el commit `fcea89c3fd026f7970e53fe63d12e37e99492bd6`. Las 303 notas se compararon con el texto del commit y los 14 recursos byte a byte. Los pendientes ajenos no se publicaron.
