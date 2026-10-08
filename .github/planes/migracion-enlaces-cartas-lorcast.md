# Plan de migración de enlaces de cartas a Lorcast

Fecha: 08/10/2026. Estado: migración completada, subida y publicada; catálogo público reducido y corpus local conservado.

## Objetivo y criterio editorial

La guía se centra en explicar reglas e interacciones. Los nombres de cartas de sus artículos abren la imagen de la carta proporcionada por Lorcast, como ya ocurre en el artículo de Héctor Rivera y The Torn Corner. El catálogo completo deja de ser un destino habitual de lectura.

Se propone conservar los archivos locales de cartas como corpus de verificación y recuperación del MCP. Aligerar la navegación pública no exige borrarlos del repositorio. La retirada de las fichas publicadas se trata como una fase distinta, posterior a la migración de enlaces.

Este cambio afecta a la presentación y los enlaces; no constituye una revisión normativa de todos los artículos. Lorcast aporta datos e imágenes comunitarios; el PDF oficial inglés sigue siendo la autoridad para reglas y las erratas oficiales prevalecen cuando proceda.

## Situación comprobada

- El commit `3a4e856` cambió el artículo de Héctor Rivera: sus tres enlaces externos abren imágenes `large` en `cards.lorcast.io`.
- El barrido inicial de Markdown versionado localizó **505 enlaces internos a cartas en 149 artículos activos**, todos dentro de `01. Reglas`. Hay **240 pares de destino local y epígrafe**, que todavía no equivalen a 240 cartas distintas: se deben unificar referencias alternativas y reimpresiones.
- **Tres enlaces usan anclas de línea** (`#L2429`, `#L2436`, `#L534`) en el artículo de Fergus, Hold Fast y alcance del descarte. Deben resolverse por la carta citada y su ficha completa. Por ejemplo, la línea actual 534 del set 1 corresponde a Magic Broom, mientras el artículo rotula The Queen - Commanding Presence; no convertir esa referencia por número de línea.
- Se inventariaron aparte **47 enlaces en 16 archivos legacy**, un ejemplo de enlace en la plantilla y cuatro enlaces a catálogos/sets en dos documentos internos. Los archivos legacy quedan fuera de la migración editorial activa.
- El catálogo versionado contiene **16 Markdown**, aproximadamente **1,43 MB** y **2.968 encabezados de ficha**; esas cifras no acreditan cartas únicas ni completitud de cada colección.
- `Empecemos.md` ya enlaza la documentación de la API, pero escribe «Lorecast API». Debe corregirse a **Lorcast** y explicar su contribución.
- Solo se ha verificado la configuración local de Publish; todavía no se ha comprobado qué fichas del catálogo están publicadas.

El [inventario inicial](inventario-enlaces-cartas.tsv) registra categoría, artículo, línea, destino y etiqueta por ocurrencia. Es una base de trabajo: su barrido identifica wikilinks y enlaces Markdown con destino al catálogo explícito o nombre exacto de archivo. La ejecución debe ampliar la revisión a enlaces externos de cartas, imágenes incrustadas, referencias de definición y posibles destinos abreviados no identificados. Las líneas son las del barrido, no identificadores estables.

## Formato elegido y obtención de destinos

Formato público: `[Nombre visible de la carta](URL_de_imagen_devuelta_por_Lorcast)`. Conservar los alias y el texto visible de cada enlace; usar nombre y versión completos cuando haga falta distinguir cartas. Los enlaces de reglas, artículos y fuentes oficiales conservan su función actual.

Obtener el destino desde `image_uris.digital.large` del registro exacto de la API. No construir rutas concatenando nombres o identificadores; tampoco eliminar el parámetro final de actualización. Lorcast advierte que pueden cambiar la estructura y el dominio de las imágenes en su [documentación de imágenes](https://lorcast.com/docs/api/images).

Crear un mapa reutilizable con: archivo y epígrafe local, nombre, versión, set, número de colección, idioma, ID de Lorcast, URL de imagen, fecha de obtención y estado de resolución. Consultar por set y número cuando estén disponibles; si hay que buscar por nombre, verificar la versión y la impresión antes de aceptar el resultado. No escoger automáticamente el primer resultado. Las reimpresiones con textos distintos, promos y cartas especiales requieren revisión.

La API describe estas identidades y las imágenes en su [modelo de cartas](https://lorcast.com/docs/api/cards). Descargar los sets necesarios una sola vez, reutilizar resultados y respetar su [política de acceso](https://lorcast.com/docs/api): espaciar peticiones entre 50–100 ms y conservar los datos descargados al menos 24 horas. No consultar la API por cada aparición del enlace.

Si no existe una coincidencia inequívoca o falta la imagen, registrar la incidencia y conservar el enlace local hasta resolverla. Una carta sin cobertura no debe desaparecer ni recibir la imagen de otra versión. El cierre de la migración exige resolver todas las incidencias o documentar expresamente las excepciones restantes.

## Fases de ejecución

### 1. Completar inventario y mapa

Repetir el barrido sobre el estado inicial de la ejecución, conservar cambios previos y separar artículos activos, navegación, plantilla y documentos internos. Ampliar los formatos detectados y revisar los enlaces externos existentes. Resolver cada destino contra la ficha local completa y el registro de Lorcast; agrupar duplicados para evitar consultas repetidas. Generar un informe de correspondencias y excepciones antes de editar artículos.

### 2. Fijar el nuevo comportamiento de documentación

Actualizar conjuntamente la plantilla de casos, `.github/copilot-instructions.md`, las instrucciones de alcance, verificación de cartas y enlaces Obsidian, y el workflow de rulings. El criterio debe distinguir **verificar el texto en el corpus local** de **enlazar la imagen externa para el lector**. La exigencia actual de obtener todos los enlaces exclusivamente del catálogo debe admitir las URL verificadas del mapa de Lorcast.

Revisar también `AGENTS.md`, las dos copias de la skill de consulta rápida, su prompt, las instrucciones de preguntas SQL, `Premisas agente IA Lorcana.md`, `Arquitectura de Skills - Agente Lorcana.md` y la skill de importación de sets. Actualizar únicamente las piezas afectadas, manteniendo los modos de consulta y la jerarquía normativa. Los generadores que aún introducen wikilinks de cartas deberán usar el mapa o quedar marcados como históricos si ya no se ejecutan.

El MCP sigue recuperando fichas locales; no necesita una petición externa por cada consulta. Si se decide más adelante trasladar el corpus, habrá que adaptar su clasificación de fuentes y regenerar/validar los índices de búsqueda en una tarea específica.

### 3. Piloto y atribución

Migrar una muestra que incluya un personaje con versión, una acción, una localización, una reimpresión y los enlaces de línea de Fergus. Comprobar que se abre la imagen correcta y que resulta legible en ordenador y móvil desde Obsidian Publish. Usar el artículo de Héctor como referencia de presentación.

Añadir a `Empecemos.md`, en «Recursos y Herramientas», este texto visible:

> **Cartas e imágenes:** los enlaces a cartas de esta guía utilizan imágenes obtenidas mediante la API de [Lorcast](https://lorcast.com). Gracias a Lorcast por facilitar su consulta. [Documentación de la API](https://lorcast.com/docs/api).

Corregir «Lorecast API» en «Links de interés» a «Lorcast API». Mantener el aviso general existente sobre Disney y Ravensburger. La atribución propuesta es textual y enlazada; no se ha identificado en las páginas consultadas un distintivo gráfico obligatorio. No inventar un sello de colaboración oficial.

### 4. Migración completa y validación

Aplicar exclusivamente sustituciones resueltas por el mapa, por lotes temáticos. Conservar redacción, ejemplos, referencias normativas, nombres de archivo, tags y enlaces entre artículos. Revisar el diff y comprobar que una segunda ejecución no produce cambios.

Verificar: cobertura de las 505 ocurrencias iniciales más las detectadas en el barrido ampliado; identidad de carta y versión; respuesta válida y tipo de contenido de cada imagen única; preservación de etiquetas; Markdown válido; y ausencia de enlaces internos a fichas en artículos migrados. Revisar visualmente una muestra diversa en Publish. Mantener un manifiesto exacto de archivos por lote y un registro de excepciones.

### 5. Reducir el catálogo público

Tras comprobar los artículos publicados, retirar las fichas largas de la navegación pública y sustituir la página «Cartas de Lorcana» por una entrada breve a Lorcast. Conservar inicialmente las fichas en Git y en la bóveda para el MCP, y excluirlas de futuras publicaciones.

Comprobar qué páginas del catálogo existen realmente en Publish y qué enlaces públicos siguen apuntando a ellas antes de despublicar. Excluir un archivo local no elimina una publicación existente. Conviene mantener temporalmente la entrada de catálogo como orientación para visitantes con enlaces guardados; no asumir que Publish permite redirecciones por cada epígrafe antiguo.

Los borrados públicos se ejecutarán con una lista explícita de páginas del catálogo, verificada y separada de las actualizaciones de artículos. El workflow actual de rulings y `publicar.py` autorizan altas/actualizaciones selectivas y prohíben borrados: no sirven para retirar el catálogo. Esta fase requiere una operación específica de despublicación dentro del alcance acordado para ejecutar el plan.

### 6. Entrega y mantenimiento

Crear commits por fase o lote con solo los cambios correspondientes, subirlos y publicar las rutas explícitas de cada transacción. La herramienta actual admite casos de la sección 11, portada y registro de tags; cualquier artículo fuera de ese alcance que aparezca en el inventario ampliado, así como la entrada breve del catálogo, requiere ampliar de forma explícita y acotada la selección admitida. Nunca publicar todos los pendientes de la bóveda.

Tras publicar, comprobar las páginas públicas y la portada. Conservar el inventario final, el mapa, los manifiestos y los commits para poder revertir sustituciones. Regenerar las URL desde la API cuando se revise un set o se detecten imágenes rotas; no añadir una dependencia de la API al abrir cada artículo.

## Criterios de finalización

1. Todos los enlaces de cartas de los artículos activos están migrados y verificados, con cualquier excepción residual identificada expresamente.
2. Los artículos nuevos siguen el mismo criterio mediante plantilla e instrucciones coherentes.
3. La portada reconoce a Lorcast y enlaza la API.
4. El catálogo público queda reducido según el alcance ejecutado, sin romper el corpus local ni el MCP.
5. Los cambios están subidos y publicados selectivamente, con comprobación del resultado público y un inventario final reproducible.

## Ejecución autorizada

Iván indicó «Llévalo a cabo» el 08/10/2026. Se han migrado 505 enlaces en 149 artículos, actualizado portada, entrada breve, plantilla e instrucciones y excluido las 15 fichas locales de futuras publicaciones. El mapa, el manifiesto y la comprobación HTTP de 241 imágenes quedan versionados junto al inventario. Los 149 artículos se compararon íntegramente con la versión inicial; la migración es idempotente y las 16 pruebas de identidad, selección y conservación del corpus pasan.

Dos correcciones editoriales acompañan los destinos: el contraste «from any discard» del artículo de Fergus se atribuye a Magic Broom - Bucket Brigade, cuyo texto aparece en la línea histórica citada, en lugar de The Queen - Commanding Presence, que no tiene esa habilidad; Baloo se rotula como Delivery Pilot y PAYMENT UP FRONT al enlazar su imagen inglesa, correspondiente a la ficha francesa #188 conservada localmente. No se han cambiado los fallos de las dudas.

Se comprobó Publish: hay 15 páginas del catálogo (entrada y 14 fichas extensas; el set 14 todavía no estaba publicado), y ninguna de las 16 páginas legacy del inventario está publicada. Los cambios previos de Empates intencionales, el índice de casos y el workspace de Obsidian quedan fuera de la selección. La consulta auxiliar MCP de Fergus sigue recuperando su ficha completa con coincidencia exacta y cita verificada, mediante lectura actual en memoria porque el índice ya estaba desactualizado.

### Resultado público verificado

El commit de implementación `41480b15bb734faf82306d263edb608019cfbdb3` está en GitHub. Se publicaron selectivamente **152 páginas**: 149 artículos, portada, entrada breve y la plantilla, que también estaba publicada. Se comparó el contenido de las 152 respuestas públicas con los archivos locales y coinciden. Las 240 imágenes distintas que realmente enlazan los artículos migrados y el artículo de Héctor están dentro de las 241 imágenes comprobadas por HTTP. Se revisaron visualmente la atribución, los enlaces de personaje (Elsa), acción (All Is Found), localización (Sleepy Hollow) y reimpresión (Mulan en Fabled, #126/204 EN 9), y la legibilidad del artículo y la imagen de carta en tamaño móvil.

Se retiraron las **14 fichas extensas** que estaban publicadas; el set 14 ya estaba ausente. Publish conserva únicamente «Cartas de Lorcana» en esa carpeta pública. La lectura remota de cada ficha retirada devuelve «Not Found» (el servicio entrega ese mensaje con HTTP 200); sus 15 archivos locales conservan exactamente sus hashes anteriores. Las exclusiones evitan volver a publicarlos accidentalmente.

No quedan pendientes de esta selección. Las instrucciones, herramientas y registros de validación se suben al repositorio y no se publican en la bóveda. Los cambios previos en Empates intencionales, el índice y el workspace no se han incluido ni publicado. No se ha actualizado el índice de búsqueda del MCP: su recuperación actual en memoria fue comprobada.

Registros de cierre: [resultado](resultado-migracion-lorcast.json), [selección pública](seleccion-publicacion-lorcast.json), [verificación de las páginas](verificacion-publicacion-lorcast.json), [retirada y hashes locales](retirada-catalogo-lorcast.json), [mapa de correspondencias](mapa-cartas-lorcast.json) y [manifiesto de sustituciones](manifiesto-migracion-cartas.json).
