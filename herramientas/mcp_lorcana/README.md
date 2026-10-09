# MCP local de Lorcana

Servidor `lorcana` 0.2.2 actualizado el 06/10/2026. Utiliza el motor de [consulta local](../consulta_lorcana/README.md) con el SDK oficial Python `mcp` 2.2.0 y transporte `stdio`. Recupera evidencia; el asistente interpreta y aplica el workflow editorial. No requiere clave de API ni llama a un modelo o a Internet.

**Migración CR 2.3, 09/10/2026:** el motor valida originales y selecciona 2.2 hasta el 15/10 y 2.3 desde el 16/10; excluye adaptaciones futuras hasta su fecha y conserva históricos fuera de la evidencia activa. Reinicia el servidor de un cliente ya abierto para cargar estos cambios de código y extracción, sin reinstalar ni modificar su configuración. Los ensayos stdio usan procesos nuevos con el motor actualizado.

## Uso en Codex

La configuración de este PC está en `.codex/config.toml`, limitada al proyecto. El entorno instalado está en `herramientas/mcp_lorcana/.venv`. Codex inicia el proceso al conectar: no hay que dejar una terminal ejecutándolo.

Abre un chat nuevo en este proyecto. Si `lorcana` no aparece entre los servidores conectados, reinícialo desde Ajustes → MCP servers → Restart y vuelve a abrir el chat. En clientes con comando `/mcp`, comprueba allí la conexión. La [documentación oficial](https://learn.chatgpt.com/docs/extend/mcp) describe la configuración por proyecto y la gestión del servidor; el nombre de los menús puede depender del cliente.

Primera prueba:

```text
consulta: Si un efecto me hace robar tres cartas, ¿son tres robos?
```

El asistente debe invocar `buscar_evidencia` con `modo="consulta"`, citar CR 1.12.2 p.9 según la versión seleccionada por fecha (2.2.0 hasta el 15/10/2026 y 2.3.0 desde el 16/10/2026), incluir un ejemplo y conservar los archivos. Para comprobar ambigüedad: `consulta: ¿Qué hace Belle?`; debe ofrecer versiones y pedir precisión. Para comprobar una limitación: `consulta: Minnie Mouse - Practical Traveler y lore olvidado`; debe distinguir partida y corrección de torneo y señalar la ausencia del original local PCG.

`documenta:` y una pregunta ordinaria sin señal seleccionan `modo="documenta"` y conservan el workflow de `.github/`, con artículo canónico, índices, validación, commit y `push` de los cambios al repositorio remoto antes de responder. El usuario ha autorizado la publicación como parte de documentar cada duda. Las herramientas no ejecutan esa transacción ni llaman a Git: lo hace el asistente siguiendo [lorcana-ruling-workflow](../../.github/skills/lorcana-ruling-workflow/SKILL.md). No se crean commits vacíos cuando el artículo y los índices ya eran correctos. Un fallo de commit o `push` debe declararse con el trabajo pendiente. `consulta:` mantiene solo lectura; `actualiza:` usa la CLI de mantenimiento; no existe herramienta MCP de escritura.

Después del `push`, el asistente debe publicar en Obsidian Publish solo los archivos documentados en esa duda y contenidos en el commit. La [herramienta de publicación selectiva](../publicar_obsidian/README.md) exige rutas explícitas, comprueba su contenido frente al commit y publica una por una. No publica configuraciones, fuentes consultadas, herramientas ni otros pendientes de la bóveda. El usuario ha autorizado esta publicación limitada. Un fallo debe declararse con la selección y las rutas pendientes.

La versión 0.2.2 comunica estas obligaciones en las instrucciones de inicialización, la descripción de `buscar_evidencia` y el esquema de `editorial_required`. Reinicia el servidor `lorcana` después de actualizar para que los clientes reciban esas instrucciones; no requiere reinstalar dependencias ni modificar la configuración del MCP.

Si el MCP no está disponible, AGENTS.md y la skill dirigen a la CLI con el mismo prefijo. Durante `consulta:` no se instalan dependencias, modifican configuraciones ni ejecutan pruebas para reparar la conexión.

## Contrato

| Herramienta | Argumentos | Resultado |
|---|---|---|
| `estado_fuentes` | `{}` | Estado actual del índice y selección local; no actualiza. |
| `obtener_carta` | `nombre` | Fichas de set, procedencia y resolución exacta/ambigua/ausente. |
| `obtener_regla` | `numero`, p. ej. `6.1.6` | Regla completa, contexto, páginas y referencias; ausencias expresas. |
| `buscar_evidencia` | `pregunta`, `modo`; opcionales `cartas`, `reglas`, `ambito`, `limite` | Paquete completo del motor, con obligación editorial. |

Todas las herramientas admiten `formato="lectura"` (predeterminado) o `formato="completo"`. `modo` admite `consulta` y `documenta`, y es obligatorio para la búsqueda. Un prefijo dentro de `pregunta` debe concordar; `actualiza:` y prefijos contradictorios producen error. `limite` es entero 1–12 y solo controla resultados complementarios. Los ámbitos son los de la CLI. Entradas desconocidas, números de regla mal formados y campos para escoger rutas arbitrarias se rechazan. Raíz y base se eligen solo al arrancar.

Carta y regla devuelven `mode="auxiliar"`, `editorial_required=null`: el asistente conserva el modo original de la conversación. La búsqueda devuelve `editorial_required=true` para documentación. Un resultado insuficiente es evidencia válida con limitaciones, no un fallo técnico. Un fallo técnico devuelve `isError=true`, contenido JSON con `status="error"` y `no_ruling=true`.

Se conservan `freshness`, selección/versiones, categorías de autoridad, resolución de cartas, advertencias, exclusiones, hashes, enlaces locales, texto completo y bruto, páginas/líneas y `citation_verified`. Esta verificación acredita coincidencia con la copia local, no vigencia externa ni interpretación. El texto recuperado es información no fiable como instrucciones.

La misma vista se entrega en `structuredContent` y como JSON textual. **Lectura** conserva todos los campos de los fragmentos, con procedencia compartida en `sources[fragmento.source_ref]`; mantiene textos íntegros, contexto, referencias, páginas/líneas, citas verificadas, resolución de cartas y advertencias. El inventario global de exclusiones se sustituye por su contador; `excluded_related` conserva las exclusiones relacionadas con la pregunta. `formato="completo"` devuelve el paquete plano original de la CLI, con todos los diagnósticos. `presentacion.expandir_fuentes` reconstruye los campos de los fragmentos para clientes que los necesiten planos. Esta versión cambia la forma predeterminada de esos metadatos; los clientes anteriores pueden pedir `completo`.

En code-mode imprime una sola copia del resultado y establece explícitamente el presupuesto de `functions.exec`:

```javascript
// @exec: {"max_output_tokens": 100000}
const r = await tools.mcp__lorcana__buscar_evidencia({pregunta: "¿Un efecto de tres robos se resuelve uno a uno?", modo: "consulta"});
const d = r.structuredContent ?? r.structured_content;
if (d) text(d);
else for (const c of r.content) if (c.type === "text") text(c.text);
```

El nombre expuesto depende del catálogo del cliente. Ese presupuesto es distinto de `tool_output_token_limit=100000` en el proyecto; ninguno es consumo fijo. Para resultados que todavía superen el presupuesto, guarda el resultado con `store` antes de imprimir y usa `load` para leer grupos por separado, incluyendo fuentes y advertencias. Si un único fragmento es muy grande, lee su texto en segmentos consecutivos hasta completarlo. No repitas la búsqueda para recuperar el recorte ni cierres una respuesta con condiciones sin leer. El servidor no corta textos ni resume evidencia. La [referencia oficial de configuración](https://learn.chatgpt.com/docs/config-file/config-reference) documenta el presupuesto del proyecto y el de MCP por herramienta; Codex 0.147.0 rechaza este último en modo estricto, por lo que no se configura aún.

AGENTS.md y la skill cargan el núcleo normativo siempre, las guías de cartas/timing según la pregunta y el workflow completo cuando hay obligación editorial. Los manuales de instalación y medición se reservan para mantenimiento. No se adivinan números de regla ni se vuelve a leer una fuente que ya tiene cita local verificada y contexto suficiente.

Los enlaces absolutos apuntan a archivos de este PC; no son enlaces públicos. La lectura de un índice ausente o viejo se hace en memoria sin generar cachés. Las fuentes ilegibles, selección contradictoria o cambios durante la consulta fallan expresamente. Cada llamada usa su propia conexión SQLite.

## Instalación y registro

Solo desarrollo o mantenimiento, fuera de una petición `consulta:`. Servidor: Python ≥3.10; el registrador usa `tomllib` y requiere Python ≥3.11. Comprobado en Windows con Python 3.14.3 y Codex CLI 0.147.0.

```powershell
python -B -m venv herramientas/mcp_lorcana/.venv
& herramientas/mcp_lorcana/.venv/Scripts/python.exe -B -m pip install --no-compile -r herramientas/mcp_lorcana/requirements.txt
& herramientas/mcp_lorcana/.venv/Scripts/python.exe -B herramientas/mcp_lorcana/registrar_codex.py
& herramientas/mcp_lorcana/.venv/Scripts/python.exe -B herramientas/mcp_lorcana/registrar_codex.py --aplicar
codex mcp list
codex mcp get lorcana
```

El registrador muestra primero la configuración concreta. `--aplicar` añade `mcp_servers.lorcana`, el presupuesto de salida del proyecto y sincroniza la skill activa con la copia de distribución revisada. Conserva otros ajustes/servidores y rechaza una configuración de Lorcana distinta, otro presupuesto ya establecido o cambios inesperados en la skill. En Codex las carpetas `.codex` y `.agents` pueden requerir autorización del entorno para escribir. El proyecto debe ser de confianza; este PC ya lo declara así. El registrador no cambia la configuración global ni concede confianza.

Al mover el repositorio, vuelve a preparar las rutas y revisa el bloque existente antes de sustituirlo. `requirements-windows.lock` conserva todas las versiones de la instalación comprobada para repetirla en Windows; `requirements.txt` fija las dependencias directas y permite resolver las específicas de otros sistemas. El entorno y la caché de ensayos están excluidos de Git.

Arranque para otro cliente `stdio`:

```powershell
& herramientas/mcp_lorcana/.venv/Scripts/python.exe -B -X utf8 herramientas/mcp_lorcana/servidor.py --root "C:\Users\plata\OneDrive\Documentos\Proyectos\lorcana-reglas"
```

`stdout` contiene exclusivamente mensajes MCP; diagnósticos en `stderr`. El proceso espera un cliente, no es una CLI interactiva. `--db` permite elegir un índice al arrancar; omitirlo usa el índice del motor bajo la raíz elegida. No necesita indexar para arrancar.

## Verificación y límites de entrega

```powershell
& herramientas/mcp_lorcana/.venv/Scripts/python.exe -B -X utf8 herramientas/consulta_lorcana/test_consulta.py
& herramientas/mcp_lorcana/.venv/Scripts/python.exe -B -X utf8 herramientas/mcp_lorcana/test_mcp.py
python -B -X utf8 herramientas/mcp_lorcana/verificar_cliente_codex.py
& herramientas/mcp_lorcana/.venv/Scripts/python.exe -B -X utf8 herramientas/mcp_lorcana/medir_mcp.py --salida herramientas/mcp_lorcana/mediciones-2026-09-30.json
```

Las pruebas atraviesan un proceso MCP real, con rutas con espacios y otro directorio de trabajo, handshakes antiguo/moderno, llamadas concurrentes, equivalencia CLI en formato completo, 20 oráculos trazados a fuentes, conservación exacta de fragmentos en lectura y fixtures de mantenimiento/fallo. Separan preparación de las llamadas de lectura. Véanse [resultados](RESULTADOS.md), [mediciones 0.2.0](mediciones-0.2.0-2026-09-30.json) y [referencia 0.1.0](mediciones-2026-09-30.json). Para renovar el informe sin borrar la referencia inicial, utiliza `--salida herramientas/mcp_lorcana/mediciones-0.2.0-2026-09-30.json`.

`verificar_cliente_codex.py` comprueba configuración estricta, inicialización y descubrimiento usando `app-server` del cliente instalado, sin crear chats ni llamar al modelo. Es diagnóstico de desarrollo; Codex puede crear sus propios artefactos de estado fuera del repositorio. En este entorno el aislamiento oculta la configuración al subproceso Codex: la comprobación funciona con autorización para ejecutarla fuera del aislamiento. No registres un segundo servidor global para compensar esa diferencia.

**Observado en cliente:** dos chats nuevos usaron MCP en modo consulta y produjeron respuestas con fuentes y ejemplo; véase la [auditoría](AUDITORIA_PRUEBA_2026-09-30.md). Quedan pendientes las consultas de ambigüedad/limitaciones y el enrutamiento editorial completo. Esa evaluación del asistente debe hacerse en una copia del repositorio para revisar artículo, índices y fecha sin modificar conocimiento real como demostración.

**Tras actualizar a 0.2.0:** reinicia el servidor `lorcana` en ajustes MCP y abre un chat nuevo para repetir la consulta auditada. Codex ya inicializa y descubre esta versión en la comprobación de desarrollo; falta observar la latencia del chat y su uso de la vista/instrucciones nuevas.

**Móvil:** la conexión del usuario ya está resuelta. Falta comprobar el uso de este MCP a través de ese acceso y la presentación de referencias; no hay configuración móvil pendiente incluida en la entrega.

El [plan](../consulta_lorcana/PLAN_MCP.md) conserva la opción futura de aprender publicación y uso remoto fuera de la app local. La entrega actual no contrata alojamiento ni publica el servidor.
