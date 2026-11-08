# DBX-GAI batch plan (topics owned per batch)
Exam: Databricks Certified Generative AI Engineer Associate, guide (dated 2026-03-18) read 2026-11-08. Target 225 (D1 31, D2 31, D3 68, D4 50, D5 18, D6 27), about 15% multi-answer "(Select TWO)" (the guide lists multiple-selection).
Rules and facts: `tools/qgen/DATABRICKS.md` (DBX-GAI section and DBX-DEA rules). Header `@ DBX-GAI Dx Tx.y <level> <kind>` (two tokens after the task id, e.g. "applied use-case").
Before writing, grep the published Databricks questions (data/DBX-*.json) on the same topic. Shared hot spots belong to ONE batch; others may use them as distractors.

| Batch | Tasks (count) | Total | Owns |
|---|---|---|---|
| b01 | T1.1 (6), T1.2 (5), T1.3 (5), T1.4 (5), T1.5 (5) | 26 | - |
| b02 | T1.6 (5), T2.1 (4), T2.2 (4), T2.3 (4), T2.4 (4), T2.5 (4), T2.6 (4) | 29 | Agent Bricks (legacy/Beta status: check); chunking basics (owned here) |
| b03 | T2.7 (4), T2.8 (3), T3.1 (6), T3.2 (6), T3.3 (6), T3.4 (5) | 30 | advanced chunking (parent-child etc.); re-ranking (owned here); chunking choice from evaluation |
| b04 | T3.5 (5), T3.6 (5), T3.7 (5), T3.8 (5), T3.9 (5), T3.10 (5) | 30 | guardrails (functional; Gov owns masking/malicious input) |
| b05 | T3.11 (5), T3.12 (5), T3.13 (5), T4.1 (4), T4.2 (4), T4.3 (4) | 27 | MLflow + Agent Framework (owned here); evaluation vs monitoring; Genie / Conversation API |
| b06 | T4.4 (4), T4.5 (4), T4.6 (3), T4.7 (3), T4.8 (3), T4.9 (3), T4.10 (3), T4.11 (3), T4.12 (3) | 29 | create/query index (owned here); Vector Search concepts/components; ai_query batch (owned here); index sizing/endpoint types; Lakebase / persistent memory; CI/CD, prompt promotion |
| b07 | T4.13 (3), T4.14 (3), T4.15 (3), T5.1 (5), T5.2 (5), T5.3 (4), T5.4 (4) | 27 | MCP servers (owned here); prompt registry/versioning; masking (owned here); malicious input guardrails (owned here) |
| b08 | T6.1 (3), T6.2 (3), T6.3 (3), T6.4 (3), T6.5 (3), T6.6 (3), T6.7 (3), T6.8 (2), T6.9 (2), T6.10 (2) | 27 | MLflow tracing/scoring; inference tables + Agent Monitoring; judges needing ground truth (owned here); AI Gateway (renamed Unity Gateway in docs: check); custom scorers (owned here); SME feedback / review app |

Waves (about 4 writers at a time): b01, b03, b05, b07; then b02, b04, b06, b08. Ingest each reviewed batch before the next review starts (reviewers replace duplicates of published questions).

Note: `qgen plan` rounds each domain on its own (half to even), so its per-domain "need" can differ by 1 from the largest-remainder counts above; this plan sums to exactly the target.
