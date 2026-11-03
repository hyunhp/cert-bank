"""Explanation rendering guard: python3 tools/explain_format_test.py
- A wrong option whose name holds a colon (kms:Encrypt, aws:SourceIp) keeps its name in the rendered explanation.
- No stored explanation has a wrong-option line with an empty name ("- ✗ **B.:** ...")."""
import glob, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools" / "qgen"))
import qgen

ok = fail = 0
def check(name, cond, info=""):
    global ok, fail
    if cond: ok += 1
    else: fail += 1; print("FAIL", name, info)

item = {"bg": "## Background\ntext", "keys": ["C"], "why": "Decrypt for consumers: reading needs kms:Decrypt.", "why_by": {},
        "wrong": {"A": "CreateGrant for the service principal: Kinesis uses the caller's permissions.",
                  "B": "kms:Encrypt for consumers: consumers only read and decrypt.",
                  "D": "Store the logs on large EBS volumes attached to a dedicated logging instance: EBS is priced per provisioned GB."},
        "take": "Key."}
text = qgen.rich_explanation(item, ["A", "B", "C", "D"])
lines = {l[4:6]: l for l in text.split("\n") if l.startswith("- ")}
check("name with a colon is kept", "**B. kms:Encrypt for consumers:** consumers only read" in text, text)
check("plain name still works", "**A. CreateGrant for the service principal:** Kinesis uses" in text)
check("long wrong-option name is kept", "**D. Store the logs on large EBS volumes attached to a dedicated logging instance:** EBS is priced" in text)
check("correct option label", "**C. Decrypt for consumers (correct):** reading needs" in text)

bad = []
for f in sorted(glob.glob(str(ROOT / "data" / "explanations" / "*.json"))):
    for qid, t in json.load(open(f, encoding="utf-8")).items():
        if isinstance(t, str) and any(re.match(r"^- ✗ \*\*[A-H]\.:\*\*", l) for l in t.split("\n")):
            bad.append((pathlib.Path(f).stem, qid))
check("no wrong-option line without a name", not bad, bad[:10])
print(f"{ok}/{ok + fail} passed"); sys.exit(1 if fail else 0)
