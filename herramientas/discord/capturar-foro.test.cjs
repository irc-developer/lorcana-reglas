// Pruebas de agrupación y navegación con paneles simulados; sin acceso a Discord.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const source = fs.readFileSync(path.join(__dirname, "capturar-foro.js"), "utf8");

function message(thread, id, content, options = {}) {
  const node = {
    nodeType: 1,
    id: options.listId ? "" : `chat-messages-${thread}-${id}`,
    innerText: content,
    isConnected: true,
    parentElement: null,
    matches: () => true,
    closest() { return this; },
    getAttribute(name) {
      return name === "data-list-item-id" && options.listId ? `chat-messages___${thread}-${id}` : null;
    },
    querySelector(selector) {
      if (selector === `[id="message-content-${id}"]`) return { textContent: this.innerText };
      if (selector === `[id="message-username-${id}"]` && options.author) return { textContent: options.author };
      if (selector === "time[datetime]" && options.timestamp) return { getAttribute: () => options.timestamp };
      return null;
    },
    querySelectorAll(selector) {
      if (selector === "img[src], video[src], source[src]") return (options.media || []).map(src => ({ src }));
      if (selector === "a[href]") return (options.links || []).map(href => ({ href }));
      return [];
    },
  };
  return node;
}

function panel(title, messages) {
  const heading = { innerText: title, closest: () => null };
  const parent = {
    parentElement: null,
    querySelector: () => null,
    querySelectorAll: selector => selector.startsWith("h1") ? [heading] : messages,
  };
  messages.forEach(node => { node.parentElement = parent; });
  return parent;
}

function setup(initial = []) {
  let callback;
  let pending = [];
  let disconnected = false;
  const elements = initial;
  const downloads = [];
  const document = {
    nodeType: 9,
    body: { appendChild() {} },
    querySelectorAll: () => elements,
    createElement: () => ({ click() {}, remove() {} }),
  };
  const context = {
    window: {}, document,
    location: { hostname: "discord.com", pathname: "/channels/111/222" },
    console: { info() {}, warn() {} }, Blob,
    URL: { createObjectURL(blob) { downloads.push(blob); return "blob:test"; }, revokeObjectURL() {} },
    setTimeout: fn => fn(),
    MutationObserver: class {
      constructor(fn) { callback = fn; }
      observe() {}
      disconnect() { disconnected = true; }
      takeRecords() { const result = pending; pending = []; return result; }
    },
  };
  vm.runInNewContext(source, context);
  return {
    context, elements, downloads, api: context.window.lorcanaForo,
    emit: (addedNodes = [], removedNodes = [], target = document) => callback([{ addedNodes, removedNodes, target }]),
    queue: record => pending.push(record),
    disconnected: () => disconnected,
  };
}

(async () => {
  // Se puede iniciar desde un foro que aún no tiene una tarjeta abierta.
  const state = setup();
  assert.equal(state.api.estado().publicaciones, 0);
  const first = message("900000000000000001", "900000000000000001", "¿Shift activa Beckon?", {
    author: "Persona A", timestamp: "2026-09-03T02:38:00Z",
    media: ["https://cdn.discordapp.com/attachments/1/2/merida.png", "https://cdn.discordapp.com/avatars/3/4.png"],
  });
  const answer = message("900000000000000001", "900000000000000003", "Yes.");
  panel("Merida Wisp Conjurer and shift", [first, answer]);
  state.elements.push(first, answer);
  state.emit([first, answer]);
  let data = state.api.datos();
  assert.equal(data.threads.length, 1);
  assert.equal(data.threads[0].title, "Merida Wisp Conjurer and shift");
  assert.equal(data.threads[0].firstPostCaptured, true);
  assert.equal(data.threads[0].completeThreadVerified, false);
  assert.equal(data.threads[0].messages.length, 2);
  assert.equal(data.threads[0].messages[0].mediaUrls.length, 1);
  assert.equal(data.threads[0].messages[0].author, "Persona A");

  // Otra tarjeta retira el primer panel: ambas conversaciones se conservan.
  const other = message("900000000000000002", "900000000000000002", "Otra duda", { listId: true });
  panel("Ability Question", [other]);
  first.isConnected = answer.isConnected = false;
  state.elements.splice(0, 2, other);
  state.emit([other], [first, answer]);
  data = state.api.datos();
  assert.equal(data.threads.length, 2);
  assert.equal(data.threads[0].title, "Merida Wisp Conjurer and shift");
  assert.equal(data.threads[1].title, "Ability Question");
  assert.equal(data.threads[0].messages[1].content, "Yes.");
  assert.equal(state.api.estado().mensajes, 3);

  // Reabrir y editar no duplica mensajes. Un título manual tiene prioridad.
  state.api.titular("900000000000000001", "Título confirmado");
  first.isConnected = answer.isConnected = true;
  answer.innerText = "Yes. Additional explanation.";
  state.elements.splice(0, 1, first, answer);
  state.emit([first, answer]);
  data = state.api.datos();
  assert.equal(state.api.estado().mensajes, 3);
  assert.equal(data.threads[0].title, "Título confirmado");
  assert.equal(data.threads[0].titleSource, "manual");
  assert.equal(data.threads[0].messages[1].content, "Yes. Additional explanation.");

  // Un mensaje del foro principal no pasa a ser una publicación.
  const parentMessage = message("222", "99", "Canal principal");
  state.emit([parentMessage]);
  assert.equal(state.api.estado().publicaciones, 2);
  // Si solo se cargó una respuesta, declarar que falta la pregunta inicial.
  const partial = message("900000000000000004", "900000000000000005", "Solo una respuesta");
  state.emit([partial]);
  data = state.api.datos();
  assert.equal(data.threads[2].firstPostCaptured, false);
  assert.equal(data.threads[2].title, null);
  // Un mensaje compuesto únicamente por una imagen también se conserva.
  const imageOnly = message("900000000000000004", "900000000000000006", "", {
    media: ["https://cdn.discordapp.com/attachments/1/2/card.png"],
  });
  state.queue({ addedNodes: [imageOnly], removedNodes: [], target: state.context.document });
  assert.equal(state.api.descargar(), 3);
  const exported = JSON.parse(await state.downloads[0].text());
  assert.equal(exported.threads[2].messages.length, 2);
  assert.equal(exported.completeForumVerified, false);
  assert.equal(exported.threads[0].messages[1].url,
    "https://discord.com/channels/111/900000000000000001/900000000000000003");

  // Una publicación conocida a pantalla completa sigue dentro del alcance.
  state.context.location.pathname = "/channels/111/900000000000000001";
  assert.equal(state.api.estado().activa, true);
  // Un canal ajeno detiene la captura y no importa sus mensajes.
  const outsider = message("333", "100", "Fuera del foro");
  state.context.location.pathname = "/channels/111/333";
  state.elements.splice(0, 2, outsider);
  state.emit([outsider]);
  assert.equal(state.api.estado().activa, false);
  assert.equal(state.disconnected(), true);
  assert.equal(state.api.descargar(), 3);
  // Reejecutar el script nunca destruye una captura existente.
  vm.runInNewContext(source, state.context);
  assert.equal(state.context.window.lorcanaForo, state.api);

  // No tomar el encabezado de una tarjeta vecina como título del hilo.
  const untitled = message("444", "444", "Pregunta sin título reconocible");
  untitled.parentElement = {
    parentElement: null,
    querySelectorAll: () => [untitled, outsider],
    querySelector: () => null,
  };
  const noTitle = setup([untitled]);
  assert.equal(noTitle.api.datos().threads[0].title, null);
  noTitle.api.detener();
  assert.equal(noTitle.api.estado().activa, false);
  assert.equal(noTitle.api.descargar(), 1);
  console.log("OK: foro vacío, hilos laterales, títulos, deduplicación, medios, JSON, cobertura parcial, navegación y parada.");
})().catch(error => { console.error(error); process.exitCode = 1; });
