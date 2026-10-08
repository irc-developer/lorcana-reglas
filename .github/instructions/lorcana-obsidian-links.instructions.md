---
name: lorcana-obsidian-links
description: "Usar cuando redactes o corrijas documentación de reglas de Lorcana en Markdown u Obsidian y necesites validar enlaces internos, citas de reglas o terminología."
---

# Enlaces y terminología de documentación

## Cartas

- En artículos y respuestas de lectura, enlaza cartas mediante `[Texto visible](URL_de_imagen_Lorcast)`, conservando nombre y versión cuando hagan falta para distinguirlas. Los enlaces internos que siguen se aplican a reglas y artículos, no a fichas de cartas.
- Verifica primero la ficha completa en el archivo del set de `02. Listado de Cartas/`. Las fichas se conservan localmente para evidencia y no se publican como catálogo extenso.
- Consulta `.github/planes/mapa-cartas-lorcast.json` por archivo y epígrafe, o recupera el registro exacto de Lorcast y lee `image_uris.digital.large`. Conserva la URL completa con su parámetro de actualización. Nunca construyas una URL por nombre/ID ni elijas el primer resultado de una búsqueda ambigua.
- Comprueba nombre, versión, set, idioma e impresión; para traducciones verifica la correspondencia y rotula el idioma correctamente. Si falta cobertura, comunica la excepción y resuélvela sin enlazar otra versión ni inventar un destino. `consulta:` no permite escribir el mapa o descargar una caché a disco.
- La API se consulta una vez por set o carta necesaria, reutilizando datos descargados al menos 24 horas y espaciando solicitudes 50–100 ms. Las imágenes se revisan al mantener el set o detectar un enlace roto, sin introducir peticiones de API al abrir cada artículo.
- La atribución general a Lorcast vive en `Empecemos.md`; no repitas información técnica sobre la API en cada duda.

## Reglas y artículos

- Prefiere enlaces simples al nombre exacto del archivo cuando el destino sea inequívoco.
- Si el nombre del archivo no basta o la validación falla, usa la ruta completa sin anchors.
- No uses anchors `#...` para referencias de reglas si puedes resolver el enlace por archivo.
- Cita reglas con texto visible en castellano.
- Verifica que el archivo citado exista y que la sección o el epígrafe referenciados sean válidos antes de cerrar la edición.
- Si una sección parece imposible, comprueba antes que el rango numerado de esa carpeta la admita.
- Mantener la terminología de zonas en castellano según la instrucción de alcance.
- No introducir enlaces a fuentes fuera del alcance normativo para justificar un ruling.
- Si una ruta o un epígrafe no están confirmados, detenerse y corregir la referencia antes de cerrar.

Complementa esta instrucción con [lorcana-file-hygiene.instructions.md](lorcana-file-hygiene.instructions.md) cuando haya problemas de codificación o estructura.
