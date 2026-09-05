# Validación de los 102 casos claros

Fecha de contraste: **2026-09-05**. Se revisaron los 102 casos de `casos_claros.json` contra las Comprehensive Rules 2.2.0, Tournament Rules 6.11.2026, documentación de Coconut beta, release notes de Attack of the Vine y la wiki local.

La conversación de Discord se usa como evidencia de la pregunta y de la respuesta recibida, pero no como autoridad normativa. `parcial` significa que hay una conclusión válida pero falta alcance, texto, fecha o verificación; `pendiente` significa que no hay una fuente local suficiente; `desactualizada` indica que una regla vigente sustituyó la respuesta histórica.

[JSON detallado](validacion_casos_102.json) · [Casos claros originales](casos_claros.json)

## Resultado

| Veredicto | Casos |
| --- | ---: |
| **correcta** | 72 (CASO-002, CASO-003, CASO-004, CASO-005, CASO-006, CASO-007, CASO-008, CASO-009, CASO-011, CASO-012, CASO-013, CASO-015, CASO-020, CASO-021, CASO-022, CASO-024, CASO-026, CASO-028, CASO-031, CASO-035, CASO-037, CASO-039, CASO-042, CASO-049, CASO-051, CASO-052, CASO-054, CASO-055, CASO-056, CASO-064, CASO-065, CASO-068, CASO-071, CASO-072, CASO-075, CASO-076, CASO-077, CASO-078, CASO-079, CASO-080, CASO-082, CASO-086, CASO-087, CASO-093, CASO-094, CASO-095, CASO-096, CASO-099, CASO-100, CASO-101, CASO-104, CASO-105, CASO-107, CASO-108, CASO-109, CASO-110, CASO-111, CASO-113, CASO-114, CASO-115, CASO-116, CASO-117, CASO-118, CASO-120, CASO-122, CASO-123, CASO-130, CASO-131, CASO-132, CASO-134, CASO-135, CASO-136) |
| **desactualizada** | 1 (CASO-048) |
| **incorrecta** | 1 (CASO-098) |
| **parcial** | 26 (CASO-001, CASO-010, CASO-014, CASO-017, CASO-018, CASO-029, CASO-040, CASO-058, CASO-062, CASO-063, CASO-066, CASO-067, CASO-070, CASO-084, CASO-088, CASO-089, CASO-102, CASO-103, CASO-119, CASO-124, CASO-125, CASO-126, CASO-128, CASO-129, CASO-133, CASO-137) |
| **pendiente** | 2 (CASO-016, CASO-073) |

## Detalle

### CASO-001 — Prohibiciones y legalidad cuando los documentos no están actualizados

**Consulta:** ¿Qué fuente permite comprobar las prohibiciones y la legalidad de cartas si el documento de torneo todavía no incorpora el anuncio?

**Veredicto:** **parcial** (fuente_y_vigencia).

**Comprobación:** La aplicación puede servir como consulta auxiliar, pero la legalidad y las prohibiciones deben comprobarse en las Tournament Rules y en el anuncio oficial vigente. La conversación mezcla un documento atrasado con una aplicación que también puede contener erratas.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

**Acción:** Documentar siempre el comunicado o la lista oficial que esté en vigor; no presentar la aplicación como autoridad única.

### CASO-002 — Reemplazos simultáneos para acontecimientos diferentes

**Consulta:** ¿Puede haber varios efectos de reemplazo simultáneos que no se apliquen al mismo acontecimiento?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Varios efectos de reemplazo solo pueden competir cuando modifican el mismo acontecimiento; acontecimientos distintos no son simultáneos. La respuesta del canal es correcta en ese sentido.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Interacción entre efectos de reemplazo y habilidades disparadas con requisitos.md`

### CASO-003 — Orden de elección y revelado con Return of Hercules

**Consulta:** ¿Quién revela y juega primero con Return of Hercules, y puede el siguiente jugador elegir conociendo la elección anterior?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** El jugador activo realiza primero las elecciones y revelados de su parte; después continúa el orden de turno. La información ya revelada es pública para la elección siguiente.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Qué pasa cuando se juegan dos cartas a la vez.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Prioridad entre jugador activo y no activo.md`

### CASO-004 — Bronx: preparado, agotado y tinta secándose

**Consulta:** ¿Un Bronx que entra preparado pero secándose sigue preparado en el siguiente turno, y pueden otros efectos interactuar con personajes que se están secando?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Preparado/agotado y seco/secándose son estados independientes. Secándose impide las acciones que exigen estar seco, pero no toda interacción con la carta.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Heredar una palabra clave al hacer shift.md`

**Acción:** Mantener separados los términos preparado y seco en la redacción de la wiki.

### CASO-005 — Fin del turno: disparos frente a efectos que expiran

**Consulta:** ¿Se resuelven primero los disparos al final del turno o desaparecen antes los efectos hasta el final del turno?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** En el final del turno se añaden y resuelven primero las habilidades de final de turno; después expiran los efectos que duran hasta el final del turno y se hace la comprobación de estado.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Habilidades disparadas 'Al final del turno'.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Orden de resolución en habilidades disparadas.md`

### CASO-006 — Cinderella Stouthearted y cantar antes de jugarla

**Consulta:** ¿Cinderella Stouthearted debe estar en juego cuando se canta la canción para poder desafiar a un personaje preparado?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La habilidad de Cinderella Stouthearted debe estar funcionando cuando se canta la canción. Jugarla después no retroactiva el canto anterior.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Habilidades estáticas presentes en juego y sus interacciones.md`

### CASO-007 — Cinderella Stouthearted y Bodyguard preparado

**Consulta:** ¿Cinderella Stouthearted debe elegir un Bodyguard preparado al usar su permiso para desafiar personajes preparados?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Bodyguard crea una restricción de elección: si un personaje con Bodyguard preparado es una opción legal, debe ser el objetivo del desafío cuando el efecto permite desafiar personajes preparados.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Bodyguard.md`

### CASO-008 — Resist frente a daño movido

**Consulta:** ¿Resist reduce el daño que se mueve a un personaje?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Resist reduce daño que se va a infligir al personaje o localización; mover contadores de daño no es infligir daño y no se reduce con Resist.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Mover daño no es retirar daño.md`

### CASO-009 — Robin Hood Sharpshooter con Firefly Swarm

**Consulta:** ¿Las cartas descartadas con Robin Hood Sharpshooter cuentan al resolver Firefly Swarm elegida por su habilidad?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La acción jugada por Robin se resuelve después de terminar el efecto inicial que pone las demás cartas en el descarte. Firefly Swarm comprueba entonces su condición con el descarte actualizado.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Firefly Swarm con Robin Hood - Sharpshooter sí habilita el segundo modo.md`

### CASO-010 — Sets permitidos en el campeonato de Wilds Unknown

**Consulta:** ¿El campeonato de Wilds Unknown utiliza únicamente sets 9–12 o todo el formato Core vigente?

**Veredicto:** **parcial** (historico).

**Comprobación:** La tabla de Core de las Tournament Rules respalda el conjunto de sets legal en la fecha de la regla, pero no demuestra por sí sola las instrucciones históricas del campeonato concreto de Wilds Unknown ni sus fechas. La respuesta necesita el kit o anuncio de ese evento.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

**Acción:** Conservar la conclusión de Core como provisional y adjuntar el anuncio del campeonato antes de publicarla.

### CASO-011 — Elisa Maza frente a una reducción previa de Jessie

**Consulta:** ¿Jugar Elisa Maza devuelve la fuerza de un personaje a su valor impreso tras una reducción aplicada por Jessie?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** El valor actual de Fuerza se obtiene combinando todos los modificadores; la habilidad de Elisa fija un mínimo basado en la Fuerza impresa sin borrar la reducción de Jessie.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Elisa Maza - Forever Strong y reducciones de Fuerza previas.md`

### CASO-012 — Boost de Cheshire Cat sin destinatario para mover daño

**Consulta:** ¿Puede activarse Boost de Cheshire Cat Inexplicable sin poder completar su efecto, y puede retirarse daño si no existe personaje rival válido?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Se puede activar Boost aunque la resolución posterior no pueda completarse. Si no hay un personaje rival que pueda recibir el daño, no existe movimiento válido y el daño de origen permanece.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Resolución parcial sin objetivo válido.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Mover daño no es retirar daño.md`

### CASO-013 — Quién ordena los disparos de la bolsa

**Consulta:** ¿El jugador activo ordena todos los disparos o cada jugador decide el orden de los suyos?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Cada jugador ordena sus propias habilidades disparadas en la bolsa; el jugador activo no ordena arbitrariamente las del rival.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Orden de resolución en habilidades disparadas.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Múltiples habilidades a la vez.md`

### CASO-014 — Listas de mazo y comprobaciones en Set Championships

**Consulta:** ¿Son obligatorias las listas de mazo y sus comprobaciones en Set Championships?

**Veredicto:** **parcial** (torneo).

**Comprobación:** Las listas son exigibles en eventos Competitive/Premier cuando lo indican las Tournament Rules o el kit. La regla no exige efectuar un deck check a todos los jugadores: establece comprobaciones donde sea posible y una expectativa mínima para Premier.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

**Acción:** Separar obligación de lista, presencia de juez y muestreo de deck checks.

### CASO-015 — Merida daña al atacante antes del daño de desafío

**Consulta:** ¿El daño disparado de Merida puede desterrar al personaje que la desafía antes de que ese personaje le haga daño de desafío?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La habilidad de Merida se dispara durante el desafío y se resuelve antes del paso de daño. Si destierra al atacante, el paso de daño no llega a producirse.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Boo - Energetic Child destierra antes del daño del desafío.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Merida frente a Lilo y Rapunzel - infligir daño no es recibir daño.md`

### CASO-016 — Bloquear inscripciones de una persona en Carde.io

**Consulta:** ¿Puede una organización impedir en Carde.io que una persona excluida de la tienda se inscriba en futuros eventos?

**Veredicto:** **pendiente** (herramienta_externa).

**Comprobación:** El supuesto ajuste de Carde.io no está descrito en la documentación local ni se puede verificar con el texto del JSON; la respuesta del canal reconoce que no se ha probado.

**Fuentes oficiales:** No localizada en la documentación oficial local.

**Wiki local:** No localizada.

**Acción:** Comprobarlo en una cuenta de organización o retirar la afirmación operativa.

### CASO-017 — Elección de jugador inicial en rondas posteriores de Top Cut

**Consulta:** ¿Quién elige jugar primero o segundo a partir de la segunda ronda de Top Cut?

**Veredicto:** **parcial** (torneo).

**Comprobación:** En un nuevo enfrentamiento de Top Cut de Premier, el seed más alto de la fase suiza elige quién juega primero en la primera partida; en las partidas siguientes elige quien perdió la partida anterior. El alcance puede variar si el evento es Competitive y el kit establece otra regla.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

**Acción:** Añadir el nivel y el kit del evento antes de convertirlo en regla general.

### CASO-018 — Rondas y tamaño de Top Cut con 18 jugadores

**Consulta:** ¿Qué consecuencias matemáticas tiene jugar cuatro rondas y Top 4 con 18 jugadores, y puede modificarse así un Set Championship?

**Veredicto:** **parcial** (torneo).

**Comprobación:** La tabla de Tournament Rules asigna 5 rondas suizas y Top 8 a 17–32 jugadores. El análisis de Top 4 y sus combinaciones depende de supuestos matemáticos que no sustituyen la tabla ni autorizan cambiar un Set Championship.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Set Championship con 65 jugadores o más.md`

**Acción:** Usar la tabla oficial y pedir autorización expresa para cualquier estructura distinta.

### CASO-020 — Luisa High Climber mueve su propio daño sin otro aliado

**Consulta:** ¿Puede Luisa High Climber activar su habilidad siendo el único personaje propio y pasar su daño a un rival sin recibir antes daño de otro personaje?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Luisa puede mover su propio daño: el efecto se hace tanto como sea posible y no exige que exista otro personaje propio. La comprobación de estado se realiza después de resolver el efecto.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Luisa Madrigal - I Can Take It, condición Then-if y GSC.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Luisa Madrigal - I Can Take It, llega a 4 daños y no se destierra.md`

### CASO-021 — Syndrome’s Remote y Buzz’s Arm durante el turno rival

**Consulta:** ¿Por qué Syndrome’s Remote puede dispararse en el turno rival y Buzz’s Arm no puede jugarse normalmente cuando Buzz es desterrado en ese turno?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** El disparo de Syndrome's Remote entra en la bolsa aunque ocurra en el turno rival. Buzz's Arm solo ofrece un coste alternativo para jugar un objeto; hace falta una ventana legal para jugarlo.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Disparar habilidades mientras se resuelve una carta.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Jugar una carta con shift reduciendo su coste (incluso gratis).md`

### CASO-022 — Escape Plan como segunda carta que llega al descarte

**Consulta:** ¿Se puede jugar Escape Plan cuando sería la segunda carta que va al descarte ese turno?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La condición de Escape Plan se comprueba al jugar la carta. Que el efecto vaya a producir la segunda carta en el descarte no satisface una condición que exige que ya haya dos.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Escape Plan con acción gratis al questear.md`

### CASO-024 — Significado de GRE en arbitraje

**Consulta:** ¿Qué significa la sigla GRE?

**Veredicto:** **correcta** (arbitraje).

**Comprobación:** GRE se usa en la guía de correcciones como General Rules Error (Error general de reglas). Es una categoría de infracción, no una regla de juego.

**Fuentes oficiales:** No localizada en la documentación oficial local.

**Wiki local:** `04. Guia de correccion de jugadas/02. Errores de reglas/2.4 Error general de reglas (General Rule Error).md`; `04. Guia de correccion de jugadas/05. Consejos generales/Causa raíz y corrección apropiada (GRE).md`

### CASO-026 — Diablo parece robar dos cartas tras un desafío en simulador

**Consulta:** ¿Hay un error si, después de desafiar Will of the Wisp con Gantu y dañar a Diablo mediante un lugar, parece que el rival recibe dos robos?

**Veredicto:** **correcta** (autocorreccion).

**Comprobación:** El propio registro aclara la aparente duplicación: una carta vuelve a la mano y solo la otra es el robo de Diablo. No queda una interacción de reglas pendiente.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** No localizada.

### CASO-028 — Cartas de Shift cuentan como cartas debajo

**Consulta:** ¿Una carta debajo de Zipper por Shift cuenta para los efectos que exigen tener cartas debajo, aunque no proceda de Boost?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Shift crea una pila y la carta que queda debajo sigue siendo una carta under, con independencia de que se colocara mediante Shift o Boost.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Cartas en una pila.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Shift y Webby's Diary - diferencia entre encima y debajo.md`

### CASO-029 — Acumular dos permisos de entintar adicionales

**Consulta:** ¿Jugar dos copias de la carta denominada sails permite poner dos cartas adicionales en el tintero?

**Veredicto:** **parcial** (regla_oficial).

**Comprobación:** Los permisos de entintar adicionales son efectos separados y se acumulan si ambos proceden de cartas identificadas. El nombre incompleto «sails» impide comprobar el texto exacto y sus restricciones.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** No localizada.

**Acción:** Identificar la carta completa antes de publicar una respuesta definitiva.

### CASO-031 — Grandmother Willow no reduce costes de una habilidad

**Consulta:** ¿Varias Grandmother Willow pueden hacer gratis tanto jugar Finnick como activar su efecto de devolver un personaje a la mano?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La reducción de Grandmother Willow se aplica al coste de tinta para jugar el siguiente personaje; no reduce el coste de una habilidad activada de Finnick.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Reducciones de coste apiladas - Akood et Emuti y Grandmother Willow.md`

### CASO-035 — Reducir fuerza con Mickey para aplicar Under the Sea

**Consulta:** ¿Una reducción temporal de fuerza de Mickey convierte un personaje de fuerza 4 en un personaje válido para Under the Sea al dejarlo en fuerza 2?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Under the Sea comprueba la Fuerza modificada en el momento de resolver. Una reducción que deja al personaje en 2 o menos lo hace elegible.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Under the Sea y reordenación de pilas al mazo.md`

### CASO-037 — Descalificación del evento principal y participación en paralelos

**Consulta:** ¿Una descalificación del evento principal impide jugar los eventos paralelos?

**Veredicto:** **correcta** (torneo).

**Comprobación:** Una descalificación de un evento no equivale por sí sola a una prohibición general del recinto o de otros eventos. Esa extensión requiere una medida de elegibilidad separada del organizador.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

### CASO-039 — Sid ve desterrar Toys al mismo tiempo que él

**Consulta:** ¿Sid obtiene lore con Raging Storm si él y un Toy propio son desterrados a la vez durante el turno propio?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Las cartas que salen de juego simultáneamente se ven como un único conjunto al comprobar las habilidades que observan el evento. Sid puede haber disparado su habilidad aunque después esté en el descarte.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/GSC y habilidades que dañan.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Desterrar y volver a la mano desde la zona de juego.md`

### CASO-040 — Marcadores numéricos para cambios de fuerza o voluntad

**Consulta:** ¿Pueden usarse dados o fichas con +1, −1 o −3 para recordar modificaciones como las de Jessie, y qué alternativas hay?

**Veredicto:** **parcial** (torneo).

**Comprobación:** La prohibición de representar numéricamente información de Fuerza/Voluntad en fichas está respaldada por las reglas de torneo. La sugerencia del canal de usar papeles con números es incorrecta; deben ser marcadores no numéricos y no confundirse con daño.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Fichas de recordatorio sobre el mazo.md`

**Acción:** Conservar la prohibición y eliminar la recomendación de papeles o fichas numéricas.

### CASO-042 — Prepararse dentro de un desafío y recibir daño

**Consulta:** ¿Una habilidad que prepara al personaje antes del cálculo de daño evita que reciba daño de desafío?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Enderezar un personaje durante el desafío no elimina el desafío ni evita el cálculo de daño. El personaje puede estar preparado cuando recibe el daño.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Ming Lee - Giant Red Panda sigue en el desafío al enderezarse.md`

### CASO-048 — Fecha de actualización documental y tinta boca arriba

**Consulta:** ¿Cuándo se actualizarán las reglas para documentar mantener boca arriba la carta entintada hasta el final del turno antes del DLC de Brasil?

**Veredicto:** **desactualizada** (vigencia).

**Comprobación:** La respuesta sobre que aún no estaba documentado el procedimiento quedó superada: Tournament Rules 6.11 §5.5 exige mantener boca arriba la carta entintada por la acción normal durante el turno y ponerla boca abajo al final.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

**Acción:** Sustituir la respuesta histórica por la regla vigente y conservar la fecha solo como contexto.

### CASO-049 — Dados para indicar el tamaño de la mano

**Consulta:** ¿Está permitido utilizar un dado para representar cuántas cartas quedan en la mano y qué debe hacerse si se usa?

**Veredicto:** **correcta** (torneo).

**Comprobación:** Un dado que muestra el tamaño de la mano es una representación numérica de información privada y no está permitido como marcador. Se puede pedir que se retire y llamar al juez.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Fichas de recordatorio sobre el mazo.md`

### CASO-051 — Quién autoriza un takeback aceptado por el rival

**Consulta:** ¿Pueden los jugadores acordar solos un takeback o debe intervenir el juez aunque el oponente esté conforme?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Los jugadores no pueden autorizar por sí solos un takeback. La excepción debe evaluarla y aprobarla el Lore Guide conforme a los criterios de la regla de takebacks.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** `01. Reglas/10. Artículos/Reversión de jugadas (takebacks).md`

### CASO-052 — One and Only contra personajes con varios nombres

**Consulta:** Si One and Only elige a Woody & Buzz, ¿destierra también a Woody y Buzz individuales? ¿Qué ocurre al elegir a Woody o a The Madrigal Family?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Un personaje con dos nombres de equipo conserva ambos nombres y sigue siendo un solo personaje. One and Only compara nombres, por lo que un equipo coincide con sus nombres individuales; no concede todos los nombres de una familia por asociación temática.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/One and Only compara el nombre sin la versión.md`

### CASO-054 — Marcadores apilables de reducción de fuerza sin cifras

**Consulta:** ¿Se pueden apilar marcadores con el símbolo de fuerza y un signo menos para recordar reducciones de fuerza?

**Veredicto:** **correcta** (torneo).

**Comprobación:** Los marcadores con símbolos no numéricos pueden recordar una modificación si son claros y no se confunden con daño. La prohibición alcanza a los valores +1, −1, −3, etc.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Fichas de recordatorio sobre el mazo.md`

### CASO-055 — Descartar Look What You've Done como coste de Shift

**Consulta:** Si se descarta Look What You've Done para hacer Shift con Diablo, ¿se juega la acción antes o después de cubrir el Diablo base y usa la bolsa?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Descartar Look What You've Done es parte del coste de Shift. El Shift se completa; después la habilidad disparada permite jugar la acción desde el descarte y el efecto de la acción se resuelve en su momento.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`; `Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Look What You've Done no se dispara al terminar de resolverse.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Temporary Shift funciona aunque quede en medio de la pila.md`

### CASO-056 — Repetir Look What You've Done desde el descarte

**Consulta:** ¿Puede jugarse repetidamente Look What You've Done porque vuelve al descarte al resolverse?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Una acción que termina de resolverse y se coloca en el descarte no se está descartando desde la mano. Ese movimiento no vuelve a disparar una condición que exige descartar una carta.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`; `Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Look What You've Done no se dispara al terminar de resolverse.md`

### CASO-058 — Takeback de acciones agrupadas y origen de la política

**Consulta:** ¿Solicitar lore con tres personajes a la vez puede deshacerse como una sola jugada si no hay información nueva? ¿Desde cuándo existe esa política?

**Veredicto:** **parcial** (torneo).

**Comprobación:** La regla permite tratar varias acciones inmediatas como una jugada agrupada para una secuencia fuera de orden cuando no se obtuvo información nueva, pero siempre requiere evaluación del Lore Guide. La fecha histórica de Milwaukee no está verificada en la documentación local.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** `01. Reglas/10. Artículos/Reversión de jugadas (takebacks).md`

**Acción:** Publicar la regla práctica sin afirmar la fecha hasta localizar el anuncio original.

### CASO-062 — Nombrar equipos con Bruno y cuántos personajes representan

**Consulta:** ¿Qué nombres tiene un equipo al nombrar una carta con Bruno? ¿Hamish, Hubert & Harris representa varios personajes?

**Veredicto:** **parcial** (regla_oficial).

**Comprobación:** Bruno nombra un nombre de carta y un equipo sigue siendo un personaje con varios nombres. La conclusión general es correcta; la anomalía concreta de Hamish, Hubert & Harris depende de la redacción de esa carta y del CRD aplicable.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** No localizada.

**Acción:** Comprobar el texto vigente de Hamish, Hubert & Harris antes de fijar el ejemplo.

### CASO-063 — Takeback de pasar turno y decisiones de final de turno

**Consulta:** ¿Puede deshacerse el pase de turno antes de que el oponente actúe? ¿Cuenta como una jugada agrupada haber omitido una habilidad opcional de final de turno?

**Veredicto:** **parcial** (torneo).

**Comprobación:** Un pase de turno puede rebobinarse solo si el Lore Guide considera que se cumplen los criterios de takeback; una habilidad opcional olvidada y la información obtenida son hechos decisivos. No es una autorización general ni una jugada agrupada automática.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** `01. Reglas/10. Artículos/Reversión de jugadas (takebacks).md`

**Acción:** Registrar el caso como decisión arbitral dependiente de hechos.

### CASO-064 — Mr. Big con Bodyguard concedido por Powhatan's Staff

**Consulta:** ¿Dar Bodyguard a Mr. Big impide todos los desafíos si el rival no tiene personajes capaces de desafiarlo?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Bodyguard solo obliga a escoger ese personaje si el rival puede desafiarlo legalmente. Powhatan's Staff añade por separado la opción de entrar agotado; ninguna de las dos cosas impide todos los desafíos sin un atacante legal.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Bodyguard.md`

### CASO-065 — Momento de la derrota por mazo vacío y victoria al final del turno

**Consulta:** ¿Cuándo se comprueba la derrota por mazo vacío? ¿Puede ganarse por llegar a 20 lore con una habilidad de final de turno antes de esa derrota? ¿Importa vaciarse durante el turno rival?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La derrota por mazo vacío se comprueba al final del turno del jugador cuyo mazo está vacío. Las comprobaciones de estado se hacen en el orden de la fase: una victoria por lore alcanzada antes termina la partida antes de esa derrota.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Derrota, timing mazo vacío.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/GSC y el final de partida.md`

### CASO-066 — Cambiar el mazo entre partidas o rondas en sellado y draft

**Consulta:** En prerelease, sellado y draft, ¿se pueden cambiar cartas entre partidas o solo entre rondas?

**Veredicto:** **parcial** (torneo).

**Comprobación:** Las Comprehensive/Tournament Rules permiten reglas de construcción comunicadas para Limited, pero no fijan aquí un sideboard universal entre partidas o rondas. La respuesta histórica describe práctica de organizador, no una obligación normativa.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

**Acción:** Seguir la regla anunciada por el organizador y conservar separadas las prácticas de cada evento.

### CASO-067 — Reparto de premios, compensaciones externas y resultados pactados

**Consulta:** ¿Qué repartos de premios son legales: pagar media alfombrilla, conceder por premios, vender Golden Mickey y compartir valor, o decidir al dado?

**Veredicto:** **parcial** (torneo).

**Comprobación:** La regla de prize splitting permite repartir premios disponibles en Entry/Competitive si todos los jugadores restantes aceptan y no se intercambia el resultado. No permite contraprestaciones por conceder ni decidir un resultado al azar; el alcance Premier y los objetos concretos dependen del nivel y del premio anunciado.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** `04. Guia de correccion de jugadas/04. Conducta antideportiva/4.5 Resultado de un encuentro inapropiado (Improper Match Result).md`

**Acción:** Separar reparto de premios, concesión, venta posterior y apuestas en subcasos distintos.

### CASO-068 — Mover daño con Cheshire sin destino legal

**Consulta:** ¿Puede Cheshire - Inexplicable quitarse 2 daños al hacer Boost si no hay personaje rival al que moverlos?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Mover daño exige un origen y un destino legales. Si no existe destino rival, el movimiento completo no ocurre y no se retira el daño de Cheshire.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Mover daño no es retirar daño.md`

### CASO-070 — Entrar con daño y entrar agotado: relación con reemplazos

**Consulta:** ¿Hay que aplicar tanto entrar con daño como entrar agotado o se elige solo uno como efecto de reemplazo?

**Veredicto:** **parcial** (regla_oficial).

**Comprobación:** La regla vigente aclara que las modificaciones de cómo una carta entra en juego se resuelven junto con el juego de la carta y no son efectos de reemplazo. La respuesta del canal no desarrolla qué ocurre cuando ambos modificadores se aplican, por lo que queda incompleta.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Habilidades estáticas presentes en juego y sus interacciones.md`

**Acción:** Añadir una secuencia que aplique conjuntamente los dos modificadores concretos.

### CASO-071 — Orden y visibilidad de cartas enviadas al fondo por Under the Sea

**Consulta:** ¿Quién ordena las cartas enviadas al fondo por Under the Sea y puede el jugador afectado conocer ese orden?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Under the Sea permite poner las cartas en el fondo en cualquier orden; quien controla el efecto organiza las pilas y la información de las cartas boca arriba debe ser conocida por todos.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Under the Sea y reordenación de pilas al mazo.md`

### CASO-072 — Fundas legales y opacidad

**Consulta:** ¿Qué requisitos deben cumplir las fundas en torneo y sirven las de reverso translúcido?

**Veredicto:** **correcta** (torneo).

**Comprobación:** Las fundas de torneo deben tener reverso completamente opaco, no reflectante, sin daños ni marcas que permitan distinguir cartas. «Matte» describe textura y no garantiza opacidad.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

### CASO-073 — Enlace here roto en un documento

**Consulta:** ¿Cuál es el destino del enlace here que no funciona en un documento?

**Veredicto:** **pendiente** (documental).

**Comprobación:** El texto conserva una URL recuperada de una versión anterior, pero la documentación local no identifica qué documento debía enlazarla ni verifica que el vídeo siga disponible. No puede certificarse como enlace vigente.

**Fuentes oficiales:** No localizada en la documentación oficial local.

**Wiki local:** No localizada.

**Acción:** Comprobar el documento de origen y la URL antes de enlazarla en la wiki.

### CASO-075 — Bodyguard concedido y opción de entrar agotado

**Consulta:** ¿Por qué Woody con Bodyguard de Bo Peep no entra igual que con Powhatan's Staff?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Bodyguard no contiene una opción de entrar agotado. Esa opción procede del texto de Powhatan's Staff y no se hereda por ganar la palabra clave.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Bodyguard.md`

### CASO-076 — Duo Shift sobre Morph o sobre un único equipo

**Consulta:** ¿Basta un solo Morph para Duo Shift? ¿Puede usarse un único Mickey & Minnie como sus dos bases?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Duo Shift exige dos personajes distintos como bases. Morph puede cubrir una de las identidades, pero un único equipo sigue siendo un solo personaje y no satisface ambas bases por sí solo.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`; `Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Mickey Mouse & Minnie Mouse necesita dos personajes para Duo Shift.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Morph - Little Imitator funciona con todas las variantes de Shift.md`

### CASO-077 — Bambi entrando agotado y carta añadida por Scrooge

**Consulta:** ¿Se dispara Bambi si entra agotado por Horned King o Simba y Scrooge le pone una carta debajo?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Entrar agotado no es una transición que dispare una habilidad «whenever this character exerts». La carta que Scrooge pone debajo llega por una habilidad posterior de la bolsa, no como parte de la entrada inicial de Bambi.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Habilidades disparadas 'Al final del turno'.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Bambi – Ethereal Faun cantando una canción.md`

### CASO-078 — Cantar una canción revelada por Dash Parr

**Consulta:** ¿Puede agotarse a otros personajes para cantar la canción revelada por Dash Parr - Super Fast?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Jugar una canción mediante el efecto de Dash no significa que deba pagarse gratis: el jugador puede usar el coste alternativo de cantar y agotar otros personajes que cumplan el requisito.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Cantar o jugar gratis cuenta como pagar 0 tinta.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Acción jugada debido a un efecto de otra carta.md`

### CASO-079 — Hades y Vine Pod para jugar personajes de equipo

**Consulta:** ¿Pueden Hades o Vine Pod jugar un equipo al desterrar a uno de sus personajes individuales?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Un personaje de equipo posee sus nombres individuales. Hades o Vine Pod pueden comprobar uno de esos nombres y jugar el personaje de equipo si el resto del efecto es legal.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Ursula - Deal Maker solo puede elegir un personaje en juego.md`

### CASO-080 — Fragile as a Flower sobre un personaje ya agotado

**Consulta:** ¿Se puede elegir un personaje ya agotado para Fragile as a Flower?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Fragile as a Flower puede elegir un personaje ya agotado si cumple el coste; el texto no exige que esté preparado ni condiciona la siguiente parte a haberlo preparado.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Enderezar un personaje.md`

### CASO-082 — Habilidades que pueden usarse mientras el personaje se seca

**Consulta:** ¿El secado impide pagar tinta para usar una habilidad? ¿Por qué Hamm debe esperar y Willow puede actuar el mismo turno?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Secándose solo impide quest, challenge y costes/efectos que exigen el símbolo de agotar. Una habilidad sin ese requisito puede usarse durante el mismo turno en que entra.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Performance Review y secado - cuando puedes agotar.md`

### CASO-084 — Nombres inapropiados al registrar un mazo

**Consulta:** ¿Hay límites para nombres de mazo con dobles sentidos al inscribirse en un evento oficial?

**Veredicto:** **parcial** (torneo).

**Comprobación:** Las reglas de torneo y conducta permiten sancionar nombres ofensivos o inapropiados, pero no hay una regla local que resuelva el nombre concreto «circle herc». La respuesta general es válida y la decisión concreta queda al organizador/Lore Guide.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

**Acción:** No presentar el nombre concreto como aprobado sin una decisión documentada.

### CASO-086 — Temporary Shift cubierto por otra carta

**Consulta:** ¿La carta con Temporary Shift vuelve a la mano si otra carta se desplaza encima y tapa su texto? ¿Es un efecto aplicado o una habilidad retrasada?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Temporary Shift crea una habilidad retrasada que comprueba si la carta sigue en la zona de juego al final del turno. Que otra carta la cubra o quede encima no la saca de esa zona.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`; `Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Temporary Shift funciona aunque quede en medio de la pila.md`

### CASO-087 — Elinor al final del turno y Run Away de Rex

**Consulta:** Si Elinor destierra a Rex con Coordinated Efforts al final del turno, ¿sigue siendo durante mi turno a efectos de Run Away?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** El final del turno sigue siendo parte del turno del jugador activo hasta que termina la fase. Una habilidad que dice «during your turn» puede aplicarse antes de ese momento.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Habilidades disparadas 'Al final del turno'.md`

### CASO-088 — Potato Shift: estado seco sobre Morph y sobre un Potato recién jugado

**Consulta:** ¿Potato Shift sobre un Morph seco entra seco? ¿Preparar un Potato jugado este turno permite que el personaje con Potato Shift entre seco?

**Veredicto:** **parcial** (regla_oficial).

**Comprobación:** La parte de Potato jugado este turno es clara: preparar el objeto no cambia que no estuviera en juego al comienzo del turno, por lo que el personaje entra secándose. La interacción Morph/Potato combina la herencia de estado de Shift con la regla especial de Potato y el propio canal reconoce una ambigüedad de redacción.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`; `Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Morph - Little Imitator funciona con todas las variantes de Shift.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Posey - Vampire Potato puede usar Potato Shift sobre Morph.md`

**Acción:** Mantener la variante Morph como pendiente de aclaración oficial y publicar solo la parte inequívoca.

### CASO-089 — Daño infligido y recibido tras aplicar Resist

**Consulta:** ¿El daño reducido a cero sigue considerándose infligido? ¿Qué daño reproduce Mulan y cómo se distinguen daño base, infligido y recibido?

**Veredicto:** **parcial** (regla_oficial).

**Comprobación:** Resist reduce el daño que recibe el objetivo a cero, pero el efecto de origen sigue siendo un efecto que inflige daño. La conclusión sobre daño base/recibido es correcta; la cantidad exacta que reproduce Mulan depende del texto de esa carta y no queda resuelta por el debate.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Escudos (replacement) vs Resist.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Merida - Steady Aim y Resist.md`

**Acción:** Separar la regla general de Resist de la interpretación específica de Mulan.

### CASO-093 — Lilo – Bundled Up con Resist y daño reducido a cero

**Consulta:** ¿Se consume la protección de Lilo – Bundled Up si Resist reduce a cero el daño que recibiría?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Cuando Resist reduce el daño a cero, el personaje no toma daño. Por tanto no se consume la protección de Lilo que reemplaza daño que se recibiría.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Lilo - Bundled Up y Malicious, Mean, and Scary.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Escudos (replacement) vs Resist.md`

### CASO-094 — Responsabilidad de anunciar Source of the Vine

**Consulta:** ¿Quién debe recordar y comunicar la habilidad de Source of the Vine al buscar lore el rival? ¿Puede su controlador ganar lore por asumir que el rival no pagó?

**Veredicto:** **correcta** (torneo).

**Comprobación:** Source of the Vine contiene una elección obligatoria con una opción de pago. El controlador debe anunciarla y ambos jugadores deben mantener el estado correcto; no se puede inferir que el rival rechazó pagar por silencio.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`; `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** No localizada.

### CASO-095 — John Smith: desafío de un personaje que ya abandonó el juego

**Consulta:** Con John Smith agotado, si otro personaje desafió y fue desterrado, ¿se gana lore al final del turno porque ninguno de los personajes actuales desafió?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La condición de John Smith pregunta si algún personaje de ese jugador desafió durante el turno. El desafío es un evento ya ocurrido; que el personaje que desafió sea desterrado después no convierte el evento en «ningún desafío». Por eso no se gana el lore en el supuesto descrito.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Desterrar y volver a la mano desde la zona de juego.md`

**Acción:** Usar siempre el texto exacto de John Smith – Snow Tracker; no confundirlo con John Smith – Undaunted Protector.

### CASO-096 — Localizar reglas de protección de un solo uso y daño

**Consulta:** ¿Dónde explica el CRD2.2 la interacción de las reglas de daño con las protecciones de un solo uso?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** El CRD no tiene una entrada separada para cada combinación de cartas. Se aplican las reglas generales de reemplazos, daño, habilidades y el texto de cada carta; si persiste una duda concreta decide el Lore Guide.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Aplicación de múltiples efectos de reemplazo (Escudos).md`

### CASO-098 — Belle bajo The Black Cauldron y jugarla al desterrar el objeto

**Consulta:** ¿Se puede jugar Belle que estaba bajo The Black Cauldron al desterrar el objeto y cuenta como jugada desde el descarte?

**Veredicto:** **incorrecta** (regla_oficial).

**Comprobación:** Una carta debajo de The Black Cauldron no está en juego, por lo que Belle no puede usar desde ahí su habilidad WHAT A MESS para desterrar el objeto. Si el Caldero es desterrado, las cartas de la pila pasan al descarte; eso no crea por sí solo un permiso para jugar Belle desde el descarte. El Caldero sí permite jugarla desde debajo mientras permanece en juego mediante RISE AND JOIN ME!.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Scrooge McDuck - Resourceful Miser desde The Black Cauldron.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Hide Away sobre The Black Cauldron con Hades debajo.md`; `02. Listado de Cartas/Set 7 - Archazia''s Island.md`; `02. Listado de Cartas/Set 10 - Whispers in the Well.md`

**Acción:** Corregir la respuesta del canal y especificar qué efecto adicional, si lo hay, permite jugar la carta desde el descarte.

### CASO-099 — Activar Scream Canister sin objetivo para gastar tinta

**Consulta:** ¿Se puede activar Scream Canister sin personajes rivales elegibles para agotar tinta y permitir que Randall busque2 de lore?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** El coste de Scream Canister se puede pagar aunque no haya un personaje rival elegible. En la resolución se agotan las cartas de tinta y se hace la parte del objetivo hasta donde sea posible; no se crea un objetivo ilegal.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Resolución parcial sin objetivo válido.md`

**Acción:** Conservar la distinción entre pagar el coste y resolver una elección sin objetivo.

### CASO-100 — Windstorm y comprobación de destierro entre sus efectos

**Consulta:** ¿Windstorm destierra a Peter Pan y Tinker Bell antes de su daño adicional a Evasive? ¿La palabra «then» crea una comprobación intermedia, a diferencia de Let the Storm Rage On con Diablo?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** «Then» ordena los efectos dentro de la misma resolución, pero no crea una comprobación de estado intermedia. Windstorm termina su efecto completo antes de la comprobación que pueda desterrar personajes por daño.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Qué pasa cuando se juegan dos cartas a la vez.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Let The Storm Rage On sobre Angel - Experiment 624.md`

### CASO-101 — Orden de cartas de un personaje Shift o Boost al cambiar de zona

**Consulta:** ¿Quién decide el orden de las cartas de un personaje con Shift o Boost cuando el efecto las mueve, y qué reglas lo respaldan?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Al mover una pila a una zona, el propietario puede ordenar sus cartas salvo que el efecto indique otra cosa. Las cartas boca arriba y las pilas se mantienen conocidas según las reglas de zonas y del efecto que las mueve.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Cartas en una pila.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Under the Sea y reordenación de pilas al mazo.md`

### CASO-102 — Cambiar cartas del mazo en una presentación o formato limitado

**Consulta:** ¿Se permite hacer sideboard entre rondas o entre partidas de una presentación, y quién determina la norma aplicable?

**Veredicto:** **parcial** (torneo).

**Comprobación:** No hay una regla general local que conceda sideboard entre partidas de Limited. El organizador debe anunciar la construcción y cualquier cambio permitido; una práctica habitual no es una obligación reglamentaria.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

**Acción:** Conservar la norma comunicada por el organizador y no generalizar la práctica de una tienda.

### CASO-103 — Clasificación Hunny: versiones distintas y reimpresiones

**Consulta:** ¿Las versiones antiguas de un personaje reciben Hunny porque una versión nueva lo tiene? ¿Qué ocurre con la reimpresión de Pooh – Hunny Wizard si la app no está actualizada?

**Veredicto:** **parcial** (regla_oficial).

**Comprobación:** Las clasificaciones pertenecen a cada carta concreta y no se transfieren por compartir personaje. La parte sobre Hunny es correcta si se refiere a la errata de Pooh – Hunny Wizard; la aplicación desactualizada no es prueba suficiente de la errata.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Winnie the Pooh - Hunny Archmage cuenta otra copia como other Hunny.md`

**Acción:** Citar la errata o fuente de carta vigente junto a la regla de que las versiones son cartas distintas.

### CASO-104 — Shift sobre un personaje cuyo daño supera la nueva voluntad

**Consulta:** ¿El personaje recién jugado con Shift es desterrado si hereda daño igual o superior a su voluntad?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Shift conserva el daño de la pila. Tras jugar la nueva carta se comprueba el estado: si el daño acumulado es igual o superior a su Voluntad, el personaje es desterrado.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Heredar una palabra clave al hacer shift.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/GSC y el final de partida.md`

### CASO-105 — Protección de Rapunzel frente a un atacante con fuerza cero

**Consulta:** ¿Un desafío con fuerza0 consume Act of Kindness de Rapunzel? ¿Cambia si la fuerza era1 y se redujo a0 por Rhino?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Fuerza 0 significa que el personaje no inflige daño durante el desafío; no hay daño que consumiría Act of Kindness. Esto es distinto de infligir daño y que Resist lo reduzca después.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Rapunzel conserva su protección si Resist reduce el daño a 0.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Rapunzel – Act of Kindness y mover daño.md`

### CASO-107 — Lilo jugada desde el descarte frente a The Horned King

**Consulta:** ¿Cómo interactúa la entrada agotada de Lilo desde el descarte con The Horned King, en comparación con una interacción de Merida mostrada en un vídeo?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La entrada agotada que impone Horned King o el efecto propio de Lilo se aplica al jugarla desde el descarte. La comparación con el vídeo de Merida no cambia el texto de Lilo ni exige una segunda entrada agotada.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Horned King - Toca descarte antes de volver a mano.md`

### CASO-108 — Orden para alterar la mano inicial

**Consulta:** ¿Puede un jugador esperar a que su rival termine de alterar la mano inicial antes de hacerlo él?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Al alterar la mano inicial, el jugador que empieza lo hace primero y los demás siguen el orden de turno. No se espera a que todos elijan simultáneamente.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Prioridad entre jugador activo y no activo.md`

### CASO-109 — Rapunzel & Flynn Rider: jugar el personaje descartado durante un desafío

**Consulta:** ¿Cuándo se juega el personaje descartado gracias a Rapunzel & Flynn Rider – Unlikely Pair? ¿Puede hacerse durante un desafío contra Dr. Bushroot?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La habilidad disparada de Rapunzel & Flynn Rider se añade a la bolsa tras el descarte y se resuelve antes del paso de daño que aún no haya ocurrido. Puede jugar el personaje en esa ventana si es legal.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Lyle Tiberius Rourke y Rapunzel & Flynn Rider.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Disparar habilidades mientras se resuelve una carta.md`

### CASO-110 — Vine Pod y personajes con nombres dobles

**Consulta:** ¿Se puede desterrar un Mickey individual con Vine Pod para jugar Mickey & Minnie? ¿Cuántos nombres tiene un personaje doble y dónde se define?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Un equipo con dos nombres de personaje tiene tres nombres relevantes (los dos individuales y el nombre del equipo) y basta una coincidencia textual cuando el efecto pide un nombre. Vine Pod debe seguir además sus costes y objetivos propios.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/One and Only compara el nombre sin la versión.md`

### CASO-111 — Willow: qué personaje consume la reducción de coste

**Consulta:** ¿Puede elegirse a qué personaje aplicar Willow o la consume el siguiente, incluso si se juega gratis mediante un efecto?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La palabra «next» identifica el siguiente personaje que se juegue y la reducción se consume en ese primer juego legal, incluso si un efecto lo juega gratis.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Reducciones de coste apiladas - Akood et Emuti y Grandmother Willow.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Jugar carta sin objetivo válido.md`

### CASO-113 — Iago con reducción de fuerza y Challenger

**Consulta:** Si Iago – Stomping Mad recibe−2 de fuerza de Della’s Moon Lullaby, ¿desafía con3 o5 en el turno rival?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Los modificadores se combinan: 0 − 2 + 5 = 3 de Fuerza durante el desafío. Challenger solo se aplica mientras Iago está desafiando.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Cálculo de fuerza con Tiana y Desafiador.md`

### CASO-114 — Entintar boca arriba: regla de torneo o regla general

**Consulta:** ¿Por qué4.2.1.3 sigue indicando colocar tinta boca abajo si se utiliza entintado boca arriba?

**Veredicto:** **correcta** (torneo).

**Comprobación:** La regla de las Comprehensive Rules describe el entintado normal boca abajo; Tournament Rules §5.5 añade el procedimiento de torneo temporal de mantener la carta boca arriba durante el turno y girarla al final.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`; `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** No localizada.

### CASO-115 — Super Goof contra Peter Pan – Never Land Prankster

**Consulta:** ¿Super Goof gana2 de lore al desafiar mientras Peter Pan – Never Land Prankster está agotado?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La restricción estática de Peter Pan impide ganar lore por efectos mientras se aplica, pero deja de aplicarse al declararse un desafío legal. Super Goof gana el lore de su habilidad en ese momento.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/No poder ganar lore por efecto estático.md`

### CASO-116 — Pocahontas – Peacekeeper retirada por Red Alert

**Consulta:** ¿Sigue vigente la prohibición de desafiar de Pocahontas – Peacekeeper si Red Alert la retira del juego?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** La habilidad de Pocahontas se creó al jugarla y no dice que dependa de que permanezca en juego. Red Alert puede retirar la fuente y la prohibición temporal sigue vigente.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Fuente estática abandona el juego.md`

### CASO-117 — Mover o colocar daño frente a Hercules – Mighty Leader

**Consulta:** ¿Mover o colocar contadores con Cheshire Cat o Malicious, Mean and Scary evita el efecto de Hercules – Mighty Leader?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Infligir daño, mover contadores de daño y poner contadores de daño son eventos distintos. Hercules solo reacciona al evento que su texto describe como daño infligido.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Mover daño no es retirar daño.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/GSC y habilidades que dañan.md`

### CASO-118 — Cartas alteradas, Enchanted y cartas marcadas

**Consulta:** ¿«Altered art» de TR3.11 incluye Enchanted? ¿Pueden usarse si su grosor o curvatura permiten distinguirlas incluso enfundadas?

**Veredicto:** **correcta** (torneo).

**Comprobación:** Una Enchanted es una versión oficial de la carta, no una carta con arte alterado por un jugador. Puede usarse si cumple legalidad y no es distinguible; grosor, curvatura o marcas pueden hacerla ilegal.

**Fuentes oficiales:** `Documentacion Oficial/Tournament-Rules-6.11.2026_Update-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Legalidad de cartas firmadas.md`

### CASO-119 — Touch the Sky y la condición de elegir de Tod

**Consulta:** ¿Touch the Sky dispara Tod – Knows All the Tricks aunque se determine qué personaje mover sin usar «choose/chosen»? ¿Cómo se relacionaría ese texto con Ward si permitiera mover rivales?

**Veredicto:** **parcial** (regla_oficial).

**Comprobación:** Touch the Sky no usa una elección «chosen» en su texto actual, por lo que no satisface una condición que exige elegir. La variante hipotética sobre mover un rival y Ward no es una regla aplicable a la carta impresa.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Qué pasa cuando se juegan dos cartas a la vez.md`

**Acción:** Mantener separada la carta impresa de cualquier redacción hipotética.

### CASO-120 — Elegir un personaje propio con Ward

**Consulta:** ¿Ward impide que el propietario elija sus propios personajes?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Ward solo impide que los oponentes elijan la carta. Su propietario puede elegir un personaje propio con Ward siempre que el efecto lo permita.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Habilidades estáticas presentes en juego y sus interacciones.md`

### CASO-122 — Dónde localizar las guías de sets de GooglyGlimmers

**Consulta:** ¿Dónde se publican actualmente las guías de sets del autor para consultar interacciones?

**Veredicto:** **correcta** (recurso_comunitario).

**Comprobación:** La respuesta describe la disponibilidad de un recurso comunitario y no una regla: el autor no tenía guías recientes escritas y ofrecía vídeos de interacciones. Es correcta como estado de ese recurso, no como fuente oficial.

**Fuentes oficiales:** No localizada en la documentación oficial local.

**Wiki local:** No localizada.

### CASO-123 — Violet sobre Violet: disparadas de ambas cartas y Merida

**Consulta:** Con Violet Parr – Super Resilient y Merida agotadas, ¿jugar otra Violet mediante Shift dispara a Merida y a las dos Violet? ¿La Violet de abajo ve jugar la nueva?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Al jugar la segunda Violet se generan los disparos aplicables de Merida y de las Violet. La Violet que queda debajo sigue siendo la fuente que ve jugar a la nueva antes de que la pila se cubra.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Disparar habilidades mientras se resuelve una carta.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.5. Keywords/Dash Parr & Violet Parr combina los estados con Combo Shift.md`

### CASO-124 — Tod y el límite de dos veces si se rechaza prepararlo

**Consulta:** ¿Se consume una de las dos resoluciones de Tod si se elige no prepararlo, por ejemplo porque ya estaba preparado al recibir Education or Elimination?

**Veredicto:** **parcial** (regla_oficial).

**Comprobación:** Rechazar una opción «may» no cuenta como usarla. La regla de «once» respalda el principio, pero la conversación lo extrapola a «twice» sin una cita directa; debe comprobarse la redacción concreta de Tod.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Tod + You Came Back y habilidades en el Bolsa.md`

**Acción:** Publicar la conclusión solo junto al texto exacto de Tod o una aclaración oficial.

### CASO-125 — Pool de cartas y rotación en Coconut

**Consulta:** ¿Coconut usa el pool de Infinity o Core y le afectan rotación o prohibiciones?

**Veredicto:** **parcial** (formato_beta).

**Comprobación:** El reglamento de Coconut beta define construcción y victoria a 25 lore, pero no define legalidad de sets, rotación ni prohibiciones propias. Por eso no se puede afirmar normativamente que todas las cartas sean legales sin una decisión del organizador.

**Fuentes oficiales:** `Documentacion Oficial/FormatCoconut_Rules.pdf`; `Documentacion Oficial/FormatCoconut_BetaCoconutCards.pdf`

**Wiki local:** `01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md`

**Acción:** Tratar la legalidad como regla anunciada para cada evento hasta que Coconut publique una política propia.

### CASO-126 — Tiempo de ronda y organización de eventos Coconut

**Consulta:** ¿Qué límite de tiempo y estructura se deberían usar en un evento Coconut de tienda?

**Veredicto:** **parcial** (formato_beta).

**Comprobación:** Coconut se publica como beta y no aporta rondas suizas ni límite de tiempo de torneo. La estructura abierta y el tiempo son decisiones de la tienda/organizador, no una regla oficial del formato.

**Fuentes oficiales:** `Documentacion Oficial/FormatCoconut_Rules.pdf`

**Wiki local:** `01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md`

### CASO-128 — Robin Hood en Coconut: colección y número de arcos externos

**Consulta:** ¿Qué significa «collection» en Robin Hood – Sneaky Sleuth? ¿Hay que llevar varios Robin’s Bow fuera del mazo?

**Veredicto:** **parcial** (formato_beta).

**Comprobación:** En Coconut la carta asociada puede aparecer hasta cuatro veces y el resto del mazo es singleton. «Collection» no es una zona definida por el reglamento; llevar Robin's Bow adicional es una interpretación de la habilidad, no una obligación general del formato.

**Fuentes oficiales:** `Documentacion Oficial/FormatCoconut_Rules.pdf`; `Documentacion Oficial/FormatCoconut_BetaCoconutCards.pdf`

**Wiki local:** `01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md`

**Acción:** Citar el texto exacto de la habilidad Coconut antes de fijar cuántos objetos externos se necesitan.

### CASO-129 — Ursula Coconut y Angel – Underdog al cantar

**Consulta:** ¿Angel – Underdog canta por4 o3 con Ursula Coconut?

**Veredicto:** **parcial** (formato_beta).

**Comprobación:** La habilidad Coconut de Ursula modifica el coste que cuentan los personajes al cantar, pero el resumen no conserva el texto completo de Ursula ni el coste de Angel. El resultado 4 es plausible solo después de verificar ambos textos.

**Fuentes oficiales:** `Documentacion Oficial/FormatCoconut_Rules.pdf`; `Documentacion Oficial/FormatCoconut_BetaCoconutCards.pdf`

**Wiki local:** `01. Reglas/9. Multijugador (Multiplayer)/Cartas Coconut de la beta.md`

**Acción:** Añadir los textos de Ursula Coconut y Angel – Underdog al caso.

### CASO-130 — Dos John Smith – Undaunted Protector frente a Red Alert

**Consulta:** ¿Dos John Smith – Undaunted Protector se protegen entre sí hasta dejar Red Alert sin elecciones legales?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Cada John Smith es un objetivo legal independiente para Red Alert. La restricción de uno no elimina al otro ni obliga a considerar que ambos sean un único personaje.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/John Smith - Do your worst y restricción de elección.md`

### CASO-131 — Jessie – Lively Cowgirl: tinta pagada al cantar y reducciones

**Consulta:** ¿Jessie se dispara al cantar una canción de coste superior a2 sin pagar tinta? ¿Importa el coste impreso o lo realmente pagado, y desde cuándo se interpreta así?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Cantar paga un coste alternativo de 0 tinta, pero la carta conserva su coste impreso para efectos que miran el coste de la carta; Jessie comprueba la cantidad de tinta pagada según su texto. Las reducciones que dejan el pago en 2 o menos satisfacen la condición.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.3. Costes y Requisitos/Cantar o jugar gratis cuenta como pagar 0 tinta.md`

### CASO-132 — Redacción hipotética de Milo: elegir antes de descartar

**Consulta:** Si Milo dijera «puedes elegir un personaje rival; si lo haces, puedes descartar…», ¿se podría descartar sin un rival elegible?

**Veredicto:** **correcta** (hipotetico).

**Comprobación:** En la redacción hipotética, la segunda cláusula depende de haber elegido primero un personaje rival. Sin objetivo legal no se puede realizar esa primera elección ni su efecto condicional posterior.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Resolución parcial sin objetivo válido.md`

### CASO-133 — Decisión arbitral en retransmisión: Luisa con3 de daño sin otros personajes

**Consulta:** ¿Qué ocurrió en Sailor contra Dillon del campeonato norteamericano y fue correcto impedir mover el daño de Luisa?

**Veredicto:** **parcial** (incidente_arbitral).

**Comprobación:** Con tres daños y sin otro personaje, la regla de Luisa permite mover su propio daño tanto como sea posible. Lo que no está verificado es el relato de la retransmisión y la decisión arbitral concreta.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/Luisa Madrigal - I Can Take It, condición Then-if y GSC.md`

**Acción:** Separar la conclusión reglamentaria del incidente hasta disponer del vídeo o acta.

### CASO-134 — Ursula – Voice Stealer sin personaje rival preparado

**Consulta:** ¿Ursula – Voice Stealer permite jugar una canción si el único personaje rival ya está agotado?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Ursula – Voice Stealer requiere un personaje rival preparado para poder agotarlo y conocer su coste. Si el único rival está agotado, no se realiza esa elección y la cláusula posterior no tiene personaje «the exerted character» al que referirse.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.2. Zonas y Movimientos/Ursula - Deal Maker solo puede elegir un personaje en juego.md`

### CASO-135 — Milo: descartar obliga a devolver un personaje elegible

**Consulta:** ¿Puede Milo descartar sin devolver ningún personaje? Si es el único personaje en juego, ¿debe devolverse a sí mismo?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** En el texto real de Milo, la opción de descartar y devolver está vinculada: si se elige descartar, hay que devolver un personaje elegible. Si Milo es el único objetivo legal, puede devolverse a sí mismo.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Resolución parcial sin objetivo válido.md`; `01. Reglas/11. Casos de ejemplo y aclaraciones/11.6. Interacciones Complejas/John Smith - Obligado elegir si objetivo válido.md`

### CASO-136 — Violet – Learning New Powers y John Smith sin daño

**Consulta:** ¿Puede elegirse John Smith – Undaunted Protector sin daño como origen del daño que Violet intenta mover? ¿Cambiaría si el texto exigiera un personaje dañado?

**Veredicto:** **correcta** (regla_oficial).

**Comprobación:** Un efecto que dice «remove up to» puede elegir un personaje sin daño y retirar cero; la elección solo sería ilegal si el texto exigiera expresamente un personaje dañado. La condición de John Smith no añade Ward contra su propietario.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`

**Wiki local:** `01. Reglas/11. Casos de ejemplo y aclaraciones/11.4. Habilidades/Habilidades y sus efectos.md`

### CASO-137 — Robin’s Bow externo devuelto al mazo en Coconut

**Consulta:** ¿Robin’s Bow traído desde la colección puede entrar en el mazo mediante You’re Welcome?

**Veredicto:** **parcial** (formato_beta).

**Comprobación:** Una vez que Robin's Bow está en juego es un objeto normal y You're Welcome puede barajarlo si es un objetivo legal. Lo no definido por Coconut es cómo una carta de la «collection» entra en juego y pasa a ser una carta del juego.

**Fuentes oficiales:** `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`; `Documentacion Oficial/FormatCoconut_Rules.pdf`; `Documentacion Oficial/FormatCoconut_BetaCoconutCards.pdf`

**Wiki local:** `01. Reglas/9. Multijugador (Multiplayer)/Formato Coconut (Beta).md`

**Acción:** Acordar o documentar la zona inicial de las cartas de collection antes de aplicar esta interacción.

