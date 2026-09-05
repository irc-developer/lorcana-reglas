// Pruebas de acumulación con una página simulada; no conectan con Discord.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

function setup(initial = []) {
  let callback;
  let pending = [];
  let disconnected = false;
  const elements = initial;
  const body = { appendChild() {} };
  const document = {
    nodeType: 9,
    body,
    querySelectorAll: () => elements,
    createElement: () => ({ click() {}, remove() {} }),
  };
  const location = { hostname: "discord.com", pathname: "/channels/111/222" };
  const context = {
    window: {}, document, location, console: { info() {}, warn() {} },
    Blob, URL, setTimeout: fn => fn(),
    MutationObserver: class {
      constructor(fn) { callback = fn; }
      observe() {}
      disconnect() { disconnected = true; }
      takeRecords() { const result = pending; pending = []; return result; }
    },
  };
  const source = fs.readFileSync(path.join(__dirname, "capturar-mensajes.js"), "utf8");
  vm.runInNewContext(source, context);
  return {
    context, elements,
    api: context.window.lorcanaCaptura,
    emit: record => callback([record]),
    queue: record => pending.push(record),
    disconnected: () => disconnected,
  };
}

function message(id, text, channel = "222") {
  return {
    nodeType: 1,
    id: `chat-messages-${channel}-${id}`,
    innerText: text,
    matches: () => true,
    closest() { return this; },
    querySelector(selector) {
      if (selector.includes("message-content-")) return { textContent: this.innerText };
      return null;
    },
    querySelectorAll: () => [],
  };
}

const recent = message("999999999999999999", "Una pregunta reciente");
const old = message("999999999999999998", "Una pregunta anterior");
const state = setup([recent]);
assert.equal(state.api.estado().mensajes, 1);
// Discord retira el mensaje reciente y muestra uno anterior.
state.elements.splice(0, 1, old);
state.emit({ removedNodes: [recent], addedNodes: [old], target: state.context.document });
let data = state.api.datos();
assert.equal(data.messages.length, 2);
assert.equal(data.messages[0].id, old.id.split("-").at(-1));
assert.equal(data.messages[1].content, "Una pregunta reciente");
assert.equal(data.messages[0].author, null);
assert.equal(data.completeHistoryVerified, false);
// Ver de nuevo un mensaje lo actualiza sin duplicarlo.
old.innerText = "Pregunta anterior corregida";
state.emit({ removedNodes: [], addedNodes: [], target: old });
data = state.api.datos();
assert.equal(data.messages.length, 2);
assert.equal(data.messages[0].content, "Pregunta anterior corregida");
// Un hilo lateral pertenece a otro canal y queda fuera.
const thread = message("1000000000000000000", "Otro hilo", "333");
state.emit({ removedNodes: [], addedNodes: [thread], target: thread });
assert.equal(state.api.estado().mensajes, 2);
// Captura nodos añadidos y retirados antes de la siguiente lectura.
const transient = message("999999999999999997", "Bloque retirado");
state.queue({ removedNodes: [transient], addedNodes: [], target: state.context.document });
assert.equal(state.api.descargar(), 3);
// Cambiar de canal detiene la captura sin perder lo anterior.
state.context.location.pathname = "/channels/111/333";
state.elements.splice(0, 1, thread);
assert.equal(state.api.estado().activa, false);
assert.equal(state.api.datos().messages.length, 3);
assert.equal(state.disconnected(), true);
assert.equal(state.api.descargar(), 3);
// Fallar explícitamente si el HTML no contiene mensajes reconocibles.
assert.throws(() => setup([]), /No se han reconocido mensajes/);
const stopped = setup([recent]);
stopped.api.detener();
assert.equal(stopped.api.estado().activa, false);
assert.equal(stopped.api.datos().messages.length, 1);
console.log("OK: acumulación, orden de IDs, deduplicación, actualizaciones, aislamiento de canal, descarga y parada.");
