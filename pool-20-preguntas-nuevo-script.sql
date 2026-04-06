PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

-- =========================================================
-- PREGUNTA: Mano inicial de cada jugador
-- =========================================================
-- Tipo: OPCION_UNICA
-- Dificultad: FACIL
-- Categoria: Reglas Basicas
-- Referencia editorial: CR 2.2.1.4
-- Regla principal sugerida: 2.2.1.4
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Reglas Basicas'),
    'Durante la etapa de preparación, cada jugador roba 7 cartas. Esas 7 cartas forman su mano inicial.',
    'CR 2.2.1.4',
    NULL,
    NULL,
    1,
    1,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?'), '5 cartas', 0, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?'), '6 cartas', 0, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?'), '7 cartas', 1, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?'), '8 cartas', 0, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT
    (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?'),
    105,
    'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?') AND "ReglaId" = 105);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT
    (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?'),
    424,
    'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuántas cartas forman la mano inicial de cada jugador al empezar una partida?') AND "ReglaId" = 424);

-- =========================================================
-- PREGUNTA: Alterar la mano solo una vez
-- =========================================================
-- Tipo: VERDADERO_FALSO
-- Dificultad: MEDIA
-- Categoria: Reglas Basicas
-- Referencia editorial: CR 2.2.2
-- Regla principal sugerida: 2.2.2
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Cada jugador puede alterar su mano inicial como máximo una vez por partida.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Reglas Basicas'),
    'La etapa de preparación permite modificar la mano inicial una sola vez por partida. Después, quien lo haya hecho debe barajar de nuevo y ofrecer corte o barajado al oponente.',
    'CR 2.2.2',
    NULL,
    NULL,
    1,
    2,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Cada jugador puede alterar su mano inicial como máximo una vez por partida.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Cada jugador puede alterar su mano inicial como máximo una vez por partida.'), 'Verdadero', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Cada jugador puede alterar su mano inicial como máximo una vez por partida.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Cada jugador puede alterar su mano inicial como máximo una vez por partida.'), 'Falso', 0, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Cada jugador puede alterar su mano inicial como máximo una vez por partida.') AND "Orden" = 2);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Cada jugador puede alterar su mano inicial como máximo una vez por partida.'),
    106,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Cada jugador puede alterar su mano inicial como máximo una vez por partida.') AND "ReglaId" = 106);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Cada jugador puede alterar su mano inicial como máximo una vez por partida.'),
    109,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Cada jugador puede alterar su mano inicial como máximo una vez por partida.') AND "ReglaId" = 109);

-- =========================================================
-- PREGUNTA: Orden básico del setup
-- =========================================================
-- Tipo: ORDENAR
-- Dificultad: FACIL
-- Categoria: Reglas Basicas
-- Referencia editorial: CR 2.2.1.1-2.2.1.4
-- Regla principal sugerida: 2.2.1.1
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'ORDENAR'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Reglas Basicas'),
    'Primero se decide el jugador inicial, después se barajan los mazos, luego ambos jugadores empiezan con 0 de lore y finalmente roban 7 cartas para la mano inicial.',
    'CR 2.2.1.1-2.2.1.4',
    NULL,
    NULL,
    1,
    1,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.'), 'Escoger al jugador inicial', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.'), 'Barajar los mazos', 1, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.'), 'Empezar la partida con 0 de lore', 1, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.'), 'Robar 7 cartas', 1, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.'),
    102,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.') AND "ReglaId" = 102);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.'),
    105,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena los pasos básicos de la etapa de preparación antes de alterar la mano inicial.') AND "ReglaId" = 105);

-- =========================================================
-- PREGUNTA: Poner en la mano no es robar
-- =========================================================
-- Tipo: OPCION_UNICA
-- Dificultad: FACIL
-- Categoria: Reglas Basicas
-- Referencia editorial: CR 1.12.3
-- Regla principal sugerida: 1.12.3
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Reglas Basicas'),
    'Poner una carta en la mano no cuenta como robar. Aunque el movimiento físico se parezca, las reglas distinguen ambos conceptos.',
    'CR 1.12.3',
    NULL,
    NULL,
    1,
    1,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?'), 'Cuenta como robar si la carta viene del mazo.', 0, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?'), 'No cuenta como robar aunque el movimiento físico se parezca.', 1, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?'), 'Solo cuenta como robar en el turno del jugador activo.', 0, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?'), 'Cuenta como robar salvo que la carta ya estuviera revelada.', 0, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?'),
    93,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?') AND "ReglaId" = 93);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?'),
    91,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "poner una carta en tu mano", ¿qué es correcto según las reglas?') AND "ReglaId" = 91);

-- =========================================================
-- PREGUNTA: Robos múltiples son individuales
-- =========================================================
-- Tipo: VERDADERO_FALSO
-- Dificultad: FACIL
-- Categoria: Reglas Basicas
-- Referencia editorial: CR 1.12.2
-- Regla principal sugerida: 1.12.2
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Si un efecto te hace robar tres cartas, esas cartas se roban de una en una.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Reglas Basicas'),
    'Las reglas indican que los robos múltiples no forman un único robo masivo. Se resuelven una tras otra, carta por carta.',
    'CR 1.12.2',
    NULL,
    NULL,
    1,
    1,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Si un efecto te hace robar tres cartas, esas cartas se roban de una en una.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto te hace robar tres cartas, esas cartas se roban de una en una.'), 'Verdadero', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto te hace robar tres cartas, esas cartas se roban de una en una.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto te hace robar tres cartas, esas cartas se roban de una en una.'), 'Falso', 0, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto te hace robar tres cartas, esas cartas se roban de una en una.') AND "Orden" = 2);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto te hace robar tres cartas, esas cartas se roban de una en una.'),
    92,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto te hace robar tres cartas, esas cartas se roban de una en una.') AND "ReglaId" = 92);

-- =========================================================
-- PREGUNTA: El jugador inicial no roba en el primer turno
-- =========================================================
-- Tipo: VERDADERO_FALSO
-- Dificultad: FACIL
-- Categoria: Reglas Basicas
-- Referencia editorial: CR 3.2.3.1
-- Regla principal sugerida: 3.2.3.1
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'En el primer turno de la partida, el jugador inicial se salta el paso de robar.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Reglas Basicas'),
    'La regla del paso de robar establece una excepción para el primer turno: el starting player no roba carta en ese paso.',
    'CR 3.2.3.1',
    NULL,
    NULL,
    1,
    1,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'En el primer turno de la partida, el jugador inicial se salta el paso de robar.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'En el primer turno de la partida, el jugador inicial se salta el paso de robar.'), 'Verdadero', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'En el primer turno de la partida, el jugador inicial se salta el paso de robar.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'En el primer turno de la partida, el jugador inicial se salta el paso de robar.'), 'Falso', 0, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'En el primer turno de la partida, el jugador inicial se salta el paso de robar.') AND "Orden" = 2);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'En el primer turno de la partida, el jugador inicial se salta el paso de robar.'),
    140,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'En el primer turno de la partida, el jugador inicial se salta el paso de robar.') AND "ReglaId" = 140);

-- =========================================================
-- PREGUNTA: Solo habilidades disparadas van a la bolsa
-- =========================================================
-- Tipo: OPCION_UNICA
-- Dificultad: FACIL
-- Categoria: Mecanicas de Juego
-- Referencia editorial: CR 7.7.2
-- Regla principal sugerida: 7.7.2
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    '¿Qué puede añadirse a la bolsa según las reglas?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Mecanicas de Juego'),
    'La bolsa solo contiene habilidades disparadas. Las habilidades activadas, las cartas en resolución y el hecho de jugar ciertos tipos de carta no se añaden a ella.',
    'CR 7.7.2',
    NULL,
    NULL,
    1,
    1,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?'), 'Solo habilidades disparadas', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?'), 'Habilidades activadas y disparadas por igual', 0, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?'), 'Cualquier efecto que esté pendiente de terminar', 0, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?'), 'Todas las cartas que acaban de jugarse', 0, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?'),
    447,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?') AND "ReglaId" = 447);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?'),
    446,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué puede añadirse a la bolsa según las reglas?') AND "ReglaId" = 446);

-- =========================================================
-- PREGUNTA: Trigger durante otra resolución
-- =========================================================
-- Tipo: VERDADERO_FALSO
-- Dificultad: MEDIA
-- Categoria: Mecanicas de Juego
-- Referencia editorial: CR 7.7.3.1
-- Regla principal sugerida: 7.7.3.1
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Si una habilidad disparada se dispara mientras otro efecto se está resolviendo, espera a que ese efecto termine antes de resolverse.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Mecanicas de Juego'),
    'La habilidad se añade a la bolsa en cuanto se cumple su condición, pero no interrumpe la resolución actual. Se resuelve cuando el efecto en curso ha terminado por completo.',
    'CR 7.7.3.1',
    NULL,
    NULL,
    1,
    2,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Si una habilidad disparada se dispara mientras otro efecto se está resolviendo, espera a que ese efecto termine antes de resolverse.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si una habilidad disparada se dispara mientras otro efecto se está resolviendo, espera a que ese efecto termine antes de resolverse.'), 'Verdadero', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si una habilidad disparada se dispara mientras otro efecto se está resolviendo, espera a que ese efecto termine antes de resolverse.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si una habilidad disparada se dispara mientras otro efecto se está resolviendo, espera a que ese efecto termine antes de resolverse.'), 'Falso', 0, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si una habilidad disparada se dispara mientras otro efecto se está resolviendo, espera a que ese efecto termine antes de resolverse.') AND "Orden" = 2);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si una habilidad disparada se dispara mientras otro efecto se está resolviendo, espera a que ese efecto termine antes de resolverse.'),
    449,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si una habilidad disparada se dispara mientras otro efecto se está resolviendo, espera a que ese efecto termine antes de resolverse.') AND "ReglaId" = 449);

-- =========================================================
-- PREGUNTA: Resolución de la bolsa
-- =========================================================
-- Tipo: MULTIPLE
-- Dificultad: DIFICIL
-- Categoria: Mecanicas de Juego
-- Referencia editorial: CR 7.7.4-7.7.6
-- Regla principal sugerida: 7.7.4.2
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'MULTIPLE'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'DIFICIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Mecanicas de Juego'),
    'Si el jugador activo tiene habilidades en la bolsa, elige una de las suyas y la resuelve. Si quien resolvió el último efecto sigue teniendo habilidades pendientes, continúa con las suyas. Las nuevas habilidades del jugador no activo esperan a que la bolsa pase y, cuando la bolsa se vacía, la partida continúa con el jugador activo.',
    'CR 7.7.4-7.7.6',
    NULL,
    NULL,
    1,
    3,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.'), 'Si el jugador activo tiene habilidades en la bolsa, elige una de las suyas y la resuelve por completo.', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.'), 'Si el jugador que resolvió el último efecto aún tiene habilidades en la bolsa, sigue resolviendo las suyas antes de pasarla.', 1, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.'), 'Las habilidades activadas pendientes entran en la bolsa junto con las disparadas.', 0, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.'), 'Si una nueva habilidad la añade el jugador no activo mientras otro jugador resuelve, espera a que llegue su turno de resolver efectos desde la bolsa.', 1, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.') AND "Orden" = 4);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.'), 'Cuando la bolsa queda vacía, la partida continúa con el jugador activo.', 1, 5, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.') AND "Orden" = 5);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.'),
    452,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.') AND "ReglaId" = 452);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.'),
    457,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre la resolución de la bolsa.') AND "ReglaId" = 457);

-- =========================================================
-- PREGUNTA: Perder por mazo vacío al final del turno
-- =========================================================
-- Tipo: OPCION_UNICA
-- Dificultad: MEDIA
-- Categoria: Mecanicas de Juego
-- Referencia editorial: CR 1.8.1.2
-- Regla principal sugerida: 1.8.1.2
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Mecanicas de Juego'),
    'Según este reglamento del repositorio, la condición se comprueba cuando un jugador termina su turno sin cartas en el deck. No se formula como una derrota inmediata al mero hecho de intentar robar.',
    'CR 1.8.1.2',
    NULL,
    NULL,
    1,
    2,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?'), 'En cuanto intenta robar una carta y no puede.', 0, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?'), 'Cuando termina su turno sin cartas en el deck.', 1, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?'), 'Solo cuando ambos jugadores se quedan sin mazo a la vez.', 0, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?'), 'Únicamente al comienzo de su siguiente turno.', 0, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?'),
    65,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo pierde la partida un jugador por mazo vacío según el game state check de este reglamento?') AND "ReglaId" = 65);

-- =========================================================
-- PREGUNTA: Triggers del GSC no se resuelven en mitad del chequeo
-- =========================================================
-- Tipo: VERDADERO_FALSO
-- Dificultad: MEDIA
-- Categoria: Mecanicas de Juego
-- Referencia editorial: CR 1.8.2-1.8.3
-- Regla principal sugerida: 1.8.2
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Las habilidades disparadas provocadas por un game state check se resuelven antes de que terminen todas las comprobaciones del propio game state check.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Mecanicas de Juego'),
    'Las habilidades disparadas creadas por el GSC se colocan en la bolsa, pero no se resuelven hasta que las comprobaciones han terminado. Si todavía hay condiciones que cumplir, el juego sigue evaluándolas antes de pasar a la bolsa.',
    'CR 1.8.2-1.8.3',
    NULL,
    NULL,
    1,
    2,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Las habilidades disparadas provocadas por un game state check se resuelven antes de que terminen todas las comprobaciones del propio game state check.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las habilidades disparadas provocadas por un game state check se resuelven antes de que terminen todas las comprobaciones del propio game state check.'), 'Verdadero', 0, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las habilidades disparadas provocadas por un game state check se resuelven antes de que terminen todas las comprobaciones del propio game state check.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las habilidades disparadas provocadas por un game state check se resuelven antes de que terminen todas las comprobaciones del propio game state check.'), 'Falso', 1, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las habilidades disparadas provocadas por un game state check se resuelven antes de que terminen todas las comprobaciones del propio game state check.') AND "Orden" = 2);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las habilidades disparadas provocadas por un game state check se resuelven antes de que terminen todas las comprobaciones del propio game state check.'),
    68,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las habilidades disparadas provocadas por un game state check se resuelven antes de que terminen todas las comprobaciones del propio game state check.') AND "ReglaId" = 68);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las habilidades disparadas provocadas por un game state check se resuelven antes de que terminen todas las comprobaciones del propio game state check.'),
    69,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las habilidades disparadas provocadas por un game state check se resuelven antes de que terminen todas las comprobaciones del propio game state check.') AND "ReglaId" = 69);

-- =========================================================
-- PREGUNTA: Bodyguard tiene dos componentes
-- =========================================================
-- Tipo: MULTIPLE
-- Dificultad: MEDIA
-- Categoria: Cartas y Personajes
-- Referencia editorial: CR 8.3.2-8.3.3
-- Regla principal sugerida: 8.3.2
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Selecciona las afirmaciones correctas sobre Bodyguard.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'MULTIPLE'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Bodyguard representa dos habilidades: una permite entrar en juego agotado en lugar de preparado y otra crea una restricción de desafío que obliga al oponente a elegir un personaje con Bodyguard si puede.',
    'CR 8.3.2-8.3.3',
    NULL,
    NULL,
    1,
    2,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.'), 'Un personaje con Bodyguard puede entrar en juego agotado en lugar de preparado.', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.'), 'Si un oponente va a elegir uno de tus personajes para desafiar, debe elegir uno con Bodyguard si es posible.', 1, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.'), 'Bodyguard obliga a que ese personaje desafíe cada turno si puede.', 0, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.'), 'Bodyguard concede Evasive mientras el personaje está preparado.', 0, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.'),
    468,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.') AND "ReglaId" = 468);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.'),
    469,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre Bodyguard.') AND "ReglaId" = 469);

-- =========================================================
-- PREGUNTA: Challenger solo al desafiar
-- =========================================================
-- Tipo: VERDADERO_FALSO
-- Dificultad: FACIL
-- Categoria: Cartas y Personajes
-- Referencia editorial: CR 8.5.1-8.5.2
-- Regla principal sugerida: 8.5.2
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Un personaje con Challenger +N obtiene ese bono también cuando está siendo desafiado.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Challenger +N solo funciona mientras el personaje está desafiando. Si está siendo desafiado, no recibe ese bono.',
    'CR 8.5.1-8.5.2',
    NULL,
    NULL,
    1,
    1,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Un personaje con Challenger +N obtiene ese bono también cuando está siendo desafiado.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje con Challenger +N obtiene ese bono también cuando está siendo desafiado.'), 'Verdadero', 0, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje con Challenger +N obtiene ese bono también cuando está siendo desafiado.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje con Challenger +N obtiene ese bono también cuando está siendo desafiado.'), 'Falso', 1, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje con Challenger +N obtiene ese bono también cuando está siendo desafiado.') AND "Orden" = 2);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje con Challenger +N obtiene ese bono también cuando está siendo desafiado.'),
    476,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje con Challenger +N obtiene ese bono también cuando está siendo desafiado.') AND "ReglaId" = 476);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje con Challenger +N obtiene ese bono también cuando está siendo desafiado.'),
    475,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje con Challenger +N obtiene ese bono también cuando está siendo desafiado.') AND "ReglaId" = 475);

-- =========================================================
-- PREGUNTA: Reckless y acciones permitidas
-- =========================================================
-- Tipo: OPCION_UNICA
-- Dificultad: FACIL
-- Categoria: Cartas y Personajes
-- Referencia editorial: CR 8.7.2-8.7.4
-- Regla principal sugerida: 8.7.4
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Reckless impide questear y restringe cómo terminas el turno si el personaje puede desafiar, pero no impide agotarlo para usar habilidades o cantar canciones.',
    'CR 8.7.2-8.7.4',
    NULL,
    NULL,
    1,
    1,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?'), 'Hacer quest normalmente si aún no ha sido exerted.', 0, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?'), 'Agotarse para usar una habilidad o para cantar una canción.', 1, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?'), 'Ignorar todos los desafíos legales si el jugador lo desea.', 0, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?'), 'Ganar Rush hasta fin de turno por defecto.', 0, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?'),
    483,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?') AND "ReglaId" = 483);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?'),
    481,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué sigue pudiendo hacer un personaje con Reckless si es legal hacerlo?') AND "ReglaId" = 481);

-- =========================================================
-- PREGUNTA: Resist no afecta a daño puesto o movido
-- =========================================================
-- Tipo: OPCION_UNICA
-- Dificultad: MEDIA
-- Categoria: Cartas y Personajes
-- Referencia editorial: CR 8.8.3
-- Regla principal sugerida: 8.8.3
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Resist reduce daño que fuera a infligirse, pero no modifica daño que se pone o se mueve sobre la carta por otros efectos.',
    'CR 8.8.3',
    NULL,
    NULL,
    1,
    2,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?'), 'Resist reduce tanto el daño infligido como el daño que se pone o se mueve.', 0, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?'), 'Resist no afecta al daño puesto o movido sobre la carta.', 1, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?'), 'Resist convierte el daño movido en daño infligido si el origen era un personaje.', 0, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?'), 'Resist solo funciona contra daño de desafío, no contra otras fuentes.', 0, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?'),
    487,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?') AND "ReglaId" = 487);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?'),
    485,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a Resist frente al daño puesto o movido?') AND "ReglaId" = 485);

-- =========================================================
-- PREGUNTA: Resist a cero no es daño infligido
-- =========================================================
-- Tipo: VERDADERO_FALSO
-- Dificultad: MEDIA
-- Categoria: Cartas y Personajes
-- Referencia editorial: CR 8.8.2
-- Regla principal sugerida: 8.8.2
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Si Resist reduce el daño a 0, no se considera que se haya infligido daño alguno.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'La regla específica de Resist aclara que cuando el daño queda reducido a 0, el juego no considera que se haya infligido daño.',
    'CR 8.8.2',
    NULL,
    NULL,
    1,
    2,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Si Resist reduce el daño a 0, no se considera que se haya infligido daño alguno.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si Resist reduce el daño a 0, no se considera que se haya infligido daño alguno.'), 'Verdadero', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si Resist reduce el daño a 0, no se considera que se haya infligido daño alguno.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si Resist reduce el daño a 0, no se considera que se haya infligido daño alguno.'), 'Falso', 0, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si Resist reduce el daño a 0, no se considera que se haya infligido daño alguno.') AND "Orden" = 2);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si Resist reduce el daño a 0, no se considera que se haya infligido daño alguno.'),
    486,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si Resist reduce el daño a 0, no se considera que se haya infligido daño alguno.') AND "ReglaId" = 486);

-- =========================================================
-- PREGUNTA: Rush permite desafiar, no questear
-- =========================================================
-- Tipo: OPCION_UNICA
-- Dificultad: FACIL
-- Categoria: Cartas y Personajes
-- Referencia editorial: CR 8.9.1
-- Regla principal sugerida: 8.9.1
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    '¿Qué permite exactamente Rush el turno en que se juega el personaje?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Rush permite desafiar como si el personaje hubiera estado en juego desde el comienzo de tu turno. No otorga permiso para questear antes de secarse.',
    'CR 8.9.1',
    NULL,
    NULL,
    1,
    1,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?'), 'Questear inmediatamente como si el personaje ya estuviera seco.', 0, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?'), 'Desafiar como si hubiera estado en juego desde el comienzo de tu turno.', 1, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?'), 'Entrar preparado aunque otro efecto dijera lo contrario.', 0, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?'), 'Usar cualquier habilidad activada aunque su coste incluya exert y el personaje siga secándose.', 0, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?'),
    489,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?') AND "ReglaId" = 489);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?'),
    136,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite exactamente Rush el turno en que se juega el personaje?') AND "ReglaId" = 136);

-- =========================================================
-- PREGUNTA: Notas permitidas en partida
-- =========================================================
-- Tipo: MULTIPLE
-- Dificultad: MEDIA
-- Categoria: Torneos y Competitivo
-- Referencia editorial: TR 5.2
-- Regla principal sugerida: 5.2
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'MULTIPLE'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Torneos y Competitivo'),
    'Se permite llevar registro escrito de los totales de lore, pero no otras notas durante la partida. Los tokens pueden usarse para información pública propia, aunque no para números salvo el daño. Además, no se permite tomar ni mirar notas durante Draft o Limited Deck Construction.',
    'TR 5.2',
    NULL,
    NULL,
    1,
    2,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.'), 'Se permite llevar por escrito los totales de lore.', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.'), 'Se pueden tomar otras notas estratégicas durante la partida si ambos jugadores están de acuerdo.', 0, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.'), 'Los tokens pueden usarse para seguir información pública propia, pero no se permiten números en ellos salvo para el daño.', 1, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.'), 'No se permite tomar ni mirar notas durante el Drafting o la Limited Deck Construction.', 1, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.'),
    256,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre notas y seguimiento de información durante un torneo.') AND "ReglaId" = 256);

-- =========================================================
-- PREGUNTA: Emparejamientos en Competitive Draft
-- =========================================================
-- Tipo: OPCION_UNICA
-- Dificultad: MEDIA
-- Categoria: Torneos y Competitivo
-- Referencia editorial: TR 6.4.1
-- Regla principal sugerida: 6.4.1
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Torneos y Competitivo'),
    'En Casual Draft los jugadores pueden emparejarse con cualquier jugador del torneo. En Competitive Draft deben emparejarse solo con jugadores de su propio pod.',
    'TR 6.4.1',
    NULL,
    NULL,
    1,
    2,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?'), 'En Competitive Draft los jugadores deben emparejarse únicamente contra jugadores de su propio pod.', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?'), 'En Competitive Draft los jugadores deben cambiar de pod cada ronda.', 0, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?') AND "Orden" = 2);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?'), 'En Casual Draft los jugadores solo pueden jugar contra personas de su mismo pod.', 0, 3, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?') AND "Orden" = 3);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?'), 'No existe diferencia de emparejamientos entre ambos.', 0, 4, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?') AND "Orden" = 4);

INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?'),
    362,
       'principal', 1, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?') AND "ReglaId" = 362);
INSERT INTO "PreguntaReglas" ("PreguntaId", "ReglaId", "TipoVinculo", "Prioridad", "Notas", "FechaCreacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?'),
    361,
       'secundaria', 2, NULL, '2026-03-28T16:00:00Z'
WHERE NOT EXISTS (SELECT 1 FROM "PreguntaReglas" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué regla de emparejamiento distingue a un Competitive Draft de un Casual Draft?') AND "ReglaId" = 361);

-- =========================================================
-- PREGUNTA: Dropear en Limitado y conservar cartas
-- =========================================================
-- Tipo: VERDADERO_FALSO
-- Dificultad: FACIL
-- Categoria: Torneos y Competitivo
-- Referencia editorial: TR 3.9
-- Regla principal sugerida: 3.9
-- =========================================================

INSERT INTO "Preguntas"
(
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion",
    "FechaCreacion", "FechaModificacion"
)
SELECT
    'Si un jugador se retira durante un torneo Limitado, conserva las cartas que le proporcionó el organizador para ese evento.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Torneos y Competitivo'),
    'La regla de retirada en torneo lo dice expresamente para eventos Limitados: el jugador conserva las cartas proporcionadas, incluidos sobres abiertos y sobres parcialmente drafteados.',
    'TR 3.9',
    NULL,
    NULL,
    1,
    1,
    '2026-03-28T16:00:00Z',
    NULL
WHERE NOT EXISTS
(
    SELECT 1 FROM "Preguntas"
    WHERE "Texto" = 'Si un jugador se retira durante un torneo Limitado, conserva las cartas que le proporcionó el organizador para ese evento.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un jugador se retira durante un torneo Limitado, conserva las cartas que le proporcionó el organizador para ese evento.'), 'Verdadero', 1, 1, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un jugador se retira durante un torneo Limitado, conserva las cartas que le proporcionó el organizador para ese evento.') AND "Orden" = 1);
INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un jugador se retira durante un torneo Limitado, conserva las cartas que le proporcionó el organizador para ese evento.'), 'Falso', 0, 2, NULL
WHERE NOT EXISTS (SELECT 1 FROM "OpcionesRespuesta" WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un jugador se retira durante un torneo Limitado, conserva las cartas que le proporcionó el organizador para ese evento.') AND "Orden" = 2);


COMMIT;