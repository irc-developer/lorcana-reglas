# Lectura personal de Duels

Cliente Python 3.10+ sin dependencias externas. Solo permite identidad, historial propio, los dos POST de manifiestos y descargas. No crea mesas ni modifica cuentas o mazos. El contrato de los POST los define como lecturas sin mutaciones; Duels sí registra el uso del token.

Referencia releída el 15/10/2026: [API oficial](https://duels.ink/api-docs) y [Markdown canónico](https://duels.ink/api-docs.md). [Contrato de salida v1](CONTRATO.md). [Verificación real y entrega](VERIFICACION.md).

Diagnósticos posteriores del contenido exportado: [incidencias locales](INCIDENCIAS.md). El auditor offline es independiente de la adquisición y no reclasifica automáticamente un archivo descargado como reconstrucción íntegra.

## Credencial

Configura `DUELS_TOKEN` en el entorno o en `.env` de la raíz. También admite `DUELS_API_TOKEN` y el alias local ya existente `duels-token`. `--token-env NOMBRE` elige otra etiqueta. Primero busca las alternativas en el entorno y después en el archivo. No pases el valor en argumentos. `--env-file RUTA` selecciona un archivo distinto.

El lector acepta asignaciones de una línea, comentarios, `export` opcional y valores simples o entrecomillados. No ejecuta el archivo ni interpola variables o comandos. Comprueba el formato de token personal documentado (96 caracteres hexadecimales); no implementa OAuth ni cookies. Los diagnósticos no incluyen cuerpos HTTP ni URLs privadas. No cambia, crea ni revoca credenciales.

## Uso desde la raíz del repositorio

Muestra pequeña en un directorio nuevo; el directorio predeterminado `../lorcana-trabajo/adquisiciones/duels/sample` ya contiene la prueba real:

```powershell
python herramientas/duels/duels.py --out ../lorcana-trabajo/adquisiciones/duels/ejemplo --limit 2 --max-pages 1 --download-games 1
```

Reanudar páginas de ese mismo lote, sin descargar más archivos:

```powershell
python herramientas/duels/duels.py --out ../lorcana-trabajo/adquisiciones/duels/ejemplo --max-pages 1
```

Descargar una partida ya enumerada y volver a ejecutar para comprobar la omisión de sus archivos verificados. Sustituye `g_example` por un ID del manifiesto, que es dato privado local:

```powershell
python herramientas/duels/duels.py --out ../lorcana-trabajo/adquisiciones/duels/ejemplo --skip-history --game-id g_example --download-games 1
```

Para enumeración histórica, la agente de datos elige límites temporales y un directorio **nuevo**. Ejemplo reproducible de ventana UTC, sin iniciarlo como parte de esta entrega:

```powershell
python herramientas/duels/duels.py --out ../lorcana-trabajo/adquisiciones/duels/historico-ventana-01 --from 2026-01-01T00:00:00Z --to 2026-10-16T00:00:00Z --limit 250 --max-pages 0
python herramientas/duels/duels.py --out ../lorcana-trabajo/adquisiciones/duels/historico-ventana-01 --skip-history --download-games 100
```

`--max-pages 0` enumera hasta el final; `--download-games 0` descarga **cero** partidas. Los valores predeterminados son una página, 10 filas/página y cero descargas. Las descargas operan sobre hasta N partidas pendientes, con replay y gamelog por separado. No hay opción implícita de descargar todo. `--game-id` es repetible, debe existir en ese lote y solo restringe descargas. El orden del diccionario `games` no expresa orden temporal. Para procesar lo pendiente, vuelve a ejecutar el comando con el mismo `--out`.

`--source all` (o ausencia de filtro) incluye todas las fuentes; también admite subconjuntos separados por comas de `matchmaking,private,bot`. `--queue` acepta IDs separados por comas y **solo limita filas de matchmaking**. No hay filtro de colores ni de nombre de mazo. El historial no documenta el nombre del mazo. La asociación con «ROTOR Investigaorets» necesita evidencia adicional del `your_deck_id`, sin extender aquí la lista de endpoints.

## Ventanas y reanudación

`from` es inclusivo y `to` exclusivo sobre la **última actualización del registro**, no el inicio de la partida. Se exige zona horaria; se normaliza a UTC. Si omites `to`, se congela el instante inicial del lote. El servidor conserva el orden y se usa literalmente su cursor opaco, secuencialmente. No se calcula el cursor ni un watermark a partir de las fechas de inicio/fin.

Cada `--out` fija su cuenta y sus parámetros (`limit` incluido). Al reanudar, omite los filtros para heredar los guardados o repítelos exactamente. Para otra ventana o tamaño de página usa otro directorio. `state.enumeration_complete` acredita final de esa ventana; terminar una ejecución con éxito no significa que haya terminado el historial. Las actualizaciones posteriores se adquieren en un lote nuevo, con ventanas solapadas, y la agente de datos consolida por `(account_id, game_id)`, conservando las versiones y procedencias. El cliente deduplica por `game_id` dentro de cada lote.

Se guarda un checkpoint atómico después de cada página validada y cada intento de archivo. Un fallo en la página deja el cursor anterior para repetirla; una página recibida con formato inválido se conserva como observación sin avanzar el checkpoint. Un cierre abrupto puede dejar originales sin referencia; no se borran. `.lock` evita escritores simultáneos por directorio. Si queda tras un cierre abrupto, comprueba que su PID no sigue ejecutándose y retíralo manualmente. Ejecuta también adquisiciones de directorios distintos secuencialmente, pues comparten los cupos de la cuenta.

## Descargas, límites y fallos

La implementación mantiene una petición simultánea, separa peticiones de historial por al menos 3,1 s y las demás de cada grupo por 2,1 s. Respeta agotamiento de `X-RateLimit-Remaining/Reset`, `Retry-After` numérico/fecha y `retryAfterSeconds`. Hace hasta tres reintentos adicionales ante 429, 5xx o fallos de red. Las esperas largas se dividen en tramos de 30 s para permitir interrupción. Un 401 detiene toda la importación inmediatamente; comprueba token, caducidad, revocación o alcance antes de reanudar. Los 403 no se reintentan automáticamente.

Las redirecciones se siguen manualmente, solo con HTTPS y hasta seis saltos. `Authorization` solo puede enviarse al origen exacto `https://duels.ink` y las rutas autorizadas. Se elimina tras el primer salto y nunca se reintroduce en una cadena de redirecciones. El CDN no recibe la credencial. Cada archivo obtiene un manifiesto individual, suficiente para lotes secuenciales; no se necesita batching para el piloto.

Antes de omitir un archivo `downloaded`, se comprueban los SHA-256 de su original y JSON. Si falla la integridad, se vuelve a adquirir y se conservan los bytes dañados. Las respuestas y descargas usan nombres basados en hash; nunca se usan IDs ni `filename` del servidor como rutas. Los bytes gzip originales y los bytes JSON descomprimidos se guardan por separado. No se reserializa el JSON original para archivarlo.

`unavailable` no se vuelve a pedir salvo `--retry-unavailable`; los fallos de descarga sí se reintentan al procesar la partida. Ni `missing` ni HTTP 404 demuestran caducidad: puede ser falta de preparación, permiso o disponibilidad. No se promete recuperar todo el histórico.

Salida: JSON breve sin IDs/URLs de descargas; códigos 0 = ejecución correcta (puede quedar material pendiente/no disponible), 1 = fallo global/interrupción/autenticación, 2 = hay algún archivo con `download_failed` en el lote. El estado detallado siempre se consulta en el manifiesto. `--skip-history` omite páginas, pero mantiene la comprobación de identidad.

## Pruebas y verificación local

```powershell
python -m unittest discover -s herramientas/duels -v
python herramientas/duels/verificar_muestra.py --out ../lorcana-trabajo/adquisiciones/duels/sample
```

El segundo comando no usa red. Verifica hashes y procedencias de filas, descomprime, aplica el extractor existente por partida, contrasta la lista propia del historial y compara con el piloto anterior cuando es la misma partida. El extractor no es una autoridad de reglas. Su función `extract()` se reutiliza sin el `main()` que exige mismo encuentro y misma lista en todos los archivos.

El verificador genera derivados privados en `verification/`; no se usan como datos nuevos de adquisición ni como vistas para enseñar decisiones. El replay y los derivados contienen resultado, orden del mazo y futuro. La fase docente tendrá que generar una vista que los excluya efectivamente.

`local/` y cachés de Python están excluidos mediante el `.gitignore` de este componente. Usa un destino privado igualmente excluido si eliges otro `--out`; no añadas manifiestos ni originales a commits o Publish. El lote queda en disco local y OneDrive según la configuración de Iván; esta herramienta no lo envía a servicios de análisis.
