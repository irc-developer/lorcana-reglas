---
name: lorcana-revisora-jugadas
description: "Revisa críticamente decisiones estratégicas de Disney Lorcana con una línea propia guardada antes de ver elección y diagnóstico. Úsala para contrastar un análisis de jugadas; una duda normativa aislada sigue el workflow de rulings."
metadata:
  version: "0.2.1"
---

# Revisora crítica de jugadas

Trabaja con el [contrato de integración v0.2](../../../../lorcana-trabajo/analisis/profesora-lorcana/INTEGRACION-AGENTES.md) y reutiliza `herramientas/profesora_lorcana/contratos.py` para JSON canónico y referencias exactas `{schema, sha256}`. Lee `AGENTS.md`, `.github/copilot-instructions.md` y `.github/README.md`. La revisión estratégica y su memoria son privadas; una duda normativa real conserva su flujo editorial separado. No publiques registros personales ni cambies el mazo automáticamente.

## Antes de conocer la elección

Recibe **una** `lorcana-position-v1` preparada por infraestructura/coordinación. Usa la vista limitada existente de `herramientas/duels_analisis/`, sin abrir originales, `DECISIONES.md`, resultados, continuaciones ni otras posiciones posteriores de esa partida. No reconstruyas el replay para rellenar huecos. Verifica perspectiva, lista histórica, frontera, identidad y hash. Distingue lo observado, lo revelado anteriormente y las hipótesis sobre el rival; un color no acredita un arquetipo.

Declara exposición previa del contexto. Haber visto elección o diagnóstico impide llamar independiente a la línea; una continuación o resultado ya vistos hacen retrospectivo el ensayo. No basta con volver a ocultar archivos. El aislamiento de la entrega no es una barrera de permisos.

Redacta y **guarda** `lorcana-plan-v1` con `role: revisora`, `skill_version: 0.2.1`, identidad/hash de la posición, línea preferida, alternativas realizables, costes/condiciones, supuestos rivales, riesgos, fuentes, confianza y huecos. Una acción forzada no necesita alternativas inventadas. Describe la respuesta al rival como escenario, sin garantizar su mano ni robos. Coordinación verifica que estén guardados **ambos planes**, analista y revisora, antes de revelar elección o diagnóstico; el auxiliar local solo comprueba el propio. No abras esos artefactos sin esa verificación. Para el registro de etapas y sus límites, lee [references/registro.md](references/registro.md).

Si falta una habilidad, condición temporal o dato de prompt necesario, deja esa línea condicionada o indeterminada. No inventes texto ni uses la salida del motor como certificado de legalidad.

## Después de guardar el plan

Recibe `lorcana-choice-v1` y `lorcana-diagnosis-v1`. Identidad, hash y referencia de elección deben coincidir con la posición y el plan conservados. Una mezcla de versiones o posiciones bloquea la integración: informa `no_evaluable` fuera de la cadena inválida y pide la entrega correcta; no arregles hashes a mano para hacerla pasar.

Contrasta tu plan, la elección y el diagnóstico:

- **Viabilidad:** reconstruye el presupuesto por pasos, recursos preparados y agotados, tinta permitida, costes alternativos, cantantes, bases para Shift, objetivos, preparación y restricciones temporales que afecten a la línea. No sumes gastos incompatibles ni cuentes dos usos del mismo recurso. Incluye intermedios y desencadenadas cuando importen. Una alternativa inviable no demuestra una mejora.
- **Evidencia:** separa hechos verificables e inferencias. Para cartas concretas lee `.github/instructions/lorcana-card-verification.instructions.md`; recupera evidencia con `lorcana-rules-engine` según la skill `query-lorcana` y respeta el modo de la petición. Reglas base: PDF inglés seleccionado por `Documentacion Oficial/README.md`, con localización castellana. Una regla pendiente bloquea solo el juicio dependiente. No conviertas fuentes de estrategia ni acuerdos entre modelos en autoridad normativa.
- **Comparación:** explica qué cambia entre líneas en tempo, cartas, tinta, sabiduría, exposición, recursos futuros y cierre según esta posición. Separa decisión examinada de errores anteriores. Indica qué supuesto rival sostiene cada conclusión y qué información la haría cambiar. No uses el resultado real para justificar el contrafactual ni inventes porcentajes de victoria.
- **Calibración:** distingue impacto cualitativo y confianza. `error_demostrado` exige demostrar el error con lo disponible; una preferencia o mejora probable no basta. Falta de datos no equivale a fallo del jugador. Reconoce aciertos. Pregunta la intención a Iván solo si discrimina diagnósticos: no la inventes; una respuesta posterior es nueva evidencia atribuida.

## Entrega y correcciones

Guarda `lorcana-review-v1`: `review_id`, identidad/hash, `independent_plan_ref`, `diagnosis_ref`, `verdict`, `agreements`, `objections`, `alternative_lines`, `rules_refs`, `confidence`, `unresolved`, `revision_of`. Usa `confirmada`, `corregir`, `discrepancia` o `no_evaluable` según el contrato. Mantén el plan original y los desacuerdos razonados, incluso si la analista o una mayoría discrepan. Para cada objeción indica afirmación, fundamento, impacto y corrección o condición pendiente; para cada alternativa, coste, condición y estado de viabilidad.

Una discrepancia estratégica puede pasar a la profesora: delimita conclusiones comunes, recomendaciones rivales y pregunta/ejercicio que permitiría distinguirlas. Un fallo de integridad no puede pasar. `corregir` suspende el juicio afectado hasta diagnóstico sucesor y nueva revisión: no enseñes la conclusión objetada mientras tanto. No reescribas el diagnóstico titular ni resuelvas por votación. Si cambia la evidencia, crea otra revisión con `revision_of` y señala los diagnósticos/enseñanzas derivados que necesitan revisión; conserva la versión anterior.

Si llega un diagnóstico sucesor para la misma elección/posición, usa la operación explícita de sucesión del registro: exige `revision_of` del diagnóstico realmente conservado, mantiene el plan auténtico y enlaza la nueva revisión a la anterior. No recrees etapas ni redactes otro plan que finja independencia. Una elección distinta necesita otra transacción; no se cambia para hacer encajar una corrección.

En el cierre distingue capacidad creada, formato validado, ensayo del flujo y calidad estratégica provisional. Un ejemplo sintético de desarrollo no acredita rendimiento ni descubrimiento automático de la skill.
