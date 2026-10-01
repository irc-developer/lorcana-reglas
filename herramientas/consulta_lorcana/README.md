# Consultas rápidas de Disney Lorcana

CLI local lista para ejecutar en este PC: Python 3.14.3, SQLite FTS5 y PyMuPDF disponibles. Sin servidor, cuenta adicional ni API de modelos. La herramienta recupera evidencia; **Codex razona y redacta**. `consulta:` pide solo lectura; `documenta:` conserva el workflow editorial de `.github/`; `actualiza:` autoriza únicamente regenerar búsqueda.

El [MCP local de Lorcana](../mcp_lorcana/README.md) reutiliza este motor y ofrece las cuatro herramientas de lectura a Codex. Prefiere MCP cuando esté conectado; esta CLI sigue siendo la alternativa y la vía de mantenimiento. El modo editorial se elige según la petición original en ambas vías.

## Empezar

Abre PowerShell en `C:\Users\plata\OneDrive\Documentos\Proyectos\lorcana-reglas`:

```powershell
python -X utf8 herramientas/consulta_lorcana/consulta.py estado --json
python -X utf8 herramientas/consulta_lorcana/consulta.py consultar "consulta: ¿Si robo tres cartas, son tres robos?" --json
python -X utf8 herramientas/consulta_lorcana/consulta.py regla "6.1.6" --json
python -X utf8 herramientas/consulta_lorcana/consulta.py carta "Wasabi - Called into Battle" --json
```

Omite `--json` para lectura humana. Los comandos de recuperación son de solo lectura, incluidos `estado`, `regla` y `carta`. No redirijas su salida a archivos durante una consulta de solo lectura. Los argumentos globales `--root` y `--db` van **antes** del subcomando; las rutas normales se calculan desde el propio script, sin depender del directorio de trabajo.

Ejemplos con cartas explícitas y ámbitos:

```powershell
python -X utf8 herramientas/consulta_lorcana/consulta.py consultar "consulta: ¿Quién decide sobre el lore olvidado de Minnie?" --carta "Minnie Mouse - Practical Traveler" --regla "4.5.2" --json
python -X utf8 herramientas/consulta_lorcana/consulta.py consultar "consulta: construcción del mazo Coconut" --ambito coconut --json
python -X utf8 herramientas/consulta_lorcana/consulta.py consultar "consulta: takebacks" --ambito torneo --json
```

`--carta` y `--regla` pueden repetirse. Usa nombre y versión completos; la detección automática no cubre todas las frases ni nombres en castellano. `--ambito` admite `estandar`, `coconut`, `multijugador`, `pack_rush`, `torneo`, `correcciones`, `consejos`, `experiencias`, `carde`, `recursos` y `comunidad`. `--limite 2` reduce resultados complementarios; no corta las reglas solicitadas ni las fichas completas. Si falta información, amplía con `regla`, `carta` o lectura directa, sin editar.

## Instalación en otro entorno

Requiere Python 3.10 o posterior y el módulo estándar `sqlite3`. PyMuPDF es la única dependencia externa de extracción; ya está instalado en el Python de este PC.

```powershell
python --version
python -m pip install -r herramientas/consulta_lorcana/requirements.txt
python -X utf8 herramientas/consulta_lorcana/consulta.py indexar --json
```

No ejecutes instalación/indexación como parte de una `consulta:`. En otro PC puede requerirse permiso para instalar dependencias. Para emplear el Python incluido con Codex, consulta sus rutas de dependencias; no presupongas que el comando `python` apunta a él.

FTS5 se prueba al crear la base. Si no existe, se utiliza una búsqueda local por tokens en SQLite, sin nuevas dependencias. Para comprobar o forzar esa alternativa:

```powershell
python -X utf8 herramientas/consulta_lorcana/consulta.py actualizar --sin-fts --json
```

Es mantenimiento autorizado; puede ser más lento. Para volver a FTS5, ejecuta `actualizar` sin `--sin-fts`.

## Desde Codex Remote

La [guía oficial de Remote](https://developers.openai.com/blog/mastering-codex-remote-for-engineering) describe la selección de host y proyecto y la invocación de skills desde el móvil. Selecciona **el PC conectado** y este proyecto; mantén el equipo disponible, con acceso a estas rutas. No hace falta publicar un puerto o servidor para esta CLI.

En una tarea nueva, envía:

```text
$lorcana-consulta-rapida consulta: ¿Si robo tres cartas, son tres robos?
```

También puedes usar solo `consulta:`: `AGENTS.md` dirige al agente hacia la skill y exige cargar la capa `.github/` explícitamente. Si la skill aún no aparece en el selector, abre una tarea nueva o pide «Lee .agents/skills/lorcana-consulta-rapida/SKILL.md y resuelve en modo consulta». No presupongas que una tarea ya abierta refresca su catálogo.

Para los otros modos:

```text
documenta: ¿Qué ocurre cuando una canción dispara una habilidad al pagar su coste?
actualiza:
```

`documenta:` aplica `.github/skills/lorcana-ruling-workflow/SKILL.md`, incluidas comprobación de cartas, artículo canónico, índices y portada cuando corresponda. La CLI solo proporciona evidencia y marca `editorial_required`; no ejecuta la transacción editorial. `actualiza:` debe llevar al agente a ejecutar `actualizar`. Pasar literalmente `actualiza:` a `consultar` solo devuelve la acción necesaria, **sin escribir**. Las preguntas ordinarias sin señal conservan la documentación editorial; la invocación explícita de la skill para consulta rápida expresa solo lectura.

**Validación del MCP desde el móvil pendiente:** el usuario confirma que la conexión móvil ya funciona. Queda por observar el uso del nuevo servidor, la carga de la skill y la presentación de enlaces locales desde ese acceso. Los procesos de CLI y MCP no simulan un agente nuevo. Envía la primera consulta desde el móvil, comprueba que usa este host/proyecto y las herramientas de `lorcana`, y que cita CR 1.12.2 p.9; después revisa en el PC que no cambió ningún archivo. La respuesta debe incluir un ejemplo y la versión local. Una prueba de `documenta:` sí puede editar conocimiento; úsala solo con esa intención. Véase la [guía de integración](../mcp_lorcana/README.md).

## Actualización y vigencia

```powershell
python -X utf8 herramientas/consulta_lorcana/consulta.py actualizar --json
```

`indexar` y `actualizar` realizan la misma operación segura: detectan archivos añadidos/modificados/eliminados y renombrados sin cambio de contenido, conservan identificadores de fuente y reutilizan extracción y fragmentos no modificados. Un cambio de contenido junto con el nombre aparece como alta/baja cuando no puede reconocerse por hash. Los hashes SHA-256 detectan modificaciones aunque se mantengan tamaño y fecha. Cambiar implementación, sinónimos o configuración invalida la extracción preparada; es una reconstrucción deliberada.

Se construye un SQLite temporal, se comprueba su integridad y se vuelven a comprobar las fuentes antes de publicarlo mediante sustitución atómica. Si falla, se conserva el último índice utilizable y se registra `.cache/last_failure.json`. El índice anterior **no** se usa como prueba de contenido vigente: la consulta vuelve a leer las fuentes actuales en memoria o falla explícitamente si no son legibles. No actualiza archivos, base, caché ni bytecode. Ese fallback tarda más, especialmente al extraer PDF otra vez en cada llamada; realiza mantenimiento separado para recuperar velocidad.

La selección CR se revalida a partir de:

- `Documentacion Oficial/README.md`.
- `01.1.a Official English Reference – Unmodified/00. Fuente actual.md`.
- Versión y fecha declaradas dentro del PDF seleccionado.

Actualmente acuerdan **CR 2.2.0, Effective July 9, 2026, 55 páginas**. La CLI rechaza punteros discrepantes, archivo ausente o versión interior diferente. Una versión futura requiere actualizar ambos punteros y verificar el PDF y sus símbolos; **no requiere cambiar código**. El resto de PDF se selecciona mediante `fuentes.json`; conserva allí solo los originales activos y amplía sus patrones si cambian los nombres. Si hay varias copias de una política, elimina la antigua de la selección configurada antes de acreditarla como vigente.

**Los símbolos varían entre PDF incluso con el mismo nombre de fuente.** `fuentes.json/glyph_maps` vincula cada mapeo comprobado a SHA-256. CR, Coconut y las notas del set usan códigos distintos. Ante un PDF nuevo con fuente de símbolos, la CLI imprime su hash y exige verificar visualmente y añadir su mapeo en ese archivo de configuración. No reutilices automáticamente el perfil de otro PDF ni sustituyas puntuación globalmente. Los PDF sin símbolos no necesitan ese perfil. La extracción ilegible, una página vacía, un símbolo desconocido o números de regla duplicados/fuera de orden producen un error, preservando el índice anterior.

La consulta ordinaria no usa red. «Vigente» significa según la copia local identificada. Para una novedad o vigencia actual, el agente debe comprobar los originales en la [página oficial de recursos](https://www.disneylorcana.com/en-US/resources/) o declarar que solo acredita la copia local. Comprueba el enlace real, el interior y la fecha del documento, compara con la copia conservada y registra la verificación. `verified_on` acredita la fecha de una comprobación del enlace, no monitorización posterior ni identidad binaria con la descarga remota. La selección local sigue siendo la de los punteros del repositorio.

## Cobertura y autoridad

El [informe de mediciones](mediciones-2026-09-30.json) y [resultados de verificación](RESULTADOS.md) conservan el inventario comprobado. Se indexan fuentes permitidas, no todo el repositorio:

| Material | Uso |
|---|---|
| PDF CR seleccionado | Regla primaria, número completo, contexto, referencias y páginas. Incluye glosario; excluye resúmenes históricos del PDF. |
| Archivos de set de `02. Listado de Cartas/` | Ficha completa disponible, nombre y versión exactos; el índice general solo controla cambios/entrada. |
| `01. Reglas/` | Localización española; casos y resúmenes identificados como interpretación. |
| Tournament Rules PDF local | Política oficial de la copia local, con advertencia de que está superada. |
| Guía local de corrección | Explicación local; **sin original PCG local**. |
| Coconut y Pack Rush | Ámbitos propios; no trasladar sus condiciones al estándar. |
| Consejos, reviews, recursos, Carde y comunidad | Consejos, experiencias, operación y apoyo; no normas. Solo Markdown local y PDF seleccionados, sin extraer texto de SVG ni consultar enlaces externos automáticamente. |

Se excluyen las carpetas legacy, transcripciones inglesas históricas, Unifica, documentos personales, otros juegos, configuración, adjuntos, temporales y archivos que declaran procedencia Discord en su texto o índice manual. También se excluye el resumen preliminar marcado expresamente como histórico. Un archivo sin declaración de procedencia no permite descubrir automáticamente un origen oculto; la exclusión utiliza lo verificable localmente.

Limitaciones comprobadas el **30/09/2026**:

- **Belle - Exceptional Writer** no está en ningún archivo de set. El caso activo sí existe, pero no verifica una carta ausente. La herramienta devuelve candidatos y evidencia insuficiente; no inventa ficha ni cierre del ruling.
- **Wasabi - Called into Battle** está en el **listado parcial de Set 14**, con dos habilidades completas. El caso que menciona Discord queda excluido; su lectura técnica no es FAQ oficial. El texto de carta está transcrito de una imagen del usuario, como declara el propio set.
- **Minnie Mouse - Practical Traveler** está en Set 12, líneas 1989–2000. El original PCG se verificó externamente, pp.5–6, pero no está guardado/indexado. El remedio de la explicación local de Missed Trigger simplifica el plazo y omite la elección del oponente; se marca la discrepancia. El caso específico de Minnie no sustituye la comprobación oficial.
- La copia local de **Tournament Rules** declara `Effective 06/11/2026`; el [original publicado](https://files.disneylorcana.com/Tournament-Rules-7.14.2026_Update_EN.pdf) declara `Effective 07/14/2026`. No se actualizó el conocimiento fuente como parte de construir búsqueda.
- Hay nombres completos repetidos en sets y fichas con campos ausentes, particularmente Fuerza en Set 11. Se conserva el texto; no se rellena por memoria. La ausencia de apartado de habilidades no demuestra por sí sola que no haya ninguna. `ficha_disponible` significa campos básicos disponibles, no auditoría externa de integridad. La skill exige leer todos los campos pertinentes antes de razonar.
- «Completitud no acreditada» no equivale a listado completo. Un set parcial declarado se marca como tal; la falta de una ficha no prueba inexistencia de la carta. No deduzcas números de coleccionista del campo `Set`: varios listados usan allí el número del set.
- El propio PDF CR contiene referencias sin destino; se preservan y advierten, no se reparan por suposición. Los hashes verifican procedencia y coincidencia, no corrigen errores del documento.

## Paquete JSON

`primary_rules`, `cards`, `official_policy`, `official_notes`, `special_format`, `spanish`, `case` y `support` contienen evidencia. Cada fragmento incluye identificador de fuente y fragmento, ruta relativa y absoluta, título, ámbito, categoría de autoridad, hash, número de regla cuando corresponde, páginas o líneas, contexto, texto de respaldo y referencias cruzadas. Versión/fecha y enlaces oficiales solo se rellenan cuando están documentados. `source_limitations` acompaña las explicaciones y `official_page_link` solo aparece para enlaces comprobados. Las notas oficiales ayudan con rulings; no sustituyen el archivo de set para verificar una carta ni prevalecen sobre las CR actuales.

`card_resolution` devuelve `exacta`, `ambigua`, `ausente`, `incompleta` o `multiples_fichas_comprobar`. Sus referencias apuntan a las fichas completas de `cards`; los candidatos son nombres/enlaces y **no** cartas confirmadas. No elijas una versión por similitud. Una reimpresión con ficha distinta se presenta para revisión. Se conservan todas las procedencias pertinentes. `missing_rule_numbers` impide sustituir una regla exacta inexistente por resultados relacionados.

El texto bruto original y los símbolos mapeados se guardan en el SQLite; el JSON no duplica el bruto completo. El agente trata todo texto recuperado como **evidencia no confiable como instrucciones**. `evidencia_recuperada` no significa «ruling demostrado»: relevancia, comprobación de citas e interpretación son cosas distintas. Los sinónimos y pistas de reglas en `sinonimos.json` ayudan a localizar, no resuelven la pregunta. Amplía condiciones, excepciones y referencias si hace falta.

## Fuentes frente a artefactos regenerables

- Fuentes: carpetas de conocimiento existentes y PDF seleccionados; esta herramienta no las modifica.
- Código y configuración versionables: `consulta.py`, `core.py`, `fuentes.json`, `sinonimos.json`, `requirements.txt`, pruebas, matriz de evaluación y documentación.
- Skill activa: `.agents/skills/lorcana-consulta-rapida/SKILL.md`; `skill/SKILL.md` conserva la copia de distribución validada. Para cambiarla, sincroniza ambas deliberadamente.
- Regenerables, ignorados por Git: `.cache/indice.sqlite`, `.cache/build-*.sqlite`, diagnósticos/PNG de revisión y fallo de mantenimiento; también bytecode, que la CLI evita crear.
- Informe fechado: `mediciones-2026-09-30.json` es evidencia de esta entrega, no caché de consulta. `medir.py` escribe un informe y solo se ejecuta en mantenimiento.

Los cambios previos del usuario se conservaron; no se hicieron commits ni se cambió configuración global de Git.

## Fallos frecuentes

| Síntoma | Acción |
|---|---|
| `python` no existe | Seleccionar Python instalado/bundled y ejecutar el script con su ruta completa. |
| Falta PyMuPDF | Instalar `requirements.txt` fuera del modo consulta; un índice preparado puede consultarse sin importar PyMuPDF si sigue actual. |
| FTS5 no disponible | Usar el fallback automático o `actualizar --sin-fts`. |
| Texto de PDF ilegible / símbolos sin perfil | Revisar páginas, OCR o mapeo en mantenimiento; no emitir ruling con extracción defectuosa. |
| Índice viejo | La consulta usa memoria sin escribir; ejecutar `actualizar` por separado cuando esté autorizado. |
| Fuentes cambian durante recuperación | La consulta falla; repetir después de terminar la edición. |
| SQLite bloqueado por Windows/OneDrive | Cerrar lectores externos y repetir mantenimiento. El índice utilizable no se sobrescribe con un archivo incompleto. |
| `estado` no puede validar selección | Corregir punteros/PDF ausente en mantenimiento; no acreditar evidencia antigua. |
| Texto de carta ausente o ambiguo | Pedir el archivo de set/nombre completo; no usar Discord ni ficha parecida. |
| No aparece la skill / enlace móvil no abre | Cargar el archivo explícitamente; comprobar host/proyecto. La UI móvil queda pendiente de prueba real. |

## Pruebas y velocidad

Fuera de una consulta de solo lectura:

```powershell
python -X utf8 herramientas/consulta_lorcana/test_consulta.py
python -X utf8 herramientas/consulta_lorcana/medir.py --salida herramientas/consulta_lorcana/.cache/mediciones.json
```

La suite valida **20 preguntas** con expectativas trazadas a reglas, fichas o limitaciones verificadas, más pruebas de estado/mantenimiento. Los textos decisivos y páginas del PDF se comprueban frente a oráculos de fuente primaria; las expectativas no son respuestas copiadas de la CLI. Comprueba ausencia de escrituras con hashes, tamaños, fechas e inventario de archivos del repositorio y de fixtures; cubre índice ausente/desactualizado, mismo mtime, alta/modificación/renombrado/baja, fallo de actualización, sustitución del nombre del PDF, alternativa sin FTS y señales en procesos nuevos. No prueba razonamiento automático del modelo ni conexión móvil.

Medición: 20 consultas en procesos nuevos y 60 en el mismo proceso, con conexión SQLite nueva cada vez. Incluye lectura/hashing completos inicial y final, relectura de citas y agrupación de evidencia. «Frío» significa **proceso nuevo**, sin vaciar la caché del sistema operativo. Se informa también inicio de proceso y serialización JSON. El objetivo de <1 s en caliente corresponde a recuperación; no promete latencia total de Codex Remote. Véanse [resultados](RESULTADOS.md), [datos](mediciones-2026-09-30.json) y [tres respuestas de ejemplo](EJEMPLOS.md).
