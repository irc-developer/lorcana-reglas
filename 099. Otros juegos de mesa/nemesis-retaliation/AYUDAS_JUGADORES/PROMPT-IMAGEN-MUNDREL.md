# Nemesis: Represalia — Prompt para ayuda visual de ronda

## Objetivo

Generar una ayuda visual horizontal en proporción 12:7 para **Nemesis: Represalia** (*Nemesis: Retaliation*), pensada para explicar la ronda completa y resolver consultas frecuentes durante una partida base.

Debe condensar las cuatro fases, las tres partes del turno, Movimiento y Ruido, Disparo y Acribillamiento, Oxígeno, defensas y salida sin convertirse en un reglamento en miniatura.

**Fuentes mecánicas revisadas:**

- `doc/Nemesis-RT-Rulebook-EN.pdf` — reglamento final oficial de 40 páginas.
- `doc/RETALIATION_FAQ_v1.1.pdf` — FAQ oficial v1.1 de 19/11/2025.

**Límite de edición:** juego base con Primigenios. No usar contenido visual ni reglas de *Nemesis*, *Nemesis: Lockdown* o expansiones de *Retaliation*.

---

## Prompt listo para pegar

Crea una ayuda visual panorámica horizontal en proporción exacta **12:7** para el juego de mesa **NEMESIS: REPRESALIA**, cuyo título original es **NEMESIS: RETALIATION**. Debe ser una hoja de referencia funcional para jugadores novatos, densa pero muy ordenada y legible durante la partida. No quiero una portada, un póster cinematográfico ni una escena decorativa: quiero una ayuda que parezca un componente técnico del juego.

Mantén un lenguaje visual militar de ciencia ficción industrial:

- fondo negro carbón y metal oscuro;
- retícula de interfaz táctica;
- amarillo industrial para estructura y acciones;
- azul cian para Oxígeno y Soporte vital;
- verde militar para Asegurar, Reforzar y Equipo táctico;
- rojo de alarma para Intrusos, Fuego, Ataques y muerte;
- morado para Contaminación e infección;
- títulos blancos en mayúsculas y tipografía sans serif condensada;
- iconografía coherente para cartas de Acción, Oxígeno, Salud, Ruido, Peligro, Fuego, Avería, Asegurar, Munición, Compartimento, Pasillo, Puerta, tipos de Intruso, salidas y Contaminación.

El color nunca debe ser el único identificador. Usa símbolos, etiquetas y formas diferentes. La ilustración ambiental puede ocupar como máximo un 8 % de la pieza y nunca puede competir con las reglas.

No mezcles esta edición con las anteriores. Quedan prohibidos en la imagen: Energía, Oscuridad, Encuentros por tamaño de mano, motores, coordenadas de vuelo, cápsulas de escape del Nemesis original, SEC, búnker, Rover, Conocimiento, Contingencias y Acechadores nocturnos.

### Composición

Organiza la imagen en tres columnas y una franja inferior:

1. **Cabecera compacta:** título, edición y condiciones de victoria.
2. **Columna izquierda:** «TU TURNO», «ACCIONES» y «EQUIPO TÁCTICO».
3. **Columna central dominante:** «RONDA COMPLETA» y «MOVER → EXPLORAR → RUIDO».
4. **Columna derecha:** «COMBATE», «ASEGURAR / REFORZAR» y «OXÍGENO».
5. **Franja inferior:** «SALIDAS», «FINAL», «VALORES CRÍTICOS» y «FAQ».

La ronda y el flujo de Movimiento deben ser los bloques más grandes. Usa iconos grandes, flechas sin cruces, microtablas y frases breves. No uses párrafos dentro de la imagen.

### Texto mecánico exacto que debe aparecer

#### CABECERA

**NEMESIS: REPRESALIA — AYUDA DE RONDA**

Subtítulo pequeño: **RETALIATION · JUEGO BASE · PRIMIGENIOS**

**GANA = HUIR O HIBERNAR + CUMPLIR OBJETIVO + SOBREVIVIR A INFECCIÓN/ECLOSIÓN**

#### RONDA COMPLETA

Representa cuatro fases numeradas, con una flecha continua:

**1 · FASE DE LOS JUGADORES**

- Turnos en sentido horario hasta que todos Pasen.
- Cada turno: **2 ACCIONES → OXÍGENO → FUEGO**.

**2 · FASE DE LOS INTRUSOS**

- Intrusos en Fuego: **1 impacto**.
- Fuego en Nido: destruye **1 Huevo**.
- Intrusos en Compartimentos con personajes: **ATACAN**.

**3 · FASE DE EVENTO**

- Movimiento de Intrusos.
- Efecto principal.
- Efecto secundario.
- Desarrollo de la bolsa.

**4 · FASE DE ORDENAMIENTO**

- Pasa Jugador inicial.
- Roba hasta **5 cartas**.
- Avanza ronda y resuelve fichas.

#### TU TURNO

Usa un bloque A–B–C:

**A · REALIZA 2 ACCIONES**

**B · SOPORTE VITAL INACTIVO → −1 OXÍGENO**

**C · FUEGO EN TU COMPARTIMENTO → −1 SALUD**

Debajo:

- Pasar es una acción.
- Pasar no evita Oxígeno ni Fuego.
- Tras Pasar: sin más turnos, pero sí Reacciones.
- Contaminación no paga acciones.

#### ACCIONES Y COSTES

**0 CARTAS**

- Jugar carta de Acción.
- Pasar.

**1 CARTA**

- Moverse.
- Asegurar.
- Disparar.
- Acribillar.
- Cuerpo a cuerpo.
- Usar Objeto.
- Activar Robot.
- Intercambiar.
- Usar Equipo táctico.

**2 CARTAS**

- Usar Compartimento.
- Movimiento cauteloso.

Nota: **Fuera de Combate = no usar con Intrusos en tu Compartimento.**

#### MOVER → EXPLORAR → RUIDO

Construye este diagrama:

**ELIGE PASILLO**

↓

**¿INTRUSOS EN ORIGEN O PASILLO?**

Sí → **hasta 3 ATAQUES DE OPORTUNIDAD**, de mayor a menor.

↓

**¿DESTINO DESCUBIERTO?**

- Sí → mueve → Asegura si era cauteloso → tira Ruido.
- No → coloca Compartimento y Pasillos → marcadores → entra → efecto de Entrada.

Alerta grande:

**RUIDO DESPUÉS DE CADA MOVIMIENTO**

**También si llegas junto a otro personaje o un Intruso.**

#### TIRADA DE RUIDO

**RESULTADO 1–4 · resuelve TODOS los Pasillos adyacentes con ese valor**

- Intruso presente → el mayor entra y ataca.
- Ya hay Ruido → resuelve el marcador.
- Pasillo vacío → coloca Ruido.
- No existe ese valor → nada.

**PELIGRO**

- Roba ficha de la bolsa.
- Usa solo el **ICONO DEL FRONTAL**.
- Ignora el número del reverso.
- Coloca el tipo indicado; si entra contigo, ataca.

**RESOLVER RUIDO**

- Retira marcador.
- Roba ficha.
- Usa **NÚMERO DEL REVERSO**.
- Coloca el grupo en el Pasillo.
- Ficha a su pila; blanco vuelve a la bolsa.

#### COMBATE

Haz una tabla de tres filas:

**DISPARAR**

- 1 Intruso de tu Compartimento.
- Arma a distancia operativa y cargada.
- Añade 1 impacto y tira Disparo.
- Crítico: muere / Reina resuelve Salud.
- 2–5: muere si resultado ≤ impactos.
- Munición: gasta 1 paso.
- Disparar normalmente no gasta Munición.

**ACRIBILLAR**

- Grupo en Pasillo adyacente.
- Siempre gasta 1 paso de Munición.
- Reparte la tirada.
- Adulto 1 · Larva 1 · Dron 2 exactos · Reina a su pista.

**CUERPO A CUERPO**

- Intruso de tu Compartimento.
- Gana 1 Contaminación.
- Añade 1 impacto y tira Disparo.
- Si vive: avería un arma para evitar Ataque o recibe Ataque.

#### REINA

**IMPACTOS → PISTA DE LA REINA**

Al alcanzar umbral o con tirada que mataría un Adulto:

**ROBA SALUD → DESCARTA ADICIONALES → RESUELVE EFECTO → PISTA A 0**

**MAZO VACÍO → REINA MUERTA → GIRA HOJA DE INTRUSOS**

#### ASEGURAR / REFORZAR

Divide el bloque en dos:

**ASEGURAR COMPARTIMENTO**

- Máximo 3.
- No se coloca con Intrusos dentro.
- Descarta 1 para evitar Ataque de Intruso que entra.
- No protege de Intrusos ya presentes ni de la fase de Ataques.

**REFORZAR PASILLO**

- Solo Pasillo vacío.
- Retira Ruido y gira a valor 0.
- Las tiradas no colocan Ruido.
- Los Intrusos todavía pueden entrar.
- Nunca en Pasillos del Hibernatorio.

#### EQUIPO TÁCTICO

- **MUNICIÓN:** recarga; ficha llena = 2 gastos.
- **OXÍGENO:** +3, máximo 7.
- **GRANADA:** dado de Acribillamiento +2.
- **BOTIQUÍN:** +2 Salud.
- Una acción permite usar **VARIAS**, decidiendo una a una.

#### OXÍGENO

- Máximo **7**.
- Soporte vital Inactivo al final de cada turno: **−1**.
- Llegar a 0: recibe **ASFIXIA**, dial queda en 0.
- Próxima pérdida con Asfixia: **MUERTE**.
- Quita Asfixia al ganar Oxígeno o terminar turno con Soporte vital Activo.
- Soporte vital Activo no recupera Oxígeno.

#### SALIDAS

Cabecera:

**TODAS: USAR COMPARTIMENTO + TIRADA DE RUIDO**

**Intruso contigo después de la tirada → FALLA**

**LANZADERA**

- Debe aterrizar y superar Antiaéreo.
- Espera dentro; si aparece Intruso, sales.
- Al inicio de Evento, decide despegar cualquier ocupante.

**HIBERNATORIO**

- Debe estar descubierto y Activo.
- La destrucción del Complejo mata a quien Hiberna.

**CÁPSULA DE ESCAPE**

- Huida inmediata.
- Antiaéreo no afecta.

#### FINAL

**RONDA 14 / TODOS FUERA O MUERTOS**

↓

**SIN LARVA → reúne cartas → Procedimiento de Infección**

↓

**CON LARVA → +1 Contaminación → baraja todo → roba 4**

**Cualquier Contaminación entre las 4 → MUERTE**

↓

**REVELA Y COMPRUEBA OBJETIVO**

#### VALORES CRÍTICOS

- Acciones: **2**.
- Mano al reponer: **5**.
- Oxígeno máximo: **7**.
- Asegurar máximo: **3**.
- Ataques de oportunidad máximos: **3**.
- Intrusos por Pasillo: **6**; Reina = **4**.
- Final: **ronda 14**.
- Autodestrucción: **5 espacios por delante**.

#### FAQ / NO LO OLVIDES

- Avería en Compartimento **no borra** icono de Ordenador.
- Autodestrucción activa: antes del chequeo final.
- Peligro: una Reacción de Movimiento no evita su Ataque.
- «Retira esta carta» no es efecto de Entrada.
- Refugio «siempre asegurado» no es ficha descartable.
- Arma «No requiere Munición» puede «gastar» para efectos.
- Arma averiada no puede gastar Munición.

### Requisitos de legibilidad

- Español correcto y tildes completas.
- Ningún texto inventado o ilegible.
- No alterar valores, orden ni consecuencias.
- Máximo 12 palabras por viñeta cuando sea posible.
- Números de fase muy visibles.
- Diferencia inequívoca entre icono frontal y número del reverso de la ficha de Intruso.
- Diferencia inequívoca entre Disparar y Acribillar.
- Diferencia inequívoca entre Asegurar y Reforzar.
- Fondo de cada módulo casi negro y texto con contraste alto.
- Nada de texto sobre ilustraciones.

Antes de entregar, comprueba que la imagen contiene las cuatro fases, el turno A–B–C, la alerta de Ruido tras cada Movimiento y las tres condiciones de victoria.

---

## Prompt negativo

No crear portada, póster, escena cinematográfica, collage, tablero completo, manual en miniatura, texto diminuto, párrafos largos, tipografía ornamental, interfaz holográfica de bajo contraste, manchas detrás del texto, flechas cruzadas, iconos ambiguos, cifras inventadas ni reglas de otras entregas.

No incluir Energía, Oscuridad, Contingencia, Conocimiento, SEC, Rover, búnker, motores, coordenadas, cápsulas del Nemesis original, Encuentros por tamaño de mano ni Acechadores nocturnos.

---

## Validación posterior

Después de generar, comparar línea por línea con [AYUDA-VISUAL-MESA.md](./AYUDA-VISUAL-MESA.md). Si el generador de imagen deforma texto o iconos, conservar la composición como boceto y maquetar el contenido final con texto vectorial.

---

[Especificación visual](./AYUDA-VISUAL-MESA.md) · [Resumen de turno](./RESUMEN-TURNO.md) · [Guía para novatos](./RESUMEN-Y-GUIA-NOVATO.md) · [FAQ oficial resumida](./FAQ-OFICIAL-RESUMIDA.md)
