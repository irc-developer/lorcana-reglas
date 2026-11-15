"""Lectura personal y reanudable de Duels.ink, solo con biblioteca estándar."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

# Permite también ejecutar las CLI directamente desde otro directorio.
if str(Path(__file__).resolve().parents[2]) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from herramientas.rutas_trabajo import resolver_ruta, ruta_trabajo

BASE = "https://duels.ink"
ROOT = Path(__file__).resolve().parents[2]
VERSION = 1


class DuelsError(Exception):
    """Mensaje seguro: nunca incluye cuerpos, URLs privadas ni credenciales."""


class AuthError(DuelsError):
    pass


class RequestError(DuelsError):
    def __init__(self, code, status=None):
        self.code, self.status = code, status
        super().__init__(f"{code}" + (f" (HTTP {status})" if status else ""))


def now():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def utc(value):
    try:
        date = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if date.tzinfo is None:
            raise ValueError
        precision = "microseconds" if date.microsecond % 1000 else "milliseconds"
        return date.astimezone(timezone.utc).isoformat(timespec=precision).replace("+00:00", "Z")
    except (ValueError, AttributeError):
        raise DuelsError("Fecha inválida: usa ISO 8601 con Z o desplazamiento horario") from None


def date_argument(value):
    try:
        return utc(value)
    except DuelsError as exc:
        raise argparse.ArgumentTypeError(str(exc)) from None


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(data):
    return (json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def atomic(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("wb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temp, path)


def load_token(env_file=ROOT / ".env", variable=None):
    """No shell, interpolación, ejecución ni escritura del .env. Entorno prevalece."""
    values = {}
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8-sig").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            match = re.fullmatch(r"(?:export\s+)?([A-Za-z_][A-Za-z_0-9-]*)\s*=\s*(.*)", line)
            if not match:
                raise DuelsError("Formato .env no admitido; usa NOMBRE=valor en una línea")
            key, value = match.groups()
            if value.startswith(('"', "'")):
                quote = value[0]
                end = value.find(quote, 1)
                if end < 0 or (value[end + 1:].strip() and not value[end + 1:].strip().startswith("#")):
                    raise DuelsError("Valor entrecomillado no admitido en .env")
                value = value[1:end]
            else:
                value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
            values[key] = value
    keys = [variable] if variable else ["DUELS_TOKEN", "DUELS_API_TOKEN", "duels-token"]
    # Primero todas las alternativas de entorno, después el archivo.
    token = next((os.environ[k] for k in keys if os.environ.get(k)), None)
    token = token or next((values[k] for k in keys if values.get(k)), None)
    if not token:
        raise AuthError("Falta token: configura DUELS_TOKEN o --token-env; se admite duels-token local")
    if not re.fullmatch(r"[0-9A-Fa-f]{96}", token):
        raise AuthError("El token local no tiene el formato personal documentado (96 caracteres hex)")
    return token


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def delay(headers, body=b"", fallback=1):
    value = headers.get("Retry-After")
    if value:
        try:
            return max(0, float(value))
        except ValueError:
            try:
                return max(0, parsedate_to_datetime(value).timestamp() - time.time())
            except (ValueError, TypeError, OverflowError):
                pass
    try:
        return max(0, float(json.loads(body)["retryAfterSeconds"]))
    except (ValueError, TypeError, KeyError):
        return fallback


class Client:
    """Una petición simultánea; cupos conservadores y reintentos acotados."""
    def __init__(self, token, *, opener=None, sleep=time.sleep, clock=time.time, retries=3):
        self._token = token
        self.opener = opener or urllib.request.build_opener(NoRedirect())
        self.sleep, self.clock, self.retries = sleep, clock, retries
        self.ready = {}
        self.requests = 0

    def wait(self, seconds):
        # Trozos pequeños para permitir interrupción incluso con Retry-After largo.
        while seconds > 0:
            step = min(seconds, 30)
            self.sleep(step)
            seconds -= step

    def request(self, url, *, method="GET", payload=None, authenticated=False, bucket="cdn"):
        parsed = urllib.parse.urlsplit(url)
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
            raise RequestError("unsafe_download_url")
        same_origin = (parsed.scheme, parsed.netloc) == ("https", "duels.ink")
        path = parsed.path
        allowed = ((method == "GET" and path in ("/api/me", "/api/me/match-history")) or
                   (method == "POST" and path in ("/api/me/bulk-replays", "/api/me/bulk-gamelogs")) or
                   (method == "GET" and (path.startswith("/r/") or path.startswith("/g/"))))
        if authenticated and (not same_origin or not allowed):
            raise RequestError("credential_origin_or_route_denied")
        headers = {"User-Agent": "Mozilla/5.0 DuelsPersonalReader/1", "Accept": "application/json", "Accept-Encoding": "identity"}
        if authenticated:
            headers["Authorization"] = "Bearer " + self._token
        if payload is not None:
            headers["Content-Type"] = "application/json"
        interval = 3.1 if bucket == "history" else 2.1
        for attempt in range(self.retries + 1):
            self.wait(max(0, self.ready.get(bucket, 0) - self.clock()))
            self.ready[bucket] = self.clock() + interval
            req = urllib.request.Request(url, data=encode(payload) if payload is not None else None,
                                         headers=headers, method=method)
            try:
                self.requests += 1
                with self.opener.open(req, timeout=45) as response:
                    body, status, received = response.read(), response.status, dict(response.headers)
            except urllib.error.HTTPError as exc:
                body, status, received = exc.read(), exc.code, dict(exc.headers)
            except (urllib.error.URLError, TimeoutError, OSError):
                if attempt == self.retries:
                    raise RequestError("network_failed") from None
                self.wait(2 ** attempt)
                continue
            received = {k.lower(): v for k, v in received.items()}
            if received.get("x-ratelimit-remaining") == "0":
                try:
                    self.ready[bucket] = max(self.ready[bucket], float(received["x-ratelimit-reset"]) + 1)
                except (ValueError, KeyError):
                    self.ready[bucket] = max(self.ready[bucket], self.clock() + 61)
            if status == 401:
                raise AuthError("HTTP 401: token ausente, caducado, revocado o sin alcance; importación detenida")
            if status == 429 or 500 <= status <= 599:
                if attempt < self.retries:
                    self.wait(delay({"Retry-After": received.get("retry-after", "")}, body, 2 ** attempt))
                    continue
            if status in (301, 302, 303, 307, 308):
                return body, status, received
            if status != 200:
                raise RequestError("http_failed", status)
            return body, status, received
        raise RequestError("retries_exhausted")

    def api(self, path, params=None, ids=None):
        if path not in ("/api/me", "/api/me/match-history", "/api/me/bulk-replays", "/api/me/bulk-gamelogs"):
            raise RequestError("route_denied")
        url = BASE + path + (("?" + urllib.parse.urlencode(params)) if params else "")
        body, status, headers = self.request(url, method="POST" if ids is not None else "GET",
                                             payload={"ids": ids} if ids is not None else None,
                                             authenticated=True, bucket="history" if "match-history" in path else path)
        if status != 200:
            raise RequestError("api_redirect_denied", status)
        try:
            value = json.loads(body)
        except (ValueError, UnicodeError):
            raise RequestError("api_invalid_json") from None
        return value, body, headers

    def download(self, url):
        chain = []
        # NoRedirect impide que urllib copie Authorization al CDN. Tras primer salto,
        # nunca se reintroduce la credencial, aunque el CDN redirija al origen.
        for hop in range(6):
            p = urllib.parse.urlsplit(url)
            auth = hop == 0 and p.netloc == "duels.ink" and p.scheme == "https"
            bucket = "/r/" if p.path.startswith("/r/") and auth else "/g/" if auth else "cdn"
            body, status, headers = self.request(url, authenticated=auth, bucket=bucket)
            chain.append({"url": url, "status": status})
            if status == 200:
                return body, headers, chain
            location = headers.get("location")
            if not location:
                raise RequestError("redirect_without_location")
            url = urllib.parse.urljoin(url, location)
        raise RequestError("too_many_redirects")


def original(out, body, suffix):
    digest = sha(body)
    relative = f"raw/{digest}{suffix}"
    path = out / relative
    if path.exists() and sha(path.read_bytes()) != digest:
        # Conservar bytes dañados para inspección; no sobreescribir evidencia.
        relative = f"raw/{digest}-recovered-{time.time_ns()}{suffix}"
        path = out / relative
    if not path.exists():
        atomic(path, body)
    return {"path": relative, "sha256": digest, "bytes": len(body)}


def observation(out, body, endpoint, params, headers):
    return {"endpoint": endpoint, "parameters": params, "acquired_at": now(),
            "file": original(out, body, ".json"),
            "headers": {k: v for k, v in headers.items() if k in
                        ("content-type", "etag", "last-modified", "x-ratelimit-limit", "x-ratelimit-remaining", "x-ratelimit-reset")}}


def validate_asset(kind, data, row):
    """Validación estructural de entrada; la auditoría completa usa el extractor."""
    if kind == "replay":
        if not isinstance(data, dict) or data.get("format") != "duels-replay-v1":
            raise RequestError("unsupported_replay_format")
        if data.get("gameId") != row["game_id"] or data.get("perspective") != row.get("your_player"):
            raise RequestError("replay_identity_mismatch")
        if not isinstance(data.get("baseSnapshot"), dict) or not isinstance(data.get("frames"), list) or not isinstance(data.get("logs"), list):
            raise RequestError("invalid_replay_structure")
        if data["baseSnapshot"].get("viewingAs") != data["perspective"]:
            raise RequestError("replay_perspective_mismatch")
        return {"format": data["format"], "frames": len(data["frames"]), "logs": len(data["logs"])}
    # El contrato HTTP no especifica esquema interno del gamelog: no inventarlo.
    if not isinstance(data, (dict, list)):
        raise RequestError("invalid_gamelog_structure")
    return {"json_type": type(data).__name__, "items": len(data)}


class Importer:
    def __init__(self, out, client):
        self.out, self.client = resolver_ruta(out), client
        self.path = self.out / "manifest.json"
        self.m = json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else None
        if self.m and self.m.get("schema_version") != VERSION:
            raise DuelsError("Versión de manifiesto no admitida")

    def save(self):
        self.m["updated_at"] = now()
        atomic(self.path, encode(self.m))

    def run(self, params, *, max_pages=1, download_games=0, skip_history=False,
            retry_unavailable=False, game_ids=None):
        """Usar bajo Lock(out). No cambiar parámetros de una ventana ya iniciada."""
        try:
            account = self.identity(params)
            pages = 0 if skip_history else self.enumerate(max_pages)
            selected = self.assets(download_games, retry_unavailable, game_ids)
            statuses = {}
            for game in self.m["games"].values():
                for kind, asset in game["assets"].items():
                    key = kind + ":" + asset["status"]
                    statuses[key] = statuses.get(key, 0) + 1
            return {"account_name": account.get("name"), "account_confirmed": True,
                    "games": len(self.m["games"]), "new_pages": pages,
                    "enumeration_complete": self.m["state"]["enumeration_complete"],
                    "selected_games": selected, "assets": statuses, "http_requests": self.client.requests}
        except (DuelsError, KeyboardInterrupt) as exc:
            if self.m:
                self.m["errors"].append({"at": now(), "code": exc.code if isinstance(exc, RequestError) else
                                          "authentication_failed" if isinstance(exc, AuthError) else "interrupted_or_local_error",
                                          "recoverable": not isinstance(exc, AuthError)})
                self.save()
            raise

    def identity(self, params):
        value, body, headers = self.client.api("/api/me")
        if not isinstance(value, dict) or not isinstance(value.get("id"), str) or not value["id"]:
            raise RequestError("invalid_account")
        if self.m and self.m["account"]["id"] != value["id"]:
            raise DuelsError("La cuenta no coincide con el manifiesto; usa otro directorio")
        if self.m and self.m["parameters"] != params:
            raise DuelsError("Los parámetros no coinciden; reanuda sin filtros o usa otro directorio")
        if not self.m:
            self.m = {"schema_version": VERSION, "source": BASE, "created_at": now(), "account": {},
                      "parameters": params, "state": {"next_cursor": None, "enumeration_complete": False, "pages": 0, "cursor_hashes": []},
                      "games": {}, "observations": [], "errors": []}
        self.m["account"] = value
        self.m["observations"].append(observation(self.out, body, "/api/me", {}, headers))
        self.save()
        return value

    def enumerate(self, max_pages):
        count = 0
        while not self.m["state"]["enumeration_complete"] and (max_pages == 0 or count < max_pages):
            params = dict(self.m["parameters"])
            cursor = self.m["state"]["next_cursor"]
            if cursor is not None:
                params["cursor"] = cursor
            page, body, headers = self.client.api("/api/me/match-history", params)
            obs = observation(self.out, body, "/api/me/match-history", params, headers)
            self.m["observations"].append(obs)
            self.save()
            if not isinstance(page, dict) or not isinstance(page.get("games"), list) or "next_cursor" not in page:
                raise RequestError("invalid_history_page")
            nxt = page["next_cursor"]
            seen = self.m["state"].setdefault("cursor_hashes", [])
            if nxt is not None and (not isinstance(nxt, str) or not nxt or nxt == cursor or
                                    sha(nxt.encode()) in seen or not page["games"]):
                raise RequestError("invalid_or_repeated_cursor")
            # Toda la página se valida antes de mutar el checkpoint.
            for row in page["games"]:
                if not isinstance(row, dict) or not isinstance(row.get("game_id"), str) or not row["game_id"]:
                    raise RequestError("invalid_history_row")
                if row.get("your_user_id") != self.m["account"]["id"]:
                    raise RequestError("history_account_mismatch")
            for index, row in enumerate(page["games"]):
                key = row["game_id"]
                entry = self.m["games"].setdefault(key, {"game_id": key, "account_id": self.m["account"]["id"],
                                                        "row_versions": [], "assets": {}})
                entry["row"] = row
                source = {"file": obs["file"], "index": index, "acquired_at": obs["acquired_at"], "row_sha256": sha(encode(row))}
                entry["row_source"] = source
                if not entry["row_versions"] or entry["row_versions"][-1]["row_sha256"] != source["row_sha256"]:
                    entry["row_versions"].append(source)
                for kind in ("replay", "gamelog"):
                    asset_id = row.get("replay_id") if kind == "replay" else key
                    previous = entry["assets"].get(kind)
                    if not previous or previous["id"] != asset_id:
                        if previous:
                            entry.setdefault("previous_assets", []).append({"kind": kind, **previous})
                        entry["assets"][kind] = {"id": asset_id, "status": "pending" if asset_id else "absent", "attempts": []}
            self.m["state"].update(next_cursor=nxt, enumeration_complete=nxt is None, pages=self.m["state"]["pages"] + 1)
            if nxt is not None:
                seen.append(sha(nxt.encode()))
            self.save()
            count += 1
        return count

    def verified(self, asset):
        if asset["status"] != "downloaded":
            return False
        for name in ("original", "json"):
            ref = asset.get(name, {})
            path = (self.out / ref.get("path", "")).resolve()
            if not path.is_relative_to(self.out.resolve()):
                raise DuelsError("Ruta local fuera del directorio de adquisición")
            if not path.is_file() or sha(path.read_bytes()) != ref.get("sha256"):
                asset["status"] = "download_failed"
                asset["error"] = {"code": "local_integrity_failed", "recoverable": True, "at": now()}
                self.save()
                return False
        return True

    def assets(self, max_games, retry_unavailable=False, game_ids=None):
        if game_ids and not set(game_ids) <= self.m["games"].keys():
            raise DuelsError("Hay game_id solicitados que no están enumerados en este manifiesto")
        selected = 0
        for entry in self.m["games"].values():
            if game_ids and entry["game_id"] not in game_ids:
                continue
            if max_games == 0 or selected >= max_games:
                break
            needs = []
            for kind, asset in entry["assets"].items():
                if self.verified(asset) or asset["status"] == "absent":
                    continue
                if asset["status"] == "unavailable" and not retry_unavailable:
                    continue
                needs.append(kind)
            if not needs:
                continue
            selected += 1
            for kind in needs:
                self.acquire(entry, kind)
        return selected

    def acquire(self, entry, kind):
        asset = entry["assets"][kind]
        attempt = {"at": now()}
        asset["attempts"].append(attempt)
        self.save()
        try:
            endpoint = "/api/me/bulk-replays" if kind == "replay" else "/api/me/bulk-gamelogs"
            value, body, headers = self.client.api(endpoint, ids=[asset["id"]])
            obs = observation(self.out, body, endpoint, {"ids": [asset["id"]]}, headers)
            self.m["observations"].append(obs)
            attempt["manifest"] = obs
            if not isinstance(value, dict) or not isinstance(value.get("files"), list) or not isinstance(value.get("missing"), list):
                raise RequestError("invalid_download_manifest")
            files = [f for f in value["files"] if isinstance(f, dict) and f.get("id") == asset["id"]]
            if not files and asset["id"] in value["missing"]:
                asset.update(status="unavailable", error={"code": "manifest_missing", "recoverable": True, "at": now()})
                attempt["status"] = "unavailable"
                return
            if len(files) != 1 or not isinstance(files[0].get("url"), str):
                raise RequestError("invalid_download_manifest")
            attempt["file"] = files[0]  # URL privada conservada solo localmente.
            self.save()
            raw, headers, chain = self.client.download(files[0]["url"])
            attempt["redirects"] = chain
            compressed = raw.startswith(b"\x1f\x8b")
            ref = original(self.out, raw, ".gz" if compressed else ".json")
            attempt["original"] = ref
            self.save()  # No perder originales aunque gzip/JSON o validación fallen.
            try:
                decoded = gzip.decompress(raw) if compressed else raw
                data = json.loads(decoded)
            except (ValueError, OSError, EOFError, UnicodeError):
                raise RequestError("invalid_gzip_or_json") from None
            json_ref = original(self.out, decoded, ".json")
            attempt["json"] = json_ref
            validation = validate_asset(kind, data, entry["row"])
            asset.update(status="downloaded", original=ref, json=json_ref, validation=validation, acquired_at=now())
            asset.pop("error", None)
            attempt["status"] = "downloaded"
        except AuthError:
            attempt["status"] = "authentication_failed"
            raise
        except RequestError as exc:
            status = "unavailable" if exc.status in (404, 410) else "download_failed"
            asset.update(status=status, error={"code": exc.code, "http_status": exc.status, "recoverable": True, "at": now()})
            attempt["status"] = status
        finally:
            self.save()


class Lock:
    """Evita dos escritores. Tras un cierre abrupto revisar y retirar .lock manualmente."""
    def __init__(self, out):
        self.path = resolver_ruta(out) / ".lock"

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        try:
            fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            raise DuelsError("Directorio bloqueado por .lock; comprueba que no hay otro proceso antes de retirarlo") from None
        with os.fdopen(fd, "w") as handle:
            handle.write(str(os.getpid()))
        return self

    def __exit__(self, *args):
        self.path.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=resolver_ruta, default=ruta_trabajo("adquisiciones/duels/sample"))
    parser.add_argument("--env-file", type=resolver_ruta, default=ROOT / ".env")
    parser.add_argument("--token-env", help="Nombre de variable, nunca su valor")
    parser.add_argument("--from", dest="from_", type=date_argument)
    parser.add_argument("--to", type=date_argument)
    parser.add_argument("--source", help="all o subconjunto separado por comas: matchmaking,private,bot")
    parser.add_argument("--queue", help="IDs separados por comas; solo limita filas matchmaking")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--max-pages", type=int, default=1, help="Páginas nuevas en esta ejecución; 0 = todas")
    parser.add_argument("--download-games", type=int, default=0, help="Máximo de partidas pendientes a descargar; 0 = ninguna")
    parser.add_argument("--retry-unavailable", action="store_true")
    parser.add_argument("--skip-history", action="store_true", help="Solo identidad/archivos de filas ya enumeradas")
    parser.add_argument("--game-id", action="append", help="Limita descargas a IDs ya enumerados; repetible")
    args = parser.parse_args(argv)
    if args.max_pages < 0 or args.download_games < 0 or (args.limit is not None and not 1 <= args.limit <= 250):
        parser.error("Límites inválidos; página entre 1 y 250; cantidades no negativas")
    if args.source and args.source != "all" and not set(args.source.split(",")) <= {"matchmaking", "private", "bot"}:
        parser.error("source no admitido")
    client = None
    try:
        with Lock(args.out):
            client = Client(load_token(args.env_file, args.token_env))
            importer = Importer(args.out, client)
            params = dict(importer.m["parameters"]) if importer.m else {"format": "json", "limit": 10, "to": now()}
            for key, value in (("from", args.from_), ("to", args.to), ("source", args.source), ("queue", args.queue), ("limit", args.limit)):
                if value is not None:
                    params[key] = value
            if params.get("from") and datetime.fromisoformat(params["from"].replace("Z", "+00:00")) >= datetime.fromisoformat(params["to"].replace("Z", "+00:00")):
                raise DuelsError("from debe ser anterior a to")
            result = importer.run(params, max_pages=args.max_pages, download_games=args.download_games,
                                  skip_history=args.skip_history, retry_unavailable=args.retry_unavailable,
                                  game_ids=args.game_id)
            print(json.dumps(result, ensure_ascii=False))
            return 2 if any(k.endswith(":download_failed") for k in result["assets"]) else 0
    except (DuelsError, KeyboardInterrupt) as exc:
        # No imprimir tracebacks ni excepciones de urllib con URLs/cabeceras.
        print(str(exc) if isinstance(exc, DuelsError) else "Interrumpido; reanuda con el mismo --out", file=sys.stderr)
        return 1
    except Exception:
        print("Error local inesperado; originales y checkpoint conservados. Revisa archivos/permisos y versión del formato.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
