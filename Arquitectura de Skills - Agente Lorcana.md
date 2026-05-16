# Arquitectura de Skills - Agente Lorcana

Estado: Documento de diseño  
Fecha de actualización: 2026-05-13  
Origen del borrador: 2026-03-18

> Este archivo describe el diseño objetivo. No es un agente activo ni una skill cargable. La customización operativa del workspace vive en `.github/`.

## Estado actual

### Qué está implementado hoy

- Instrucciones modulares en `.github/instructions/` para alcance, aclaración, verificación de cartas, timing, robos, casos, tags, enlaces y saneado de archivos.
- Skills activas en `.github/skills/` para importación de sets, seeds SQL de preguntas y actualización de portada e índices.
- Consolidación de la lógica de preguntas en la skill local del repositorio, sin depender ya de la skill global duplicada.
- Un primer agente mínimo de rulings en `.github/agents/lorcana-ruling.agent.md`.

### Qué no está implementado todavía

- No existe un orquestador real que encadene subagentes o fases con contratos formales.
- No existe una skill separada de `Rule Finder`, `Card Finder`, `Ruling Engine` o `Case Writer` como componentes ejecutables autónomos.
- No hay prompts de workspace específicos para activación corta del flujo de ruling.

### Cómo se resuelve hoy el trabajo

El flujo actual se apoya en una combinación de:

1. instrucciones modulares que fijan el criterio;
2. skills puntuales para tareas repetibles;
3. un agente mínimo de rulings que ya documenta el caso tras cada duda resuelta, aunque todavía sin orquestador dedicado.

Esto funciona para el estado actual del repositorio, pero no expresa todavía una arquitectura formal de ejecución de rulings.

## Objetivo del diseño

Separar el flujo de ruling en componentes pequeños para ganar:

1. consistencia de criterio;
2. trazabilidad de qué parte decide cada cosa;
3. posibilidad de orquestar pasos sin mezclar fuentes ni responsabilidades;
4. facilidad para evolucionar cada parte sin tocar todo el sistema.

## Principios de diseño vigentes

- El alcance normativo debe seguir viviendo en las instrucciones locales del repo.
- La autoridad primaria para reglas sigue siendo `01.1.a Official English Reference – Unmodified`.
- El texto exacto de cartas debe verificarse solo en la sección `02. Listado de Cartas`, usando el archivo del set correspondiente.
- Ningún componente del diseño debe hacer fallback a carpetas legacy o auxiliares fuera del alcance permitido.
- Las preguntas al usuario deben ser mínimas y solo cuando bloqueen la decisión normativa.
- La salida final debe mantenerse breve, precisa y defendible.

## Diseño objetivo

### Vista general

| Componente | Función | Estado deseado |
|-----------|---------|----------------|
| Rule Finder | Localizar reglas base, conflictos y epígrafes relevantes | Futuro |
| Card Finder | Verificar nombres y texto exacto de cartas | Futuro |
| Ruling Engine | Emitir el ruling final con secuencia oficial | Futuro |
| Case Writer | Documentar el caso cuando proceda | Futuro |
| Orquestador | Coordinar el flujo de extremo a extremo | Futuro |

### 1. Rule Finder

**Propósito**  
Identificar epígrafes normativos relevantes y detectar conflictos documentales.

**Entrada mínima**

- `question`
- `knownFacts`
- `language`
- `scope`

**Salida mínima**

- `primaryRules`
- `secondaryRules`
- `conflicts`
- `missingCriticalFacts`

**Validaciones clave**

- devolver al menos dos referencias primarias cuando sea posible;
- no salir de `01. Reglas` y `01.1.a Official English Reference – Unmodified`;
- listar conflictos de forma explícita cuando existan.

### 2. Card Finder

**Propósito**  
Resolver menciones de cartas y verificar su texto exacto sin contaminar el análisis con fuentes legacy.

**Entrada mínima**

- `cardsMentioned`
- `allowedSources`

**Salida mínima**

- `cards`
- `ambiguities`
- `missingCriticalFacts`

**Validaciones clave**

- usar solo la sección `02. Listado de Cartas` y el archivo del set correspondiente;
- no usar `02. Habilidades de las cartas_OLD`, `20. Reglas CR 1.X` ni `Unifica`;
- detener la resolución si el texto exacto no está confirmado;
- no dejar pasar ambigüedades de nombre sin confirmación.

### 3. Ruling Engine

**Propósito**  
Emitir el ruling normativo final con secuencia oficial.

**Entrada mínima**

- `question`
- `facts`
- `rules`
- `cards`

**Salida mínima**

- `verdict`
- `shortAnswer`
- `explanation`
- `sequence`
- `citations`
- `conflictHandling`
- `missingCriticalFacts`

**Validaciones clave**

- formato final: Sí/No + explicación + secuencia;
- si hay conflicto alto, devolver fallo provisional y explicarlo;
- no usar léxico de zonas en inglés en la salida final.

### 4. Case Writer

**Propósito**  
Redactar y guardar el caso final en formato estándar del repositorio tras cada duda resuelta, salvo instrucción explícita en contra o bloqueo real.

**Entrada mínima**

- `title`
- `duda`
- `ruling`
- `tags`
- `targetFolder`

**Salida mínima**

- `filePath`
- `status`
- `qualityChecks`

**Validaciones clave**

- respetar la plantilla vigente del proyecto;
- no incluir bloques de dato faltante en el documento final;
- no sobrescribir contenido válido cuando ya exista histórico;
- cerrar también índices y portada cuando la operación lo exija.

### 5. Orquestador

**Propósito**  
Coordinar el flujo de extremo a extremo cuando exista un agente dedicado.

**Flujo objetivo**

1. recibir la duda y el contexto;
2. ejecutar `Rule Finder` y `Card Finder` en paralelo;
3. si falta dato crítico, preguntar lo mínimo y esperar respuesta;
4. reejecutar los componentes afectados con los datos confirmados;
5. ejecutar `Ruling Engine`;
6. ejecutar `Case Writer` tras cada duda resuelta salvo instrucción explícita en contra o bloqueo real;
7. devolver ruling corto, referencias usadas y ruta del caso si se creó.

## Brechas entre el estado actual y el diseño objetivo

- Hoy las reglas están bien separadas, pero la ejecución aún no lo está.
- El repositorio ya tiene criterio modular, pero todavía no tiene componentes ejecutables con contratos formales.
- El comportamiento actual depende del agente general y de instrucciones dispersas, no de un pipeline explícito.
- La activación corta tipo “Resuelve esta duda” no está modelada todavía como prompt o agente del workspace.

## Roadmap recomendado

### Completado

1. Mover la autoridad operativa del repo a `.github/`.
2. Trocear las premisas en instrucciones pequeñas y reusables.
3. Consolidar la skill de preguntas en el workspace y retirar la duplicidad global.

### Siguiente fase razonable

1. Decidir si merece la pena crear un agente personalizado de rulings.
2. Si la respuesta es sí, definir primero el contrato mínimo real de `Rule Finder`, `Card Finder`, `Ruling Engine` y `Case Writer` a partir del uso del repositorio, no del deseo teórico.
3. Crear entonces un `.agent.md` del workspace que orqueste esas fases.

### Fase posterior

1. Añadir normalización de nombres de cartas por alias.
2. Añadir detector de contradicciones entre casos antiguos y reglas actuales.
3. Añadir una métrica de trazabilidad para medir cuánto de cada ruling queda sustentado por citas directas.

## Qué no conviene hacer todavía

- Crear un agente solo para “tener uno” sin un flujo estable.
- Duplicar en este documento reglas operativas que ya viven en instrucciones o skills.
- Reabrir una arquitectura monolítica de premisas que mezcle diseño, ejecución real y material histórico.