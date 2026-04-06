# Guía editorial para pools SQL de preguntas de Lorcana

## Fuente estructural obligatoria

La salida debe seguir la estructura completa de la plantilla SQL del repositorio. Cada pregunta incluye tres capas:

1. `Preguntas`
2. `OpcionesRespuesta`
3. `PreguntaReglas`

No usar el formato antiguo de solo `Preguntas` + `OpcionesRespuesta` cuando el usuario pida un seed nuevo basado en la plantilla vigente.

## Estructura mínima por pregunta

### 1. Cabecera editorial

Mantener comentarios equivalentes a:

- título interno o resumen,
- tipo,
- dificultad,
- categoría,
- referencia editorial,
- regla principal sugerida.

### 2. Insert en Preguntas

Campos obligatorios:

- `Texto`
- `TipoPreguntaId`
- `DificultadId`
- `CategoriaId`
- `Explicacion`
- `ReferenciaRegla`
- `ImagenUrl`
- `ImagenDescripcion`
- `Activa`
- `Puntuacion`
- `FechaCreacion`
- `FechaModificacion`

Patrones obligatorios:

- Resolver ids con subconsultas por clave o nombre.
- Proteger duplicados con `WHERE NOT EXISTS` por `Preguntas.Texto`.
- En altas iniciales usar `FechaModificacion = NULL`.

## 3. Inserts en OpcionesRespuesta

Reglas:

- Cada opción se inserta con `PreguntaId` resuelto por el `Texto` exacto.
- Cada opción usa su propio `WHERE NOT EXISTS` por `PreguntaId` + `Orden`.
- `Orden` debe ser correlativo desde 1.
- `Explicacion` de opción puede ir en `NULL` si no aporta valor.

Recuento orientativo:

- `VERDADERO_FALSO`: 2 opciones.
- `OPCION_UNICA`: normalmente 4 opciones.
- `MULTIPLE`: normalmente 4 o 5 opciones.
- `ORDENAR`: una opción por cada paso de la secuencia.

## 4. Inserts en PreguntaReglas

Reglas:

- Cada vínculo debe resolver `ReglaId` por `NumeroOficial` y `VersionReglamentoId`.
- `VersionReglamentoId` debe resolverse por `VersionesReglamento.Codigo`.
- Código por defecto ya verificado para seed manual de reglas: `2.1.0`.
- Proteger duplicados con `WHERE NOT EXISTS` por `PreguntaId` + `ReglaId`.

Convención editorial:

- Incluir al menos una regla principal.
- Incluir segunda regla cuando realmente complemente la justificación.
- `Prioridad` debe reflejar qué regla sostiene el núcleo de la respuesta.

## Dato no cerrado todavía

El literal exacto permitido por base de datos para `PreguntaReglas.TipoVinculo` no está documentado en este repositorio.

Por tanto:

- Si el usuario no lo proporciona y no aparece definido en el repo, preguntar antes de emitir SQL final ejecutable.
- Si se trabaja solo en borrador editorial, se pueden dejar placeholders temporales, pero no en la entrega final que deba ejecutarse.

## Criterios de redacción

- Redactar en español claro y preciso.
- Evitar preguntas que dependan de interpretación subjetiva.
- Los distractores deben representar errores reales de comprensión.
- La explicación de la pregunta debe resolver el concepto, no repetir solo la respuesta correcta.
- La dificultad debe guardar relación con la interacción real, no con lo conocida que sea la keyword.

## Convenciones recomendadas de puntuación

- `FACIL`: 1
- `MEDIA`: 2
- `DIFICIL`: 3

## Checklist final antes de entregar un pool

- Cada pregunta tiene `INSERT INTO "Preguntas"`.
- Cada pregunta tiene todas sus opciones.
- Cada pregunta tiene al menos un vínculo en `PreguntaReglas`.
- No se han inventado claves de catálogo.
- `VersionesReglamento.Codigo` es `2.1.0` salvo instrucción distinta.
- El literal de `TipoVinculo` está confirmado.
- Todas las cláusulas `WHERE NOT EXISTS` usan la misma clave de deduplicación que la plantilla.
