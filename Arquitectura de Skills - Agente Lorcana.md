# Arquitectura de Skills - Agente Lorcana

Estado: Documento de diseño implementado
Fecha de actualización: 2026-07-26
Origen del borrador: 2026-03-18

> Este archivo explica la arquitectura. La configuración operativa vive en `.github/`.

## Arquitectura activa

El flujo de rulings se mantiene pequeño y explícito:

1. `.github/copilot-instructions.md` contiene el contrato breve y siempre activo.
2. `.github/skills/lorcana-ruling-workflow/SKILL.md` es la única fuente de verdad para el ciclo obligatorio completo.
3. `.github/agents/lorcana-ruling.agent.md` dispone de lectura, búsqueda, edición y ejecución, y sigue esa skill antes de responder.
4. `.github/instructions/` conserva conocimiento técnico y editorial reutilizable.

No hay una skill obligatoria separada para la portada o los índices. Esa conducta está incorporada en el workflow unificado para impedir que dependa de una segunda selección automática.

## Transacción editorial

Una duda de reglas se procesa en este orden:

1. concretar la pregunta;
2. localizar fuentes oficiales y verificar cartas;
3. producir el ruling técnico;
4. buscar duplicados o solapamientos;
5. crear o actualizar el artículo canónico;
6. revisar estructura, metadatos, tags, enlaces, fuentes, ortografía y formato;
7. sincronizar todos los índices afectados;
8. actualizar la fecha visible de `Empecemos.md` cuando el artículo cambie materialmente;
9. validar el conjunto;
10. responder con el ruling y las rutas de los artículos.

La respuesta al usuario es el cierre de la transacción, no una fase anterior a la documentación.

## Responsabilidades

| Capa | Responsabilidad |
| --- | --- |
| Contrato global | Garantizar que cualquier ruling active el ciclo completo y sus dos únicas excepciones |
| Workflow unificado | Ordenar, ejecutar y validar todas las fases obligatorias |
| Agente de rulings | Proporcionar identidad, herramientas y salida final del flujo |
| Instrucciones especializadas | Aportar alcance, verificación de cartas, timing, deduplicación, formato, tags, enlaces e higiene |
| Documentos históricos | Explicar decisiones sin imponer comportamiento operativo |

## Fuentes y límites

- La autoridad primaria para reglas es `01.1.a Official English Reference – Unmodified/`.
- La localización y documentación en castellano vive en `01. Reglas/`.
- Los nombres y textos exactos de cartas se verifican en el archivo del set dentro de `02. Listado de Cartas/`.
- Las carpetas legacy o auxiliares no son autoridad normativa.
- Las preguntas al usuario se limitan a datos críticos que cambien el resultado.
- La documentación solo se omite por petición explícita de no editar o por un bloqueo técnico comprobado.

## Decisión histórica aclarada

Se retiró la antigua regla monolítica que mezclaba todas las responsabilidades en un único documento de premisas. No se retiró la documentación automática de rulings: permanece activa y ahora se ejecuta mediante el workflow unificado.

El diseño previo proponía componentes autónomos como `Rule Finder`, `Card Finder`, `Ruling Engine` y `Case Writer`. Esas etiquetas pueden seguir siendo útiles para razonar sobre responsabilidades, pero no son agentes ni skills obligatorias separadas. Crear varias piezas mandatorias volvería a introducir selección probabilística y fuentes de verdad competidoras.

## Limitación residual

Las instrucciones pueden imponer orden, herramientas y criterios de cierre, pero no ofrecen por sí solas una transacción de base de datos con rollback automático. La garantía práctica depende de que el agente inspeccione el diff y valide artículo, índices y fecha antes de responder; ante un fallo real debe declarar el bloqueo y el trabajo incompleto.
