# Recopilar un canal de Discord al desplazarse

Este recopilador guarda en memoria los mensajes que Discord muestra mientras recorres manualmente un canal. Conserva lo acumulado aunque la lista retire mensajes anteriores de la página y evita duplicados mediante el ID de mensaje. No requiere instalar un bot.

Para un foro con tarjetas de publicaciones y un hilo lateral, usa **`capturar-foro.js`** y las instrucciones de la sección siguiente. `capturar-mensajes.js` sirve para un canal de mensajes y excluye deliberadamente otros IDs de canal, incluidos los hilos laterales.

## Foros: tarjetas con preguntas y respuestas

1. Abre Discord web en Chrome y entra en la **lista de tarjetas del foro** (como `rules-questions`). Inicia aquí el recopilador, no desde la URL de una publicación aislada. Puedes dejar una tarjeta abierta en el panel lateral.
2. Copia todo `capturar-foro.js` y ejecútalo en la consola (`Ctrl+Shift+J`). No hace falta volver a ejecutarlo con cada tarjeta. Tiene su propio objeto `lorcanaForo`, independiente de la captura anterior.
3. Abre una tarjeta **en esa misma pestaña y en el panel lateral**. Espera a que cargue y recorre su contenido desde la pregunta inicial hasta las últimas respuestas. Si hay respuestas anteriores sin cargar, desplázate también hacia arriba.
4. Ejecuta `lorcanaForo.estado()`: muestra cuántas publicaciones y mensajes ha guardado, con un detalle por publicación. `preguntaInicialCapturada: true` significa que se ha visto el mensaje inicial, **no** que el hilo esté completo.
5. Abre otra tarjeta. Se conservará la anterior y se acumulará la nueva en su propio grupo. Reabrir una tarjeta no duplica sus mensajes.
6. Descarga periódicamente con `lorcanaForo.descargar()`. Obtendrás un solo JSON con las publicaciones agrupadas y sus mensajes ordenados. Descarga antes de recargar o cerrar la pestaña.
7. Al terminar, ejecuta `lorcanaForo.detener()`. El JSON sigue disponible para descargar mientras mantengas la pestaña abierta.

**Primera prueba:** abre dos tarjetas cortas y comprueba que aparecen dos publicaciones, cada una con su pregunta y las respuestas que has visto. Después continúa con el resto.

La vista de tarjetas solo contiene resúmenes: pasar por ella no descarga las respuestas de cada publicación. Hay que abrir las publicaciones que se deseen recopilar. Los filtros activos del foro limitan las tarjetas que puedes encontrar; revisa los filtros de etiquetas y el orden si quieres recorrer más dudas.

El recopilador busca el título en los encabezados del panel del hilo. El campo `titleSource: "panel-heading-heuristic"` señala este método; comprueba los títulos en la primera prueba. Si no puede reconocer uno, lo deja vacío. Puedes fijarlo manualmente con `lorcanaForo.titular("ID_DEL_HILO", "Título exacto")`; usa el ID del detalle de `estado()`.

Cada mensaje conserva su ID, enlace de origen, texto, autor y fecha cuando se muestran, además de enlaces a imágenes y adjuntos. **No descarga las imágenes ni interpreta las respuestas como rulings confirmados.** El archivo es material de trabajo para su posterior contraste con las reglas y comparación con la wiki.

El foro y cada hilo tienen IDs diferentes. Se aceptan los hilos observados desde la vista inicial del foro y se permite continuar en una publicación reconocida abierta a pantalla completa. Si cambias a un canal desconocido o a otro servidor, se detiene y conserva lo acumulado. Si una tarjeta cambia de URL antes de que se reconozcan sus mensajes, usa el panel lateral desde la lista del foro; descarga y recarga para iniciar una nueva sesión si ya se detuvo.

Los selectores dependen del HTML de Discord. Se han probado con mensajes simulados, no con una sesión autenticada real. Si el contador sigue a cero tras abrir una tarjeta, hace falta revisar su HTML; una captura de pantalla no permite verificar los identificadores internos.

## Uso en Chrome para Windows

1. Abre `https://discord.com/app`, inicia sesión y entra en el canal de dudas. Cierra el panel de búsqueda para trabajar sobre la conversación del canal.
2. Abre `capturar-mensajes.js` en un editor y copia su contenido completo.
3. En Discord web, pulsa `Ctrl+Shift+J` para abrir la consola. Ejecuta allí el contenido del archivo. El código lee el contenido de la página: no obtiene tokens, no consulta la API y no envía mensajes.
4. Debe aparecer «Captura iniciada» y un número de mensajes mayor que cero. Si aparece un error de reconocimiento, el HTML de Discord puede haber cambiado: conserva el error para adaptar el recopilador.
5. Desplázate manualmente hacia mensajes anteriores, esperando a que cada bloque cargue. Puedes cerrar las herramientas de desarrollo y volver a abrirlas; conserva abierta la pestaña de Discord.
6. Comprueba periódicamente el contador ejecutando `lorcanaCaptura.estado()` en la consola.
7. Ejecuta `lorcanaCaptura.descargar()` para descargar un JSON con todo lo acumulado hasta ese momento. Puedes hacerlo varias veces; cada descarga contiene también los mensajes anteriores.
8. Para finalizar la observación ejecuta `lorcanaCaptura.detener()`. Aún puedes descargar los datos después de detenerla.

Haz una primera prueba con dos o tres bloques: comprueba que el contador aumenta y que el JSON conserva tanto mensajes recientes como antiguos. Después continúa con el intervalo necesario.

## Alcance y límites

- La captura está en memoria. Recargar o cerrar la pestaña la pierde: descarga periódicamente.
- Solo recopila el canal en cuya URL se inició. Al detectar un cambio de canal se detiene; los mensajes acumulados siguen disponibles para descargar. Para otro canal o hilo, usa otra pestaña y una captura independiente.
- No demuestra que se haya recorrido todo el historial. Saltar a una fecha puede dejar huecos: recorre de forma continua el intervalo que necesites.
- Guarda ID, enlace de origen, texto mostrado, autor y fecha cuando están disponibles, y enlaces de medios. Algunos mensajes agrupados no muestran el autor; ese campo queda vacío sin inventarlo.
- El texto mostrado puede incluir respuestas citadas, reacciones y etiquetas de la interfaz; habrá que depurarlo antes de convertirlo en casos.
- No descarga archivos ni hace OCR. Los enlaces de adjuntos pueden caducar. Si una duda depende de una imagen, habrá que conservar ese adjunto por separado.
- El JSON puede contener nombres y mensajes de participantes. Es material de trabajo: guarda la exportación fuera de las carpetas publicadas de la wiki. Para los casos finales usaremos el contenido necesario y contrastaremos las respuestas con fuentes de reglas.
- El selector del HTML de Discord es un detalle interno que puede cambiar. Se valida sobre mensajes simulados, pero requiere comprobar el contador en tu sesión real.

## Referencias

- [MutationObserver: observar cambios de la página](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/observe).
- [Abrir las herramientas de Chrome](https://developer.chrome.com/docs/devtools/open).
- [Foros e hilos en Discord](https://docs.discord.com/developers/topics/threads).

No se ha extraído ningún mensaje real al preparar esta herramienta.
