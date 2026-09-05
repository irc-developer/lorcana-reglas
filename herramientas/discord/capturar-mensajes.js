// Ejecutar en la consola de Discord WEB, con el canal de dudas abierto.
// Lee los mensajes presentes en la página mientras tú desplazas el historial.
// No realiza peticiones, no obtiene credenciales y no desplaza la página.
(() => {
  "use strict";
  if (window.lorcanaCaptura) {
    console.info("Ya existe una captura. Usa lorcanaCaptura.estado() o .descargar().");
    return;
  }
  const route = location.pathname.match(/^\/channels\/(\d+)\/(\d+)(?:\/|$)/);
  if (!route || location.hostname !== "discord.com") {
    throw new Error("Abre un canal de servidor en https://discord.com y vuelve a ejecutar.");
  }
  const [, guildId, channelId] = route;
  const selector = '[id^="chat-messages-"]';
  const messages = new Map();
  const startedAt = new Date().toISOString();
  let active = true;
  let observer;

  function sameChannel() {
    const current = location.pathname.match(/^\/channels\/(\d+)\/(\d+)(?:\/|$)/);
    return current?.[1] === guildId && current?.[2] === channelId;
  }

  function capture(element) {
    // El ID incluye el canal: evita mezclar un hilo lateral u otro canal.
    const match = element.id?.match(/^chat-messages-(\d+)-(\d+)$/);
    if (!match || match[1] !== channelId) return;
    const id = match[2];
    const rawText = (element.innerText || element.textContent || "").trim();
    if (!rawText) return;
    const previous = messages.get(id);
    const contentNode = element.querySelector('[id^="message-content-"]');
    const authorNode = element.querySelector('[id^="message-username-"]');
    const timestamp = element.querySelector("time[datetime]")?.getAttribute("datetime");
    const links = [...element.querySelectorAll("a[href]")]
      .map(node => node.href).filter(url => /^https?:\/\//.test(url));
    const mediaUrls = [...element.querySelectorAll("img[src], video[src], source[src]")]
      .map(node => node.currentSrc || node.src)
      .filter(url => /^https?:\/\//.test(url) && !/\/(avatars|emojis)\//.test(url));
    messages.set(id, {
      id,
      channelId,
      url: `https://discord.com/channels/${guildId}/${channelId}/${id}`,
      // Algunos mensajes agrupados no muestran autor: no se infiere uno.
      author: authorNode?.textContent?.trim() || previous?.author || null,
      timestamp: timestamp || previous?.timestamp || null,
      content: contentNode
        ? (contentNode.innerText || contentNode.textContent || "").trim()
        : previous?.content ?? null,
      // Incluye contexto visible (respuesta citada, embeds, reacciones, etc.).
      observedText: rawText,
      links: [...new Set([...(previous?.links || []), ...links])],
      mediaUrls: [...new Set([...(previous?.mediaUrls || []), ...mediaUrls])],
      firstSeenAt: previous?.firstSeenAt || new Date().toISOString(),
      lastSeenAt: new Date().toISOString(),
    });
  }

  function scan(root) {
    if (root.nodeType !== 1 && root.nodeType !== 9) return;
    if (root.matches?.(selector)) capture(root);
    root.querySelectorAll(selector).forEach(capture);
  }

  function consume(records) {
    if (!active) return;
    if (!sameChannel()) {
      active = false;
      observer.disconnect();
      console.warn("Captura detenida al cambiar de canal. Descarga lo guardado con lorcanaCaptura.descargar().");
      return;
    }
    for (const record of records) {
      // Conservar también nodos retirados por la virtualización de la lista.
      record.removedNodes.forEach(scan);
      record.addedNodes.forEach(scan);
      const target = record.target.nodeType === 1
        ? record.target : record.target.parentElement;
      const message = target?.closest(selector);
      if (message) capture(message);
    }
  }

  function flush() {
    if (!active) return;
    consume(observer.takeRecords());
    if (active && sameChannel()) scan(document);
  }

  function snapshot() {
    flush();
    return {
      schema: "lorcana-discord-dom-v1",
      source: "manual-browser-scroll",
      guildId,
      channelId,
      startedAt,
      exportedAt: new Date().toISOString(),
      completeHistoryVerified: false,
      limitations: [
        "Solo incluye mensajes observados en la página durante esta captura.",
        "El texto corresponde a lo mostrado por Discord, no a una exportación de su API.",
        "Los autores y fechas ausentes no se han inferido.",
        "Los adjuntos son enlaces; no se descargan y sus URL pueden caducar.",
        "No se extrae el texto dentro de imágenes ni se recorren hilos automáticamente.",
      ],
      messages: [...messages.values()].sort((a, b) =>
        BigInt(a.id) < BigInt(b.id) ? -1 : BigInt(a.id) > BigInt(b.id) ? 1 : 0),
    };
  }

  observer = new MutationObserver(consume);
  scan(document);
  if (!messages.size) {
    throw new Error("No se han reconocido mensajes. Cierra paneles de búsqueda, abre el canal y espera a que cargue. Si persiste, habrá que adaptar el selector al HTML actual.");
  }
  observer.observe(document.body, {
    childList: true,
    subtree: true,
    characterData: true,
    attributes: true,
    attributeFilter: ["id", "src", "href", "datetime"],
  });
  window.lorcanaCaptura = Object.freeze({
    estado() {
      const data = snapshot();
      return {
        canal: channelId,
        mensajes: data.messages.length,
        activa: active,
        mensajeMasAntiguo: data.messages[0]?.url,
        mensajeMasReciente: data.messages.at(-1)?.url,
      };
    },
    datos: snapshot,
    descargar() {
      const data = snapshot();
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = `lorcana-discord-${channelId}-${Date.now()}.json`;
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      setTimeout(() => URL.revokeObjectURL(url), 10000);
      console.info(`Descarga solicitada: ${data.messages.length} mensajes. La captura conserva lo acumulado.`);
      return data.messages.length;
    },
    detener() {
      flush();
      active = false;
      observer.disconnect();
      return `${messages.size} mensajes conservados. Puedes descargarlos todavía.`;
    },
  });
  console.info(`Captura iniciada: ${messages.size} mensajes. Desplaza el canal despacio hacia mensajes anteriores. Usa lorcanaCaptura.estado() y lorcanaCaptura.descargar(). No recargues ni cierres esta pestaña antes de descargar.`);
})();
