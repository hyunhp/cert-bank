"""Per-exam domain/task fields: python3 tools/data_scope_test.py
Every question in data/<EXAM>.json carries `examDomain` and `examTask`: its domain and task IN THAT EXAM. A question shared from another
exam keeps that exam's `domainCode`/`taskId` (the site maps them with exam-domains.json and exam-shared-tasks.json), so a reader of the
raw files must use these two fields. This checks they are present, valid for the exam, and equal to what the site computes."""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from testkit import Checker
D = ROOT / "data"
specs = {k: v for k, v in json.load(open(D / "exam-specs.json", encoding="utf-8")).items() if isinstance(v, dict) and "vendor" in v}
dmap = json.load(open(D / "exam-domains.json", encoding="utf-8"))
tmap = json.load(open(D / "exam-shared-tasks.json", encoding="utf-8"))

C = Checker(); check = C.check

for code, spec in sorted(specs.items()):
    path = D / f"{code}.json"
    if not path.exists():
        continue
    qs = json.load(open(path, encoding="utf-8"))
    doms = {d["code"] for d in spec["domains"]}
    missing, bad_dom, wrong_dom, wrong_task = [], [], [], []
    for q in qs:
        if "examDomain" not in q or "examTask" not in q:
            missing.append(q["id"]); continue
        primary = q["examCodes"][0]
        # the site's rules (index.html docDomain / docTask)
        want_d = q["domainCode"] if primary == code else dmap.get(q["id"], {}).get(code, q["domainCode"])
        want_t = q.get("taskId") if primary == code else (tmap.get(q["id"], {}).get(code) or (q.get("taskId") if spec.get("tasksFrom") == primary else None))
        if q["examDomain"] not in doms: bad_dom.append(q["id"])
        if q["examDomain"] != want_d: wrong_dom.append(q["id"])
        if q["examTask"] != want_t: wrong_task.append(q["id"])
        if q["examTask"] and not q["examTask"].startswith("T" + q["examDomain"][1:] + ".") and primary == code:
            wrong_task.append(q["id"])
    check(f"{code}: every question has examDomain and examTask", not missing, missing[:5])
    check(f"{code}: examDomain is a domain of {code}", not bad_dom, bad_dom[:5])
    check(f"{code}: examDomain follows the site's mapping", not wrong_dom, wrong_dom[:5])
    check(f"{code}: examTask follows the site's mapping", not wrong_task, wrong_task[:5])
sys.exit(C.exit())
