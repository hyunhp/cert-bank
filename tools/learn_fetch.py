"""Shared cache of documentation pages (learn.microsoft.com, docs.aws.amazon.com, ...) for question writers and reviewers.

A page is downloaded once, reduced to its main article as plain text (headings as #, list items as -, tables as
| cells), and stored in a cache folder that every agent of the machine shares. Later calls read the cached copy,
so a reviewer checking a writer's sources costs no new download, and --grep shows only the lines that matter
instead of the whole page.

    python3 tools/learn_fetch.py <url> [<url> ...]              # fetch (or reuse) and print path, size, title
    python3 tools/learn_fetch.py --grep "retire|preview" <url>   # matching lines with 2 lines of context
    python3 tools/learn_fetch.py --grep "quota" -C 5 <url>       # more context
    python3 tools/learn_fetch.py --show <url>                    # whole cached text
    python3 tools/learn_fetch.py --refresh <url>                 # download again (page changed)
    python3 tools/learn_fetch.py --list                          # cached pages with their fetch dates

Cache folder: $DOCS_CACHE, else ~/.cache/cert-bank-docs. Uses the HTTPS proxy and CA bundle of the environment
(HTTPS_PROXY, SSL_CERT_FILE / REQUESTS_CA_BUNDLE, or /root/.ccr/ca-bundle.crt when present).
"""
import datetime, hashlib, html.parser, os, pathlib, re, ssl, sys, urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # Windows consoles default to cp949

CACHE = pathlib.Path(os.environ.get("DOCS_CACHE") or pathlib.Path.home() / ".cache" / "cert-bank-docs")
SKIP = {"script", "style", "nav", "header", "footer", "aside", "noscript", "svg", "form", "button"}
BLOCK = {"p", "div", "section", "article", "br", "tr", "pre", "blockquote", "dd", "dt", "table", "ol", "ul"}


VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Text(html.parser.HTMLParser):
    """Collects the page text twice: everything, and only what is inside <main> (used when the page has one)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.all, self.main = [], []
        self.stack = []                   # (tag, starts_skip) for every open non-void element
        self.skip, self.in_main, self.pre = 0, 0, 0
        self.title, self.in_title, self.meta = "", False, {}

    def emit(self, piece):
        self.all.append(piece)
        if self.in_main:
            self.main.append(piece)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta" and a.get("name") in ("updated_at", "ms.date"):
            self.meta[a["name"]] = a.get("content", "")
        if tag == "title":
            self.in_title = True
        if tag in VOID:
            if tag == "br" and not self.skip:
                self.emit("\n")
            return
        hidden = tag in SKIP or "hidden" in a or "visually-hidden" in (a.get("class") or "")
        self.stack.append((tag, hidden))
        if hidden:
            self.skip += 1
            return
        if tag == "main":
            self.in_main += 1
        if self.skip:
            return
        if tag == "pre":
            self.pre += 1
        if re.fullmatch(r"h[1-6]", tag):
            self.emit("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.emit("\n- ")
        elif tag in ("td", "th"):
            self.emit(" | ")
        elif tag in BLOCK:
            self.emit("\n")
        elif tag == "code" and not self.pre:
            self.emit("`")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag in VOID or not any(t == tag for t, _ in self.stack):
            return                        # stray end tag
        while self.stack:                 # close implicitly-closed children too
            t, hidden = self.stack.pop()
            if hidden:
                self.skip -= 1
            elif t == "main":
                self.in_main -= 1
            elif not self.skip:
                if t == "pre":
                    self.pre = max(0, self.pre - 1)
                    self.emit("\n")
                elif t == "code" and not self.pre:
                    self.emit("`")
                elif re.fullmatch(r"h[1-6]", t) or t in BLOCK:
                    self.emit("\n")
            if t == tag:
                break

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if not self.skip:
            self.emit(data if self.pre else re.sub(r"\s+", " ", data))


def to_text(raw):
    p = Text()
    p.feed(raw)
    text = "".join(p.main) if "".join(p.main).strip() else "".join(p.all)
    text = "\n".join(line.strip() if not line.startswith("    ") else line.rstrip() for line in text.splitlines())
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return re.sub(r"\s+", " ", p.title).strip(), p.meta, text


def cache_path(url):
    u = re.sub(r"^https?://", "", url.split("#")[0])
    slug = re.sub(r"[^A-Za-z0-9]+", "-", u).strip("-")[-90:]
    return CACHE / f"{slug}-{hashlib.sha1(url.encode()).hexdigest()[:8]}.txt"


def ssl_context():
    for f in (os.environ.get("SSL_CERT_FILE"), os.environ.get("REQUESTS_CA_BUNDLE"), "/root/.ccr/ca-bundle.crt"):
        if f and os.path.exists(f):
            return ssl.create_default_context(cafile=f)
    return ssl.create_default_context()


def fetch(url, refresh=False):
    path = cache_path(url)
    if path.exists() and not refresh:
        return path, False
    req = urllib.request.Request(url, headers={"User-Agent": "cert-bank-docs-cache/1.0"})
    with urllib.request.urlopen(req, timeout=60, context=ssl_context()) as r:
        raw = r.read().decode(r.headers.get_content_charset() or "utf-8", errors="replace")
    title, meta, text = to_text(raw)
    head = [f"URL: {url}", f"Title: {title}", f"Fetched: {datetime.date.today().isoformat()}"]
    if meta.get("updated_at") or meta.get("ms.date"):
        head.append(f"Page updated: {meta.get('updated_at') or meta.get('ms.date')}")
    CACHE.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text("\n".join(head) + "\n\n" + text + "\n", encoding="utf-8")
    tmp.replace(path)                     # atomic: parallel agents never read a half-written page
    return path, True


def grep(path, pattern, ctx):
    lines = path.read_text(encoding="utf-8").splitlines()
    rx = re.compile(pattern, re.I)
    hits = [i for i, l in enumerate(lines) if rx.search(l)]
    shown = set()
    for i in hits:
        lo, hi = max(0, i - ctx), min(len(lines), i + ctx + 1)
        if shown and lo > max(shown) + 1:
            print("  --")
        for j in range(lo, hi):
            if j not in shown:
                print(f"  {j + 1:4}{'>' if j == i else ':'} {lines[j]}")
                shown.add(j)
    return len(hits)


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "--list":
        for f in sorted(CACHE.glob("*.txt")):
            head = f.read_text(encoding="utf-8").splitlines()[:3]
            print(f"{head[2][9:] if len(head) > 2 else '?':10}  {head[0][5:] if head else f.name}")
        return 0
    refresh = "--refresh" in argv
    show = "--show" in argv
    pattern, ctx, urls, it = None, 2, [], iter(argv)
    for a in it:
        if a == "--grep":
            pattern = next(it)
        elif a == "-C":
            ctx = int(next(it))
        elif not a.startswith("--"):
            urls.append(a)
    status = 0
    for url in urls:
        try:
            path, new = fetch(url, refresh)
        except Exception as e:            # report and go on with the other pages
            print(f"FAILED {url}: {e}")
            status = 1
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        print(f"{'fetched' if new else 'cached '} {path}  ({len(lines)} lines)  {lines[1] if len(lines) > 1 else ''}")
        if pattern:
            n = grep(path, pattern, ctx)
            print(f"  {n} matching line(s) for /{pattern}/")
        elif show:
            print("\n".join(lines))
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
