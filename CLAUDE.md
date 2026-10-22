# cert-bank (formerly aws_qbank) — working notes for Claude Code

Static GitHub Pages site with original certification practice questions, grouped by vendor
(AWS, Palantir). The repo was renamed from `aws_qbank` on 2026-10-14; Pages now serves https://hyunhp.github.io/cert-bank/ and the old address no longer redirects. No build step: `index.html`, `js/*.js`, `data/*.json`, `diagrams/*.json`.
Explanations live apart from the questions: `data/<EXAM>.json` has none, `data/explanations/<EXAM>.json` is `{id: text}`
(qgen `load_exam`/`save_exam` merge and split them; the site fetches them on first reveal).
Section filter chips (domain/task, `#exam=X&d=D4&t=T4.1`), per-domain accuracy (localStorage only, not in the bookmark
backup) and the mock exam "one section only" option read `data/exam-specs.json`, `exam-domains.json` and
`exam-tasks.json` (English task names; keep it in step with `tools/qgen/tasks.json`).
Vendors: `exam-specs.json` gives each exam a `vendor`; `index.html` has `EXAMS` (code, name, vendor) and `VENDORS`
(the tabs). Exam codes are globally unique (Palantir codes start with `PLTR-`), so links, bookmarks and stats carry no
vendor. Keep the `aws_qbank_*` localStorage keys: renaming them would wipe every user's bookmarks and history.
Palantir exams publish a percent pass mark (`passingPct`) and no domain weights (`weightsAssumed`, equal weights).
**Before any `PLTR-*` work read `tools/qgen/PALANTIR.md`** (official facts and writing rules).
Open work items are in `TODO.md` — read it at the start of a session.
Study guide: `study.html` + `js/study.js` read `data/study/<EXAM>.json` (day-by-day plans, edited directly,
not through qgen) and mark terms from `data/glossary.json` with tap/hover popovers (EN + KO). See
`tools/study/README.md` for the glossary rules and the planned (unbuilt) backend design.
Donations: `support.html` holds the only copy of the payment links (`METHODS`; empty url = "coming soon").
KakaoPay links only open in the phone app (404 in desktop browsers): the card shows `assets/kakaopay-qr.svg` and is a
link only on phones/tablets (user-agent check, not pointer type). If the
link changes, regenerate it (`segno.make(url, error="m").save(path, scale=1, border=2)`).
The header link, the sticky top bars (question bank exam bar, study day bar), the bottom card in `index.html`, the study
page header and the mock exam results all point to it.

## Hard rules
- Never create files or folders the site reads whose names start with `_` (GitHub Pages/Jekyll
  drops them; `.nojekyll` is a safety net, not a license). Mock exam broke on 2026-09-26 because of this.
- Questions are added or changed only through batch files in `tools/qgen/batches/<EXAM>/bNN.txt`
  and `python3 tools/qgen/qgen.py ingest <file>`. Never hand-edit `data/<EXAM>.json`.
- `ingest` assigns question ids and rewrites shared data files: run it **one batch at a time,
  never in parallel**. Parallel work = writing batch files only.
- After editing `js/mock.js` run `python3 tools/stamp_version.py`.
- Never paste tokens into files or chat; push with the local git credential (gh auth / SSH).

## Batch format (see tools/qgen/qgen.py docstring)
```
@ EXAM Dx Tx.x basic|applied|advanced use-case|tradeoff|comparison|troubleshooting [+OTHER:Dy]
S: stem (multi-answer stems end with "(Select TWO)")
A:..D: (E: for multi)   K: A  or  K: A,C
W: why correct   X: B=... | C=... | D=...   T: takeaway   V: services (optional)
G: background (detailed explanation; required style for all new and rewritten explanations)
```
Detailed explanations (see `tools/qgen/batches/ANS-C01/e01.txt` for the reference style):
- `G:` teaches the concept a learner needs first: `## Heading` lines, short paragraphs, `- ` bullets,
  `code` for CIDRs/ARNs/commands, a concrete example. `G:`, `W:`, `X:` may span lines.
- `W:` and each `X:` entry start with a short option name then a colon (`B=VPC peering: ...`) and give
  the real reason it works or fails; one `X:` entry per line. `T:` is the one-sentence key idea.
- Multi-answer questions: `W:` has one entry per correct option, one per line, like `X:`
  (`W: A=Name: why` / `D=Name: why`).
- Never refer to options by letter in the text ("option B"): ingest reorders choices.
- Rewrite an existing question's explanation with an explain-only batch
  `tools/qgen/batches/<EXAM>/eNN.txt` using `@ Q001592 explain` blocks (G/W/X/T; X letters are the
  published letters). Ingest never replaces a detailed explanation with a short one.
Quality gates enforced by `qgen check`: schema, near-duplicates, length bias (correct answer
must not be clearly the longest option too often; write distractors as long and specific as the
answer), stem length. `python3 tools/qgen/length_bias.py <batch>` lists the questions to fix.

## Commands
- Plan gaps: `python3 tools/qgen/qgen.py plan <EXAM>`; status: `python3 tools/qgen/qgen.py report`
- Validate: `python3 tools/qgen/qgen.py check <batch>`; write: `... ingest <batch>`
- Tests (all must pass before commit):
  `node tools/mock_unit_test.mjs && python3 tools/study_test.py && python3 tools/mock_e2e_test.py && python3 tools/mock_link_test.py && python3 tools/bookmark_backup_test.py && python3 tools/loading_perf_test.py && python3 tools/domain_filter_test.py && python3 tools/vendor_tabs_test.py && python3 tools/support_test.py && python3 tools/diagrams/scroll_ui_test.py && python3 tools/diagrams/check.py && python3 tools/diagrams/site_test.py`
