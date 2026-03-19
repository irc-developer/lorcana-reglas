# Arquitectura de Skills - Agente Lorcana

Estado: Borrador operativo v1  
Fecha: 2026-03-18

## Objetivo

Separar el agente en skills especializados para aumentar consistencia, trazabilidad y calidad de ruling:

1. Skill de búsqueda de reglas.
2. Skill de búsqueda y normalización de cartas.
3. Skill de resolución (ruling engine).
4. Skill de documentación final.
5. Orquestador que controla el flujo.

---

## Principios globales (heredados)

- Alcance normativo: solo `01. Reglas`.
- Casos del bloque 11: apoyo interpretativo, nunca por encima de reglas base.
- Resúmenes del bloque 12: material docente.
- Citas de reglas: formato Obsidian con epígrafe/ancla.
- Citas de cartas: formato Obsidian `[[Cartas de Lorcana#Nombre Exacto|Texto visible]]`.
- Léxico de zonas obligatorio:
  - discard = descarte / zona de descarte
  - hand = mano
  - play = zona de juego
  - inkwell = pozo de tinta
- Si falta dato crítico: preguntar antes del ruling final.

---

## Skill 1 — Rule Finder

### Propósito
Identificar epígrafes normativos relevantes y conflictos documentales.

### Entrada
```json
{
  "question": "texto de duda",
  "knownFacts": ["hecho1", "hecho2"],
  "language": "es",
  "scope": "01.Reglas"
}
```

### Salida
```json
{
  "primaryRules": [
    {
      "ref": "[[7.7. Bolsa (Bag)#7.7.3.1. Añadir a la bolsa un efecto|7.7.3.1. Añadir a la bolsa un efecto]]",
      "why": "disparo durante resolución"
    }
  ],
  "secondaryRules": [
    {
      "ref": "[[11.2.03 Cláusula - El uso de Then#Respuesta|11.2.03 Cláusula - El uso de Then]]",
      "why": "interpretación de cláusulas"
    }
  ],
  "conflicts": [
    {
      "topic": "string",
      "sources": ["refA", "refB"],
      "status": "none|low|high"
    }
  ],
  "missingCriticalFacts": ["hecho crítico faltante"]
}
```

### Validaciones
- Debe devolver al menos 2 referencias primarias cuando sea posible.
- No puede devolver referencias fuera de `01. Reglas`.
- Si detecta conflicto, debe listarlo explícitamente.

---

## Skill 2 — Card Finder

### Propósito
Obtener texto de cartas y normalizar nombres/enlaces Obsidian.

### Entrada
```json
{
  "cardsMentioned": ["Lilo gris", "malicious"],
  "source": "Cartas de Lorcana"
}
```

### Salida
```json
{
  "cards": [
    {
      "canonicalName": "Lilo - Bundled Up",
      "obsidianLink": "[[Cartas de Lorcana#Lilo - Bundled Up|Lilo - Bundled Up]]",
      "oracleText": [
        "EXTRA LAYERS During each opponent's turn, the first time this character would take damage, she takes no damage instead."
      ]
    }
  ],
  "ambiguities": [
    {
      "input": "malicious",
      "candidates": ["Malicious, Mean, and Scary", "Potion of Malice"]
    }
  ],
  "missingCriticalFacts": ["qué carta de malicious"]
}
```

### Validaciones
- Todo nombre de carta en salida debe incluir enlace Obsidian válido.
- Si hay ambigüedad de nombre, no pasa a resolución sin confirmación.

---

## Skill 3 — Ruling Engine

### Propósito
Emitir ruling normativo final con secuencia oficial.

### Entrada
```json
{
  "question": "texto final de duda ya desambiguada",
  "facts": ["hechos confirmados"],
  "rules": {
    "primaryRules": [],
    "secondaryRules": [],
    "conflicts": []
  },
  "cards": []
}
```

### Salida
```json
{
  "verdict": "yes|no|provisional",
  "shortAnswer": "texto corto en español",
  "explanation": "motivo normativo",
  "sequence": [
    {"step": "Coste", "detail": "..."},
    {"step": "Objetivos", "detail": "..."},
    {"step": "Resolución", "detail": "..."},
    {"step": "Disparos", "detail": "..."},
    {"step": "GSC", "detail": "..."}
  ],
  "citations": ["ref1", "ref2"],
  "conflictHandling": {
    "hasConflict": false,
    "provisionalText": ""
  },
  "missingCriticalFacts": []
}
```

### Validaciones
- Formato obligatorio: Sí/No + explicación + secuencia.
- Si hay conflicto alto: `verdict = provisional` y detallar conflicto.
- No usar términos de zonas en inglés en salida final.

---

## Skill 4 — Case Writer

### Propósito
Redactar y guardar el caso final en formato estándar del repositorio.

### Entrada
```json
{
  "title": "nombre del caso",
  "duda": "enunciado final con datos críticos ya integrados",
  "ruling": {
    "shortAnswer": "...",
    "explanation": "...",
    "sequence": [],
    "citations": []
  },
  "tags": ["#Tag1", "#Tag2"],
  "targetFolder": "01. Reglas/11. Casos de ejemplo y aclaraciones"
}
```

### Salida
```json
{
  "filePath": "ruta creada",
  "status": "created|updated",
  "qualityChecks": {
    "hasObsidianCardLinks": true,
    "hasRuleCitations": true,
    "usesSpanishZonesLexicon": true,
    "matchesTemplate": true
  }
}
```

### Validaciones
- Debe seguir la plantilla vigente del proyecto.
- No incluye bloque de “dato faltante” en documento final.
- Tags dinámicos según contexto.
- No sobrescribe contenido existente: si el archivo ya existe o hay título similar, añade la nueva entrada en el mismo archivo (append) conservando histórico.

---

## Orquestador — Flujo E2E

1. Recibe comando (`Resuelve esta duda`) y contexto.
2. Ejecuta Rule Finder + Card Finder en paralelo.
3. Si hay `missingCriticalFacts`, pregunta al usuario y espera respuesta.
4. Reejecuta skills afectados con datos confirmados.
5. Ejecuta Ruling Engine.
6. Ejecuta Case Writer.
7. Devuelve al usuario:
   - ruling corto
   - epígrafes usados
   - ruta del caso documentado

### Política de preguntas mínimas

- Máximo 1–2 preguntas, solo si bloquean decisión normativa.
- Preguntas cerradas (sí/no) siempre que sea posible.
- Cada pregunta debe incluir una justificación breve de por qué ese dato cambia el ruling.
- Una vez respondidas, integrar esas respuestas en la sección Duda final.

### Política de conflictos de fuentes

- Si se detecta conflicto alto de fuentes, el orquestador no cierra el ruling final automáticamente.
- Debe preguntar al usuario qué criterio aplicar antes de continuar.
- Solo tras esa respuesta se emite ruling final y se documenta.

---

## Reglas de calidad (checklist)

- [ ] Usa solo `01. Reglas` para fundamentar.
- [ ] Citas de reglas en formato Obsidian con ancla.
- [ ] Cartas en formato `[[Cartas de Lorcana#...|...]]`.
- [ ] Léxico de zonas en castellano.
- [ ] Secuencia completa: Coste, Objetivos, Resolución, Disparos, GSC.
- [ ] Caso guardado en raíz de `11. Casos de ejemplo y aclaraciones`.

---

## Modo MVP (recomendado para empezar)

- Ejecutar Rule Finder y Card Finder en paralelo.
- Usar Ruling Engine con plantilla fija.
- Case Writer añade entrada sin sobrescribir cuando exista archivo relacionado.
- Sin memoria avanzada entre sesiones (solo archivo de premisas).

---

## Evolución futura (v2)

- Añadir normalizador de nombres de cartas por alias.
- Añadir detector de contradicciones entre casos antiguos y reglas actuales.
- Añadir score de trazabilidad (qué % de afirmaciones tiene cita directa).
