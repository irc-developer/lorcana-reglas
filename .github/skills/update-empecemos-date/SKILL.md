---
name: update-empecemos-date
description: "Usar cuando una tarea implique crear, modificar, renombrar o eliminar archivos en este repositorio y haya que actualizar la fecha de Empecemos.md y revisar los índices manuales afectados por artículos nuevos o movidos."
---

# Actualizar fecha de Empecemos e índices manuales

## Objetivo

Mantener sincronizada la portada del proyecto en [Empecemos.md](Empecemos.md) cada vez que una tarea cambie archivos del workspace.

Además, cuando la tarea cree, renombre, mueva o elimine artículos dentro de secciones con índice manual, mantener ese índice actualizado en la misma operación.

## Flujo

1. Identifica si la tarea ha producido cambios reales en archivos del repositorio.
2. Si hubo cambios, actualiza la línea de fecha de [Empecemos.md](Empecemos.md) al día real del cambio.
3. Conserva el formato exacto `*Última actualización dd/mm/aa*`.
4. Si la fecha ya coincide con el día actual, no hagas más cambios en [Empecemos.md](Empecemos.md).
5. Si la tarea crea, renombra, mueve o elimina un artículo en una carpeta con índice manual, localiza ese índice y actualízalo en la misma sesión.
6. En el caso de [01. Reglas/11. Casos de ejemplo y aclaraciones/ÍNDICE - Casos de ejemplo y aclaraciones.md](01.%20Reglas/11.%20Casos%20de%20ejemplo%20y%20aclaraciones/%C3%8DNDICE%20-%20Casos%20de%20ejemplo%20y%20aclaraciones.md), esto es obligatorio cada vez que cambie el contenido de sus subcarpetas de casos.

## Regla crítica de índices

Si se crea un nuevo artículo y el índice manual afectado no se actualiza con su enlace y contadores en la misma operación, la tarea no está terminada.

### Checklist obligatorio para índices manuales

1. Añadir o quitar la entrada con enlace exacto al archivo afectado.
2. Mantener el orden que use ese índice; en el índice de casos, orden alfabético dentro de la subcarpeta.
3. Renumerar la lista de la sección si hace falta.
4. Actualizar el contador de la subsección, por ejemplo `### 11.6. Interacciones Complejas (N casos)`.
5. Actualizar los totales o estadísticas globales del índice si existen.
6. Actualizar la fecha del índice si existe un campo de última actualización.

### Validación mínima antes de cerrar

1. Comparar el contenido de la carpeta afectada con el índice.
2. Confirmar que no hay archivos nuevos sin enlace.
3. Confirmar que los contadores coinciden con los archivos reales.

## Notas

- No applies este flujo en tareas de solo lectura.
- Haz esta comprobación antes de dar la tarea por cerrada.
- Esta skill debe tratar el índice como requisito de cierre, no como mejora opcional.