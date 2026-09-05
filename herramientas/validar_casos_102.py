"""Contrasta los 102 casos claros de Discord con la documentación local.

La conversación de Discord se conserva como evidencia, pero no se trata como
fuente normativa. Cada entrada recibe un veredicto y referencias a las reglas
oficiales, a la wiki local o, cuando no es posible comprobarlo, una explicación
de la limitación.
"""

from __future__ import annotations

import json
from collections import Counter
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "analisis/discord-2026-09-05"
INPUT = OUT / "casos_claros.json"
OUTPUT_JSON = OUT / "validacion_casos_102.json"
OUTPUT_MD = OUT / "VALIDACION_CASOS.md"


def v(
    veredicto: str,
    comprobacion: str,
    oficiales: tuple[str, ...] = (),
    wiki: tuple[str, ...] = (),
    *,
    alcance: str = "regla_oficial",
    accion: str = "",
) -> dict:
    """Construye una validación pequeña y serializable."""
    cobertura = "localizada" if wiki else "no_localizada"
    return {
        "veredicto": veredicto,
        "alcance": alcance,
        "comprobacion": comprobacion,
        "fuentes_oficiales": list(oficiales),
        "fuentes_wiki": list(wiki),
        "cobertura_wiki": cobertura,
        "accion_recomendada": accion,
    }


CR = "Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf"
TR = "Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf"
COCONUT = "Documentacion Oficial/FormatCoconut_Rules.pdf"
COCONUT_CARDS = "Documentacion Oficial/FormatCoconut_BetaCoconutCards.pdf"
VINE = "Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf"

W = "01. Reglas/11. Casos de ejemplo y aclaraciones/"
TA = W + "11.0. Timing y Resolución/"
ZM = W + "11.2. Zonas y Movimientos/"
CO = W + "11.3. Costes y Requisitos/"
HA = W + "11.4. Habilidades/"
KW = W + "11.5. Keywords/"
IC = W + "11.6. Interacciones Complejas/"


VALIDACIONES: dict[str, dict] = {
    "CASO-001": v(
        "parcial",
        "La aplicación puede servir como consulta auxiliar, pero la legalidad y las prohibiciones deben comprobarse en las Tournament Rules y en el anuncio oficial vigente. La conversación mezcla un documento atrasado con una aplicación que también puede contener erratas.",
        (TR,),
        (),
        alcance="fuente_y_vigencia",
        accion="Documentar siempre el comunicado o la lista oficial que esté en vigor; no presentar la aplicación como autoridad única.",
    ),
    "CASO-002": v("correcta", "Varios efectos de reemplazo solo pueden competir cuando modifican el mismo acontecimiento; acontecimientos distintos no son simultáneos. La respuesta del canal es correcta en ese sentido.", (CR,), (TA + "Interacción entre efectos de reemplazo y habilidades disparadas con requisitos.md",)),
    "CASO-003": v("correcta", "El jugador activo realiza primero las elecciones y revelados de su parte; después continúa el orden de turno. La información ya revelada es pública para la elección siguiente.", (CR,), (TA + "Qué pasa cuando se juegan dos cartas a la vez.md", TA + "Prioridad entre jugador activo y no activo.md")),
    "CASO-004": v("correcta", "Preparado/agotado y seco/secándose son estados independientes. Secándose impide las acciones que exigen estar seco, pero no toda interacción con la carta.", (CR,), (KW + "Heredar una palabra clave al hacer shift.md",), accion="Mantener separados los términos preparado y seco en la redacción de la wiki."),
    "CASO-005": v("correcta", "En el final del turno se añaden y resuelven primero las habilidades de final de turno; después expiran los efectos que duran hasta el final del turno y se hace la comprobación de estado.", (CR,), (TA + "Habilidades disparadas 'Al final del turno'.md", TA + "Orden de resolución en habilidades disparadas.md")),
    "CASO-006": v("correcta", "La habilidad de Cinderella Stouthearted debe estar funcionando cuando se canta la canción. Jugarla después no retroactiva el canto anterior.", (CR,), (HA + "Habilidades estáticas presentes en juego y sus interacciones.md",)),
    "CASO-007": v("correcta", "Bodyguard crea una restricción de elección: si un personaje con Bodyguard preparado es una opción legal, debe ser el objetivo del desafío cuando el efecto permite desafiar personajes preparados.", (CR,), (KW + "Bodyguard.md",)),
    "CASO-008": v("correcta", "Resist reduce daño que se va a infligir al personaje o localización; mover contadores de daño no es infligir daño y no se reduce con Resist.", (CR,), (IC + "Mover daño no es retirar daño.md",)),
    "CASO-009": v("correcta", "La acción jugada por Robin se resuelve después de terminar el efecto inicial que pone las demás cartas en el descarte. Firefly Swarm comprueba entonces su condición con el descarte actualizado.", (CR,), (CO + "Firefly Swarm con Robin Hood - Sharpshooter sí habilita el segundo modo.md",)),
    "CASO-010": v("parcial", "La tabla de Core de las Tournament Rules respalda el conjunto de sets legal en la fecha de la regla, pero no demuestra por sí sola las instrucciones históricas del campeonato concreto de Wilds Unknown ni sus fechas. La respuesta necesita el kit o anuncio de ese evento.", (TR,), (), alcance="historico", accion="Conservar la conclusión de Core como provisional y adjuntar el anuncio del campeonato antes de publicarla."),
    "CASO-011": v("correcta", "El valor actual de Fuerza se obtiene combinando todos los modificadores; la habilidad de Elisa fija un mínimo basado en la Fuerza impresa sin borrar la reducción de Jessie.", (CR,), (IC + "Elisa Maza - Forever Strong y reducciones de Fuerza previas.md",)),
    "CASO-012": v("correcta", "Se puede activar Boost aunque la resolución posterior no pueda completarse. Si no hay un personaje rival que pueda recibir el daño, no existe movimiento válido y el daño de origen permanece.", (CR,), (TA + "Resolución parcial sin objetivo válido.md", IC + "Mover daño no es retirar daño.md")),
    "CASO-013": v("correcta", "Cada jugador ordena sus propias habilidades disparadas en la bolsa; el jugador activo no ordena arbitrariamente las del rival.", (CR,), (TA + "Orden de resolución en habilidades disparadas.md", TA + "Múltiples habilidades a la vez.md")),
    "CASO-014": v("parcial", "Las listas son exigibles en eventos Competitive/Premier cuando lo indican las Tournament Rules o el kit. La regla no exige efectuar un deck check a todos los jugadores: establece comprobaciones donde sea posible y una expectativa mínima para Premier.", (TR,), (), alcance="torneo", accion="Separar obligación de lista, presencia de juez y muestreo de deck checks."),
    "CASO-015": v("correcta", "La habilidad de Merida se dispara durante el desafío y se resuelve antes del paso de daño. Si destierra al atacante, el paso de daño no llega a producirse.", (CR,), (TA + "Boo - Energetic Child destierra antes del daño del desafío.md", IC + "Merida frente a Lilo y Rapunzel - infligir daño no es recibir daño.md")),
    "CASO-016": v("pendiente", "El supuesto ajuste de Carde.io no está descrito en la documentación local ni se puede verificar con el texto del JSON; la respuesta del canal reconoce que no se ha probado.", (), (), alcance="herramienta_externa", accion="Comprobarlo en una cuenta de organización o retirar la afirmación operativa."),
    "CASO-017": v("parcial", "En un nuevo enfrentamiento de Top Cut de Premier, el seed más alto de la fase suiza elige quién juega primero en la primera partida; en las partidas siguientes elige quien perdió la partida anterior. El alcance puede variar si el evento es Competitive y el kit establece otra regla.", (TR,), (), alcance="torneo", accion="Añadir el nivel y el kit del evento antes de convertirlo en regla general."),
    "CASO-018": v("parcial", "La tabla de Tournament Rules asigna 5 rondas suizas y Top 8 a 17–32 jugadores. El análisis de Top 4 y sus combinaciones depende de supuestos matemáticos que no sustituyen la tabla ni autorizan cambiar un Set Championship.", (TR,), (IC + "Set Championship con 65 jugadores o más.md",), alcance="torneo", accion="Usar la tabla oficial y pedir autorización expresa para cualquier estructura distinta."),
    "CASO-020": v("correcta", "Luisa puede mover su propio daño: el efecto se hace tanto como sea posible y no exige que exista otro personaje propio. La comprobación de estado se realiza después de resolver el efecto.", (CR,), (IC + "Luisa Madrigal - I Can Take It, condición Then-if y GSC.md", IC + "Luisa Madrigal - I Can Take It, llega a 4 daños y no se destierra.md")),
    "CASO-021": v("correcta", "El disparo de Syndrome's Remote entra en la bolsa aunque ocurra en el turno rival. Buzz's Arm solo ofrece un coste alternativo para jugar un objeto; hace falta una ventana legal para jugarlo.", (CR,), (TA + "Disparar habilidades mientras se resuelve una carta.md", CO + "Jugar una carta con shift reduciendo su coste (incluso gratis).md")),
    "CASO-022": v("correcta", "La condición de Escape Plan se comprueba al jugar la carta. Que el efecto vaya a producir la segunda carta en el descarte no satisface una condición que exige que ya haya dos.", (CR,), (CO + "Escape Plan con acción gratis al questear.md",)),
    "CASO-024": v("correcta", "GRE se usa en la guía de correcciones como General Rules Error (Error general de reglas). Es una categoría de infracción, no una regla de juego.", (), ("04. Guia de correccion de jugadas/02. Errores de reglas/2.4 Error general de reglas (General Rule Error).md", "04. Guia de correccion de jugadas/05. Consejos generales/Causa raíz y corrección apropiada (GRE).md"), alcance="arbitraje"),
    "CASO-026": v("correcta", "El propio registro aclara la aparente duplicación: una carta vuelve a la mano y solo la otra es el robo de Diablo. No queda una interacción de reglas pendiente.", (CR,), (), alcance="autocorreccion"),
    "CASO-028": v("correcta", "Shift crea una pila y la carta que queda debajo sigue siendo una carta under, con independencia de que se colocara mediante Shift o Boost.", (CR,), (TA + "Cartas en una pila.md", HA + "Shift y Webby's Diary - diferencia entre encima y debajo.md")),
    "CASO-029": v("parcial", "Los permisos de entintar adicionales son efectos separados y se acumulan si ambos proceden de cartas identificadas. El nombre incompleto «sails» impide comprobar el texto exacto y sus restricciones.", (CR,), (), accion="Identificar la carta completa antes de publicar una respuesta definitiva."),
    "CASO-031": v("correcta", "La reducción de Grandmother Willow se aplica al coste de tinta para jugar el siguiente personaje; no reduce el coste de una habilidad activada de Finnick.", (CR,), (CO + "Reducciones de coste apiladas - Akood et Emuti y Grandmother Willow.md",)),
    "CASO-035": v("correcta", "Under the Sea comprueba la Fuerza modificada en el momento de resolver. Una reducción que deja al personaje en 2 o menos lo hace elegible.", (CR,), (ZM + "Under the Sea y reordenación de pilas al mazo.md",)),
    "CASO-037": v("correcta", "Una descalificación de un evento no equivale por sí sola a una prohibición general del recinto o de otros eventos. Esa extensión requiere una medida de elegibilidad separada del organizador.", (TR,), (), alcance="torneo"),
    "CASO-039": v("correcta", "Las cartas que salen de juego simultáneamente se ven como un único conjunto al comprobar las habilidades que observan el evento. Sid puede haber disparado su habilidad aunque después esté en el descarte.", (CR,), (IC + "GSC y habilidades que dañan.md", ZM + "Desterrar y volver a la mano desde la zona de juego.md")),
    "CASO-040": v("parcial", "La prohibición de representar numéricamente información de Fuerza/Voluntad en fichas está respaldada por las reglas de torneo. La sugerencia del canal de usar papeles con números es incorrecta; deben ser marcadores no numéricos y no confundirse con daño.", (TR,), (IC + "Fichas de recordatorio sobre el mazo.md",), alcance="torneo", accion="Conservar la prohibición y eliminar la recomendación de papeles o fichas numéricas."),
    "CASO-042": v("correcta", "Enderezar un personaje durante el desafío no elimina el desafío ni evita el cálculo de daño. El personaje puede estar preparado cuando recibe el daño.", (CR,), (TA + "Ming Lee - Giant Red Panda sigue en el desafío al enderezarse.md",)),
    "CASO-048": v("desactualizada", "La respuesta sobre que aún no estaba documentado el procedimiento quedó superada: Tournament Rules 6.11 §5.5 exige mantener boca arriba la carta entintada por la acción normal durante el turno y ponerla boca abajo al final.", (TR,), (), alcance="vigencia", accion="Sustituir la respuesta histórica por la regla vigente y conservar la fecha solo como contexto."),
    "CASO-049": v("correcta", "Un dado que muestra el tamaño de la mano es una representación numérica de información privada y no está permitido como marcador. Se puede pedir que se retire y llamar al juez.", (TR,), (IC + "Fichas de recordatorio sobre el mazo.md",), alcance="torneo"),
    "CASO-051": v("correcta", "Los jugadores no pueden autorizar por sí solos un takeback. La excepción debe evaluarla y aprobarla el Lore Guide conforme a los criterios de la regla de takebacks.", (TR,), ("01. Reglas/10. Artículos/Reversión de jugadas (takebacks).md",)),
    "CASO-052": v("correcta", "Un personaje con dos nombres de equipo conserva ambos nombres y sigue siendo un solo personaje. One and Only compara nombres, por lo que un equipo coincide con sus nombres individuales; no concede todos los nombres de una familia por asociación temática.", (CR,), (HA + "One and Only compara el nombre sin la versión.md",)),
    "CASO-054": v("correcta", "Los marcadores con símbolos no numéricos pueden recordar una modificación si son claros y no se confunden con daño. La prohibición alcanza a los valores +1, −1, −3, etc.", (TR,), (IC + "Fichas de recordatorio sobre el mazo.md",), alcance="torneo"),
    "CASO-055": v("correcta", "Descartar Look What You've Done es parte del coste de Shift. El Shift se completa; después la habilidad disparada permite jugar la acción desde el descarte y el efecto de la acción se resuelve en su momento.", (CR, VINE), (ZM + "Look What You've Done no se dispara al terminar de resolverse.md", KW + "Temporary Shift funciona aunque quede en medio de la pila.md")),
    "CASO-056": v("correcta", "Una acción que termina de resolverse y se coloca en el descarte no se está descartando desde la mano. Ese movimiento no vuelve a disparar una condición que exige descartar una carta.", (CR, VINE), (ZM + "Look What You've Done no se dispara al terminar de resolverse.md",)),
    "CASO-058": v("parcial", "La regla permite tratar varias acciones inmediatas como una jugada agrupada para una secuencia fuera de orden cuando no se obtuvo información nueva, pero siempre requiere evaluación del Lore Guide. La fecha histórica de Milwaukee no está verificada en la documentación local.", (TR,), ("01. Reglas/10. Artículos/Reversión de jugadas (takebacks).md",), alcance="torneo", accion="Publicar la regla práctica sin afirmar la fecha hasta localizar el anuncio original."),
    "CASO-062": v("parcial", "Bruno nombra un nombre de carta y un equipo sigue siendo un personaje con varios nombres. La conclusión general es correcta; la anomalía concreta de Hamish, Hubert & Harris depende de la redacción de esa carta y del CRD aplicable.", (CR,), (), accion="Comprobar el texto vigente de Hamish, Hubert & Harris antes de fijar el ejemplo."),
    "CASO-063": v("parcial", "Un pase de turno puede rebobinarse solo si el Lore Guide considera que se cumplen los criterios de takeback; una habilidad opcional olvidada y la información obtenida son hechos decisivos. No es una autorización general ni una jugada agrupada automática.", (TR,), ("01. Reglas/10. Artículos/Reversión de jugadas (takebacks).md",), alcance="torneo", accion="Registrar el caso como decisión arbitral dependiente de hechos."),
    "CASO-064": v("correcta", "Bodyguard solo obliga a escoger ese personaje si el rival puede desafiarlo legalmente. Powhatan's Staff añade por separado la opción de entrar agotado; ninguna de las dos cosas impide todos los desafíos sin un atacante legal.", (CR,), (KW + "Bodyguard.md",)),
    "CASO-065": v("correcta", "La derrota por mazo vacío se comprueba al final del turno del jugador cuyo mazo está vacío. Las comprobaciones de estado se hacen en el orden de la fase: una victoria por lore alcanzada antes termina la partida antes de esa derrota.", (CR,), (TA + "Derrota, timing mazo vacío.md", IC + "GSC y el final de partida.md")),
    "CASO-066": v("parcial", "Las Comprehensive/Tournament Rules permiten reglas de construcción comunicadas para Limited, pero no fijan aquí un sideboard universal entre partidas o rondas. La respuesta histórica describe práctica de organizador, no una obligación normativa.", (TR,), (), alcance="torneo", accion="Seguir la regla anunciada por el organizador y conservar separadas las prácticas de cada evento."),
    "CASO-067": v("parcial", "La regla de prize splitting permite repartir premios disponibles en Entry/Competitive si todos los jugadores restantes aceptan y no se intercambia el resultado. No permite contraprestaciones por conceder ni decidir un resultado al azar; el alcance Premier y los objetos concretos dependen del nivel y del premio anunciado.", (TR,), ("04. Guia de correccion de jugadas/04. Conducta antideportiva/4.5 Resultado de un encuentro inapropiado (Improper Match Result).md",), alcance="torneo", accion="Separar reparto de premios, concesión, venta posterior y apuestas en subcasos distintos."),
    "CASO-068": v("correcta", "Mover daño exige un origen y un destino legales. Si no existe destino rival, el movimiento completo no ocurre y no se retira el daño de Cheshire.", (CR,), (IC + "Mover daño no es retirar daño.md",)),
    "CASO-070": v("parcial", "La regla vigente aclara que las modificaciones de cómo una carta entra en juego se resuelven junto con el juego de la carta y no son efectos de reemplazo. La respuesta del canal no desarrolla qué ocurre cuando ambos modificadores se aplican, por lo que queda incompleta.", (CR,), (HA + "Habilidades estáticas presentes en juego y sus interacciones.md",), accion="Añadir una secuencia que aplique conjuntamente los dos modificadores concretos."),
    "CASO-071": v("correcta", "Under the Sea permite poner las cartas en el fondo en cualquier orden; quien controla el efecto organiza las pilas y la información de las cartas boca arriba debe ser conocida por todos.", (CR,), (ZM + "Under the Sea y reordenación de pilas al mazo.md",)),
    "CASO-072": v("correcta", "Las fundas de torneo deben tener reverso completamente opaco, no reflectante, sin daños ni marcas que permitan distinguir cartas. «Matte» describe textura y no garantiza opacidad.", (TR,), (), alcance="torneo"),
    "CASO-073": v("pendiente", "El texto conserva una URL recuperada de una versión anterior, pero la documentación local no identifica qué documento debía enlazarla ni verifica que el vídeo siga disponible. No puede certificarse como enlace vigente.", (), (), alcance="documental", accion="Comprobar el documento de origen y la URL antes de enlazarla en la wiki."),
    "CASO-075": v("correcta", "Bodyguard no contiene una opción de entrar agotado. Esa opción procede del texto de Powhatan's Staff y no se hereda por ganar la palabra clave.", (CR,), (KW + "Bodyguard.md",)),
    "CASO-076": v("correcta", "Duo Shift exige dos personajes distintos como bases. Morph puede cubrir una de las identidades, pero un único equipo sigue siendo un solo personaje y no satisface ambas bases por sí solo.", (CR, VINE), (KW + "Mickey Mouse & Minnie Mouse necesita dos personajes para Duo Shift.md", KW + "Morph - Little Imitator funciona con todas las variantes de Shift.md")),
    "CASO-077": v("correcta", "Entrar agotado no es una transición que dispare una habilidad «whenever this character exerts». La carta que Scrooge pone debajo llega por una habilidad posterior de la bolsa, no como parte de la entrada inicial de Bambi.", (CR,), (TA + "Habilidades disparadas 'Al final del turno'.md", KW + "Bambi – Ethereal Faun cantando una canción.md")),
    "CASO-078": v("correcta", "Jugar una canción mediante el efecto de Dash no significa que deba pagarse gratis: el jugador puede usar el coste alternativo de cantar y agotar otros personajes que cumplan el requisito.", (CR,), (CO + "Cantar o jugar gratis cuenta como pagar 0 tinta.md", IC + "Acción jugada debido a un efecto de otra carta.md")),
    "CASO-079": v("correcta", "Un personaje de equipo posee sus nombres individuales. Hades o Vine Pod pueden comprobar uno de esos nombres y jugar el personaje de equipo si el resto del efecto es legal.", (CR,), (ZM + "Ursula - Deal Maker solo puede elegir un personaje en juego.md",)),
    "CASO-080": v("correcta", "Fragile as a Flower puede elegir un personaje ya agotado si cumple el coste; el texto no exige que esté preparado ni condiciona la siguiente parte a haberlo preparado.", (CR,), (HA + "Enderezar un personaje.md",)),
    "CASO-082": v("correcta", "Secándose solo impide quest, challenge y costes/efectos que exigen el símbolo de agotar. Una habilidad sin ese requisito puede usarse durante el mismo turno en que entra.", (CR,), (HA + "Performance Review y secado - cuando puedes agotar.md",)),
    "CASO-084": v("parcial", "Las reglas de torneo y conducta permiten sancionar nombres ofensivos o inapropiados, pero no hay una regla local que resuelva el nombre concreto «circle herc». La respuesta general es válida y la decisión concreta queda al organizador/Lore Guide.", (TR,), (), alcance="torneo", accion="No presentar el nombre concreto como aprobado sin una decisión documentada."),
    "CASO-086": v("correcta", "Temporary Shift crea una habilidad retrasada que comprueba si la carta sigue en la zona de juego al final del turno. Que otra carta la cubra o quede encima no la saca de esa zona.", (CR, VINE), (KW + "Temporary Shift funciona aunque quede en medio de la pila.md",)),
    "CASO-087": v("correcta", "El final del turno sigue siendo parte del turno del jugador activo hasta que termina la fase. Una habilidad que dice «during your turn» puede aplicarse antes de ese momento.", (CR,), (TA + "Habilidades disparadas 'Al final del turno'.md",)),
    "CASO-088": v("parcial", "La parte de Potato jugado este turno es clara: preparar el objeto no cambia que no estuviera en juego al comienzo del turno, por lo que el personaje entra secándose. La interacción Morph/Potato combina la herencia de estado de Shift con la regla especial de Potato y el propio canal reconoce una ambigüedad de redacción.", (CR, VINE), (KW + "Morph - Little Imitator funciona con todas las variantes de Shift.md", IC + "Posey - Vampire Potato puede usar Potato Shift sobre Morph.md"), accion="Mantener la variante Morph como pendiente de aclaración oficial y publicar solo la parte inequívoca."),
    "CASO-089": v("parcial", "Resist reduce el daño que recibe el objetivo a cero, pero el efecto de origen sigue siendo un efecto que inflige daño. La conclusión sobre daño base/recibido es correcta; la cantidad exacta que reproduce Mulan depende del texto de esa carta y no queda resuelta por el debate.", (CR,), (HA + "Escudos (replacement) vs Resist.md", HA + "Merida - Steady Aim y Resist.md"), accion="Separar la regla general de Resist de la interpretación específica de Mulan."),
    "CASO-093": v("correcta", "Cuando Resist reduce el daño a cero, el personaje no toma daño. Por tanto no se consume la protección de Lilo que reemplaza daño que se recibiría.", (CR,), (KW + "Lilo - Bundled Up y Malicious, Mean, and Scary.md", HA + "Escudos (replacement) vs Resist.md")),
    "CASO-094": v("correcta", "Source of the Vine contiene una elección obligatoria con una opción de pago. El controlador debe anunciarla y ambos jugadores deben mantener el estado correcto; no se puede inferir que el rival rechazó pagar por silencio.", (TR, CR), (), alcance="torneo"),
    "CASO-095": v("correcta", "La condición de John Smith pregunta si algún personaje de ese jugador desafió durante el turno. El desafío es un evento ya ocurrido; que el personaje que desafió sea desterrado después no convierte el evento en «ningún desafío». Por eso no se gana el lore en el supuesto descrito.", (CR,), (ZM + "Desterrar y volver a la mano desde la zona de juego.md",), accion="Usar siempre el texto exacto de John Smith – Snow Tracker; no confundirlo con John Smith – Undaunted Protector."),
    "CASO-096": v("correcta", "El CRD no tiene una entrada separada para cada combinación de cartas. Se aplican las reglas generales de reemplazos, daño, habilidades y el texto de cada carta; si persiste una duda concreta decide el Lore Guide.", (CR,), (HA + "Aplicación de múltiples efectos de reemplazo (Escudos).md",)),
    "CASO-098": v("incorrecta", "Una carta debajo de The Black Cauldron no está en juego, por lo que Belle no puede usar desde ahí su habilidad WHAT A MESS para desterrar el objeto. Si el Caldero es desterrado, las cartas de la pila pasan al descarte; eso no crea por sí solo un permiso para jugar Belle desde el descarte. El Caldero sí permite jugarla desde debajo mientras permanece en juego mediante RISE AND JOIN ME!.", (CR,), (CO + "Scrooge McDuck - Resourceful Miser desde The Black Cauldron.md", ZM + "Hide Away sobre The Black Cauldron con Hades debajo.md", "02. Listado de Cartas/Set 7 - Archazia''s Island.md", "02. Listado de Cartas/Set 10 - Whispers in the Well.md"), accion="Corregir la respuesta del canal y especificar qué efecto adicional, si lo hay, permite jugar la carta desde el descarte."),
    "CASO-099": v("correcta", "El coste de Scream Canister se puede pagar aunque no haya un personaje rival elegible. En la resolución se agotan las cartas de tinta y se hace la parte del objetivo hasta donde sea posible; no se crea un objetivo ilegal.", (CR,), (TA + "Resolución parcial sin objetivo válido.md",), accion="Conservar la distinción entre pagar el coste y resolver una elección sin objetivo."),
    "CASO-100": v("correcta", "«Then» ordena los efectos dentro de la misma resolución, pero no crea una comprobación de estado intermedia. Windstorm termina su efecto completo antes de la comprobación que pueda desterrar personajes por daño.", (CR,), (TA + "Qué pasa cuando se juegan dos cartas a la vez.md", HA + "Let The Storm Rage On sobre Angel - Experiment 624.md")),
    "CASO-101": v("correcta", "Al mover una pila a una zona, el propietario puede ordenar sus cartas salvo que el efecto indique otra cosa. Las cartas boca arriba y las pilas se mantienen conocidas según las reglas de zonas y del efecto que las mueve.", (CR,), (TA + "Cartas en una pila.md", ZM + "Under the Sea y reordenación de pilas al mazo.md")),
    "CASO-102": v("parcial", "No hay una regla general local que conceda sideboard entre partidas de Limited. El organizador debe anunciar la construcción y cualquier cambio permitido; una práctica habitual no es una obligación reglamentaria.", (TR,), (), alcance="torneo", accion="Conservar la norma comunicada por el organizador y no generalizar la práctica de una tienda."),
    "CASO-103": v("parcial", "Las clasificaciones pertenecen a cada carta concreta y no se transfieren por compartir personaje. La parte sobre Hunny es correcta si se refiere a la errata de Pooh – Hunny Wizard; la aplicación desactualizada no es prueba suficiente de la errata.", (CR,), (HA + "Winnie the Pooh - Hunny Archmage cuenta otra copia como other Hunny.md",), accion="Citar la errata o fuente de carta vigente junto a la regla de que las versiones son cartas distintas."),
    "CASO-104": v("correcta", "Shift conserva el daño de la pila. Tras jugar la nueva carta se comprueba el estado: si el daño acumulado es igual o superior a su Voluntad, el personaje es desterrado.", (CR,), (KW + "Heredar una palabra clave al hacer shift.md", IC + "GSC y el final de partida.md")),
    "CASO-105": v("correcta", "Fuerza 0 significa que el personaje no inflige daño durante el desafío; no hay daño que consumiría Act of Kindness. Esto es distinto de infligir daño y que Resist lo reduzca después.", (CR,), (IC + "Rapunzel conserva su protección si Resist reduce el daño a 0.md", IC + "Rapunzel – Act of Kindness y mover daño.md")),
    "CASO-107": v("correcta", "La entrada agotada que impone Horned King o el efecto propio de Lilo se aplica al jugarla desde el descarte. La comparación con el vídeo de Merida no cambia el texto de Lilo ni exige una segunda entrada agotada.", (CR,), (IC + "Horned King - Toca descarte antes de volver a mano.md",)),
    "CASO-108": v("correcta", "Al alterar la mano inicial, el jugador que empieza lo hace primero y los demás siguen el orden de turno. No se espera a que todos elijan simultáneamente.", (CR,), (TA + "Prioridad entre jugador activo y no activo.md",)),
    "CASO-109": v("correcta", "La habilidad disparada de Rapunzel & Flynn Rider se añade a la bolsa tras el descarte y se resuelve antes del paso de daño que aún no haya ocurrido. Puede jugar el personaje en esa ventana si es legal.", (CR,), (IC + "Lyle Tiberius Rourke y Rapunzel & Flynn Rider.md", TA + "Disparar habilidades mientras se resuelve una carta.md")),
    "CASO-110": v("correcta", "Un equipo con dos nombres de personaje tiene tres nombres relevantes (los dos individuales y el nombre del equipo) y basta una coincidencia textual cuando el efecto pide un nombre. Vine Pod debe seguir además sus costes y objetivos propios.", (CR,), (HA + "One and Only compara el nombre sin la versión.md",)),
    "CASO-111": v("correcta", "La palabra «next» identifica el siguiente personaje que se juegue y la reducción se consume en ese primer juego legal, incluso si un efecto lo juega gratis.", (CR,), (CO + "Reducciones de coste apiladas - Akood et Emuti y Grandmother Willow.md", CO + "Jugar carta sin objetivo válido.md")),
    "CASO-113": v("correcta", "Los modificadores se combinan: 0 − 2 + 5 = 3 de Fuerza durante el desafío. Challenger solo se aplica mientras Iago está desafiando.", (CR,), (IC + "Cálculo de fuerza con Tiana y Desafiador.md",)),
    "CASO-114": v("correcta", "La regla de las Comprehensive Rules describe el entintado normal boca abajo; Tournament Rules §5.5 añade el procedimiento de torneo temporal de mantener la carta boca arriba durante el turno y girarla al final.", (CR, TR), (), alcance="torneo"),
    "CASO-115": v("correcta", "La restricción estática de Peter Pan impide ganar lore por efectos mientras se aplica, pero deja de aplicarse al declararse un desafío legal. Super Goof gana el lore de su habilidad en ese momento.", (CR,), (HA + "No poder ganar lore por efecto estático.md",)),
    "CASO-116": v("correcta", "La habilidad de Pocahontas se creó al jugarla y no dice que dependa de que permanezca en juego. Red Alert puede retirar la fuente y la prohibición temporal sigue vigente.", (CR,), (ZM + "Fuente estática abandona el juego.md",)),
    "CASO-117": v("correcta", "Infligir daño, mover contadores de daño y poner contadores de daño son eventos distintos. Hercules solo reacciona al evento que su texto describe como daño infligido.", (CR,), (IC + "Mover daño no es retirar daño.md", IC + "GSC y habilidades que dañan.md")),
    "CASO-118": v("correcta", "Una Enchanted es una versión oficial de la carta, no una carta con arte alterado por un jugador. Puede usarse si cumple legalidad y no es distinguible; grosor, curvatura o marcas pueden hacerla ilegal.", (TR,), (IC + "Legalidad de cartas firmadas.md",), alcance="torneo"),
    "CASO-119": v("parcial", "Touch the Sky no usa una elección «chosen» en su texto actual, por lo que no satisface una condición que exige elegir. La variante hipotética sobre mover un rival y Ward no es una regla aplicable a la carta impresa.", (CR,), (TA + "Qué pasa cuando se juegan dos cartas a la vez.md",), accion="Mantener separada la carta impresa de cualquier redacción hipotética."),
    "CASO-120": v("correcta", "Ward solo impide que los oponentes elijan la carta. Su propietario puede elegir un personaje propio con Ward siempre que el efecto lo permita.", (CR,), (HA + "Habilidades estáticas presentes en juego y sus interacciones.md",)),
    "CASO-122": v("correcta", "La respuesta describe la disponibilidad de un recurso comunitario y no una regla: el autor no tenía guías recientes escritas y ofrecía vídeos de interacciones. Es correcta como estado de ese recurso, no como fuente oficial.", (), (), alcance="recurso_comunitario"),
    "CASO-123": v("correcta", "Al jugar la segunda Violet se generan los disparos aplicables de Merida y de las Violet. La Violet que queda debajo sigue siendo la fuente que ve jugar a la nueva antes de que la pila se cubra.", (CR,), (TA + "Disparar habilidades mientras se resuelve una carta.md", KW + "Dash Parr & Violet Parr combina los estados con Combo Shift.md")),
    "CASO-124": v("parcial", "Rechazar una opción «may» no cuenta como usarla. La regla de «once» respalda el principio, pero la conversación lo extrapola a «twice» sin una cita directa; debe comprobarse la redacción concreta de Tod.", (CR,), (ZM + "Tod + You Came Back y habilidades en el Bolsa.md",), accion="Publicar la conclusión solo junto al texto exacto de Tod o una aclaración oficial."),
    "CASO-125": v("parcial", "El reglamento de Coconut beta define construcción y victoria a 25 lore, pero no define legalidad de sets, rotación ni prohibiciones propias. Por eso no se puede afirmar normativamente que todas las cartas sean legales sin una decisión del organizador.", (COCONUT, COCONUT_CARDS), ("01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md",), alcance="formato_beta", accion="Tratar la legalidad como regla anunciada para cada evento hasta que Coconut publique una política propia."),
    "CASO-126": v("parcial", "Coconut se publica como beta y no aporta rondas suizas ni límite de tiempo de torneo. La estructura abierta y el tiempo son decisiones de la tienda/organizador, no una regla oficial del formato.", (COCONUT,), ("01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md",), alcance="formato_beta"),
    "CASO-128": v("parcial", "En Coconut la carta asociada puede aparecer hasta cuatro veces y el resto del mazo es singleton. «Collection» no es una zona definida por el reglamento; llevar Robin's Bow adicional es una interpretación de la habilidad, no una obligación general del formato.", (COCONUT, COCONUT_CARDS), ("01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md",), alcance="formato_beta", accion="Citar el texto exacto de la habilidad Coconut antes de fijar cuántos objetos externos se necesitan."),
    "CASO-129": v("parcial", "La habilidad Coconut de Ursula modifica el coste que cuentan los personajes al cantar, pero el resumen no conserva el texto completo de Ursula ni el coste de Angel. El resultado 4 es plausible solo después de verificar ambos textos.", (COCONUT, COCONUT_CARDS), ("01. Reglas/9. Multijugador (Multiplayer)/Cartas Coconut de la beta.md",), alcance="formato_beta", accion="Añadir los textos de Ursula Coconut y Angel – Underdog al caso."),
    "CASO-130": v("correcta", "Cada John Smith es un objetivo legal independiente para Red Alert. La restricción de uno no elimina al otro ni obliga a considerar que ambos sean un único personaje.", (CR,), (IC + "John Smith - Do your worst y restricción de elección.md",)),
    "CASO-131": v("correcta", "Cantar paga un coste alternativo de 0 tinta, pero la carta conserva su coste impreso para efectos que miran el coste de la carta; Jessie comprueba la cantidad de tinta pagada según su texto. Las reducciones que dejan el pago en 2 o menos satisfacen la condición.", (CR,), (CO + "Cantar o jugar gratis cuenta como pagar 0 tinta.md",)),
    "CASO-132": v("correcta", "En la redacción hipotética, la segunda cláusula depende de haber elegido primero un personaje rival. Sin objetivo legal no se puede realizar esa primera elección ni su efecto condicional posterior.", (CR,), (TA + "Resolución parcial sin objetivo válido.md",), alcance="hipotetico"),
    "CASO-133": v("parcial", "Con tres daños y sin otro personaje, la regla de Luisa permite mover su propio daño tanto como sea posible. Lo que no está verificado es el relato de la retransmisión y la decisión arbitral concreta.", (CR,), (IC + "Luisa Madrigal - I Can Take It, condición Then-if y GSC.md",), alcance="incidente_arbitral", accion="Separar la conclusión reglamentaria del incidente hasta disponer del vídeo o acta."),
    "CASO-134": v("correcta", "Ursula – Voice Stealer requiere un personaje rival preparado para poder agotarlo y conocer su coste. Si el único rival está agotado, no se realiza esa elección y la cláusula posterior no tiene personaje «the exerted character» al que referirse.", (CR,), (ZM + "Ursula - Deal Maker solo puede elegir un personaje en juego.md",)),
    "CASO-135": v("correcta", "En el texto real de Milo, la opción de descartar y devolver está vinculada: si se elige descartar, hay que devolver un personaje elegible. Si Milo es el único objetivo legal, puede devolverse a sí mismo.", (CR,), (TA + "Resolución parcial sin objetivo válido.md", IC + "John Smith - Obligado elegir si objetivo válido.md")),
    "CASO-136": v("correcta", "Un efecto que dice «remove up to» puede elegir un personaje sin daño y retirar cero; la elección solo sería ilegal si el texto exigiera expresamente un personaje dañado. La condición de John Smith no añade Ward contra su propietario.", (CR,), (HA + "Habilidades y sus efectos.md",)),
    "CASO-137": v("parcial", "Una vez que Robin's Bow está en juego es un objeto normal y You're Welcome puede barajarlo si es un objetivo legal. Lo no definido por Coconut es cómo una carta de la «collection» entra en juego y pasa a ser una carta del juego.", (CR, COCONUT, COCONUT_CARDS), ("01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md",), alcance="formato_beta", accion="Acordar o documentar la zona inicial de las cartas de collection antes de aplicar esta interacción."),
}


def main() -> None:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    cases = data["casos"]
    ids = {case["id"] for case in cases}
    missing = ids - VALIDACIONES.keys()
    extra = VALIDACIONES.keys() - ids
    if missing or extra or len(cases) != 102:
        raise SystemExit(f"Casos inesperados: faltan={sorted(missing)} sobran={sorted(extra)} total={len(cases)}")

    validated_cases = []
    for case in cases:
        enriched = deepcopy(case)
        enriched["validacion"] = VALIDACIONES[case["id"]]
        validated_cases.append(enriched)

    counts = Counter(item["veredicto"] for item in VALIDACIONES.values())
    metadata = {
        "fecha_validacion": "2026-09-05",
        "fuente_casos": str(INPUT.relative_to(ROOT)).replace("\\", "/"),
        "casos_validados": len(validated_cases),
        "criterio": "Se priorizan Comprehensive Rules 2.2.0, Tournament Rules 6.11.2026, reglas y cartas Coconut beta y release notes oficiales. La wiki local sirve como corroboración. La conversación de Discord no se considera autoridad por sí sola.",
        "significado_veredictos": {
            "correcta": "La conclusión recogida coincide con una regla o carta verificable.",
            "parcial": "Contiene una parte correcta, pero mezcla alcance, supuestos, fecha o información no comprobada.",
            "incorrecta": "La conclusión contradice una fuente verificable.",
            "desactualizada": "Fue razonable en el contexto histórico, pero una regla vigente la sustituyó.",
            "pendiente": "No hay fuente local suficiente para certificarla.",
        },
        "resumen_veredictos": dict(sorted(counts.items())),
        "casos": validated_cases,
    }
    OUTPUT_JSON.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Validación de los 102 casos claros",
        "",
        "Fecha de contraste: **2026-09-05**. Se revisaron los 102 casos de `casos_claros.json` contra las Comprehensive Rules 2.2.0, Tournament Rules 6.11.2026, documentación de Coconut beta, release notes de Attack of the Vine y la wiki local.",
        "",
        "La conversación de Discord se usa como evidencia de la pregunta y de la respuesta recibida, pero no como autoridad normativa. `parcial` significa que hay una conclusión válida pero falta alcance, texto, fecha o verificación; `pendiente` significa que no hay una fuente local suficiente; `desactualizada` indica que una regla vigente sustituyó la respuesta histórica.",
        "",
        "[JSON detallado](validacion_casos_102.json) · [Casos claros originales](casos_claros.json)",
        "",
        "## Resultado",
        "",
        "| Veredicto | Casos |",
        "| --- | ---: |",
    ]
    for verdict, count in sorted(counts.items()):
        ids_for_verdict = ", ".join(sorted(k for k, item in VALIDACIONES.items() if item["veredicto"] == verdict))
        lines.append(f"| **{verdict}** | {count} ({ids_for_verdict}) |")
    lines += ["", "## Detalle", ""]
    for case in validated_cases:
        check = case["validacion"]
        lines += [
            f"### {case['id']} — {case['titulo']}",
            "",
            f"**Consulta:** {case['pregunta']}",
            "",
            f"**Veredicto:** **{check['veredicto']}** ({check['alcance']}).",
            "",
            f"**Comprobación:** {check['comprobacion']}",
            "",
            "**Fuentes oficiales:** " + ("; ".join(f"`{item}`" for item in check["fuentes_oficiales"]) or "No localizada en la documentación oficial local."),
            "",
            "**Wiki local:** " + ("; ".join(f"`{item}`" for item in check["fuentes_wiki"]) or "No localizada."),
            "",
        ]
        if check["accion_recomendada"]:
            lines += [f"**Acción:** {check['accion_recomendada']}", ""]
    OUTPUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"casos": len(validated_cases), "veredictos": dict(sorted(counts.items())), "json": str(OUTPUT_JSON), "markdown": str(OUTPUT_MD)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
