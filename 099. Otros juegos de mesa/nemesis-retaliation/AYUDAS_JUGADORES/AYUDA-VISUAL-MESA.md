# Nemesis: Represalia — Especificación de ayuda visual de mesa

**Título original:** *Nemesis: Retaliation*  
**Propósito:** definir una ayuda imprimible de consulta rápida  
**Fuentes:** [reglamento final oficial en inglés](../doc/Nemesis-RT-Rulebook-EN.pdf) y [FAQ oficial v1.1](../doc/RETALIATION_FAQ_v1.1.pdf), de 19/11/2025  
**Cobertura:** juego base estándar con Primigenios; sin reglas de otras entregas ni expansiones  
**Última validación:** 02/08/2026

---

## Objetivo

La pieza debe permitir resolver sin abrir el manual:

1. las cuatro fases de la ronda;
2. las tres partes de cada turno;
3. acciones y costes;
4. Movimiento, Exploración y Ruido;
5. Disparar, Acribillar y cuerpo a cuerpo;
6. Asegurar frente a Reforzar;
7. Oxígeno, Contaminación y final;
8. las aclaraciones oficiales que alteran consultas frecuentes.

No debe intentar sustituir las cartas de personaje, Objetos, Compartimentos, hoja de Intrusos ni carta de Tarea de la Misión.

---

## Formato recomendado

### Opción principal

- A4 horizontal a dos caras.
- Cara A: ronda, turno, acciones, Movimiento y Ruido.
- Cara B: Combate, defensa, Oxígeno, vías de salida y final.
- Márgenes mínimos de 10 mm.
- Cuerpo de texto de 9 pt o mayor.

### Opción panorámica

- Una cara en proporción 12:7.
- Cuatro fases como columna vertebral central.
- Tres columnas y franja inferior.
- Adecuada para [PROMPT-IMAGEN-MUNDREL.md](./PROMPT-IMAGEN-MUNDREL.md).

---

## Jerarquía visual

1. **Nivel 1:** ronda 1–4 y turno A–C.
2. **Nivel 2:** Movimiento → Exploración → Ruido.
3. **Nivel 3:** Disparar / Acribillar / cuerpo a cuerpo.
4. **Nivel 4:** Oxígeno, salida, final y FAQ.

Cada regla rápida debe combinar:

- icono;
- verbo;
- valor;
- consecuencia.

Ejemplos:

```text
SOPORTE VITAL INACTIVO · fin de cada turno · −1 OXÍGENO
FUEGO · fin de cada turno · −1 SALUD
ACRIBILLAR · Pasillo adyacente · gasta MUNICIÓN
```

---

## Cara A — Ronda, acciones y exploración

### Cabecera

```text
NEMESIS: REPRESALIA — AYUDA DE RONDA
GANA = SALIDA + OBJETIVO + SOBREVIVIR A INFECCIÓN/ECLOSIÓN
```

Aviso de edición visible:

```text
RETALIATION / REPRESALIA · NO NEMESIS · NO LOCKDOWN
```

### Bloque A — Las cuatro fases

```text
1 JUGADORES
   turnos hasta que todos Pasen
   turno = 2 acciones → Oxígeno → Fuego

2 INTRUSOS
   Fuego: 1 impacto a Intrusos / 1 Huevo en Nido
   Ataques de Intrusos ya presentes

3 EVENTO
   movimiento → efecto principal → efecto secundario
   desarrollo de la bolsa

4 ORDENAMIENTO
   Jugador inicial → robar hasta 5 → avanzar ronda
```

### Bloque B — Tu turno

```text
A 2 ACCIONES
B SOPORTE VITAL INACTIVO → −1 OXÍGENO
C FUEGO EN COMPARTIMENTO → −1 SALUD
```

Notas pequeñas:

- Pasar es una acción y no omite Oxígeno ni Fuego.
- Tras Pasar no hay más turnos, pero sí Reacciones.
- Contaminación no paga acciones.
- Reacción no cuenta como acción.

### Bloque C — Costes

```text
0 CARTAS
Jugar Acción · Pasar

1 CARTA
Mover · Asegurar · Disparar · Acribillar
Cuerpo a cuerpo · Objeto · Robot · Intercambiar
Equipo táctico

2 CARTAS
Usar Compartimento · Movimiento cauteloso
```

### Bloque D — Movimiento

```text
ELIGE PASILLO
↓
INTRUSOS en origen/pasillo
→ hasta 3 ATAQUES DE OPORTUNIDAD
↓
DESTINO DESCUBIERTO
→ mover → Asegurar si cauteloso → RUIDO

DESTINO SIN DESCUBRIR
→ EXPLORAR → entrar → efecto de Entrada
```

Aviso dominante:

```text
RUIDO DESPUÉS DE CADA MOVIMIENTO
también con personajes o Intrusos en destino
```

### Bloque E — Ruido

```text
1–4 · TODOS los Pasillos con ese valor
Intruso → el mayor entra y ataca
Ruido → resolver marcador
Vacío → colocar Ruido

PELIGRO
ficha de bolsa → usa ICONO, ignora número
coloca tipo indicado → si entra contigo, ataca
```

### Bloque F — Resolver marcador de Ruido

```text
retira Ruido → roba ficha → usa REVERSO
coloca grupo en Pasillo → ficha a su pila
BLANCO vuelve a la bolsa
```

---

## Cara B — Combate y supervivencia

### Bloque G — Tres ataques

| Acción | Objetivo | Munición | Resultado |
|---|---|---|---|
| Disparar | 1 Intruso del mismo Compartimento | Solo con cara de Munición | +1 impacto y tirada de muerte |
| Acribillar | Intrusos de Pasillo adyacente | Siempre 1 paso | Reparte 1–4 impactos |
| Cuerpo a cuerpo | 1 Intruso del mismo Compartimento | No | +1 Contaminación; si vive, responde |

Tabla compacta de Acribillar:

```text
ADULTO 1 · LARVA 1 · DRON 2 exactos · REINA a su pista
```

Tabla compacta de Disparo:

```text
CRÍTICO → muere / Reina resuelve Salud
2–5 → muere si resultado ≤ impactos
MUNICIÓN → gasta 1 paso
```

### Bloque H — Reina

```text
IMPACTOS → pista
umbral / tirada mortal
→ roba Salud
→ descarta adicionales
→ resuelve efecto
→ pista a 0

MAZO VACÍO → REINA MUERTA → gira hoja de Intrusos
```

### Bloque I — Asegurar / Reforzar

| Asegurar Compartimento | Reforzar Pasillo |
|---|---|
| Máximo 3 | Solo vacío |
| Evita Ataque de Intruso que entra | Retira Ruido y gira a 0 |
| No protege en fase de Ataques | No bloquea Intrusos |
| No se coloca con Intrusos | Nunca en accesos del Hibernatorio |

### Bloque J — Equipo táctico

```text
MUNICIÓN → recarga; lleno = 2 gastos
OXÍGENO → +3, máximo 7
GRANADA → Acribillamiento +2
BOTIQUÍN → +2 Salud

1 acción permite usar VARIAS fichas, una a una
```

### Bloque K — Oxígeno y Asfixia

```text
MÁXIMO 7
Soporte vital Inactivo · fin de turno · −1
0 → ASFIXIA, dial queda en 0
próxima pérdida → MUERTE

quitar Asfixia:
ganar Oxígeno / acabar turno con Soporte activo
```

### Bloque L — Salidas

```text
TODAS → Usar Compartimento + tirada de Ruido
Intruso contigo tras tirada → FALLA

LANZADERA
debe aterrizar y superar Antiaéreo
despegue al inicio de Evento; decide 1 ocupante

HIBERNATORIO
descubierto + Activo
no protege de destrucción

CÁPSULA DE ESCAPE
huida inmediata; Antiaéreo no afecta
```

### Bloque M — Final

```text
RONDA 14 / todos fuera o muertos
↓
SIN LARVA → reúne cartas → INFECCIÓN
CON LARVA → +1 Contaminación → baraja todo → roba 4
Contaminación en esas 4 → MUERTE
↓
revela OBJETIVO
```

### Bloque N — Valores críticos

```text
ACCIONES              2
MANO                  5
OXÍGENO MÁXIMO        7
ASEGURAR MÁXIMO       3
OPORTUNIDAD MÁXIMO    3 ataques
PASILLO               6 Intrusos; Reina = 4
FINAL                 ronda 14
AUTODESTRUCCIÓN       +5 espacios
```

### Bloque O — FAQ de mesa

```text
AVERÍA EN COMPARTIMENTO ≠ borrar icono de Ordenador
AUTODESTRUCCIÓN activa → antes del chequeo final
PELIGRO → Reacción de Movimiento no evita su Ataque
«RETIRAR CARTA» ≠ efecto de Entrada
REFUGIO «SIEMPRE ASEGURADO» ≠ ficha descartable
ARMA SIN MUNICIÓN → puede «gastar» para efectos
ARMA AVERIADA → no puede gastar Munición
```

---

## Sistema visual

### Colores

- Negro carbón: fondo.
- Blanco: texto principal.
- Amarillo industrial: ronda, acciones y estructura.
- Azul cian: Soporte vital y Oxígeno.
- Rojo: Intrusos, Ataques, Fuego y muerte.
- Verde militar: Asegurar, Reforzar y Equipo táctico.
- Morado: Contaminación e infección.

El color nunca debe ser el único identificador.

### Iconos prioritarios

- carta de Acción;
- Oxígeno y Soporte vital activo/inactivo;
- Salud y Herida grave;
- Ruido y Peligro;
- Fuego y Avería;
- Asegurar y Pasillo reforzado;
- Disparo, Acribillamiento y Munición;
- Compartimento, Pasillo y Puerta;
- Larva, Adulto, Dron y Reina;
- Lanzadera, Hibernatorio y Cápsula de escape;
- Contaminación.

### Tipografía

- Máximo dos familias.
- Sans serif condensada para títulos y valores.
- Sans serif de alta legibilidad para reglas.
- Mayúsculas solo en fases, acciones y alertas.

---

## Restricciones de densidad

- Máximo 12 palabras por viñeta.
- Máximo 7 líneas por módulo, salvo fases y acciones.
- Nada de párrafos sobre ilustraciones.
- Flechas sin cruces.
- No reproducir efectos de cartas concretas.
- Si falta espacio, eliminar decoración antes que reglas.

---

## Control previo a impresión

- Aparecen las 4 fases y el orden es correcto.
- El turno contiene acciones, Oxígeno y Fuego.
- Pasar figura como acción.
- Se exige Ruido tras cada Movimiento.
- Peligro usa el frontal; resolver Ruido usa el reverso.
- Disparar y Acribillar no comparten objetivo ni gasto de Munición.
- Asegurar y Reforzar están separados.
- La Reina usa pista y mazo de Salud.
- El final contiene Infección antes de Eclosión y luego Objetivo.
- La Autodestrucción activa se resuelve antes del final.
- No aparecen Energía, Oscuridad, Encuentros, motores, coordenadas ni Contingencias.
- Se lee a distancia de brazo y en escala de grises.

---

[Resumen de turno](./RESUMEN-TURNO.md) · [Guía para novatos](./RESUMEN-Y-GUIA-NOVATO.md) · [FAQ oficial resumida](./FAQ-OFICIAL-RESUMIDA.md) · [Prompt de imagen](./PROMPT-IMAGEN-MUNDREL.md)
