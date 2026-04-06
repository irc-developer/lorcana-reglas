PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

-- =========================================================
-- PREGUNTA: {{TITULO_INTERNO_O_RESUMEN}}
-- =========================================================
-- Tipo: {{TIPO_PREGUNTA_CLAVE}}
-- Dificultad: {{DIFICULTAD_CLAVE}}
-- Categoria: {{CATEGORIA_NOMBRE}}
-- Referencia editorial: {{REFERENCIA_REGLA}}
-- Regla principal sugerida: {{REGLA_PRINCIPAL_NUMERO}}
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto",
    "TipoPreguntaId",
    "DificultadId",
    "CategoriaId",
    "Explicacion",
    "ReferenciaRegla",
    "ImagenUrl",
    "ImagenDescripcion",
    "Activa",
    "Puntuacion",
    "FechaCreacion",
    "FechaModificacion"
)
SELECT
    '{{TEXTO_PREGUNTA}}',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = '{{TIPO_PREGUNTA_CLAVE}}'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = '{{DIFICULTAD_CLAVE}}'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = '{{CATEGORIA_NOMBRE}}'),
    '{{EXPLICACION_PREGUNTA}}',
    '{{REFERENCIA_REGLA}}',
    {{IMAGEN_URL_O_NULL}},
    {{IMAGEN_DESCRIPCION_O_NULL}},
    {{ACTIVA_BOOL}},
    {{PUNTUACION_INT}},
    '{{FECHA_CREACION_ISO_UTC}}',
    NULL
WHERE NOT EXISTS
(
    SELECT 1
    FROM "Preguntas"
    WHERE "Texto" = '{{TEXTO_PREGUNTA}}'
);

-- ---------- OPCIONES ----------
-- Repetir una vez por opción

INSERT INTO "OpcionesRespuesta"
(
    "PreguntaId",
    "Texto",
    "EsCorrecta",
    "Orden",
    "Explicacion"
)
SELECT
    (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}'),
    '{{OPCION_1_TEXTO}}',
    {{OPCION_1_ES_CORRECTA_BOOL}},
    1,
    {{OPCION_1_EXPLICACION_O_NULL}}
WHERE NOT EXISTS
(
    SELECT 1
    FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta"
(
    "PreguntaId",
    "Texto",
    "EsCorrecta",
    "Orden",
    "Explicacion"
)
SELECT
    (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}'),
    '{{OPCION_2_TEXTO}}',
    {{OPCION_2_ES_CORRECTA_BOOL}},
    2,
    {{OPCION_2_EXPLICACION_O_NULL}}
WHERE NOT EXISTS
(
    SELECT 1
    FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta"
(
    "PreguntaId",
    "Texto",
    "EsCorrecta",
    "Orden",
    "Explicacion"
)
SELECT
    (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}'),
    '{{OPCION_3_TEXTO}}',
    {{OPCION_3_ES_CORRECTA_BOOL}},
    3,
    {{OPCION_3_EXPLICACION_O_NULL}}
WHERE NOT EXISTS
(
    SELECT 1
    FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta"
(
    "PreguntaId",
    "Texto",
    "EsCorrecta",
    "Orden",
    "Explicacion"
)
SELECT
    (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}'),
    '{{OPCION_4_TEXTO}}',
    {{OPCION_4_ES_CORRECTA_BOOL}},
    4,
    {{OPCION_4_EXPLICACION_O_NULL}}
WHERE NOT EXISTS
(
    SELECT 1
    FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}')
      AND "Orden" = 4
);

-- Si aplica, añadir opción 5 del mismo modo.

-- ---------- REGLAS RELACIONADAS ----------
-- Repetir una vez por vínculo

INSERT INTO "PreguntaReglas"
(
    "PreguntaId",
    "ReglaId",
    "TipoVinculo",
    "Prioridad",
    "Notas",
    "FechaCreacion"
)
SELECT
    (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}'),
    (
        SELECT "Id"
        FROM "Reglas"
        WHERE "NumeroOficial" = '{{REGLA_1_NUMERO_OFICIAL}}'
          AND "VersionReglamentoId" =
          (
              SELECT "Id"
              FROM "VersionesReglamento"
              WHERE "Codigo" = '{{REGLA_1_VERSION_CODIGO}}'
          )
    ),
    '{{REGLA_1_TIPO_VINCULO}}',
    {{REGLA_1_PRIORIDAD}},
    {{REGLA_1_NOTAS_O_NULL}},
    '{{REGLA_1_FECHA_CREACION_ISO_UTC}}'
WHERE NOT EXISTS
(
    SELECT 1
    FROM "PreguntaReglas"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}')
      AND "ReglaId" =
      (
          SELECT "Id"
          FROM "Reglas"
          WHERE "NumeroOficial" = '{{REGLA_1_NUMERO_OFICIAL}}'
            AND "VersionReglamentoId" =
            (
                SELECT "Id"
                FROM "VersionesReglamento"
                WHERE "Codigo" = '{{REGLA_1_VERSION_CODIGO}}'
            )
      )
);

INSERT INTO "PreguntaReglas"
(
    "PreguntaId",
    "ReglaId",
    "TipoVinculo",
    "Prioridad",
    "Notas",
    "FechaCreacion"
)
SELECT
    (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}'),
    (
        SELECT "Id"
        FROM "Reglas"
        WHERE "NumeroOficial" = '{{REGLA_2_NUMERO_OFICIAL}}'
          AND "VersionReglamentoId" =
          (
              SELECT "Id"
              FROM "VersionesReglamento"
              WHERE "Codigo" = '{{REGLA_2_VERSION_CODIGO}}'
          )
    ),
    '{{REGLA_2_TIPO_VINCULO}}',
    {{REGLA_2_PRIORIDAD}},
    {{REGLA_2_NOTAS_O_NULL}},
    '{{REGLA_2_FECHA_CREACION_ISO_UTC}}'
WHERE NOT EXISTS
(
    SELECT 1
    FROM "PreguntaReglas"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '{{TEXTO_PREGUNTA}}')
      AND "ReglaId" =
      (
          SELECT "Id"
          FROM "Reglas"
          WHERE "NumeroOficial" = '{{REGLA_2_NUMERO_OFICIAL}}'
            AND "VersionReglamentoId" =
            (
                SELECT "Id"
                FROM "VersionesReglamento"
                WHERE "Codigo" = '{{REGLA_2_VERSION_CODIGO}}'
            )
      )
);

COMMIT;