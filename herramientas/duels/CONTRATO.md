# Contrato de adquisición Duels v1

Estado de entrega: **v1 utilizable**, 15/10/2026. Propietario de cliente, credencial, HTTP, cursores y descargas: `herramientas/duels/`. La fase de datos consume este contrato y usa la CLI para nuevas adquisiciones; no necesita reimplementar HTTP. No modifica los originales ni el manifiesto del cliente. La selección y consolidación del histórico pertenecen a esa fase. No hay cambios en `../lorcana-trabajo/analisis/profesora-lorcana/DISENO.md` ni `COORDINACION.md`.

Esquemas JSON Schema 2020-12: [manifest-v1.schema.json](schemas/manifest-v1.schema.json), [history-row-v1.schema.json](schemas/history-row-v1.schema.json). Son documentación de intercambio; el cliente valida invariantes esenciales sin instalar un validador de JSON Schema. Campos adicionales de Duels se conservan. Un cambio incompatible incrementará `schema_version`; los consumidores deben rechazar versiones desconocidas y admitir campos adicionales de v1.

## Unidad y claves

Un directorio de adquisición contiene `manifest.json` y `raw/`; opcionalmente `verification/` con derivados de comprobación. Todas las rutas del manifiesto son relativas al directorio de adquisición. No se debe aceptar ninguna ruta que escape de él. Los nombres originales sugeridos se guardan como metadatos, nunca como rutas.

La clave global es `(source, account.id, game_id)`; en este origen basta `(account_id, game_id)`. `match_id` agrupa un encuentro y puede ser nulo. `match_game_number` no es el ID de partida. No contar un encuentro BO3 y sus juegos como unidades equivalentes. Los IDs y los cursores son opacos: ni analizarlos ni fabricarlos. El orden de las claves de `games` no es cronológico.

## Manifiesto

| Campo | Contrato |
| --- | --- |
| `schema_version` | Entero `1` |
| `source` | `https://duels.ink` |
| `created_at`, `updated_at` | Instantes de adquisición/checkpoint UTC, ISO 8601 |
| `account` | Respuesta íntegra de `/api/me`: `id` estable, `name` mutable, avatar y metadatos del token. No contiene el token secreto |
| `parameters` | Consulta fija: `format=json`, `limit` 1–250, `to` exclusivo obligatorio, `from` inclusivo opcional, `source`/`queue` opcionales |
| `state` | `next_cursor` literal o null, `enumeration_complete`, `pages` comprometidas; `cursor_hashes` auxiliares para detectar ciclos |
| `observations[]` | Cada respuesta de API recibida y aceptada como JSON: `endpoint`, `parameters`, `acquired_at`, `file`, `headers` permitidas |
| `games` | Objeto indexado por `game_id`; entrada definida abajo |
| `errors[]` | Fallos globales capturados: `at`, código seguro y `recoverable`. Un fallo anterior a identificar una cuenta puede no tener manifiesto |

**Las observaciones del historial se reconocen mediante `endpoint == "/api/me/match-history"`**, no hay campo `history_page` ni discriminador `type`. Sus `parameters` incluyen el cursor usado si lo hubo; el archivo original contiene `{games,next_cursor}`. Se conservan también páginas inválidas como evidencia: `state.pages` es el número validado y comprometido, no necesariamente el número de observaciones. No contar dos veces una página repetida ni asumir que cada observación avanzó el checkpoint. Comprobar las filas mediante `games.*.row_source` o las versiones referenciadas.

`headers` solo incluye tipo de contenido, ETag/última modificación y límites de frecuencia. Nunca guarda `Authorization`, cookies ni cabeceras completas. Los cuerpos se archivan tal como se recibieron. Cuerpos HTTP de errores no se imprimen ni se archivan, para evitar volcados sensibles.

## Entrada por partida

| Campo | Contrato |
| --- | --- |
| `game_id`, `account_id` | Claves estables; coinciden con la clave del diccionario y `row.your_user_id` |
| `row` | Fila íntegra de historial, sin cambios de nombres ni normalización de valores |
| `row_source` | Referencia de la observación más reciente: `file`, `index` base cero dentro de `games`, `acquired_at`, `row_sha256` |
| `row_versions[]` | Referencias de contenidos diferentes sucesivos. Si una observación repite la misma fila, no añade versión, pero permanece en `observations` |
| `assets.replay`, `assets.gamelog` | Estados de archivo independientes; definidos debajo |
| `previous_assets[]` | Si cambia un ID de archivo, conserva el estado anterior con `kind` |

La `row` retiene todos los campos presentes del contrato oficial: encuentro, posición inicial, cola, temporada, MMR propio/rival, resultado, deck ID y `your_decklist`, incluyendo nulos y campos adicionales. **La lista propia es la de esa partida**, no la lista actual del mazo. No imponer 60 cartas ni asumir misma composición por deck ID o colores. El nombre «ROTOR Investigaorets» no aparece como campo documentado del historial; la muestra tampoco tiene `your_deck_name`. Necesita vinculación independiente con evidencia. Una composición coincidente con el piloto es una candidata, no una atribución histórica automática.

No hay lista rival completa en el historial. No rellenarla ni inferirla en esta fase. Los originales son evidencia de Duels, no normativa de Lorcana.

`row_sha256` es SHA-256 de la fila serializada por `duels.encode()` (UTF-8, `ensure_ascii=False`, `sort_keys=True`, `indent=2`, salto final). Sirve para detectar revisiones dentro del cliente. Para integridad del archivo se usa siempre el SHA del **cuerpo original**, no una reserialización. Un consumidor puede comprobar la referencia abriendo `file.path`, verificando hash, y seleccionando `page.games[index]`.

## Archivos e intentos

Toda referencia `file`, `original` o `json` contiene `{path,sha256,bytes}`. El hash es hexadecimal SHA-256 de los bytes guardados y `bytes` su longitud. `raw/<sha>.gz` conserva exactamente la descarga gzip. `raw/<sha>.json` conserva los bytes descomprimidos o la respuesta JSON recibida sin compresión. Un mismo contenido puede compartir archivo. Si un nombre existente contiene bytes dañados, se conserva y el contenido recuperado usa `-recovered-<ns>`.

Cada asset tiene `id` (replay ID o game ID para logs), `status` y `attempts[]`:

| `status` | Significado y reanudación |
| --- | --- |
| `pending` | No intentado todavía o intento interrumpido antes de determinar estado |
| `absent` | Historial sin `replay_id`; no se solicita manifiesto de replay |
| `unavailable` | `manifest_missing` o HTTP 404/410. Puede estar sin preparar, no accesible o retirado; **no demuestra expiración**. Reintento explícito con `--retry-unavailable` |
| `download_failed` | Red, HTTP distinto de los anteriores, integridad local o formato/identidad inválidos. Se puede reintentar en otra ejecución |
| `downloaded` | Descarga, descompresión, lectura JSON y comprobación estructural correctas. Tiene `original`, `json`, `acquired_at`, `validation`; no certifica por sí sola reconstrucción íntegra |

Cada intento tiene `at`; puede añadir `manifest` (observación completa), `file` (id/filename/url del manifiesto), `redirects` (URL/status), `original`, `json` y `status`. Es posible conservar originales de un intento fallido sin marcarlos como descargados. Un 401 registra `authentication_failed` en el intento y detiene globalmente; no debe convertirse en `unavailable`. Tras una interrupción puede existir un intento solo con `at`; se reintentará. `error` contiene código seguro, `http_status` opcional, `at` y `recoverable`. Esta última propiedad significa que se puede volver a intentar, no que se haya demostrado recuperable en el servidor. El 401 requiere intervención en la credencial, nunca un bucle automático.

La validación de entrada de replay comprueba `duels-replay-v1`, `gameId`, perspectiva, `viewingAs` y tipos de `baseSnapshot/frames/logs`. Para gamelog solo exige objeto o lista JSON, porque la referencia HTTP no especifica su estructura interna. La muestra real es una lista de eventos. `verificar_muestra.py` hace las comprobaciones adicionales con el extractor y registra su hash en el informe.

Las URLs de `row`, manifiestos y redirecciones pueden conceder acceso al replay. Estos datos son **privados**, necesarios para adquisición y procedencia; no publicarlos, copiarlos a respuestas de chat ni enviarlos a otros servicios. Los consumidores pasan rutas locales y claves a la fase de análisis.

## Ejemplo ficticio de consumo sin secretos

```python
import hashlib
import json
from pathlib import Path

folder = Path('../lorcana-trabajo/adquisiciones/duels/sample').resolve()
m = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
assert m['schema_version'] == 1
for game_id, entry in m['games'].items():
    assert entry['account_id'] == m['account']['id']
    assert entry['row']['game_id'] == game_id
    assert entry['row']['your_user_id'] == entry['account_id']
    for kind, asset in entry['assets'].items():
        if asset['status'] != 'downloaded':
            continue
        ref = asset['original']
        local = (folder / ref['path']).resolve()
        assert local.is_relative_to(folder)
        content = local.read_bytes()
        assert len(content) == ref['bytes']
        assert hashlib.sha256(content).hexdigest() == ref['sha256']
        # Registrar (account_id, game_id, kind, local, sha256) sin revelar URLs.
```

La agente de datos debe registrar el lote y su ventana, unir por clave estable, conservar todas las procedencias y presentar por separado cobertura de filas, replay y gamelog. Un lote con `enumeration_complete=false` no permite conclusiones de cobertura histórica. Para actualizar, crear una ventana nueva con solapamiento temporal sobre última actualización y consolidar después; no editar cursores a mano. La vista docente que impide información futura sigue pendiente en la fase de análisis.
