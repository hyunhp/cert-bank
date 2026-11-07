# DBX-DAA batch plan (topics owned per batch)
Exam: Databricks Certified Data Analyst Associate, guide of 2026-10-08 read 2026-11-07. Target 225 (D1 25, D2 18, D3 11, D4 45, D5 34, D6 36, D7 27, D8 11, D9 18), single answer only.
Rules and facts: `tools/qgen/DATABRICKS.md` (DBX-DAA section and DBX-DEA rules). Header `@ DBX-DAA Dx Tx.y <level> <kind>` (two tokens after the task id, e.g. "applied use-case").
Before writing, grep the published DBX-DEA/DBX-DEP questions on the same topic and write analyst-side scenarios. Shared hot spots belong to ONE batch; others may use them as distractors.

| Batch | Tasks (count) | Total | Owns |
|---|---|---|---|
| b01 | T1.1 (10), T1.2 (10), T1.3 (5) | 25 | platform components (Mosaic AI, Lakeflow, Delta Lake, Unity Catalog, Databricks SQL, Lakebase); catalogs/schemas/managed vs external tables, views, certified tables, metric views, lineage in Catalog Explorer; Marketplace |
| b02 | T2.1 (5), T2.2 (6), T2.3 (7), T3.1 (8), T3.2 (3) | 29 | discover/query certified datasets; governed tags and lineage; SQL data cleaning (NULLs, invalid rows); ingestion approaches (S3, Delta Sharing, API, Auto Loader, Lakeflow Connect, Marketplace); UI file upload |
| b03 | T4.1 (8), T4.2 (5), T4.3 (5), T4.4 (8) | 26 | Genie Code (commands, debugging); SQL warehouse role (types, scaling, serverless); federated joins; materialized views vs streaming tables vs dynamic views (owned here) |
| b04 | T4.5 (5), T4.6 (6), T4.7 (2), T4.8 (4), T4.9 (2), T5.1 (5) | 24 | aggregates (approx_count_distinct, summary stats); joins and set ops; sort/filter; managed vs external tables; time travel and VACUUM (owned here); Photon |
| b05 | T5.2 (7), T5.3 (5), T5.4 (5), T5.5 (8) | 25 | Query Insights and query profile; Delta history for audit and comparison (DESCRIBE HISTORY, RESTORE); query history and caching; Predictive Optimization and automatic Liquid Clustering (owned here) |
| b06 | T5.6 (4), T6.1 (8), T6.2 (4), T6.3 (5), T6.4 (6) | 27 | fix a query; AI/BI dashboard build (pages, datasets, widgets); notebook/SQL editor visualizations; parameters; sharing, links and embedding |
| b07 | T6.5 (3), T6.6 (4), T6.7 (6), T7.1 (5), T7.2 (9) | 27 | dashboard refresh schedules; SQL alerts (owned here); choosing visualization types; Genie purpose and components; creating Genie spaces (sample questions, instructions, warehouse, Trusted Assets) |
| b08 | T7.3 (6), T7.4 (7), T8.1 (7), T8.2 (4) | 24 | Genie permissions and distribution; Genie optimization (monitoring, feedback, benchmarks, metadata); star/snowflake/data vault; Medallion alignment |
| b09 | T9.1 (8), T9.2 (4), T9.3 (6) | 18 | Unity Catalog roles/grants and sharing settings; three-level namespace; table ownership and PII protection |

Waves (about 4 writers at a time): b01, b03, b05, b07; then b02, b04, b06, b08; then b09. Ingest each reviewed batch before the next review starts (reviewers replace duplicates of published questions).
