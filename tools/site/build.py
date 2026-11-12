#!/usr/bin/env python3
"""Static, crawlable pages for cert-bank (no JavaScript needed to read them).

Writes, from the data the bank already has:
  exams/index.html            list of every exam, by vendor
  exams/<code>/index.html     one hub per exam: format, domains (weights, tasks, written briefs), study order,
                              what the bank holds, recent changes, buttons into the bank / mock exam / study plan
  about.html, privacy.html    site pages
  sitemap.xml                 the indexable pages only (the bank, mock exam and study screens are tools, not pages)

Sources: data/exam-specs.json, data/exam-tasks.json, data/<EXAM>.json (examDomain only), data/study/<EXAM>.json,
data/changes/*.json, content/domain-briefs.json (hand-written per exam|domain; copied from blogger-publisher
content/domains.json at 7b009c4), EXAMS / VENDORS in index.html.

Output is deterministic (no build date), so `python3 tools/site/build.py --check` can fail a test when a page is stale.
Run `python3 tools/site/build.py` after any data change; tools/site_test.py checks it.
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guides import Guides, KINDS, TXT  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BASE = "https://hyunhp.github.io/cert-bank/"
SITE = "cert-bank"
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
LEVELS = [("foundational", "Foundational"), ("associate", "Associate"), ("professional", "Professional"),
          ("expert", "Expert"), ("specialty", "Specialty")]
esc = lambda s: html.escape(str(s), quote=True)


def load(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return json.load(f)


def nice_date(d):
    y, m, day = map(int, d.split("-"))
    return f"{MONTHS[m - 1]} {day}, {y}"


def pct(w):
    return f"{w:g}%" if w == round(w, 1) else f"{w:.1f}%"


def index_js():
    """EXAMS and VENDORS from index.html, so names stay in one place."""
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    ex = re.search(r"const EXAMS = \[(.*?)\n\]", src, re.S).group(1)
    exams = [(m[0], m[1], m[2] or "aws") for m in re.findall(r'\["([^"]+)","([^"]+)"(?:,"([^"]+)")?\]', ex)]
    ven = re.search(r"const VENDORS = (\[.*?\]);", src).group(1)
    vendors = [(m[0], m[1]) for m in re.findall(r'\["([^"]+)","([^"]+)"', ven) if m[0] != "archive"]
    return exams, vendors


def slug(code):
    return code.lower()


# ---------------------------------------------------------------- page frame
UI = {
    "en": {"exams": "Exams", "bank": "Question bank", "study": "Study plans", "guides": "Guides", "about": "About",
           "contact": "Contact", "privacy": "Privacy", "support": "Support", "source": "Source on GitHub",
           "free": '<b>Every question here is free and will stay free.</b> No ads, no sign-up. If the site helped you, '
                   '<a href="{up}support.html">a coffee keeps new questions coming</a> (optional).',
           "fine": "Unofficial study material. Not affiliated with or endorsed by AWS, Palantir, Microsoft, Google, "
                   "Databricks or HashiCorp. Exam names belong to their owners."},
    "ko": {"exams": "시험", "bank": "문제은행", "study": "학습 계획", "guides": "가이드", "about": "소개",
           "contact": "문의", "privacy": "개인정보", "support": "후원", "source": "GitHub 소스",
           "free": '<b>모든 문제는 앞으로도 무료입니다.</b> 광고도 가입도 없습니다. 도움이 되셨다면 '
                   '<a href="{up}support.html">커피 한 잔으로 응원</a>해 주세요(선택).',
           "fine": "비공식 학습 자료입니다. AWS, Palantir, Microsoft, Google, Databricks, HashiCorp와 제휴하거나 "
                   "보증받지 않았습니다. 시험 이름은 각 소유자의 것입니다."},
}


def page(title, desc, path, body, depth, crumbs=(), lang="en", alternates=None, og_type="website", image=None):
    """alternates: {lang: path} of the same page in each language (hreflang)."""
    up = "../" * depth
    canon = BASE + path
    t = UI[lang]
    nav = ' <span aria-hidden="true">›</span> '.join(f'<a href="{up}{h}">{esc(x)}</a>' for x, h in crumbs)
    alt = ""
    if alternates:
        alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{p}">\n' for l, p in alternates.items())
        alt += f'<link rel="alternate" hreflang="x-default" href="{BASE}{alternates.get("en", path)}">\n'
    img = f'<meta property="og:image" content="{esc(image)}">\n' if image else ""
    guides = f'<a href="{up}{"ko/" if lang == "ko" else ""}guides/">{t["guides"]}</a>'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{alt}<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="{og_type}">
{img}<link rel="apple-touch-icon" href="{up}assets/icon-180.png">
<meta name="theme-color" content="#1E5AA8">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body>
<header class="site"><div class="in">
  <a class="brand" href="{up}exams/">{SITE}</a>
  <nav><a href="{up}exams/">{t["exams"]}</a>{guides}<a href="{up}./">{t["bank"]}</a><a href="{up}study.html">{t["study"]}</a><a href="{up}about.html">{t["about"]}</a></nav>
</div></header>
<main class="in">
{f'<p class="crumbs">{nav}</p>' if crumbs else ''}{body}
</main>
<footer class="site"><div class="in">
  <p class="support">{t["free"].format(up=up)}</p>
  <p><a href="{up}about.html">{t["about"]}</a> · <a href="{up}contact.html">{t["contact"]}</a> · <a href="{up}privacy.html">{t["privacy"]}</a> · <a href="{up}support.html">{t["support"]}</a> · <a href="https://github.com/hyunhp/cert-bank">{t["source"]}</a></p>
  <p class="fine">{t["fine"]}</p>
</div></footer>
</body>
</html>
"""


# ---------------------------------------------------------------- data
def bank_facts(code):
    qs = load(f"data/{code}.json")
    by_dom, multi = {}, 0
    for q in qs:
        by_dom[q["examDomain"]] = by_dom.get(q["examDomain"], 0) + 1
        multi += len(q["correctKeys"]) > 1
    return len(qs), by_dom, multi


def study_plan(code):
    p = os.path.join(ROOT, "data", "study", f"{code}.json")
    if not os.path.exists(p):
        return []
    runs = []   # [domain, first day, last day, title of the first day]
    for d in load(f"data/study/{code}.json")["days"]:
        dom = d.get("domain")
        if runs and runs[-1][0] == dom:
            runs[-1][2] = d["day"]
        else:
            runs.append([dom, d["day"], d["day"], d.get("title", "")])
    return runs


def changes_by_exam():
    """{exam: [(date, pr, note, {kind: n})]} newest first; per PR, the kinds that touched that exam."""
    out = {}
    folder = os.path.join(ROOT, "data", "changes")
    for name in os.listdir(folder):
        if not name.endswith(".json"):
            continue
        groups = {}
        for e in load(f"data/changes/{name}"):
            g = groups.setdefault(e["exam"], {"date": e["date"], "pr": e["pr"], "notes": [], "kinds": {}})
            g["kinds"][e["change"]] = g["kinds"].get(e["change"], 0) + 1
            if e.get("note") and e["note"] not in g["notes"]:
                g["notes"].append(e["note"])
            g["date"] = max(g["date"], e["date"])
        for exam, g in groups.items():
            out.setdefault(exam, []).append(g)
    for v in out.values():
        v.sort(key=lambda g: (g["date"], g["pr"]), reverse=True)
    return out


KIND_WORDS = {"added": ("question added", "questions added"), "removed": ("question removed", "questions removed"),
              "stem": ("question reworded", "questions reworded"), "choices": ("answer choice set changed", "answer choice sets changed"),
              "answer": ("answer key corrected", "answer keys corrected"), "explanation": ("explanation rewritten", "explanations rewritten"),
              "domain": ("question moved to another domain", "questions moved to another domain")}


def kinds_text(kinds):
    parts = []
    for k, (one, many) in KIND_WORDS.items():
        n = kinds.get(k)
        if n:
            parts.append(f"{n:,} {one if n == 1 else many}")
    return ", ".join(parts)


# ---------------------------------------------------------------- hubs
def hub(code, name, vendor_name, spec, tasks, briefs, changes, successor, predecessor, guides=()):
    total, by_dom, multi = bank_facts(code)
    level = dict(LEVELS).get(spec.get("level"), "")
    title = f"{code} {vendor_name} {name}: domains, weights and study order | {SITE}"
    desc = (f"{code} ({vendor_name} {name}) at a glance: {spec['questions']} questions in {spec['minutes']} minutes, "
            f"{len(spec['domains'])} domains, what each domain asks, a study order, and {total:,} free original practice questions.")
    up = "../../"
    b = [f'<h1><span class="code">{code}</span> {esc(vendor_name)} {esc(name)}</h1>']
    last = spec.get("lastDay")
    if spec.get("update"):   # the bank's own dated note on a version change says the most
        other = successor or predecessor
        link = f' <a href="../{slug(other)}/">{other} exam page</a>.' if other else ""
        b.append(f'<p class="notice">{esc(spec["update"])}{link}</p>')
    elif last:
        nxt = f' Its replacement is <a href="../{slug(successor)}/">{successor}</a>.' if successor else ""
        b.append(f'<p class="notice">The last day to take {code} is {nice_date(last)}.{nxt} '
                 f'After that date this page and its questions stay online for the topics they cover.</p>')
    elif predecessor:
        b.append(f'<p class="notice">{code} is the new version of <a href="../{slug(predecessor)}/">{predecessor}</a>.</p>')

    # buttons into the tools
    b.append('<p class="actions">'
             f'<a class="btn primary" href="{up}#exam={code}">Practice {total:,} questions</a>'
             f'<a class="btn" href="{up}#mock={code}">Take a timed mock exam</a>'
             + (f'<a class="btn" href="{up}study.html#exam={code}">Day-by-day study plan</a>' if study_plan(code) else "")
             + "</p>")
    if guides:
        b.append("<h2>Guides for this exam</h2><ul class=\"guides\">" + "".join(
            f'<li><a href="{up}guides/{g["slug"]}/">{esc(g["lang"]["en"]["title"])}</a>'
            + (f' · <a href="{up}ko/guides/{g["slug"]}/" hreflang="ko" lang="ko">한국어</a>' if "ko" in g["lang"] else "")
            + "</li>" for g in guides) + "</ul>")

    # format
    if spec.get("passingScore"):
        passing = f"{spec['passingScore']} on a scaled score of 100–1,000"
    elif spec.get("passingPct"):
        passing = f"{spec['passingPct']}% of the questions"
    else:
        passing = "Not published by the vendor"
    rows = [("Level", level), ("Questions", f"{spec['questions']}"), ("Time", f"{spec['minutes']} minutes "
            f"(about {spec['minutes'] / spec['questions']:.1f} minutes per question)".replace(".0 minutes", " minutes")), ("Passing mark", passing)]
    if last:
        rows.append(("Last day to take it", nice_date(last)))
    b.append("<h2>The exam at a glance</h2><table class=\"facts\">" + "".join(
        f"<tr><th scope=\"row\">{k}</th><td>{esc(v)}</td></tr>" for k, v in rows if v) + "</table>")

    # domains
    doms = spec["domains"]
    b.append("<h2>Domains and weights</h2>")
    if spec.get("weightsAssumed"):
        b.append("<p>The vendor does not publish domain weights for this exam, so the shares below are equal by assumption. "
                 "Treat every domain as roughly the same size.</p>")
    b.append('<table class="doms"><thead><tr><th>Domain</th><th>Weight</th><th>Practice questions here</th></tr></thead><tbody>'
             + "".join(f'<tr><td>{d["code"]} · {esc(d["name"])}</td><td>{pct(d["weight"])}</td>'
                       f'<td><a href="{up}#exam={code}&amp;d={d["code"]}">{by_dom.get(d["code"], 0):,}</a></td></tr>' for d in doms)
             + "</tbody></table>")
    if multi:
        b.append(f"<p>{multi:,} of the {total:,} practice questions ({multi / total:.0%}) ask for more than one answer.</p>")

    for d in doms:
        dc = d["code"]
        b.append(f'<h3 id="{dc.lower()}">{dc} · {esc(d["name"])} <span class="w">{pct(d["weight"])}</span></h3>')
        br = briefs.get(f"{code}|{dc}")
        if br:
            b.append(f"<p>{esc(br['how'])}</p>")
            if br.get("focus"):
                b.append("<p class=\"label\">What to watch for</p><ul>" + "".join(f"<li>{esc(x)}</li>" for x in br["focus"]) + "</ul>")
        mine = [(k, v) for k, v in tasks.items() if k.split(".")[0] == dc[1:]]
        if mine:
            b.append(f'<details><summary>Tasks in the official exam guide ({len(mine)})</summary><ul class="tasks">'
                     + "".join(f'<li><a href="{up}#exam={code}&amp;d={dc}&amp;t=T{k}">{k}</a> {esc(v)}</li>' for k, v in mine)
                     + "</ul></details>")

    # study order
    runs = study_plan(code)
    if runs:
        names = {d["code"]: d["name"] for d in doms}
        days = runs[-1][2]
        items = []
        for dom, a, z, first in runs:
            when = f"Day {a}" if a == z else f"Days {a}–{z}"
            what = f"{dom} · {esc(names.get(dom, dom))}" if dom else esc(first or "Review")
            items.append(f'<li><a href="{up}study.html#exam={code}&amp;day={a}">{when}</a>: {what}</li>')
        b.append(f"<h2>A study order that works</h2><p>The {days}-day study plan for {code} takes the domains in this order. "
                 "Each day has a short reading, key terms and a quiz from the bank.</p><ol class=\"plan\">" + "".join(items) + "</ol>")

    # changes
    ch = changes.get(code, [])[:5]
    if ch:
        lis = []
        for g in ch:
            what = kinds_text(g["kinds"])
            if "exam-added" in g["kinds"]:
                what = "Exam added to the bank" + (f" ({what})" if what else "")
            lis.append(f"<li><time datetime=\"{g['date']}\">{nice_date(g['date'])}</time>: {esc(what)}</li>")
        b.append("<h2>Recent changes to these questions</h2><ul class=\"changes\">" + "".join(lis) + "</ul>")

    b.append("<h2>About these questions</h2><p>Every question is original, written from the public exam guide and checked "
             "against the vendor's own documentation. None comes from a real exam. Each one has an explanation of why the "
             f'answer is right and why the other options are wrong. <a href="{up}about.html#how">How the questions are written</a>.</p>')
    return title, desc, "\n".join(b)


def exam_list(exams, vendors, specs):
    b = ["<h1>Certification exams</h1>",
         f"<p class=\"lead\">Free, original practice questions, mock exams and day-by-day study plans for {len(exams)} "
         "cloud, data and AI certification exams. Pick an exam for its domains, weights, a study order and what the bank holds.</p>"]
    for vid, vname in vendors:
        mine = [e for e in exams if e[2] == vid]
        if not mine:
            continue
        b.append(f"<h2 id=\"{vid}\">{esc(vname)}</h2><ul class=\"exams\">")
        for code, name, _ in mine:
            s = specs[code]
            lv = dict(LEVELS).get(s.get("level"), "")
            end = f' · last day {nice_date(s["lastDay"])}' if s.get("lastDay") else ""
            b.append(f'<li><a href="{slug(code)}/"><span class="code">{code}</span> {esc(name)}</a>'
                     f'<span class="meta">{lv} · {s["questions"]} questions, {s["minutes"]} min{end}</span></li>')
        b.append("</ul>")
    return "\n".join(b)


# ---------------------------------------------------------------- site pages
ABOUT = """<h1>About cert-bank</h1>
<p class="lead">cert-bank is a free study site for cloud, data and AI certification exams: original practice questions with
explanations, timed mock exams, and day-by-day study plans. There are no ads and no sign-up, and nothing is behind a paywall.</p>

<h2>What is here</h2>
<ul>
<li><a href="exams/">Exam pages</a>: one page per exam with its format, domains and weights, what each domain asks,
and a study order.</li>
<li><a href="./">Question bank</a>: practice by exam, domain or task, bookmark questions and see your accuracy per domain.</li>
<li>Mock exams: a timed exam drawn from the bank, with the real exam's length and domain mix, and a review afterwards.</li>
<li><a href="study.html">Study plans</a>: a reading, key terms and a short quiz for every day.</li>
</ul>
<p>Your progress (answers, bookmarks, mock exam history) stays in your own browser. Nothing is sent to a server; see the
<a href="privacy.html">privacy page</a>.</p>

<h2 id="how">How the questions are written</h2>
<p>The questions are written with Claude, an AI model by Anthropic, and the site is maintained by its owner. They are
not exam dumps: none is copied or reconstructed from a real exam. The process:</p>
<ol>
<li>Each exam starts from its <b>public exam guide</b>: the domains, their weights and the tasks listed under each.</li>
<li>Questions are written for one task at a time, as scenarios that ask for a decision, a comparison or a fix, and each
one carries an explanation of the right answer and of every wrong option.</li>
<li>A separate reviewer checks every batch against the <b>vendor's own documentation</b> (for example
docs.aws.amazon.com, learn.microsoft.com, docs.cloud.google.com, docs.databricks.com, developer.hashicorp.com) and
removes questions that repeat another, rely on preview features, or cannot be confirmed.</li>
<li>Automatic checks run before anything is published: format, near-duplicates, stem length, and whether the correct
answer is too often the longest option (a give-away in many question banks).</li>
<li>When a service or an exam changes, questions are corrected in place and the change is logged; each exam page lists
its recent changes.</li>
</ol>
<p>Mistakes still happen. If you find a wrong answer, please <a href="contact.html">tell us</a> with the question id.</p>

<h2>Independence</h2>
<p>cert-bank is not affiliated with, endorsed by or sponsored by AWS, Palantir, Microsoft, Google, Databricks or HashiCorp.
Exam names and codes belong to their owners. Always check the vendor's official exam page for the current format,
price and policies before you book.</p>

<h2>Support</h2>
<p>The site runs on voluntary support. If it helped you, <a href="support.html">a coffee</a> keeps new questions coming.
It unlocks nothing extra: everyone gets the same site.</p>
"""

PRIVACY = """<h1>Privacy</h1>
<p class="lead">Short version: cert-bank has no accounts, no ads, no analytics and no cookies of its own. Your study
progress stays in your browser.</p>

<h2>What stays on your device</h2>
<p>The question bank, mock exams and study plans save your answers, bookmarks, mock exam history and study progress in
your browser's local storage, so they are there the next time you visit. This data never leaves your device unless you
export a bookmark backup yourself. Clearing your browser's site data deletes it.</p>

<h2>Who else receives a request</h2>
<ul>
<li><b>GitHub Pages</b> hosts the site. Like any web server it receives your IP address and browser details when a page
loads; see the GitHub privacy statement.</li>
<li><b>Google Fonts</b> serves the typefaces on the question bank, study and support pages, so your browser requests them
from Google's servers.</li>
<li>Images on guide pages are served from <code>hyunhp.github.io</code> (also GitHub Pages).</li>
</ul>

<h2>Payments</h2>
<p>Support is optional. The support page links to Ko-fi and KakaoPay; a payment happens entirely on their sites, under
their privacy policies. cert-bank never sees card details.</p>

<h2>Changes</h2>
<p>If this policy changes, this page changes with it. Questions about it: <a href="mailto:koreanxpodcast@gmail.com">koreanxpodcast@gmail.com</a>.
Last updated November 13, 2026.</p>
"""


CONTACT = """<h1>Contact</h1>
<p class="lead">Questions, corrections and suggestions are welcome by e-mail:
<a href="mailto:koreanxpodcast@gmail.com">koreanxpodcast@gmail.com</a>.</p>

<h2>Reporting a wrong answer</h2>
<p>Please include the exam code and the question id (for example <code>SAA-C03 Q000123</code>, shown on every question
card), what you think is wrong, and a link to the vendor documentation if you have one. Corrections are made in place,
and the exam's page lists them under its recent changes.</p>
<p>If you prefer, you can also open a <a href="https://github.com/hyunhp/cert-bank/issues">GitHub issue</a>.</p>

<h2>Languages</h2>
<p>English or Korean (한국어) are both fine.</p>
"""


def write(path, text, out, check):
    full = os.path.join(ROOT, path)
    old = open(full, encoding="utf-8").read() if os.path.exists(full) else None
    if old != text:
        out.append(path)
        if not check:
            os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
            with open(full, "w", encoding="utf-8") as f:
                f.write(text)


def write_guides(gd, changed, check):
    urls = []
    for lang in ("en", "ko"):
        pre = "ko/" if lang == "ko" else ""
        mine = [g for g in gd.items if lang in g["lang"]]
        if not mine:
            continue
        t = TXT[lang]
        b = [f"<h1>{t['list_h1']}</h1>", f"<p class=\"lead\">{t['list_lead']}</p>"]
        for prefix, label in KINDS[lang]:
            group = [g for g in mine if g["slug"].startswith(prefix)]
            if group:
                b.append(f"<h2>{label}</h2><ul class=\"exams\">" + "".join(
                    f'<li><a href="{g["slug"]}/">{esc(g["lang"][lang]["title"])}</a>'
                    f'<span class="meta">{", ".join(g["exams"])}</span></li>' for g in group) + "</ul>")
        alts = {"en": "guides/", "ko": "ko/guides/"}
        depth = 2 if lang == "ko" else 1
        write(pre + "guides/index.html", page(f"{t['list_h1']} | {SITE}", t["list_lead"][:155], pre + "guides/", "\n".join(b),
                                             depth, lang=lang, alternates=alts), changed, check)
        urls.append(pre + "guides/")
        for g in mine:
            path = gd.path(g["slug"], lang)
            depth = path.count("/")
            up = "../" * depth
            other = "ko" if lang == "en" else "en"
            g_l = g["lang"][lang]
            body = gd.render_body(g, lang, up)
            sw = (f'<p class="langswitch"><a href="{up}{gd.path(g["slug"], other)}" hreflang="{other}" lang="{other}">'
                  f'{t["read_other"]}</a></p>') if other in g["lang"] else ""
            art = f'{sw}<article class="paper"><h1>{esc(g_l["title"])}</h1>\n{body}\n</article>'
            alts = {l: gd.path(g["slug"], l) for l in g["lang"]}
            img = f"https://hyunhp.github.io/bdb-images/images/{g['slug']}.png"
            crumbs = [(UI[lang]["guides"], pre + "guides/")]
            write(path + "index.html", page(f"{g_l['title']} | {SITE}", gd.description(body, lang), path, art, depth, crumbs,
                                            lang=lang, alternates=alts, og_type="article", image=img), changed, check)
            urls.append(path)
    return urls


def main():
    check = "--check" in sys.argv
    exams, vendors = index_js()
    vendor_name = dict(vendors)
    specs = {k: v for k, v in load("data/exam-specs.json").items() if isinstance(v, dict)}
    tasks = load("data/exam-tasks.json")
    briefs = load("content/domain-briefs.json")
    changes = changes_by_exam()
    names = {c: n for c, n, _ in exams}
    assert set(names) == set(specs), "EXAMS in index.html and exam-specs.json differ"
    # successor: same name with " (new)"; predecessor the reverse
    base = lambda n: n.replace(" (new)", "")
    succ = {c: o for c, n, _ in exams for o, m, _ in exams if o != c and base(m) == n and m.endswith(" (new)")}
    pred = {v: k for k, v in succ.items()}

    gd = Guides(ROOT, specs, lambda c: bank_facts(c)[0], lambda c: (study_plan(c) or [[0, 0, 0]])[-1][2],
                lambda p: open(os.path.join(ROOT, p), encoding="utf-8").read())
    changed, urls = [], ["", "exams/", "about.html", "contact.html", "privacy.html"]
    urls += write_guides(gd, changed, check)
    write("exams/index.html", page(f"Certification exams: domains, weights and study plans | {SITE}",
                                   f"Free original practice questions, mock exams and study plans for {len(exams)} cloud, data and AI certification exams.",
                                   "exams/", exam_list(exams, vendors, specs), 1), changed, check)
    for code, name, vid in exams:
        title, desc, body = hub(code, name, vendor_name[vid], specs[code], tasks.get(code, {}), briefs, changes,
                                succ.get(code), pred.get(code), gd.for_exam(code))
        path = f"exams/{slug(code)}/"
        write(path + "index.html", page(title, desc, path, body, 2, [("Exams", "exams/")]), changed, check)
        urls.append(path)
    write("about.html", page(f"About {SITE}: how the practice questions are written", "What cert-bank is, how its original "
                             "practice questions are written and reviewed, and who runs it.", "about.html", ABOUT, 0), changed, check)
    write("privacy.html", page(f"Privacy | {SITE}", "cert-bank has no accounts, ads, analytics or cookies; study progress "
                               "stays in your browser.", "privacy.html", PRIVACY, 0), changed, check)
    write("contact.html", page(f"Contact | {SITE}", "How to reach cert-bank: questions, corrections to practice "
                               "questions and suggestions, by e-mail.", "contact.html", CONTACT, 0), changed, check)
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{BASE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    write("sitemap.xml", sm, changed, check)
    if check:
        if changed:
            print("stale (run python3 tools/site/build.py):", *changed, sep="\n  ")
            sys.exit(1)
        print(f"site pages up to date ({len(urls)} urls)")
    else:
        print(f"wrote {len(changed)} file(s); sitemap has {len(urls)} urls")


if __name__ == "__main__":
    main()
