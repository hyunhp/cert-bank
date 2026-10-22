"""Study guide page (study.html) and its data (Playwright, local server).

- Every data/study/<EXAM>.json is well formed: days numbered 1..n, domains are the exam's D-codes
  (or null for the final review day), two quiz questions with a valid answer index.
- #exam=X&day=N opens that day; prev/next and the day list move between days; the last day opened
  is remembered per exam; "Mark as studied" persists across reloads.
- The quiz marks right/wrong answers and shows the explanation; the practice link filters the
  question bank to the day's domain. No horizontal overflow on a phone-sized viewport.
    python3 tools/study_test.py
"""
import functools, http.server, json, pathlib, threading
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

specs = json.load(open(pathlib.Path(ROOT, "data", "exam-specs.json"), encoding="utf-8"))
idx = json.load(open(pathlib.Path(ROOT, "data", "exams-index.json"), encoding="utf-8"))
files = sorted(pathlib.Path(ROOT, "data", "study").glob("*.json"))
check("12 study guides", len(files) == 12, [f.stem for f in files])
check("index lists every guide", sorted(idx.get("study", {})) == [f.stem for f in files])
for f in files:
    g = json.load(open(f, encoding="utf-8"))
    codes = {d["code"] for d in specs[f.stem]["domains"]}
    days = g["days"]
    check(f"{f.stem} days numbered", [d["day"] for d in days] == list(range(1, len(days) + 1)))
    check(f"{f.stem} domains", all(d["domain"] in codes for d in days[:-1]) and days[-1]["domain"] is None)
    check(f"{f.stem} quiz", all(len(d["quiz"]) == 2 and all(0 <= q["answer"] < len(q["choices"]) for q in d["quiz"]) for d in days))
    check(f"{f.stem} content", all(d["title"] and d["concepts"] and d["examPoints"] and d["recap"] for d in days))
saa = json.load(open(pathlib.Path(ROOT, "data", "study", "SAA-C03.json"), encoding="utf-8"))

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_context(viewport={"width": 390, "height": 844}).new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.route("**/fonts.googleapis.com/**", lambda r: r.abort())

    pg.goto(BASE + "study.html"); pg.wait_for_selector("#examRow .chip")
    check("exam chips", pg.locator("#examRow .chip").count() == 12)
    check("empty state before picking", "Pick an exam" in pg.inner_text("#main"))

    pg.goto(BASE + "study.html#exam=SAA-C03&day=3"); pg.reload(); pg.wait_for_selector(".daytitle")
    check("deep link opens day 3", pg.inner_text(".daytitle") == saa["days"][2]["title"])
    check("domain badge", pg.inner_text(".eyebrow .dbadge") == saa["days"][2]["domain"])
    check("concepts rendered", pg.locator(".concept").count() == len(saa["days"][2]["concepts"]))
    href = pg.get_attribute(".qblink", "href")
    check("practice link filters domain", href == f"./#exam=SAA-C03&d={saa['days'][2]['domain']}", href)

    pg.click("#nextBtn"); pg.wait_for_function("location.hash.endsWith('day=4')")
    pg.wait_for_function(f"document.querySelector('.daytitle').textContent === {json.dumps(saa['days'][3]['title'])}")
    check("next goes to day 4", True)
    pg.click("#prevBtn"); pg.wait_for_function("location.hash.endsWith('day=3')")

    q = saa["days"][2]["quiz"][0]
    wrong = (q["answer"] + 1) % len(q["choices"])
    first = pg.locator(".quiz-q").first
    first.locator(".choice").nth(wrong).click()
    check("wrong pick marked", "incorrect" in (first.locator(".choice").nth(wrong).get_attribute("class") or ""))
    check("right answer shown", "correct" in (first.locator(".choice").nth(q["answer"]).get_attribute("class") or "").split())
    check("explanation shown", q["explain"][:40] in first.inner_text())
    first.locator(".retry").click()
    check("retry resets", first.locator(".choice:disabled").count() == 0)

    pg.click("#doneBtn")
    check("marked studied", pg.get_attribute("#doneBtn", "aria-pressed") == "true")
    pg.click("#dayNav summary")
    check("day list shows tick", pg.locator(".daylink[data-day='3'] .ck").count() == 1)
    groups = pg.eval_on_selector_all(".daygroup h3", "els => els.map(e => e.textContent)")
    check("day list grouped by domain", groups[0].startswith("D1 ·") and groups[-1] == "Final review", groups)
    pg.click(".daylink[data-day='10']")
    pg.wait_for_function("document.querySelector('.eyebrow').textContent.includes('Day 10 /')")
    check("day list jumps", pg.locator("#dayNav").get_attribute("open") is None)

    pg.goto(BASE + "study.html#exam=DEA-C01"); pg.wait_for_selector(".daytitle")
    check("other exam starts at day 1", pg.evaluate("location.hash") == "#exam=DEA-C01&day=1")
    pg.goto(BASE + "study.html#exam=SAA-C03"); pg.reload(); pg.wait_for_selector(".daytitle")
    check("last day remembered", pg.evaluate("location.hash") == "#exam=SAA-C03&day=10", pg.evaluate("location.hash"))
    pg.goto(BASE + "study.html#exam=SAA-C03&day=3"); pg.reload(); pg.wait_for_selector(".daytitle")
    check("studied persists", pg.get_attribute("#doneBtn", "aria-pressed") == "true")
    pg.goto(BASE + "study.html#exam=SAA-C03&day=999"); pg.reload(); pg.wait_for_selector(".daytitle")
    check("day clamps to last", pg.evaluate("location.hash") == f"#exam=SAA-C03&day={len(saa['days'])}")
    check("final day links whole exam", pg.get_attribute(".qblink", "href") == "./#exam=SAA-C03")

    for code in ["SAP-C02", "AIF-C01"]:
        pg.goto(BASE + f"study.html#exam={code}&day=1"); pg.wait_for_selector(".daytitle")
        check(f"{code} no horizontal overflow", pg.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"))

    pg.goto(BASE); pg.wait_for_selector(".qcard")
    check("question bank links to study guide", pg.get_attribute(".studylink", "href") == "study.html")
    check("no page errors", not errs, errs)
    b.close()
print(f"{ok}/{ok + fail} passed")
