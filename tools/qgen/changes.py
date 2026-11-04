"""Change log for readers of the bank (the blog publisher): python3 tools/qgen/changes.py <PR> [--base origin/main] [--head <ref>] [--date YYYY-MM-DD] [--note "why"]

Compares data/ at --base (default origin/main) with --head (default: the working tree) and writes data/changes/<PR>.json,
one entry per change:
    {"date": "2026-11-04", "pr": 102, "exam": "SAA-C03", "id": "Q001234", "change": "answer", "important": true, "note": "..."}
Question changes (id set): added, removed, stem, choices, answer, explanation, domain (examDomain/examTask).
Exam changes (id null): exam-added, exam-removed, lastDay, domains.
`important` = a post built from the old text would now be wrong or obsolete: stem, choices, answer, domain, removed and every exam change.
Fill `note` with the reason (--note sets it for every entry; edit the file for finer notes). No data change: no file."""
import datetime, json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
CHANGES = {"added", "removed", "stem", "choices", "answer", "explanation", "domain", "exam-added", "exam-removed", "lastDay", "domains"}
IMPORTANT = {"removed", "stem", "choices", "answer", "domain", "exam-added", "exam-removed", "lastDay", "domains"}


def _entry(date, pr, exam, qid, change, note=""):
    return {"date": date, "pr": pr, "exam": exam, "id": qid, "change": change, "important": change in IMPORTANT, "note": note}


def diff_questions(exam, old, new, old_exp, new_exp, date, pr):
    """old/new: lists of question dicts of one exam file; *_exp: {id: explanation}."""
    o, n = {q["id"]: q for q in old}, {q["id"]: q for q in new}
    out = []
    for qid in sorted(set(n) - set(o)):
        out.append(_entry(date, pr, exam, qid, "added"))
    for qid in sorted(set(o) - set(n)):
        out.append(_entry(date, pr, exam, qid, "removed"))
    for qid in sorted(set(o) & set(n)):
        a, b = o[qid], n[qid]
        if a.get("stem") != b.get("stem"):
            out.append(_entry(date, pr, exam, qid, "stem"))
        # choices: compare the texts as a set (a re-ordered answer list is not a change); the answer: the correct texts
        ct = lambda q: sorted(c["text"] for c in q.get("choices", []))
        ans = lambda q: sorted(c["text"] for c in q.get("choices", []) if c["key"] in q.get("correctKeys", []))
        if ct(a) != ct(b):
            out.append(_entry(date, pr, exam, qid, "choices"))
        if ans(a) != ans(b):
            out.append(_entry(date, pr, exam, qid, "answer"))
        if (a.get("examDomain"), a.get("examTask")) != (b.get("examDomain"), b.get("examTask")) and "examDomain" in a:
            out.append(_entry(date, pr, exam, qid, "domain"))
        if old_exp.get(qid) != new_exp.get(qid):
            out.append(_entry(date, pr, exam, qid, "explanation"))
    return out


def diff_specs(old, new, date, pr):
    """old/new: exam-specs.json contents."""
    exams = lambda d: {k: v for k, v in d.items() if isinstance(v, dict) and "vendor" in v}
    o, n = exams(old), exams(new)
    out = [_entry(date, pr, e, None, "exam-added") for e in sorted(set(n) - set(o))]
    out += [_entry(date, pr, e, None, "exam-removed") for e in sorted(set(o) - set(n))]
    for e in sorted(set(o) & set(n)):
        if o[e].get("lastDay") != n[e].get("lastDay"):
            out.append(_entry(date, pr, e, None, "lastDay", f"{o[e].get('lastDay')} -> {n[e].get('lastDay')}"))
        dom = lambda s: [(d["code"], d["name"], d["weight"]) for d in s.get("domains", [])]
        if dom(o[e]) != dom(n[e]):
            out.append(_entry(date, pr, e, None, "domains"))
    return out


def _git(base, path):
    r = subprocess.run(["git", "show", f"{base}:{path}"], cwd=ROOT, capture_output=True, text=True)
    return json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else None


def _read(ref, path):
    if ref is None:
        p = ROOT / path
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None
    return _git(ref, path)


def collect(pr, base, head, date):
    specs_new = _read(head, "data/exam-specs.json") or {}
    specs_old = _read(base, "data/exam-specs.json") or {}
    out = diff_specs(specs_old, specs_new, date, pr)
    for exam in sorted(set(k for k, v in {**specs_old, **specs_new}.items() if isinstance(v, dict) and "vendor" in v)):
        out += diff_questions(exam, _read(base, f"data/{exam}.json") or [], _read(head, f"data/{exam}.json") or [],
                              _read(base, f"data/explanations/{exam}.json") or {}, _read(head, f"data/explanations/{exam}.json") or {}, date, pr)
    return out


def main(argv):
    if not argv or not argv[0].isdigit():
        print(__doc__); return 2
    pr = int(argv[0])
    opt = lambda name, default=None: argv[argv.index(name) + 1] if name in argv else default
    entries = collect(pr, opt("--base", "origin/main"), opt("--head"), opt("--date", datetime.date.today().isoformat()))
    note = opt("--note", "")
    for e in entries:
        e["note"] = e["note"] or note
    if not entries:
        print("no data changes, no file written"); return 0
    (ROOT / "data" / "changes").mkdir(exist_ok=True)
    (ROOT / "data" / "changes" / f"{pr}.json").write_text(json.dumps(entries, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    imp = sum(e["important"] for e in entries)
    print(f"data/changes/{pr}.json: {len(entries)} entries, {imp} important")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
