"""Vendor tabs (AWS | Palantir | Azure | Google Cloud) and the Palantir mock exam wording (Playwright, local server).

- One tab per vendor with that vendor's question total; the chip row lists only that vendor's exams.
- Switching vendor selects its first exam and updates #exam=; #exam= and #vendor= links pick the tab.
- Palantir exams: 70% pass mark and equal (assumed) domain weights are stated in the mock exam.
    python3 tools/vendor_tabs_test.py
"""
import functools, http.server, json, pathlib, sys, threading
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
def total(vendor): return sum(idx["exams"].get(c, {}).get("count", 0) for c, s in specs.items() if isinstance(s, dict) and s.get("vendor") == vendor)
pl_exams = [c for c, s in specs.items() if isinstance(s, dict) and s.get("vendor") == "palantir"]

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_context(viewport={"width": 390, "height": 844}).new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.route("**/fonts.googleapis.com/**", lambda r: r.abort())
    pg.goto(BASE + "#exam=SAA-C03"); pg.wait_for_selector(".qcard")
    tabs = pg.eval_on_selector_all(".vtab", "els => els.map(e => [e.dataset.vendor, e.getAttribute('aria-selected'), e.querySelector('.cnt').textContent])")
    check("vendor tabs", [t[0] for t in tabs] == ["aws", "palantir", "azure", "gcp", "databricks", "hashicorp"], tabs)
    check("aws selected for AWS exam link", tabs[0][1] == "true" and tabs[1][1] == "false", tabs)
    # index.html keeps its own exam list (EXAMS, EXAM_LEVEL): it must match exam-specs.json
    ex = pg.evaluate("EXAMS.map(([c, n, v]) => [c, v, EXAM_LEVEL[c] || null])")
    spec_exams = {c: s for c, s in specs.items() if isinstance(s, dict) and "vendor" in s}
    check("EXAMS lists every exam in exam-specs.json", sorted(c for c, _, _ in ex) == sorted(spec_exams), sorted(set(spec_exams) ^ {c for c, _, _ in ex}))
    check("EXAMS vendor and EXAM_LEVEL match exam-specs.json", all(spec_exams.get(c, {}).get("vendor") == v and spec_exams.get(c, {}).get("level") == l for c, v, l in ex),
          [(c, v, l) for c, v, l in ex if spec_exams.get(c, {}).get("vendor") != v or spec_exams.get(c, {}).get("level") != l])
    check("tab totals", [int(t[2]) for t in tabs] == [total(v) for v in ("aws", "palantir", "azure", "gcp", "databricks", "hashicorp")], tabs)
    codes = pg.eval_on_selector_all("#chipRow .chip[data-code]", "els => els.map(e => e.dataset.code)")
    check("aws chips only", "SAA-C03" in codes and not any(c.startswith("PLTR-") for c in codes), codes)
    check("bookmarks is an icon, not an exam chip", "__BOOKMARKS__" not in codes and pg.is_visible("#bmIcon"), codes)

    # Exam picker: chips of every level sit under level headings; there is no separate level control.
    heads = pg.eval_on_selector_all("#chipRow .lvlhead", "els => els.map(e => e.firstChild.textContent)")
    check("aws level headings", heads == ["Foundational", "Associate", "Professional", "Specialty"], heads)
    check("no level segmented control", pg.locator(".levelseg, .lseg, #levelRow").count() == 0)
    check("specialty chips under their heading", pg.eval_on_selector_all("#chipRow .lvlgroup[aria-label='Specialty'] .chip", "els => els.map(e => e.dataset.code)") == ["ANS-C01", "SCS-C03"])
    check("chip shows exam name", "Advanced Networking" in pg.inner_text("#chipRow"))
    # Picking a chip folds the picker to a one-line summary; the head reopens it.
    pg.click("#chipRow .chip[data-code='SCS-C03']"); pg.wait_for_function("location.hash === '#exam=SCS-C03'")
    check("picker folds after a pick", pg.get_attribute("#examToggle", "aria-expanded") == "false" and not pg.is_visible("#chipRow"))
    check("folded summary names the exam", "SCS-C03" in pg.inner_text("#examSum") and "Specialty" in pg.inner_text("#examSum"), pg.inner_text("#examSum"))
    pg.click("#examToggle")
    check("head reopens the picker", pg.is_visible("#chipRow .chip[data-code='SAA-C03']"))
    pg.click(".vtab[data-vendor='palantir']"); pg.wait_for_selector(".qcard")
    codes = pg.eval_on_selector_all("#chipRow .chip[data-code]", "els => els.map(e => e.dataset.code)")
    check("palantir has one level and no heading", pg.locator("#chipRow .lvlhead").count() == 0 and pg.locator("#chipRow .lvlgroup").count() == 1)
    check("palantir chips only", sorted(codes) == sorted(pl_exams), codes)
    active = pg.eval_on_selector("#chipRow .chip.active", "e => e.dataset.code")
    check("first palantir exam selected", active in pl_exams, active)
    check("hash follows", pg.evaluate("location.hash") == f"#exam={active}", pg.evaluate("location.hash"))
    check("palantir cards", pg.locator(".qcard").count() == idx["exams"][active]["count"])

    pg.goto(BASE + "#vendor=palantir"); pg.reload(); pg.wait_for_selector(".qcard")
    check("#vendor= link", pg.eval_on_selector(".vtab[aria-selected='true']", "e => e.dataset.vendor") == "palantir")
    pg.goto(BASE + "#exam=PLTR-DE"); pg.reload(); pg.wait_for_selector(".qcard")
    check("#exam= link sets vendor", pg.eval_on_selector(".vtab[aria-selected='true']", "e => e.dataset.vendor") == "palantir")
    check("#exam= link selects exam", pg.eval_on_selector("#chipRow .chip.active", "e => e.dataset.code") == "PLTR-DE")

    # Star icon: opens the bookmark view with the exam's level kept; pressed again it goes back to that exam.
    pg.goto(BASE + "#exam=SAP-C03"); pg.reload(); pg.wait_for_selector(".qcard")
    pg.click("#bmIcon"); pg.wait_for_function("location.hash === '#bookmarks'")
    check("star pressed in bookmark view", pg.get_attribute("#bmIcon", "aria-pressed") == "true")
    check("bookmark view keeps the exam in the summary", "SAP-C03" in pg.inner_text("#examSum"), pg.inner_text("#examSum"))
    pg.click("#bmIcon"); pg.wait_for_function("location.hash === '#exam=SAP-C03'")
    check("star again returns to the exam", pg.eval_on_selector("#chipRow .chip.active", "e => e.dataset.code") == "SAP-C03" and pg.get_attribute("#bmIcon", "aria-pressed") == "false")
    nav = pg.evaluate("(() => { const t = document.getElementById('vendorRow').getBoundingClientRect(), s = document.getElementById('bmIcon').getBoundingClientRect(); return [t.bottom, s.top]; })()")
    check("bookmarks pill sits in the header, above the tab row", nav[1] < nav[0], nav)
    ov = pg.eval_on_selector("#vendorRow", "e => [e.scrollHeight, e.clientHeight, e.scrollWidth, e.clientWidth]")
    check("tab row has no vertical scroll (no stray scrollbar on Windows)", ov[0] <= ov[1], ov)
    names = pg.eval_on_selector_all(".vtab", "els => els.filter(e => e.offsetParent).map(e => e.innerText.trim())")
    check("phone tab names are readable (no PLTR/DBX/HC)", not any(n in ("PLTR", "DBX", "HC") for n in names), names)
    nar = b.new_context(viewport={"width": 340, "height": 800}).new_page()
    nar.route("**/fonts.googleapis.com/**", lambda r: r.abort())
    nar.goto(BASE + "#exam=VLT-VA003"); nar.wait_for_selector(".qcard")
    cls = nar.eval_on_selector("#vendorRow", "e => [e.className, e.scrollWidth > e.clientWidth]")
    check("340px: overflowing tab row shows an edge fade", (not cls[1]) or "fade" in cls[0], cls)

    pg.goto(BASE + "#vendor=azure"); pg.reload(); pg.wait_for_selector(".qcard")
    check("#vendor=azure opens AZ-900", pg.eval_on_selector("#chipRow .chip.active", "e => e.dataset.code") == "AZ-900"
          and pg.locator(".qcard").count() == idx["exams"]["AZ-900"]["count"])
    pg.goto(BASE + "#exam=PLTR-APD"); pg.reload(); pg.wait_for_selector(".qcard")
    check("PLTR-APD chip selectable", pg.eval_on_selector("#chipRow .chip.active", "e => e.dataset.code") == "PLTR-APD")
    pg.goto(BASE + "#mock=PLTR-AIE"); pg.reload(); pg.wait_for_selector("#mockRoot .mk")
    setup = pg.inner_text("#mockRoot")
    check("mock setup says equal weights", "official weights are not published" in setup, setup[:300])
    check("mock setup states the percent pass mark", "official pass mark 70% correct" in setup and "undefined" not in setup, setup[:400])
    pg.click('[data-act="start"]'); pg.wait_for_selector(".mkbar")
    pg.click('[data-act="grid"]'); pg.click('[data-act="ask"]')
    pg.click('[data-act="submit"]'); pg.wait_for_selector("#mockRoot .score")
    res = pg.inner_text("#mockRoot")
    check("result states 70% pass mark", "official pass mark is 70% correct" in res, res[:400])
    check("result has no AWS scaled-score note", "/1000" not in res and "AWS scaled" not in res)
    check("no page errors", not errs, errs)

    # 320 px phones: a NEW badge does not push the count to its own line.
    sm = b.new_context(viewport={"width": 320, "height": 800}).new_page()
    sm.route("**/fonts.googleapis.com/**", lambda r: r.abort())
    sm.goto(BASE + "#exam=SAA-C03"); sm.wait_for_selector(".qcard")
    ov = sm.evaluate("document.documentElement.scrollWidth <= document.documentElement.clientWidth")
    check("320px: page has no horizontal overflow", ov)
    off = sm.eval_on_selector_all("#chipRow .chip", "cs => cs.filter(c => Math.abs(c.querySelector('.cnt').getBoundingClientRect().top - c.querySelector('.code').getBoundingClientRect().top) > 4).map(c => c.dataset.code)")
    check("320px: counts on the code line", not off, off)
    b.close()
print(f"{ok}/{ok + fail} passed"); sys.exit(1 if fail else 0)
