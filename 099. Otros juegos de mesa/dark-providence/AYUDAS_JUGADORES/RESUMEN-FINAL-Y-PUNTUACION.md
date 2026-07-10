# Cthulhu: Dark Providence - Final y puntuación

**Uso**: resolver final de partida sin abrir el reglamento  
**Fuente**: reglamento ES local, hoja-resumen visual y aclaraciones BGG del diseñador  
**Última validación**: 09/07/2026

---

## Cuándo se dispara el final

Resuelve por completo la acción que lo provoca y después puntuad.

| Disparador | Detalle |
|---|---|
| **PV** | Un jugador alcanza el umbral por número de jugadores. |
| **Locura** | Un jugador obtiene su 3ª Locura y revela Investigador o Disidente. |
| **Asesinato** | El Agente principal de un jugador es asesinado. |
| **Medidores** | Ritual o Investigación llega a la Última casilla. |
| **Profundos** | Se juega la acción de Profundos y los 8 Profundos están en juego. |

Nota FAQ: si algun Profundo fue aniquilado, puede ser imposible llegar a tener los 8 en juego. Los Profundos asesinados no se aniquilan: vuelven al suministro personal de su propietario.

### Umbrales de PV

| Jugadores | Umbral |
|---:|---:|
| 2 | 33 PV |
| 3 | 30 PV |
| 4 | 26 PV |
| 5 | 22 PV |

---

## Orden de puntuación

1. Suma PV que ya estaban en el marcador: Ciudades controladas y PV inmediatos de cartas.
2. Aplica puntuación general.
3. Revelad Lealtades no reveladas.
4. Aplica puntuación específica de Lealtad.
5. Aplica efectos de FINAL DE LA PARTIDA de Mitos.
6. Determinad la Lealtad eliminada.
7. Entre supervivientes, resolved ganador.

---

## Puntuación general

Todos los jugadores:

- +3 PV si su Lealtad no fue revelada durante la partida.
- PV de cartas y Agentes reclamados con PV genéricos o aplicables.
- Efectos de FINAL DE LA PARTIDA de Mitos.

Aviso: quien ya uso la acción **Revelar Lealtad** no vuelve a puntuar medidor ni Portales por esa Lealtad en el calculo final.

---

## Puntuación por Lealtad

### Investigadores

Puntuan:

- intervalo del medidor de Investigación;
- valor de cada Portal propio cerrado <img src="../img/icons/portal-cerrado.png" alt="[CER]" width="18">;
- PV de Agentes reclutados con PV de Investigador <img src="../img/icons/pv-investigador.png" alt="[PV-INV]" width="18">.

No puntúan por asesinatos ni Portales abiertos.

### Sectarios

Puntuan:

- intervalo del medidor de Ritual;
- 1 PV por cada Agente asesinado en su Cripta;
- valor de cada Portal propio abierto <img src="../img/icons/portal-abierto.png" alt="[ABR]" width="18">;
- PV de cartas de Mitos con PV de Sectario <img src="../img/icons/pv-sectario.png" alt="[PV-SEC]" width="18">;
- 1 PV por cada Agente Resucitado que controlen;
- 8 PV si reclamaron Profundos y los 8 Profundos están en juego.

No puntúan Portales cerrados.

### Disidentes

Puntuan:

- -3 PV si revelaron Lealtad antes de la puntuación final;
- Investigador disidente: intervalo del medidor de Investigación;
- Sectario disidente: intervalo del medidor de Ritual;
- valor de cada Portal propio cerrado <img src="../img/icons/portal-cerrado.png" alt="[CER]" width="18"> y abierto <img src="../img/icons/portal-abierto.png" alt="[ABR]" width="18">;
- 1 PV por cada Agente asesinado en su Cripta.

No puntúan PV de facción de cartas o Agentes reclamados: ni PV de Investigador ni PV de Sectario.

Impostor puede cambiar si un Disidente puntúa como Investigador Disidente o Sectario Disidente, pero nunca crea compañeros entre Disidentes.

---

## Determinar el ganador

Esta es la regla que más cambia la lectura de la partida:

1. Mira quien tiene la puntuación individual más baja.
2. Elimina a todos los jugadores que compartan Lealtad con ese jugador.
3. Si el peor es un único Disidente, solo se elimina ese jugador.
4. Los Disidentes nunca tienen compañeros: no eliminan a otro Disidente por compartir etiqueta tras Impostor.
5. Entre los jugadores restantes, gana quien tenga más PV.

### Empates por abajo

| Situacion | Resultado |
|---|---|
| Empatan los dos Disidentes como peor puntuación | Se elimina el Sectario Disidente. |
| Empate entre Disidente y Sectario | El empate favorece a Sectarios. |
| Empate entre Investigador y otro bando | El empate favorece a Investigadores. |

### Empates por arriba

1. Gana quien tenga más cartas de Mitos.
2. Si persiste, prioridad de Lealtades: Investigadores por encima de ambos; Sectarios por encima de Disidentes.
3. Si sigue el empate, victoria compartida.

---

## Checklist de cierre

- ¿Se resolvió por completo la acción que dispar? el final?
- ¿Todos sumaron PV ya obtenidos durante partida?
- ¿Se aplicó +3 PV por Lealtad oculta solo a quien correspondía?
- ¿Se revisaron Mitos con FINAL DE LA PARTIDA?
- ¿Los Disidentes evitaron puntuar PV de facción?
- ¿Se eliminó primero la Lealtad del jugador con menor PV?
- ¿El ganador se eligió solo entre los no eliminados?

---

[Resumen de turno](./RESUMEN-TURNO.md) - [FAQ BGG](../FAQs-Dark-Providence.md) - [Reglas completas](../Dark-Providence.md)
