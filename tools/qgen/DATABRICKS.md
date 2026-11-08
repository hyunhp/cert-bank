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

## DBX-DAA Databricks Certified Data Analyst Associate (added 2026-11-07)
Sources: https://www.databricks.com/learn/certification/data-analyst-associate and the guide
https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Data-Analyst-Associate-Exam-Guide-August-2026.pdf
(guide updated 2026-10-08, exam published 2026-10-19, read 2026-11-07). The guide still carries a template line ("[Author: list every section ...]"); the outline itself is complete.

| Item | Value |
|---|---|
| Questions | 45 scored multiple choice (+ up to 10 unscored), 90 min, USD 200, valid 2 years, no prerequisite, 6 months hands-on recommended |
| Pass mark | Not published. `passMarkUnpublished: true`; the mock aims at 80% |
| Sections | D1 Platform 11%, D2 Managing Data 8%, D3 Importing Data 5%, D4 Executing queries with Databricks SQL and SQL warehouses 20%, D5 Analyzing Queries 15%, D6 Dashboards and Visualizations 16%, D7 AI/BI Genie Agents (Genie spaces) 12%, D8 Data Modeling with Databricks SQL 5%, D9 Securing Data 8% |
| Tasks | 39 (`data/exam-tasks.json`): 1.1-1.3, 2.1-2.3, 3.1-3.2, 4.1-4.9, 5.1-5.6, 6.1-6.7, 7.1-7.4, 8.1-8.2, 9.1-9.3 (one per outline bullet) |
| Code | All SQL is ANSI SQL per the exam page; short snippets (<=6 lines) fine |
| Format | Single answer only (the guide's samples are single answer): this bank uses single answer only |

Writing rules (in addition to the DBX-DEA ones above):
- Analyst view, not engineer view: which query, view, table type, dashboard setting or Genie setting answers the business need. Test the decision, not the click path.
- Current names: Genie Code (Databricks Assistant), AI/BI Dashboards, AI/BI Genie Agents (Genie spaces; docs may still say "Genie spaces"), SQL warehouse (serverless, pro, classic),
  Lakeflow Declarative Pipelines, Lakeflow Connect, Unity Catalog metric views, Predictive Optimization, Liquid Clustering. Old names only in G: once.
- Preview/Beta check on every docs page banner. Likely candidates: Genie Agents features (benchmarks, channel apps, Trusted Assets variants), dashboard embedding, external lineage, Lakebase,
  metric views, governed tags, Lakeflow Connect connectors, Genie Code slash commands. No prices, DBU rates, limits or runtime versions.
- Overlap: DBX-DEA owns Auto Loader, COPY INTO, Jobs, Delta basics and Unity Catalog grants at engineer depth. Read its published questions first (grep data/DBX-DEA.json) and ask the analyst-side decision.

## DBX-MLA Databricks Certified Machine Learning Associate (added 2026-11-08)
Sources: https://www.databricks.com/learn/certification/machine-learning-associate and the guide
https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Machine-Learning-Associate-Exam-Guide-August-2026.pdf
(file name says August 2026 but the guide text is dated March 1, 2025 for publication and update, read 2026-11-08: its wording is older than the docs; docs win).

| Item | Value |
|---|---|
| Questions | 48 scored multiple-choice and multiple-selection (+ up to 10 unscored), 90 min, USD 200, valid 2 years, English/Japanese/pt-BR/Korean |
| Pass mark | Not published. `passMarkUnpublished: true`; the mock aims at 80% |
| Sections | D1 Databricks Machine Learning 38%, D2 Data Processing 19%, D3 Model Development 31%, D4 Model Deployment 12% |
| Tasks | 48 (`data/exam-tasks.json`): 1.1-1.18, 2.1-2.9, 3.1-3.15, 4.1-4.6 (one per outline bullet) |
| Format | The guide says multiple-selection exists: unlike DBX-DEA/DEP/DAA, about 15% of the bank is "(Select TWO)" |

Writing rules (in addition to the DBX-DEA ones above):
- ML-practitioner view: choose the right Databricks ML feature, metric, tuning method or deployment mode for a scenario; short Python (scikit-learn, Spark ML, MLflow) snippets <=8 lines allowed. Not API-name recall.
- Names change: check the docs for the current name before keying. Likely traps: workspace Feature Store (legacy) vs feature tables in Unity Catalog (current feature engineering); workspace model registry (legacy) vs Unity Catalog models with aliases (stages are legacy); "Delta Live Tables" is now Lakeflow Spark Declarative Pipelines; online tables / online feature stores have changed (check the banner); Mosaic AI Model Serving; Hyperopt status on recent ML runtimes (docs list Optuna, Ray Tune, Hyperopt: verify before keying); MLflow 3 vs MLflow 2 API differences.
- Nothing preview, beta or deprecated in keys (check each docs page banner). Where the guide asks about a legacy item (workspace registry, Hyperopt), key the documented current comparison and say in G: what is legacy. No prices, DBU rates, limits or runtime versions.
- Spark ML and scikit-learn facts (estimators/transformers, pipelines, CrossValidator, metrics) come from spark.apache.org and scikit-learn docs where reachable; math facts (bias-variance, metrics, number of models in grid x folds) are generally accepted definitions.
- Overlap: DBX-DEA has Unity Catalog, Jobs and Delta basics; DBX-DAA has SQL analysis. Test the ML decision, not platform trivia. AWS MLA-C02 shares ML concepts, not products.
