> **cert-bank note (2026-11-13):** these guides now live only here (`content/guides/{en,ko}/<slug>.html`); the
> blogger-publisher copy is frozen. Blog-specific steps below (`blogger_publish.py`, `make_images.py`, drafts on
> Blogger, the `practice questions` tag) no longer apply: publish by adding the slug to `PUBLISHED.txt` and running
> `python3 tools/site/build.py`. Diagrams: edit `diagrams/<slug>.json`, run `python3 tools/site/make_diagrams.py`
> (English only; mirror the change in the Korean file by hand). Covers stay on hyunhp.github.io/bdb-images (permanent).

> **Frozen 11/13 (owner):** the guides now live in cert-bank (`content/guides/{en,ko}/`), which is their only source.
> Do not edit this folder; send fixes to the cert-bank session. Last versions handed over: English f3881bc, Korean 5406067.

# Writing guides (owner decisions 11/11)

Guides are hand-written articles in this folder, published with `python blogger_publish.py --posts-dir guides --apply`
(drafts first; the owner reviews before anything goes public). They exist because AdSense rejected the site for
"low value content": they must add what the question bank does not have.

## Three kinds, three units

| Kind | Unit | Target |
|---|---|---|
| Exam study guide | one per exam (`guide-<exam>-...`) | 43 |
| Concept comparison | one per topic, tagged with every exam it serves (`compare-...`) | 20-40 |
| Common-mistake analysis | per exam for large exams, per vendor for small ones (`mistakes-...`) | 10-15 |

Priority: popular entry exams first (CLF-C02, DEA-C01, AZ-104, GCP-ACE, DBX-DEA, TF-TA004 ...), then exams with the
most questions. Two or three guides per batch, reviewed by the owner.

## Each guide

- The main text serves the exam candidate: scope, weights, study order, traps, practice links.
- No shared template: every guide gets its own structure, built around what is particular to that exam.
- Ground claims in the bank (`../hyunhp/cert-bank`: counts of questions, services, scenario types) and in the official
  exam guide; say where numbers come from; no number that cannot be checked.
- Tags: vendor, exam code(s), `study guide` (+ `comparison` / `common mistakes`), level and official cert labels.
  Never the `practice questions` tag.

## Cover and diagram (owner 11/12)

- Cover: a `<!-- Cover: BIG | small -->` line under the title (the title stays long for search). Big text: the exam
  code, or a short topic that fits one line at the one size all covers use; small text: one line, at most two.
  `python make_images.py --posts-dir guides` draws it and puts the <img> before the jump break; then
  `python make_images.py --publish`.
- Diagram: one per guide, `guides/diagrams/<id>.json` (flow, decide or layers; see `make_diagrams.py`), drawn as HTML
  so it reads on phones. `python make_diagrams.py` inserts it before the named heading. Content from the guide only.

## Beginner tips and "Going deeper" (owner 11/11)

Both layers, decided after weighing them (thesis: one article serves both readers and shows expertise; antithesis:
confusion, length, a template smell, accuracy risk; synthesis below):

- **Beginner tip**: at the exact point where beginners get stuck, as a concrete action ("build one VPC with two
  subnets by hand"), never generic advice. Visible, short. Style: `TIP_STYLE` below.
- **Going deeper**: a collapsed `<details>` box that explains *why* an exam rule holds (the mechanism behind it), for
  readers who already know the basics. Only what official documentation confirms. Not trivia beyond the exam.
- One to three of each per guide, placed where the content calls for them; no fixed positions, never the same set of
  boxes in every guide.
- The owner's own perspective and experience, when given, goes in as a first-person "From experience" note.

```html
<p style="margin:16px 0;padding:12px 16px;border-left:4px solid #c9952e;background:#fbf3e2;border-radius:8px">
<strong>Beginner tip:</strong> ...</p>

<details style="margin:16px 0;padding:12px 16px;border:1px solid #d9d4ec;border-radius:10px;background:#f6f4fb">
<summary style="cursor:pointer;font-weight:700;color:#5b4b9e">Going deeper: ...</summary>
<p>...</p></details>
```
