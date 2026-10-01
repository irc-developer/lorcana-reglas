# Verificación de la entrega · 30/09/2026

Implementación ejecutada en Windows, Python 3.14.3, SQLite FTS5 y PyMuPDF existentes. No se instaló una API de modelos ni un servicio. El índice preparado está en `.cache/indice.sqlite`, ignorado por Git. No se modificaron fuentes, artículos, índices editoriales ni portada; se conservaron los cambios previos del usuario.

## Pruebas ejecutadas

```powershell
python -X utf8 herramientas/consulta_lorcana/consulta.py actualizar --json
python -X utf8 herramientas/consulta_lorcana/test_consulta.py
python -X utf8 herramientas/consulta_lorcana/medir.py --salida herramientas/consulta_lorcana/mediciones-2026-09-30.json
```

Última suite: **15 pruebas, OK, 35,332 s**, incluidas **20 preguntas verificadas** mediante subtests. [Matriz y expectativas](evaluacion.json), [suite reproducible](test_consulta.py). La comparación numérica independiente del PDF comprueba continuidad y presencia de sus reglas sustantivas; se verifican citas textuales decisivas y páginas en la matriz. Se comprueban también números de regla ausentes y recuperación de notas oficiales sin utilizarlas como fichas de cartas. No se evalúa una respuesta generada por el sistema como oráculo.

| Grupo | Resultado |
|---|---|
| Regla directa, inglés/español, variantes sin tildes | Regla primaria correcta, versión 2.2.0 y páginas verificadas. |
| Carta exacta y nombre ambiguo | Fichas completas disponibles y versiones candidatas; no selección aproximada silenciosa. |
| Timing, reemplazos, robos múltiples, movimiento de daño | Reglas y excepciones primarias presentes, incluidas 1.12.2, 7.7.3.1, 6.5, 1.9.2.4 y 8.8.3. |
| Torneo | Política local identificada por sección con advertencia de copia superada. |
| Coconut / Pack Rush | Ámbitos separados y originales pertinentes; no se presentan como formato estándar. |
| Fuente antigua, carta ausente, listado parcial | Exclusión o estado insuficiente/limitado, sin inventar evidencia. |
| Belle / Wasabi / Minnie | Se conservan ausencia de ficha de Belle, set parcial y caso excluido de Wasabi, y falta de original local PCG para Minnie. |
| Continuidad entre páginas | CR 6.1.6 incluye definición en p.26 y ejemplo en p.27. Los diez cruces detectados se registran en el informe de extracción. |
| Símbolos | CR tinta/Fuerza/agotamiento; Coconut lore/agotamiento; notas del set lore/Fuerza verificados con renderizado e incorporados a tests. Un perfil PDF desconocido falla expresamente. |
| Solo lectura | Estado, regla, carta y consulta ejecutados en procesos nuevos; mismos archivos, hashes, tamaños y mtimes del repositorio. Fallback desactualizado/ausente también sin escrituras en su fixture. |
| Mantenimiento | Altas, cambios incluso con mismo mtime, renombrado con ID conservado, bajas, actualización fallida con último índice intacto, selección discrepante y sustitución del nombre de PDF sin cambiar código. |
| FTS5 ausente | Alternativa por tokens forzada y validada con evidencia primaria. |
| Modos | `consulta:`, `documenta:` y `actualiza:` reconocidos; proceso nuevo marca documentación requerida. No se ejecuta el workflow desde la CLI. |

La skill pasó el validador `quick_validate.py` de skill-creator. Se comprobó el contrato de modos y se enlaza la capa `.github/` explícitamente. Eso no acredita razonamiento del agente en una conversación nueva ni carga del selector móvil.

## Latencia medida

[Datos completos](mediciones-2026-09-30.json), p95 por rango más próximo (`ceil(0,95 × n)`). No se purgó caché del sistema operativo.

| Medición | n | Mediana | p95 |
|---|---:|---:|---:|
| Frío: recuperación en proceso nuevo | 20 | 890,651 ms | 1.010,372 ms |
| Frío: CLI con inicio de proceso y JSON | 20 | 1.051,988 ms | 1.171,375 ms |
| Caliente: mismo proceso, conexión nueva por consulta | 60 | **851,740 ms** | **957,307 ms** |
| Comprobación inicial completa de hashes | 60 | 262,072 ms | 274,762 ms |

Ambos modos recuperan de un índice persistente y comprueban todas las fuentes al principio y al final; las citas se vuelven a leer directamente. No hay daemon o conexión SQLite retenida. El coste inicial de comprobación es parte de la recuperación, no se suma otra vez. En la muestra caliente el máximo fue 1.006,733 ms: el objetivo orientativo de <1 s se alcanza en mediana y p95, no en toda ejecución. Razonamiento, redacción, permisos y transporte remoto no están medidos.

## Cobertura preparada

**487 archivos de evidencia, 4.516 fragmentos**; otros archivos de control/exclusión se hashean sin exponerse como conocimiento. Se detectaron **39 exclusiones declaradas** en la capa permitida, además de la exclusión completa por carpetas fuera de alcance.

| Categoría | Fragmentos |
|---|---:|
| Fichas de sets (incluye reimpresiones) | 2.763 |
| Casos locales interpretativos | 200 |
| CR: 489 reglas sustantivas + 66 secciones + 10 capítulos + 89 entradas de glosario | 654 |
| Localización española / explicaciones locales | 455 |
| Notas oficiales del set | 30 |
| Coconut | 4 |
| Consejos, experiencias, comunidad, Carde, recursos y resúmenes | 355 |
| Secciones de Tournament Rules local | 55 |

FTS5 utiliza normalización de tildes, apóstrofos, ligaduras y guiones para búsqueda; el texto original permanece en la base. Los PDF se extraen una vez por versión indexada; archivos no modificados se reutilizan. Un `actualizar` sin cambios devolvió **534 fuentes/control reutilizados y 0 parseados**.

## Mantenimiento oficial y límites

Se abrió la [página oficial de recursos](https://www.disneylorcana.com/en-US/resources/) y sus documentos el 30/09/2026:

- [CR 2.2.0](https://files.disneylorcana.com/Comprehensive-Rules_2.2.0-EN.pdf): 55 páginas, efectiva 9/07/2026, concordante en versión/fecha con la copia local. No se comparó su hash remoto con la copia local.
- [Tournament Rules publicada](https://files.disneylorcana.com/Tournament-Rules-7.14.2026_Update_EN.pdf): efectiva **14/07/2026**. La copia local declara **11/06/2026** y queda advertida; no se sustituyó la fuente.
- [Play Correction Guidelines](https://files.disneylorcana.com/Disney_Lorcana_Play_Correction_Guidelines_052124update.pdf): efectiva **21/05/2024**; §2.1 en pp.5–6 contrastada para Minnie. No hay original local indexado. La solución general local simplifica el plazo y omite la elección del oponente; se registra la discrepancia.
- [Coconut Rules](https://files.disneylorcana.com/FormatCoconut_Rules.pdf) y [Beta Coconut Cards](https://files.disneylorcana.com/FormatCoconut_BetaCoconutCards.pdf): beta, sin fecha/versión declarada. Ámbito separado.

Estos chequeos no son monitorización de futuras publicaciones. Las consultas ordinarias usan copias locales identificadas; una pregunta sobre actualidad necesita mantenimiento web separado. Las reglas originales contienen referencias internas inexistentes, conservadas con advertencia. La matriz de evaluación acepta detener un ruling cuando falta evidencia; no fabrica una respuesta para que pase una prueba.

La comprobación desde un **móvil real mediante Codex Remote queda pendiente**, incluyendo conexión del host, carga de skill y presentación de enlaces locales. Se verificaron comandos y señales en nuevos procesos locales, no una sesión remota ni una conversación nueva de Codex. [Procedimiento de uso y prueba remota](README.md), [tres ejemplos completos](EJEMPLOS.md).
