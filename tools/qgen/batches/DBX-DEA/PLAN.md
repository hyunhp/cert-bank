# DBX-DEA batch plan (topics owned per batch)
Exam: Databricks Certified Data Engineer Associate, guide read 2026-10-31. Target 225 (D1 14, D2 47, D3 50, D4 36, D5 22, D6 22, D7 34). Rules and
facts: `tools/qgen/DATABRICKS.md`. SINGLE ANSWER ONLY (no "Select TWO"). Technical scenario stems; short SQL/PySpark snippets allowed. Before writing,
read the published questions of the exam (`data/DBX-DEA.json`) and use new scenarios. Shared hot spots belong to ONE batch only; others may use them as distractors.

| Batch | Tasks | Count | Owns | Leave to |
|---|---|---|---|---|
| b01 | D1 (T1.1-T1.2) 14, T5.1 5, T5.2 5 | 24 | platform architecture, Delta Lake (ACID, time travel), Unity Catalog basics, compute choice (serverless, all-purpose vs jobs, SQL warehouse, single node); Git folders workflow; bundle variables and target overrides | bundle deploy and CLI (b06) |
| b02 | T2.1, T2.2, T2.3 | 24 | batch vs streaming vs incremental patterns, COPY INTO (idempotent, options), Auto Loader (directory listing vs file notification, schema enforcement/evolution, checkpoints) | connectors and method choice (b03) |
| b03 | T2.4, T2.5, T2.6, T2.7 | 23 | Lakeflow Connect standard/managed connectors, JDBC/ODBC/REST ingestion, choosing between ingestion methods, semi-structured and unstructured data (JSON, nested, variant-style handling) | COPY INTO / Auto Loader mechanics (b02) |
| b04 | T3.1, T3.2, T3.3 | 25 | bronze to silver cleaning, joins (inner, left, broadcast, cross, multi-key), union vs union all, columns/rows (explode, rename, split, filter) | dedupe/aggregation, tuning, gold, quality (b05) |
| b05 | T3.4, T3.5, T3.6, T3.7 | 25 | deduplication and aggregates (approx_count_distinct, summary), tuning parameters (shuffle partitions, autoBroadcastJoinThreshold, memory), gold objects (materialized views, views, streaming tables, tables), data quality checks/expectations | cleaning and joins (b04) |
| b06 | T4.1, T4.2, T5.3, T5.4 | 30 | Lakeflow Jobs retries, conditional tasks, branching/looping, task types (notebook, SQL, dashboard, pipeline) and dependencies (T4: 18); bundle deployment across dev/test/prod, Databricks CLI validate/deploy (T5: 12) | schedules/triggers (b07) |
| b07 | T4.3, T4.4, T6.1, T6.2 | 26 | schedules and trigger types (scheduled, file arrival, table update), time-based vs data-driven (T4: 18); run history trends, job statuses, task graph, failure rates (T6: 8) | bottlenecks and diagnosis (b08) |
| b08 | T6.3, T6.4, T6.5, T7.1, T7.2 | 28 | Spark UI (skew, shuffle, spill), Liquid Clustering, predictive optimization, startup failures, library conflicts, OOM (T6: 14); managed vs external tables and conversion, GRANT/REVOKE/DENY hierarchy (T7: 14) | masking, row-level, ABAC (b09) |
| b09 | T7.3, T7.4 | 20 | column masking, row filters, row-level security by group, Unity Catalog ABAC policies (check each doc page for Preview status; key only what is GA) | tables and grants (b08) |

Waves (about 4 writers at a time): b01, b02, b04, b06; then b03, b05, b07, b08, b09.
