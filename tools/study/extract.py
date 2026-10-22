"""Import the day-by-day study curricula from the old study-tracker pages into data/study/<EXAM>.json.

One-off migration (2026-10): each tracker page embedded its curriculum as
<script type="application/json" id="curriculum-data">. Point this at a folder holding one
<EXAM>/index.html per tracker:

    python3 tools/study/extract.py <tracker_dir>

Kept: title, domain, services, concepts, exam points, quiz (2 per day) and the one-line recap.
Dropped: hands-on steps and progress state. Domains become the repo's D1..Dn codes (the order
in data/exam-specs.json) so a day can link to the matching question-bank filter; the final
review day has domain null. After this migration data/study/ is the source of truth.
"""
import html, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
DATA = ROOT / "data"
OUT = DATA / "study"

# DEA-C01's tracker used names instead of d1..d4.
NAMED = {"ingest": "D1", "store": "D2", "ops": "D3", "security": "D4"}


def domain_code(raw, n_domains):
    if raw == "final":
        return None
    code = NAMED.get(raw) or re.fullmatch(r"d(\d+)", raw) and f"D{raw[1:]}"
    if not code or int(code[1:]) > n_domains:
        raise ValueError(f"unknown domain {raw!r}")
    return code


def clean(text):
    return html.unescape(text).strip()


def convert(code, page, spec):
    m = re.search(r'<script type="application/json" id="curriculum-data">(.*?)</script>', page, re.S)
    if not m:
        raise ValueError("no curriculum-data block")
    days = []
    for i, d in enumerate(json.loads(m.group(1)), 1):
        if d["day"] != i:
            raise ValueError(f"day {d['day']} out of order")
        quiz = []
        for q in d["quiz"]:
            if not 0 <= q["answer"] < len(q["choices"]):
                raise ValueError(f"day {i}: answer index out of range")
            quiz.append({"q": clean(q["q"]), "choices": [clean(c) for c in q["choices"]],
                         "answer": q["answer"], "explain": clean(q["explain"])})
        days.append({
            "day": i,
            "domain": domain_code(d["domain"], len(spec["domains"])),
            "title": clean(d["title"]),
            "services": [clean(s) for s in d["services"]],
            "concepts": [{"heading": clean(c["heading"]), "body": clean(c["body"])} for c in d["concepts"]],
            "examPoints": [clean(p) for p in d["examPoints"]],
            "quiz": quiz,
            "recap": clean(d["recap"]),
        })
    return {"exam": code, "days": days}


def main(src):
    specs = json.loads((DATA / "exam-specs.json").read_text(encoding="utf-8"))
    OUT.mkdir(exist_ok=True)
    for folder in sorted(pathlib.Path(src).iterdir()):
        code = folder.name
        if code not in specs:
            raise SystemExit(f"{code}: not in exam-specs.json")
        doc = convert(code, (folder / "index.html").read_text(encoding="utf-8"), specs[code])
        (OUT / f"{code}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{code}: {len(doc['days'])} days")


if __name__ == "__main__":
    main(sys.argv[1])
