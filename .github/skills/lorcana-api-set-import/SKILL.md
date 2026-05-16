---
name: lorcana-api-set-import
description: 'Recupera un set nuevo de lorcana-api y lo convierte en un articulo de la seccion 2 siguiendo el patron del repositorio. Usar cuando el usuario pida traer el set 12, importar un set futuro desde lorcana-api, crear un articulo nuevo con cartas de un set o comprobar si un set ya existe en la API.'
argument-hint: 'Indica el numero del set objetivo y si quieres solo verificar disponibilidad o crear el articulo nuevo en 02. Listado de Cartas.'
user-invocable: true
---

# Lorcana API Set Import

## Cuando usar

Usa esta skill cuando el usuario pida cualquiera de estos trabajos:

- Traer el set 12 cuando aparezca en lorcana-api.
- Verificar si un set nuevo ya esta disponible en la API.
- Crear un articulo nuevo en la seccion 2 con las cartas de un set.
- Importar un set futuro desde lorcana-api sin repetir la investigacion.

## Objetivo

Resolver de forma corta y verificable dos pasos:

1. Confirmar si el set existe realmente en lorcana-api.
2. Si existe, descargar sus cartas y transformarlas en un articulo nuevo dentro de 02. Listado de Cartas siguiendo el patron del repo.

## Reglas operativas

1. Confirmar siempre la existencia del set desde https://api.lorcana-api.com/sets/all; no inferirla desde /cards.
2. Si /sets/all no contiene el Set_Num pedido, detenerse y no inventar cartas ni articulo.
3. Guardar del set al menos Name, Set_ID, Set_Num y Cards.
4. Para descargar cartas, preferir https://api.lorcana-api.com/cards/fetch?search=Set_Num=<numero>.
5. El filtro por Set_ID tambien funciona y sirve de respaldo: https://api.lorcana-api.com/cards/fetch?search=Set_ID=<codigo>.
6. En la comprobacion rapida puede usarse displayonly para reducir ruido.
7. En la descarga final del set no usar displayonly si hace falta generar el articulo completo.
8. Comparar el numero de cartas recibidas con el campo Cards del set. Si no coincide, paginar antes de redactar.
9. El artículo debe seguir el patrón de los archivos de set de ../../02. Listado de Cartas, por ejemplo ../../02. Listado de Cartas/Set 12 - Wilds Unknown.md; si se crea como archivo independiente, también el de ../../02. Listado de Cartas/Illumineer's Quest - Palace Heist.md.
10. Crear un articulo nuevo dentro de 02. Listado de Cartas salvo instruccion distinta del usuario.
11. Si se modifica cualquier archivo del repo, revisar Empecemos.md y mantener el formato exacto de la fecha: *Ultima actualizacion dd/mm/aa*.

## Procedimiento

1. Consultar https://api.lorcana-api.com/sets/all?displayonly=Name;Set_ID;Set_Num;Cards y localizar el Set_Num pedido.
2. Si existe, guardar Name, Set_ID y Cards esperadas.
3. Descargar las cartas con https://api.lorcana-api.com/cards/fetch?search=Set_Num=<numero>&pagesize=500.
4. Si conviene validar el codigo corto o el filtro anterior falla, usar https://api.lorcana-api.com/cards/fetch?search=Set_ID=<codigo>&pagesize=500.
5. Verificar que el total recibido coincide con Cards del paso 2. Si no coincide, repetir con paginacion.
6. Ordenar las cartas por Card_Num.
7. Redactar un articulo nuevo en 02. Listado de Cartas con:
   - encabezado del set
   - una seccion ## por carta
   - linea de coste, tipo, color, tinta y rareza
   - linea de fuerza, voluntad y lore solo en personajes
   - linea de set e imagen
   - bloque de habilidades cuando haya Body_Text
   - separador ---
8. Mantener saltos de linea legibles cuando Body_Text o Flavor_Text traigan varias lineas.
9. Validar visualmente que el articulo respeta el patron existente antes de cerrar.

## Receta minima ya validada

- Comprobacion del set: https://api.lorcana-api.com/sets/all
- Filtro funcional por numero: https://api.lorcana-api.com/cards/fetch?search=Set_Num=11&pagesize=5
- Filtro funcional por codigo: https://api.lorcana-api.com/cards/fetch?search=Set_ID=WIN&pagesize=5
- Sintaxis de busqueda: search=clave=valor
- Sintaxis de reduccion de columnas: displayonly=columna1;columna2;columna3

## Campos utiles para el articulo

- Name
- Cost
- Type
- Color
- Inkable
- Rarity
- Strength
- Willpower
- Lore
- Body_Text
- Flavor_Text
- Image
- Set_Name
- Set_ID
- Set_Num
- Card_Num

## Referencias

- [Patrón de artículo de set](../../02. Listado de Cartas/Set 12 - Wilds Unknown.md)
- [Patron de articulo independiente](../../02. Listado de Cartas/Illumineer's Quest - Palace Heist.md)
- https://lorcana-api.com/docs/sets/fetching-sets
- https://lorcana-api.com/docs/cards/parameters/search-parameter
- https://lorcana-api.com/docs/cards/parameters/displayonly-parameter