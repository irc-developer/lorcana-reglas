# Revisión de la wiki: CR 2.3 e Hyperia City

**Fecha:** 09/10/2026. **Estado:** edición, validación, commit, push y publicación selectiva completados. La recarga de la conexión MCP persistente queda pendiente.

Se revisaron individualmente los **495 documentos** del inventario, incluidos **239 casos** y **15 documentos históricos**. Se actualizaron **294 documentos del inventario**; esta cifra incluye ajustes de referencias y enlaces y no representa 294 errores de reglas. Se conservaron los históricos como antecedentes y se cerraron las decisiones sobre los **34 temas de Hyperia City**.

La selección pública contiene **303 notas y 14 archivos gráficos**, correspondientes a siete diagramas con su fuente editable y su imagen. Se crearon ocho artículos. De los 317 archivos seleccionados, 176 cambian únicamente referencias, enlaces o etiquetas; los demás incluyen artículos nuevos, contenido, ejemplos y recursos. El índice publicable contiene **246 casos**. El borrador previo de Peter Pan’s Shadow/Pegasus pertenece a otra transacción y permanece sin publicar aquí.

## Las ocho entradas nuevas

- Belle — Apprentice Inventor: continuar la jugada después de desterrar The Black Cauldron como pago.
- Jukebox: «another card» exige una carta distinta de la canción que originó el disparo.
- Minnie Mouse — Urban Visionary: las dos opciones son independientes y determinan cuándo agotar el pozo.
- Baymax — Amped Up: retirar gotas directamente no equivale a un coste de tinta.
- Madam Mim — Resourceful Trickster: las gotas usadas antes de su entrada no disparan BAUBLE GAME.
- Thomas O’Malley — Savvy Vagabond: revelación de todos los jugadores y comparación del máximo global.
- Flippant Taunt: duración del efecto cuando sale quien lo generó.
- Clawhauser — Safety Officer: jugar gratis no elimina su requisito de haber jugado otro personaje.

Las demás aclaraciones se integraron en los documentos canónicos, evitando altas repetidas. Entre las correcciones adicionales están la duración de palabras clave, los disparos flotantes, los efectos secuenciales, los efectos de entrada, las restricciones para acciones y las dependencias de políticas de torneo. Estas políticas se contrastaron con sus propios originales: no se deducen penalizaciones de CR 2.3.

## Vigencia y fuentes

Los anticipos indican **16/10/2026**. CR 2.2 sigue siendo la referencia aplicable hasta el 15/10. Las seis notas antiguas ya retiradas en la migración anterior no se retiran de nuevo.

Se conserva el original inglés CR 2.3, su comparación con 2.2 y el HTML de las notas oficiales de Hyperia junto a una extracción identificada. Las fichas distinguen texto impreso y erratas, sin inventar una redacción completa de las cinco modificaciones de Adventurous. Se incorporaron los originales de Tournament Rules del 14/07/2026 y Play Correction Guidelines del 21/05/2024, con procedencia y hashes. El catálogo largo y las fuentes permanecen fuera de Publish.

## Comprobaciones

- Lectura individual y decisiones: inventario y registro de lectura con hashes finales.
- Enlaces locales: sin destinos rotos en el alcance activo; los marcadores de plantilla están excluidos. Las referencias a PDF usan fuentes oficiales accesibles.
- Etiquetas de los casos seleccionados: canónicas y entre dos y seis por caso; contador y fecha del registro reconciliados.
- Siete diagramas inspeccionados visualmente; las exportaciones corresponden a sus SVG. La bolsa conserva el turno de resolución del último jugador mientras tenga habilidades propias.
- Motor de consulta: **16 pruebas superadas**.
- Hyperia y erratas: **6 pruebas superadas**, incluida la invalidación del índice al cruzar la fecha de aplicación.
- MCP por stdio: **11 pruebas superadas**, incluida la selección futura de CR 2.3 y la conservación de evidencia completa en ambos formatos.
- Publicación selectiva: **13 pruebas superadas**. Las **4 pruebas de la transición CR 2.3** se habían superado también durante esta ejecución.

El corpus y el índice están actualizados. Los procesos MCP nuevos cargan esta implementación. La conexión ya abierta fue comprobada y conserva el código anterior, por lo que no puede acreditarse que tenga incorporadas las nuevas notas y erratas. No hay una herramienta disponible para recargarla y no se terminan procesos de otros chats. Esta comprobación queda explícitamente pendiente.

## Conservación del trabajo previo

Se aislaron las versiones de esta auditoría de Bodyguard, Strange Things, el índice y el registro de tags antes de commit y Publish; después se restauró el contenido combinado con comprobación de hashes. Empates intencionales y Peter Pan’s Shadow/Pegasus se conservan con sus hashes iniciales. La configuración de la interfaz de Obsidian no se incluye en el commit ni en Publish.

## Git y publicación

El commit [fcea89c](https://github.com/irc-developer/lorcana-reglas/commit/fcea89c3fd026f7970e53fe63d12e37e99492bd6) está subido a `origin/main`. La API oficial de GitHub comprobó que la cuenta configurada es propietaria y administradora del remoto. La publicación selectiva terminó con **279 archivos subidos, 38 ya actualizados y cero pendientes de la selección**. Se preservaron los demás pendientes de la bóveda.

El contenido público de las **303 notas** coincide con el commit, normalizando solo BOM y finales de línea. Los **14 recursos** coinciden byte a byte. Los informes [de publicación](auditoria-cr-2.3-publicacion.json) y [de verificación pública](auditoria-cr-2.3-verificacion-publica.json) incluyen las rutas, enlaces y hashes.

El índice del MCP se reconstruyó después de restaurar los cuatro archivos compartidos. Se verificaron las ocho cartas y sus casos desde un proceso nuevo, con CR 2.3 en la fecha futura. El único paso pendiente es recargar la conexión MCP que ya estaba abierta; no quedan notas de esta auditoría pendientes de publicación.
