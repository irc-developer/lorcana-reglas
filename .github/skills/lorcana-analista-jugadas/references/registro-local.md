# Registro local opcional

Desde la raíz del repositorio, solo biblioteca estándar:

```powershell
python -B -m herramientas.profesora_lorcana.analista.registro position POSICION.json --session RUTA_PRIVADA_NUEVA
python -B -m herramientas.profesora_lorcana.analista.registro plan PLAN.json --session RUTA_PRIVADA
python -B -m herramientas.profesora_lorcana.analista.registro choice ELECCION.json --session RUTA_PRIVADA
python -B -m herramientas.profesora_lorcana.analista.registro diagnosis DIAGNOSTICO.json --session RUTA_PRIVADA
python -B -m herramientas.profesora_lorcana.analista.registro verify --session RUTA_PRIVADA
python -B -m unittest herramientas.profesora_lorcana.analista.test_registro -v
```

No abrir el archivo de elección para rellenar el plan. Coordinación revela la elección después de comprobar el guardado de **ambos planes** sobre la misma posición. El auxiliar solo comprueba la cadena propia, con hashes y escritura exclusiva; bloquea su orden equivocado y detecta alteraciones accidentales. Usar un único escritor por sesión. **No prueba lo que una agente ya leyó**, no impone permisos de aislamiento y no es un motor de reglas. No descarga, abre originales, consulta APIs ni modifica el catálogo. No convierte vistas de Duels: recibe la posición común ya preparada.

La CLI comprueba la etapa propia **antes** de leer una entrada posterior. La API `append` recibe un objeto ya cargado: quien la llama controla su lectura y la comprobación de ambos planes. Ninguno de los dos mecanismos sustituye la autorización de revelación que conserva coordinación.

## Intercambio v0.2 y recibos locales separados

`schema` identifica cada tipo. `position_sha256` es `contratos.digest(posicion_completa)` según `canonical-json-v1`: claves ordenadas, UTF-8, sin espacios separadores ni salto final, sin NaN ni claves JSON duplicadas. No es el hash de la vista interior en `boundary`. `append` y la CLI devuelven la referencia canónica exacta `{schema, sha256}`; `choice_ref` y `revision_of` usan esa forma. El auxiliar comprueba la referencia de elección contra la elección realmente conservada, y cada posición/versión contra la posición original de su sesión.

Los archivos se guardan con sangrado para lectura. Los recibos locales `lorcana-analyst-record-v2` usan `artifact_receipt` y `previous_record` con `{path, sha256_bytes}`. Estos detectan cambios de bytes y **no** se intercambian como referencias de artefactos. Un cambio de sangrado cambia el recibo local pero conserva el hash canónico. Los ensayos v0.1 se mantienen intactos y no se aceptan como sesiones v0.2: el auxiliar rechaza el recibo antiguo. Su resultado histórico se conserva en el manifiesto previo; cualquier nueva validación usa un directorio nuevo.

`confidence` usa `{level, basis}` y `impact` usa `{level, reason}` según los valores de `criterios.md`. Los campos hechos/inferencias/límites/referencias son listas; la herramienta comprueba forma mínima, no la verdad del texto. `revision_of` es `null` en el primer diagnóstico; en uno posterior apunta al diagnóstico previo. La revisión explica el cambio en `facts`/`limitations` y enumera las conclusiones derivadas afectadas. La intención posterior puede citarse allí con procedencia; no se reescribe la elección original ni el plan.

Para comprobar cuentas, cada línea usa esta extensión dentro de `preferred_line`/`alternatives`:

```json
{
  "label": "Desarrollar dos piezas",
  "status": "realizable",
  "resources": {"ink": 5, "card_a": 1, "card_b": 1},
  "steps": [
    {"action": "Jugar A", "spend": {"ink": 2, "card_a": 1}, "gain": {}, "evidence_refs": ["estado/recurso", "texto/coste-a"]},
    {"action": "Jugar B", "spend": {"ink": 3, "card_b": 1}, "gain": {}, "evidence_refs": ["texto/coste-b"]}
  ],
  "conditions": [],
  "benefit": "Dos piezas en mesa",
  "risk": "Consume toda la tinta disponible",
  "rules_refs": ["evidencia-verificada"]
}
```

Recursos enteros no negativos; cada paso resta antes de sumar. Declara cartas/agotamientos además de tinta cuando limite su reutilización. Un incremento exige evidencia, no un robo favorable supuesto. `status: condicionada` obliga a enumerar condiciones y no permite presentar la línea como mejora actualmente disponible. `resources` debe partir del estado conocido; el auxiliar solo comprueba la aritmética declarada, por lo que falsificar el saldo inicial o el coste seguiría pasando: comprobarlos contra posición y fuentes es trabajo de analista/revisora. `preferred_line: null` admite datos insuficientes; si no hay alternativas, incluir `alternatives_note` explicando acción forzada o indeterminación. Los diagnósticos reutilizan las mismas líneas financiadas en `alternatives`.

La herramienta revisa claves obvias de futuro en posiciones, pero un texto libre o clave desconocida puede contener contaminación. La comprobación semántica de todos los campos y de la frontera sigue siendo imprescindible. Una discrepancia normativa impide el juicio dependiente; el validador de estructura no puede detectarla por sí solo.
