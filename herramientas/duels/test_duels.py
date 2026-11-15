"""Pruebas sin red ni credenciales reales: python -m unittest discover -s herramientas/duels."""
import copy
import contextlib
import gzip
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

import duels as d


def row(game="g1", replay="r1", deck=None):
    return {"game_id": game, "your_user_id": "u1", "match_id": "m1", "match_game_number": 1,
            "your_player": 2, "replay_id": replay, "your_deck_id": "deck1",
            "your_decklist": deck if deck is not None else [{"cardId": "14-1", "count": 4}]}


def replay(game="g1"):
    return {"format": "duels-replay-v1", "gameId": game, "perspective": 2,
            "baseSnapshot": {"viewingAs": 2}, "frames": [], "logs": []}


class FakeAPI:
    def __init__(self, pages=()):
        self.pages = list(pages)
        self.calls = []
        self.downloads = []
        self.manifest_missing = False
        self.download_error = None
        self.requests = 0

    def api(self, path, params=None, ids=None):
        self.requests += 1
        self.calls.append((path, copy.deepcopy(params), ids))
        if path == "/api/me":
            value = {"id": "u1", "name": "example", "token": None}
        elif path == "/api/me/match-history":
            value = self.pages.pop(0)
            if isinstance(value, Exception):
                raise value
        else:
            value = {"files": [] if self.manifest_missing else [{"id": ids[0], "filename": "../../bad.gz", "url": "https://cdn.duels.ink/example"}],
                     "missing": ids if self.manifest_missing else []}
        return value, d.encode(value), {}

    def download(self, url):
        self.requests += 1
        self.downloads.append(url)
        if self.download_error:
            raise self.download_error
        return gzip.compress(d.encode(replay()), mtime=0), {}, [{"url": url, "status": 200}]


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.out = Path(self.tmp.name)
        self.params = {"format": "json", "limit": 2, "from": "2026-01-01T00:00:00.000Z", "to": "2026-10-15T00:00:00.000Z"}

    def make(self, pages):
        api = FakeAPI(pages)
        importer = d.Importer(self.out, api)
        importer.identity(self.params)
        return importer, api

    def test_pagination_resume_and_historical_rows(self):
        cursor = "opaque + / | ? = &"
        first = row()
        second = row(deck=[{"cardId": "1-1", "count": 2}])
        imp, api = self.make([{"games": [first], "next_cursor": cursor}, d.RequestError("network_failed")])
        imp.enumerate(1)
        with self.assertRaises(d.RequestError):
            imp.enumerate(1)
        resumed = d.Importer(self.out, FakeAPI([{"games": [second, row("g2", None)], "next_cursor": None}]))
        resumed.identity(self.params)
        resumed.enumerate(0)
        self.assertEqual(resumed.client.calls[-1][1]["cursor"], cursor)
        self.assertEqual(len(resumed.m["games"]), 2)
        self.assertEqual(len(resumed.m["games"]["g1"]["row_versions"]), 2)
        old = resumed.m["games"]["g1"]["row_versions"][0]
        original = json.loads((self.out / old["file"]["path"]).read_bytes())
        self.assertEqual(original["games"][old["index"]]["your_decklist"], first["your_decklist"])
        self.assertTrue(resumed.m["state"]["enumeration_complete"])
        self.assertEqual(resumed.m["games"]["g2"]["assets"]["replay"]["status"], "absent")
        self.assertEqual(resumed.enumerate(0), 0)

    def test_page_validation_does_not_advance_checkpoint(self):
        bad = row("other")
        bad["your_user_id"] = "different"
        imp, _ = self.make([{"games": [row(), bad], "next_cursor": "opaque"}])
        with self.assertRaises(d.RequestError):
            imp.enumerate(1)
        self.assertEqual(imp.m["state"]["pages"], 0)
        self.assertEqual(imp.m["games"], {})
        self.assertTrue((self.out / imp.m["observations"][-1]["file"]["path"]).exists())

    def test_cursor_cycle_rejected(self):
        imp, _ = self.make([{"games": [row()], "next_cursor": "A"},
                            {"games": [row()], "next_cursor": "B"},
                            {"games": [row()], "next_cursor": "A"}])
        with self.assertRaises(d.RequestError):
            imp.enumerate(0)
        self.assertEqual(imp.m["state"]["next_cursor"], "B")
        self.assertEqual(imp.m["state"]["pages"], 2)

    def test_second_run_skips_verified_files_and_preserves_gzip(self):
        imp, api = self.make([{"games": [row()], "next_cursor": None}])
        imp.enumerate(1)
        imp.assets(1)
        self.assertEqual(len(api.downloads), 2)
        asset = imp.m["games"]["g1"]["assets"]["replay"]
        raw = (self.out / asset["original"]["path"]).read_bytes()
        self.assertEqual(d.sha(raw), asset["original"]["sha256"])
        self.assertEqual(gzip.decompress(raw), (self.out / asset["json"]["path"]).read_bytes())
        resumed = d.Importer(self.out, api)
        before = len(api.calls)
        self.assertEqual(resumed.assets(1), 0)
        self.assertEqual(len(api.calls), before)
        self.assertEqual(len(api.downloads), 2)
        self.assertFalse((self.out.parent / "bad.gz").exists())

    def test_corrupt_local_file_is_detected_and_preserved(self):
        imp, api = self.make([{"games": [row()], "next_cursor": None}])
        imp.enumerate(1)
        imp.assets(1)
        asset = imp.m["games"]["g1"]["assets"]["replay"]
        path = self.out / asset["original"]["path"]
        path.write_bytes(b"corrupt")
        imp.assets(1)
        self.assertEqual(path.read_bytes(), b"corrupt")
        self.assertEqual(asset["status"], "downloaded")
        self.assertNotEqual(self.out / asset["original"]["path"], path)

    def test_missing_unavailable_download_failed_and_retry(self):
        imp, api = self.make([{"games": [row()], "next_cursor": None}])
        imp.enumerate(1)
        api.manifest_missing = True
        imp.assets(1)
        self.assertEqual(imp.m["games"]["g1"]["assets"]["replay"]["error"]["code"], "manifest_missing")
        before = len(api.calls)
        imp.assets(1)
        self.assertEqual(len(api.calls), before)
        api.manifest_missing = False
        api.download_error = d.RequestError("http_failed", 410)
        imp.assets(1, True)
        self.assertEqual(imp.m["games"]["g1"]["assets"]["replay"]["status"], "unavailable")
        api.download_error = d.RequestError("network_failed")
        imp.assets(1, True)
        self.assertEqual(imp.m["games"]["g1"]["assets"]["replay"]["status"], "download_failed")
        api.download_error = None
        imp.assets(1)
        self.assertEqual(imp.m["games"]["g1"]["assets"]["replay"]["status"], "downloaded")

    def test_wrong_replay_keeps_original_and_fails(self):
        imp, api = self.make([{"games": [row("g2")], "next_cursor": None}])
        imp.enumerate(1)
        imp.assets(1)
        a = imp.m["games"]["g2"]["assets"]["replay"]
        self.assertEqual(a["status"], "download_failed")
        self.assertTrue((self.out / a["attempts"][0]["original"]["path"]).exists())

    def test_account_and_parameter_mixing_denied(self):
        imp, _ = self.make([])
        with self.assertRaises(d.DuelsError):
            imp.identity({**self.params, "limit": 100})
        imp.m["account"]["id"] = "another"
        with self.assertRaises(d.DuelsError):
            imp.identity(self.params)

    def test_writer_lock_and_atomic_save(self):
        with d.Lock(self.out):
            with self.assertRaises(d.DuelsError):
                with d.Lock(self.out):
                    pass
        self.assertFalse((self.out / ".lock").exists())
        d.atomic(self.out / "a", b"first")
        d.atomic(self.out / "a", b"second")
        self.assertEqual((self.out / "a").read_bytes(), b"second")

    def test_run_records_auth_failure_without_advancing_cursor(self):
        imp, api = self.make([d.AuthError("HTTP 401")])
        with d.Lock(self.out), self.assertRaises(d.AuthError):
            imp.run(self.params)
        saved = json.loads((self.out / "manifest.json").read_bytes())
        self.assertEqual(saved["errors"][-1]["code"], "authentication_failed")
        self.assertFalse(saved["errors"][-1]["recoverable"])
        self.assertEqual(saved["state"]["pages"], 0)
        self.assertFalse((self.out / ".lock").exists())

    def test_cli_end_to_end_and_resume_with_mocked_http(self):
        env = self.out / ".env"
        env.write_text("DUELS_TOKEN=" + "a" * 96, encoding="utf-8")
        first = FakeAPI([{"games": [row()], "next_cursor": None}])
        buf = io.StringIO()
        args = ["--out", str(self.out), "--env-file", str(env), "--limit", "2", "--download-games", "1"]
        with patch.object(d, "Client", return_value=first), patch.dict(os.environ, {}, clear=True), contextlib.redirect_stdout(buf):
            self.assertEqual(d.main(args), 0)
        self.assertEqual(json.loads(buf.getvalue())["http_requests"], 6)
        buf = io.StringIO()
        second = FakeAPI()
        with patch.object(d, "Client", return_value=second), patch.dict(os.environ, {}, clear=True), contextlib.redirect_stdout(buf):
            self.assertEqual(d.main(args + ["--skip-history"]), 0)
        self.assertEqual(json.loads(buf.getvalue())["http_requests"], 1)
        self.assertFalse(second.downloads)

    def test_invalid_cli_date_is_reported_without_traceback(self):
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf), self.assertRaises(SystemExit) as ctx:
            d.main(["--from", "2026-01-01"])
        self.assertEqual(ctx.exception.code, 2)
        self.assertNotIn("Traceback", buf.getvalue())


class Reply:
    def __init__(self, body=b"{}", headers=None):
        self.body, self.headers, self.status = body, headers or {}, 200
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self): return self.body


class QueueOpener:
    def __init__(self, replies):
        self.replies, self.requests = list(replies), []
    def open(self, req, timeout):
        self.requests.append(req)
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return reply


def http(status, headers=None, body=b"{}"):
    return urllib.error.HTTPError("https://duels.ink/private", status, "error", headers or {}, io.BytesIO(body))


class ClientTests(unittest.TestCase):
    def client(self, replies, retries=3):
        times = [100.0]
        waits = []
        def sleep(s):
            times[0] += s
            waits.append(s)
        opener = QueueOpener(replies)
        return d.Client("a" * 96, opener=opener, sleep=sleep, clock=lambda: times[0], retries=retries), opener, waits

    def test_no_authorization_on_cdn_or_return_redirect(self):
        c, o, _ = self.client([http(302, {"Location": "https://cdn.duels.ink/file"}),
                                http(302, {"Location": "https://duels.ink/r/x"}), Reply()])
        c.download("https://duels.ink/r/x")
        self.assertIn("Authorization", o.requests[0].headers)
        self.assertNotIn("Authorization", o.requests[1].headers)
        self.assertNotIn("Authorization", o.requests[2].headers)

    def test_external_initial_download_and_https_only(self):
        c, o, _ = self.client([Reply()])
        c.download("https://cdn.duels.ink/file")
        self.assertNotIn("Authorization", o.requests[0].headers)
        for url in ("http://cdn.duels.ink/file", "file:///a", "https://user:pass@duels.ink/r/x"):
            with self.assertRaises(d.RequestError):
                c.download(url)

    def test_401_never_retries_or_leaks_body(self):
        c, o, _ = self.client([http(401, body=b"sensitive url and token")])
        with self.assertRaises(d.AuthError) as ctx:
            c.api("/api/me")
        self.assertEqual(len(o.requests), 1)
        self.assertNotIn("sensitive", str(ctx.exception))

    def test_retry_after_and_rate_remaining_zero(self):
        c, o, waits = self.client([http(429, {"Retry-After": "7"}),
                                   Reply(headers={"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "170"}), Reply()])
        c.api("/api/me")
        c.api("/api/me")
        self.assertGreaterEqual(sum(waits), 71)
        self.assertIn(7, waits)
        self.assertTrue(all(x <= 30 for x in waits))

    def test_retry_body_and_bounded_5xx(self):
        c, o, waits = self.client([http(429, body=b'{"retryAfterSeconds":8}'), Reply()])
        c.api("/api/me")
        self.assertIn(8, waits)
        c, o, _ = self.client([http(503), http(503)], retries=1)
        with self.assertRaises(d.RequestError):
            c.api("/api/me")
        self.assertEqual(len(o.requests), 2)

    def test_cursor_encoded_verbatim_and_write_route_denied(self):
        c, o, _ = self.client([Reply()])
        cursor = "opaque+ /|?&="
        c.api("/api/me/match-history", {"cursor": cursor})
        query = d.urllib.parse.parse_qs(d.urllib.parse.urlsplit(o.requests[0].full_url).query)
        self.assertEqual(query["cursor"], [cursor])
        with self.assertRaises(d.RequestError):
            c.api("/api/table/create", ids=[])
        with self.assertRaises(d.RequestError):
            c.request("https://elsewhere.example/api/me", authenticated=True)

    def test_utc_and_nonexecuting_dotenv_and_env_precedence(self):
        self.assertEqual(d.utc("2026-10-15T02:00:00+02:00"), "2026-10-15T00:00:00.000Z")
        self.assertEqual(d.utc("2026-10-15T02:00:00.123456+02:00"), "2026-10-15T00:00:00.123456Z")
        with self.assertRaises(d.DuelsError):
            d.utc("2026-10-15")
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {}, clear=True):
            path = Path(tmp) / ".env"
            path.write_text("# local\nduels-token='" + "a"*96 + "' # comment\n", encoding="utf-8")
            self.assertEqual(d.load_token(path), "a" * 96)
            os.environ["DUELS_API_TOKEN"] = "b" * 96
            self.assertEqual(d.load_token(path), "b" * 96)
            os.environ.clear()
            path.write_text("DUELS_TOKEN=$(do-not-execute)\n", encoding="utf-8")
            with self.assertRaises(d.AuthError) as ctx:
                d.load_token(path)
            self.assertNotIn("do-not-execute", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
