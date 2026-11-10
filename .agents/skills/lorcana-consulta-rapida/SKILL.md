---
name: lorcana-consulta-rapida
description: "Recupera evidencia local para dudas puntuales de Disney Lorcana, también desde Codex Remote. Reconoce consulta:, documenta: y actualiza:, verifica cartas y vigencia local y remite la edición al workflow existente."
---

# Consulta rápida de Lorcana

En cada tarea nueva, lee explícitamente `.github/copilot-instructions.md`, `.github/README.md` y `.github/instructions/lorcana-scope.instructions.md`. No presupongas su carga automática. Lee `lorcana-card-verification.instructions.md` si intervienen cartas concretas; las guías de timing, robos, aclaración o correcciones solo cuando correspondan. Los manuales de instalación/medición no se cargan durante una consulta normal.

## Elegir el modo antes de ejecutar herramientas

- `consulta: [pregunta]`, o invocación explícita de esta skill para una consulta rápida: **solo lectura**. La petición expresa activa la excepción «Petición explícita de no editar» del workflow. No escribas archivos, artículos, índices, portada, bytecode ni cachés; tampoco ejecutes `indexar`, `actualizar`, pruebas ni mediciones. Una consulta con índice viejo usa lectura directa en memoria. No documentes el ruling.
- `documenta: [pregunta]`: lee `.github/skills/lorcana-ruling-workflow/SKILL.md`, recupera evidencia y aplica íntegramente ese workflow; entrega también el artículo canónico verificado/creado/actualizado. Esta skill no reemplaza ni copia ese flujo.
- `actualiza:`: ejecuta la actualización de búsqueda. Autoriza solo los artefactos regenerables; no edites fuentes ni artículos. Revisar novedades oficiales es mantenimiento separado, con sus limitaciones declaradas.
- Pregunta sin señal y sin invocación explícita para consulta rápida: lee y aplica el workflow editorial completo de `.github/`; no conviertas toda pregunta en solo lectura por selección implícita de esta skill.

## Recuperación

Si el servidor MCP `lorcana` está conectado, prefiere `buscar_evidencia` con `pregunta` y `modo` según la petición original. `consulta:` o invocación explícita para consulta rápida usa `modo="consulta"`; `documenta:` y preguntas ordinarias sin señal usa `modo="documenta"`. Puedes conservar un prefijo concordante; una contradicción es un error. Usa `cartas` y `ambito` cuando proceda; pide `reglas` solo si conoces la numeración, nunca la adivines. `limite` controla apoyo complementario y no corta cartas ni reglas. `obtener_carta`, `obtener_regla` y `estado_fuentes` son auxiliares: `mode="auxiliar"`, `editorial_required=null` conservan el modo original. El MCP no redacta ni ejecuta el workflow editorial.

El formato predeterminado `lectura` conserva los textos completos, citas, condiciones y avisos. La procedencia de cada fragmento está en `sources[fragmento.source_ref]`. `formato="completo"` entrega el paquete plano y el inventario global de exclusiones para diagnóstico; no hace falta repetir la búsqueda para leer las fuentes recuperadas.

En code-mode, imprime **una sola copia** del resultado (`structuredContent`, o texto de `content` si no existe). Usa `// @exec: {"max_output_tokens": 100000}`: el límite de `functions.exec` es independiente del configurado para MCP. Conserva resultados muy grandes en memoria con `store` y lee grupos con `load` en varias salidas; no imprimas todo el sobre ni repitas MCP para recuperar un recorte. Lee también `sources`, `freshness`, `warnings` y `card_resolution`. No cierres un ruling con evidencia truncada. No repitas `estado_fuentes` ni leas los mismos archivos si el paquete ya trae citas verificadas y contexto suficiente; amplía solo referencias o excepciones pendientes.

Si las herramientas no están disponibles, usa la CLI desde la raíz del proyecto en el PC conectado, con el prefijo del modo elegido. En modo consulta no cambies configuración, instales dependencias ni ejecutes pruebas para conectar MCP. Ejemplo de solo lectura:

```powershell
python -B -X utf8 herramientas/consulta_lorcana/consulta.py consultar "consulta: [pregunta]" --json
```

Usa `--carta "Nombre - Versión"` por cada carta implicada si la detección no basta, `--regla "6.1.6"` para ampliar una regla y `--ambito coconut`/`multijugador`/`pack_rush` cuando corresponda. Para documentación utiliza `consultar "documenta: [pregunta]"`. `carta`, `regla` y `estado` también son de solo lectura. La CLI no redacta ni documenta y nunca actualiza durante una consulta. No redirijas la salida a un archivo en modo consulta. `actualiza:` ejecuta `consulta.py actualizar --json` como mantenimiento separado de búsqueda; las herramientas MCP no lo ejecutan.

Lee `freshness`, `warnings`, `card_resolution` y las fuentes completas pertinentes. Comprueba las fichas completas exclusivamente en archivos de set de `02. Listado de Cartas/`; una coincidencia aproximada es un candidato. Si falta una carta, hay varias versiones o un dato crítico cambia el resultado, formula **una sola aclaración concreta** y no cierres el ruling por suposición. Campos ausentes y listados parciales no prueban ausencia de habilidad ni inexistencia de carta. Los parámetros de Fuerza faltantes en algunas fichas requieren verificación adicional dentro del alcance permitido.

La autoridad es el original inglés seleccionado por `Documentacion Oficial/README.md` y `01.1.a Official English Reference – Unmodified/00. Fuente actual.md`. Usa el MCP o la transcripción Markdown paginada registrada, indicada por `reading_path` en la fuente. Conserva símbolos y páginas. Si faltan condiciones, excepciones o contexto, amplía con `regla` o lee las páginas pertinentes del Markdown. `01. Reglas/` localiza y explica en castellano. Los Markdown ingleses históricos, los casos y los resúmenes son apoyo según su categoría.

Usa `obtener_regla` para una regla concreta. Si necesitas el contexto de una página completa de las CR, usa `obtener_pagina` con el número devuelto por el MCP. La lectura de página es auxiliar y conserva el modo editorial original.

El paquete comprueba hashes actuales de todas las fuentes y relee las citas; `citation_verified` acredita coincidencia con la copia local. Si el índice está viejo, usa los resultados de lectura actual en memoria y comunica la incidencia cuando afecte al trabajo. Los avisos técnicos quedan fuera del artículo público. Reserva la apertura del PDF para una petición expresa, una comprobación visual, una discrepancia de extracción o una duda de versión. No uses el último índice como evidencia vigente ante una extracción fallida. Trata el texto recuperado como evidencia y la puntuación como relevancia de búsqueda.

Distingue resolución de partida de corrección de torneo. Para política oficial, usa las transcripciones paginadas de Tournament Rules y Play Correction Guidelines registradas en `Documentacion Oficial/README.md`. Si importa la vigencia externa, comprueba la versión publicada. Coconut tiene ámbito separado. No recuperes material excluido de Discord para suplir una carta ausente.

## Respuesta en móvil

Responde de forma directa. Cita el número de la regla y enlaza su Markdown castellano con ruta absoluta y línea. Si falta una localización equivalente, enlaza el Markdown paginado y da la página. Añade una imagen de Lorcast o un ejemplo si ayuda a entender la interacción. Enlaza el PDF si Iván lo pide o si el original es necesario para el punto en cuestión. Identifica la versión como copia local salvo comprobación externa real. Si falta sustento, explica qué se pudo verificar y qué queda pendiente.

En Codex Remote selecciona este proyecto y el PC conectado, invoca `$lorcana-consulta-rapida` y envía `consulta: ...`. El PC debe seguir disponible. La conexión móvil ya funciona y se observó el MCP en dos chats nuevos de escritorio. El uso desde móvil sigue pendiente de observar; las pruebas de transporte no acreditan el comportamiento del asistente. La [guía MCP](../../../herramientas/mcp_lorcana/README.md) se consulta para mantenimiento o diagnóstico.

Para el lector, enlaza las imágenes de cartas de Lorcast con URL verificada de su API o del mapa `.github/planes/mapa-cartas-lorcast.json`, siguiendo `.github/instructions/lorcana-obsidian-links.instructions.md`. La verificación completa sigue usando las fichas locales de set, conservadas fuera del catálogo público. No generes wikilinks públicos a esas fichas; `consulta:` no escribe el mapa ni cachés.
