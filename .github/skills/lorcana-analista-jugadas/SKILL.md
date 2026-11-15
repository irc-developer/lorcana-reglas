---
name: lorcana-analista-jugadas
description: "Analiza decisiones de Disney Lorcana desde una posición limitada, guarda una línea antes de conocer la elección y emite un diagnóstico trazable para revisión y enseñanza. Úsala para mulligan, tinta, secuencia o cierre; no sustituye el workflow de rulings ni prepara replays."
---

# Analista de jugadas de Lorcana

Versión de skill: **0.2.0**. Contrato: `../lorcana-trabajo/analisis/profesora-lorcana/INTEGRACION-AGENTES.md`, v0.2; leerlo junto con `AGENTS.md`, `.github/copilot-instructions.md` y `.github/README.md`. Reutiliza `herramientas/profesora_lorcana/contratos.py` para hash canónico de la posición y referencias exactas `{schema, sha256}`. Los hashes de bytes se conservan aparte. La memoria personal se guarda en la ruta privada asignada a la sesión, nunca en esta skill.

## Entrada y frontera

Recibe una sola `lorcana-position-v1` preparada por infraestructura/coordinación. Confirma partida opaca, perspectiva, ordinal, versión histórica y composición de mazo, frontera y hash; conserva contradicciones y ausencias. No atribuyas el último mazo a partidas anteriores ni deduzcas arquetipo por colores. Si falla la identidad, no integres conclusiones.

No abras el replay completo, catálogo con resultados, posiciones posteriores o elección todavía oculta. Las herramientas existentes `herramientas/duels_analisis/` preparan vistas y `herramientas/duels_datos/` conserva listas/procedencia; su ejecución y el puente de `duels-decision-view-v1` al contrato corresponden a quien entrega la posición. Solicita el dato limitado que falta. Una vista de Duels no certifica legalidad, textos ni completitud. Declara cualquier exposición al futuro ya ocurrida: un ensayo redactado no acredita ceguera independiente.

## Línea antes de elección

Guarda `lorcana-plan-v1` con `role: analista` antes de solicitar o abrir `lorcana-choice-v1`. Lee [references/registro-local.md](references/registro-local.md) si necesitas sellar artefactos y comprobar identidad, orden y cuentas con el auxiliar local. La revisora recibe la misma posición y guarda su línea en un registro separado. Coordinación debe comprobar **ambos planes** antes de revelar elección o diagnóstico: el auxiliar local solo acredita su propia secuencia. Esta skill no simula a la revisora ni inicia chats por su cuenta.

Compara la línea preferida con alternativas realizables: acciones en orden, pagos acumulados, cartas/agotamientos utilizados, objetivo legal, condiciones, oportunidad sacrificada y estado al terminar. Una alternativa que exige otra tinta, base de Shift, objetivo, condición temporal o carta ausente se marca condicional; no la presentes como mejora financiada. No cuentes dos veces tinta, personajes o cartas. No garantices robos, respuestas rivales ni aceleración futura. Si solo hay acción forzada, explica por qué no hay alternativa; si faltan datos, delimita qué no se puede elegir.

Separa riesgo, impacto potencial y confianza. Describe escenarios plausibles según información observada y revela sus supuestos. No inventes porcentajes de victoria ni confundas una línea de mayor techo con una línea dominante. Lee [references/criterios.md](references/criterios.md) para apertura, desarrollo, cierre y categorías del diagnóstico.

## Contraste y diagnóstico

Una vez persistida la línea, recibe la elección con evidencia temporal y hash coincidente. Mantén el plan previo intacto. Emite `lorcana-diagnosis-v1` con hechos, inferencias, alternativas pagables, referencias normativas, límites y preguntas de intención que realmente puedan cambiar la evaluación. Usa `acierto`, `defendible`, `mejora_probable`, `error_demostrado` o `indeterminada`; explica impacto y confianza por separado. Reconoce lo bien resuelto aunque señales una mejora.

No uses el resultado ni la continuación para justificar un contrafactual. Evalúa la decisión examinada, separándola de errores anteriores que prepararon la posición. Si hay duda normativa, verifica cartas en el corpus de sets y reglas según la capa `.github/`; una duda real se deriva al workflow editorial existente. Suspende únicamente la conclusión que dependa de esa incertidumbre; conserva las observaciones independientes. El análisis privado no autoriza publicar datos ni saltarse la transacción editorial de un ruling.

Cuando Iván aporte su intención, atribúyela como evidencia posterior. Conserva el diagnóstico anterior y emite una revisión con `revision_of`, motivo del cambio y referencias derivadas afectadas. Una revisión de la revisora puede confirmar, corregir o discrepar: registra las diferencias y revisa solo lo sustentado. Un veredicto `corregir` suspende el juicio afectado hasta un diagnóstico sucesor y nueva revisión. Comprueba cada referencia contra el artefacto completo recibido y su posición original. Entrega a coordinación/profesora posición, plan, elección, diagnóstico versionado y limitaciones; la profesora recibe también la revisión independiente antes de enseñar conclusiones firmes.
