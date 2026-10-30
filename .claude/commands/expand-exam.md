---
description: Generate N new questions for an exam with parallel writers, review, then ingest serially
argument-hint: <EXAM> <N>
---
Goal: add $ARGUMENTS (exam code and count) questions to the bank.

1. Run `python3 tools/qgen/qgen.py plan` for the exam and split the needed questions by
   domain into chunks of 25-30 (fewer, larger batches: every agent pays a fixed cost to read the rules). Pick the
   next free batch numbers under tools/qgen/batches/<EXAM>/.
2. Write `tools/qgen/batches/<EXAM>/PLAN.md` before launching anyone: for each batch, its tasks, the topics and
   scenarios it owns, and the shared hot spots it must leave to a named sibling (e.g. "structured outputs: b07 only",
   "MCP approval flow: b04 only"). Parallel writers otherwise drift into the same scenarios.
3. In ONE message, launch one `question-writer` subagent per batch in parallel, each with its exam, domain/task
   ids, count, batch path and its PLAN.md section. Writers work in this checkout and write only their own file.
4. Launch a `batch-reviewer` for each batch as soon as its writer finishes. Model choice: keep the default model for
   writers and fact-checking reviewers on fast-changing vendor facts; use `model: "sonnet"` for format-only work
   (length-bias or wording fixes, glossary or study-guide format checks).
5. Ingest each reviewed batch as soon as its review ends, ONE AT A TIME: `python3 tools/qgen/qgen.py ingest <batch>`.
   Then tell the reviewers still running what was just published, so overlaps are replaced before their check.
6. Run the full test command from CLAUDE.md. If all pass, commit with a message listing the
   batches and new counts. Do not push unless asked.
