"""Resume after leaving the question bank by mistake (Playwright, local server).

- After a reload in the same tab the list keeps its order, answered cards show their answers again and the score
  pill keeps its count (sessionStorage, per tab).
- A "Resume" button next to Mock Exam appears when the question that was in view is off screen and jumps to it.
- Switching to another exam and back shows the earlier answers again (cards used to come back blank and locked).
- Reset clears the saved state of that list.
    python3 tools/resume_test.py
"""
import functools, http.server, pathlib, sys, threading
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

ORDER = "els => els.map(e => e.dataset.qid)"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_context(viewport={"width": 390, "height": 844}).new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.route("**/fonts.googleapis.com/**", lambda r: r.abort())
    pg.goto(BASE + "#exam=AZ-900"); pg.wait_for_selector(".qcard")
    order = pg.eval_on_selector_all("#listArea .qcard", ORDER)
    # answer the first single-answer card, then scroll well down the list
    first = pg.evaluate("[...document.querySelectorAll('#listArea .qcard')].find(c => !c.querySelector('.check-btn')).dataset.qid")
    pg.click(f"#card-{first} .choice >> nth=0")
    pg.wait_for_selector(f"#explain-{first}.show")
    target = order[30]
    pg.evaluate(f"document.getElementById('card-{target}').scrollIntoView({{block:'start'}})")
    pg.wait_for_timeout(1200)
    check("resume button hidden while the saved question is in view", pg.is_hidden("#resumeBtn"))

    pg.reload(); pg.wait_for_selector(".qcard")
    pg.evaluate("window.scrollTo(0, 0)"); pg.wait_for_timeout(900)
    check("order kept after reload", pg.eval_on_selector_all("#listArea .qcard", ORDER) == order)
    check("answered card shown again", pg.is_visible(f"#explain-{first}.show"))
    check("score kept", "1" in (pg.text_content("#scorePill") or ""), pg.text_content("#scorePill"))
    check("resume button shown", pg.is_visible("#resumeBtn"))
    check("resume button names the position", "31 /" in pg.text_content("#resumeBtn"), pg.text_content("#resumeBtn"))
    pg.click("#resumeBtn"); pg.wait_for_timeout(900)
    top = pg.evaluate(f"document.getElementById('card-{target}').getBoundingClientRect().top")
    check("resume scrolls to the saved question", 0 <= top < 200, top)

    # another exam and back: the answer is still shown and the card is not stuck
    pg.evaluate("window.scrollTo(0, 0)")
    pg.evaluate("location.hash = '#exam=AZ-104'"); pg.wait_for_timeout(1500)
    pg.evaluate("location.hash = '#exam=AZ-900'"); pg.wait_for_selector(f"#card-{first}"); pg.wait_for_timeout(500)
    check("answers survive an exam switch", pg.is_visible(f"#explain-{first}.show"))
    check("try again still works", pg.is_visible(f"#card-{first} .retry-btn"))

    # reset clears this list's saved state
    pg.click(".resetScoreBtn"); pg.wait_for_timeout(500)
    pg.reload(); pg.wait_for_selector(".qcard"); pg.wait_for_timeout(500)
    check("reset clears the answers", not pg.is_visible(f"#explain-{first}.show"))
    check("no page errors", not errs, errs)
    b.close()

print(f"{ok}/{ok + fail} passed")
sys.exit(1 if fail else 0)
