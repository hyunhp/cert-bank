#!/usr/bin/env python3
"""Static site pages (tools/site/build.py): up to date with the data, crawlable without JavaScript, links resolve,
sitemap lists only indexable pages, tool screens carry noindex, pages fit a phone."""
import html.parser, os, pathlib, re, subprocess, sys, urllib.parse
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(__file__))
from testkit import serve, Checker

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE_URL = "https://hyunhp.github.io/cert-bank/"
C = Checker()

r = subprocess.run([sys.executable, str(ROOT / "tools" / "site" / "build.py"), "--check"], capture_output=True, text=True)
C.check("generated pages are up to date (run python3 tools/site/build.py)", r.returncode == 0, r.stdout + r.stderr)


class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.links, self.scripts, self.meta, self.canon, self.h1 = [], 0, {}, None, 0
    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag == "a" and a.get("href"): self.links.append(a["href"])
        if tag == "link" and a.get("rel") == "stylesheet": self.links.append(a["href"])
        if tag == "link" and a.get("rel") == "canonical": self.canon = a["href"]
        if tag == "script": self.scripts += 1
        if tag == "meta" and a.get("name"): self.meta[a["name"]] = a.get("content", "")
        if tag == "h1": self.h1 += 1


sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
urls = re.findall(r"<loc>([^<]+)</loc>", sm)
C.check("sitemap has home, exam list, every hub, about, contact and privacy", len(urls) >= 49 and len(urls) == len(set(urls)), len(urls))
pages = []
for u in urls:
    rel = u[len(BASE_URL):] if u.startswith(BASE_URL) else None
    f = ROOT / (rel + "index.html" if rel == "" or rel.endswith("/") else rel) if rel is not None else None
    if not f or not f.exists():
        C.check(f"sitemap url has a file: {u}", False); continue
    pages.append((rel, f))
C.check("every sitemap url is under the site and has a file", len(pages) == len(urls))

bad_links, no_canon, scripted, noindexed, desc = [], [], [], [], []
for rel, f in pages:
    p = Links(); p.feed(f.read_text(encoding="utf-8"))
    if p.canon != BASE_URL + rel: no_canon.append(rel)
    if p.scripts and rel: scripted.append(rel)   # the home page is the question bank (JS), its intro is static
    if "noindex" in p.meta.get("robots", ""): noindexed.append(rel)
    if not (50 <= len(p.meta.get("description", "")) <= 300) or p.h1 != 1: desc.append(rel)
    for h in p.links:
        if re.match(r"^(https?:|mailto:)", h): continue
        target = urllib.parse.urlsplit(urllib.parse.urljoin("/x/" + rel, h)).path   # resolve relative to the page
        target = (ROOT / target.lstrip("/")[2:]) if target.startswith("/x/") else None
        if target is None: bad_links.append((rel, h)); continue
        if target.is_dir() or str(target).endswith("/"): target = target / "index.html"
        if not target.exists(): bad_links.append((rel, h))
C.check("each page's canonical is its own sitemap url", not no_canon, no_canon[:5])
C.check("generated pages need no JavaScript (no <script>)", not scripted, scripted[:5])
C.check("indexable pages carry no noindex", not noindexed, noindexed)
C.check("each page has one h1 and a description of 50-300 chars", not desc, desc[:5])
C.check("every local link and stylesheet resolves", not bad_links, bad_links[:8])
C.check("study screens are noindex", 'name="robots" content="noindex"' in (ROOT / "study.html").read_text(encoding="utf-8"))
C.check("tool pages are not in the sitemap", not any(u.endswith(("study.html", "support.html")) for u in urls))
C.check("home page is in the sitemap", BASE_URL in urls)
con = (ROOT / "contact.html").read_text(encoding="utf-8")
C.check("contact page gives the e-mail address", 'href="mailto:koreanxpodcast@gmail.com"' in con)

hub = (ROOT / "exams" / "saa-c03" / "index.html").read_text(encoding="utf-8")
C.check("hub has weights, briefs, study order and tool links",
        all(s in hub for s in ("30%", "What to watch for", "A study order that works", "#mock=SAA-C03", "study.html#exam=SAA-C03")))
ret = (ROOT / "exams" / "sap-c02" / "index.html").read_text(encoding="utf-8")
C.check("retiring exam names its last day and its replacement", "2026-11-16" in ret and 'href="../sap-c03/"' in ret)
C.check("index.html footer links the exam pages", 'href="exams/"' in (ROOT / "index.html").read_text(encoding="utf-8"))

srv, BASE = serve(str(ROOT))
with sync_playwright() as pw:
    b = pw.chromium.launch()
    for scheme in ("light", "dark"):
        c = b.new_context(java_script_enabled=False, viewport={"width": 375, "height": 800}, color_scheme=scheme)
        q = c.new_page()
        for path in ("exams/", "exams/saa-c03/", "exams/pltr-aware/", "about.html", "contact.html", "privacy.html"):
            q.goto(BASE + path)
            w = q.evaluate("document.documentElement.scrollWidth")
            C.check(f"[{scheme}] {path}: readable without JS, no horizontal scroll on a phone", w <= 375 and q.inner_text("h1"), w)
        q.goto(BASE)
        C.check(f"[{scheme}] home: static intro links the exam pages without JS", q.locator('header.top p.intro a[href="exams/#aws"]').is_visible())
        q.goto(BASE + "privacy.html")
        bg = q.evaluate("getComputedStyle(document.body).backgroundColor")
        C.check(f"[{scheme}] page background follows the color scheme", (bg == "rgb(16, 21, 28)") == (scheme == "dark"), bg)
        c.close()
    b.close()
sys.exit(C.exit())
