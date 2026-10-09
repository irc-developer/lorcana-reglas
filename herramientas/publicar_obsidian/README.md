# Publicación de una duda en Obsidian

El usuario ha autorizado publicar cada duda documentada, con la restricción de subir o actualizar **solo sus archivos**. Esta herramienta ejecuta la CLI oficial con `publish:add path=...`, una ruta por llamada. No publica toda la bóveda, no usa `changed`, no elimina contenido y no amplía la selección siguiendo enlaces.

La selección es explícita: artículo(s), índices, portada y registro de tags que hayan cambiado en la transacción actual. Se admiten Markdown de la sección 11, `Empecemos.md`, `Registro de Tags - Master List.md` y la entrada breve `02. Listado de Cartas/Cartas de Lorcana.md`. Las fichas completas de sets siguen fuera del alcance. Los archivos de configuración, herramientas, fuentes y notas ajenas quedan fuera. Si una duda necesita otros recursos, hay que ampliar el alcance expresamente antes de publicarlos.

Cada ruta debe haber sido añadida o modificada en el commit indicado y su contenido local debe coincidir con ese commit. Para subir, además, el commit debe ser `HEAD` y estar contenido en la rama remota de seguimiento; refresca ese seguimiento después del `push`. El workflow editorial debe haber excluido cambios previos ajenos, incluidos los que compartan un índice con la duda actual.

## Uso

Desde la raíz del repositorio, después de validar y subir el commit de la duda:

```powershell
python -B -X utf8 herramientas/publicar_obsidian/publicar.py --commit HEAD --archivo "01. Reglas/11. Casos de ejemplo y aclaraciones/11.0. Timing y Resolución/Nombre del caso.md" --archivo "01. Reglas/11. Casos de ejemplo y aclaraciones/ÍNDICE - Casos de ejemplo y aclaraciones.md"
```

Sin otra opción solo prepara un plan local. Añade `--comprobar` para verificar la bóveda, el sitio y los pendientes sin subir. Para publicar, sustituye `HEAD` por el hash concreto devuelto en el plan revisado y añade `--aplicar`, conservando la misma selección. Así un avance de la rama no cambia el commit que vas a publicar. Incluye `Empecemos.md` o el registro de tags únicamente si realmente cambiaron en ese commit. No hay selección implícita de todos los archivos del commit.

El informe JSON contiene el hash del commit, las rutas y hashes SHA-256. La comprobación añade el sitio y el número de pendientes ajenos. La publicación distingue `publicados`, `ya_actualizados` y `pendientes` y devuelve enlaces. Ante un fallo se detiene y conserva el informe parcial: no confirma éxito total ni intenta publicar otras rutas. Un archivo ya actualizado en Publish no se vuelve a subir. Verifica también el artículo en su enlace público antes de cerrar la duda.

## Entorno

Requiere Git, Python estándar y la [CLI oficial de Obsidian](https://obsidian.md/help/cli) habilitada, con instalador 1.12.7 o posterior y una sesión Publish válida. Obsidian debe estar abierto. La herramienta identifica la bóveda por su ID en el registro local de Obsidian y comprueba su ruta real para evitar confundir bóvedas con el mismo nombre. En Windows utiliza `obsidian` en PATH o `LOCALAPPDATA/Programs/obsidian/Obsidian.com`.

El 6 de octubre de 2026 se actualizó este PC al instalador 1.14.4, se habilitó la CLI y se comprobó el acceso al sitio `https://publish.obsidian.md/reglas-lorcana` (`www.reglas-lorcana.es`). Esa preparación no publica las notas o herramientas que estén pendientes en la bóveda.

## Migración expresa de las reglas CR 2.3

`publicar.py --perfil reglas` admite los Markdown editoriales de `01. Reglas/`, además de las rutas auxiliares ya permitidas. Exige un `--archivo` por ruta modificada del commit; nunca selecciona una carpeta completa. El perfil predeterminado `dudas` conserva su alcance. PDF, fuentes internas, herramientas y fichas largas siguen excluidos.

La retirada autorizada de las seis notas históricas 2.2 usa `retirar_reglas.py --commit HASH --archivo RUTA --informe-publicacion INFORME_JSON --informe RESULTADO_JSON`. Sin `--aplicar` comprueba el reemplazo ya publicado, el commit subido, la bóveda, hashes y enlaces; con él retira exclusivamente la lista explícita. Conserva los archivos locales y registra éxitos y fallos parciales. La entrada 2.3 y la portada deben estar publicadas primero. La lista permitida está cerrada a las seis páginas inventariadas de esta migración; no afecta al PDF 2.2 ni a secciones cuyo número sea 2.2.

## Retirada expresa del catálogo de cartas

La migración a Lorcast autorizada el 08/10/2026 utiliza `retirar_catalogo.py` como operación específica, separada del workflow de dudas. Recibe un hash subido, el informe de publicación completa de artículos/portada/entrada breve y un `--archivo` por ficha. Verifica exclusiones, enlaces restantes, selección y conservación del corpus local antes de llamar a `publish:remove path=...`. Sin `--aplicar` prepara el informe; con él despublica solo las fichas explícitas y comprueba la lista pública tras cada operación. Nunca borra archivos locales ni retira «Cartas de Lorcana». No usar esta operación en una duda ordinaria sin una autorización expresa para retirar el catálogo.

## Pruebas

```powershell
python -B -X utf8 herramientas/publicar_obsidian/test_publicar.py
```

Las pruebas usan repositorios temporales y una CLI simulada. Comprueban selección de rutas, contenido frente al commit, pendientes ajenos, fallos parciales y publicación de una única duda; no escriben en el sitio real.
