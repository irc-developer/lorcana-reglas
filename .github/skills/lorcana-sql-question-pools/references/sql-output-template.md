# Plantilla de salida SQL

Usa esta referencia como guía resumida y toma como plantilla estructural base [plantilla_pregunta.sql](../../../plantilla_pregunta.sql).

## Bloques obligatorios por pregunta

Cada pregunta nueva debe incluir estas tres capas:

1. `INSERT INTO "Preguntas"`
2. `INSERT INTO "OpcionesRespuesta"`
3. `INSERT INTO "PreguntaReglas"`

## Reglas de consistencia SQL

- usa siempre `WHERE NOT EXISTS`;
- usa el mismo `Texto` exacto de la pregunta en todos los subselects asociados;
- no generes `INSERT` de `ExamenPregunta` salvo petición expresa;
- no generes catálogos nuevos salvo instrucción explícita;
- mantén `ImagenUrl` e `ImagenDescripcion` en `NULL` salvo que el usuario pida imagen;
- usa `FechaModificacion = NULL` en alta inicial.

## Reglas mínimas por tabla

### `Preguntas`

- resolver `TipoPreguntaId`, `DificultadId` y `CategoriaId` con subconsultas por clave o nombre;
- deduplicar por `Preguntas.Texto`;
- alinear `Puntuacion` con la dificultad cuando el usuario no fije otro valor.

### `OpcionesRespuesta`

- deduplicar por `PreguntaId` + `Orden`;
- mantener `Orden` correlativo desde 1;
- `VERDADERO_FALSO`: dos opciones, `Verdadero` y `Falso`;
- `OPCION_UNICA`: normalmente 4 opciones;
- `MULTIPLE`: normalmente 4 o 5 opciones;
- `ORDENAR`: una opción por cada paso real de la secuencia.

### `PreguntaReglas`

- resolver `ReglaId` por `NumeroOficial` y `VersionReglamentoId`;
- deduplicar por `PreguntaId` + `ReglaId`;
- incluir al menos un vínculo principal;
- añadir una segunda regla solo cuando complemente de verdad la justificación;
- si el literal de `TipoVinculo` no está confirmado para el caso, preguntar antes de emitir SQL final ejecutable.

## Checklist previo a entregar

- `TipoPreguntaId` correcto;
- `DificultadId` correcta;
- `CategoriaId` correcta;
- `Puntuacion` alineada con dificultad;
- `ReferenciaRegla` suficiente y concisa;
- número de opciones coherente con el tipo;
- al menos un vínculo en `PreguntaReglas`.