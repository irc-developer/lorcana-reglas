---
name: lorcana-sql-question-pools
description: 'Genera pools de preguntas de examen de Disney Lorcana en seed SQL completo. Usar cuando el usuario pida crear un pool de preguntas, preguntas de examen, preguntas tipo test, seed SQL, convertir reglas o casos en preguntas, inserts para Preguntas/OpcionesRespuesta/PreguntaReglas o trabajo basado en plantilla_pregunta.sql.'
argument-hint: 'Indica fuente, cantidad, tema, categoría, dificultad, tipo de pregunta y si quieres SQL final o también borrador editorial.'
user-invocable: true
---

# Lorcana SQL Question Pools

## Cuándo usar

Usa esta skill cuando el usuario pida cualquiera de estos trabajos:

- Crear un pool de preguntas.
- Generar preguntas de examen de Lorcana.
- Redactar un seed SQL para Carde.io.
- Convertir reglas, artículos o casos en preguntas tipo test.
- Convertir artículos Markdown o escenarios concretos en preguntas evaluables.
- Producir bloques `INSERT INTO "Preguntas"`, `INSERT INTO "OpcionesRespuesta"` y `INSERT INTO "PreguntaReglas"`.

## Objetivo

Generar SQL listo para seed siguiendo la estructura completa de la plantilla del repositorio, no el formato antiguo reducido. Cada pregunta debe contemplar:

1. Registro en `Preguntas`.
2. Sus opciones en `OpcionesRespuesta`.
3. Sus vínculos normativos en `PreguntaReglas`.

La skill trabaja en tres fases: redacción de candidatas, validación editorial y conversión final a SQL. La referencia resumida del flujo está en [arquitectura de workflow](./references/workflow-architecture.md).

El objetivo no es solo poblar la base de datos. Cada pregunta debe servir también como ejemplo pedagógico reutilizable para futuros pools.

## Entradas esperadas

La entrada puede incluir uno o varios de estos elementos:

- uno o varios artículos de reglas en Markdown,
- casos de uso o escenarios concretos,
- cantidad,
- tema,
- categoría fija,
- dificultad fija,
- tipo de pregunta fijo.

Si el usuario no fija categoría, dificultad o tipo, debes inferirlos a partir del contenido y de la taxonomía ya verificada en este repositorio.

## Reglas operativas

1. Antes de escribir el SQL, identificar el alcance normativo exacto pedido por el usuario.
2. Si el pool es de reglas base, usar exclusivamente `01. Reglas` y `01.1.a Official English Reference – Unmodified`.
3. `01.1.a Official English Reference – Unmodified` es la autoridad normativa primaria; `01. Reglas` se usa para citación y redacción en castellano.
4. Si una pregunta depende del texto exacto de una carta, verificar ese texto en `02. Listado de Cartas/Cartas de Lorcana.md`.
5. No usar `02. Habilidades de las cartas_OLD`, `20. Reglas CR 1.X`, `Unifica`, compilaciones auxiliares ni ningún material fuera de las fuentes permitidas.
6. Si un dato no puede sostenerse con esas fuentes, detenerse y pedir precisión al usuario antes de generar el seed.
7. Si la petición es ambigua, preguntar lo mínimo imprescindible antes de generar el seed.
8. Mantener el texto en español, con ortografía normalizada y explicaciones breves pero suficientes.
9. No inventar categorías, claves o literales de catálogo si no están confirmados en el repo o por el usuario.
10. Si falta el literal exacto de `PreguntaReglas.TipoVinculo`, detenerse y preguntar antes de emitir SQL final ejecutable.

## Taxonomía verificada en este repositorio

### Categorías permitidas

- `Reglas Basicas`
- `Mecanicas de Juego`
- `Cartas y Personajes`
- `Torneos y Competitivo`

### Dificultades permitidas

- `FACIL`
- `MEDIA`
- `DIFICIL`
- `EXPERTO`

### Tipos de pregunta permitidos

- `OPCION_UNICA`
- `VERDADERO_FALSO`
- `ORDENAR`
- `MULTIPLE`

## Valores por defecto ya verificados

- `VersionesReglamento.Codigo` por defecto para seeds manuales de reglas de Lorcana: `2.1.0`.
- `Activa`: `1`, salvo que el usuario pida otra cosa.
- `Puntuacion`: por defecto `FACIL -> 1`, `MEDIA -> 2`, `DIFICIL -> 3`, `EXPERTO -> 4`, salvo instrucción distinta.
- `FechaModificacion`: `NULL` en alta inicial.
- `ImagenUrl` e `ImagenDescripcion`: `NULL` salvo material proporcionado.

## Heurística de calibración de dificultad

Usa estas reglas prácticas salvo que la fuente o el caso concreto justifiquen otra cosa:

- `FACIL`: concepto base, keyword aislada, definición operativa simple o regla directa sin interacción relevante extra.
- `MEDIA`: aplicación de una regla con una confusión común, una restricción adicional o una interacción sencilla de timing o legalidad.
- `DIFICIL`: cruce de varias reglas, varias restricciones simultáneas o secuencias donde el error habitual exige analizar más de un punto normativo.
- `EXPERTO`: lectura profunda de sistema, procesos internos como GSC o interacciones poco intuitivas propias de arbitraje avanzado.

Regla práctica importante:

- una pregunta sobre una keyword por sí sola normalmente debe ser `FACIL`;
- no subas la dificultad solo porque la keyword sea conocida por jueces o porque el nombre suene técnico;
- sube a `MEDIA` o más solo si la pregunta obliga a aplicar esa keyword junto con timing, objetivos, restricciones o varias reglas a la vez.

## Procedimiento

1. Leer la petición y extraer cantidad, tema, dificultad, categoría y fuente.
2. Si falta alguno de esos datos y afecta al resultado, preguntar lo mínimo.
3. Redactar primero el contenido editorial de cada pregunta.
4. Validar cada candidata con el contrato intermedio y con las reglas de calidad antes de tocar el SQL.
5. Vincular cada pregunta con al menos una regla principal y, si aporta valor, una secundaria.
6. Convertir todo al formato SQL completo descrito en [referencia editorial](./references/editorial-guidelines.md) y en la [plantilla SQL](./references/sql-output-template.md).
7. Entregar el resultado en bloques SQL listos para pegar o guardar.

## Contrato intermedio recomendado

Antes de generar SQL, cada pregunta debe existir en una forma intermedia con estos campos:

- `Texto`
- `Tipo`
- `Categoria`
- `Dificultad`
- `Puntuacion`
- `ReferenciaRegla`
- `Explicacion`
- `NotaPedagogica`
- `Opciones` con `Orden`, `Texto` y `EsCorrecta`

No conviertas a SQL una pregunta que no pueda expresarse limpiamente con ese contrato.

## Validaciones obligatorias

Antes de devolver una pregunta, verifica todo esto:

- no duplica semánticamente una pregunta ya existente en el lote;
- la categoría es coherente con lo que realmente evalúa la pregunta;
- la dificultad es coherente con la complejidad real;
- la explicación resuelve la duda central;
- la referencia existe y es suficiente;
- la pregunta tiene valor pedagógico como ejemplo futuro.

### Validaciones por tipo

#### `OPCION_UNICA`

- debe haber entre 3 y 5 opciones;
- exactamente una opción correcta;
- los distractores deben ser plausibles.

#### `VERDADERO_FALSO`

- exactamente dos opciones: `Verdadero` y `Falso`;
- exactamente una correcta;
- la dificultad debe venir de la regla, no del lenguaje.

#### `MULTIPLE`

- al menos 4 opciones cuando sea razonable;
- dos o más opciones correctas solo si la pregunta realmente lo necesita;
- no convertir la pregunta en una suma de minipreguntas inconexas.

#### `ORDENAR`

- las opciones deben representar pasos o hitos reales de una secuencia;
- el orden debe ser objetivamente defendible desde la fuente;
- la explicación debe resumir la lógica de la secuencia.

## Criterios editoriales mínimos

- Las preguntas deben ser comprobables con reglas, no opiniones.
- La explicación debe justificar por qué la opción correcta lo es y por qué el matiz importa.
- La `ReferenciaRegla` debe ser corta, útil y consistente con la explicación.
- Evitar distractores absurdos; los incorrectos deben sonar plausibles.
- En `VERDADERO_FALSO`, las opciones deben ser `Verdadero` y `Falso` salvo instrucción en contra.
- En `ORDENAR`, cada opción representa un paso real de la secuencia.

Prefiere preguntas que:

- enfrenten una confusión frecuente entre jugadores o jueces,
- distingan entre permiso, obligación y restricción,
- midan timing, legalidad, secuencia o resultado de una interacción,
- obliguen a aplicar la regla y no solo a recitarla,
- sirvan como ejemplos sólidos de referencia para futuros lotes.

Evita:

- reformular la misma idea demasiadas veces,
- distractores absurdos,
- referencias innecesariamente largas,
- preguntas que dependan de información no dada o no verificable.

## Salida esperada

Por defecto, devolver SQL completo para el pool pedido con `Preguntas`, `OpcionesRespuesta` y `PreguntaReglas`.

Si el usuario pide solo borrador editorial, puedes detenerte antes del SQL.

Si el usuario además pide contexto editorial, preceder el SQL con un resumen breve de:

- tema cubierto,
- distribución de dificultad,
- criterios normativos usados,
- dudas abiertas si alguna impide cerrar el seed.

## Referencias

- [Guía editorial](./references/editorial-guidelines.md)
- [Arquitectura de workflow](./references/workflow-architecture.md)
- [Plantilla SQL](./references/sql-output-template.md)
