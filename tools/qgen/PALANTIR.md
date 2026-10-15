# Palantir question rules (PLTR-*)

Read this before writing, reviewing or fixing any `PLTR-*` batch. It records what the official pages say
(checked 2026-10-14) and the rules this bank adds on top. Re-check the sources every few months: the
platform and the exams change quickly.

## Official facts the site mirrors
Sources: Associate exam guides at learn.palantir.com/page/associate-exam-guides, the certification
FAQ (learn.palantir.com/page/faqs) and Palantir's community announcement of the 2026 refresh.

| Item | Value |
|---|---|
| Current exams | Associate: Data Engineer, Application Developer (both refreshed), AI Engineer (new), live since 2026-08-03 |
| Format | Timed, open-book, multiple choice; certificates valid for two years |
| Data Engineer / AI Engineer | 95 questions, 3 hours, pass mark 70% correct, questions sequential, 8 domains each |
| Application Developer | 85 questions, 3 hours, pass mark 70% correct, questions sequential, 8 domains (read 2026-10-15) |
| Domain weights | Not published. This bank weights the 8 domains equally (`weightsAssumed` in `exam-specs.json`) |
| Retakes | 14-day wait after a fail; 11 months before retaking an exam you passed |
| Specialist level | Hands-on live exams in a real Foundry/AIP environment: out of scope for this bank |

Not confirmed, so never state them in questions or on the site as fact: whether "sequential" forbids going
back to earlier questions, whether open-book includes AI tools, and details of Foundry Aware.
All three guides were re-read on 2026-10-15: DE and AIE unchanged (95 q, 70%, no weights).

## Codes and task ids
- `PLTR-DE` (Data Engineer – Associate), `PLTR-AIE` (AI Engineer – Associate), `PLTR-APD` (Application Developer – Associate).
- Domains D1-D8 follow the guides' order and names exactly.
- The guides publish no task statements. Task ids (`T1.1` ...) are this bank's own split of each domain's
  bullets, recorded in `tools/qgen/tasks.json` and `data/exam-tasks.json`. They are unofficial.

## Writing rules
1. **Sources**: the official exam guide and palantir.com/docs only. Third-party practice sites and community
   posts are never a source for facts.
2. **Role boundary**: each guide has a "You own / You do not primarily own" table. The keyed answer stays inside
   the exam's own column; the other column is good material for distractors ("hand it to the ontology owner",
   "train a custom model").
3. **Judgement over trivia**: the guides reward choosing the simplest safe option from evidence. Prefer
   troubleshooting and tradeoff stems (target: troubleshooting 30%+, tradeoff ~20%), and distractors that the
   guides warn against: rebuild first, grant broad access, bigger model, longer prompt, more context, silent
   filters, overwrite production.
4. **No UI paths**: no menu names, button labels or click sequences unless palantir.com/docs shows them. Name
   products and concepts as the docs do (AIP Logic, Pipeline Builder, Workshop, Automate, markings, ...).
5. **Original wording**: the guides' practice scenarios may inspire a situation, but never reuse their sentences
   or their exact setup. Never reproduce real exam questions.
6. **Format**: single answer, four options. Multiple choice is the only confirmed format, so no "(Select TWO)"
   until a guide shows it.
7. **Explanations**: the same detailed G/W/X/T style as AWS batches. `G:` may cite the guide's own principle
   ("the exam guide asks you to ...") when it is the reason an answer wins.
8. **Review**: every batch is fact-checked by an independent reviewer against these rules before ingest.

## Facts checked against palantir.com/docs (2026-10-15 review)
- Transactions: an APPEND only adds files and **cannot modify existing files**; committing an APPEND that overwrote
  a file fails. UPDATE may overwrite. (data-integration/datasets)
- APPEND file syncs ingest files not yet ingested, **keyed by file path name**. (data-connection/file-based-syncs)
- Restricted views are built on a backing dataset and **cannot be used as an input for transforms**.
  (security/restricted-views)
- Markings are mandatory, conjunctive and propagate through transform and analysis logic; granular policies on
  restricted views are discretionary and do not propagate. (security/markings, security/access-control-propagation)
Fixed after this review (f01, pinned): Q004782, Q005038, Q005136, Q005264.
