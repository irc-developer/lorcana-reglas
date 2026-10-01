"""Descubrimiento con el cliente Codex real, sin crear chats ni llamar al modelo."""
import sys
sys.dont_write_bytecode = True
import json
from pathlib import Path
import queue
import shutil
import subprocess
import threading

ROOT = Path(__file__).resolve().parents[2]


def verificar():
    binary = shutil.which("codex")
    if not binary:
        raise RuntimeError("Codex CLI no está en PATH")
    process = subprocess.Popen([binary, "app-server", "--strict-config"], cwd=ROOT,
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, encoding="utf-8")
    messages = queue.Queue()
    diagnostics = []

    def read_stdout():
        for line in process.stdout:
            try:
                messages.put(json.loads(line))
            except ValueError:
                continue
        messages.put({"end_of_stream": True})

    def read_stderr():
        for line in process.stderr:
            # Consumir para evitar bloqueo de pipes; no volcar ajustes, tokens ni datos de otros servidores.
            if "unknown configuration field" in line:
                diagnostics.append("Hay campos de configuración no admitidos por este cliente.")

    threading.Thread(target=read_stdout, daemon=True).start()
    threading.Thread(target=read_stderr, daemon=True).start()

    def request(number, method, params):
        process.stdin.write(json.dumps({"id": number, "method": method, "params": params}) + "\n")
        process.stdin.flush()
        while True:
            try:
                message = messages.get(timeout=40)
            except queue.Empty:
                raise RuntimeError("El cliente Codex no respondió en 40 s; comprobar permisos y configuración.") from None
            if message.get("end_of_stream"):
                raise RuntimeError("Codex terminó antes de responder. " + " ".join(diagnostics))
            if message.get("id") == number:
                if "error" in message:
                    raise RuntimeError(f"Codex rechazó {method}: {message['error'].get('code')}")
                return message["result"]

    try:
        request(1, "initialize", {"clientInfo": {"name": "lorcana-verificacion", "version": "0.1.0"}})
        process.stdin.write(json.dumps({"method": "initialized", "params": {}}) + "\n")
        process.stdin.flush()
        config = request(2, "config/read", {"cwd": str(ROOT), "includeLayers": False})
        if not config["config"].get("mcp_servers", {}).get("lorcana", {}).get("enabled"):
            raise RuntimeError("Codex no carga el MCP del proyecto; comprobar confianza y permisos del entorno.")
        inventory = request(3, "mcpServerStatus/list", {"detail": "toolsAndAuthOnly"})
        servers = inventory.get("data", [])
        while inventory.get("nextCursor"):
            inventory = request(4, "mcpServerStatus/list", {"detail": "toolsAndAuthOnly", "cursor": inventory["nextCursor"]})
            servers.extend(inventory.get("data", []))
        server = next((s for s in servers if s["name"] == "lorcana"), None)
        expected = {"estado_fuentes", "obtener_carta", "obtener_regla", "buscar_evidencia"}
        if server is None or set(server["tools"]) != expected:
            raise RuntimeError("El cliente no descubrió las cuatro herramientas de lorcana")
        return {"client": "Codex app-server (strict config)", "server": "lorcana", "tools": sorted(expected),
                "version": server.get("serverInfo", {}).get("version"),
                "model_called": False, "new_chat_verified": False}
    finally:
        process.stdin.close()
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.terminate()
            process.wait(timeout=10)


if __name__ == "__main__":
    print(json.dumps(verificar(), ensure_ascii=False, indent=2))
