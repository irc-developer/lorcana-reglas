// Ejecutar en la consola de Discord WEB, desde la lista de tarjetas del foro.
// Abrir y recorrer manualmente cada publicación; exportar con lorcanaForo.descargar().
// Solo observa el HTML. No realiza peticiones, obtiene tokens ni pulsa botones.
(() => {
  "use strict";
  if (window.lorcanaForo) {
    console.info("Ya hay una captura de foro. Consulta lorcanaForo.estado() o descarga con lorcanaForo.descargar().");
    return;
  }
  const getRoute = () => location.pathname.match(/^\/channels\/(\d+)\/(\d+)(?:\/|$)/);
  const initial = getRoute();
  if (location.hostname !== "discord.com" || !initial) {
    throw new Error("Abre la lista de publicaciones de un foro en https://discord.com.");
  }
  const [, guildId, forumId] = initial;
  const messageSelector = '[id^="chat-messages-"], [data-list-item-id^="chat-messages___"]';
  const headingSelector = 'h1, h2, h3, [role="heading"]';
  const threads = new Map();
  const startedAt = new Date().toISOString();
  let active = true;
  let observer;

  const textOf = node => (node?.innerText || node?.textContent || "").trim();
  const unique = values => [...new Set(values)];
  const compareIds = (a, b) => BigInt(a.id) < BigInt(b.id) ? -1 : BigInt(a.id) > BigInt(b.id) ? 1 : 0;
  function identity(node) {
    const id = node.id || "";
    const listId = node.getAttribute?.("data-list-item-id") || "";
    const match = id.match(/^chat-messages-(\d+)-(\d+)$/)
      || listId.match(/^chat-messages___(\d+)-(\d+)$/);
    return match ? { threadId: match[1], messageId: match[2] } : null;
  }

  function ensureThread(id) {
    if (!threads.has(id)) {
      threads.set(id, {
        id,
        title: null,
        titleSource: null,
        url: `https://discord.com/channels/${guildId}/${id}`,
        firstSeenAt: new Date().toISOString(),
        messages: new Map(),
      });
    }
    return threads.get(id);
  }

  function findTitle(message, threadId) {
    // Buscar el encabezado en el panel del hilo, nunca en la lista global.
    // Heurística de HTML: si no se identifica con claridad, conservar null.
    if (!message.isConnected) return null;
    for (let parent = message.parentElement; parent && parent !== document.body; parent = parent.parentElement) {
      const peers = [...parent.querySelectorAll(messageSelector)];
      if (peers.some(node => identity(node)?.threadId !== threadId)) break;
      if (parent.querySelector('[data-list-id^="forum-channel-list"]')) break;
      const headings = [...parent.querySelectorAll(headingSelector)].filter(node =>
        !node.closest(messageSelector) && !node.closest('[contenteditable="true"]'));
      const titles = unique(headings.map(textOf).filter(Boolean));
      if (titles.length === 1) return titles[0];
      if (titles.length > 1) return null;
    }
    return null;
  }

  function capture(element) {
    const ids = identity(element);
    if (!ids || ids.threadId === forumId) return;
    const { threadId, messageId } = ids;
    const route = getRoute();
    // En una publicación a pantalla completa, solo admitir su propio panel.
    if (route?.[2] !== forumId && route?.[2] !== threadId) return;
    const observedText = textOf(element);
    const mediaUrls = [...element.querySelectorAll("img[src], video[src], source[src]")]
      .map(node => node.currentSrc || node.src)
      .filter(url => /^https?:\/\//.test(url) && !/\/(avatars|emojis|role-icons)\//.test(url));
    if (!observedText && !mediaUrls.length) return;
    const thread = ensureThread(threadId);
    if (thread.titleSource !== "manual") {
      const title = findTitle(element, threadId);
      if (title) {
        thread.title = title;
        thread.titleSource = "panel-heading-heuristic";
      }
    }
    const previous = thread.messages.get(messageId);
    const contentNode = element.querySelector(`[id="message-content-${messageId}"]`);
    const authorNode = element.querySelector(`[id="message-username-${messageId}"]`);
    const timestamp = element.querySelector("time[datetime]")?.getAttribute("datetime");
    const links = [...element.querySelectorAll("a[href]")]
      .map(node => node.href).filter(url => /^https?:\/\//.test(url));
    thread.messages.set(messageId, {
      id: messageId,
      channelId: threadId,
      url: `https://discord.com/channels/${guildId}/${threadId}/${messageId}`,
      author: textOf(authorNode) || previous?.author || null,
      timestamp: timestamp || previous?.timestamp || null,
      content: contentNode ? textOf(contentNode) : previous?.content ?? null,
      observedText: observedText || previous?.observedText || "",
      links: unique([...(previous?.links || []), ...links]),
      mediaUrls: unique([...(previous?.mediaUrls || []), ...mediaUrls]),
      firstSeenAt: previous?.firstSeenAt || new Date().toISOString(),
      lastSeenAt: new Date().toISOString(),
    });
  }

  function scan(root) {
    if (root.nodeType !== 1 && root.nodeType !== 9) return;
    if (root.matches?.(messageSelector)) capture(root);
    root.querySelectorAll(messageSelector).forEach(capture);
  }

  function allowedRoute() {
    const route = getRoute();
    // La pertenencia al foro se observa desde su vista inicial; no se infiere
    // que cualquier canal del servidor sea una publicación del mismo foro.
    return route?.[1] === guildId && (route[2] === forumId || threads.has(route[2]));
  }

  function consume(records) {
    if (!active) return;
    if (!allowedRoute()) {
      active = false;
      observer.disconnect();
      console.warn("Captura detenida: has salido del foro y sus publicaciones reconocidas. Descarga con lorcanaForo.descargar().");
      return;
    }
    for (const record of records) {
      record.removedNodes.forEach(scan);
      record.addedNodes.forEach(scan);
      const target = record.target.nodeType === 1 ? record.target : record.target.parentElement;
      const message = target?.closest(messageSelector);
      if (message) capture(message);
    }
    // También recoge encabezados que cargan después del contenido del hilo.
    scan(document);
  }

  function flush() {
    if (active) consume(observer.takeRecords());
  }

  function snapshot() {
    flush();
    return {
      schema: "lorcana-discord-forum-dom-v1",
      source: "manual-forum-browsing",
      guildId,
      forumId,
      startedAt,
      exportedAt: new Date().toISOString(),
      completeForumVerified: false,
      limitations: [
        "Solo se recopilan mensajes de publicaciones abiertas y cargadas en el navegador.",
        "No se enumeran todas las tarjetas ni se abren automáticamente.",
        "El título se identifica por el encabezado del panel cuando es posible; revisar titleSource.",
        "Tener el mensaje inicial no demuestra haber cargado todas las respuestas.",
        "El texto mostrado puede incluir citas, reacciones y etiquetas de la interfaz.",
        "Los adjuntos se guardan como enlaces que pueden caducar; no se descargan ni se hace OCR.",
      ],
      threads: [...threads.values()].sort(compareIds).map(thread => ({
        id: thread.id,
        title: thread.title,
        titleSource: thread.titleSource,
        url: thread.url,
        firstSeenAt: thread.firstSeenAt,
        firstPostCaptured: thread.messages.has(thread.id),
        completeThreadVerified: false,
        messages: [...thread.messages.values()].sort(compareIds),
      })),
    };
  }

  observer = new MutationObserver(consume);
  scan(document);
  observer.observe(document.body, {
    childList: true, subtree: true, characterData: true, attributes: true,
    attributeFilter: ["id", "data-list-item-id", "src", "href", "datetime"],
  });
  window.lorcanaForo = Object.freeze({
    estado() {
      const data = snapshot();
      return {
        activa: active,
        foro: forumId,
        publicaciones: data.threads.length,
        mensajes: data.threads.reduce((sum, thread) => sum + thread.messages.length, 0),
        detalle: data.threads.map(thread => ({
          id: thread.id, titulo: thread.title, mensajes: thread.messages.length,
          preguntaInicialCapturada: thread.firstPostCaptured,
        })),
      };
    },
    datos: snapshot,
    titular(id, title) {
      const thread = threads.get(String(id));
      if (!thread || typeof title !== "string" || !title.trim()) {
        throw new Error('Usa un ID capturado y un título: lorcanaForo.titular("ID", "Título").');
      }
      thread.title = title.trim();
      thread.titleSource = "manual";
      return thread.title;
    },
    descargar() {
      const data = snapshot();
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = `lorcana-foro-${forumId}-${Date.now()}.json`;
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      setTimeout(() => URL.revokeObjectURL(url), 10000);
      console.info(`Descarga solicitada: ${data.threads.length} publicaciones. Se conserva lo acumulado.`);
      return data.threads.length;
    },
    detener() {
      flush();
      active = false;
      observer.disconnect();
      return `${threads.size} publicaciones conservadas; aún puedes descargarlas.`;
    },
  });
  console.info(`Captura de foro iniciada: ${threads.size} publicaciones reconocidas. Abre las tarjetas en el panel lateral y recorre sus respuestas. Consulta lorcanaForo.estado() y descarga con lorcanaForo.descargar().`);
  if (!threads.size) {
    console.warn("Aún no se reconocen mensajes de publicaciones. Abre una tarjeta y comprueba lorcanaForo.estado(); si sigue en cero habrá que revisar el HTML o la URL inicial.");
  }
})();
