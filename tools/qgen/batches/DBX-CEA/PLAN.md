# DBX-CEA batch plan (topics owned per batch)
Exam: Databricks Certified Context Engineer Associate, guide (dated 2026-07-29) read 2026-11-08. Target 225 (D1 36, D2 20, D3 45, D4 41, D5 29, D6 25, D7 29), about 15% multi-answer "(Select TWO)" (the guide lists multiple-selection).
Rules and facts: `tools/qgen/DATABRICKS.md` (DBX-CEA section and DBX-DEA rules). Header `@ DBX-CEA Dx Tx.y <level> <kind>` (two tokens after the task id, e.g. "applied use-case").
Before writing, grep the published Databricks questions (data/DBX-*.json) on the same topic. Shared hot spots belong to ONE batch; others may use them as distractors.

| Batch | Tasks (count) | Total | Owns |
|---|---|---|---|
| b01 | T1.1 (6), T1.2 (5), T1.3 (5), T1.4 (5), T1.5 (5) | 26 | failure modes poisoning/distraction/confusion/clash (owned here) |
| b02 | T1.6 (5), T1.7 (5), T2.1 (5), T2.2 (5), T2.3 (5) | 25 | reasoning modes; Genie space instructions/trusted assets (owned here) |
| b03 | T2.4 (5), T3.1 (5), T3.2 (5), T3.3 (5), T3.4 (5) | 25 | UC metadata (comments, tags) for accuracy; Genie space curation; AI Search configuration diagnosis; RAG over UC volumes |
| b04 | T3.5 (5), T3.6 (5), T3.7 (5), T3.8 (5), T3.9 (5) | 25 | pre-inference vs JIT retrieval (owned here); authoritative vs derived assets |
| b05 | T4.1 (6), T4.2 (5), T4.3 (5), T4.4 (5), T4.5 (5) | 26 | memory types (owned here); Lakebase retrieval: AI Search vs SQL |
| b06 | T4.6 (5), T4.7 (5), T4.8 (5), T5.1 (5), T5.2 (5) | 25 | Lakebase durable memory configuration; progressive disclosure (owned here) |
| b07 | T5.3 (5), T5.4 (5), T5.5 (5), T5.6 (4), T6.1 (5) | 24 | Agent Skills |
| b08 | T6.2 (5), T6.3 (5), T6.4 (5), T6.5 (5), T7.1 (5) | 25 | compaction prompt tuning (owned here); aggressive vs conservative compaction |
| b09 | T7.2 (5), T7.3 (5), T7.4 (5), T7.5 (5), T7.6 (4) | 24 | dispatch with full traces (owned here); orchestrator context load |

Waves (about 4 writers at a time): b01, b03, b05, b07; then b09; then b02, b04, b06, b08. Ingest each reviewed batch before the next review starts (reviewers replace duplicates of published questions).

Note: `qgen plan` rounds each domain on its own (half to even), so its per-domain "need" can differ by 1 from the largest-remainder counts above; this plan sums to exactly the target.
