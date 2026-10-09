# Plan de actualización de la wiki: CR 2.2 → CR 2.3

**Preparado:** 9 de octubre de 2026.
**Estado:** adaptación ejecutada y validada; commit, publicación y retirada en curso.
**Decisión posterior de Iván:** «En cuanto la tengamos completada la publicaremos». La publicación y retirada se ejecutan ahora con avisos de vigencia; la aplicación normativa cambia el 16/10/2026.
**Objetivo:** adaptar la wiki a CR 2.3.0, retirar CR 2.2 de la referencia activa y de la publicación seleccionada, y crear una entrada que explique los cambios generales entre ambas versiones.

## 1. Fecha de transición y alcance

La página oficial de recursos anuncia la actualización del 8 de octubre de 2026, pero la portada del nuevo PDF establece **Version 2.3.0, Effective October 16, 2026**: entra en vigor el **16 de octubre de 2026**. Publicación y entrada en vigor son fechas distintas.

- **Del 9 al 15 de octubre:** preparar fuentes, comparación, traducciones, artículos y selección de publicación. Cualquier anticipo público de 2.3 debe indicar claramente que entra en vigor el 16 de octubre. La referencia vigente continúa siendo 2.2.0.
- **Al completar la revisión, según la instrucción posterior de Iván:** publicar la adaptación, portada y entrada general, y retirar exclusivamente las seis páginas antiguas después de verificar su reemplazo.
- **Desde el 16 de octubre:** el motor actualizado selecciona 2.3.0 por fecha y valida ambos originales. Los anticipos excluidos pasan a evidencia activa. Si un índice de 2.2 sigue preparado, la consulta lee 2.3 en memoria sin escribir hasta el siguiente mantenimiento.
- No se programa una tarea futura. La selección por fecha forma parte del motor; los clientes MCP ya abiertos deben reiniciar su servidor para cargar el código actualizado.

«Retirar 2.2» significa dejar de presentarla como vigente y despublicar los documentos antiguos expresamente seleccionados. Se conserva el PDF y el historial editorial local para contrastes; no se borra la evidencia de la comparación ni el historial de Git. Tampoco se eliminan las secciones cuyo número sea 2.2: por ejemplo, **2.2. Etapa de preparación** pertenece al reglamento y debe permanecer.

El alcance incluye reglas españolas, glosario, resúmenes afectados, casos que dependan de los cambios, referencia inglesa, fuentes y búsqueda local, navegación y publicación selectiva. Las políticas de torneo, la guía de corrección, Coconut y el catálogo de cartas no se migran como si fueran parte de CR 2.3. Solo se revisan sus enlaces o dependencias cuando corresponda.

## 2. Fuentes comprobadas y estado inicial

Los párrafos de esta sección registran la preparación anterior a la ejecución. El estado posterior se documenta en `cr-2.3-ejecucion.md`.

| Fuente | Identificación comprobada | Uso |
| --- | --- | --- |
| [Recursos oficiales](https://www.disneylorcana.com/en-US/resources/) | Comprehensive Rules actualizadas el 08/10/2026; enlace inglés al PDF de octubre | Procedencia y comprobación de nuevas revisiones |
| [CR 2.3 oficial en inglés](https://files.disneylorcana.com/CRUpdate_EN_Oct-2026.pdf) | 2.3.0; efectiva 16/10/2026; 56 páginas; portada p. 1; Update Summary pp. 53–54 | Autoridad de la migración |
| `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf` | 2.2.0; efectiva 09/07/2026; 55 páginas | Base de comparación; vigente hasta el cambio de fecha |
| [Notas oficiales de Hyperia City](https://www.disneylorcana.com/en-US/news/2026/10/hyperia-city-set-release-notes) | Publicadas el 08/10/2026 | Contexto y rulings del set; no sustituyen el PDF |

SHA-256 del PDF 2.3 descargado para preparar este plan: `8b7a458169978a13b688493d4b24d713bdc8baee32ce5e774b0515079a0b91fe`.

La comprobación preparatoria incluyó extracción del documento, comparación textual inicial y revisión visual de portada, resumen oficial y páginas seleccionadas. **No equivale a una auditoría completa de las 56 páginas.** El PDF se consultó en una carpeta temporal; aún no se ha incorporado al corpus oficial del repositorio.

Actualmente `Documentacion Oficial/README.md`, `01.1.a Official English Reference – Unmodified/00. Fuente actual.md` y `Empecemos.md` declaran 2.2.0. El MCP también selecciona ese PDF. `estado_fuentes` devuelve índice utilizable pero desactualizado; su último mantenimiento es del 30/09/2026. No se ha actualizado en esta tarea.

### Cambios previos que deben preservarse

El estado inicial de Git contiene cambios en `.obsidian/workspace.json`, `Bodyguard.md`, `Strange Things y This Growing Pressure - prohibición frente a obligación condicional.md`, `Empates intencionales y acuerdos de grupo.md`, el índice de casos, `Empecemos.md` y el registro de tags. Hay además una nota nueva sobre Peter Pan's Shadow y Pegasus y archivos de trabajo no versionados.

Antes de ejecutar, repetir el inventario: podría haber nuevas ediciones. No usar un commit global ni mezclar esos cambios con la migración. En archivos compartidos, aislar los cambios propios antes de commit y Publish, o coordinar la integración de la transacción previa. El contenido completo publicado debe corresponder a la selección y al commit validados.

## 3. Entregables de la ejecución

1. PDF 2.3 original, sin modificar, en `Documentacion Oficial/CRUpdate_EN_Oct-2026.pdf`, con versión, fecha, páginas, URL y hash registrados.
2. Matriz interna de diferencias en `.github/planes/cr-2.3-matriz-diferencias.tsv`: regla o término; texto/página 2.2; texto/página 2.3; alta, baja, modificación o traslado; naturaleza del cambio; archivo afectado; decisión editorial; estado de revisión.
3. Adaptación castellana actualizada y las dos secciones nuevas de contadores y Adventurous.
4. **Nueva entrada pública:** `01. Reglas/9. Resúmenes/Reglas completas de Disney Lorcana 2.3 - cambios respecto a 2.2.md`.
5. Casos canónicos e índices actualizados cuando el contraste lo exija; sin duplicar artículos ya existentes.
6. Ambos selectores normativos, portada y búsqueda sincronizados con la fase temporal correcta.
7. Inventario explícito de altas/actualizaciones y de retiradas en Publish, resultado de validación y comprobación de los enlaces públicos.
8. Commits y push que contengan únicamente la migración; informe final de lo publicado y retirado.

Los informes de implementación, incidencias del PDF y comprobaciones técnicas se guardarán en `.github/planes/`, fuera de las páginas para lectores.

## 4. Cobertura mínima del resumen oficial

El Update Summary de pp. 53–54 enumera **11 entradas principales, 8 ajustes de redacción/referencias y 7 entradas de glosario**. No son 26 reglas individuales: algunas entradas abarcan secciones enteras. La matriz debe cubrirlas todas y añadir diferencias reales que no aparezcan en ese resumen.

### 4.1. Reglas nuevas o modificadas

| Referencia 2.3 | Trabajo editorial | Destino principal en `01. Reglas/` |
| --- | --- | --- |
| 1.13, p. 9 | Incorporar contadores e ink drops; distinguirlos de cartas y tinta | **Crear** `1. Principios generales/1.13. Contadores (Counters).md`; revisar 1.9 y 7.5 |
| 4.3.2, p. 13 | Explicar continuidad del proceso si la carta cambia de zona | `4. Acciones de turno (Turn Actions)/4.3. Jugar una carta (Play a Card).md` |
| 4.3.3 y 6.7.9, pp. 13 y 38 | Revisar el momento y orden de aplicación de efectos de entrada | 4.3 y `6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects).md` |
| 4.7.1–4.7.2, p. 18 | Revisar elecciones de movimiento y movimiento a la misma localización | `4. Acciones de turno (Turn Actions)/4.7 Mover un personaje (Move a character).md` |
| 6.1.4.2, p. 26 | Incorporar decisiones independientes cuando hay varios «may» | `6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.1. General (General).md` |
| 6.7.6.1, p. 37 | Actualizar resolución por partes entre jugadores | 6.7 y `9. Multijugador (Multiplayer)/9.2. Reglas adicionales de multijugador (Multiplayer Rules).md` |
| 6.7.7, p. 37 | Incorporar la lista de características y valores característicos | 6.7 y `5. Cartas y tipos de carta (Cards and Card types)/5.2. Partes de una carta (Parts of a Card).md` |
| 8.1.2, p. 41 | Explicar comparación de duraciones de palabras clave no acumulables | `8. Palabras clave (Keywords)/8.1. Generalidades (General).md` |
| 8.16, p. 44 | Incorporar Adventurous y su relación con otras acciones | **Crear** `8. Palabras clave (Keywords)/8.16. Aventurero (Adventurous).md`; revisar 4.5, 4.6 y 3.4 |

«Aventurero» y «gotas de tinta» serán términos de adaptación editorial; conservar los nombres ingleses y comprobar si hay terminología oficial española antes de cerrar. No presentar una traducción propia como traducción oficial.

### 4.2. Ajustes de redacción, referencias y pagos

| Referencias del resumen | Acción |
| --- | --- |
| 4.3.2.1 | Actualizar la zona desde la que se revela la carta |
| 4.3.2.4, 4.4.3.4 y 4.7.3.4 | Incorporar ink drops en los tres procesos de pago; comprobar otras explicaciones de costes que puedan quedar incompletas |
| 5.1.1.5 | Corregir la referencia numérica según el PDF |
| 6.1.14.3 | Precisar el alcance de acciones sobre cartas reveladas |
| 6.4.2.1 y 6.4.2.3 | Ajustar qué pueden afectar las habilidades estáticas |

Destinos adicionales: `4. Acciones de turno (Turn Actions)/4.4. Usar una habilidad activada (Use an Activated Ability).md`, `5. Cartas y tipos de carta (Cards and Card types)/5.1. Estados de las cartas (Card States).md`, `6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.4. Habilidades Estáticas (Static Abilities).md` y `1. Principios generales/1.5 Costes (Costs).md`.

### 4.3. Glosario

Actualizar `01. Reglas/Glosario.md` contrastando sus entradas con pp. 47–53:

- Modificar `action, turn`, `passing the bag`, `Set step` y `triggered ability`.
- Añadir `counter` e `ink drop`.
- Retirar la entrada duplicada `Turn action`, conservando la definición correspondiente en `action, turn`.

Revisar enlaces y referencias de cada entrada y su traducción existente, sin limitarse a copiar los títulos del Update Summary.

### 4.4. Diferencias y deuda editorial detectadas fuera del resumen

- **7.1.6.1:** la comparación inicial detecta su eliminación. Revisar referencias a ese número en `7. Zonas (Zones)/7.1. General.md` y en casos; contrastar el principio aplicable con 6.7.8.1 antes de sustituir citas. Una eliminación de duplicación no debe describirse automáticamente como cambio de resultado.
- **8.10.6:** la extracción detecta una precisión para Shift sobre uno o varios personajes. Verificar visualmente la página y ajustar `8. Palabras clave (Keywords)/8.10. Cambio (Shift).md` y sus ejemplos si corresponde.
- **6.1.14.1–6.1.14.2:** el ejemplo de cartas reveladas pasa de 6.1.14.2 a 6.1.14.1. Separar este traslado de la regla nueva 6.1.14.3.
- **8.1.1:** la lista de palabras clave del propio PDF no incluye Adventurous, aunque sí existe 8.16. Registrar la discrepancia; la lista castellana puede enlazar la sección nueva, sin atribuir al original una enumeración que no contiene.
- **Bodyguard:** el Markdown de 8.3.2 todavía habla de un efecto de reemplazo. Los dos PDF comparados ya describen esa habilidad como estática. Corregir la deuda de localización y revisar resúmenes dependientes; no anunciarla como una novedad textual de 2.3 sin comprobar el historial.
- **`9. Resúmenes/Jugar una carta.md`:** aún dice que las acciones nunca entran en la zona de juego y contiene un encabezado de desafío dentro del proceso de jugar. Reescribirlo según 4.3 y 6.7; registrar esas correcciones como deuda previa, separadas del delta 2.2 → 2.3.
- **`9. Resúmenes/Tipos de habilidades.md`:** conserva referencias legacy y presenta «enter/enters» como identificación general de reemplazos. Revisar el documento completo frente a la versión nueva y retirar cualquier afirmación incompatible.

La comparación automática también detecta diferencias de ligaduras, comillas, diagramas y saltos de página. No convertirlas en cambios funcionales ni contabilizarlas como reglas distintas.

## 5. Nueva entrada general de cambios

**Ruta:** `01. Reglas/9. Resúmenes/Reglas completas de Disney Lorcana 2.3 - cambios respecto a 2.2.md`.
**Título:** «Reglas completas de Disney Lorcana 2.3: cambios respecto a la versión 2.2».

Estructura prevista:

1. Introducción con versión, publicación, entrada en vigor y límites del resumen; aviso de futura vigencia si se publica antes del 16/10.
2. Resumen de los cambios que afectan a una partida.
3. Contadores e ink drops.
4. Adventurous.
5. Continuidad al jugar una carta y efectos de entrada en juego.
6. Movimiento por acción y por efecto.
7. Resolución por partes entre jugadores.
8. Duraciones de palabras clave no acumulables.
9. Opcionalidad, características y cartas reveladas.
10. Correcciones, traslados, referencias y glosario, incluido lo detectado fuera del Update Summary.
11. Fuentes oficiales y enlaces a las secciones españolas actualizadas.

Cada cambio relevante debe explicar el comportamiento anterior, el nuevo y su consecuencia práctica, con número y página verificados en ambos PDF cuando proceda. Distinguir novedades funcionales, aclaraciones, movimientos de texto y correcciones. No trasladar al artículo público el informe técnico de ejecución ni reproducir íntegramente los reglamentos.

Los ejemplos con cartas se verificarán en `02. Listado de Cartas/`, incluido `Set 14 - Hyperia City.md`. Los enlaces de lectura usarán imágenes verificadas de Lorcast. No crear wikilinks públicos al catálogo ni reconstruir URLs de imagen. Para Adventurous, revisar interacción con Reckless, posibilidad de cantar o usar habilidades y personajes con 0 de Leyenda.

## 6. Revisión de casos y material derivado

Buscar por números de regla, conceptos y conclusiones en toda la sección 11. Esta lista inicia la revisión; no obliga a modificar todos los archivos si siguen siendo correctos.

| Cambio | Casos existentes que revisar primero |
| --- | --- |
| Duraciones de palabras clave | `11.5. Keywords/Peter Pan's Shadow y Pegasus - duración de Evasive.md`; `Ancestral Guitar no convierte Singer en Singer X.md`; `Heredar una palabra clave al hacer shift.md` |
| Entrada en juego | `11.5. Keywords/Bodyguard.md`; `11.4. Habilidades/Merida - Wisp Conjurer entra ya agotada.md`; casos de habilidades estáticas y reemplazos |
| Carta jugada cambia de zona | `11.3. Costes y Requisitos/Scrooge McDuck - Resourceful Miser desde The Black Cauldron.md`; `11.2. Zonas y Movimientos/Remember Me permite jugar personajes desde la mano y el descarte.md` |
| Efectos entre jugadores | `11.0. Timing y Resolución/No hay bolsa entre la parte del jugador activo y la del no activo.md`; `11.6. Interacciones Complejas/Colors of the Wind - Resolución de robo múltiple.md`; dudas de bolsa y orden multijugador |
| Movimiento | `11.7. Dudas por desarrollar/Moverse a una localización recién jugada.md`; casos con localizaciones, elecciones y movimiento por efectos |
| Varios «may» | `11.0. Timing y Resolución/Woody - Helping a Friend resuelve las opciones en el orden impreso.md`; casos de costes opcionales y resolución parcial |
| Características | `11.6. Interacciones Complejas/Headless Horseman y Wreck-It Ralph - último valor conocido y bolsa.md`; casos de valores, clasificaciones y última información conocida |

La nota nueva sobre Peter Pan's Shadow ya distingue 2.2 y la futura 2.3: integrar su contenido cuando se cierre su transacción previa, sin sobrescribirlo ni recrear el artículo. La misma precaución se aplica a Bodyguard y los archivos compartidos pendientes.

Solo crear casos nuevos si falta un canónico que cubra el concepto. Si se documentan, aplicar el workflow completo de casos: verificación de cartas, deduplicación, plantilla, tags, índice, contadores, fecha, commit, push y Publish selectivo.

Revisar también `9. Resúmenes/Declarar un desafío.md`, `Verificaciones del Estado del Juego.md`, 7.5 y 7.7, y la documentación de multijugador. No deducir cambios de GSC o de la bolsa solamente del nuevo orden por partes: contrastar las reglas correspondientes.

## 7. Retirada de 2.2 y navegación

### Selección normativa

La transición fechada se documenta conjuntamente desde esta publicación:

- `Documentacion Oficial/README.md`.
- `01.1.a Official English Reference – Unmodified/00. Fuente actual.md`.
- `Empecemos.md`: versión, fecha efectiva y enlace visible a la entrada de cambios.

Ambos selectores documentan los dos originales y su periodo. El motor valida sus hashes y utiliza 2.2 hasta el 15/10 y 2.3 desde el 16/10. El PDF previo aparece primero para que un cliente antiguo abierto no interprete anticipadamente 2.3 como vigente. La fecha visible de la portada será la fecha real de publicación material; ya muestra 09/10/26 y no necesita una edición artificial durante la planificación.

Conservar `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf` como histórico. El motor añade como CR únicamente el PDF seleccionado; comprobar que los patrones auxiliares no vuelven a introducir el anterior. No presentar los Markdown numerados ingleses como una transcripción consolidada: mantener y actualizar el aviso de alcance y revisar los que resulten afectados.

### Páginas 2.2 que retirar de la publicación activa

Inventariar si estas seis notas están publicadas y registrar las rutas exactas presentes en Publish:

1. `01. Reglas/9. Resúmenes/Reglas completas de Disney Lorcana 2.2 - cambios respecto a 2.1.md`.
2. `01. Reglas/9. Resúmenes/CR 2.2 - matriz de diferencias respecto a CR 2.1.md`.
3. `01. Reglas/9. Resúmenes/CR 2.2 - comparación final con Attack of the Vine.md`.
4. `01. Reglas/9. Resúmenes/CR 2.2 - revisión editorial del PDF oficial.md`.
5. `01. Reglas/9. Resúmenes/CR 2.2 - resumen de implementación.md`.
6. `01. Reglas/9. Resúmenes/Attack of the Vine - cambios anunciados y control para CR 2.2.md`.

Se conservarán localmente con un aviso inequívoco: **«Se conserva como registro histórico»**, periodo de referencia y remisión a la nueva entrada. El motor ya excluye documentos con esa declaración; verificar el resultado después del mantenimiento. Los informes técnicos dejan de ser páginas de lectura pública.

Actualizar los enlaces activos que apunten a esos documentos antes de despublicarlos. Conservar referencias de versiones antiguas cuando formen parte de una comparación expresamente histórica. Sustituir citas normativas a 2.2 solo tras revisar el fundamento contra 2.3; no hacer un reemplazo masivo de números o URLs.

Si el PDF 2.2 o avisos ingleses antiguos están publicados como recursos activos, añadir sus rutas exactas al inventario de retirada o actualización. Para fuentes oficiales, preferir el enlace externo al nuevo PDF. No retirar recursos por mera coincidencia con la cadena «2.2».

## 8. Búsqueda local y MCP

1. Incorporar la URL comprobada del nuevo PDF en `herramientas/consulta_lorcana/fuentes.json/verified_urls`; conservar la URL antigua identificada como histórica.
2. Verificar visualmente los glifos del PDF 2.3 y registrar su mapeo vinculado a su SHA-256. No reutilizar automáticamente el mapeo 2.2: tinta, agotamiento, Fuerza, Voluntad, Leyenda y movimiento deben comprobarse en páginas adecuadas.
3. Revisar `sinonimos.json` para contadores, ink drops y Adventurous; validar referencias nuevas o eliminadas.
4. Actualizar la documentación activa de consulta/MCP y `.github/prompts/crear-consulta-rapida-lorcana.prompt.md`. No modificar retrospectivamente auditorías o mediciones fechadas del 30/09; son evidencia histórica. No confundir versiones del SDK o del servidor con la versión de CR.
5. Revisar fixtures y oráculos de `test_consulta.py` y `test_mcp.py` que fijan PDF, versión, páginas o textos anteriores; conservar pruebas de sustitución de fuente y lectura sin escrituras.
6. Después de activar ambos selectores, ejecutar la CLI de mantenimiento `python -B -X utf8 herramientas/consulta_lorcana/consulta.py actualizar --json`.
7. Comprobar selección 2.3 y recuperación de 1.13, 6.1.4.2, 6.7.6.1, 8.1.2 y 8.16; verificar que 7.1.6.1 aparece ausente y que las notas 2.2 históricas no se ofrecen como evidencia activa. Las consultas posteriores deben seguir sin escribir cachés.

No cambiar configuración de conexión ni instalar dependencias para esta migración salvo necesidad técnica comprobada. La sustitución de fuente está soportada por el diseño actual.

## 9. Ejecución por fases y dependencias

| Fase | Acciones | Criterio de salida |
| --- | --- | --- |
| A. Preparación | Registrar Git y Publish; incorporar el original; extraer ambos PDF; comprobar símbolos y páginas; construir la matriz completa | Fuentes identificadas y diferencia trazable; selección vigente todavía 2.2 si es antes del 16/10 |
| B. Adaptación | Actualizar reglas/glosario; crear 1.13 y 8.16; revisar casos y resúmenes; redactar la entrada general | Cada diferencia confirmada tiene destino y decisión editorial; texto nuevo identificado temporalmente |
| C. Validación editorial | Revisar español, ejemplos, enlaces, citas, índices y avisos; separar deuda previa del delta | No hay afirmaciones incompatibles ni referencias rotas; cambios ajenos preservados |
| D. Preparación de publicación | Ampliar la herramienta selectiva; inventariar rutas de alta/actualización y retirada; probar sin subir | Manifiestos revisables, rutas permitidas y pruebas de selección/retirada correctas |
| E. Transición y subida | Documentar ambos periodos; verificar selección por fecha y lectura futura; mantener índice actual; commit y push | 2.2 antes del 16 y 2.3 desde el 16; commit propio confirmado en remoto |
| F. Publicación y retirada | Comprobar y publicar nuevas páginas/actualizaciones; verificar contenido; despublicar exclusivamente las antiguas seleccionadas | Sitio actualizado; retiradas comprobadas; ningún pendiente ajeno publicado |
| G. Cierre | Guardar informe, hashes, enlaces públicos y resultado de búsqueda | Trazabilidad completa o pendientes concretos declarados |

La instrucción posterior de Iván autoriza publicar la adaptación completa y retirar las páginas antiguas al terminar, antes del 16/10 si procede. Los avisos mantienen la distinción entre publicación y vigencia normativa. La selección futura está implementada y probada; un cliente MCP abierto con código anterior necesita reiniciarse para cargarla.

## 10. Publicación selectiva: adaptación necesaria

Se ha añadido `--perfil reglas` a `publicar.py`; el perfil predeterminado conserva su alcance. `retirar_reglas.py` implementa una operación independiente, limitada a las seis páginas históricas, que exige el reemplazo publicado. Ambas operaciones tienen pruebas de alcance, conservación y fallos.

La ejecución debe añadir un perfil o selección específica de migración, con pruebas, que permita las rutas documentadas de esta actualización. Mantener los controles existentes: commit subido, contenido idéntico al commit, bóveda correcta, exclusión de cambios ajenos y un `--archivo` por ruta. No ampliar implícitamente a toda la carpeta ni a todos los pendientes.

Preparar primero el manifiesto de publicación y ejecutar `--comprobar`; después `--aplicar` con el hash concreto y las mismas rutas. Publicar y verificar el reemplazo **antes** de retirar páginas antiguas.

Para retiradas, crear una operación específica con una lista exacta y un informe previo. Puede reutilizar los controles de `retirar_catalogo.py`, pero no usar esa herramienta directamente para reglas: está limitada a fichas del catálogo. La operación debe llamar a `publish:remove path=...` únicamente para las rutas 2.2 comprobadas, verificar cada retirada y conservar todo archivo local. Nunca utilizar publicación global, `publish:add changed` ni despublicación por patrón.

Los PDF fuente, configuraciones, scripts, informes internos y fichas largas de cartas quedan fuera de las altas en Publish. Los punteros internos no se publican por defecto; si ya tienen una página pública, decidir y registrar su actualización o retirada explícita para evitar referencias obsoletas.

Si una publicación falla parcialmente, detener las retiradas dependientes y conservar el informe de éxitos y pendientes. Si falla una retirada, registrar la ruta todavía pública. No afirmar que la migración pública terminó mientras quede publicada una referencia activa incompatible.

## 11. Validación y criterio de cierre

- [x] Portada, versión, fecha efectiva, idioma, páginas, URL y hash del PDF 2.3 comprobados.
- [x] Revisión completa de texto y comprobación visual de páginas con cambios, símbolos, tablas y diagramas; revisión global de las 56 páginas para detectar pérdidas de extracción.
- [x] Matriz cubre las 11 entradas principales, los 8 ajustes y las 7 entradas de glosario, además de bajas/traslados y diferencias no resumidas.
- [x] Incidencias anteriores del PDF 2.2 contrastadas con 2.3: no arrastrar correcciones o advertencias sin volver a verificarlas.
- [x] Localización coherente y sin mojibake; nuevas secciones enlazadas y traducciones propias identificadas.
- [x] Casos verificados, deduplicados e índices/tags sincronizados cuando cambien.
- [x] Nueva entrada distingue cambios de 2.3 y deuda previa; ejemplos y enlaces Lorcast comprobados.
- [x] Antes del 16/10 no se presenta 2.3 como vigente. Después de activar, ambos selectores y portada coinciden.
- [x] Referencias activas a 2.2 revisadas, históricos identificados y enlaces hacia páginas retiradas reparados.
- [x] MCP/búsqueda recuperan 2.3, excluyen históricos y conservan la lectura sin escrituras; pruebas relevantes de consulta/MCP y publicación selectiva pasan.
- [ ] Diff revisado y `git diff --check` correcto; commits solo de la migración; push confirmado sin forzar ni incorporar commits ajenos.
- [ ] Altas/actualizaciones públicas verificadas y retiradas exactas comprobadas; pendientes ajenos intactos.
- [ ] Informe final con commit(s), rutas, enlaces de la nueva entrada y pendientes reales, si los hubiera.

**Ejecución:** véase `cr-2.3-ejecucion.md` y los manifiestos explícitos. Los informes de Publish y retirada se guardarán tras sus operaciones; no se adelanta su confirmación.
