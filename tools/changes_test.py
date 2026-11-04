"""Change log guard: python3 tools/changes_test.py
- diff_questions / diff_specs report the right change kinds (and ignore a re-ordered answer list);
- every data/changes/<PR>.json is well formed."""
import json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "qgen"))
import changes

ok = fail = 0
def check(name, cond, info=""):
    global ok, fail
    if cond: ok += 1
    else: fail += 1; print("FAIL", name, info)

def q(qid, stem="S", texts=("a", "b", "c", "d"), correct=("A",), dom="D1", task="T1.1"):
    return {"id": qid, "stem": stem, "choices": [{"key": k, "text": t} for k, t in zip("ABCDE", texts)], "correctKeys": list(correct), "examDomain": dom, "examTask": task}

kinds = lambda old, new, oe={}, ne={}: sorted((e["id"], e["change"]) for e in changes.diff_questions("X", old, new, oe, ne, "2026-01-01", 1))
check("added", kinds([], [q("Q1")]) == [("Q1", "added")])
check("removed", kinds([q("Q1")], []) == [("Q1", "removed")])
check("stem", kinds([q("Q1")], [q("Q1", stem="T")]) == [("Q1", "stem")])
check("answer", kinds([q("Q1")], [q("Q1", correct=("B",))]) == [("Q1", "answer")])
check("choices text", kinds([q("Q1")], [q("Q1", texts=("a", "b", "c", "z"))]) == [("Q1", "choices")])
check("re-ordered choices with the same answer are not a change", kinds([q("Q1")], [q("Q1", texts=("b", "a", "c", "d"), correct=("B",))]) == [])
check("domain", kinds([q("Q1")], [q("Q1", dom="D2", task="T2.1")]) == [("Q1", "domain")])
check("explanation", kinds([q("Q1")], [q("Q1")], {"Q1": "x"}, {"Q1": "y"}) == [("Q1", "explanation")])
check("unchanged is silent", kinds([q("Q1")], [q("Q1")], {"Q1": "x"}, {"Q1": "x"}) == [])
imp = lambda ch: changes._entry("d", 1, "X", "Q1", ch)["important"]
check("important kinds", all(imp(c) for c in ("answer", "stem", "choices", "domain", "removed", "lastDay", "exam-added")) and not imp("explanation") and not imp("added"))

spec = lambda **k: {"vendor": "aws", "level": "associate", "domains": [{"code": "D1", "name": "n", "weight": 100}], **k}
d = lambda old, new: sorted((e["exam"], e["change"]) for e in changes.diff_specs(old, new, "d", 1))
check("exam added / removed", d({}, {"A": spec()}) == [("A", "exam-added")] and d({"A": spec()}, {}) == [("A", "exam-removed")])
check("lastDay", d({"A": spec()}, {"A": spec(lastDay="2026-12-31")}) == [("A", "lastDay")])
check("domain weights", d({"A": spec()}, {"A": spec(domains=[{"code": "D1", "name": "n", "weight": 90}])}) == [("A", "domains")])

files = sorted((ROOT / "data" / "changes").glob("*.json"))
for f in files:
    data = json.load(open(f, encoding="utf-8"))
    good = isinstance(data, list) and data and all(
        isinstance(e, dict) and set(e) == {"date", "pr", "exam", "id", "change", "important", "note"}
        and re.fullmatch(r"\d{4}-\d{2}-\d{2}", e["date"]) and e["pr"] == int(f.stem) and e["change"] in changes.CHANGES
        and e["important"] == (e["change"] in changes.IMPORTANT) and (e["id"] is None) == e["change"].startswith("exam-") | (e["change"] in ("lastDay", "domains"))
        for e in data)
    check(f"{f.name} is well formed", good)
print(f"{ok}/{ok + fail} passed"); sys.exit(1 if fail else 0)
