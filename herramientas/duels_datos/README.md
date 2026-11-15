# Catálogo local de Duels

Consolida evidencia ya descargada. Solo biblioteca estándar de Python; no abre conexiones, no lee `.env`, no adquiere archivos y no publica. Los originales permanecen en su ubicación; nunca se modifican. Los catálogos personales deben guardarse en `../lorcana-trabajo/analisis/profesora-lorcana/datos/privado/`, excluido de Git mediante el `.gitignore` de esa carpeta. El código, los tests y esta documentación son independientes de los datos personales.

Desde la raíz del repositorio:

```powershell
python -m unittest herramientas.duels_datos.test_catalogo -v
python -m herramientas.duels_datos.catalogo build --manual ../lorcana-trabajo/analisis/duels-2026-10-15 --out ../lorcana-trabajo/analisis/profesora-lorcana/datos/privado/lotes
python -m herramientas.duels_datos.catalogo verify RUTA_DEL_LOTE
python -m herramientas.duels_datos.catalogo query RUTA_DEL_LOTE --selection candidate
python -m herramientas.duels_datos.catalogo query RUTA_DEL_LOTE --game-id ID --full
```

`query` admite también `--match-id`. Su salida breve omite listas y rutas; `--full` entrega el registro personal completo. Los catálogos no contienen URLs de replays ni de manifiestos privados, ni cursores. **Siguen siendo datos personales locales**, aunque se eliminen esas URLs.

## Entradas

1. `--manual DIRECTORIO`: utiliza los resúmenes `partida-*-resumen.json`, sus originales referidos y los estados/acciones/eventos asociados. Verifica SHA-256, JSON, partida, perspectiva, estructura del replay y coincidencia de la lista original con el resumen. Conserva hashes y rutas de todos los derivados; comprueba secuencias, intervalos de eventos, cantidades y estado final. No vuelve a ejecutar los parches: el informe de extracción conserva esa validación anterior.
2. `--manifest RUTA_MANIFEST_JSON`: adaptador directo al `schema_version=1` del cliente `herramientas/duels/duels.py`. Lee las páginas originales de `observations` para conservar todas las filas, incluidas versiones repetidas. Comprueba hashes y `your_user_id`, examina `games.assets` y vuelve a verificar los archivos existentes. No ejecuta el cliente. Las descargas deben realizarse mediante la CLI de infraestructura cuando el coordinador asigne esa fase.
3. `--contract RUTA_JSON`: contrato local alternativo `duels-datos-input-v1`, documentado más abajo. No es necesario convertir el manifiesto de infraestructura a este formato.

Se pueden combinar las entradas; `--manifest` es repetible para reutilizar la muestra sin volver a descargar sus archivos. **Por defecto no se fusiona una cuenta manual sin ID con una cuenta API**. `--link-manual-account` exige coincidencia de game ID, perspectiva y huella exacta de impresión con una única cuenta API antes de unirla. `--account-id ID` permite también una atribución explícita previamente verificada. Sin esa comprobación se conserva `account_id: null` y `account_scope: manual-name:…`, clave local provisional que no representa un ID de Duels. En el lote histórico ya se ha comprobado la vinculación del piloto.

## Lotes e interfaz

Cada lote vive en un directorio cuyo nombre es el SHA-256 de su manifiesto de artefactos. Una segunda ejecución con las mismas entradas devuelve el mismo directorio y compara cada byte. Un lote alterado provoca error; no se sobrescribe. Las escrituras iniciales usan un directorio temporal y un cambio de nombre al completar los archivos.

El checkpoint mutable del cliente se copia por hash a `privado/entradas/` antes de referenciarlo: una reanudación posterior no invalida los lotes anteriores. El cliente conserva su checkpoint original. Los archivos y páginas referidos por este deben permanecer dentro del directorio de adquisición; el adaptador rechaza rutas que escapan de él.

| Archivo | Contrato |
| --- | --- |
| `manifiesto.json` | `duels-datos-batch-v1`, ID del lote y SHA-256 de cada artefacto |
| `catalogo.jsonl` | Una fila por `(account_scope, game_id)`; IDs de cuenta/encuentro/partida, número, resultado, perspectiva, fechas UTC, cola/temporada/contexto, ausencias y procedencia |
| `encuentros.jsonl` | Asociación por cuenta, `match_id` y partidas; no deduce un resultado de encuentro ni añade partidas que falten |
| `composiciones.jsonl` | Asociación de cada huella de composición con sus partidas; la composición concreta está en `catalogo.deck` |
| `fuentes.json` | Ruta, hash, tamaño y tipo de cada documento de entrada; las filas apuntan al hash y al índice de la fila original |
| `normalizacion.json` | Mapa ID de impresión → identidad y composiciones piloto utilizadas como candidatas |
| `seleccion.json` | Evidencia adicional de selección, si se aporta `--selection-evidence` |
| `cobertura.json` | Partidas/encuentros, listas ausentes, estados de archivos, selección ROTOR, anomalías y alcance de paginación |

`catalogo.sources` conserva **cada observación**, incluso duplicados idénticos; `observation_count` permite identificarlos. `field_sources` documenta de dónde sale cada valor no nulo. `deck_observations` conserva cada lista original, también las ausentes. Se priorizan las páginas API frente a resúmenes y después `updated_at`, fecha de consulta y desempate determinista por hash/índice. Si falta `updated_at`, no se fabrica: la fecha de consulta sirve solo para ordenar las observaciones. Los desacuerdos se conservan en `conflicts`. `deck` es la última lista observada: una lista nula posterior **no se sustituye** por una antigua. Los valores escalares no nulos anteriores pueden permanecer como evidencia adicional, con procedencia y ausencias por observación explícitas.

`files.replay` y `files.gamelog` distinguen `not_requested`, `pending`, `absent`, `unavailable`, `download_failed`, `absent_local`, `hash_mismatch`, `corrupt_or_unsupported` y `verified_json`. Conservan el estado declarado por infraestructura en `infrastructure_status` cuando procede. `file_observations` preserva además las referencias y estados de cada observación, incluidos los originales manuales si posteriormente se adquiere el mismo juego por API. `verified_json` acredita hash/JSON y, para replay, identidad/perspectiva/estructura; no acredita reconstrucción semántica ni que un log baste para enseñar. Los gamelogs no tienen un esquema interno certificado: se valida JSON, no se fabrica una asociación desde su contenido. Se conservan los hashes del comprimido original y del JSON descomprimido cuando el cliente proporciona ambos. `cobertura.file_statuses_by_selection` separa cobertura segura, candidata y pendiente.

`verify` comprueba manifiesto, hashes de artefactos, documentos de entrada, originales y derivados actuales. Devuelve código 1 si algo cambió. La inmutabilidad es una convención respaldada por hashes, no un bloqueo de escritura del sistema de archivos. Si se mueve o cambia un original, el lote conserva la referencia anterior y la auditoría lo detecta.

## Huellas y normalización

- `printing_sha256`: agrega cantidades por ID exacto y ordena por ID. Ignora orden de filas y distribución en filas duplicadas; conserva la lista original completa.
- `composition_sha256`: agrega cantidades por identidad de carta. El mapa utilizado se guarda en `normalizacion.json`. No elimina sufijos de IDs ni deduce equivalencias por números, colores o similitud.
- En el piloto, las identidades son `full-name:` más el nombre completo inglés **observado en la extracción**, normalizado únicamente mediante Unicode NFKC y espacios exteriores. Incluyen personaje y versión. No se traducen, no se cambian mayúsculas ni puntuación. Es identidad descriptiva de ese corpus; no una verificación normativa del texto de las cartas.
- IDs sin correspondencia usan `unresolved-id:` y producen una huella provisional, con `identity_complete: false` y los IDs afectados. No se presenta una diferencia entre esos IDs como cambio estratégico confirmado. Una futura mejora del mapa puede cambiar la huella; siempre se comparan junto con la versión y el mapa.
- Las impresiones con identidad conocida compartida producen una misma huella de composición y una huella de impresión diferente. Las cantidades inválidas, listas inválidas o ausentes no obtienen una huella aparentemente válida. Listas de menos de 60 cartas se señalan sin corregirlas.

`identidades.py` amplía el mapa con `fullName` exacto presente en replays descargados, sin consultar red ni deducir a partir del ID. `--selection` restringe la lectura al subconjunto ya elegido. Registra cada replay fuente con hash; IDs con nombres contradictorios quedan sin resolver. El mapa se conserva como versión independiente y se incorpora a `build --observed-identities RUTA`. No se sobrescriben mapas anteriores diferentes.

```powershell
python -m herramientas.duels_datos.identidades --manifest RUTA_MANIFIESTO --selection RUTA_SELECCION_PRIVADA --out RUTA_MAPA_NUEVO
python -m herramientas.duels_datos.catalogo build --manual ../lorcana-trabajo/analisis/duels-2026-10-15 --manifest RUTA_MANIFIESTO --manifest ../lorcana-trabajo/adquisiciones/duels/sample/manifest.json --link-manual-account --selection-evidence RUTA_EVIDENCIA --observed-identities RUTA_MAPA_NUEVO --out ../lorcana-trabajo/analisis/profesora-lorcana/datos/privado/lotes
```

## Selección ROTOR y cobertura

`safe` admite dos fundamentos diferenciados: nombre histórico exacto en una observación o identidad del objeto de mazo vinculada mediante captura de interfaz y el nombre explícito dado por Iván. El segundo se aporta con `--selection-evidence` (`duels-selection-evidence-v1`), verifica cuenta/deck ID y conserva hash de la captura. En ese caso se registra `scope: deck_object_identity` y `historical_name_verified: false`: no se atribuye ese nombre a cada fecha. La captura del 15 de octubre acredita ese objeto para el histórico actual.

`candidate` indica coincidencia de composición con el piloto, un deck ID ligado al piloto sin vínculo nominal o una lista exacta de un **deck ID distinto** coincidente con alguna composición segura. La comparación queda limitada a la misma cuenta. Compartir un deck ID no impone una composición fija. `pending` conserva el resto; no se descartan filas. Los colores Zafiro/Acero por sí solos no seleccionan nada. La API no documenta el nombre del mazo. Los candidatos de otros objetos no provocan descargas automáticas; el cliente recibe una lista explícita del subconjunto justificado.

Las cantidades de cobertura distinguen partidas y encuentros. Para el manifiesto API se conserva `enumeration_complete_claimed` y se comprueba además final de cursor, cadena de páginas y filtros. Las respuestas solapadas no se borran: se señalan y no se acredita completitud automáticamente. Incluso una cadena completa solo acredita lo devuelto para esos filtros; no garantiza toda la vida de la cuenta ni la retención histórica de archivos. `not_requested` no equivale a archivo perdido ni caducado.

## Auditorías posteriores y fuentes contradictorias

`registrar_auditoria.py` consume un informe `duels-reconstruction-audit-v1` de análisis y lo vincula por batch ID al lote verificado. Exige cobertura exacta de sus filas `safe`, conserva una copia por hash y crea un suplemento inmutable independiente, sin modificar el lote ni escoger silenciosamente una lista en conflicto. Para los fallos compara el encabezado del replay con cada página API original, identifica diferencias de impresión/composición/cantidad, verifica cuenta, perspectiva y deck ID, y registra fronteras de logs no monótonas. El resultado de reconstrucción se atribuye al informe de análisis; las nuevas comprobaciones no equivalen a ejecutar todo el motor.

```powershell
python -m herramientas.duels_datos.registrar_auditoria --batch RUTA_LOTE --audit RUTA_RECONSTRUCCION_JSON --out ../lorcana-trabajo/analisis/profesora-lorcana/datos/privado/auditorias
python -m unittest herramientas.duels_datos.test_catalogo herramientas.duels_datos.test_auditoria -v
```

El lote `7332f06e…` tiene una incidencia posterior documentada: 152 reconstruidos, cuatro fallidos y un ausente. Tres listas API difieren de las listas declaradas en el replay, aunque ambos archivos e identidades sean válidos. Los estados `verified_json` permanecen como cobertura de adquisición, con ese límite semántico explícito.

## Extraer el último mazo jugado y detectar cambios

Desde la raíz del repositorio:

```powershell
python -B -m herramientas.duels_datos.mazo_actual --actualizar
python -B -m herramientas.duels_datos.mazo_actual
python -B -m herramientas.duels_datos.mazo_actual --manifest RUTA_MANIFEST_JSON
python -B -m unittest herramientas.duels_datos.test_mazo_actual -q
```

La primera orden consulta el historial autenticado mediante el cliente existente. Enumera todos los metadatos de la cuenta hasta un límite UTC registrado, sin asumir que el orden de respuesta corresponde al de juego. Reutiliza replays del lote histórico cuando coinciden partida, replay ID y perspectiva; si faltan, adquiere archivos de **hasta dos partidas** seleccionadas (el cliente obtiene replay y gamelog). No vuelve a descargar el corpus. Usa el token de `.env` a través del cliente, sin mostrarlo.

La segunda orden trabaja solo con el lote indicado por `datos/privado/entrega-historico-final.json`: es una lectura histórica, no una consulta actual. `--manifest` permite consumir sin red una adquisición completa ya hecha con el cliente, sin filtros de fecha inferior, cola ni fuente. Es útil para separar adquisición y lectura cuando los permisos del entorno lo requieren. Para una consulta nueva usa un directorio de adquisición nuevo; reanudar un manifiesto terminado conserva su límite temporal anterior.

Selecciona la última partida por `started_at` de la misma cuenta y **objeto de mazo ROTOR**. Compara con la partida anterior de composición distinta, saltando repeticiones y cambios solo de impresión. Una vuelta a una versión antigua se compara con la versión distinta inmediatamente precedente, no con la primera aparición histórica. Si la última partida de la cuenta usa otro objeto, lo advierte y muestra la última de ROTOR. No lee cambios del constructor que todavía no se hayan jugado.

Exporta en `datos/privado/mazo-actual/<hash>/` una lista con cantidades (`mazo-actual.txt`), un informe legible (`INFORME.md`), la comparación estructurada y su manifiesto de hashes. Conserva una copia del checkpoint de adquisición por hash. No sobrescribe informes existentes distintos; las páginas y replays seleccionados se comprueban por hash. No modifica el lote histórico ni amplía automáticamente el diagnóstico de análisis.

Las listas de 60/61 cartas se conservan tal como aparecen. Un desacuerdo con el encabezado del replay queda visible con ambas listas, sin elegir silenciosamente una como verdadera. Las identidades desconocidas se muestran por ID y la comparación queda provisional; no se deducen equivalencias. Las fechas ambiguas y las listas ausentes detienen la selección. Los nombres completos proceden del mapa observado del lote, no de una verificación normativa.

Las 13 pruebas del extractor cubren selección temporal, reversiones, cuenta/objeto, impresiones, cantidades, identidades desconocidas, fuentes alteradas, contradicciones, exportación idempotente y el flujo de actualización con transporte simulado.

## Contrato local alternativo

```json
{
  "schema": "duels-datos-input-v1",
  "account_id": "ID_VERIFICADO",
  "pages": [{"path": "pagina-original.json", "sha256": "HASH", "fetched_at": "2026-10-15T00:00:00Z"}],
  "files": [{"game_id": "PARTIDA", "kind": "replay", "status": "downloaded", "path": "original.replay.gz", "sha256": "HASH"}],
  "identities": {"ID_IMPRESION": "IDENTIDAD_DOCUMENTADA"},
  "coverage": {"enumeration_complete": false}
}
```

Las rutas relativas se resuelven respecto al JSON. Las páginas tienen `{games, next_cursor}`. Las entradas de archivos sin ruta pueden declarar estado/motivo de indisponibilidad. Este adaptador conserva la cobertura declarada sin certificar su cadena; para la cobertura comprobada utiliza `--manifest`. Nunca incluyas tokens ni URLs de descarga en este contrato.
