"""Study guide page (study.html) and its data (Playwright, local server).

- Every data/study/<EXAM>.json is well formed: days numbered 1..n, domains are the exam's D-codes
  (or null for the final review day), two quiz questions with a valid answer index.
- #exam=X&day=N opens that day; prev/next and the day list move between days; the last day opened
  is remembered per exam; "Mark as studied" persists across reloads.
- The quiz marks right/wrong answers and shows the explanation; the practice link filters the
  question bank to the day's domain. No horizontal overflow on a phone-sized viewport.
    python3 tools/study_test.py
"""
import functools, hashlib, http.server, json, pathlib, threading
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
check("study guides present", len(files) >= 12, [f.stem for f in files])
check("index lists every guide", sorted(idx.get("study", {})) == [f.stem for f in files])
for f in files:
    g = json.load(open(f, encoding="utf-8"))
    codes = {d["code"] for d in (specs[f.stem]["domains"] if f.stem in specs else g["domains"])}
    days = g["days"]
    check(f"{f.stem} days numbered", [d["day"] for d in days] == list(range(1, len(days) + 1)))
    check(f"{f.stem} domains", all(d["domain"] in codes for d in days[:-1]) and days[-1]["domain"] is None)
    check(f"{f.stem} quiz", all(len(d["quiz"]) == 2 and all(0 <= q["answer"] < len(q["choices"]) for q in d["quiz"]) for d in days))
    check(f"{f.stem} content", all(d["title"] and d["concepts"] and d["examPoints"] and d["recap"] for d in days))
saa = json.load(open(pathlib.Path(ROOT, "data", "study", "SAA-C03.json"), encoding="utf-8"))

# Glossary: unique ids, short definitions, every match form really appears (outside quiz text)
# in each listed exam, and no form belongs to two terms in the same exam.
import re
gloss = json.load(open(pathlib.Path(ROOT, "data", "glossary.json"), encoding="utf-8"))["terms"]
marked = {f.stem: "\n".join([c["body"] for d in json.load(open(f, encoding="utf-8"))["days"] for c in d["concepts"]] +
                            [p for d in json.load(open(f, encoding="utf-8"))["days"] for p in d["examPoints"] + [d["recap"]]])
          for f in files}
def occurs(m, exam): return re.search(r"(?<![\w-])" + re.escape(m) + r"(?![\w-])", marked[exam]) is not None
check("glossary ids unique", len({t["id"] for t in gloss}) == len(gloss))
check("glossary fields", all(t["term"] and t["match"] and t["en"] and t["ko"] and t["exams"] for t in gloss))
check("glossary en short", all(len(t["en"].split()) <= 45 for t in gloss), [t["term"] for t in gloss if len(t["en"].split()) > 45])
check("glossary ko short", all(len(t["ko"]) <= 120 for t in gloss), [t["term"] for t in gloss if len(t["ko"]) > 120])
check("glossary exams appear", all(any(occurs(m, e) for m in t["match"]) for t in gloss for e in t["exams"]),
      [(t["term"], e) for t in gloss for e in t["exams"] if not any(occurs(m, e) for m in t["match"])])
owner = {}
for t in gloss:
    for e in t["exams"]:
        for m in t["match"]:
            check(f"glossary form '{m}' has one owner in {e}", owner.setdefault((e, m), t["id"]) == t["id"])
per_exam = {e: sum(e in t["exams"] for t in gloss) for e in marked}
check("glossary stays selective (<= 45 per exam)", max(per_exam.values()) <= 45, per_exam)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_context(viewport={"width": 390, "height": 844}).new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.route("**/fonts.googleapis.com/**", lambda r: r.abort())

    # No exam in the link: the first listed exam opens; afterwards the last exam studied reopens.
    first = "CLF-C02" if "CLF-C02" in idx.get("study", {}) else "AIF-C01"
    pg.goto(BASE + "study.html"); pg.wait_for_selector(".daytitle")
    check("default opens first exam", pg.evaluate("location.hash") == f"#exam={first}&day=1", pg.evaluate("location.hash"))
    tabs = pg.eval_on_selector_all(".lseg", "els => els.map(e => [e.dataset.level, e.getAttribute('aria-pressed')])")
    check("level tabs", [t[0] for t in tabs] == ["foundational", "associate", "professional", "specialty"] and tabs[0][1] == "true", tabs)
    chips = pg.eval_on_selector_all("#examRow .chip", "els => els.map(e => e.dataset.exam)")
    check("foundational chips", "AIF-C01" in chips and "SAA-C03" not in chips, chips)
    pg.click(".lseg[data-level='specialty']")
    chips = pg.eval_on_selector_all("#examRow .chip", "els => els.map(e => e.dataset.exam)")
    check("specialty tab lists its exams", chips == ["ANS-C01", "SCS-C03"], chips)
    vt = pg.eval_on_selector_all(".vtab", "els => els.map(e => [e.dataset.vendor, +e.querySelector('.cnt').textContent])")
    check("all exams reachable", sum(n for _, n in vt) == len(files) if vt else len(files) == sum(int(c) for c in pg.eval_on_selector_all(".lseg .cnt", "els => els.map(e => e.textContent)")), vt)

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
    pg.goto(BASE + "study.html"); pg.reload(); pg.wait_for_selector(".daytitle")
    check("last exam reopens", pg.evaluate("location.hash").startswith("#exam=DEA-C01"), pg.evaluate("location.hash"))
    pg.goto(BASE + "study.html#exam=SAA-C03"); pg.reload(); pg.wait_for_selector(".daytitle")
    check("last day remembered", pg.evaluate("location.hash") == "#exam=SAA-C03&day=10", pg.evaluate("location.hash"))
    pg.goto(BASE + "study.html#exam=SAA-C03&day=3"); pg.reload(); pg.wait_for_selector(".daytitle")
    check("studied persists", pg.get_attribute("#doneBtn", "aria-pressed") == "true")
    pg.goto(BASE + "study.html#exam=SAA-C03&day=999"); pg.reload(); pg.wait_for_selector(".daytitle")
    check("day clamps to last", pg.evaluate("location.hash") == f"#exam=SAA-C03&day={len(saa['days'])}")
    check("final day links whole exam", pg.get_attribute(".qblink", "href") == "./#exam=SAA-C03")

    # Term popovers: each term marked at most once per day, never inside quiz text; tap pins the
    # popover with both languages; Escape and clicking elsewhere close it.
    pg.goto(BASE + "study.html#exam=SAA-C03&day=3"); pg.reload(); pg.wait_for_selector(".daytitle")
    ids = pg.eval_on_selector_all(".term", "els => els.map(e => e.dataset.term)")
    check("terms marked", len(ids) > 0, ids)
    check("each term once per day", len(ids) == len(set(ids)), ids)
    check("no terms in quiz", pg.locator(".quiz-q .term").count() == 0)
    t0 = next(t for t in gloss if t["id"] == ids[0])
    pg.locator(".term").first.click()
    pop = pg.inner_text("#termPop")
    check("popover shows term, en and ko", t0["term"] in pop and t0["en"][:30] in pop and t0["ko"][:10] in pop, pop)
    check("popover marks expanded", pg.get_attribute(".term >> nth=0", "aria-expanded") == "true")
    box = pg.eval_on_selector("#termPop", "e => { const r = e.getBoundingClientRect(); return [r.left, r.right, innerWidth]; }")
    check("popover inside viewport", box[0] >= 0 and box[1] <= box[2], box)
    pg.keyboard.press("Escape")
    check("escape closes popover", not pg.is_visible("#termPop"))
    pg.locator(".term").first.click(); pg.click(".daytitle")
    check("outside click closes popover", not pg.is_visible("#termPop"))
    pg.goto(BASE + "study.html#exam=AIB-C01&day=1"); pg.wait_for_selector(".daytitle")
    other = pg.eval_on_selector_all(".term", "els => els.map(e => e.dataset.term)")
    check("terms limited to their exams", all("AIB-C01" in next(t for t in gloss if t["id"] == i)["exams"] for i in other), other)

    for code in ["SAP-C02", "AIF-C01"]:
        pg.goto(BASE + f"study.html#exam={code}&day=1"); pg.wait_for_selector(".daytitle")
        check(f"{code} no horizontal overflow", pg.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"))

    # Compact day bar (same as the question bank's exam bar) and back-to-top.
    pg.goto(BASE + "study.html#exam=SAA-C03&day=3"); pg.reload(); pg.wait_for_selector(".daytitle")
    check("day bar hidden at top", not pg.evaluate("document.getElementById('dayBar').classList.contains('show')"))
    pg.evaluate("window.scrollTo(0, document.body.scrollHeight)"); pg.wait_for_timeout(300)
    check("day bar shown after scrolling", pg.evaluate("document.getElementById('dayBar').classList.contains('show')"))
    check("day bar text", pg.inner_text("#dayBarCode") == "SAA-C03" and pg.inner_text("#dayBarName").startswith("Day 3 / "), pg.inner_text("#dayBar"))
    check("back-to-top shown", pg.evaluate("document.getElementById('toTop').classList.contains('show')"))
    check("day bar support link", pg.get_attribute("#dayBar .barsupport", "href") == "support.html")
    pg.click("#barNext"); pg.wait_for_function("location.hash === '#exam=SAA-C03&day=4'")
    pg.wait_for_function("scrollY === 0")
    check("bar next opens next day at the top", pg.inner_text(".eyebrow").startswith("SAA-C03 · Day 4"))
    try: pg.wait_for_function("!document.getElementById('dayBar').classList.contains('show')", timeout=3000); hidden = True
    except Exception: hidden = False
    check("day bar hides again at top", hidden)
    pg.goto(BASE + "study.html#exam=SAA-C03&day=1"); pg.reload(); pg.wait_for_selector(".daytitle")
    pg.evaluate("window.scrollTo(0, document.body.scrollHeight)"); pg.wait_for_timeout(300)
    check("bar prev disabled on day 1", pg.evaluate("document.getElementById('barPrev').disabled"))

    # A cached older study.html (no day bar) paired with the current script must still render the day.
    old = re.sub(r'<div class="exambar" id="dayBar".*?</div></div>\s*<button class="totop"[^>]*>.</button>', "",
                  open(pathlib.Path(ROOT, "study.html"), encoding="utf-8").read(), flags=re.S)
    check("test setup: day bar stripped", 'id="dayBar"' not in old)
    pg2 = b.new_context(viewport={"width": 390, "height": 844}).new_page()
    errs2 = []
    pg2.on("pageerror", lambda e: errs2.append(str(e)))
    pg2.route("**/study.html*", lambda r: r.fulfill(status=200, content_type="text/html", body=old))
    pg2.goto(BASE + "study.html#exam=SAA-C03&day=2"); pg2.wait_for_selector(".daytitle")
    pg2.evaluate("window.scrollTo(0, document.body.scrollHeight)"); pg2.wait_for_timeout(200)
    check("old page + new script: day renders without errors", not errs2, errs2)
    h = hashlib.sha1(pathlib.Path(ROOT, "js", "study.js").read_bytes()).hexdigest()[:10]
    check("study.js version stamp is current (run tools/stamp_version.py)",
          f'js/study.js?v={h}"' in open(pathlib.Path(ROOT, "study.html"), encoding="utf-8").read())

    pg.goto(BASE); pg.wait_for_selector(".qcard")
    check("question bank links to study guide", pg.get_attribute(".studylink", "href") == "study.html")
    check("no page errors", not errs, errs)
    b.close()
print(f"{ok}/{ok + fail} passed")
