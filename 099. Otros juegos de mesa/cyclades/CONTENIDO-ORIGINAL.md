# Contenido original - Cyclades: Edición Legendaria

## Propósito

Este archivo identifica las fuentes crudas, su edición y el uso permitido dentro de la documentación. Sirve para auditar reglas sin confundir la Edición Legendaria con el Cyclades clásico.

## Fuentes locales

| Fuente | Tipo | Edición | Estado | Uso |
|---|---|---|---|---|
| [`doc/[C]_Rulesbook_-_VERSION_KS_-_Master_Es__05062024.pdf`](./doc/%5BC%5D_Rulesbook_-_VERSION_KS_-_Master_Es__05062024.pdf) | Escaneo español, 20 páginas | Edición Legendaria; contenido equivalente al retail ES | Fuente principal | Terminología, componentes y reglas completas |
| [`manual-base.txt`](./manual-base.txt) | OCR español | Derivado del escaneo | Completo, con separadores de página | Búsqueda y auditoría; puede contener errores OCR |
| [`doc/Cyclades_v5.pdf`](./doc/Cyclades_v5.pdf) | Ayuda de Universal Head, 13 páginas | Cyclades clásico + Hades, Titans, Monuments y C3K | Fuente secundaria | Contrastar mecanismos heredados, nunca sustituir la regla Legendaria |
| [`resumen-ingles-v5.txt`](./resumen-ingles-v5.txt) | Extracción de texto | Derivado de v5 | Completo, con separadores de página | Búsqueda auxiliar |

## Fuentes externas verificadas

| Fuente | Autoridad | Uso |
|---|---|---|
| [Página oficial de la edición](https://open-sesame.games/cyclades-legendary-edition/) | Open Sesame Games | Identidad de edición y cambios generales |
| [Reglamento inglés seleccionable](https://meepletron-storage.s3.us-east-2.amazonaws.com/resources/cycldes-legendary-edition-rulebook.pdf) | Copia digital de reglas de la edición | Contraste de OCR y redacción |
| [FAQ oficial de Studio H](https://boardgamegeek.com/filepage/308663/cyclades-legendary-edition-faq-by-studio-h) | Editorial | Registro de existencia y futuras revisiones |

## Mapeo de contenido

| Páginas ES | Contenido | Documento procesado |
|---:|---|---|
| 1 | Objetivo y componentes | `Cyclades.md` |
| 2 | Preparación y colocación | `Cyclades.md`, guía novato |
| 3-5 | Ciclo, ingresos, Ofrendas y acciones | `Cyclades.md`, resumen de turno |
| 5-9 | Dioses, movimiento y combate | `Cyclades.md`, referencia de Dioses y combate |
| 9-11 | Héroes, Apolo, Metrópolis, Criaturas y Movimiento Heroico | Documento principal y ayudas |
| 12 | Equipos y 2 jugadores | Documento principal y FAQ |
| 13-15 | Criaturas y Héroes | Referencia de Criaturas y Héroes |
| 16-19 | Disposiciones recomendadas | Conservadas en el PDF; no reproducidas porque dependen del diagrama |
| 20 | Índice | Control de cobertura |

## Protocolo de consulta

1. Busca primero la regla procesada en `Cyclades.md` o en una ayuda.
2. Si hay duda, localiza la página mediante el separador `===== PAGINA N =====` de `manual-base.txt`.
3. Comprueba visualmente esa página en el PDF, porque el OCR puede confundir `1/I`, nombres decorativos o el orden de columnas.
4. Si el resumen v5 contradice la Edición Legendaria, prevalece el reglamento español Legendario.
5. Las interacciones no cubiertas deben contrastarse con la FAQ oficial antes de incorporarse como errata.

## Integridad

- Escaneo: 20/20 páginas legibles y revisadas visualmente.
- OCR: 20/20 páginas procesadas; las páginas 16-19 son principalmente mapas y contienen poco texto reconocible.
- Resumen v5: 13/13 páginas extraídas.
- Última verificación: 14/07/2026.
