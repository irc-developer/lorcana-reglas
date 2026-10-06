---
name: lorcana-ruling-workflow
description: "Resuelve y documenta una duda de Disney Lorcana, valida artículos e índices, sube el commit y publica solo los archivos de esa duda en Obsidian Publish antes de responder."
argument-hint: "Describe la duda o interacción de Lorcana que debe resolverse y documentarse."
user-invocable: true
---

# Workflow unificado de rulings de Lorcana

## Contrato

Un ruling, su artículo, los índices afectados, la fecha visible de `Empecemos.md`, el commit y `push` y la publicación de esos archivos en Obsidian Publish forman una sola transacción editorial. La tarea no está terminada si solo existe una respuesta de chat, si los cambios documentados siguen únicamente en local o si falta su publicación en el sitio.

El usuario ha autorizado crear y subir ese commit y publicar en Obsidian cada duda documentada con cambios, tanto con `documenta:` como con una pregunta ordinaria que active este workflow. La publicación solo puede subir o actualizar los archivos documentados en esa transacción; no otros pendientes de la bóveda. No solicites otra confirmación para esos pasos; una instrucción posterior del usuario de no subir o publicar cambios prevalece. `consulta:` sigue siendo solo lectura: no crea commits, hace `push` ni publica.

Solo se permite omitir las ediciones cuando el usuario pide explícitamente no modificar el repositorio o cuando una comprobación demuestra que editar es técnicamente imposible. La incertidumbre normativa, la falta de activación automática de otra instrucción o una ubicación incómoda no son bloqueos.

## Fuentes y guías de apoyo

- Reglas primarias: PDF inglés seleccionado por `Documentacion Oficial/README.md` y `01.1.a Official English Reference – Unmodified/00. Fuente actual.md`. Los Markdown ingleses numerados son transcripciones históricas incompletas y no sustituyen el PDF seleccionado.
- Localización y documentación en castellano: `01. Reglas/`.
- Texto exacto de cartas: archivo de set correspondiente dentro de `02. Listado de Cartas/`.
- Artículos: `01. Reglas/11. Casos de ejemplo y aclaraciones/`.
- Índice manual principal: `01. Reglas/11. Casos de ejemplo y aclaraciones/ÍNDICE - Casos de ejemplo y aclaraciones.md`.
- Plantilla vigente: `01. Reglas/11. Casos de ejemplo y aclaraciones/Plantilla - Caso de ejemplo y aclaración.md`.

Aplica directamente, cuando corresponda, las guías reutilizables de [alcance](../../instructions/lorcana-scope.instructions.md), [aclaración](../../instructions/lorcana-question-clarification.instructions.md), [verificación de cartas](../../instructions/lorcana-card-verification.instructions.md), [deduplicación](../../instructions/lorcana-case-dedup.instructions.md), [formato de casos](../../instructions/lorcana-case-writing.instructions.md), [tags](../../instructions/lorcana-case-tags.instructions.md), [enlaces Obsidian](../../instructions/lorcana-obsidian-links.instructions.md) e [higiene Markdown](../../instructions/lorcana-file-hygiene.instructions.md). Estas guías afinan pasos concretos; ninguna sustituye este flujo.

## Flujo obligatorio y ordenado

1. **Determinar la pregunta exacta y el estado inicial.** Reconstruye cartas, versiones, estado de mesa, elecciones y secuencia. Registra el estado de Git antes de editar y conserva una lista explícita de los archivos de esta duda. Si un dato crítico admite resultados distintos, pide solo la aclaración mínima antes de continuar.
2. **Identificar y priorizar fuentes oficiales.** Busca primero la referencia inglesa oficial sin modificar y después la localización castellana equivalente. Los casos existentes sirven para localizar o comparar, nunca para prevalecer sobre la regla primaria.
3. **Verificar el texto de cartas cuando sea relevante.** Confirma nombre, versión y texto completo en el archivo de set de `02. Listado de Cartas/`. No uses carpetas legacy ni inventes texto ausente.
4. **Producir el ruling técnico.** Determina veredicto, fundamento, orden de eventos, disparos, bolsa y GSC aplicables. Conserva las referencias exactas que sostienen cada conclusión.
5. **Buscar artículos duplicados o solapados.** Busca en toda la sección 11 por nombres de cartas, mecánicas, conceptos, tags y conclusión normativa; revisa la subcarpeta probable y el índice manual.
6. **Decidir crear o actualizar.** Actualiza el artículo canónico si ya cubre la misma interacción o concepto. Crea uno nuevo solo cuando la diferencia conceptual sea material. Si varios se solapan, elige el mejor canónico, integra allí lo útil y evita otro duplicado.
7. **Escribir el artículo completo.** Ubícalo en la subcarpeta 11.* adecuada y sigue la plantilla vigente y la guía de escritura. La duda documentada debe contener los hechos ya confirmados y la respuesta debe coincidir con el ruling técnico. La comprobación de fuentes es completa, pero el artículo presenta solo la respuesta, su explicación y referencias suficientes. No vuelques el relato de investigación, verificaciones fechadas, capturas ni incidencias técnicas. Añade ejemplos o una secuencia solo cuando aporten algo distinto.
8. **Aplicar estructura y calidad editorial.** Revisa nombre de archivo, título si lo usa, frontmatter y metadatos según la convención vigente, headings, ejemplos, tags, enlaces de cartas y reglas, fuentes oficiales, ortografía, gramática, UTF-8 y formato. Elimina repeticiones y pasos genéricos sin perder condiciones críticas, excepciones ni advertencias materiales. Integra ampliaciones y deja los tags al final. Actualmente la plantilla de casos no usa frontmatter: valida su ausencia y no inventes campos.
9. **Actualizar todos los índices afectados.** Para cada índice manual, añade, corrige o elimina el enlace exacto; conserva el orden; renumera; actualiza contadores de subsección, total, estadísticas, búsquedas temáticas y fecha del índice cuando existan. Compara las entradas con los archivos reales.
10. **Actualizar `Empecemos.md`.** Si el artículo se creó o cambió materialmente, sustituye la fecha visible por la fecha real del entorno usando el formato existente `*Última actualización dd/mm/aa*`. Si ya coincide, no hagas un cambio artificial. No cambies la fecha en tareas sin modificación material de un artículo de ruling.
11. **Validar la transacción completa.** Inspecciona el diff y comprueba: artículo frente al ruling; plantilla/frontmatter; tags y registro maestro; destinos de enlaces; fuentes citadas; presencia única en índices; contadores; fecha del índice; fecha de `Empecemos.md`; Markdown/YAML; y ausencia de cambios ajenos. Ejecuta los validadores existentes si los hay.
12. **Crear el commit y subirlo al remoto.** Tras validar, revisa el estado de Git y el remoto configurado de la rama. Incluye solo los archivos y cambios de esta transacción editorial; conserva cambios previos ajenos y no los añadas al commit. Crea un commit con un mensaje descriptivo de la duda y haz `push` a la rama remota correspondiente del repositorio. Comprueba que el remoto contiene el commit. No uses `push --force` ni publiques commits previos ajenos sin autorización. Si la rama no tiene un destino remoto inequívoco, la autenticación falla o hay un rechazo/conflicto, conserva el trabajo local, registra el error concreto y declara la publicación pendiente; no afirmes que se completó.
13. **Publicar solo esta duda en Obsidian Publish.** Usa la [herramienta de publicación selectiva](../../../herramientas/publicar_obsidian/README.md) con el hash del commit subido y un `--archivo` por ruta de la lista de esta transacción. Incluye solo los artículos y los índices, portada o registro de tags que realmente cambiaron para esta duda y que formen parte de ese commit. No publiques configuraciones, herramientas, fuentes consultadas ni otros pendientes; tampoco amplíes la selección por enlaces o por el estado global de Publish. Si un archivo comparte cambios previos ajenos, aísla el contenido de la duda antes de publicarlo; subir el archivo completo también expondría esos cambios. Primero prepara y revisa el plan y usa `--comprobar`; después ejecuta `--aplicar`. La herramienta comprueba el commit, los contenidos y la bóveda y llama a `publish:add path=...` por cada ruta. Nunca uses `publish:add changed`, publicación global, borrados ni sincronización masiva. Comprueba que las rutas seleccionadas no siguen pendientes y abre el enlace público de cada artículo para verificar el contenido. Si falla, conserva el commit y el informe parcial e indica las rutas publicadas y las pendientes; no lo presentes como publicación completa.
14. **Preparar la respuesta final.** Solo después de editar, validar, subir el commit y publicar la selección, responde con el ruling breve, su secuencia o fundamento necesario, la ruta de cada artículo creado o actualizado, el enlace o hash del commit subido y el enlace público de los artículos. Para un artículo verificado sin cambios, devuelve su ruta sin fabricar un commit vacío ni publicar pendientes antiguos. Si existe un bloqueo verificado, indica exactamente qué paso quedó pendiente.

## Excepciones

### Petición explícita de mantener el trabajo en local

Si el usuario pide no crear commits, no subir a Git o no publicar, completa las ediciones y validaciones autorizadas y conserva la selección de archivos para retomarla. Omite los pasos restringidos y deja constancia de lo pendiente; la instrucción sigue vigente hasta que el usuario la cambie. No interpretes esa restricción como una petición de no editar. En la respuesta final informa del resultado local sin fabricar un hash ni un enlace publicado.

### Petición explícita de no editar

Resuelve con las mejores fuentes disponibles, no modifiques archivos e indica brevemente que se omitió la documentación porque el usuario lo pidió expresamente.

### Bloqueo técnico verificado

Intenta y registra una comprobación concreta del impedimento. Aun así ofrece el mejor ruling sustentado posible e identifica exactamente el bloqueo y qué artículo, índice, fecha, commit, `push` o publicación en Obsidian no pudo completarse. Si el commit existe, conserva e informa su hash para reanudar los pasos pendientes; si Publish falló parcialmente, conserva también la selección y el informe de rutas. No afirmes que la transacción se completó.

## Criterio de cierre

No cierres mientras artículo, índices y fecha estén desincronizados o los cambios de esta transacción sigan sin commit, `push` y publicación selectiva en Obsidian, salvo instrucción posterior del usuario o bloqueo técnico verificado. Si el artículo existente ya era completo y correcto y la transacción no requiere ningún cambio, no lo edites artificialmente, crees un commit vacío ni publiques otros pendientes: devuelve su ruta y deja constancia interna de que se verificaron duplicado, índice y fecha.
