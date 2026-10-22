"""Support page and its entry points (Playwright, local server).

- support.html: KakaoPay opens as a link only on phones/tablets; computers (also touchscreen laptops) get a
  non-link card with a QR code, because KakaoPay links give a 404 in desktop browsers. Empty urls show "coming soon".
- Korean browsers get Korean text and KakaoPay first; others get English and Ko-fi first.
- The header link, the bottom card and the mock exam results point to support.html.
    python3 tools/support_test.py
"""
import functools, http.server, pathlib, threading
from playwright.sync_api import sync_playwright

ROOT = str(pathlib.Path(__file__).resolve().parents[1])
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Q, directory=ROOT))
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{srv.server_address[1]}/"
ok = fail = 0
def check(name, cond, info=""):
    global ok, fail
    if cond: ok += 1
    else: fail += 1; print("FAIL", name, info)

WIN = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
IPHONE = ("Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
          "Version/18.0 Mobile/15E148 Safari/604.1")
errs = []
KAKAO = "[data-method=kakaopay]"

with sync_playwright() as p:
    b = p.chromium.launch()
    def page(locale="ko-KR", **kw):
        pg = b.new_context(locale=locale, **kw).new_page()
        pg.on("pageerror", lambda e: errs.append(str(e)))
        return pg

    for name, kw in [("desktop", dict(user_agent=WIN)), ("touch laptop", dict(user_agent=WIN, has_touch=True))]:
        pg = page(viewport={"width": 1000, "height": 800}, **kw)
        pg.goto(BASE + "support.html"); pg.wait_for_selector(KAKAO + " .qr")
        check(f"{name}: KakaoPay card is not a link", pg.eval_on_selector(KAKAO, "e => e.tagName") == "DIV")
        pg.wait_for_function(f"document.querySelector('{KAKAO} .qr').complete", timeout=5000)
        check(f"{name}: QR image loads", pg.eval_on_selector(KAKAO + " .qr", "e => e.naturalWidth > 0"))
        check(f"{name}: scan hint", "QR" in pg.inner_text(KAKAO + " .go"))

    pg = page(viewport={"width": 390, "height": 844}, user_agent=IPHONE, has_touch=True, is_mobile=True)
    pg.goto(BASE + "support.html"); pg.wait_for_selector(KAKAO)
    check("phone: KakaoPay card links to the app", (pg.eval_on_selector(KAKAO, "e => e.getAttribute('href')") or "")
          .startswith("https://qr.kakaopay.com/"))
    check("phone: QR still shown", pg.locator(KAKAO + " .qr").count() == 1)
    check("phone: no horizontal scroll", not pg.evaluate("document.documentElement.scrollWidth > innerWidth"))

    order = pg.eval_on_selector_all(".method", "els => els.map(e => e.dataset.method)")
    check("Korean: KakaoPay first", order[:1] == ["kakaopay"], order)
    check("Korean: Korean title", "후원" in pg.title())
    check("empty url shows coming soon", pg.eval_on_selector("[data-method=kofi]", "e => e.tagName") == "DIV"
          and "준비 중" in pg.inner_text("[data-method=kofi]"))

    pg = page(locale="en-US", viewport={"width": 1000, "height": 800}, user_agent=WIN)
    pg.goto(BASE + "support.html"); pg.wait_for_selector(".method")
    order = pg.eval_on_selector_all(".method", "els => els.map(e => e.dataset.method)")
    check("English: Ko-fi first", order[:1] == ["kofi"], order)
    pg.click(".lang[data-lang=ko]")
    check("language toggle switches to Korean", "후원" in pg.inner_text("h1"))

    pg.goto(BASE + "#exam=SAA-C03"); pg.wait_for_selector(".qcard")
    check("header support link", pg.get_attribute(".supportlink", "href") == "support.html"
          and pg.inner_text(".supportlink").strip() == "☕ Support this site", pg.inner_text("header.top"))
    check("bottom support card", pg.get_attribute(".supportcard a", "href") == "support.html")
    pg.click("#mockBtn"); pg.wait_for_selector(".mk h2"); pg.click('[data-mode="short"]')
    pg.click('[data-act="start"]'); pg.wait_for_selector(".mkbar")
    pg.click('[data-act="grid"]'); pg.click('[data-act="ask"]')
    pg.click('[data-act="submit"]'); pg.wait_for_selector("#mockRoot .score")
    check("mock results support line", pg.get_attribute(".mk .support a", "href") == "support.html")
    pg.goto(BASE + "study.html"); pg.wait_for_selector(".supportlink")
    check("study header support link", pg.get_attribute(".supportlink", "href") == "support.html")

    check("no page errors", not errs, errs)
    b.close()
print(f"{ok}/{ok + fail} passed")
