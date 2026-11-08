"""Shared test helpers: a quiet local static server and a pass/fail counter."""
import functools, http.server, threading


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


class _Server(http.server.ThreadingHTTPServer):
    daemon_threads = True

    def handle_error(self, request, client_address):   # a browser aborting a request is not a test failure
        pass


def serve(root):
    """Serve `root` on 127.0.0.1 (free port, daemon thread). Returns (server, base_url with trailing slash)."""
    srv = _Server(("127.0.0.1", 0), functools.partial(_Quiet, directory=str(root)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}/"


class Checker:
    """check(name, cond, detail): counts results. Default prints only failures ("FAIL name detail");
    verbose=True also prints "PASS name" and shows detail as "  [detail]" on failure."""

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.ok = self.fail = 0

    def check(self, name, cond, detail=""):
        if cond:
            self.ok += 1
            if self.verbose: print("PASS " + name)
        else:
            self.fail += 1
            print(("FAIL " + name + (f"  [{detail}]" if detail else "")) if self.verbose else f"FAIL {name} {detail}")
        return bool(cond)

    __call__ = check

    def exit(self):
        """Print "ok/total passed"; return 1 on any failure else 0 (use sys.exit(c.exit()))."""
        print(f"{self.ok}/{self.ok + self.fail} passed")
        return 1 if self.fail else 0
