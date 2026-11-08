# DBX-MLA batch plan (topics owned per batch)
Exam: Databricks Certified Machine Learning Associate, guide (text dated 2025-03-01) read 2026-11-08. Target 240 (D1 91, D2 46, D3 74, D4 29), about 15% multi-answer "(Select TWO)".
Rules and facts: `tools/qgen/DATABRICKS.md` (DBX-MLA section and DBX-DEA rules). Header `@ DBX-MLA Dx Tx.y <level> <kind>` (two tokens after the task id, e.g. "applied use-case").
Before writing, grep the published DBX-DEA/DEP/DAA questions on the same topic. Shared hot spots belong to ONE batch; others may use them as distractors.

| Batch | Tasks (count) | Total | Owns |
|---|---|---|---|
| b01 | T1.1 (6), T1.2 (5), T1.3 (5), T1.4 (5), T1.5 (5) | 26 | MLOps strategy (environments, code vs model promotion basics); ML runtime advantages; AutoML model/feature selection and benefits (generated notebooks, glass box); UC feature tables vs workspace feature tables |
| b02 | T1.6 (5), T1.7 (5), T1.8 (5), T1.9 (5), T1.10 (5) | 25 | create and write feature tables in UC (primary keys, timeseries, merge/overwrite); train with feature lookups (create_training_set); batch scoring with score_batch; online vs offline tables (owned here) |
| b03 | T1.11 (5), T1.12 (5), T1.13 (5), T1.14 (5), T1.15 (5) | 25 | MLflow Client API (search_runs, best run); manual logging (params, metrics, artifacts, models, autolog vs manual); MLflow UI; register model in UC; UC registry vs workspace registry |
| b04 | T1.16 (5), T1.17 (5), T1.18 (5), T2.1 (6), T2.2 (5) | 26 | promote code vs models (owned here); model tags; aliases champion/challenger; summary statistics (.summary(), dbutils.data.summarize); outlier removal (std dev, IQR) |
| b05 | T2.3 (5), T2.4 (5), T2.5 (5), T2.6 (5), T2.7 (5) | 25 | visualizations; comparing features (correlation, chi-square, t-test and similar); imputation choice (mean/median/mode) and Imputer; one-hot encoding basics |
| b06 | T2.8 (5), T2.9 (5), T3.1 (5), T3.2 (5), T3.3 (5), T3.4 (5) | 30 | one-hot suitability (trees, high cardinality); log transform; algorithm selection; imbalance mitigation; estimators vs transformers; Spark ML pipelines |
| b07 | T3.5 (5), T3.6 (5), T3.7 (5), T3.8 (5), T3.9 (5) | 25 | tuning: Hyperopt fmin / SparkTrials (verify current status), search strategies, parallelizing single-node models; cross-validation trade-offs and fitting |
| b08 | T3.10 (5), T3.11 (5), T3.12 (5), T3.13 (5), T3.14 (5), T3.15 (4) | 29 | number of models in grid x folds; classification and regression metrics; metric choice; exponentiating log targets; bias-variance and complexity |
| b09 | T4.1 (5), T4.2 (5), T4.3 (5), T4.4 (5), T4.5 (5), T4.6 (4) | 29 | batch vs real-time vs streaming serving; custom model endpoints (Mosaic AI Model Serving); pandas/Spark batch inference; streaming inference with declarative pipelines; querying endpoints; traffic split |

Waves (about 4 writers at a time): b01, b03, b05, b07; then b02, b04, b06, b08; then b09. Ingest each reviewed batch before the next review starts (reviewers replace duplicates of published questions).
