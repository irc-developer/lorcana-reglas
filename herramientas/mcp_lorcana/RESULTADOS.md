# Verificación del MCP local — 30/09/2026

Implementación local y registro completados. Se observó el uso del MCP por el asistente en dos chats nuevos de consulta sobre Resist: llamadas correctas, ejemplo y fuentes. Véase la [auditoría de los registros](AUDITORIA_PRUEBA_2026-09-30.md). Pendiente una transacción editorial completa de evaluación en una copia, consultas de ambigüedad/limitaciones y el uso del MCP desde el acceso móvil ya existente.

## Entorno y pruebas

Windows, Python 3.14.3, SDK MCP 2.2.0, PyMuPDF 1.27.2.3, Codex CLI 0.147.0. `pip check` sin dependencias incompatibles. Versiones directas fijadas en `requirements.txt`; instalación completa conservada en `requirements-windows.lock`.

| Comprobación final | Resultado |
|---|---|
| Suite del motor, `test_consulta.py` | 15 pruebas, OK, 40,621 s. |
| Suite de transporte/contrato, `test_mcp.py` | 0.2.0: 10 pruebas, OK, 88,776 s. Incluye regresión de tamaño y conservación de evidencia. |
| Matriz de referencia | 20 preguntas en ambas suites; reglas, páginas, textos decisivos, cartas, ámbitos y limitaciones trazados a fuentes. |
| Cliente Codex real, `verificar_cliente_codex.py` | Configuración estricta aceptada; inicializa `lorcana` 0.2.0 y descubre sus cuatro herramientas. Sin chat ni llamada al modelo. |
| Skill activa y distribución | Validación `quick_validate.py` correcta en ambas; contenido idéntico. |
| Sintaxis y revisión | Módulos Python válidos; diff de archivos versionados sin errores de espacios; entorno/caché excluidos de Git. |

Cobertura del MCP: descubrimiento, esquemas de entrada/salida, anotaciones de lectura, handshake antiguo/moderno, otro directorio de trabajo, rutas con espacios, llamadas concurrentes, igualdad del paquete con CLI descontando tiempos, JSON textual igual al estructurado, rechazo de entradas inválidas y recuperación del proceso después de un error.

Se verificaron cartas exactas, versiones ambiguas, ausentes, fichas repetidas en sets, campos de Fuerza ausentes y listados parciales. Se conservan los textos completos y las limitaciones; no se rellena información por memoria. Una regla exacta inexistente devuelve evidencia insuficiente, distinta de un error técnico.

Los fixtures cubren índice ausente/obsoleto, cambios de texto con fecha conservada, fuente PDF dañada, discrepancia de selección, cambio durante la recuperación y sustitución atómica del índice con el servidor abierto. El mantenimiento `actualizar` se ejecuta por CLI en una copia de ensayo. Los errores impresos durante esos ensayos son fallos deliberados de los fixtures.

Los snapshots incluyen inventario, hashes, tamaño y mtime de los archivos del repositorio, incluidas las dependencias y sus cachés preparadas antes del ensayo; se excluyen metadatos Git. Arranque y llamadas MCP no modificaron fuentes, índice, cachés ni bytecode. La preparación de fixtures y la escritura del informe son acciones de desarrollo separadas.

La primera ejecución de la suite antigua con el Python del nuevo entorno detectó bytecode de `pywin32_bootstrap` generado al iniciar su subproceso CLI, antes del código de consulta. Se añadieron `-B` a los dos lanzadores de prueba; la suite completa volvió a pasar. El motor y su CLI no se modificaron. El lanzador MCP desactiva bytecode desde el inicio y también fija `PYTHONDONTWRITEBYTECODE` en la configuración.

## Integración comprobada

La configuración está en `.codex/config.toml`, con rutas de este PC, cuatro herramientas permitidas, arranque de 20 s y llamadas de 120 s. El proyecto ya estaba declarado de confianza. Se conserva la configuración global, los otros servidores y los cambios previos del usuario. AGENTS.md y la skill prefieren MCP conectado y mantienen la CLI como alternativa y vía de mantenimiento.

La documentación oficial actual describe `mcp_servers.<id>.tools.<tool>.output_token_limit`; **Codex 0.147.0 lo rechaza en modo estricto**. Se utiliza `tool_output_token_limit=100000` en el ámbito del proyecto, compatible con el cliente instalado. Afecta al presupuesto de salida de las herramientas del proyecto y no es un consumo fijo. El contenedor `functions.exec` tiene otro límite: AGENTS.md, skill e instrucciones del servidor exigen fijarlo explícitamente y leer resultados muy grandes por grupos desde memoria. No se cambió la configuración global ni el modelo.

Dentro del aislamiento de esta tarea, el subproceso `codex mcp list` no mostraba los servidores configurados. La comprobación autorizada fuera del aislamiento sí mostró `lorcana` habilitado. El cliente `app-server` real confirmó inicialización, versión y descubrimiento con configuración estricta; no se añadió un servidor global para compensar esa diferencia.

`buscar_evidencia` requiere un modo y rechaza prefijos contradictorios/`actualiza:`. Las pruebas confirman `editorial_required=true` en modo documenta. Carta/regla devuelven modo auxiliar y no cambian la obligación editorial. Las instrucciones mantienen que una pregunta ordinaria sin señal use documenta. Los dos chats auditados confirman además el modo consulta; el enrutamiento y la transacción completa de documentación siguen pendientes de observar.

## Latencia y tamaño de referencia — 0.1.0

Datos reproducibles: [mediciones-2026-09-30.json](mediciones-2026-09-30.json), 3 procesos nuevos y 60 llamadas en un proceso (20 casos × 3). Sin vaciar la caché del sistema operativo y sin modelo ni tráfico de red del servidor.

| Medida | Mediana | P95 |
|---|---:|---:|
| Arranque + descubrimiento | 2066,443 ms | 2082,088 ms |
| Primera llamada en proceso nuevo | 802,640 ms | 809,863 ms |
| Recuperación y transporte | 872,740 ms | 985,546 ms |
| Motor de recuperación | 864,049 ms | 976,741 ms |
| Diferencia transporte/adaptación/cliente | 8,772 ms | 11,725 ms |

La llamada máxima observada fue 1029,877 ms. El paquete textual mayor tuvo 104.701 caracteres; el sobre completo, incluyendo la copia estructurada, 214.346 bytes. Estas cifras corresponden a la entrega 0.1.0, antes de la optimización; no miden el razonamiento del asistente, sus tokens ni la latencia móvil.

## Optimización — 0.2.0

`formato="lectura"` es la vista predeterminada: comparte metadatos de procedencia y entrega JSON sin espacios de formato. Se conservan íntegros todos los fragmentos y sus campos mediante `sources[source_ref]`. Solo el inventario global de exclusiones pasa a un contador; las exclusiones relacionadas, cambios del corpus, advertencias, ambigüedades y reglas ausentes siguen completos. `formato="completo"` mantiene la igualdad con CLI. La regresión comprueba reconstrucción exacta de todos los fragmentos, además de los 20 oráculos de fuente.

Para una consulta de Resist sin cartas concretas, la carga inicial prescrita pasa de siete archivos y 28.493 caracteres observados a cuatro y 13.508 caracteres medidos (52,6 % menos). Se conserva el núcleo normativo obligatorio; guías de cartas/timing se cargan cuando corresponden y el workflow completo sigue siendo obligatorio en `documenta:` y preguntas ordinarias. No se carga el manual de instalación durante una consulta normal. Se alinearon contrato, alcance y workflow con el PDF seleccionado por ambos punteros locales.

El índice estaba desactualizado por cambios previos en tres fuentes; se actualizó explícitamente como mantenimiento, sin editar esas fuentes. Las consultas posteriores verificaron índice actual y ausencia de escrituras mediante snapshots. Las copias activa y de distribución de la skill son idénticas y pasan `quick_validate.py`; sintaxis Python/YAML y diff comprobados.

Mediciones actuales en [mediciones-0.2.0-2026-09-30.json](mediciones-0.2.0-2026-09-30.json): 60 llamadas de lectura, 20 completas para comparar evidencia y cuatro para reproducir los argumentos auditados. La mediana de recuperación/transporte es 867,344 ms; P95 1049,766 ms. La mediana de arranque/descubrimiento es 2059,921 ms. El texto mayor tiene 81.204 caracteres y el sobre 168.094 bytes. La reducción textual mediana frente a `completo` sobre las mismas fuentes es 23,63 % (mínima 14,44 %); fichas largas reducen menos porque se conservan sus textos.

| Reproducción de argumentos auditados | Completo | Lectura | Reducción |
|---|---:|---:|---:|
| Resist / daño puesto con «put» | 38.029 caracteres | 27.098 caracteres | 28,74 % |
| Resist / «put counter damage», con sección 9.2 solicitada originalmente | 51.606 caracteres | 38.075 caracteres | 26,22 % |

No son nuevos chats con modelo ni una medición de tokens facturados. Las fuentes cambiaron desde los registros originales: la comparación de tamaño se hace entre ambos formatos sobre la misma copia actual. La latencia completa de chat y el seguimiento de las nuevas instrucciones siguen pendientes de observar. Reinicia `lorcana` en la configuración MCP y abre un chat nuevo antes de repetir la consulta, para que el proceso cargue 0.2.0.

## Validaciones pendientes

1. Abrir un chat nuevo de Codex en el proyecto y enviar `consulta: Si un efecto me hace robar tres cartas, ¿son tres robos?`. Observar llamada a `buscar_evidencia`, `modo="consulta"`, CR 1.12.2 p.9, ejemplo, versión local y ausencia de ediciones. Si no aparece el servidor, reiniciarlo desde ajustes MCP y abrir el chat otra vez.
2. Probar en ese cliente carta ambigua y consulta con limitaciones, según los ejemplos de [README.md](README.md).
3. En una copia del repositorio, evaluar `documenta:` y pregunta sin señal con el asistente: revisar artículo canónico, índices y fecha siguiendo `.github/skills/lorcana-ruling-workflow/SKILL.md`. El contrato probado no sustituye esa transacción editorial completa.
4. Repetir la consulta desde el acceso móvil existente y observar que utiliza las herramientas del nuevo MCP. La conexión móvil del usuario se da por resuelta; esta comprobación evalúa el nuevo servidor y las referencias.

La publicación pública y el transporte remoto quedan como opción futura del plan, sin despliegue ni contratación realizados.
