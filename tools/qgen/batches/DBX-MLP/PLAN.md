# DBX-MLP batch plan (topics owned per batch)
Exam: Databricks Certified Machine Learning Professional, guide (dated 2025-09-30) read 2026-11-08. Target 295 (D1 130, D2 130, D3 35), single answer only (the guide lists multiple choice only: no "Select TWO").
Rules and facts: `tools/qgen/DATABRICKS.md` (DBX-MLP section and DBX-DEA rules). Header `@ DBX-MLP Dx Tx.y <level> <kind>` (two tokens after the task id, e.g. "applied use-case").
Before writing, grep the published Databricks questions (data/DBX-*.json) on the same topic. Shared hot spots belong to ONE batch; others may use them as distractors.

| Batch | Tasks (count) | Total | Owns |
|---|---|---|---|
| b01 | T1.1 (6), T1.2 (6), T1.3 (6), T1.4 (6) | 24 | SparkML vs single node (owned here) |
| b02 | T1.5 (6), T1.6 (6), T1.7 (6), T1.8 (6) | 24 | SparkML vs single-node model for batch/real-time/streaming inference |
| b03 | T1.9 (6), T1.10 (6), T1.11 (6), T1.12 (6) | 24 | Optuna + MlflowSparkStudy (verify class names in docs); Ray on Databricks (Ray Tune) |
| b04 | T1.13 (6), T1.14 (6), T1.15 (6), T1.16 (6), T1.17 (6) | 30 | Ray vs Spark comparison; applyInPandas / mapInPandas group-wise models; nested runs |
| b05 | T1.18 (6), T1.19 (6), T1.20 (6), T1.21 (5), T1.22 (5) | 28 | point-in-time lookups (timeseries keys); online feature stores (formerly online tables; Lakebase-backed); on-demand features / feature serving |
| b06 | T2.1 (7), T2.2 (7), T2.3 (7), T2.4 (7) | 28 | deploy-code strategy (owned here; aliases); unit vs integration tests per stage |
| b07 | T2.5 (7), T2.6 (7), T2.7 (7), T2.8 (7) | 28 | integration test design (owned here); bundle ML resources (owned here) |
| b08 | T2.9 (7), T2.10 (7), T2.11 (6), T2.12 (6) | 26 | retraining triggers; model selection in retraining (metrics, calibration); drift statistical tests |
| b09 | T2.13 (6), T2.14 (6), T2.15 (6), T2.16 (6), T2.17 (6) | 30 | monitor types snapshot/time series/inference; inference-table performance trends |
| b10 | T2.18 (6), T2.19 (6), T2.20 (6), T3.1 (7) | 25 | custom metrics; endpoint health metrics; canary vs blue-green (owned here) |
| b11 | T3.2 (7), T3.3 (7), T3.4 (7), T3.5 (7) | 28 | traffic split in Model Serving (served entities); custom PyFunc + UC artifacts; query via REST / MLflow Deployments SDK (not ai_query) |

Waves (about 4 writers at a time): b01, b03, b05, b07; then b09, b11; then b02, b04, b06, b08; then b10. Ingest each reviewed batch before the next review starts (reviewers replace duplicates of published questions).
