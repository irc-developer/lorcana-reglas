# Sesiones, seguimiento y rectificaciones

El contrato común v0.2 define los campos y referencias intercambiados. La observación
y el índice de memoria son convenciones locales de profesora v0.2.0. Reutiliza
`herramientas/profesora_lorcana/contratos.py` para leer JSON estricto, obtener hashes
y verificar referencias. No afirmar integración real hasta que coordinación pruebe
las tres capacidades juntas. Los ejemplos v0.1 conservan su incompatibilidad histórica;
no regenerarlos ni aceptarlos como entradas v0.2.

## Entradas y salida

`input_refs`: lista de referencias exactas `{schema, sha256}` de diagnóstico y
revisión. El hash es SHA-256 canónico del artefacto completo (`canonical-json-v1`).
La propia referencia identifica su versión de contenido; los IDs y `skill_version`
siguen en el artefacto. `choice_ref`, `diagnosis_ref`, `independent_plan_ref` y
`revision_of` no nulo usan la misma forma exacta. Verificarlos contra los artefactos
recibidos con `check_reference`. Rechazar ID solo, referencia con ruta o hash de bytes.
Los recibos locales `receipts` conservan `{role, reference, sha256_bytes}` aparte.
Guardar los originales inmutables permite verificar ese recibo. Cambiar sangrado
conserva referencia canónica pero cambia el recibo; cambiar contenido altera ambas.
Una referencia no resoluble bloquea el par; no buscar continuaciones para resolverla.

En la salida, fortalezas/prioridades/ejercicios incluyen `source_refs` comunes para
entradas y `source_ids` solo para conclusiones locales identificadas. En ejercicios incluye
`exercise_id`, `position_id`, `objective`, `observable_criterion`,
`eligible_occasions`, `exclusions`. `follow_up` registra alcance (versión de lista,
enfrentamiento observado y contexto), criterio previo, observaciones y próximo
punto de revisión. No sumar muestras de ámbitos diferentes sin distinguirlas.

El ayudante de biblioteca estándar `herramientas/profesora_lorcana/profesora/seguimiento.py`
ofrece tres operaciones de lectura. Desde la raíz del repositorio:

```powershell
python herramientas/profesora_lorcana/profesora/seguimiento.py comprobar diagnostico.json revision.json posicion.json eleccion.json plan-revisora.json
# Si hay revision_of, añadir los artefactos anteriores:
# --previous-diagnosis diagnostico-anterior.json --previous-review revision-anterior.json
python herramientas/profesora_lorcana/profesora/seguimiento.py medir observaciones.json
python herramientas/profesora_lorcana/profesora/seguimiento.py revisar memoria.json diagnostico-sustituido.json
```

`comprobar` verifica campos superiores, schemas, referencias y posición original
contra los cinco artefactos suministrados. Los antecesores son obligatorios si hay
`revision_of`, y se contrastan su referencia real, schema y campos requeridos,
`position_id` y `position_sha256` iguales a los actuales. El diagnóstico antecesor
debe conservar también la misma `choice_ref`: esta fase revisa el juicio sobre la
misma posición y elección; no corrige la reconstrucción ni la elección observada.
Si cambia el estado o la elección, no integrar el par como esta cadena de revisión;
remitirlo a coordinación para preparar y distinguir la nueva evidencia.
Emite referencias comunes y recibos locales de bytes. Devuelve `suspendida` para `corregir`,
`incierta` para `no_evaluable`/`indeterminada`, `disputada` para `discrepancia` y
`utilizable` para el resto confirmado. No certifica legalidad, calidad estratégica,
contenido semántico, autenticidad de fuentes ni orden temporal del plan.
Se calcula el hash de la posición realmente recibida; no basta con igualar dos
campos de hash. Coordinación sigue comprobando procedencia, estado limitado y
que ambos planes se guardaron antes de las revelaciones. Un hash no demuestra que
el contenido sea correcto ni que las reconstrucciones inicial y corregida sean iguales.

## Denominadores

Una ocasión es elegible si cumple el criterio definido para el ejercicio antes de
leer el resultado: posición reconstruida suficiente, versión/ámbito pertinente y
alternativas necesarias verificadas. La ausencia de explicación del jugador es
`missing`, no `unmet`. Usa dos denominadores: ocasiones elegibles y ocasiones con
evidencia evaluable. Expresa «X de Y evaluables; Z elegibles, M sin registro».
No presentes `0/0` como rendimiento cero. Separar más tarde «lo explicó ahora» de
«lo registró durante la partida». No imputar la segunda a partir de la primera.

`medir` recibe una lista de observaciones de un solo objetivo y ámbito:

```json
[{"occasion_id":"posicion-y-frontera", "objective_id":"comparar-tintas",
  "scope":"lista-v1/enfrentamiento-observado/contexto",
  "eligible":true, "outcome":"missing",
  "evidence_ref":null, "reason":"No se registró la explicación"}]
```

`met`/`unmet` requieren referencia al registro de respuesta; si no es elegible,
`outcome` es `null` y `reason` explica la exclusión. La clave de ocasión identifica
la misma frontera aunque se vuelva a evaluar; no duplicarla al releer un replay.
El ayudante rechaza duplicados, ámbitos mezclados y resultados sin evidencia.
No decide si una explicación satisface el criterio: esa valoración debe ser trazable
y admite revisión. Los recuentos de ejercicios distintos se presentan separados.

## Memoria privada y corrección

Separar `perfil.json` (tiempo, preferencias, prioridades acordadas), sesiones
inmutables, referencias de evidencia y un índice `memoria.json` de conclusiones
vigentes. No copiar este perfil a la skill. Conservar listas históricas exactas;
no descargar partidas ni completar el estado desde datos posteriores.

Convención del índice para `revisar`: lista de objetos
`{id, source_refs, source_ids, status, ...}`. `source_refs` referencia artefactos
externos ya verificados en las sesiones; `source_ids` enlaza conclusiones del índice.
IDs únicos, `status`: `active`, `requires_review` o `superseded`. El comando devuelve
una copia con los descendientes transitivos de las fuentes sustituidas marcados
`requires_review` y con `revision_reasons: {source_refs, source_ids}`; no escribe
archivos. La selección se hace por schema+hash de la versión sustituida, nunca por
ID solo. Preserva el histórico de fuentes y no reactiva un elemento `superseded`.
El comando recibe los archivos sustituidos y obtiene sus referencias canónicas.
No prueba por sí mismo que una referencia externa del índice fue verificada; ese
recibo debe estar en la sesión original. Un cambio de contenido con el mismo ID
es otra versión y no invalida conclusiones de la versión equivocada.

Tras una corrección:

1. Guarda la fuente sucesora y su `revision_of`, sin borrar la anterior.
2. Marca descendientes, incluidos recuentos y afirmaciones por enfrentamiento. Suspende
   su uso para puntuar o atribuir patrones, incluso si parte de la conclusión sobrevive.
3. Revisa cada elemento marcado: conserva lo independiente con nueva procedencia,
   sustituye lo afectado o retíralo. Guarda el estado anterior y las razones en la sesión
   de rectificación. Actualiza también el resumen que cargarás en la siguiente sesión.
4. Recalcula solo observaciones afectadas. Un error de reconstrucción no es fallo del
   jugador. La nueva sesión declara qué cambia y qué evidencia continúa pendiente.

Una corrección puede eliminar la prioridad activa sin exigir reemplazarla por otra.
No rellenes un cupo de objetivos cuando la evidencia no lo permite. Las conclusiones
históricas sirven para diseñar práctica; el progreso requiere ocasiones nuevas.
