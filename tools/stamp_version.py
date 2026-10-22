"""Stamp content hashes so GitHub Pages caching never pairs an old script with a new page (or the reverse):
- js/mock.js  -> index.html  (const MOCK_VERSION = "...")
- js/study.js -> study.html  (<script src="js/study.js?v=...">)
Run after editing js/mock.js or js/study.js.
    python3 tools/stamp_version.py
"""
import hashlib, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]


def stamp(script, page, pattern, repl, label):
    h = hashlib.sha1((ROOT / script).read_bytes()).hexdigest()[:10]
    p = ROOT / page
    s = p.read_text(encoding="utf-8")
    s2, n = re.subn(pattern, repl(h), s)
    assert n == 1, f"{label} marker not found in {page}"
    p.write_text(s2, encoding="utf-8", newline="")
    print(label, h)


stamp("js/mock.js", "index.html", r'const MOCK_VERSION = "[^"]*";', lambda h: f'const MOCK_VERSION = "{h}";', "MOCK_VERSION")
stamp("js/study.js", "study.html", r'<script src="js/study\.js(\?v=[0-9a-f]*)?"></script>',
      lambda h: f'<script src="js/study.js?v={h}"></script>', "STUDY_VERSION")
