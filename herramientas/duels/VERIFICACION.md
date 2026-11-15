# Entrega y verificación de la infraestructura Duels

Fecha: 15 de octubre de 2026. Contrato **v1 utilizable y estable para la entrega a datos**. Se ha implementado y probado el acceso real; no es una propuesta pendiente de autenticación. Esta tarea no ha iniciado una importación histórica completa ni análisis estratégico.

## Rutas definitivas

| Componente | Ruta desde la raíz del checkout |
| --- | --- |
| Cliente e importador/CLI | `herramientas/duels/duels.py` |
| Instrucciones reproducibles | `herramientas/duels/README.md` |
| Contrato de intercambio | `herramientas/duels/CONTRATO.md` |
| Esquemas JSON Schema | `herramientas/duels/schemas/manifest-v1.schema.json`, `history-row-v1.schema.json` |
| Pruebas sin red | `herramientas/duels/test_duels.py` |
| Verificación offline con el extractor existente | `herramientas/duels/verificar_muestra.py` |
| Muestra privada real | `../lorcana-trabajo/adquisiciones/duels/sample/manifest.json` y `raw/` |
| Informe privado de reconstrucción y hashes | `../lorcana-trabajo/adquisiciones/duels/sample/verification/report.json` |

Checkout: `C:\Users\plata\OneDrive\Documentos\Proyectos\lorcana-reglas`. Los originales, manifiestos y derivados de la muestra están excluidos de Git mediante `herramientas/duels/.gitignore`. `.env` sigue excluido por la configuración previa de la raíz. No se ha cambiado ni expuesto la credencial, ni se han creado/revocado tokens. No se han creado chats o subagentes, ni hecho commits, push o Publish en esta entrega. Se han preservado cambios previos del checkout y los archivos de diseño/coordinación.

## Comprobaciones reales con Duels

La [referencia Markdown canónica](https://duels.ink/api-docs.md) se ha descargado sin autenticación y releído antes de implementar. El primer intento directo quedó bloqueado por el sandbox; con permiso de red un cliente sin cabecera estándar obtuvo 403. La petición con `User-Agent` estándar recibió HTTP 200. El cliente incluye esa cabecera y las peticiones autenticadas funcionaron.

| Prueba | Resultado observado |
| --- | --- |
| `GET /api/me` con la configuración local | Cuenta **Shinobana**, coincidente con el piloto anterior; ID estable presente y conservado solo en los artefactos privados |
| Metadatos del token utilizado | Token personal, `scopes=null`, `expiresAt=null`; esto no impide que pueda revocarse posteriormente |
| Primera página con `limit=2` | Dos filas propias, `your_user_id` igual a la cuenta confirmada, cursor siguiente no nulo |
| Manifiestos de replay y gamelog de una de esas partidas | Ambos disponibles, respuestas originales conservadas |
| Descargas de esa misma partida | Replay gzip de **73.008 bytes** y gamelog gzip de **17.238 bytes**, ambos HTTP 200 y JSON válido tras descomprimir |
| Segunda ejecución para esa partida, con `--skip-history --game-id … --download-games 1` | **Una petición HTTP de identidad, cero páginas nuevas, cero manifiestos y cero descargas**; ambos archivos omitidos tras verificar SHA-256 |
| Siguiente página del mismo lote | Se envió el cursor guardado sin reconstruirlo; dos filas adicionales, cuatro `game_id` únicos en total, sin descargar más archivos |

La muestra contiene **dos páginas, cuatro partidas y un par replay/gamelog**. `state.enumeration_complete=false`: quedan páginas fuera de esta muestra. Hay siete respuestas API originales en `observations`. Los dos archivos de esa partida tienen un solo intento de adquisición cada uno. Las otras tres partidas permanecen `pending` para ambos tipos de archivo.

En la prueba real los manifiestos entregaron descargas directas que respondieron 200, sin saltos de redirección. La eliminación de `Authorization` al CDN y en cadenas que vuelven al origen se probó con transporte simulado; no se provocaron redirecciones artificiales en el servicio.

## Integridad y compatibilidad con el extractor previo

Comando local ejecutado con éxito:

```powershell
python herramientas/duels/verificar_muestra.py --out ../lorcana-trabajo/adquisiciones/duels/sample
```

Resultado final: **19 referencias comprobadas** entre respuestas, filas canónicas, versiones y archivos; son referencias verificadas, no un recuento de archivos distintos. Se validaron tamaños/SHA-256, coincidencia de cada fila canónica con su página y coincidencia exacta entre el JSON descomprimido y su copia conservada. El informe registra también el hash del extractor utilizado, `../lorcana-trabajo/analisis/duels-2026-10-15/extraer_replays.py`.

El replay declara `duels-replay-v1`; se aplicaron sus **169 frames** y se contabilizaron sus **536 logs**. El extractor confirmó conservación inicial de la lista, coherencia de `deckOrder/deckCount`, 60 cartas propias en el estado final y coincidencia del resultado con el encabezado. La composición propia del historial coincide por `cardId` y cantidades con el replay. Estas 60 cartas pertenecen a **esa partida**, no se atribuyen al histórico completo.

Se contrastó esa partida con la extracción manual previa: coinciden game ID, match ID, número de partida, perspectiva, ganador, número de frames/logs y composición. Los nombres recuperados no se utilizan como clave de composición, porque el catálogo observado puede variar entre archivos.

El gamelog real es una **lista de 537 objetos de evento**. Contiene los 536 IDs de evento del replay y un evento adicional `INITIAL_HAND`. Se conservan ambos originales sin eliminar ni interpretar ese evento. Esto acredita compatibilidad estructural de la muestra; no demuestra que un gamelog sin replay permita reconstruir completamente otra partida ni que todas las versiones de exportación tengan este esquema.

Los archivos incluyen información futura y privada del jugador. Esta entrega no construye todavía una vista docente ni usa los datos para evaluar decisiones, enfrentamientos o cambios de mazo.

## Pruebas locales del cliente

```powershell
python -m unittest discover -s herramientas/duels -v
```

**19 pruebas superadas**, sin red ni credenciales reales. Cubren cursores opacos y ciclos, reanudación tras fallo, página inválida sin avance parcial, deduplicación y conservación de revisiones/listas, credencial/cuenta/ventana incorrectas, flujo completo de CLI, bloqueo de escritores, escritura atómica, omisión de archivos verificados, detección y conservación de archivos dañados, replay de otra partida, `missing`/404/410/fallo de red, 401 sin reintento, 429/Retry-After/cupos, reintentos 5xx acotados, retirada de credencial al redirigir, rutas fuera de alcance, fechas UTC y lectura del `.env` sin ejecutar su contenido.

También se comprobaron ambos esquemas y el manifiesto real con el `jsonschema` ya disponible en el entorno, con resolución de referencias únicamente local. Esa biblioteca **no es dependencia** del cliente ni de la suite de pruebas. Git confirma que el manifiesto de muestra, el informe local y `.env` están ignorados.

## Entrega a la fase de datos

El consumidor puede empezar con el manifiesto de muestra y el [contrato v1](CONTRATO.md). Las páginas se descubren por `observations[].endpoint == "/api/me/match-history"`; no existe discriminador `history_page`. La fila canónica del lote está en `games[game_id].row`, su procedencia en `row_source` y sus revisiones en `row_versions`. Los estados de replay/gamelog son independientes. No escribir en el manifiesto ni en `raw/` desde el adaptador de datos.

Para una ventana histórica nueva, usar otra salida privada y los comandos de README. Esa fase decide la ventana, el tamaño de lote y la selección de descargas; ejecutará la CLI secuencialmente. Para nuevas actualizaciones, ventanas solapadas sobre última actualización y consolidación por `(account_id, game_id)` conservando procedencias. No reimplementar HTTP ni sustituir cursores por fechas de inicio/fin.

Pendientes verificados o delimitados:

- **Cobertura histórica:** no medida. No se consultaron archivos antiguos para forzar caducidades ni se promete su disponibilidad. Los estados no disponibles se han probado localmente, no observados en esta muestra real.
- **Identidad exacta de «ROTOR Investigaorets»:** el historial no entrega nombre de mazo; conserva `your_deck_id` y la composición por partida. Hace falta evidencia del vínculo nombre–ID. Colores o coincidencia con una composición del piloto solo permiten candidatos, no atribución histórica.
- **Filtros temporales y fuentes:** semántica implementada conforme al contrato y normalización UTC probada. No se agotaron ventanas reales ni todas las combinaciones de filtros para evitar llamadas innecesarias. El intervalo se aplica a última actualización, no inicio de partida.
- **Escala y formatos futuros:** no hay prueba masiva, garantía de retención, OAuth ni soporte automático de versiones futuras del replay. Un gamelog objeto/lista pasa lectura estructural; el verificador de muestra exige la lista de eventos observada y falla de forma explícita si cambia.
- **Vista docente y estrategia:** siguen a cargo de análisis. No usar resultado, `deckOrder` ni robos futuros para valorar decisiones anteriores.

La revisión automática rechazó los intentos iniciales de mensajes de coordinación por no considerar la autorización reenviada como permiso directo de Iván. No se enviaron esos mensajes ni se intentó otra vía. La entrega queda en estos archivos para que el chat coordinador la inspeccione y transmita, como indicó después. Este bloqueo no afecta al cliente ni a la prueba autenticada.
