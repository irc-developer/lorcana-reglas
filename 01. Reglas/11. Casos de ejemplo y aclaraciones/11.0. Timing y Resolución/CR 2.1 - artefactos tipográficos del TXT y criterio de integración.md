# CR 2.1 - artefactos tipográficos del TXT y criterio de integración

## Qué se ha detectado

Durante la revisión del TXT plano de CR 2.1 aparecen artefactos de espaciado y OCR que no afectan al contenido normativo, pero sí a la legibilidad del documento. Entre ellos se ven palabras pegadas o partidas de forma irregular, como por ejemplo:

- `metonly` / `gamestate` en el nuevo 1.8.5
- `achoice` / `choiceor` alrededor de 6.1.3.1 y 6.7.3
- pérdidas de espacio en expresiones como `alleffects`, `topof`, `doesn't matter.There`
- glifos de iconos mal exportados en reglas con símbolos, como 4.5.1.4, donde el original debe referirse al icono de lore y la extracción puede degradarlo hasta hacerlo parecer el de voluntad

## Referencia rápida de símbolos extraídos

La exportación a texto plano no conserva bien varios iconos del documento oficial. Como referencia práctica, estos son los casos más útiles al leer el TXT o la capa textual del PDF:

| Símbolo o concepto original | Suele aparecer al extraer | Lectura correcta |
| --- | --- | --- |
| `{S}` | `#` | Fuerza |
| `{W}` | `!` | Voluntad |
| icono de exert | `!` | Agotar |
| icono de lore | `!` | Lore |
| `{C}` | `"` | Coste |
| `{I}` | `"` | Inkwell |
| `{M}` | `{M}` | Movimiento |

La consecuencia es que `!` y `"` no pueden interpretarse de forma automática fuera de contexto. Cuando una frase habla de ganar lore, questear, exertar o comparar Willpower, el significado correcto hay que reconstruirlo por contexto y no por el carácter ASCII exportado.

## Criterio aplicado al integrar el repositorio

- No se han tratado estos artefactos como cambios de reglas.
- Cuando el sentido del texto era inequívoco y coincidía con el change log oficial, la redacción se ha normalizado al integrarla en castellano.
- Cuando el problema era puramente de exportación a texto plano, no se ha trasladado al repositorio.

## Por qué no se consideran cambios normativos

La propia actualización oficial distingue entre cambios de reglas y cambios editoriales menores. En otras palabras: no todo lo que cambia en el TXT plano cambia cómo funciona Lorcana. El criterio seguido aquí ha sido separar:

1. Los cambios con efecto real de reglas, resumidos en [[01. Reglas/9. Resúmenes/Actualización CR 2.1 - resumen de cambios|Actualización CR 2.1 - resumen de cambios]].
2. Los artefactos del TXT o correcciones menores de redacción, que no alteran el funcionamiento de las reglas.

## Reglas cuyo texto se integró atendiendo a ese criterio

- [[01. Reglas/4. Acciones de turno (Turn Actions)/4.5 Irse de aventura (Quest)#4.5.1.4. Ganar lore|4.5.1.4]]: el paso debe referirse al valor de lore del personaje. Si en la extracción del PDF o del TXT aparece un glifo que se lee como voluntad, se trata de un artefacto tipográfico y no de un cambio normativo.
- [[01. Reglas/1. Principios generales/1.8. Chequeo del estado del juego (Game State Check)#1.8.5. Las condiciones solo se cumplen cuando ocurre el GSC|1.8.5]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.1. General (General)#6.1.3.1. Requisitos y limitadores|6.1.3.1]]
- [[01. Reglas/6. Habilidades, efectos y resolución (abilities, effects, and resolving)/6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)#6.7.3. Legalidad de elecciones y selecciones|6.7.3]]

## Nota editorial adicional

El índice de aclaraciones arrastraba una inconsistencia previa entre el total declarado y la suma real de casos. Al añadir esta página se ha dejado el recuento cuadrado con el contenido actual del repositorio.

#cr-2-1 #erratas #ocr #txt #editorial #integracion #timing #resolucion