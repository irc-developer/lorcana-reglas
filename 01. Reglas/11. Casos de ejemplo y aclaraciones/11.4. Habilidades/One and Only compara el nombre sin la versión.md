## ❓ Duda

¿Cómo se resuelve [[02. Listado de Cartas/Set 13 - Attack of the Vine.md#One and Only|One and Only]] al elegir un personaje con un solo nombre, un personaje con distintas versiones o un personaje con varios nombres, como `Flotsam & Jetsam`?

---

## ✅ Respuesta

[[02. Listado de Cartas/Set 13 - Attack of the Vine.md#One and Only|One and Only]] conserva al personaje elegido y destierra a todos los demás personajes que compartan con él al menos un nombre exacto.

- La **versión** situada después del guion no se compara.
- Un nombre formado por varias palabras, como `Mickey Mouse`, sigue siendo un único nombre.
- Un personaje con `&` tiene tres nombres reglamentarios: cada nombre individual y el nombre impreso conjunto.
- `Other` excluye al personaje ya elegido, pero no protege a otras cartas con el mismo nombre.

Por tanto, si se elige un personaje llamado `A`, se destierran los demás `A` y los personajes de nombre múltiple que también cuenten como `A`. Si se elige `A & B`, se destierran los demás personajes llamados `A`, `B`, `A & B` o que compartan cualquiera de esos nombres.

---

## 🃏 Texto verificado de la carta

> **One and Only**
>
> `Choose a character. Banish all other characters with the same name as that character.`

La acción no exige que el personaje sea propio o rival. La primera frase elige un personaje; la segunda destierra a todos los demás personajes que tengan el mismo nombre que el elegido.

---

## 📘 Regla central de nombres en CR 2.2.0

### Nombre y versión

La regla **5.2.6** establece que un efecto que busca o compara un nombre solo consulta la línea de nombre e ignora la versión. El nombre y la versión forman el *nombre completo* de la carta, pero One and Only compara el **nombre**, no el nombre completo.

Esto significa que, si se elige `Winnie the Pooh – Hunny Archmage`:

- el personaje elegido permanece;
- se destierran las demás versiones de `Winnie the Pooh`;
- la versión impresa después del guion no impide la coincidencia.

Las notas oficiales de *Attack of the Vine!* confirman expresamente esta aplicación entre `Winnie the Pooh – Hunny Wizard` y `Winnie the Pooh – Hunny Archmage`.

### Nombres de varias palabras

Un nombre no se divide por palabras. `Mickey Mouse`, `Winnie the Pooh`, `Buzz Lightyear` o `Milo Thatch` son nombres únicos completos.

Por ejemplo, elegir `Buzz Lightyear` no hace coincidir un hipotético personaje llamado solo `Buzz`. La coincidencia debe ser exacta.

### Personajes con varios nombres

Las reglas **5.2.6.1–5.2.6.2** determinan que un personaje con `&` tiene dos nombres individuales además de su nombre impreso, aunque continúa siendo un solo personaje.

[[02. Listado de Cartas/Set 4 - Ursula's Return.md#Flotsam & Jetsam - Entangling Eels|Flotsam & Jetsam – Entangling Eels]] cuenta simultáneamente como:

- `Flotsam`;
- `Jetsam`;
- `Flotsam & Jetsam`.

La regla **5.2.6.3** añade una excepción expresa: [[02. Listado de Cartas/Set 6 - Azurite Sea.md#Chip 'n' Dale - Recovery Rangers|Chip 'n' Dale – Recovery Rangers]] se trata como si su nombre contuviera `&`. Por ello cuenta como `Chip`, `Dale` y `Chip 'n' Dale`.

---

## 🔎 Todos los casos de comparación

En la tabla siguiente, `A`, `B` y `C` representan nombres exactos completos, no palabras sueltas.

| Personaje elegido | Otro personaje en juego | ¿Se destierra? | Motivo |
|---|---|---:|---|
| `A` | otra versión de `A` | Sí | La versión se ignora |
| `A` | otra copia de `A` | Sí | Comparte el nombre `A` |
| `A` | `A & B` | Sí | El personaje múltiple también se llama `A` |
| `A` | `A & C` | Sí | Comparten el nombre `A` |
| `A` | `B` | No | No comparten ningún nombre |
| `A` | `A Something` | No | La coincidencia no es exacta |
| `A & B` | `A` | Sí | Comparten el nombre `A` |
| `A & B` | `B` | Sí | Comparten el nombre `B` |
| `A & B` | otro `A & B` | Sí | Comparten el nombre impreso y los individuales |
| `A & B` | `A & C` | Sí | Comparten el nombre `A` |
| `A & B` | `B & C` | Sí | Comparten el nombre `B` |
| `A & B` | `C` o `C & D` | No | No comparten ningún nombre |

La forma práctica de decidirlo es comparar los conjuntos de nombres de ambos personajes. Si tienen al menos un nombre exacto en común y no se trata del personaje elegido, One and Only intenta desterrarlo.

---

## 🧪 Ejemplos completos

### Elegir un personaje con un solo nombre

En juego hay:

- un `Flotsam` elegido para One and Only;
- otro `Flotsam` de una versión distinta;
- `Flotsam & Jetsam`;
- un `Jetsam` individual.

Resultado:

- el `Flotsam` elegido permanece;
- el otro `Flotsam` es desterrado;
- `Flotsam & Jetsam` es desterrado porque también se llama `Flotsam`;
- `Jetsam` permanece porque no se llama `Flotsam`.

### Elegir un personaje con varios nombres

Si se elige `Flotsam & Jetsam`, el personaje elegido permanece y se destierran:

- los demás `Flotsam`;
- los demás `Jetsam`;
- los demás `Flotsam & Jetsam`;
- cualquier otro personaje de nombre múltiple que comparta `Flotsam` o `Jetsam`.

No se elige cuál de sus tres nombres se utiliza: One and Only compara todos los nombres que tiene el personaje elegido.

---

## ⚙️ Interacciones relevantes

### Controlador y estado del personaje

Puede elegirse un personaje propio o rival, preparado o agotado, seco o secándose, dañado o sin daño, siempre que sea una elección legal. El efecto tampoco limita quién controla a los demás personajes, por lo que destierra tanto personajes propios como rivales que coincidan.

En una partida multijugador ordinaria, `all other characters` alcanza a los personajes de todos los jugadores. Las reglas completas 2.2.0 no cubren las variantes de juego por equipos.

### Ward

Un personaje rival con [[8.15 Protección (ward)|Ward]] no puede ser el personaje elegido inicialmente, porque Ward impide que un oponente elija esa carta al resolver un efecto.

Sin embargo, Ward no protege a los demás personajes coincidentes: One and Only solo elige al personaje de la primera frase. Los demás son afectados sin ser elegidos y, conforme a **8.15.2**, también pueden ser desterrados.

El jugador sí puede elegir uno de sus propios personajes con Ward, porque Ward solo restringe las elecciones de los oponentes.

### Vanish

Si el personaje elegido es rival y tiene [[8.14. Desvanecer (Vanish)|Vanish]], su habilidad se dispara al ser elegido. No se resuelve inmediatamente:

1. One and Only termina de resolverse y destierra a los demás personajes coincidentes.
2. Después se resuelve Vanish desde la bolsa.
3. Vanish destierra también al personaje que One and Only había conservado, si todavía está en juego.

Los demás personajes con Vanish no disparan esa palabra clave por One and Only, porque no fueron elegidos; simplemente son desterrados por el efecto general si sus nombres coinciden.

### Pilas y Shift

En una pila solo la carta superior está en juego. Las cartas situadas debajo no están en juego, no pueden elegirse y sus nombres no se utilizan para la comparación.

- Si la carta superior es el personaje elegido, toda su pila permanece.
- Si la carta superior de otra pila comparte un nombre y es desterrada, todas las cartas de esa pila se mueven con ella al descarte.

### Efectos de reemplazo

Si otro personaje coincidente tiene un efecto que reemplaza su destierro, ese reemplazo se aplica normalmente. El evento original de destierro no ocurre para ese personaje y sucede el evento modificado indicado por la habilidad.

El personaje elegido no necesita ese tipo de protección: One and Only no intenta desterrarlo debido a la palabra `other`.

### Habilidades disparadas por el destierro

Las habilidades que se disparen cuando uno de los demás personajes sea desterrado se añaden a la bolsa durante la resolución, pero esperan hasta que la acción termine de resolverse.

Los personajes son desterrados por el efecto de la acción, no por el personaje elegido. Por tanto, no se cumple una condición que exija que un personaje haya desterrado a otro.

### Sin duplicados o sin elección legal

- Si se elige un personaje que no comparte nombre con ningún otro, One and Only no destierra nada y el personaje elegido permanece.
- Si al llegar a la primera frase no existe ningún personaje que pueda elegirse legalmente, el efecto se resuelve sin efecto. Esto puede ocurrir, por ejemplo, si los únicos personajes disponibles son personajes rivales con Ward.
- Las elecciones se realizan al resolver la acción, no al anunciarla.

---

## 🔄 Secuencia oficial

1. Se juega One and Only y se paga su coste.
2. Al resolver la primera frase, se elige un personaje legal.
3. Se determina cada nombre reglamentario de ese personaje conforme a **5.2.6–5.2.6.3**, sin incluir la versión.
4. Se identifican todos los demás personajes en juego que compartan al menos uno de esos nombres exactos.
5. One and Only intenta desterrar a todos esos personajes; se aplican los efectos de reemplazo que correspondan.
6. Las habilidades disparadas durante la resolución se añaden a la bolsa y esperan.
7. One and Only termina de resolverse y se coloca en el descarte.
8. Se realiza la comprobación del estado del juego y después se resuelven las habilidades pendientes de la bolsa según las reglas aplicables.

---

## 📘 Fundamento en reglas

- [[5.2. Partes de una carta (Parts of a Card)|5.2.6. Nombre]]: compara la línea de nombre completa e ignora la versión.
- [[5.2. Partes de una carta (Parts of a Card)|5.2.6.1–5.2.6.3. Múltiples nombres]]: los personajes con `&` tienen los dos nombres individuales y el nombre impreso; `Chip 'n' Dale` es la excepción tratada como `&`.
- [[5.3. Personajes (Characters)|5.3.1. Personajes]]: una carta de personaje solo es un personaje mientras está en juego.
- [[6.1. General (General)|6.1.2–6.1.3. Orden y elecciones]]: las frases se resuelven en orden y las elecciones se realizan durante la resolución.
- [[6.1. General (General)|6.1.6. Another y other]]: `other` excluye la carta ya elegida, no las demás cartas con el mismo nombre.
- [[6.5. Efectos de Reemplazo (Replacement Effects)|6.5. Efectos de reemplazo]]: un reemplazo aplicable modifica el evento antes de que ocurra.
- [[6.7. Resolución de Cartas y Efectos (Resolving Cards and Effects)|6.7.2–6.7.5. Resolución, disparos y GSC]]: se siguen las instrucciones en orden; los disparos esperan hasta terminar la acción.
- [[8.14. Desvanecer (Vanish)|8.14. Vanish]]: se dispara al elegir al personaje rival y se resuelve después de la acción.
- [[8.15 Protección (ward)|8.15. Ward]]: impide elegir la carta, pero no evita efectos que no la eligen.
- [[5.1. Estados de las cartas (Card States)|5.1.1.5–5.1.1.8. Pilas y cartas en juego]]: las cartas debajo no están en juego y acompañan a la superior cuando esta abandona el juego.

---

## 🚫 Errores comunes

- Comparar la versión situada después del guion.
- Dividir un nombre de varias palabras como si fueran varios nombres.
- Pensar que un personaje `A & B` solo se llama `A & B`.
- Elegir uno de los nombres de un personaje múltiple en vez de aplicar todos sus nombres.
- Creer que Ward protege a los personajes que no fueron elegidos.
- Consultar los nombres de las cartas situadas debajo de una pila.
- Desterrar al personaje elegido como parte del efecto de One and Only.

---

## 🔗 Véase también

- [[No tener objetivo legal vs elegir un objetivo inválido]]
- [[Vanish e interacciones]]
- [[Shift y Webby's Diary - diferencia entre encima y debajo]]
- [[Mickey Mouse & Minnie Mouse necesita dos personajes para Duo Shift]]

---

## 📝 Fuente y estado

Caso resuelto exclusivamente con las [[Documentacion Oficial/Comprehensive-Rules_2.2.0-EN.pdf|Comprehensive Rules 2.2.0]], efectivas desde el 9 de julio de 2026, y las [[Documentacion Oficial/Attack-of-the-Vine-Set-Release-Notes_EN.pdf|Attack of the Vine! Set Release Notes]].

El ejemplo de las dos versiones de `Winnie the Pooh` es un *ruling* expreso de las notas del set. La aplicación a personajes con varios nombres se obtiene de la definición normativa de **5.2.6.1–5.2.6.3** y de la aclaración oficial de que un personaje con dos nombres cuenta con tres nombres.

---

## 🏷️ Tags

#banish #multiple-names #one-and-only #replacement-effect #shift #triggered-ability #vanish #ward
