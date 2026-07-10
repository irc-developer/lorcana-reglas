# Contenido Original - Cthulhu: Dark Providence

## Archivo Centralizado de Contenido Crudo

Este archivo registra las fuentes locales usadas para documentar Cthulhu: Dark Providence y como se relacionan con los documentos procesados del repositorio.

Uso autorizado:

- verificar reglas dudosas;
- actúalizar ayudas si aparecen erratas;
- reconstruir secciones del documento principal;
- auditar que las ayudas no contradicen el reglamento.

Evitar:

- copiar grandes bloques del manual dentro de ayudas sinteticas;
- mezclar reglas del modo solitario con multijugador sin marcarlo;
- tratar la hoja-resumen visual como fuente única cuando contradiga el reglamento completo.

---

## Fuentes

| Fuente | Ruta | Estado |
|---|---|---|
| Reglamento ES | [fuentes/DKP001_Reglamento_ES-2.pdf](./fuentes/DKP001_Reglamento_ES-2.pdf) | Leido y extraido a texto |
| Texto extraido | [manual-base.txt](./manual-base.txt) | Generado desde el PDF local con PyMuPDF |
| Hoja-resumen | [fuentes/resumendk.pdf](./fuentes/resumendk.pdf) | Imagen sin texto extraible; inspeccion visual |
| FAQ BGG 1 | [fuentes/Rules FAQ from designer _ BoardGameGeek_1.pdf](./fuentes/Rules%20FAQ%20from%20designer%20_%20BoardGameGeek_1.pdf) | Texto extraido y sintetizado |
| FAQ BGG 2 | [fuentes/Rules FAQ from designer _ BoardGameGeek2.pdf](./fuentes/Rules%20FAQ%20from%20designer%20_%20BoardGameGeek2.pdf) | Texto extraido y sintetizado |

---

## Mapeo de Contenido

| Fuente | Secciones procesadas | Documentos destino |
|---|---|---|
| Reglamento pp. 2-3 | Introducción, descripción, componentes | [Dark-Providence.md](./Dark-Providence.md) |
| Reglamento pp. 4-6 | Lealtad, tableros, cartas, Agentes | [Dark-Providence.md](./Dark-Providence.md), [RESUMEN-Y-GUIA-NOVATO.md](./AYUDAS_JUGADORES/RESUMEN-Y-GUIA-NOVATO.md) |
| Reglamento p. 7 | Preparación | [Dark-Providence.md](./Dark-Providence.md), [RESUMEN-Y-GUIA-NOVATO.md](./AYUDAS_JUGADORES/RESUMEN-Y-GUIA-NOVATO.md) |
| Reglamento pp. 8-14 | Turno, acciones, reclamar, Cordura | [Dark-Providence.md](./Dark-Providence.md), [RESUMEN-TURNO.md](./AYUDAS_JUGADORES/RESUMEN-TURNO.md) |
| Reglamento pp. 15-17 | Final, puntuación, ganador | [Dark-Providence.md](./Dark-Providence.md), [RESUMEN-FINAL-Y-PUNTUACION.md](./AYUDAS_JUGADORES/RESUMEN-FINAL-Y-PUNTUACION.md) |
| Reglamento pp. 18-22 | Modo solitario | [RESUMEN-MODO-SOLITARIO.md](./AYUDAS_JUGADORES/RESUMEN-MODO-SOLITARIO.md) |
| Reglamento p. 24 y `resumendk.pdf` | Hoja-resumen de mesa | [AYUDA-VISUAL-MESA.md](./AYUDAS_JUGADORES/AYUDA-VISUAL-MESA.md) |
| PDFs BGG | Aclaraciones de preparación, acciones gratuitas, Influencia, Profundos, Cthulhu, Cordura, R'lyeh, Disidentes e Impostor | [FAQs-Dark-Providence.md](./FAQs-Dark-Providence.md), [Dark-Providence.md](./Dark-Providence.md), ayudas de jugador |

---

## Integridad

- **Última verificacion contra fuente**: 09/07/2026.
- **Extracción PDF**: el reglamento contiene texto embebido a partir de la página 2; la portada aporta solo título.
- **Limitacion conocida**: `resumendk.pdf` no tiene texto extraible localmente. Se ha usado como apoyo visual, no como única fuente.
- **FAQ/errata**: incorporadas dos capturas PDF locales del hilo BGG con aclaraciones del diseñador.

---

## Protocolo de Actualizacion

1. Si se añade nueva FAQ/errata, actúalizar `FAQs-Dark-Providence.md`.
2. Aplicar primero la correccion al documento principal.
3. Actualizar las ayudas afectadas.
4. Registrar en este archivo que fuente corrige que seccion.
