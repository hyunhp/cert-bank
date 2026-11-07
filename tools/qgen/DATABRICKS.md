# Databricks exams — facts and writing rules

Read this before any `DBX-*` work. Facts come from the exam page, the exam guide PDF and docs.databricks.com only
(`python3 tools/learn_fetch.py --grep "<terms>" https://docs.databricks.com/aws/en/...`; cloud-neutral behavior, AWS path).
Vendor `databricks` (tab "Databricks"); exam codes have no official form, so this bank uses `DBX-`.

## DBX-DEA Databricks Certified Data Engineer Associate (added 2026-10-31)
Sources: https://www.databricks.com/learn/certification/data-engineer-associate and the guide
https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Data-Engineer-Associate-Exam-Guide-August-2026.pdf
(published 2026-05-04, updated 2026-08-06, read 2026-10-31; "check the guide two weeks before your exam").

| Item | Value |
|---|---|
| Questions | 45 scored multiple choice (+ up to 10 unscored), 90 min, USD 200, valid 2 years, no prerequisite |
| Pass mark | Not published. `passMarkUnpublished: true`; the mock aims at 80% |
| Sections | D1 Platform 6%, D2 Ingestion and Loading 21%, D3 Transformation and Modeling 22%, D4 Lakeflow Jobs 16%, D5 CI/CD 10%, D6 Troubleshooting/Monitoring/Optimization 10%, D7 Governance and Security 15% |
| Tasks | 33 (`data/exam-tasks.json`): 1.1-1.2, 2.1-2.7, 3.1-3.7, 4.1-4.4, 5.1-5.4, 6.1-6.5, 7.1-7.4 |
| Code | "SQL when possible; otherwise Python (PySpark)". Short snippets in stems are fine |
| Format | Single answer only in the guide's samples (multiple choice, no "select two"): this bank uses single answer only |

Writing rules:
- Block header: `@ DBX-DEA D2 T2.4 applied use-case` (a level word, then a type such as use-case, definition, troubleshooting, tradeoff, comparison).
- Technical, scenario-based, single-answer. Stems state the data situation and the requirement; short SQL/PySpark snippets (<=6 lines) allowed.
- Current names: Lakeflow Jobs, Lakeflow Declarative Pipelines, Lakeflow Connect (standard and managed connectors), Declarative Automation
  Bundles (formerly Databricks Asset Bundles), Databricks Git folders (formerly Repos), Unity Catalog, Auto Loader, COPY INTO, Liquid Clustering,
  predictive optimization, serverless SQL warehouse. Do not key old names (Workflows, Delta Live Tables, DAB, Repos) as the product; mention in G: once.
- Nothing preview, beta or deprecated in keys (check the docs page banner: "Public Preview", "Beta"); ABAC policies and newer governance features
  need their page checked. No prices, DBU rates, limits or runtime version numbers.
- Test the engineer's decision (which tool/option and why), not the click path; UI steps appear only as "in the Jobs UI you can see ...".
- Overlap: DEA-C01 (AWS) and PLTR-DE share data-engineering concepts; use Databricks specifics (Delta, Unity Catalog, Auto Loader) not generic ETL.

## DBX-DEP Databricks Certified Data Engineer Professional (added 2026-11-07)
Sources: https://www.databricks.com/learn/certification/data-engineer-professional and the guide
https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Data-Engineer-Professional-Exam-Guide-9-Oct-2026.pdf
(exam published and guide updated 2026-10-09, read 2026-11-07). The exam page still lists an older 10-section outline with other weights and says
59 scored questions; the guide (newer) says 60: this bank follows the guide.

| Item | Value |
|---|---|
| Questions | 60 scored multiple choice (+ unscored), 120 min, USD 200, valid 2 years, no prerequisite, 1 year hands-on recommended |
| Pass mark | Not published. `passMarkUnpublished: true`; the mock aims at 80% |
| Sections | D1 Developing Code for Data Processing using Python and SQL 23%, D2 Data Ingestion & Acquisition 12%, D3 Data Manipulation 12%, D4 Monitoring and Alerting 10%, D5 Cost & Performance Optimization 15%, D6 Ensuring Data Security and Compliance 8%, D7 Data Governance 5%, D8 Debugging and Deploying 10%, D9 Data Modeling 5% |
| Tasks | 45 (`data/exam-tasks.json`): 1.1-1.12, 2.1-2.5, 3.1-3.4, 4.1-4.5, 5.1-5.6, 6.1-6.5, 7.1-7.2, 8.1-8.4, 9.1-9.2 (one per outline bullet) |
| Format | Multiple choice, single answer only (as DBX-DEA; the guide's 6 samples are single answer) |

Writing rules (in addition to the DBX-DEA ones above):
- Professional depth: design and trade-off decisions in production pipelines (state, late data, CDC semantics, cost vs latency, governance at scale), short SQL/PySpark
  snippets (<=8 lines) allowed. Not syntax recall, not UI paths.
- Use the guide's current names: Lakeflow Pipelines / Spark Declarative Pipelines (formerly Delta Live Tables), AUTO CDC APIs (formerly APPLY CHANGES), Lakeflow Jobs,
  Lakeflow Connect, Declarative Automation Bundles (formerly Databricks Asset Bundles), Databricks Git folders (formerly Repos), OpenSharing (formerly Delta Sharing
  names in docs may differ: check), Metric Views, Predictive Optimization, Liquid Clustering, CLUSTER BY AUTO. Old names only in G: once.
- Nothing preview, beta or deprecated in keys: check every docs page banner. Likely Preview/Beta candidates here: ABAC policies, Lakehouse alerts, Metric Views,
  ai_query variants, Iceberg write support in Lakeflow Pipelines, Clean Rooms features, performance-mode settings. No prices, DBU rates, limits or runtime versions.
- Overlap: DBX-DEA (same platform, associate depth) already has Auto Loader, COPY INTO, Jobs, Unity Catalog basics, Git folders and bundles basics. Read its published
  questions first (grep data/DBX-DEA.json) and test the professional decision (when X over Y, what fails, how to repair). DEA-C01 and GCP-PDE share concepts, not products.
- Spark API pages (spark.apache.org) are reachable since 2026-11-06; use them for Structured Streaming semantics.
