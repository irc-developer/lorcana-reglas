# Ejecución de la migración CR 2.2 → 2.3

**Fecha:** 9 de octubre de 2026. **Estado:** revisión y adaptación completas; publicación y retirada pendientes de ejecución y comprobación.

Iván autorizó publicar al terminar la revisión, sin esperar al 16 de octubre. La wiki presenta la adaptación 2.3 con su fecha efectiva; el motor actualizado mantiene la fuente 2.2 hasta el 15 y selecciona 2.3 desde el 16. Se conserva el PDF previo y el historial local.

## Fuentes y comparación

- Original nuevo: `Documentacion Oficial/CRUpdate_EN_Oct-2026.pdf`, versión 2.3.0, efectiva 16/10/2026, inglés, 56 páginas; SHA-256 `8b7a458169978a13b688493d4b24d713bdc8baee32ce5e774b0515079a0b91fe`.
- Original previo: `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`, versión 2.2.0, efectiva 09/07/2026, 55 páginas; SHA-256 `5ffa31172fcaae2cbdbf127aebdd54987f01a4e72008812c96556c29d0942d8f`.
- Procedencia: [recursos oficiales](https://www.disneylorcana.com/en-US/resources/), actualizados 08/10/2026; [notas Hyperia City](https://www.disneylorcana.com/en-US/news/2026/10/hyperia-city-set-release-notes).
- Matriz: `cr-2.3-matriz-diferencias.tsv`, 55 filas. Cubre las 11 entradas principales, 8 ajustes y 7 entradas de glosario del resumen oficial, además de altas subordinadas, la baja 7.1.6.1, traslados y diferencias de puntuación/diagramas.
- Se extrajeron y compararon todas las páginas. Revisión visual global de las 56 páginas mediante siete hojas de contacto y ampliaciones de páginas con cambios, símbolos, diagramas e incidencias. La portada y el resumen se comprobaron también durante la preparación.
- 565 y 582 identificadores extraídos, respectivamente: incluyen encabezados de capítulo y sección, no son un recuento de reglas normativas independientes. 18 identificadores añadidos y uno retirado.
- Los glosarios tienen 101 fragmentos en 2.2 y 106 en 2.3: el formato nuevo separa las acepciones de discard, ink, ready y stack. Se corrige la pérdida de términos capitalizados o con símbolos y se excluyen los resúmenes históricos del PDF.
- El perfil anterior intercambiaba símbolo entintable y coste de movimiento. La revisión visual de ambos PDF confirma `& → {INKWELL}` y apóstrofo `→ {M}` en ambos; se corrige la extracción anterior, sin atribuir un cambio de regla al glifo.

## Decisiones editoriales

Se crean 1.13 y 8.16 y la entrada general 2.3. Se actualizan juego de cartas, pagos, movimiento, opcionalidad, estáticas, resolución, palabras clave, pozo de tinta, glosario y resúmenes. Las páginas de adaptación completa llevan aviso de vigencia futura; las notas complementarias indican su fecha en el párrafo correspondiente.

Casos revisados:

- **Heredar una palabra clave al hacer shift:** resultado distinto desde el 16/10. La Evasive impresa de Ariel prevalece sobre la concesión temporal; esta deja de existir y no se recupera al hacer Shift. Se conserva el criterio anterior en un aviso fechado. Textos completos de las dos Ariel verificados en los sets 3, 4 y 9; enlaces Lorcast existentes contrastados.
- **No hay bolsa entre jugadores:** mantiene el resultado de una instrucción; precisa que, con varias partes, todos completan cada parte antes de pasar a la siguiente.
- **Colors of the Wind:** corrige una revelación indebidamente descrita como simultánea y retira ejemplos con cartas mal identificadas. Solo quien resuelve la canción roba, de una en una; los disparos esperan la resolución completa. Texto verificado en Set 11.
- **Moverse a una localización recién jugada:** mantiene resultado; repara referencias a un procedimiento local antes mal numerado y cita pago 4.7.3.4 y movimiento 4.7.4.
- **Scrooge desde The Black Cauldron:** no cambia el resultado de su secuencia normal; no abandona una zona durante ese procedimiento. No extrapolar la nueva continuidad a un escenario no planteado.
- **Ancestral Guitar:** el +2 separado se mantiene; la nueva comparación de duraciones no convierte Singer en una palabra clave acumulable.
- **Merida entra agotada, Remember Me, Woody y Headless Horseman/Ralph:** se revisan las reglas pertinentes; no cambian sus resultados por este delta. 6.7.7 conserva la última información conocida; la lista nueva no modifica retroactivamente características de una carta que salió.
- **Bodyguard y Peter Pan's Shadow/Pegasus pendientes:** preservados íntegramente; no se incorporan a esta transacción previa ajena.
- **19 casos con referencias a las páginas retiradas:** enlaces sustituidos por la fuente histórica externa; no reemplazo masivo de números ni cambios de veredicto sin fundamento.

No se añaden casos nuevos ni cambian sus nombres. Cada caso actualizado conserva su entrada en el índice; contadores y fecha del índice ya estaban al 09/10. Se preserva el índice pendiente anterior. Los tags de los casos reescritos se verifican contra el registro existente. La portada aislada de esta transacción se fecha al 09/10/26.

Correcciones de deuda previa separadas del delta: Bodyguard como estática; acciones que entran en la zona de juego durante resolución; resumen de tipos de habilidades sin referencias legacy. La precisión de daño plural en Shift y las referencias de 5.1.1.5 ya estaban cubiertas en la adaptación: se verifican sin fabricar cambios.

## Incidencias del original 2.3

Se vuelven a comprobar las incidencias de 2.2. Se corrigen en el PDF las referencias de 5.1.1.5 a 5.1.1.7 y 5.1.1.6. Continúan el ejemplo con referencia inexistente 1.8.1.5, `Chrisopher`, la redacción de 1.9.4.3 y el ejemplo de 1.9.5, `greater that` en banish/banished y el término anterior conditional static ability del glosario. La cita de Sing Together sigue sin cierre visual, pese a cambios de puntuación. La formulación de variantes de Temporary Shift no resuelve expresamente la ambigüedad antes señalada. La lista 8.1.1 omite Adventurous aunque existe 8.16. No se corrige el binario original ni se presentan estas incidencias como aclaraciones oficiales nuevas.

## Búsqueda y validación

`primary_transition` valida ambos originales y ambos selectores. El índice actual se mantiene con 2.2. Se prueba el límite 15/16/17 de octubre, selección futura 2.3, recuperación de 1.13, 6.1.4.2, 6.7.6.1, 8.1.2 y 8.16, ausencia de 7.1.6.1, exclusión de históricos y lectura sin escrituras. Se actualizan sinónimos, documentación y oráculos de 2.3. Los oráculos previos se ajustan al corpus ya mantenido: Belle está disponible y Wasabi ya es un caso revisado sin procedencia Discord.

Los clientes MCP ya abiertos conservan su módulo Python anterior: deben reiniciar su servidor para cargar los cambios. No se altera su configuración ni se interrumpen servidores de otras sesiones. Los procesos stdio nuevos usados en pruebas cargan el motor actualizado.

Pruebas: 19 de consulta/extracción y transición, 16 de publicación/retirada, 11 de protocolo MCP, incluido el ensayo de lectura futura. No se instalan dependencias. Los fallos iniciales de dos oráculos se debían al mantenimiento previo del corpus, no a pérdida de evidencia: se verifican las fuentes y se corrigen las expectativas.

## Publicación y conservación

La lista exacta está en `cr-2.3-manifiesto.json`. Se publican solo sus rutas y se retiran seis notas 2.2 después de confirmar el reemplazo. Los punteros internos y el PDF 2.2 no estaban publicados; no se retiran por coincidencia de versión. Los PDF, herramientas, matrices e informes quedan fuera de Publish.

Se conservan los cambios previos de Iván. `Empecemos.md` comparte cambios ajenos: para commit y Publish se utiliza el contenido de HEAD más los cambios propios y después se repone el contenido combinado. El registro de tags, índice, Bodyguard, Strange Things y empates previos permanecen fuera del commit.

Los hashes de commit, informes de publicación/retirada y comprobaciones públicas se incorporan al cierre tras verificarlos.
