"""Incorpora en la wiki los casos de Discord ya validados.

El script conserva los informes de validación originales y genera una capa de
incorporación idempotente: los casos ya cubiertos se registran como duplicados,
los relacionados añaden una adenda al artículo existente y los restantes crean
un artículo nuevo.
"""

from __future__ import annotations

import json
import os
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATION = ROOT / "analisis/discord-2026-09-05/validacion_casos_102.json"
OUT_DIR = ROOT / "analisis/discord-2026-09-05"
INDEX = ROOT / "01. Reglas/11. Casos de ejemplo y aclaraciones/ÍNDICE - Casos de ejemplo y aclaraciones.md"

CR = "[[Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf|Comprehensive Rules 2.2.0]]"
TR = "[[Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf|Tournament Rules 6.11]]"


# Las 20 ampliaciones conservan un artículo existente como destino principal.
# CASO-126 se fuerza aquí como ampliación porque el artículo de Coconut ya
# documenta expresamente que la beta no define tiempo ni estructura.
EXPANSION_TARGETS: dict[str, str] = {
    "CASO-004": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Heredar una palabra clave al hacer shift.md",
    "CASO-018": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Set Championship con 65 jugadores o más.md",
    "CASO-040": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Fichas de recordatorio sobre el mazo.md",
    "CASO-058": "01. Reglas/10. Artículos/Reversión de jugadas (takebacks).md",
    "CASO-063": "01. Reglas/10. Artículos/Reversión de jugadas (takebacks).md",
    "CASO-067": "04. Guia de correccion de jugadas/04. Conducta antideportiva/4.5 Resultado de un encuentro inapropiado (Improper Match Result).md",
    "CASO-070": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Habilidades estáticas presentes en juego y sus interacciones.md",
    "CASO-088": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Posey - Vampire Potato puede usar Potato Shift sobre Morph.md",
    "CASO-089": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Escudos (replacement) vs Resist.md",
    "CASO-095": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Desterrar y volver a la mano desde la zona de juego.md",
    "CASO-099": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Resolución parcial sin objetivo válido.md",
    "CASO-103": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Winnie the Pooh - Hunny Archmage cuenta otra copia como other Hunny.md",
    "CASO-119": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Qué pasa cuando se juegan dos cartas a la vez.md",
    "CASO-124": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Tod + You Came Back y habilidades en el Bolsa.md",
    "CASO-125": "01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md",
    "CASO-126": "01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md",
    "CASO-128": "01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md",
    "CASO-129": "01. Reglas/9. Multijugador (Multiplayer)/Cartas Coconut de la beta.md",
    "CASO-133": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Luisa Madrigal - I Can Take It, condición Then-if y GSC.md",
    "CASO-137": "01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md",
}


NEW_ARTICLES = [
    {
        "ids": ["CASO-001"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Legalidad y prohibiciones - fuente oficial vigente.md",
        "title": "Legalidad y prohibiciones: fuente oficial vigente",
        "question": "¿Qué fuente permite comprobar las prohibiciones y la legalidad de cartas si el documento de torneo todavía no incorpora el anuncio?",
        "answer": (
            "La referencia vinculante es el comunicado o la lista oficial vigente para el evento, junto con las Tournament Rules aplicables. "
            "La aplicación oficial sirve como consulta auxiliar y puede ayudar a detectar una discrepancia, pero no sustituye un anuncio posterior ni una errata publicada. "
            "Si dos fuentes oficiales parecen incompatibles, se conserva la fecha de cada una y se consulta al Lore Guide del evento antes de registrar la legalidad."
        ),
        "foundation": f"{TR}, especialmente la sección de formatos y la comunicación oficial del evento.",
        "sequence": [
            "Anota la fecha y el nivel del evento.",
            "Comprueba la Tournament Rules y el anuncio o kit específico más reciente.",
            "Usa la aplicación solo como comprobación auxiliar y eleva cualquier conflicto al Lore Guide.",
        ],
        "tags": "#tournament-rules #communication #scope",
    },
    {
        "ids": ["CASO-010"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Wilds Unknown - sets legales según anuncio del evento.md",
        "title": "Wilds Unknown: sets legales según anuncio del evento",
        "question": "¿El campeonato de Wilds Unknown utiliza únicamente sets 9–12 o todo el formato Core vigente?",
        "answer": (
            "No puede decidirse entre «9–12» y «todo Core» usando solo una tabla actual de Tournament Rules. "
            "En un campeonato concreto manda el anuncio o kit de ese evento, con su fecha y formato. La tabla de Core permite comprobar qué era legal en la fecha de la regla, pero no demuestra por sí sola las instrucciones históricas de Wilds Unknown. "
            "Hasta localizar ese anuncio, la respuesta debe quedar como provisional y no publicarse como regla general."
        ),
        "foundation": f"{TR}, tabla de legalidad de Core y anuncio/kit del campeonato.",
        "sequence": [
            "Identifica la fecha y el nivel del campeonato.",
            "Lee el anuncio o kit específico y compáralo con la tabla de Core vigente entonces.",
            "Si falta el documento del evento, marca el caso como no verificable, sin convertir una práctica histórica en norma general.",
        ],
        "tags": "#tournament-rules #scope #round-structure",
    },
    {
        "ids": ["CASO-014"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Set Championships - decklists y deck checks.md",
        "title": "Set Championships: decklists y deck checks",
        "question": "¿Son obligatorias las listas de mazo y sus comprobaciones en Set Championships?",
        "answer": (
            "La lista de mazo es exigible cuando el nivel Competitive o Premier y el kit del evento así lo establecen. "
            "La obligación de entregar una lista no significa que el organizador tenga que revisar el mazo de todos los jugadores: las Tournament Rules exigen comprobaciones cuando sea posible y fijan una expectativa mínima para Premier. "
            "La presencia de jueces y el procedimiento de registro deben anunciarse con el evento."
        ),
        "foundation": f"{TR}, secciones 3.8 (registro de mazo) y 3.9 (comprobaciones).",
        "sequence": [
            "Comprueba el nivel del evento y el kit aplicable.",
            "Entrega la decklist en el formato y momento indicados.",
            "Aplica deck checks según la capacidad del evento y la expectativa mínima del nivel, sin prometer una revisión universal.",
        ],
        "tags": "#tournament-rules #deck-construction #communication",
    },
    {
        "ids": ["CASO-017"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Top Cut - quién elige empezar en cada partida.md",
        "title": "Top Cut: quién elige empezar en cada partida",
        "question": "¿Quién elige jugar primero o segundo a partir de la segunda ronda de Top Cut?",
        "answer": (
            "En un enfrentamiento nuevo de Top Cut Premier, el seed más alto de la fase suiza elige quién juega primero en la primera partida. "
            "En las partidas siguientes del mismo enfrentamiento elige quién perdió la partida anterior. Para un evento Competitive hay que comprobar el kit, porque puede fijar un procedimiento distinto."
        ),
        "foundation": f"{TR}, sección 3.3 sobre elección del jugador inicial en Top Cut.",
        "sequence": [
            "Al comenzar un match nuevo, identifica el seed de la fase suiza.",
            "El seed más alto elige primero en la partida 1.",
            "En cada partida posterior elige quien perdió la anterior.",
        ],
        "tags": "#round-structure #tournament-rules #timing",
    },
    {
        "ids": ["CASO-026"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Diablo y el robo aparente tras un desafío.md",
        "title": "Diablo y el robo aparente tras un desafío",
        "question": "¿Hay un error si, después de desafiar Will of the Wisp con Gantu y dañar a Diablo mediante un lugar, parece que el rival recibe dos robos?",
        "answer": (
            "No hay dos robos de Diablo en la secuencia descrita. Una carta vuelve a la mano por el efecto del lugar y solo la otra carta es el robo de Diablo. "
            "La interfaz del simulador puede mostrar ambos movimientos juntos; para revisar la jugada hay que reconstruir cada cambio de zona. Si el estado final coincide con esa secuencia, no queda una infracción de reglas pendiente."
        ),
        "foundation": f"{CR}, reglas de movimiento entre zonas y de resolución de efectos.",
        "sequence": [
            "Separa el retorno a la mano del efecto de Will of the Wisp.",
            "Comprueba el único robo generado por Diablo.",
            "Compara el número de cartas final con esas dos operaciones, sin contar la carta devuelta como un segundo robo.",
        ],
        "tags": "#draw-multiple #hand #play-zone",
    },
    {
        "ids": ["CASO-029"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Permisos adicionales para entintar se acumulan.md",
        "title": "Permisos adicionales para entintar se acumulan",
        "question": "¿Jugar dos copias de la carta denominada «sails» permite poner dos cartas adicionales en el tintero?",
        "answer": (
            "Los permisos independientes para entintar una carta adicional se acumulan: si dos cartas conceden ese permiso y no imponen una limitación incompatible, puedes realizar las dos acciones adicionales. "
            "La conversación no identifica de forma completa la carta llamada «sails», por lo que sus restricciones concretas deben comprobarse antes de confirmar el ejemplo; la regla de acumulación sí es la aplicable."
        ),
        "foundation": f"{CR}, regla 7.5.5 sobre efectos que permiten entintar cartas adicionales.",
        "sequence": [
            "Identifica cada carta y el texto exacto que concede el permiso.",
            "Aplica por separado cada permiso durante el turno indicado.",
            "Comprueba después las restricciones propias de cada efecto.",
        ],
        "tags": "#inkwell #turn-actions #gameplay",
    },
    {
        "ids": ["CASO-037"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Descalificación y eventos paralelos.md",
        "title": "Descalificación y eventos paralelos",
        "question": "¿Una descalificación del evento principal impide jugar los eventos paralelos?",
        "answer": (
            "Una descalificación se aplica al evento en el que se dicta y no crea por sí sola una prohibición general del recinto ni de todos sus eventos paralelos. "
            "Para extender la exclusión debe existir una medida de elegibilidad o conducta comunicada por la organización. Si esa medida está documentada, se aplica según su alcance."
        ),
        "foundation": f"{TR}, reglas de conducta, autoridad del organizador y alcance de las sanciones.",
        "sequence": [
            "Lee la sanción y el evento al que se refiere.",
            "Comprueba si el organizador comunicó una exclusión adicional.",
            "Si hay duda sobre el alcance, consulta al Lore Guide antes de inscribirte en el paralelo.",
        ],
        "tags": "#tournament-rules #scope #communication",
    },
    {
        "ids": ["CASO-062"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Bruno y equipos con varios nombres.md",
        "title": "Bruno y equipos con varios nombres",
        "question": "¿Qué nombres tiene un equipo al nombrar una carta con Bruno? ¿Hamish, Hubert & Harris representa varios personajes?",
        "answer": (
            "Al nombrar una carta con Bruno se usa un nombre de carta, tal como aparece impreso. Un personaje cuyo nombre contiene un equipo sigue siendo una sola carta de personaje, aunque tenga varios nombres separados por comas o conjunciones; no representa varias cartas ni varios personajes para una elección. "
            "El ejemplo concreto de Hamish, Hubert & Harris debe contrastarse con el texto vigente y cualquier CRD antes de fijar una excepción."
        ),
        "foundation": f"{CR}, reglas 5.2.6–5.2.6.2 sobre nombres dobles y personajes con varios nombres.",
        "sequence": [
            "Lee el nombre completo de la carta que se va a nombrar.",
            "Trata el equipo como un único personaje para objetivos y conteos.",
            "Comprueba la versión vigente de la carta si existe una duda de redacción.",
        ],
        "tags": "#multiple-names #scope #gameplay",
    },
    {
        "ids": ["CASO-066", "CASO-102"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Sideboard en Limited - sellado, draft y presentación.md",
        "title": "Sideboard en Limited: sellado, draft y presentación",
        "question": "En prerelease, sellado, draft o presentación, ¿se pueden cambiar cartas entre partidas o rondas y quién determina la norma?",
        "answer": (
            "No existe un permiso universal de sideboard entre partidas o rondas de Limited en la documentación consultada. El organizador debe anunciar cómo se construye el mazo y qué cambios, si alguno, están permitidos para ese evento. "
            "Una práctica de una tienda o de un evento secundario no se convierte en regla general; si no se anunció una excepción, se conserva el mazo registrado durante el encuentro."
        ),
        "foundation": f"{TR}, sección 6.2 sobre construcción de Limited y las instrucciones específicas del organizador.",
        "sequence": [
            "Consulta las instrucciones de construcción antes de abrir o registrar el pool.",
            "Pregunta qué cambios se permiten entre partidas y entre rondas.",
            "Sigue esa instrucción para todo el evento y llama al Lore Guide si el anuncio es ambiguo.",
        ],
        "tags": "#deck-construction #tournament-rules #scope",
    },
    {
        "ids": ["CASO-072"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Fundas opacas y legalidad en torneo.md",
        "title": "Fundas opacas y legalidad en torneo",
        "question": "¿Qué requisitos deben cumplir las fundas en torneo y sirven las de reverso translúcido?",
        "answer": (
            "Las fundas deben tener el reverso completamente opaco y no reflectante, ser uniformes y no presentar daños, marcas o diferencias que permitan distinguir cartas. «Mate» describe la textura, pero no garantiza opacidad. Un reverso translúcido no cumple el requisito aunque la funda sea mate."
        ),
        "foundation": f"{TR}, sección 3.11 sobre fundas, cartas alteradas y cartas marcadas.",
        "sequence": [
            "Revisa todas las fundas con la misma orientación y bajo la iluminación del torneo.",
            "Sustituye las que sean translúcidas, reflectantes, dañadas o distinguibles.",
            "Si el juez detecta una diferencia, sigue su decisión antes de continuar la partida.",
        ],
        "tags": "#tournament-rules #marked-cards #communication",
    },
    {
        "ids": ["CASO-084"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Nombres de mazo y conducta en torneo.md",
        "title": "Nombres de mazo y conducta en torneo",
        "question": "¿Hay límites para nombres de mazo con dobles sentidos al inscribirse en un evento oficial?",
        "answer": (
            "El nombre de un mazo forma parte de la comunicación del evento y está sujeto a las normas de conducta. La organización o el Lore Guide puede rechazar o exigir cambiar un nombre ofensivo, discriminatorio o inapropiado. No hay una decisión documentada en la wiki que apruebe el nombre concreto «circle herc», así que no debe presentarse como permitido sin consultar al evento."
        ),
        "foundation": f"{TR}, reglas de comunicación y conducta del evento.",
        "sequence": [
            "Usa un nombre neutral al registrar el mazo.",
            "Si la organización cuestiona el nombre, cámbialo o solicita una decisión del Lore Guide.",
            "No conviertas la aceptación informal de una tienda en una aprobación para otros eventos.",
        ],
        "tags": "#tournament-rules #communication",
    },
    {
        "ids": ["CASO-094"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Source of the Vine y responsabilidad de anunciar.md",
        "title": "Source of the Vine y responsabilidad de anunciar",
        "question": "¿Quién debe recordar y comunicar la habilidad de Source of the Vine cuando el rival hace una aventura?",
        "answer": (
            "El controlador de Source of the Vine debe comunicar su disparo obligatorio cuando un personaje rival hace una aventura. El rival decide si paga 1 tinta y esa elección debe quedar clara; el silencio no puede presumirse como una negativa a pagar. Ambos jugadores comparten la obligación de mantener el estado correcto y deben llamar al Lore Guide si el disparo se olvida."
        ),
        "foundation": f"{CR}, reglas de habilidades disparadas y elecciones, junto con {TR} en materia de comunicación.",
        "sequence": [
            "El personaje rival hace una aventura y se dispara SIPHON.",
            "El controlador anuncia el disparo y el rival declara si paga 1 tinta.",
            "Solo después se aplica la ganancia de lore o la prevención indicada por el texto.",
        ],
        "tags": "#triggered-ability #communication #lore-gain",
    },
    {
        "ids": ["CASO-114"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Entintar boca arriba en torneo.md",
        "title": "Entintar boca arriba en torneo",
        "question": "¿Por qué las Comprehensive Rules siguen indicando colocar la tinta boca abajo si el torneo usa entintado boca arriba?",
        "answer": (
            "No hay contradicción. Las Comprehensive Rules describen la acción normal de poner una carta en el tintero boca abajo. Las Tournament Rules añaden un procedimiento de torneo: la carta se mantiene boca arriba durante el turno en que se entinta y se gira boca abajo al final de ese turno. La excepción temporal sirve para comunicación y no cambia la regla general."
        ),
        "foundation": f"{CR}, regla 4.2.1.3, y {TR}, sección 5.5.",
        "sequence": [
            "Entinta la carta y déjala boca arriba durante tu turno.",
            "Usa esa visibilidad para verificar el estado del tintero.",
            "Al final del turno, gírala boca abajo según el procedimiento del torneo.",
        ],
        "tags": "#inkwell #tournament-rules #communication",
    },
    {
        "ids": ["CASO-122"],
        "path": "01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Guías comunitarias de GooglyGlimmers.md",
        "title": "Guías comunitarias de GooglyGlimmers",
        "question": "¿Dónde se publican actualmente las guías de sets de GooglyGlimmers para consultar interacciones?",
        "answer": (
            "Las guías de sets son un recurso comunitario y su disponibilidad cambia con el tiempo. Cuando no existe una guía escrita reciente, deben consultarse los canales o vídeos que el autor haya enlazado. Ese material puede ayudar a entender una interacción, pero no sustituye las Comprehensive Rules, las Tournament Rules ni una decisión del Lore Guide."
        ),
        "foundation": "Recurso comunitario del autor; no es una fuente normativa oficial.",
        "sequence": [
            "Busca el enlace más reciente publicado por el autor.",
            "Comprueba la fecha y el set al que se refiere el material.",
            "Contrasta cualquier ruling con la documentación oficial vigente.",
        ],
        "tags": "#communication #scope",
    },
]


# Ajustes verificados contra la documentación local y el texto exacto de las
# cartas. Se aplican al regenerar para que los artículos y los informes no
# vuelvan a las referencias genéricas de la primera pasada.
ARTICLE_OVERRIDES = {
    "CASO-001": {
        "foundation": "[[03. Reglas de Torneo/1. Definiciones sobre toneos/1.6 Legalidad de Sets (Set Legality).md|1.6. Legalidad de sets]] y [[03. Reglas de Torneo/5 Información y comunicación/5.4 Información en el Juego (In-Game Information).md|5.4. Información en el juego]]. La lista de prohibiciones y el anuncio del evento prevalecen para ese evento y fecha.",
    },
    "CASO-010": {
        "foundation": "[[03. Reglas de Torneo/1. Definiciones sobre toneos/1.6 Legalidad de Sets (Set Legality).md|1.6. Legalidad de sets]], incluida la rotación de Core, y el anuncio o kit específico del campeonato.",
    },
    "CASO-014": {
        "answer": "En los torneos Competitive y Premier los jugadores deben registrar su mazo; el organizador anuncia el método y la fecha límite. La obligación de entregar una lista no significa que el organizador tenga que revisar el mazo de todos los jugadores: las reglas exigen comprobaciones cuando sea posible y fijan una expectativa mínima del 10 % para Premier. La presencia de jueces y el procedimiento concreto deben anunciarse con el evento.",
        "foundation": "[[03. Reglas de Torneo/3. Operaciones en los torneos/3.8 Registro de Mazos (Deck Registration).md|Registro de mazos]] y [[03. Reglas de Torneo/3. Operaciones en los torneos/3.9 Revisión de Mazos (Deck Checks).md|Revisión de mazos]]. En Competitive y Premier se registra el mazo; en Premier se espera revisar al menos el 10 %.",
    },
    "CASO-017": {
        "question": "¿Quién elige jugar primero o robar primero en cada partida de Top Cut?",
        "answer": "En Top Cut Premier, antes de la primera partida se determina aleatoriamente qué jugador elige entre jugar primero o robar primero. En cada partida posterior elige quien perdió la partida anterior. En eliminación directa, el seed más alto de la fase suiza elige en la primera partida. Los eventos Competitive pueden anunciar una estructura distinta.",
        "foundation": "[[03. Reglas de Torneo/3. Operaciones en los torneos/3.3 Estructura de Partida (Match Structure).md|3.3. Estructura de partida]], apartados Premier Play y eliminación directa.",
        "sequence": [
            "En Premier, determina aleatoriamente quién elige primero o roba primero y toma esa decisión antes de mirar la mano inicial.",
            "En cada partida posterior elige quien perdió la partida anterior.",
            "En eliminación directa, el seed más alto elige en la partida 1; después elige quien perdió la partida anterior.",
        ],
    },
    "CASO-026": {
        "question": "¿Hay un error si, después de desafiar [[02. Listado de Cartas/Set 12 - Wilds Unknown.md#Will O' The Wisp - Forest Spirit|Will O' The Wisp]] con [[02. Listado de Cartas/Set 1 - The First Chapter.md#Gantu - Galactic Federation Captain|Gantu]] y dañar a [[02. Listado de Cartas/Set 4 - Ursula's Return.md#Diablo - Devoted Herald|Diablo]] mediante un lugar, parece que el rival recibe dos robos?",
        "foundation": "[[01. Reglas/7. Zonas (Zones)/7.4. Juego (Play).md|7.4. Juego]] y [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects).md|6.7. Resolución de cartas y efectos]], junto con el texto de [[02. Listado de Cartas/Set 12 - Wilds Unknown.md#Will O' The Wisp - Forest Spirit|Will O' The Wisp]] y [[02. Listado de Cartas/Set 4 - Ursula's Return.md#Diablo - Devoted Herald|Diablo]].",
        "sequence": [
            "Separa el retorno a la mano del efecto de [[02. Listado de Cartas/Set 12 - Wilds Unknown.md#Will O' The Wisp - Forest Spirit|Will O' The Wisp]].",
            "Comprueba el único robo generado por [[02. Listado de Cartas/Set 4 - Ursula's Return.md#Diablo - Devoted Herald|Diablo]].",
            "Compara el número de cartas final con esas dos operaciones, sin contar la carta devuelta como un segundo robo.",
        ],
    },
    "CASO-029": {
        "question": "¿Jugar dos copias de [[02. Listado de Cartas/Set 6 - Azurite Sea.md#Sail the Azurite Sea|Sail the Azurite Sea]] permite poner dos cartas adicionales en el tintero?",
        "answer": "Los permisos independientes para entintar una carta adicional se acumulan. Cada [[02. Listado de Cartas/Set 6 - Azurite Sea.md#Sail the Azurite Sea|Sail the Azurite Sea]] concede una acción adicional durante ese turno; con dos copias puedes realizar las dos, además de tu acción normal de entintar, si aún tienes cartas en la mano y cumples el resto de requisitos.",
        "foundation": "[[01. Reglas/7. Zonas (Zones)/7.5. Pozo de tinta (Inkwell).md|7.5. Pozo de tinta]] y [[01. Reglas/4. Acciones de turno (Turn Actions)/4.2 Entintar una carta (Ink a Card).md|4.2. Entintar una carta]], junto al texto de [[02. Listado de Cartas/Set 6 - Azurite Sea.md#Sail the Azurite Sea|Sail the Azurite Sea]].",
        "sequence": [
            "Identifica cada copia y su texto exacto.",
            "Aplica por separado cada permiso durante el turno indicado.",
            "Comprueba después las restricciones propias de cada efecto.",
        ],
    },
    "CASO-037": {
        "foundation": "[[03. Reglas de Torneo/7. Conducta del Jugador/7.1. Conducta Prohibida (Prohibited Conduct).md|7.1. Conducta prohibida]] y las condiciones de elegibilidad comunicadas por la organización.",
    },
    "CASO-062": {
        "question": "¿Qué nombre se debe decir al nombrar una carta con Bruno? ¿[[02. Listado de Cartas/Set 12 - Wilds Unknown.md#Hamish, Hubert & Harris - Making Mischief|Hamish, Hubert & Harris]] representa varios personajes?",
        "answer": "Al nombrar una carta con Bruno se usa un nombre de carta, tal como aparece impreso. Un personaje cuyo nombre contiene un equipo sigue siendo una sola carta de personaje, aunque el nombre incluya varios nombres separados por comas o conjunciones; no representa varias cartas ni varios personajes para una elección. [[02. Listado de Cartas/Set 12 - Wilds Unknown.md#Hamish, Hubert & Harris - Making Mischief|Hamish, Hubert & Harris]] debe tratarse como un único personaje con nombres múltiples: el nombre combinado y los nombres individuales pueden ser nombres distintos a efectos de una elección. La puntuación de esta carta genera una anomalía de redacción; si se discute qué fragmentos exactos forman cada nombre, hay que consultar el CRD o al Lore Guide.",
        "foundation": "[[01. Reglas/5. Cartas y tipos de carta (Cards and Card types)/5.2. Partes de una carta (Parts of a Card).md|5.2. Partes de una carta]], apartados de nombre y múltiples nombres, junto al texto de [[02. Listado de Cartas/Set 12 - Wilds Unknown.md#Hamish, Hubert & Harris - Making Mischief|Hamish, Hubert & Harris]].",
    },
    "CASO-066": {
        "foundation": "[[03. Reglas de Torneo/6. Formatos de torneos - Limitado/6.1 Descripción general de Limitado (Limited Overview).md|6.1. Descripción general de Limited]], [[03. Reglas de Torneo/6. Formatos de torneos - Limitado/6.2 Sellado (Sealed).md|6.2. Sellado]] y [[03. Reglas de Torneo/6. Formatos de torneos - Limitado/6.4 Draft.md|6.4. Draft]].",
    },
    "CASO-072": {
        "foundation": "[[03. Reglas de Torneo/3. Operaciones en los torneos/3.11 Accesorios Aprobados (Approved Accessories).md|3.11. Accesorios aprobados]], apartado Fundas.",
    },
    "CASO-084": {
        "foundation": "[[03. Reglas de Torneo/5 Información y comunicación/5.6. Nomenclatura y Descripciones de Cartas (Card Naming and Descriptions).md|5.6. Nomenclatura y descripciones]] y [[03. Reglas de Torneo/7. Conducta del Jugador/7.1. Conducta Prohibida (Prohibited Conduct).md|7.1. Conducta prohibida]].",
    },
    "CASO-094": {
        "question": "¿Quién debe recordar y comunicar la habilidad de [[02. Listado de Cartas/Set 13 - Attack of the Vine.md#Source of the Vine|Source of the Vine]] cuando el rival hace una aventura?",
        "foundation": "[[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.2. Habilidades Disparadas (Triggered Abilities).md|6.2. Habilidades disparadas]] y [[03. Reglas de Torneo/5 Información y comunicación/5.4 Información en el Juego (In-Game Information).md|5.4. Información en el juego]], junto al texto de [[02. Listado de Cartas/Set 13 - Attack of the Vine.md#Source of the Vine|Source of the Vine]].",
    },
    "CASO-114": {
        "foundation": "[[01. Reglas/4. Acciones de turno (Turn Actions)/4.2 Entintar una carta (Ink a Card).md|4.2. Entintar una carta]] y [[03. Reglas de Torneo/5 Información y comunicación/5.5 Pozo de tinta.md|5.5. Pozo de tinta en torneo]].",
    },
    "CASO-122": {
        "foundation": "Recurso comunitario del autor; no es una fuente normativa oficial. Contrástalo con [[01.1.a Official English Reference – Unmodified/1. Concepts.md|Comprehensive Rules]] y las [[03. Reglas de Torneo/3. Operaciones en los torneos/3.3 Estructura de Partida (Match Structure).md|Tournament Rules]] vigentes.",
    },
}

for _entry in NEW_ARTICLES:
    for _case_id in _entry["ids"]:
        if _case_id in ARTICLE_OVERRIDES:
            _entry.update(ARTICLE_OVERRIDES[_case_id])


EXPANSIONS: dict[str, str] = {
    "CASO-004": """### CASO-004 — Bronx: preparado no significa seco\n\nAl hacer Shift, hay que distinguir dos estados independientes: **preparado/agotado** y **seco/secándose**. Bronx puede estar preparado y seguir secándose si acaba de entrar en juego; prepararlo no elimina la restricción de secado. El personaje superior hereda el estado correspondiente según las reglas de Shift, pero no convierte una carta recién jugada en una carta seca.\n\nFundamento: regla 1.7.5 y regla 8.10.4 de {CR}.""",
    "CASO-018": """### CASO-018 — 18 jugadores: tabla oficial de rondas y Top Cut\n\nCon 18 jugadores, la tabla de Set Championship asigna **5 rondas suizas y Top 8**. El cálculo de qué jugadores quedarían fuera de un Top 4 puede servir para explicar las consecuencias matemáticas, pero no autoriza sustituir la tabla por cuatro rondas y Top 4. Cualquier estructura distinta requiere autorización y debe anunciarse antes del evento.\n\nFundamento: sección 3.1–3.2 de {TR}.""",
    "CASO-040": """### CASO-040 — No usar números para recordar Fuerza o Voluntad\n\nLos dados, papeles o fichas con «+1», «−1» o «−3» no pueden representar cambios numéricos de Fuerza o Voluntad. Se pueden usar recordatorios no numéricos que no oculten cartas ni creen ambigüedad. La excepción numérica prevista en las reglas de torneo es el daño.\n\nFundamento: secciones 5.1–5.2 de {TR}.""",
    "CASO-058": """### CASO-058 — Acciones agrupadas y takeback\n\nSolicitar lore con varios personajes puede tratarse como una secuencia agrupada fuera de orden si las acciones son inmediatas y no se obtuvo información nueva. La aplicación de la reversión sigue siendo una decisión del Lore Guide: no se concede automáticamente por haber actuado de forma agrupada. La fecha histórica atribuida al anuncio de esta política no queda verificada en la documentación local.\n\nFundamento: política de reversión de jugadas y sección 3.7 de {TR}.""",
    "CASO-063": """### CASO-063 — Pasar turno y habilidades opcionales olvidadas\n\nPasar turno puede rebobinarse solo si el Lore Guide considera que se cumplen los criterios de takeback. Una habilidad opcional de final de turno y un pase omitido pueden formar una única secuencia únicamente cuando no hubo información nueva y los hechos lo permiten. Robar cartas o realizar otra acción con información privada normalmente impide la reversión.\n\nFundamento: artículo de reversión de jugadas y sección 3.7 de {TR}.""",
    "CASO-067": """### CASO-067 — Separar reparto de premios y resultado del encuentro\n\nEl reparto de premios disponibles solo es válido dentro del alcance del nivel del evento y con aceptación de todos los jugadores restantes. No se puede ofrecer dinero, bienes o una ventaja externa a cambio de conceder, ni decidir el resultado al azar. La concesión, una venta posterior de un premio y un reparto autorizado son hechos distintos y deben analizarse por separado.\n\nFundamento: sección 7.1 de {TR} y la guía de resultado de encuentro inapropiado.""",
    "CASO-070": """### CASO-070 — Aplicar conjuntamente daño y agotamiento al entrar\n\nLas modificaciones de cómo una carta entra en juego no son efectos de reemplazo independientes que obliguen a escoger uno. Si un efecto hace que el personaje entre con daño y otro hace que entre agotado, se aplican ambos durante la resolución de la jugada, salvo que el propio texto establezca una incompatibilidad. El personaje puede quedar agotado y con daño mientras sigue secándose.\n\nFundamento: reglas 4.3.3 y 6.7.9 de {CR}.""",
    "CASO-088": """### CASO-088 — Potato recién jugado y variante Morph\n\nLa parte inequívoca es esta: un objeto Potato jugado durante el turno sigue sin estar en juego al comienzo de ese turno. Aunque se prepare, un personaje que use Potato Shift sobre él entra **secándose**. La combinación de Potato Shift con Morph depende de cómo se aplique la regla especial de la variante y queda marcada para una aclaración oficial; no se debe presentar una conclusión única mientras el texto siga ambiguo.\n\nFundamento: reglas 1.7.5, 8.10.4 y 8.10.8 de {CR}.""",
    "CASO-089": """### CASO-089 — Resist, daño infligido y daño recibido\n\nResist modifica el daño que recibe el objetivo. Si reduce la cantidad a cero, el efecto de origen sigue siendo un efecto que **inflige daño**, aunque el personaje no reciba daño. La cantidad que una habilidad de Mulan copie o utilice depende de su texto exacto y no debe inferirse del debate; hay que separar siempre daño indicado por el efecto, daño infligido y daño recibido.\n\nFundamento: reglas 1.9.3–1.9.5 y 8.8 de {CR}.""",
    "CASO-095": """### CASO-095 — John Smith y un personaje que abandona el juego\n\nCon John Smith — Snow Tracker se comprueba el evento de desafío con el texto exacto de esa carta. Si el desafío se declaró y el evento ocurrió antes de que el personaje abandone el juego, el movimiento posterior no borra el evento ya ocurrido. No se debe trasladar esta conclusión a John Smith — Undaunted Protector, cuyo texto es distinto.\n\nFundamento: reglas 4.6.4–4.6.6 y 7.4.3 de {CR}.""",
    "CASO-099": """### CASO-099 — Pagar Scream Canister sin objetivo legal\n\nScream Canister puede activarse y pagarse aunque no exista un objetivo legal para su efecto. El coste se paga al iniciar la acción; al resolver, se hace todo lo posible y se omite la elección que no tiene objetivo. Pagar el coste no convierte una elección sin objetivo en una elección válida.\n\nFundamento: reglas 1.2.3, 4.3.2 y 6.7.2 de {CR}.""",
    "CASO-103": """### CASO-103 — Hunny pertenece a cada versión de carta\n\nLas clasificaciones pertenecen a cada carta física concreta y no se transfieren entre versiones que comparten personaje. Para Winnie the Pooh — Hunny Wizard se aplica la errata o fuente de carta vigente; una aplicación que aún no la muestre no demuestra que la errata no exista.\n\nFundamento: regla 5.3 de {CR} y la errata publicada de la carta.""",
    "CASO-119": """### CASO-119 — Touch the Sky no usa «chosen»\n\nEl texto impreso de Touch the Sky dice «move a character of yours» y no contiene una elección «chosen». Por eso no satisface una condición de Tod que requiera que el personaje sea elegido para una acción o habilidad de objeto. La variante hipotética que permitiría mover personajes rivales no forma parte de la carta y no produce una regla aplicable sobre Ward.\n\nFundamento: reglas 5.2.6 y 6.7 de {CR}, junto al texto vigente de Touch the Sky.""",
    "CASO-124": """### CASO-124 — Rechazar un «may» de Tod\n\nRechazar una opción «may» no cuenta como usarla. Por tanto, si Tod es elegido y su controlador decide no prepararlo, esa oportunidad no se consume; las oportunidades se cuentan cuando se usa la habilidad. La cantidad exacta de usos debe comprobarse en el texto vigente de Tod y no extrapolarse sin más desde un ejemplo de «once».\n\nFundamento: regla 6.1.13 de {CR} y el texto vigente de Tod — Knows All the Tricks.""",
    "CASO-125": """### CASO-125 — Legalidad de cartas en Coconut beta\n\nEl reglamento beta de Coconut define la construcción del mazo y la victoria a 25 de lore, pero no define un pool de sets, rotación ni lista de prohibiciones propia. No se puede afirmar que todas las cartas sean legales por defecto: el organizador debe anunciar la legalidad concreta del evento hasta que Coconut publique una política específica.\n\nFundamento: [[01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md|Formato Coconut (Beta)]].""",
    "CASO-126": """### CASO-126 — Tiempo y estructura de un evento Coconut\n\nCoconut se publica como beta y no aporta rondas suizas, Top Cut ni un límite de tiempo de torneo. La tienda u organización debe fijar y anunciar la estructura, el tiempo y el procedimiento de emparejamientos. Una mesa abierta puede ser una opción práctica, pero no es una regla oficial del formato.\n\nFundamento: [[01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md|Formato Coconut (Beta)]].""",
    "CASO-128": """### CASO-128 — «Collection» no es una zona definida\n\nLa hoja beta de Coconut no define «collection» como zona de juego ni indica cuántas copias externas deben llevarse. La carta asociada puede incluirse hasta cuatro veces y el resto es singleton; cualquier Robin's Bow que entre legalmente en juego se comporta después como un objeto normal. El número de cartas externas necesarias es una decisión del organizador o una interpretación que debe acordarse antes del evento.\n\nFundamento: [[01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md|Formato Coconut (Beta)]].""",
    "CASO-129": """### CASO-129 — Ursula Coconut y Angel — Underdog\n\nAngel — Siren Singer tiene Singer 3. La habilidad Coconut de Ursula — Deceiver of All hace que los personajes cuenten como si tuvieran coste +1 al cantar, por lo que Angel cuenta como coste 4 para esa canción. La comprobación depende de usar los textos vigentes de ambas cartas; no se puede calcular con un resumen incompleto.\n\nFundamento: [[01. Reglas/9. Multijugador (Multiplayer)/Cartas Coconut de la beta.md|Cartas Coconut de la beta]] y el listado de cartas de Winterspell.""",
    "CASO-133": """### CASO-133 — Luisa con tres daños y sin otro personaje\n\nLa regla de Luisa — I Can Take It permite mover su propio daño tanto como sea posible cuando no existe otro personaje legal. La conclusión reglamentaria se mantiene aunque el relato de la retransmisión y la decisión arbitral concreta no estén verificados; esos hechos deben separarse y no citarse como precedente sin vídeo o acta.\n\nFundamento: artículo de Luisa — I Can Take It y reglas 1.9.2.4 y 6.7.2 de {CR}.""",
    "CASO-137": """### CASO-137 — Robin's Bow y «collection»\n\nUna vez que Robin's Bow está en juego es un objeto normal y You're Welcome puede barajarlo si el objetivo es legal. Lo que Coconut beta no define es cómo una carta de «collection» entra en juego y pasa a formar parte del estado de la partida. Esa zona inicial debe acordarse o documentarse antes de aplicar la interacción.\n\nFundamento: [[01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md|Formato Coconut (Beta)]].""",
}


def load_cases() -> dict[str, dict]:
    data = json.loads(VALIDATION.read_text(encoding="utf-8"))
    return {c["id"]: c for c in data["casos"]}


def build_article(entry: dict) -> str:
    sources = entry["foundation"]
    steps = "\n".join(f"{i}. {step}" for i, step in enumerate(entry["sequence"], 1))
    return (
        "## ❓ Duda\n\n"
        f"{entry['question']}\n\n---\n\n"
        "## ✅ Respuesta\n\n"
        f"{entry['answer']}\n\n---\n\n"
        "## 📘 Fundamento en reglas\n\n"
        f"- {sources}\n\n"
        "## 🔄 Secuencia oficial\n\n"
        f"{steps}\n\n---\n\n"
        "## 🏷️ Tags\n\n"
        f"{entry['tags']}\n"
    )


def update_managed_article(path: Path, entry: dict) -> None:
    """Actualiza solo la sección de tags de un artículo ya creado por este script."""
    if not path.exists():
        path.write_text(build_article(entry), encoding="utf-8")
        return
    text = path.read_text(encoding="utf-8")
    heading = "## 🏷️ Tags"
    if heading not in text:
        return
    before = text.split(heading, 1)[0].rstrip()
    path.write_text(before + "\n\n" + heading + "\n\n" + entry["tags"] + "\n", encoding="utf-8")


def append_expansion(path: Path, case_id: str) -> bool:
    text = path.read_text(encoding="utf-8")
    marker = f"### {case_id} —"
    if marker in text:
        return False
    if case_id not in EXPANSIONS:
        raise KeyError(f"No hay texto de ampliación para {case_id}")
    formatted = EXPANSIONS[case_id].format(CR=CR, TR=TR)
    first_line, *rest = formatted.splitlines()
    # El identificador solo se usa para idempotencia y no se publica en la wiki.
    visible_heading = first_line.split(" — ", 1)[1] if " — " in first_line else first_line
    if f"### {visible_heading}" in text:
        return False
    section = "\n\n---\n\n" + "\n".join([f"### {visible_heading}", *rest]) + "\n"
    path.write_text(text.rstrip() + section, encoding="utf-8")
    return True


def update_index(entries: list[dict]) -> None:
    text = INDEX.read_text(encoding="utf-8")
    block_start = "### Casos incorporados desde Discord (validación 72+26)"
    if block_start in text:
        before, rest = text.split(block_start, 1)
        stats_marker = "\n## 📊 Estadísticas"
        if stats_marker in rest:
            _, after = rest.split(stats_marker, 1)
            # Elimina el bloque antiguo completo, conservando todo lo que hay
            # antes y la tabla de estadísticas que lo sigue.
            text = before.rstrip() + "\n\n## 📊 Estadísticas" + after
    lines = [
        block_start,
        "",
        "> 15 casos revisados: 63 duplicados descartados, 20 ampliaciones y 14 artículos nuevos (dos casos de Limited comparten artículo).",
        "",
    ]
    for entry in entries:
        rel = entry["path"].replace("01. Reglas/11. Casos de ejemplo y aclaraciones/", "")
        lines.append(f"- [{entry['title']}](<{rel}>)")
    lines.extend(["", "#### Ampliaciones en artículos existentes", ""])
    for case_id, target in EXPANSION_TARGETS.items():
        rel = Path(os.path.relpath(ROOT / target, INDEX.parent)).as_posix()
        title = Path(target).stem
        lines.append(f"- [{title}](<{rel}>)")
    block = "\n".join(lines) + "\n\n"
    marker_stats = "## 📊 Estadísticas"
    if marker_stats in text:
        text = text.replace(marker_stats, block + marker_stats, 1)
    else:
        text += "\n" + block
    text = text.replace("**Total de casos:** 179", "**Total de casos:** 193", 1)
    text = text.replace("| **TOTAL**                        | **179** | **100%** |", "| **TOTAL**                        | **193** | **100%** |", 1)
    INDEX.write_text(text, encoding="utf-8")


def main() -> None:
    cases = load_cases()
    usable = [c for c in cases.values() if c["validacion"]["veredicto"] in {"correcta", "parcial"}]
    new_by_id = {case_id: entry for entry in NEW_ARTICLES for case_id in entry["ids"]}
    expansion_ids = set(EXPANSION_TARGETS)
    new_ids = set(new_by_id)
    duplicate_ids = sorted(c["id"] for c in usable if c["id"] not in expansion_ids and c["id"] not in new_ids)

    created = []
    for entry in NEW_ARTICLES:
        path = ROOT / entry["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        update_managed_article(path, entry)
        created.append(entry)

    expanded = []
    for case_id, target in EXPANSION_TARGETS.items():
        path = ROOT / target
        if not path.exists():
            raise FileNotFoundError(path)
        if append_expansion(path, case_id):
            expanded.append(case_id)

    update_index(NEW_ARTICLES)

    records = []
    for c in usable:
        cid = c["id"]
        if cid in duplicate_ids:
            decision = "duplicado_descartado"
            destinations = c["validacion"].get("fuentes_wiki", [])
        elif cid in expansion_ids:
            decision = "ampliacion"
            destinations = [EXPANSION_TARGETS[cid]]
        else:
            decision = "articulo_nuevo"
            destinations = [new_by_id[cid]["path"]]
        records.append(
            {
                "id": cid,
                "veredicto_validacion": c["validacion"]["veredicto"],
                "decision": decision,
                "destinos": destinations,
                "respuesta_corregida": (
                    new_by_id[cid]["answer"] if cid in new_by_id else EXPANSIONS.get(cid, "")
                ),
                "fuentes_wiki_antes": c["validacion"].get("fuentes_wiki", []),
            }
        )
    report = {
        "fecha": date.today().isoformat(),
        "fuente": "analisis/discord-2026-09-05/validacion_casos_102.json",
        "alcance": "72 correctas y 26 parciales; se excluyen incorrecta, desactualizada y pendientes",
        "resumen": {
            "casos_utilizados": len(usable),
            "duplicados_descartados": len(duplicate_ids),
            "ampliaciones": len(expansion_ids),
            "articulos_nuevos": len(NEW_ARTICLES),
            "casos_nuevos": len(new_ids),
            "articulos_incorporados": len(NEW_ARTICLES),
            "ampliaciones_incorporadas": len(expansion_ids),
        },
        "casos": records,
    }
    (OUT_DIR / "incorporacion_wiki.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    seleccionados = [r for r in records if r["decision"] != "duplicado_descartado"]
    seleccion = {
        "fecha": date.today().isoformat(),
        "fuente": "analisis/discord-2026-09-05/validacion_casos_102.json",
        "criterio": "Solo ampliaciones y artículos nuevos; se excluyen los 63 duplicados de la wiki.",
        "casos": seleccionados,
    }
    (OUT_DIR / "casos_para_wiki.json").write_text(json.dumps(seleccion, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# Incorporación de casos de Discord en la wiki",
        "",
        f"Fecha: {report['fecha']}",
        "",
        "Se procesan solo los 72 casos validados como correctos y los 26 parciales. CASO-098 (incorrecta), CASO-048 (desactualizada) y los pendientes quedan fuera.",
        "",
        "| Decisión | Casos | Composición | Resultado |",
        "| --- | ---: | --- | --- |",
        f"| Duplicado descartado | {len(duplicate_ids)} | 63 correctas | Ya cubierto por una página existente |",
        f"| Ampliación | {len(expansion_ids)} | 3 correctas + 17 parciales corregidas | Adenda añadida al artículo indicado |",
        f"| Artículo nuevo | {len(new_ids)} | 6 correctas + 9 parciales corregidas | {len(NEW_ARTICLES)} artículos; CASO-066 y CASO-102 se agrupan |",
        "",
        "## Duplicados descartados",
        "",
        ", ".join(duplicate_ids),
        "",
        "## Ampliaciones",
        "",
    ]
    for cid, target in EXPANSION_TARGETS.items():
        md.append(f"- **{cid}** → [{Path(target).stem}](<{target}>)")
    md += ["", "## Artículos nuevos", ""]
    for entry in NEW_ARTICLES:
        md.append(f"- **{', '.join(entry['ids'])}** → [{entry['title']}](<{entry['path']}>)")
    md += [
        "",
        "Las respuestas de los parciales se han convertido en conclusiones utilizables, conservando una limitación explícita cuando falta el anuncio del evento, el texto completo de una carta o una aclaración oficial. No se presenta una inferencia histórica como regla general.",
        "",
    ]
    (OUT_DIR / "INCORPORACION_WIKI.md").write_text("\n".join(md), encoding="utf-8")
    seleccion_md = [
        "# Casos que quedan para la wiki",
        "",
        "Este listado excluye los duplicados ya cubiertos por el índice. Incluye las ampliaciones y los artículos nuevos, con las parciales redactadas como conclusiones con alcance explícito.",
        "",
        "| Caso | Decisión | Destino |",
        "| --- | --- | --- |",
    ]
    for r in seleccionados:
        seleccion_md.append(f"| {r['id']} | {r['decision']} | {r['destinos'][0]} |")
    (OUT_DIR / "CASOS_PARA_WIKI.md").write_text("\n".join(seleccion_md) + "\n", encoding="utf-8")
    print(json.dumps(report["resumen"], ensure_ascii=False))


if __name__ == "__main__":
    main()
