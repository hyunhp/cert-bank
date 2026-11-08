# DBX-DAA study guide plan (17 days)
Rules: `tools/study/README.md` (data shape) and `tools/qgen/DATABRICKS.md` (DBX-DAA + DBX-DEA sections: names, Beta/Preview kept out). Sources: exam guide tasks in `data/exam-tasks.json` ("DBX-DAA") and docs.databricks.com only (`python3 tools/learn_fetch.py --grep "<terms>" <url>`, shared cache). Built from the reviewed bank (`data/DBX-DAA.json`, `data/explanations/DBX-DAA.json`) plus the docs; keep claims the bank already verified, re-check anything new yourself (earlier writers still had ~15 unchecked claims each).
Analyst level: what a data analyst decides and does (queries, dashboards, Genie, sharing), not engineering depth. `data/study/DBX-DEA.json` covers the engineer side: do not repeat it.
Naming: OpenSharing (Delta Sharing in parentheses once), Genie Agents (Genie spaces), Genie Code (formerly Databricks Assistant), AI/BI Dashboards, Lakeflow pipelines. No Preview/Beta in keyed answers (custom Vega-Lite visualization, Genie Ontology, PostgreSQL connector, unique constraints, VACUUM lite, ABAC DENY/metastore policies).
Shape per day: see `data/study/DBX-DEA.json` and `data/study/DBX-DEP.json` (day, domain, title, services, concepts[{heading,body}], examPoints, quiz[2], recap).
3-4 concepts of 120-190 words, 3 examPoints, quiz = 2 questions with 4 choices, `answer` is a 0-3 integer index (spread the indexes: not all 2), correct choice never the longest, no letter references in explanations. `domain` is the string "D1".."D9" (`null` on the final day).

| Day | Domain | Tasks | Topic |
|---|---|---|---|
| 1 | D1 | T1.1-T1.3 | platform components, Catalog Explorer (catalogs, schemas, tables, views, certified tables, metric views, lineage), Marketplace |
| 2 | D2 | T2.1-T2.3 | discovering certified datasets, governed tags and lineage, SQL data cleaning (NULLs, invalid rows) |
| 3 | D3 | T3.1-T3.2 | ways to bring data in (S3, OpenSharing, API, Auto Loader, Lakeflow Connect, Marketplace), file upload |
| 4 | D4 | T4.1-T4.3 | Genie Code, SQL warehouse role, federated joins |
| 5 | D4 | T4.4, T4.8 | materialized views vs streaming tables vs dynamic views; managed and external tables |
| 6 | D4 | T4.5-T4.7 | aggregates, joins and set operations, sorting and filtering |
| 7 | D4, D5 | T4.9, T5.3 | time travel, Delta history for audit and comparison (title names both; domain "D4") |
| 8 | D5 | T5.1, T5.2, T5.6 | Photon, Query Insights and query profile, fixing a query |
| 9 | D5 | T5.4, T5.5 | query history and caching, Predictive Optimization and automatic Liquid Clustering |
| 10 | D6 | T6.1, T6.2 | building AI/BI dashboards, notebook and SQL editor visualizations |
| 11 | D6 | T6.3, T6.7 | parameters and filters, choosing visualization types |
| 12 | D6 | T6.4-T6.6 | sharing and embedding, scheduled refresh, alerts |
| 13 | D7 | T7.1, T7.2 | Genie purpose and components, creating Genie spaces |
| 14 | D7 | T7.3, T7.4 | Genie permissions and distribution, optimization and benchmarks |
| 15 | D8 | T8.1, T8.2 | star, snowflake, data vault, Medallion alignment |
| 16 | D9 | T9.1-T9.3 | Unity Catalog roles and sharing, three-level namespace, ownership and PII |
| 17 | null | all | final review: decision cheat-sheet across the 9 domains, weights from `data/exam-specs.json`, 2 quiz questions |

Writers: w1 days 1-5, w2 days 6-9, w3 days 10-14, w4 days 15-17. Each writes ONLY `tools/study/drafts/DBX-DAA/wN.json` (a JSON list of day objects).
