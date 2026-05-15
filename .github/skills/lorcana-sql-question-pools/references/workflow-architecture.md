# Arquitectura de workflow

Esta skill sigue un workflow de tres fases y concentra la autoridad del repositorio para seeds de preguntas de Lorcana.

## Fase 1: Redacción

Objetivo:

- convertir reglas, artículos o casos en candidatas de alta calidad,
- producir preguntas que ya tengan valor pedagógico antes del SQL.

Salida esperada:

- `Texto`
- `Tipo`
- `Categoria`
- `Dificultad`
- `Puntuacion`
- `ReferenciaRegla`
- `Explicacion`
- `NotaPedagogica`
- `Opciones` con `Orden`, `Texto` y `EsCorrecta`

La salida de esta fase no debe contener SQL.

## Fase 2: Validación

Objetivo:

- filtrar ambigüedades, errores de regla, mala calibración de dificultad y distractores débiles,
- impedir que llegue a SQL una pregunta mediocre o defectuosa.

Posibles veredictos:

- `APROBADA`
- `CORREGIR`
- `RECHAZAR`

Una pregunta solo puede pasar a SQL si queda `APROBADA`.

## Fase 3: Conversión a SQL

Objetivo:

- transformar candidatas aprobadas en `INSERT` idempotentes de `Preguntas`, `OpcionesRespuesta` y `PreguntaReglas`.

Restricciones:

- no generar `ExamenPregunta`;
- no crear catálogos nuevos;
- no alterar la taxonomía fija del repo.

## Contrato mínimo entre fases

El contrato mínimo es este:

- `Texto`
- `Tipo`
- `Categoria`
- `Dificultad`
- `Puntuacion`
- `ReferenciaRegla`
- `Explicacion`
- `NotaPedagogica`
- `Opciones` con `Orden`, `Texto` y `EsCorrecta`

Si falta alguno de estos campos, la candidata no está lista para validación final ni para SQL.

## Regla de oro

La conversión a SQL no corrige una pregunta mala.
Si la pregunta no es clara, pedagógica, precisa y defendible antes del SQL, debe volver a redacción o quedar rechazada.