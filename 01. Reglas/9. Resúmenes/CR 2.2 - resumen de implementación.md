# CR 2.2: resumen de implementación

## Fuentes encontradas

- Comprehensive Rules 2.2.0: `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf`; 55 páginas; efectiva el 9 de julio de 2026.
- Comprehensive Rules 2.1.0: `CRUpdate_2.1.0_EN.pdf`; 49 páginas; efectiva el 30 de abril de 2026.
- *Attack of the Vine Set Release Notes*: `Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf`; 30 páginas.
- Base local de cartas y casos de ejemplo del proyecto.
- Plantillas y estilo Markdown/Obsidian existentes.

## Fuentes no encontradas o incompletas

- La base JSON local no contiene un conjunto completo verificable de las cartas de Attack of the Vine. Los nombres nuevos se comprobaron contra las *release notes* oficiales.
- No se encontró una traducción oficial española completa de CR 2.2; se conservaron los términos ingleses oficiales y se explicaron en español.

## Archivos creados

- `Documentacion Oficial/README.md`.
- `01.1.a Official English Reference – Unmodified/00. Fuente actual.md`.
- `01. Reglas/9. Resúmenes/Reglas completas de Disney Lorcana 2.2 - cambios respecto a 2.1.md`.
- `01. Reglas/9. Resúmenes/CR 2.2 - matriz de diferencias respecto a CR 2.1.md`.
- `01. Reglas/9. Resúmenes/CR 2.2 - comparación final con Attack of the Vine.md`.
- `01. Reglas/9. Resúmenes/CR 2.2 - revisión editorial del PDF oficial.md`.
- `01. Reglas/9. Resúmenes/CR 2.2 - resumen de implementación.md`.

## Archivos modificados

- Portada: `Empecemos.md`.
- Reglas españolas: 1.9, 1.10, 4.3, 4.6, 5.1, 5.3, 5.5, 5.6, 6.1, 6.4, 6.7, 8.4, 8.8, 8.10, 8.12 y `01. Reglas/Glosario.md`.
- Resúmenes: archivo preliminar de Attack of the Vine y resumen de verificaciones del estado del juego.
- Referencia inglesa: secciones 1, 4, 5 y 8; avisos de alcance en sección 6 y glosario.
- Casos: Celia Mae, Christopher Robin, Escape Plan, Rc, Angel, Ming Lee, Sulley & Boo, Dash & Violet, Mickey & Minnie, Morph y Posey.

## Principales cambios funcionales

- Una fuente sigue considerándose que inflige daño aunque los modificadores lo reduzcan a 0; el objeto afectado no recibe daño (1.9.5).
- Las excepciones de construcción exigen que la carta fuente ya sea legal (1.10.1.3).
- Las cartas inferiores adquieren los estados de la superior al cambiar de zona (5.1.1.7).
- No poder pagar un coste unido a *may* equivale a rechazar la opción (6.1.4.1).
- Duo, Combo, Temporary y Potato Shift, soportes no personaje, estados de dos soportes y variantes combinadas (8.10.4.1–8.10.9).

## Principales aclaraciones

- Proceso único de cálculo de daño (1.9.4).
- Último disparo de una carta que queda debajo (4.3.4.2).
- Preparar al desafiante no lo retira del desafío (4.6.4.4).
- Momento de pagos y elecciones durante la resolución (6.7.2–6.7.2.2).

## Cambios editoriales

- Traslado de 6.4.3–6.4.4 a 6.1.15–6.1.16 y cambio a *conditional dependent effects*.
- Renumeración de la antigua 1.9.4 a 1.9.6 y de 6.4.5 a 6.4.3.
- Referencias de daño centralizadas y ejemplos añadidos o precisados.

## Problemas del PDF oficial

- `Chrisopher Robin` (p. 8).
- Referencias inexistentes 1.8.1.5 (p. 7), 5.1.7 y 5.1.6 (p. 19).
- `greater that` en el glosario (p. 46).
- Glosario sin actualizar a *conditional dependent effect* (p. 47).
- Cita sin cierre aparente en Sing Together (p. 43).
- Ambigüedades posibles en el valor numérico del ejemplo de 1.9.5 y en las condiciones combinadas de 8.10.9.

## Resultado del contraste con Vine

Confirmados: cálculo de daño, construcción del mazo, efectos condicionales, pago y elecciones, desafío, estados de pila, clasificaciones, Boost, Resist, Sing Together y las cuatro variantes nuevas de Shift.

Confirmados con matices: daño reducido a 0, Temporary Shift, Temporary [Classification] Shift y aplicación general de Morph. Varios *rulings* de cartas no aparecen literalmente en CR 2.2 y siguen dependiendo de las *release notes* específicas.

No se ha identificado una afirmación central de Vine contradicha de forma directa por CR 2.2; sí hay afirmaciones que no fueron incorporadas como reglas generales.

## Cuestiones pendientes

- Aclaración oficial sobre la cantidad descrita en el ejemplo de 1.9.5.
- Aclaración oficial de qué condiciones exactas se acumulan en Temporary [Classification] Shift (8.10.9).
- Incorporación completa de Attack of the Vine a la base local de cartas y resolución de sus enlaces provisionales.

## Validaciones completadas

- Versión, fecha, idioma y páginas verificados dentro de ambos PDF.
- Comparación textual completa y comprobación independiente del resumen oficial.
- 555 identificadores únicos de regla localizados en CR 2.2.
- Revisión de referencias numéricas y comprobación visual de incidencias.
- Revisión visual global de las 55 páginas mediante hojas de contacto, con inspección ampliada de páginas sospechosas.
- Búsqueda de referencias activas que presentaran CR 2.1 como vigente.
- Revisión del diff y comprobación de espacios y errores de formato.

## Corrección del español

Se realizó una lectura continua de los cuatro entregables principales y una pasada específica de tildes, concordancia, puntuación, espacios, nombres de carta, términos técnicos y consistencia de fechas y versiones. No se detectó *mojibake* en los documentos nuevos.
