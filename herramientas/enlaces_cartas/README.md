# Enlaces de cartas de Lorcast

Las fichas de `02. Listado de Cartas/` se conservan como evidencia local. Los artículos públicos enlazan la imagen exacta de Lorcast, y «Cartas de Lorcana» es una entrada breve al buscador externo. La portada contiene la atribución general.

El [mapa versionado](../../.github/planes/mapa-cartas-lorcast.json) identifica cada destino local con nombre, versión, set, número, idioma, ID de Lorcast y URL completa de `image_uris.digital.large`. Las URL no se construyen ni se eliminan sus parámetros. La fecha registrada corresponde a la descarga de esta migración.

`migrar.py` prepara o aplica las sustituciones de enlaces internos resueltos. Usa datos previamente descargados: no hace peticiones de red, no cambia fichas, no publica y no modifica los modos del MCP. En futuras revisiones se debe comprobar la fecha de los datos y refrescar el mapa con el registro exacto de la API antes de introducir enlaces nuevos o reparar destinos.

```powershell
python -B -X utf8 herramientas/enlaces_cartas/migrar.py --cache .codex_tmp/lorcast-2026-10-08
python -B -X utf8 herramientas/enlaces_cartas/migrar.py --cache .codex_tmp/lorcast-2026-10-08 --aplicar
python -B -X utf8 herramientas/enlaces_cartas/test_migrar.py
```

El cache contiene `set-1.json` … `set-14.json`, descargados de `https://api.lorcast.com/v0/sets/<codigo>/cards`. Los datos deben reutilizarse al menos 24 horas y las peticiones a la API espaciarse 50–100 ms. No descargar ni actualizar el mapa durante una `consulta:` de solo lectura. Los cambios de artículos se revisan y publican con un manifiesto explícito.

Los generadores de artículos pueden llamar a `enlace_verificado(set_name, heading, label)`; una carta ausente del mapa produce un error, nunca un enlace interno de respaldo que apunte a una ficha despublicada.
