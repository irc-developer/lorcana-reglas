# Destino Google AI Studio

Comprobación documental: 18/10/2026. Fuente primaria:
[Generación de voz de Gemini](https://ai.google.dev/gemini-api/docs/speech-generation).
La documentación describe síntesis de una o varias voces y distingue TTS, que
recita un texto, de la generación de contenido. Las instrucciones de interpretación
deben separarse del texto que se quiere escuchar según los campos de la interfaz.

No fijar en la skill nombres de modelos, tamaños, voces o límites que puedan
cambiar. Verificar la interfaz elegida si la tarea requiere pasos concretos.
No prometer que veinticinco a treinta y cinco minutos quepan en una solicitud.

## Decisión práctica

Si la aplicación recibe conclusiones y construye el episodio, entregar un prompt
con dossier incorporado. Si recibe el diálogo para convertirlo en voz, entregar
el diálogo íntegro más la dirección de interpretación separada. El prompt que
solicita redactar un guion pertenece a la primera fase, aunque ambas fases se
realicen dentro de Google AI Studio.

Un fichero local no es una fuente accesible a Google por nombrarlo. El material
necesario debe estar incluido en el texto que Iván decida copiar. Los manifiestos
con referencias privadas quedan fuera del texto hablado.

La prueba local del prompt acredita preparación textual, no síntesis, duración,
pronunciación o calidad de voces. La revisión auditiva se registra solo después
de escuchar un audio real.

## Composer con Scene y bloques de hablante

Interfaz observada en captura de Iván del 18/10/2026: `Scene`, `Sample Context` y
bloques con selector de hablante/voz. Esta observación concreta no garantiza que
otras vistas o versiones tengan los mismos controles. La documentación primaria
describe a su vez transcripciones literales y atribución por turno; no acredita
por sí sola todos los botones de Composer.

- `Scene`: ambiente, relación entre voces, idioma, tono y ritmo. No pegar aquí el
  prompt para redactar el episodio ni el dossier estratégico.
- `Sample Context`: contexto breve si hace falta situar una continuación; para
  comenzar el episodio puede dejarse vacío. No inventar conversación previa.
- Cada intervención va en un bloque atribuido a su hablante. Por ejemplo,
  profesora en Speaker 1, interlocutor en Speaker 2, nueva intervención de la
  profesora en otro bloque de Speaker 1. Mantener estable la voz de cada papel.
  Quitar del texto hablado prefijos como «Profesora:» y números de turno.
- Entregar `SCENE.txt`, `GUION-POR-TURNOS.md` y dos extractos por voz con números
  de turno externos al texto copiable. Avisar que no se pegan los dos extractos
  íntegros en solo dos bloques: se perdería el orden de preguntas y respuestas.
  No prometer una importación o intercalado automático sin comprobar ese control.

Si se adapta un guion ya aceptado, conservar exactamente sus intervenciones y
verificar que, ordenando los dos extractos, se recupera el diálogo original.
Registrar la adaptación como sucesora de formato, sin alterar los recibos previos
ni simular un nuevo análisis de partidas.
