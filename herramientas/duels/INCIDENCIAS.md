# Incidencias de exportación investigadas

El diagnóstico de la frontera decreciente del lote histórico `7332…` está en [el informe privado local](local/incidencias/01a1212d-d46d-7e5a-bf78-70b3cc558d5d/INFORME.md), junto con `diagnostico.json`. Se ha comprobado el contenido original y la concordancia de adquisición/catálogo; la anomalía no la introduce el adaptador de análisis.

En seq 99 el contador baja de 258 a 256, dentro de una lista de 397 eventos. El prefijo de seq 98 contiene tres eventos posteriores. Ambos extractores fallan de forma conservadora; no se ha rellenado, recortado ni sustituido información. La propuesta para análisis es precisar el error y validar fronteras antes de persistir derivados, manteniendo la partida fuera de vistas íntegras.

`auditar_fronteras.py` permite reproducir el diagnóstico local desde un catálogo y el manifiesto de adquisición. No usa red ni credenciales, no modifica originales y no cambia el cliente ni su contrato v1. Reproduce los rechazos de ambos extractores en un directorio temporal propio y registra hashes y límites exactos en una salida privada. La documentación completa del comando permanece en el informe local porque contiene identificadores y rutas personales.
