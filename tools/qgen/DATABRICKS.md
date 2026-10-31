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
- Technical, scenario-based, single-answer. Stems state the data situation and the requirement; short SQL/PySpark snippets (<=6 lines) allowed.
- Current names: Lakeflow Jobs, Lakeflow Declarative Pipelines, Lakeflow Connect (standard and managed connectors), Declarative Automation
  Bundles (formerly Databricks Asset Bundles), Databricks Git folders (formerly Repos), Unity Catalog, Auto Loader, COPY INTO, Liquid Clustering,
  predictive optimization, serverless SQL warehouse. Do not key old names (Workflows, Delta Live Tables, DAB, Repos) as the product; mention in G: once.
- Nothing preview, beta or deprecated in keys (check the docs page banner: "Public Preview", "Beta"); ABAC policies and newer governance features
  need their page checked. No prices, DBU rates, limits or runtime version numbers.
- Test the engineer's decision (which tool/option and why), not the click path; UI steps appear only as "in the Jobs UI you can see ...".
- Overlap: DEA-C01 (AWS) and PLTR-DE share data-engineering concepts; use Databricks specifics (Delta, Unity Catalog, Auto Loader) not generic ETL.
