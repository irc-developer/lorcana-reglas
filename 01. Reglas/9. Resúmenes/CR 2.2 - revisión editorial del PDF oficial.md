# CR 2.2: revisión editorial, técnica y estructural del PDF oficial

## Inventario y validación de fuentes

| Archivo | Ruta | Tipo de documento | Versión declarada | Fecha efectiva | Idioma | Páginas | Papel en el análisis | Autoridad | Observaciones de extracción |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- |
| `Comprehensive-Rules_2.2.0-EN.pdf` | `Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf` | Comprehensive Rules oficiales | 2.2.0 | 9 de julio de 2026 | Inglés | 55 | Fuente normativa actual | 1 | Completo y legible. La capa de texto sustituye algunos símbolos y altera ocasionalmente el orden al final de página; se verificaron visualmente las incidencias. |
| `CRUpdate_2.1.0_EN.pdf` | `CRUpdate_2.1.0_EN.pdf` | Comprehensive Rules oficiales | 2.1.0 | 30 de abril de 2026 | Inglés | 49 | Base oficial de comparación | 2 | Completo y legible. Presenta las mismas limitaciones de extracción de símbolos. |
| `Attack-of-the-Vine-Set-Release-Notes_EN.pdf` | `Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf` | Notas oficiales de lanzamiento | No aplica | No declara fecha efectiva de CR | Inglés | 30 | Aproximación previa y *rulings* del set | 4 para esta comparación | Completo. No sustituye el reglamento 2.2. |
| `Disney-Lorcana-Comprehensive-Rules-020526-EN-Edited.pdf` | `Documentacion Oficial/Disney-Lorcana-Comprehensive-Rules-020526-EN-Edited.pdf` | Comprehensive Rules oficiales anteriores | 2.0.1 | 5 de febrero de 2026 | Inglés | 50 | Candidato descartado como 2.1 | Fuera de la comparación | El nombre del archivo podía inducir a error; el interior confirma 2.0.1. |
| `comprehensive-rules-020526-en.pdf` | `comprehensive-rules-020526-en.pdf` | Comprehensive Rules oficiales anteriores | 2.0.1 | 5 de febrero de 2026 | Inglés | 50 | Duplicado funcional del candidato anterior | Fuera de la comparación | No es la versión 2.1. |

Los metadatos del PDF 2.2 identifican el título interno `S13_CRUpdate_2.2.0-EN`; la primera página declara de forma inequívoca **Version 2.2.0** y **Effective July 9, 2026**. El PDF 2.1 declara **Version 2.1.0** y **Effective April 30, 2026**. Ninguno es una vista previa ni una transcripción comunitaria.

## Método de revisión

Se extrajo y leyó el texto de las 55 páginas, incluidas reglas, ejemplos, glosario y resúmenes de actualización. Se enumeraron 555 identificadores de regla únicos, se comprobaron duplicados y referencias numéricas, se buscaron patrones tipográficos sospechosos y se comparó el texto completo con 2.1. Las páginas con truncamientos, símbolos dudosos, cambios de página o posibles errores se renderizaron y comprobaron visualmente.

La revisión distingue errores del PDF de problemas de extracción. Los símbolos de Fuerza, Voluntad, Lore, tinta y agotamiento que aparecen como `#`, `$`, `%`, `"` u otros caracteres en el TXT son **problemas de extracción**, no defectos visuales del PDF.

## Incidencias encontradas

| Página | Regla o sección | Texto o problema detectado | Clasificación | Explicación | Corrección propuesta | Nivel de confianza |
| ---: | --- | --- | --- | --- | --- | --- |
| 7 | 1.8.3, ejemplo B | Remite a `section 1.8.1.5`. | Cross-reference problem | La regla 1.8.1.5 no existe. Personajes y localizaciones están reunidos en 1.8.1.4. La referencia ya era incorrecta en 2.1. | Sustituir `1.8.1.5` por `1.8.1.4`. | Alta |
| 8 | 1.9.4.3 | `from the challenge or same effect` | Editorial inconsistency | Falta un determinante antes de *same effect* y la coordinación es poco natural. | `from the same challenge or the same effect`. | Media |
| 8 | 1.9.4.3, ejemplos A y B | `the total number of damage` | Terminology inconsistency | La propia regla usa *total amount of damage*. *Damage* es incontable en este contexto. | `the total amount of damage`. | Alta |
| 8 | 1.9.5, ejemplo | `Smash deals 3 damage, but Namaari takes 0 damage` | Possible ambiguity | 1.9.4 acaba de definir la cantidad total después de modificadores como 0. La intención de 1.9.5 parece ser que Smash sigue considerándose que «deals damage», no que la cantidad final siga siendo 3. | `Smash is still considered to deal damage, but Namaari takes 0 damage...` o una formulación oficial que separe condición y cantidad. | Media |
| 8 | 1.10.1.3, ejemplo | `Chrisopher Robin – Hunny Sage` | Confirmed error | El nombre oficial mostrado en el resto del ejemplo y en las *release notes* es *Christopher Robin – Hunny Sage*. Falta una `t`. | `Christopher Robin – Hunny Sage`. | Alta |
| 19 | 5.1.1.5 | `see 5.1.7` | Cross-reference problem | No existe 5.1.7; el estado *In a stack* es 5.1.1.7. Error heredado de 2.1. | `see 5.1.1.7`. | Alta |
| 19 | 5.1.1.5 | `see 5.1.6` | Cross-reference problem | No existe 5.1.6; *On top* es 5.1.1.6. Error heredado de 2.1. | `see 5.1.1.6`. | Alta |
| 19 | 5.1.1.7 | `In a stack -` | Editorial inconsistency | Los demás estados emplean raya (`–`) entre término y definición. | Sustituir el guion por la raya usada en 5.1.1.1–5.1.1.6. | Alta |
| 43 | 8.10.9 y ejemplo | «all conditions ... must be fulfilled», seguido de un ejemplo que solo menciona clasificación y retorno | Possible ambiguity | Temporary Shift incluye una condición de mismo nombre; el ejemplo de Temporary Red Panda Shift describe como condiciones útiles la clasificación Red Panda y el disparo retardado. No queda inequívoco si el requisito de mismo nombre también se acumula o si [Classification] lo sustituye. | Aclarar qué cláusulas de cada variante se combinan y cuáles se sustituyen. | Media |
| 43 | 8.12.1 | La cita que define Sing Together comienza con comillas pero no muestra cierre antes de `where N...`. | Confirmed error | La definición citada queda tipográficamente abierta. La inspección visual confirma que no es un artefacto de extracción. | Añadir la comilla de cierre tras `ink cost of the song.` | Alta |
| 46 | Glosario, `banish/banished` | `greater that its Willpower` | Confirmed error | Debe emplearse *than*, no *that*. Error heredado de 2.1. | `greater than its Willpower`. | Alta |
| 47 | Glosario, `conditional static ability` | Mantiene el término anterior y no incluye `conditional dependent effect`. | Terminology inconsistency | Las reglas 6.1.15–6.1.16 y el resumen de cambios afirman que el concepto ha cambiado de nombre, pero el glosario no se actualizó. | Sustituir la entrada anterior por `conditional dependent effect` y su definición general. | Alta |
| 54 | Update Summary, 6.1.4.1 | El resumen afirma «chooses not to pay ... or can’t pay», mientras 6.1.4.1 solo menciona *unable to pay*. | Editorial inconsistency | El resultado completo se obtiene combinando 6.1.4 con 6.1.4.1, pero la viñeta atribuye ambos supuestos al nuevo apartado. | Indicar que la elección está en 6.1.4 y la imposibilidad en 6.1.4.1. | Media |
| 55 | Previous Update Summaries | `6.1.6.  Adjusted` | Formatting problem | Hay dos espacios después del número. No altera el significado. | Usar un solo espacio. | Alta |
| Varias | Capa de texto | Símbolos sustituidos y párrafos aparentemente truncados al final de página. | Extraction problem | La inspección visual de las páginas 8, 10, 26, 30, 31, 34–36, 41–43, 54 y 55 confirmó que los ejemplos continúan en la página siguiente y los símbolos se renderizan correctamente. | No corregir el PDF por esta causa; usar inspección visual o extracción con mapeo de fuentes. | Alta |

## Comprobación estructural

- No se han detectado números de regla duplicados en el documento visual. La duplicación de 2.2.2.1 observada en una extracción se debe al orden de lectura de la capa de texto; la página 10 muestra correctamente 2.2.2.1, 2.2.2.2 y 2.2.2.3.
- La jerarquía principal 1–10 y las secciones 1.1–10.2 mantienen orden coherente.
- Las referencias inexistentes confirmadas son 1.8.1.5, 5.1.7 y 5.1.6.
- La tabla de contenidos coincide con los encabezados principales.
- No se han observado texto solapado, tablas rotas, texto fuera del área útil ni símbolos visualmente ausentes en las páginas comprobadas.
- Los cambios de color azul y naranja se usan como indicación editorial, pero no se han empleado como única fuente para la comparación.

## Nombres de cartas y terminología

Los nombres nuevos se verificaron contra las *Attack of the Vine Set Release Notes*, fuente oficial disponible para el set. La base JSON local no contiene todavía todos los registros del set 13; por ello, para *Christopher Robin – Hunny Sage*, *Sun Yee – Red Panda Spirit*, *Sulley & Boo – Scare Buddies* y las demás cartas nuevas, la verificación se basa en el PDF oficial de lanzamiento. Esta limitación queda reflejada y no se ha presentado la base local como completa.

## Resultado editorial

El PDF es completo y utilizable como fuente normativa, pero contiene al menos seis errores inequívocos: el nombre `Chrisopher`, tres referencias inexistentes, `greater that` y la falta de cierre de comillas en Sing Together. El glosario tampoco refleja el nuevo término *conditional dependent effect*. Las ambigüedades de 1.9.5 y 8.10.9 requieren aclaración humana u oficial antes de convertir una interpretación en regla.
