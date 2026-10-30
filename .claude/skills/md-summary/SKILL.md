---
name: md-summary
description: >
  Compressed key-summary style for anything written into markdown files
  (TODO.md Now/DONE notes, handoffs, PR bodies, README rows, status reports).
  Use whenever you write or update a markdown note, or the user says
  "summarize", "압축 요약", "핵심만". Applies by default for markdown output.
---

# md-summary

Markdown notes hold only the compressed key points. Optimize every write for the next reader's warm start.

## Rules
- Lead with state: DONE / in progress / next. One line each, facts only.
- Keep: numbers (counts, dates), decisions and their reason, names of files/branches/ids, open gaps, rules learned.
- Drop: process narration, per-step history, obvious details, repeated context, adjectives, hedging.
- Size: a finished item = 1-3 lines (about 40 words per line max). A section gets shorter, never longer, when updated:
  merge or replace old lines instead of appending.
- Details live where they belong (git log, batch files, `tools/qgen/*.md`); link or name the path instead of copying.
- Lists and short fragments over paragraphs. No tables unless comparing 3+ items.
- Existing project rules still win (TODO.md "Now" must stay a warm start; keep `Updated <date>`).

## Check before saving
1. Can a reader resume from this alone? 2. Is every line a fact, decision, number or next step? 3. Can anything be cut or merged without losing (1)?
