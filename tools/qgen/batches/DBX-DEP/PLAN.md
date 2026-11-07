# DBX-DEP batch plan (topics owned per batch)
Exam: Databricks Certified Data Engineer Professional, guide of 2026-10-09 read 2026-11-07. Target 300 (D1 69, D2 36, D3 36, D4 30, D5 45, D6 24, D7 15, D8 30, D9 15), single answer only.
Rules and facts: `tools/qgen/DATABRICKS.md` (DBX-DEP section and DBX-DEA rules). Header `@ DBX-DEP Dx Tx.y <level> <kind>` (two tokens after the task id, e.g. "applied use-case").
Before writing, grep the published DBX-DEA questions (data/DBX-DEA.json) on the same topic and use professional-depth, new scenarios. Shared hot spots belong to ONE batch; others may use them as distractors.

| Batch | Tasks (count) | Total | Owns |
|---|---|---|---|
| b01 | T1.1 (6), T1.2 (5), T1.3 (5), T1.4 (8), T1.5 (4) | 28 | bundle project structure and modular code; dependency conflicts across serverless/pipeline/bundle; UDFs (Pandas, Python, SQL, UC functions); streaming pipelines with Lakeflow Pipelines + Auto Loader; Jobs via UI/API/CLI |
| b02 | T1.5 (1), T1.6 (6), T1.7 (7), T1.8 (6), T1.9 (5), T1.10 (3) | 28 | streaming table vs materialized view; AUTO CDC with SCD 1/2 (owned here); Structured Streaming vs declarative pipelines; Jobs control flow (If/Else, For Each); compute and serverless config (part) |
| b03 | T1.10 (2), T1.11 (4), T1.12 (7), T2.1 (8), T2.2 (7) | 28 | compute (rest); unit/integration tests (assertDataFrameEqual etc.); Structured Streaming state: watermarks, output modes, foreachBatch, checkpoints (owned here); ingestion of formats from Kafka/Kinesis/Pub/Sub/cloud storage; incremental CDC with Delta or Iceberg targets |
| b04 | T2.3 (8), T2.4 (6), T2.5 (7), T3.1 (7) | 28 | Lakeflow Connect CDC from SQL Server/MySQL/PostgreSQL; OpenSharing (D2D, D2O) and Clean Rooms; Lakehouse Federation with UC permissions; window functions, joins, aggregations (part) |
| b05 | T3.1 (3), T3.2 (8), T3.3 (8), T3.4 (10) | 29 | transformations (rest); VARIANT; AI functions incl. ai_query; data quality expectations (quarantine, drop, fail) |
| b06 | T4.1 (7), T4.2 (5), T4.3 (7), T4.4 (6), T4.5 (3) | 28 | system tables (owned here); REST/CLI/SDK monitoring; pipeline event logs; Lakehouse alerts; Jobs UI/API monitoring (part) |
| b07 | T4.5 (2), T5.1 (7), T5.2 (9), T5.3 (6), T5.4 (4) | 28 | Jobs monitoring (rest); managed tables, Predictive Optimization, Liquid Clustering overhead; deletion vectors, Liquid Clustering, CLUSTER BY AUTO choice; Delta cache; Change Data Feed (part) |
| b08 | T5.4 (3), T5.5 (8), T5.6 (8), T6.1 (5), T6.2 (4) | 28 | CDF (rest); query profile bottlenecks (skew, shuffle, join strategy, data skipping); Liquid Clustering vs partitioning/ZORDER (owned here); least-privilege ACLs; ABAC with governed tags (part) |
| b09 | T6.2 (1), T6.3 (4), T6.4 (5), T6.5 (5), T7.1 (7), T7.2 (6) | 28 | ABAC (rest); anonymization/pseudonymization; compliant PII pipeline; purging (GDPR erasure with Delta/UC: VACUUM, deletion vectors, retention); tags and comments; permission inheritance (part) |
| b10 | T7.2 (2), T8.1 (9), T8.2 (7), T8.3 (7), T8.4 (3) | 28 | inheritance (rest); diagnostics with Spark UI/logs/system tables/query profile; job repairs and parameter overrides; deployment with bundles (deploy side; project structure is b01); Git folders CI/CD (part) |
| b11 | T8.4 (4), T9.1 (7), T9.2 (8) | 19 | Git folders CI/CD (rest); table layout design (partitioning to data grain, clustering, compaction); dimensional models, materialized views, Metric Views |

Waves (about 4 writers at a time): b01, b03, b05, b07; then b02, b04, b06, b08; then b09, b10, b11. Ingest each reviewed batch before the next review starts (reviewers replace duplicates of published questions).
