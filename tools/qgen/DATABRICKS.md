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

## DBX-MLP Databricks Certified Machine Learning Professional (added 2026-11-08)
Sources: https://www.databricks.com/learn/certification/machine-learning-professional and the guide
https://www.databricks.com/sites/default/files/2026-10/databricks-certified-machine-learning-professional-exam-guide-august-2026.pdf
(guide text dated 2025-09-30 for publication and update although the file name says August 2026, read 2026-11-08; docs win over older guide wording).

| Item | Value |
|---|---|
| Questions | 59 scored multiple choice (+ up to 10 unscored), 120 min, USD 200, valid 2 years, English only, 1 year hands-on recommended |
| Pass mark | Not published. `passMarkUnpublished: true`; the mock aims at 80% |
| Sections | D1 Model Development 44%, D2 MLOps 44%, D3 Model Deployment 12% |
| Tasks | 47 (`data/exam-tasks.json`): 1.1-1.22, 2.1-2.20, 3.1-3.5 (one per outline bullet; D1 = Spark ML 1.1-1.7, Scaling and Tuning 1.8-1.14, Advanced MLflow 1.15-1.17, Feature Store 1.18-1.22; D2 = lifecycle 2.1-2.2, testing 2.3-2.6, environments 2.7-2.8, retraining 2.9-2.10, drift and monitoring 2.11-2.20) |
| Format | Single answer only (the guide lists multiple choice; all 10 samples are single answer): this bank uses single answer only |

Writing rules (in addition to the DBX-DEA and DBX-MLA ones above):
- Professional ML-engineer depth: choose the design (SparkML vs single node, Optuna vs Ray vs Spark, deploy code vs deploy models, snapshot vs time series vs inference monitor, canary vs blue-green) and say what fails or what to fix. The guide samples are scenario stems of 3-6 lines with four long options; match that. Short Python snippets <=8 lines.
- Names to verify in docs before keying: "Lakehouse Monitoring" is now documented as data profiling (the guide still says Lakehouse Monitoring); online tables are now Databricks Online Feature Stores, powered by Lakebase (check the SDK class names); AI Gateway is documented as Unity Gateway (AI Gateway-enabled inference tables replace the legacy endpoint inference tables); Databricks Asset Bundles are Declarative Automation Bundles (bundle resource keys `experiments`, `registered_models`, `model_serving_endpoints`); Feature Store means the Unity Catalog one (workspace Feature Store is deprecated). Old names only in G: once.
- Key only what the docs page shows today: Optuna with `MlflowSparkStudy` (docs page "Hyperparameter tuning with Optuna"), Ray on Databricks, Hyperopt is only a comparison distractor (not on the guide); route optimization and served-entity traffic split for rollouts; `mlflow.deployments` client `predict` vs REST (not `ai_query`, which is SQL batch). Point-in-time joins (timeseries keys), on-demand features (Python UDFs registered in Unity Catalog) and feature serving come from the Feature Store pages.
- Statistical drift tests, calibration/log loss, bias-variance and Spark ML definitions are generally accepted math: no doc needed, but name the exact Lakehouse Monitoring drift metric only after checking the "drift metrics table" in the data profiling docs.
- Nothing preview, beta or deprecated in keys. No prices, DBU rates, limits or runtime versions.
- Overlap: DBX-MLA owns AutoML, UC feature table basics, MLflow basics, aliases and basic serving. Read its published questions first (grep data/DBX-MLA.json) and ask the professional decision, not the associate recall.
- Preview/Beta check (docs pages, 2026-11-08): Optuna page, Ray on Databricks index, route optimization, serve-multiple-models, online feature stores and bundle resources show no Preview/Beta label. Online Feature Stores are now created as Lakebase Autoscaling projects. Lakebase page lists some items as Public Preview (Postgres changes as Delta): not needed here. Note the fetch tool keeps banner labels (it showed "Beta"/"Legacy" on other pages), so absence means no banner.

## DBX-GAI Databricks Certified Generative AI Engineer Associate (added 2026-11-08)
Sources: https://www.databricks.com/learn/certification/genai-engineer-associate and the guide
https://www.databricks.com/sites/default/files/2026-10/databricks-certified-gen-ai-associate-exam-guide-august-2026.pdf
(published and updated 2026-03-18, read 2026-11-08).

| Item | Value |
|---|---|
| Questions | 45 scored multiple-choice and multiple-selection (+ up to 10 unscored), 90 min, USD 200, valid 2 years, English/Japanese/pt-BR/Korean, 6 months hands-on recommended |
| Pass mark | Not published. `passMarkUnpublished: true`; the mock aims at 80% |
| Sections | D1 Design Applications 14%, D2 Data Preparation 14%, D3 Application Development 30%, D4 Assembling and Deploying Applications 22%, D5 Governance 8%, D6 Evaluation and Monitoring 12% |
| Tasks | 56 (`data/exam-tasks.json`): 1.1-1.6, 2.1-2.8, 3.1-3.13, 4.1-4.15, 5.1-5.4, 6.1-6.10 (one per outline bullet) |
| Format | The guide says multiple-selection exists: about 15% of the bank is "(Select TWO)" (33 of 225); the rest single answer |

Writing rules (in addition to the DBX-DEA and DBX-MLA ones above):
- GenAI-engineer view: pick the chunking, retrieval, prompt, guardrail, chain or deployment option for a scenario and say why the others fail. Short LangChain/MLflow/SQL (`ai_query`) snippets <=8 lines. Not UI paths.
- Product names moved since the guide was written; check the docs page before keying and use the current name with the guide name once in G:. Found 2026-11-08: Mosaic AI Vector Search is now Databricks AI Search (formerly Databricks Vector Search); AI Gateway is documented as Unity Gateway (governance for models, agents, MCP servers); Agent Bricks is now the agent developer platform (Agent Bricks CLI), while Knowledge Assistant and Supervisor Agent (the guide's "Multiagent Supervisor") are marked Legacy and Information Extraction is Legacy and Beta, with Genie Agents as the low-code replacement; Genie spaces are now Genie Agents; `ResponsesAgent` is the recommended agent interface (ChatAgent and ChatModel are older).
- Preview/Beta found (do not key as facts): MLflow Prompt Registry (Beta), MLflow production monitoring of agents (Beta), AI Search full-text keyword search and dedicated full-text indexes (Beta), AI Search query payload logging (Beta), Databricks-provided MCP servers `system.ai.dbsql`/`sandbox`/`web_search` (Unity Gateway beta). Task 4.14 (prompt version control) and 6.6 (Agent Monitoring) therefore need a stable framing: ask the concept (version, alias, promote across environments, trace/inference-table monitoring) with GA APIs, or key the documented behavior and mention the Beta label in G: only. Check again before ingest.
- GA candidates to confirm per question: AI Search (Delta Sync vs Direct Access, standard vs storage-optimized endpoints, hybrid search, re-ranking), Foundation Model APIs (pay-per-token vs provisioned throughput), `ai_query`, Unity Catalog model registration of pyfunc/agent models, MLflow tracing and judges (built-in judges that require ground truth are listed on the judges page), inference tables (AI Gateway-enabled), custom scorers.
- Generic LLM/RAG concepts (chunk size vs context length, re-ranking, prompt techniques, guardrails, masking, licensing) need no doc but must stay vendor-neutral where not Databricks specific; Databricks questions test the Databricks feature.
- Nothing preview, beta or deprecated in keys. No prices, DBU rates, token limits or model names that will retire; use "a foundation model" or documented current families only after checking.
- Overlap: AWS AIP-C01 and AIF-C01, Azure AI-103 and GCP-GAIL share GenAI concepts, not products. DBX-CEA owns context management, Genie configuration and Lakebase memory: keep those out of this bank except as one distractor.

## DBX-CEA Databricks Certified Context Engineer Associate (added 2026-11-08)
Sources: https://www.databricks.com/learn/certification/context-engineer-associate and the guide
https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Context-Engineer-Associate-Exam-Guide-August-2026.pdf
(published and updated 2026-07-29, read 2026-11-08; the newest and most scenario-heavy guide: bullets are long "Given ..., select ..." tasks).

| Item | Value |
|---|---|
| Questions | 45 scored multiple-choice and multiple-selection (+ up to 10 unscored), 90 min, USD 200, valid 2 years, English only, 6 months hands-on recommended |
| Pass mark | Not published. `passMarkUnpublished: true`; the mock aims at 80% |
| Sections | D1 Foundations of Context Engineering 16%, D2 System Prompt and Instruction Design 9%, D3 Knowledge Retrieval and Genie Configuration 20%, D4 Memory Architecture with Lakebase and MLflow 18%, D5 Tool Design, MCP, and Agent Context 13%, D6 Context Compression and Compaction 11%, D7 Multi-Agent and Long-Horizon Task Design 13% |
| Tasks | 45 (`data/exam-tasks.json`): 1.1-1.7, 2.1-2.4, 3.1-3.9, 4.1-4.8, 5.1-5.6, 6.1-6.5, 7.1-7.6 (one per outline bullet) |
| Format | The guide says multiple-selection exists: about 16% of the bank is "(Select TWO)" (37 of 225); the rest single answer |

Writing rules (in addition to the DBX-DEA and DBX-MLA ones above):
- Every question is a short scenario: an agent, a symptom (trace, eval log, MLflow result, config) and the decision (technique, configuration, metadata fix, strategy). Stems of 3-6 lines, four long plausible options with a real trade-off (see the guide's samples: the wrong options are sensible fixes that cost recall, tokens or maintenance). No code beyond a 3-line config or trace excerpt.
- Context-engineering vocabulary is the exam's own: context poisoning, distraction, confusion, clash; attention budget; compaction vs trimming; just-in-time vs pre-inference retrieval; progressive disclosure; Agent Skills; tool result clearing. Define it once in G: with the guide wording, never from an outside blog; the exam guide and the docs pages are the only authorities. Mark anything the docs do not state as the exam's convention in G:.
- Databricks names to verify (2026-11-08): Databricks AI Search (formerly Vector Search); Genie Agents (docs; Genie spaces in the guide; configure with instructions, trusted SQL assets, example SQL, sample questions); Lakebase Postgres (Autoscaling projects; Provisioned is the older mode); MLflow 3 (traces, eval, runs); managed MCP servers; Unity Catalog tool registration (SQL/Python functions); Unity Gateway (formerly AI Gateway); Agent Skills (check the docs page exists before keying; the guide names it).
- Preview/Beta found: Databricks-provided MCP servers `system.ai.dbsql`/`sandbox`/`web_search` (Unity Gateway beta), AI Search full-text and query payload logging (Beta), MLflow Prompt Registry and production monitoring (Beta). Keys must not depend on these. Lakebase Public Preview items (Postgres changes as Delta) are not needed: a "Delta-backed state object" (task 4.2) is plain Delta tables. Agent Bricks Knowledge Assistant and Supervisor Agent are Legacy: do not key them as the recommended design.
- Reasoning modes (task 1.6): "standard, extended thinking, reduced thinking" are model-side features; ask only about token budget and context-window effects stated in the question, not about a named model's limits.
- Overlap: DBX-GAI owns RAG building blocks, Vector Search configuration, MCP integration and Agent Framework deployment; DBX-DAA owns Genie as an analyst. Here ask the context decision (what enters the window, in what form, when).

## DBX-ASD Databricks Certified Associate Developer for Apache Spark (added 2026-11-08)
Sources: https://www.databricks.com/learn/certification/apache-spark-developer-associate and the guide
https://www.databricks.com/sites/default/files/2026-10/databricks-certified-associate-developer-apache-spark-exam-guide-august-2026.pdf
(published and updated 2026-10-08, read 2026-11-08). The guide still carries the template line ("[Author: list every section with its percentage weight ...]") above the outline and a template note in Recommended Preparation; the outline itself is complete and sums to 100.

| Item | Value |
|---|---|
| Questions | 45 scored multiple choice (+ up to 10 unscored), 90 min, USD 200, valid 2 years, English only, 6 months hands-on recommended |
| Pass mark | Not published. `passMarkUnpublished: true`; the mock aims at 80% |
| Sections | D1 Apache Spark Architecture and Components 20%, D2 Using Spark SQL 20%, D3 Developing Apache Spark DataFrame/DataSet API Applications 30%, D4 Troubleshooting and Tuning Apache Spark DataFrame API Applications 10%, D5 Structured Streaming 10%, D6 Using Spark Connect to Deploy Applications 5%, D7 Using Pandas API on Spark 5% |
| Tasks | 32 (`data/exam-tasks.json`): 1.1-1.7, 2.1-2.4, 3.1-3.10, 4.1-4.3, 5.1-5.4, 6.1-6.2, 7.1-7.2 (one per outline bullet) |
| Code | Python (PySpark) only ("basic Spark DataFrame tasks using Python"); SQL for D2. Snippets <=8 lines, runnable |
| Format | Single answer only (multiple choice; the samples are single answer): this bank uses single answer only |

Writing rules (in addition to the DBX-DEA ones above):
- Developer view: predict what a snippet returns, which API fits, why a job is slow or fails, what a config does. Code-reading questions are the core; keep them deterministic (no reliance on row order unless `orderBy`) and state the Spark behavior being tested.
- Spark facts come from spark.apache.org (reachable; `docs/latest` currently renders Spark 4.3.0 docs, 2026-11-08) and the PySpark API pages; Databricks docs only for Databricks behavior (Databricks Connect, serverless, Delta). Check the version a feature appeared in before keying: pandas API on Spark, Spark Connect (default client/server model in Spark 4), AQE (on by default since 3.2), `dropDuplicatesWithinWatermark` (3.5), `transformWithState`/`applyInPandasWithState` and StateStores (task 3.8: stateful operators are Structured Streaming features; the exam bullet says "UDFs with or without stateful operators, including StateStores", so key the documented API and state the version in G:), pandas UDFs with type hints, and ANSI SQL mode became the default in Spark 4 (avoid ANSI-sensitive casts and division by zero unless the stem names the setting; verify on the docs page).
- Do not use the removed or deprecated: RDD-first questions (RDDs only as a contrast in architecture), `SQLContext`, `registerTempTable`, Koalas, `spark.sql.shuffle.partitions` guesses without AQE context. The default `spark.sql.shuffle.partitions` is 200 but AQE coalesces; say which applies.
- Nothing preview, beta or deprecated in keys. No cluster sizes, prices or runtime version numbers.
- Overlap: DBX-DEA/DEP own Delta, Auto Loader, Lakeflow and Unity Catalog; this bank tests plain Spark. Read their published questions first (grep data/DBX-DEA.json) and keep Databricks product features out of keys except `format("delta")` file reads. DEA-C01 and GCP-PDE share Spark/Beam concepts, not APIs.
- Preview/Beta check (2026-11-08): Spark Connect overview (Spark 4.3.0 docs) shows no experimental label; the Databricks "Pandas API on Spark" page shows no Preview/Beta. The `transformWithState` API page and the structured-streaming dedup page paths tried on spark.apache.org returned 404: find the current page via the Structured Streaming programming guide before keying any stateful-operator question (tasks 3.8, 5.4).
