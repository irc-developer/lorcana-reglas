# Plan de implementación del MCP de Lorcana

Preparado el 30/09/2026. Estado: implementación local, pruebas, registro y uso del MCP en chats nuevos de consulta observados. Pendiente la evaluación editorial completa en una copia, consultas de ambigüedad/limitaciones y el nuevo MCP desde el acceso móvil existente. Véanse [guía de uso](../mcp_lorcana/README.md) y [resultados](../mcp_lorcana/RESULTADOS.md).

El objetivo es abrir un chat nuevo de Codex en este proyecto, hacer una consulta de Lorcana y recibir una explicación sustentada en la evidencia local recuperada mediante MCP. El servidor reutilizará el motor existente desde el primer prototipo.

La conexión móvil ya está resuelta, según confirma el usuario. Se aprovechará la conexión existente cuando se pruebe el MCP desde el móvil; su configuración no forma parte de este trabajo. Esa prueba comprobará el uso del nuevo servidor a través del acceso disponible.

**Decisiones de partida**

- Implementación en Python, con el SDK oficial de MCP publicado como `mcp`.
- Transporte inicial `stdio`, adecuado para el cliente local de Codex.
- Cuatro herramientas de lectura: estado de fuentes, carta, regla y búsqueda de evidencia.
- Recuperación mediante `herramientas/consulta_lorcana/core.py`, conservando la CLI existente.
- Interpretación y documentación mediante el asistente y las instrucciones/skills del repositorio.
- Dependencias MCP en un entorno dedicado. Verificar y fijar versiones compatibles durante la implementación; los ejemplos de documentación no acreditan cuál es la última versión del paquete.
- La primera entrega consulta fuentes locales. La vigencia externa se seguirá comprobando mediante el workflow existente cuando la petición lo requiera.

OpenAI documenta los SDK Python/TypeScript, los contratos de herramientas y los resultados estructurados en [Build an MCP server](https://developers.openai.com/plugins/build/mcp-server). Codex documenta `stdio`, las instrucciones del servidor y la configuración por proyecto en [Model Context Protocol](https://learn.chatgpt.com/docs/extend/mcp). Son las referencias revisadas para estas decisiones; los nombres de herramientas y el reparto de responsabilidades siguientes son decisiones de este proyecto.

**Base comprobada en el repositorio**

`consulta.py` es un lanzador que evita bytecode y llama a `core.main()`. La lógica de recuperación ya está separada en funciones importables:

| Función actual | Uso previsto |
|---|---|
| `query(root, db, question, card_names, rule_numbers, scope, explicit, limit)` | Recuperar evidencia, fichas y reglas con sus limitaciones. |
| `freshness(root, db)` | Comprobar el estado del índice y la selección local de fuentes. |
| `mode_of(question, explicit)` | Conservar la distinción entre consulta y documentación. |
| `update(root, db, force_scan)` | Mantener el índice mediante la CLI, fuera de las herramientas de lectura. |

La consulta abre su propia conexión SQLite y la cierra al terminar. Cuando el índice falta o está desactualizado, el motor recupera las fuentes en memoria. Verifica las citas y vuelve a comprobar el inventario antes de devolver evidencia.

Hay un detalle de integración obligatorio: `query()` usa `explicit=True` por defecto y, por tanto, interpreta una pregunta sin prefijo como consulta. El adaptador y las instrucciones del asistente deben conservar el modo de la petición original; una pregunta ordinaria de reglas sin señal mantiene la obligación editorial.

Existen pruebas del motor y una matriz de 20 preguntas en `evaluacion.json`. Se reutilizarán sus expectativas trazadas a fuentes, además de probar el protocolo MCP real. Los cambios previos del usuario están presentes y deberán conservarse.

**1. Preparar la integración del motor**

Revisar las importaciones y definir un adaptador pequeño que traduzca los parámetros MCP a `query()` y `freshness()`. Mantener en el motor la selección de fuentes, búsqueda, verificación de cartas, referencias, hashes y comprobación de vigencia local.

Configurar la raíz del repositorio y la ubicación de la base al iniciar el servidor. Las llamadas de herramientas recibirán preguntas y nombres, sin parámetros para elegir archivos arbitrarios o ejecutar comandos.

Arrancar con bytecode desactivado antes de importar los módulos locales. Revisar la compatibilidad del SDK con el Python disponible; el manual actual declara Python 3.14.3, dato que deberá verificarse en el entorno de implementación. Cada llamada conservará una conexión de base propia, sin compartir conexiones SQLite entre hilos.

Entregable: adaptador importable y contrato documentado. Criterio de aceptación: puede obtener evidencia utilizando el motor actual y conserva el comportamiento de la CLI.

**2. Definir los contratos de las cuatro herramientas**

| Herramienta propuesta | Entradas | Resultado principal |
|---|---|---|
| `estado_fuentes` | Ninguna. | Índice utilizable/actual, selección local y diagnóstico existente. |
| `obtener_carta` | `nombre`, incluyendo versión cuando se conozca. | Fichas completas disponibles, resolución exacta/ambigua/ausente/incompleta y procedencia. |
| `obtener_regla` | `numero`. | Evidencia de la regla solicitada, contexto, referencias y aviso explícito si falta. |
| `buscar_evidencia` | `pregunta`, `modo`, `cartas`, `reglas`, `ambito`, `limite`. | Paquete de evidencia agrupada y obligaciones del modo solicitado. |

`modo` será obligatorio en `buscar_evidencia` y admitirá `consulta` o `documenta`. Las instrucciones del asistente seleccionarán `consulta` solo cuando lo autorice la petición original, incluido el uso explícito de la skill para consulta rápida. Una pregunta de reglas sin señal seleccionará `documenta`. Si se conserva un prefijo dentro de `pregunta`, deberá concordar con `modo`; una contradicción será un error de entrada.

`cartas` y `reglas` serán listas opcionales; `ambito` utilizará los valores admitidos por la CLI; `limite` será un entero entre 1 y 12 y controlará resultados complementarios. Las reglas solicitadas y las fichas completas seguirán disponibles. Las herramientas directas de carta/regla serán auxiliares de lectura y no cambiarán el modo editorial de la conversación.

Definir esquemas de entrada/salida y descripciones precisas. Marcar las herramientas como lectura, ámbito local y comportamiento no destructivo. Preservar `evidence_only`, `content_is_untrusted_data`, `freshness`, `selection`, `warnings`, `card_resolution`, `missing_rule_numbers`, categorías de autoridad y procedencia de cada fragmento.

Devolver datos estructurados y contenido textual útil. Empezar con el paquete actual; reducir duplicación solo si las mediciones muestran que hace falta y sin cortar silenciosamente citas, texto decisivo, condiciones o limitaciones. Conservar enlaces oficiales verificados y referencias locales con páginas/líneas, sin inventar URLs accesibles desde otros clientes.

Una carta ausente o ambigua será un resultado de evidencia insuficiente. Entradas inválidas, fuentes ilegibles o discrepancias de selección serán errores explícitos, con indicación de que la evidencia no permite cerrar el ruling.

Entregable: contrato de herramientas. Criterio de aceptación: el cliente puede distinguir un fallo técnico, una ausencia de evidencia y una consulta satisfactoria con limitaciones.

**3. Construir el servidor y completar el primer recorrido**

Crear el servidor con nombre `lorcana` y versión inicial identificable. Publicar primero estado, carta y regla; probarlas a través de un cliente MCP `stdio`. Incorporar después `buscar_evidencia` usando el mismo adaptador.

Añadir instrucciones breves del servidor sobre evidencia, autoridad de fuentes, vigencia local y tratamiento de ambigüedad. Los registros irán a `stderr`; `stdout` quedará reservado al transporte MCP. El arranque y la conexión serán de lectura y no regenerarán búsqueda.

Ubicación propuesta de los archivos de implementación:

| Ruta | Contenido |
|---|---|
| `herramientas/mcp_lorcana/servidor.py` | Arranque `stdio`, instrucciones y registro de herramientas. |
| `herramientas/mcp_lorcana/adaptador.py` | Traducción de llamadas al motor existente. |
| `herramientas/mcp_lorcana/modelos.py` | Contratos tipados cuando aporten validación útil. |
| `herramientas/mcp_lorcana/requirements.txt` | Dependencias comprobadas del servidor. |
| `herramientas/mcp_lorcana/test_mcp.py` | Pruebas del transporte y del contrato. |
| `herramientas/mcp_lorcana/README.md` | Instalación, conexión, uso y diagnóstico. |

Elegir un lanzador que funcione con rutas Windows con espacios y desde otro directorio de trabajo. Mantener el entorno de dependencias y otros archivos regenerables fuera del control de versiones según la configuración efectiva del repositorio.

Entregable: servidor ejecutable. Primer hito: un cliente MCP recupera una carta y una regla reales con texto y procedencia verificados.

**4. Verificar protocolo, evidencia y ausencia de escrituras**

Ejecutar la suite existente como mantenimiento de desarrollo y añadir pruebas que atraviesen el transporte MCP: inicialización, descubrimiento, esquemas, anotaciones, llamadas y errores. Comparar resultados con la CLI y con las expectativas de fuente existentes, descontando tiempos y otros campos variables.

Cubrir nombres exactos, ambigüedad, carta ausente, fichas incompletas/reimpresas y reglas exactas inexistentes. Cubrir ámbitos separados y la conservación de advertencias de políticas locales superadas o ausentes. Comprobar que material excluido e histórico no se presenta como autoridad vigente.

Probar índice actual, ausente y desactualizado; modificaciones concurrentes de fuentes; sustitución del índice entre llamadas; entradas inválidas y varias llamadas en el mismo proceso. Usar fixtures para escenarios que requieren modificar fuentes o índices.

Verificar inventario, hashes, tamaños y fechas antes/después del arranque y de las llamadas de lectura. Incluir la ausencia de bytecode y cachés creados por nuestros módulos. Distinguir los artefactos de preparación de pruebas de las operaciones bajo prueba.

Medir la latencia del arranque y de llamadas repetidas para detectar el coste añadido por el adaptador. La medición describirá recuperación y transporte; la respuesta completa del modelo se medirá por separado si procede.

Entregable: pruebas e informe reproducible. Criterio de aceptación: las consultas mantienen la evidencia y las limitaciones del motor y no escriben archivos.

**5. Conectar Codex y adaptar las instrucciones existentes**

Configurar el servidor en el ámbito del proyecto cuando el cliente y los permisos lo permitan, usando el ejecutable correcto y rutas explícitas. Inspeccionar la configuración efectiva y conservar otros servidores y ajustes. Documentar cómo verificar que el servidor está conectado y cómo reiniciar/refrescar el cliente.

Adaptar `AGENTS.md` y la skill de consulta rápida para preferir el MCP cuando esté disponible. Sincronizar deliberadamente la skill activa y su copia de distribución. Mantener la CLI como alternativa cuando el servidor no esté conectado, con la misma selección de modo.

Conservar el workflow editorial de `.github/`: `documenta:` y preguntas ordinarias de reglas requieren sus pasos completos. El MCP aportará evidencia; el asistente seguirá resolviendo y documentando mediante ese workflow. `actualiza:` seguirá ejecutando el mantenimiento separado de la CLI y solo modificará artefactos de búsqueda.

Entregable: conexión e instrucciones integradas. Criterio de aceptación: un chat nuevo descubre las herramientas y sabe elegir el modo correcto.

**6. Validar el uso real y entregar**

Realizar una consulta nueva en Codex y comprobar la herramienta elegida, sus parámetros y la respuesta con fuentes, ejemplo y versión local. Validar además una petición con carta ambigua y una consulta con limitaciones.

Comprobar el enrutamiento de `documenta:` y de una pregunta sin prefijo en un entorno de evaluación: deben conservar la obligación editorial. Una prueba editorial completa utilizará un caso sustentable y verificará artículo canónico, índices y fecha según el workflow. Los cambios de evaluación se realizarán en una copia de prueba; no modificar conocimiento real para fabricar una demostración.

Probar `actualiza:` por la vía de mantenimiento en fixtures. Comprobar que las consultas MCP no ejecutan esa actualización implícitamente.

Cuando se haga la prueba desde el móvil, usar el acceso ya establecido y verificar que se invocan las herramientas del nuevo servidor. Registrar el resultado de esa prueba por separado; la conexión existente se da por resuelta y las pruebas de consola no acreditan por sí mismas el uso móvil del MCP.

Entregable final: servidor, instrucciones, configuración disponible, guía de uso y resultados de validación. Si abrir un chat nuevo exige una acción del usuario, dejar ese paso exacto indicado y marcar la verificación real como pendiente hasta observarla.

**Criterios de cierre de la primera entrega**

- [x] Las cuatro herramientas funcionan mediante MCP `stdio`.
- [x] Se reutiliza el motor existente y la CLI sigue operativa.
- [x] Se conservan fichas, reglas, citas, versiones, autoridad y limitaciones.
- [x] Arranque y consultas no escriben fuentes, índices, cachés ni bytecode.
- [x] Los fallos y ambigüedades se entregan al cliente de forma explícita.
- [x] Contratos e instrucciones conservan `consulta:`, `documenta:`, `actualiza:` y preguntas sin señal; falta observar el enrutamiento del asistente en un chat nuevo.
- [x] Las pruebas del motor y de integración pasan: 15 de referencia del motor + 10 actuales del MCP 0.2.0, incluida la matriz de 20 consultas y conservación de evidencia en la vista de lectura.
- [x] Un chat nuevo de Codex utiliza el MCP y devuelve una respuesta sustentada: dos consultas de Resist verificadas en sus registros.
- [x] La guía identifica cualquier validación que requiera una acción del usuario.
- [x] Se revisan los cambios de la entrega y se conservan los cambios previos.

El cliente real de Codex acepta la configuración con validación estricta e inicializa y descubre las cuatro herramientas. Posteriormente se verificó el uso del MCP en dos chats nuevos de consulta mediante sus registros. Siguen pendientes los casos de ambigüedad/limitaciones, la evaluación editorial completa y el uso móvil. La configuración instalada usa el presupuesto de salida por proyecto compatible con Codex 0.147.0; el ajuste por herramienta de la documentación actual todavía no es admitido por esa versión.

La prueba móvil complementa la entrega local. La publicación como plugin, el transporte HTTP, las herramientas MCP de escritura y las integraciones `search`/`fetch` podrán planificarse cuando exista una necesidad concreta de esos usos.

**Optimización posterior a la auditoría:** completada en 0.2.0. Vista de lectura con textos íntegros y metadatos compartidos; presupuesto explícito de `functions.exec`; carga de guías según modo y pregunta; alcance alineado con el PDF seleccionado. Cliente Codex y pruebas verificados. Falta repetir la consulta con el asistente para medir el tiempo total de chat. Véanse [resultados actuales](../mcp_lorcana/RESULTADOS.md).

**Opción futura: aprender a utilizar MCP fuera de la app local**

El usuario pide conservar esta posibilidad para explorarla más adelante (30/09/2026). Es una opción de aprendizaje posterior a la entrega local, sin fecha ni compromiso de despliegue público.

Temas para una exploración práctica:

- Ejecutar el mismo motor mediante Streamable HTTP en un servidor remoto y conectarlo desde otro cliente compatible.
- Compartir el acceso con un grupo pequeño y estudiar después la publicación como plugin en el directorio de ChatGPT y Codex.
- Comprender los costes de alojamiento y tráfico, el consumo de tokens del asistente que usa las herramientas y el consumo adicional que supondría incorporar un modelo dentro del servidor.
- Adaptar las referencias locales a enlaces accesibles para otros usuarios y practicar mantenimiento de fuentes, concurrencia y límites de uso.

Al retomar esta opción, revisar la documentación oficial y las condiciones vigentes de publicación y costes. Aprovechar la conexión móvil ya resuelta; explorar un servidor remoto es un aprendizaje adicional. La petición actual guarda la idea para el futuro y no autoriza contratar alojamiento ni publicar el servicio.
