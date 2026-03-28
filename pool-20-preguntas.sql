INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Selecciona las afirmaciones correctas sobre costes y costes alternativos.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'MULTIPLE'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Reglas Basicas'),
    'Cantar, Shift y jugar una carta gratis son formas de coste alternativo. Los modificadores de pago cambian lo que pagas, pero no el coste impreso de la carta.',
    'CR 1.5.4-1.5.5', NULL, NULL, 1, 2, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre costes y costes alternativos.'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    '¿Qué ocurre si un efecto pone una carta de otra zona en tu inkwell?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Reglas Basicas'),
    'Si un efecto pone una carta en el inkwell, entra boca abajo como tinta y no necesita símbolo de inkwell. Tampoco se revela.',
    'CR 7.5.6', NULL, NULL, 1, 1, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = '¿Qué ocurre si un efecto pone una carta de otra zona en tu inkwell?'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    '¿Qué necesita una carta para ser un personaje según las reglas?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Reglas Basicas'),
    'Para ser un personaje, una carta debe tener Fuerza, Voluntad y al menos una clasificación válida de personaje. Si falta cualquiera de esos elementos, no es un personaje.',
    'CR 5.3.3', NULL, NULL, 1, 1, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = '¿Qué necesita una carta para ser un personaje según las reglas?'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Ordena las fases básicas de un turno de Lorcana.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'ORDENAR'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Reglas Basicas'),
    'El turno avanza de fase inicial a fase principal y después a fase final de turno.',
    'CR 3.1-3.4', NULL, NULL, 1, 1, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Ordena las fases básicas de un turno de Lorcana.'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Un personaje que no está seco puede usar una habilidad activada si el coste no incluye exert.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Mecanicas de Juego'),
    'La restricción de estar seco solo aplica a habilidades activadas de personaje cuyo coste incluya exert. Si el coste no incluye exert, la habilidad puede usarse ese mismo turno.',
    'CR 6.3.1.1', NULL, NULL, 1, 2, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Un personaje que no está seco puede usar una habilidad activada si el coste no incluye exert.'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Singer cambia el coste de tinta impreso del personaje mientras canta una canción.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Singer solo permite pagar un coste alternativo para una Song como si el personaje tuviera coste N al cantar. El coste de tinta impreso del personaje no cambia.',
    'Keywords: Singer', NULL, NULL, 1, 1, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Singer cambia el coste de tinta impreso del personaje mientras canta una canción.'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    '¿Qué hace realmente Support cuando el personaje hace quest?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Support es una habilidad disparada que, al hacer quest, permite añadir la Fuerza de ese personaje a otro personaje elegido durante ese turno.',
    'Keywords: Support', NULL, NULL, 1, 1, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = '¿Qué hace realmente Support cuando el personaje hace quest?'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    '¿Qué permite Alert frente a un personaje con Evasive?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Alert permite ignorar la restricción de desafío creada por Evasive. No concede Evasive ni modifica otras restricciones.',
    'Keywords: Alert / Keywords: Evasive', NULL, NULL, 1, 2, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = '¿Qué permite Alert frente a un personaje con Evasive?'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Ward impide que los efectos del oponente afecten de cualquier forma a esa carta.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Ward solo impide que un oponente elija esa carta al resolver un efecto. Los efectos que no requieren elección pueden seguir afectándola.',
    'Keywords: Ward', NULL, NULL, 1, 2, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Ward impide que los efectos del oponente afecten de cualquier forma a esa carta.'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Selecciona las afirmaciones correctas sobre habilidades y efectos.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'MULTIPLE'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'DIFICIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Mecanicas de Juego'),
    'Las acciones tienen efectos, no habilidades. Una habilidad puede tener varios efectos dentro de una misma resolución y las elecciones se hacen al resolver, siguiendo el orden escrito.',
    'CR 6.1.1-6.1.3 / CR 5.4.3', NULL, NULL, 1, 3, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre habilidades y efectos.'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Si un efecto dice "hasta 2 personajes elegidos reciben -1 {S} este turno", ¿qué es correcto?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Mecanicas de Juego'),
    'En un efecto con hasta N objetivos, elegir 0 es válido y no puedes elegir el mismo objetivo más de una vez dentro de esa misma elección.',
    'CR 6.1.3', NULL, NULL, 1, 2, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "hasta 2 personajes elegidos reciben -1 {S} este turno", ¿qué es correcto?'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    '¿Cuándo se resuelve una habilidad disparada que se genera al activar una habilidad activada?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'DIFICIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Mecanicas de Juego'),
    'Las habilidades disparadas creadas al activar una habilidad se añaden a la bolsa, pero esperan a que la habilidad activada termine de resolverse por completo.',
    'CR 6.3.3', NULL, NULL, 1, 3, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = '¿Cuándo se resuelve una habilidad disparada que se genera al activar una habilidad activada?'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Las cartas de acción tienen efectos, no habilidades.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'VERDADERO_FALSO'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Las acciones generan efectos cuando se resuelven, pero no se consideran cartas con habilidades.',
    'CR 5.4.3', NULL, NULL, 1, 1, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Las cartas de acción tienen efectos, no habilidades.'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Ordena la resolución básica de una acción según el resumen de reglas.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'ORDENAR'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Según el resumen, al jugar una acción primero se resuelve su efecto, después la carta entra temporalmente en juego y luego va al descarte.',
    'CR 5.4.1.2', NULL, NULL, 1, 2, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Ordena la resolución básica de una acción según el resumen de reglas.'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    '¿Qué afirmación describe correctamente a las localizaciones cuando entran en juego?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'Si una localización tiene una habilidad, puede usarse en el mismo turno en que la localización se juega.',
    'CR 5.6.4', NULL, NULL, 1, 1, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a las localizaciones cuando entran en juego?'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    '¿Cuándo se destierra una localización por daño?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Cartas y Personajes'),
    'El daño en una localización es persistente y la localización se destierra durante un Game State Check si ese daño es igual o mayor que su Voluntad.',
    'CR 5.6.5.2', NULL, NULL, 1, 2, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = '¿Cuándo se destierra una localización por daño?'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Selecciona las afirmaciones correctas sobre mazos Constructed.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'MULTIPLE'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Torneos y Competitivo'),
    'En Constructed el mazo debe tener al menos 60 cartas, no más de dos colores de tinta y un máximo de cuatro copias de una misma carta. No hay tamaño máximo si el jugador puede barajarlo con normalidad.',
    'TR 5.1', NULL, NULL, 1, 2, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    '¿Cuál es el mínimo de sobres por jugador en un torneo Sellado?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'FACIL'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Torneos y Competitivo'),
    'En Sellado cada jugador recibe como mínimo seis sobres para construir su mazo.',
    'TR 6.2', NULL, NULL, 1, 1, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = '¿Cuál es el mínimo de sobres por jugador en un torneo Sellado?'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    '¿Qué describe correctamente la construcción de mazos en Limited?',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'OPCION_UNICA'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Torneos y Competitivo'),
    'En Limited los mazos de Sealed y Draft tienen un mínimo de 40 cartas, no están restringidos por tipos de tinta y pueden llevar cualquier número de copias desde el pool abierto.',
    'TR 6.1', NULL, NULL, 1, 2, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = '¿Qué describe correctamente la construcción de mazos en Limited?'
);

INSERT INTO "Preguntas" (
    "Texto", "TipoPreguntaId", "DificultadId", "CategoriaId", "Explicacion",
    "ReferenciaRegla", "ImagenUrl", "ImagenDescripcion", "Activa", "Puntuacion", "FechaCreacion"
)
SELECT
    'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.',
    (SELECT "Id" FROM "TipoPreguntas" WHERE "Clave" = 'MULTIPLE'),
    (SELECT "Id" FROM "Dificultades" WHERE "Clave" = 'MEDIA'),
    (SELECT "Id" FROM "Categorias" WHERE "Nombre" = 'Torneos y Competitivo'),
    'Un jugador puede conceder una partida incompleta en cualquier momento. Los pactos de resultado están permitidos dentro de sus límites, pero no se puede ofrecer nada a cambio ni pedir una concesión al oponente.',
    'TR 3.6', NULL, NULL, 1, 2, '2026-03-27T00:00:00Z'
WHERE NOT EXISTS (
    SELECT 1 FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.'
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre costes y costes alternativos.'), 'Cantar una Song es un coste alternativo.', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre costes y costes alternativos.')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre costes y costes alternativos.'), 'Shift es un coste alternativo.', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre costes y costes alternativos.')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre costes y costes alternativos.'), 'Un modificador de pago cambia el coste impreso de la carta.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre costes y costes alternativos.')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre costes y costes alternativos.'), 'Jugar una carta gratis es un coste alternativo.', 1, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre costes y costes alternativos.')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué ocurre si un efecto pone una carta de otra zona en tu inkwell?'), 'Debe revelarse y tener símbolo de inkwell.', 0, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué ocurre si un efecto pone una carta de otra zona en tu inkwell?')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué ocurre si un efecto pone una carta de otra zona en tu inkwell?'), 'Entra boca abajo y no necesita símbolo de inkwell.', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué ocurre si un efecto pone una carta de otra zona en tu inkwell?')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué ocurre si un efecto pone una carta de otra zona en tu inkwell?'), 'Solo entra si procede de la mano.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué ocurre si un efecto pone una carta de otra zona en tu inkwell?')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué ocurre si un efecto pone una carta de otra zona en tu inkwell?'), 'Solo entra si ya era una carta de tinta.', 0, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué ocurre si un efecto pone una carta de otra zona en tu inkwell?')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué necesita una carta para ser un personaje según las reglas?'), 'Tener Fuerza, Voluntad y al menos una clasificación válida de personaje.', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué necesita una carta para ser un personaje según las reglas?')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué necesita una carta para ser un personaje según las reglas?'), 'Mostrar la palabra Character en su línea de clasificaciones.', 0, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué necesita una carta para ser un personaje según las reglas?')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué necesita una carta para ser un personaje según las reglas?'), 'Tener Voluntad y ser una Song o un Item.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué necesita una carta para ser un personaje según las reglas?')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué necesita una carta para ser un personaje según las reglas?'), 'Tener una versión y un valor de lore, aunque no tenga Fuerza.', 0, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué necesita una carta para ser un personaje según las reglas?')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena las fases básicas de un turno de Lorcana.'), 'Fase inicial del turno', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena las fases básicas de un turno de Lorcana.')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena las fases básicas de un turno de Lorcana.'), 'Fase principal', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena las fases básicas de un turno de Lorcana.')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena las fases básicas de un turno de Lorcana.'), 'Fase final de turno', 1, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena las fases básicas de un turno de Lorcana.')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje que no está seco puede usar una habilidad activada si el coste no incluye exert.'), 'Verdadero', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje que no está seco puede usar una habilidad activada si el coste no incluye exert.')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje que no está seco puede usar una habilidad activada si el coste no incluye exert.'), 'Falso', 0, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Un personaje que no está seco puede usar una habilidad activada si el coste no incluye exert.')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Singer cambia el coste de tinta impreso del personaje mientras canta una canción.'), 'Verdadero', 0, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Singer cambia el coste de tinta impreso del personaje mientras canta una canción.')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Singer cambia el coste de tinta impreso del personaje mientras canta una canción.'), 'Falso', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Singer cambia el coste de tinta impreso del personaje mientras canta una canción.')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué hace realmente Support cuando el personaje hace quest?'), 'Añade la Fuerza de ese personaje a otro personaje elegido este turno.', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué hace realmente Support cuando el personaje hace quest?')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué hace realmente Support cuando el personaje hace quest?'), 'Da lore adicional al propio personaje que hace quest.', 0, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué hace realmente Support cuando el personaje hace quest?')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué hace realmente Support cuando el personaje hace quest?'), 'Ready a otro personaje y le da Rush hasta fin de turno.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué hace realmente Support cuando el personaje hace quest?')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué hace realmente Support cuando el personaje hace quest?'), 'Añade su Fuerza a un personaje oponente elegido.', 0, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué hace realmente Support cuando el personaje hace quest?')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite Alert frente a un personaje con Evasive?'), 'Permite desafiarlo aunque el atacante no tenga Evasive.', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite Alert frente a un personaje con Evasive?')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite Alert frente a un personaje con Evasive?'), 'Concede Evasive al personaje que tiene Alert.', 0, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite Alert frente a un personaje con Evasive?')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite Alert frente a un personaje con Evasive?'), 'Hace que Ward deje de proteger a ese personaje.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite Alert frente a un personaje con Evasive?')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite Alert frente a un personaje con Evasive?'), 'Solo funciona si ambos personajes ya están exerted.', 0, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué permite Alert frente a un personaje con Evasive?')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ward impide que los efectos del oponente afecten de cualquier forma a esa carta.'), 'Verdadero', 0, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ward impide que los efectos del oponente afecten de cualquier forma a esa carta.')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ward impide que los efectos del oponente afecten de cualquier forma a esa carta.'), 'Falso', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ward impide que los efectos del oponente afecten de cualquier forma a esa carta.')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre habilidades y efectos.'), 'Una acción no tiene habilidades; tiene efectos.', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre habilidades y efectos.')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre habilidades y efectos.'), 'Una habilidad con varias frases puede seguir siendo una única resolución.', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre habilidades y efectos.')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre habilidades y efectos.'), 'Todas las elecciones se hacen antes de anunciar la carta o habilidad.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre habilidades y efectos.')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre habilidades y efectos.'), 'Los efectos se resuelven en el orden en que están escritos.', 1, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre habilidades y efectos.')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "hasta 2 personajes elegidos reciben -1 {S} este turno", ¿qué es correcto?'), 'Puedes elegir 0 personajes y no puedes elegir el mismo personaje dos veces.', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "hasta 2 personajes elegidos reciben -1 {S} este turno", ¿qué es correcto?')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "hasta 2 personajes elegidos reciben -1 {S} este turno", ¿qué es correcto?'), 'Debes elegir exactamente 2 personajes si hay 2 legales.', 0, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "hasta 2 personajes elegidos reciben -1 {S} este turno", ¿qué es correcto?')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "hasta 2 personajes elegidos reciben -1 {S} este turno", ¿qué es correcto?'), 'Puedes elegir el mismo personaje dos veces para aplicar ambos -1 {S}.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "hasta 2 personajes elegidos reciben -1 {S} este turno", ¿qué es correcto?')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "hasta 2 personajes elegidos reciben -1 {S} este turno", ¿qué es correcto?'), 'Las elecciones de hasta 2 siempre se hacen al anunciar el efecto, no al resolverlo.', 0, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Si un efecto dice "hasta 2 personajes elegidos reciben -1 {S} este turno", ¿qué es correcto?')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se resuelve una habilidad disparada que se genera al activar una habilidad activada?'), 'En cuanto pagas el coste de la habilidad activada.', 0, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se resuelve una habilidad disparada que se genera al activar una habilidad activada?')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se resuelve una habilidad disparada que se genera al activar una habilidad activada?'), 'Después de que la habilidad activada se resuelva por completo.', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se resuelve una habilidad disparada que se genera al activar una habilidad activada?')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se resuelve una habilidad disparada que se genera al activar una habilidad activada?'), 'Solo al final del turno, durante la fase final.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se resuelve una habilidad disparada que se genera al activar una habilidad activada?')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se resuelve una habilidad disparada que se genera al activar una habilidad activada?'), 'Se pierde si fue creada durante el pago del coste.', 0, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se resuelve una habilidad disparada que se genera al activar una habilidad activada?')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las cartas de acción tienen efectos, no habilidades.'), 'Verdadero', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las cartas de acción tienen efectos, no habilidades.')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las cartas de acción tienen efectos, no habilidades.'), 'Falso', 0, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Las cartas de acción tienen efectos, no habilidades.')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena la resolución básica de una acción según el resumen de reglas.'), 'Se resuelve su efecto inmediatamente', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena la resolución básica de una acción según el resumen de reglas.')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena la resolución básica de una acción según el resumen de reglas.'), 'La carta entra temporalmente en la zona de juego', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena la resolución básica de una acción según el resumen de reglas.')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena la resolución básica de una acción según el resumen de reglas.'), 'La carta va al descarte tras resolverse', 1, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Ordena la resolución básica de una acción según el resumen de reglas.')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a las localizaciones cuando entran en juego?'), 'Si tienen una habilidad, puede usarse en el mismo turno en que se juegan.', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a las localizaciones cuando entran en juego?')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a las localizaciones cuando entran en juego?'), 'Siempre entran exerted y no pueden ganar lore hasta el siguiente turno.', 0, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a las localizaciones cuando entran en juego?')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a las localizaciones cuando entran en juego?'), 'Pueden desafiar como si fueran personajes si tienen daño marcado.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a las localizaciones cuando entran en juego?')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a las localizaciones cuando entran en juego?'), 'No tienen habilidades mientras estén en juego.', 0, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué afirmación describe correctamente a las localizaciones cuando entran en juego?')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se destierra una localización por daño?'), 'En cuanto recibe cualquier cantidad de daño.', 0, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se destierra una localización por daño?')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se destierra una localización por daño?'), 'Durante un Game State Check si su daño es igual o mayor que su Voluntad.', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se destierra una localización por daño?')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se destierra una localización por daño?'), 'Solo al final del turno del jugador activo.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se destierra una localización por daño?')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se destierra una localización por daño?'), 'Nunca; las localizaciones no pueden ser desterradas por daño.', 0, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuándo se destierra una localización por daño?')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.'), 'Deben contener al menos 60 cartas.', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.'), 'No pueden contener más de dos colores de tinta.', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.'), 'Pueden contener cualquier número de copias de una carta si el jugador la abrió en sobres.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.'), 'No existe tamaño máximo si el jugador puede barajarlo de forma oportuna sin ayuda.', 1, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.'), 'El máximo normal es cuatro copias de una misma carta.', 1, 5, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre mazos Constructed.')
      AND "Orden" = 5
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuál es el mínimo de sobres por jugador en un torneo Sellado?'), '4 sobres', 0, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuál es el mínimo de sobres por jugador en un torneo Sellado?')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuál es el mínimo de sobres por jugador en un torneo Sellado?'), '6 sobres', 1, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuál es el mínimo de sobres por jugador en un torneo Sellado?')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuál es el mínimo de sobres por jugador en un torneo Sellado?'), '8 sobres', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuál es el mínimo de sobres por jugador en un torneo Sellado?')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuál es el mínimo de sobres por jugador en un torneo Sellado?'), '12 sobres', 0, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Cuál es el mínimo de sobres por jugador en un torneo Sellado?')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué describe correctamente la construcción de mazos en Limited?'), 'Deben tener al menos 40 cartas, sin restricción de colores de tinta y con cualquier número de copias desde el pool abierto.', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué describe correctamente la construcción de mazos en Limited?')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué describe correctamente la construcción de mazos en Limited?'), 'Deben tener al menos 60 cartas y no más de dos colores de tinta.', 0, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué describe correctamente la construcción de mazos en Limited?')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué describe correctamente la construcción de mazos en Limited?'), 'Solo pueden jugarse hasta cuatro copias de cada carta, como en Constructed.', 0, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué describe correctamente la construcción de mazos en Limited?')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué describe correctamente la construcción de mazos en Limited?'), 'Deben contener exactamente 40 cartas y solo cartas de un mismo set.', 0, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = '¿Qué describe correctamente la construcción de mazos en Limited?')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.'), 'Un jugador puede conceder una partida incompleta en cualquier momento.', 1, 1, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.')
      AND "Orden" = 1
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.'), 'Se puede ofrecer algo a cambio de una concesión si ambos jugadores están de acuerdo.', 0, 2, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.')
      AND "Orden" = 2
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.'), 'Los jugadores pueden acordar un split antes de que termine el enfrentamiento.', 1, 3, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.')
      AND "Orden" = 3
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.'), 'Si recibes una oferta inapropiada relacionada con una concesión, debes llamar a un juez.', 1, 4, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.')
      AND "Orden" = 4
);

INSERT INTO "OpcionesRespuesta" ("PreguntaId", "Texto", "EsCorrecta", "Orden", "Explicacion")
SELECT (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.'), 'Puedes pedir a tu oponente que conceda una partida una vez por enfrentamiento.', 0, 5, NULL
WHERE NOT EXISTS (
    SELECT 1 FROM "OpcionesRespuesta"
    WHERE "PreguntaId" = (SELECT "Id" FROM "Preguntas" WHERE "Texto" = 'Selecciona las afirmaciones correctas sobre concesiones y pactos de resultado.')
      AND "Orden" = 5
);