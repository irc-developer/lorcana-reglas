# Registro local de etapas

Leer al preparar una revisión auditable. El contrato común v0.2 define campos, JSON canónico y referencias; el helper importa estas operaciones de `herramientas/profesora_lorcana/contratos.py`. No modifica el contrato ni convierte formatos por su cuenta.

`herramientas/profesora_lorcana/revisora/registro.py` usa solo biblioteca estándar. Desde la raíz:

```powershell
python -B herramientas/profesora_lorcana/revisora/registro.py abrir --posicion POSICION.json --sesion RUTA_PRIVADA_NUEVA --exposicion limitada --nota "Solo posición entregada; sin diagnóstico ni futuro en contexto"
python -B herramientas/profesora_lorcana/revisora/registro.py plan --sesion RUTA_PRIVADA_NUEVA --entrada PLAN.json
# Solo tras confirmar el guardado anterior, recibir/abrir elección y diagnóstico.
python -B herramientas/profesora_lorcana/revisora/registro.py revelar --sesion RUTA_PRIVADA_NUEVA --eleccion ELECCION.json --diagnostico DIAGNOSTICO.json
python -B herramientas/profesora_lorcana/revisora/registro.py referencias --sesion RUTA_PRIVADA_NUEVA
python -B herramientas/profesora_lorcana/revisora/registro.py revision --sesion RUTA_PRIVADA_NUEVA --entrada REVISION.json
# Si llega un diagnóstico sucesor autorizado para la misma elección/posición:
python -B herramientas/profesora_lorcana/revisora/registro.py diagnostico-sucesor --sesion RUTA_PRIVADA_NUEVA --entrada DIAGNOSTICO_SUCESOR.json
python -B herramientas/profesora_lorcana/revisora/registro.py revision --sesion RUTA_PRIVADA_NUEVA --entrada REVISION_SUCESORA.json
```

Guarda las sesiones en `../lorcana-trabajo/analisis/profesora-lorcana/desarrollo/revisora/` o en la ruta privada que entregue coordinación. Nunca en la skill ni en un directorio publicado. No pases una carpeta de originales. `abrir` lee únicamente el JSON limitado indicado. `revelar` verifica primero el plan conservado y solo después lee elección y diagnóstico. Los comandos imprimen referencias, sin reproducir datos personales. También existe API Python para integración local; no instala nada ni usa red.

Identidad compartida v0.2 y recibos locales:

- Cada artefacto tiene `schema` igual al nombre del contrato. `position_sha256` es SHA-256 de la posición completa serializada con `json.dumps(sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)`, UTF-8 sin salto final. No es el hash de bytes originales ni el hash de una vista interna. Solo JSON con claves string y sin claves duplicadas/NaN.
- Una referencia es exactamente `{"schema": "lorcana-plan-v1", "sha256": "…"}` (análogo para elección, diagnóstico y revisión), comprobada contra el artefacto recibido con `check_reference`. Es la forma común de `choice_ref`, `independent_plan_ref`, `diagnosis_ref` y `revision_of` cuando no sea null. Los ensayos v0.1 conservan su procedencia; los nuevos se guardan en otra ruta.
- `available_state` puede conservar la vista `duels-decision-view-v1` ya entregada, sin volver a proyectar originales. El hash de frontera de esa vista lo prepara y verifica infraestructura/coordinación: el helper no dispone del original para validarlo. Se conserva el sobre común recibido; no se presenta un adaptador nuevo como existente.
- `abrir` requiere `limitada`, `contaminada` o `desconocida` y una nota. Es una declaración del operador, no una certificación automática. El registro conserva esa declaración y el orden de escritura; tampoco prueba que otro proceso no haya leído archivos.
- Los recibos encadenan hashes de la etapa anterior. Las revisiones se añaden por ID; una corrección referencia una revisión ya conservada. Se rechaza sobrescribir archivos. Esto detecta alteraciones accidentales si se conservan los recibos; no es una firma ni almacenamiento inmutable frente a quien puede reescribir toda la sesión. Un fallo deja el archivo previo intacto; no hay recuperación automática ni edición de recibos.
- El guardado local del plan no autoriza por sí solo la revelación compartida. Coordinación verifica ambos planes antes de entregar elección/diagnóstico. `corregir` suspende lo afectado hasta diagnóstico sucesor y revisión nueva. Recibir una acción de un solo paso no permite atribuir al jugador la secuencia completa del plan.

## Diagnósticos sucesores, desde auxiliar 0.2.1

`save_diagnosis_successor(session, diagnosis_path)` y el comando `diagnostico-sucesor` añaden `diagnostico-0001.json`, etc., sin cambiar `sesion.json`, `plan.json`, `revelacion.json` ni revisiones anteriores. `revision_of` debe ser la referencia exacta del último diagnóstico guardado. `choice_ref` se comprueba contra la elección original y se mantienen posición/hash e identidad nueva de diagnóstico. El diagnóstico inicial de `revelar` lleva `revision_of: null`; una corrección posterior nunca sustituye ese recibo.

Cada sucesor enlaza el recibo del diagnóstico anterior (el primero enlaza la revelación original). La revisión nueva referencia el diagnóstico vigente y conserva `independent_plan_ref` original. Si existe revisión previa, exige `revision_of` de una revisión ya conservada, aunque se refiera al diagnóstico anterior. Se verifican todos los recibos y las referencias de versiones conservadas; no se admite una revisión que vuelva silenciosamente al diagnóstico obsoleto, un antecesor equivocado, ciclos ni versiones discontinuas.

`referencias` devuelve el diagnóstico vigente, `diagnosis_history` y referencias de revisiones conservadas. Esto no decide qué desacuerdo está resuelto: la revisión sucesora debe explicitar qué cambia, qué permanece abierto y qué enseñanzas/contadores derivados necesitan reconsideración. El helper no modifica la memoria de la profesora.

Las sesiones de auxiliar 0.1.0 y 0.2.0 se leen con sus recibos originales; los artefactos no se reetiquetan ni se reescriben. Para un ensayo de sucesión sobre una copia retrospectiva, declarar origen y conservar hashes/bytes previos: copiar un plan existente no crea una nueva prueba independiente.

La validación cubre campos/tipos básicos, identidades, referencias, etapas, revisión previa y ciertas claves de fuga conocidas, incluidas mano rival/orden de mazo introducidos como campos nuevos. **No** determina legalidad, costes, veracidad de fuentes, estrategia, exposición semántica en texto libre ni completitud de la posición. El filtro es una alarma adicional; una posición que lo pasa sigue requiriendo revisión humana/agente de la frontera. Los campos desconocidos no prohibidos se conservan. La ausencia de una clave prohibida no acredita independencia.

Si detectas contaminación en el contenido o contexto, declárala aunque el helper acepte el JSON. No falsifiques un plan previo. Una revisión retrospectiva puede resultar útil, pero no sustituye la línea independiente exigida por el piloto. Si hay fallo de identidad/hash, conserva la objeción en un registro privado aparte; el helper rechaza integrar esa cadena incluso con `no_evaluable`.

Pruebas de invariantes (sin cartas ni partidas reales):

```powershell
python -B -m unittest discover -s herramientas/profesora_lorcana/revisora -p 'test_*.py' -v
```
