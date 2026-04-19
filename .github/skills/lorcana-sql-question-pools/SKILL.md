---
name: lorcana-sql-question-pools
description: 'Genera pools de preguntas de examen de Disney Lorcana en seed SQL completo. Usar cuando el usuario pida crear un pool de preguntas, preguntas de examen, preguntas tipo test, seed SQL, inserts para Preguntas/OpcionesRespuesta/PreguntaReglas o trabajo basado en plantilla_pregunta.sql.'
argument-hint: 'Indica cantidad, tema, dificultad, categoria, alcance normativo y si quieres solo SQL o tambien resumen editorial.'
user-invocable: true
---

# Lorcana SQL Question Pools

## Cuándo usar

Usa esta skill cuando el usuario pida cualquiera de estos trabajos:

- Crear un pool de preguntas.
- Generar preguntas de examen de Lorcana.
- Redactar un seed SQL para Carde.io.
- Convertir reglas, artículos o casos en preguntas tipo test.
- Producir bloques `INSERT INTO "Preguntas"`, `INSERT INTO "OpcionesRespuesta"` y `INSERT INTO "PreguntaReglas"`.

## Objetivo

Generar SQL listo para seed siguiendo la estructura completa de la plantilla del repositorio, no el formato antiguo reducido. Cada pregunta debe contemplar:

1. Registro en `Preguntas`.
2. Sus opciones en `OpcionesRespuesta`.
3. Sus vínculos normativos en `PreguntaReglas`.

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

## Valores por defecto ya verificados

- `VersionesReglamento.Codigo` por defecto para seeds manuales de reglas de Lorcana: `2.1.0`.
- `Activa`: `1`, salvo que el usuario pida otra cosa.
- `Puntuacion`: ajustar a dificultad, salvo instrucción distinta.
- `FechaModificacion`: `NULL` en alta inicial.
- `ImagenUrl` e `ImagenDescripcion`: `NULL` salvo material proporcionado.

## Procedimiento

1. Leer la petición y extraer cantidad, tema, dificultad, categoría y fuente.
2. Si falta alguno de esos datos y afecta al resultado, preguntar lo mínimo.
3. Redactar primero el contenido editorial de cada pregunta.
4. Validar que cada pregunta tenga una respuesta correcta inequívoca o un conjunto correcto bien definido.
5. Vincular cada pregunta con al menos una regla principal y, si aporta valor, una secundaria.
6. Convertir todo al formato SQL completo descrito en [referencia editorial](./references/editorial-guidelines.md).
7. Entregar el resultado en bloques SQL listos para pegar o guardar.

## Criterios editoriales mínimos

- Las preguntas deben ser comprobables con reglas, no opiniones.
- La explicación debe justificar por qué la opción correcta lo es y por qué el matiz importa.
- La `ReferenciaRegla` debe ser corta, útil y consistente con la explicación.
- Evitar distractores absurdos; los incorrectos deben sonar plausibles.
- En `VERDADERO_FALSO`, las opciones deben ser `Verdadero` y `Falso` salvo instrucción en contra.
- En `ORDENAR`, cada opción representa un paso real de la secuencia.

## Salida esperada

Por defecto, devolver SQL completo para el pool pedido.

Si el usuario además pide contexto editorial, preceder el SQL con un resumen breve de:

- tema cubierto,
- distribución de dificultad,
- criterios normativos usados,
- dudas abiertas si alguna impide cerrar el seed.

## Referencias

- [Guía editorial](./references/editorial-guidelines.md)
