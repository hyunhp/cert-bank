# DBX-DEP study guide plan (25 days)
Rules: `tools/study/README.md` (data shape) and `tools/qgen/DATABRICKS.md` (DBX-DEP + DBX-DEA sections: names, Beta/Preview kept out). Sources: exam guide tasks in `data/exam-tasks.json` ("DBX-DEP") and docs.databricks.com only (`python3 tools/learn_fetch.py --grep "<terms>" <url>`, shared cache). Built from the reviewed bank (`data/DBX-DEP.json`, `data/explanations/DBX-DEP.json`) plus the docs; keep claims the bank already verified, re-check anything new yourself (earlier writers still had ~15 unchecked claims each).
Professional depth: DBX-DEA guide (`data/study/DBX-DEA.json`) already teaches fundamentals; do not repeat it, build on it.
Shape per day: see `data/study/DBX-DEA.json` and `data/study/GCP-PSE.json` (day, domain, title, services, concepts[{heading,body}], examPoints, quiz[2], recap).
3-4 concepts of 120-190 words, 3 examPoints, quiz = 2 questions with 4 choices, `answer` is a 0-3 integer index, correct choice never the longest, no letter references in explanations. `domain` is the string "D1".."D9" (`null` on the final day). Preview/Beta features stay out of keyed answers.

| Day | Domain | Tasks | Topic |
|---|---|---|---|
| 1 | D1 | T1.1, T1.2 | bundle project structure, modular Python code, dependency conflicts and install failures |
| 2 | D1 | T1.3 | UDFs: Pandas, Python, SQL and Unity Catalog functions |
| 3 | D1 | T1.4, T1.8 | Lakeflow Pipelines and Auto Loader streaming; Structured Streaming vs declarative pipelines |
| 4 | D1 | T1.6, T1.7 | streaming table vs materialized view; AUTO CDC (SCD 1 and 2) |
| 5 | D1 | T1.5, T1.9, T1.10 | Lakeflow Jobs via UI/API/CLI, control flow (If/Else, For Each), compute and dependency choices |
| 6 | D1 | T1.11, T1.12 | unit and integration tests; stateful Structured Streaming (watermarks, output modes, foreachBatch, checkpoints) |
| 7 | D2 | T2.1, T2.2 | ingest from message buses and cloud storage; incremental CDC with Delta or Iceberg targets |
| 8 | D2 | T2.3 | Lakeflow Connect CDC from relational databases |
| 9 | D2 | T2.4, T2.5 | OpenSharing and Clean Rooms; Lakehouse Federation with governance |
| 10 | D3 | T3.1 | advanced Spark SQL and PySpark transformations |
| 11 | D3 | T3.2, T3.3 | VARIANT; AI functions such as ai_query in pipelines |
| 12 | D3 | T3.4 | data quality expectations in Lakeflow Pipelines |
| 13 | D4 | T4.1 | system tables for cost, audit and workload monitoring |
| 14 | D4 | T4.2, T4.3 | REST/CLI/SDK monitoring; pipeline event logs |
| 15 | D4 | T4.4, T4.5 | Lakehouse alerts; Lakeflow Jobs UI and Jobs API monitoring |
| 16 | D5 | T5.1, T5.2 | managed tables, Predictive Optimization, Liquid Clustering overhead; Delta optimization by access pattern |
| 17 | D5 | T5.3, T5.4 | caching for repeated reads; Change Data Feed |
| 18 | D5 | T5.5, T5.6 | query profile bottlenecks; Liquid Clustering vs partitioning and ZORDER |
| 19 | D6 | T6.1, T6.2 | least-privilege ACLs; ABAC with governed tags |
| 20 | D6, D7 | T6.3-T6.5, T7.1, T7.2 | anonymization and pseudonymization, PII pipeline, purging; tags, comments, permission inheritance |
| 21 | D8 | T8.1 | diagnostics: Spark UI, logs, system tables, query profiles |
| 22 | D8 | T8.2 | repairs and parameter overrides |
| 23 | D8 | T8.3, T8.4 | bundle deployment; Git folders CI/CD |
| 24 | D9 | T9.1, T9.2 | table layout design; dimensional models, materialized views, Metric Views |
| 25 | null | all | final review: decision cheat-sheet across the 9 domains, 2 quiz questions |

(Day 20 mixes D6 and D7: set `domain` "D6" and name D7 in the title.)
Writers: w1 days 1-6, w2 days 7-12, w3 days 13-18, w4 days 19-25. Each writes ONLY `tools/study/drafts/DBX-DEP/wN.json` (a JSON list of day objects).
