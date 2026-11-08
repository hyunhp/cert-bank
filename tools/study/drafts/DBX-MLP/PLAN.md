# DBX-MLP study guide plan (19 days)
Rules: `tools/study/README.md` (data shape) and `tools/qgen/DATABRICKS.md` (DBX-MLP + DBX-MLA + DBX-DEA sections). Sources: tasks in `data/exam-tasks.json` ("DBX-MLP"), docs.databricks.com and spark.apache.org only (`python3 tools/learn_fetch.py --grep "<terms>" <url>`, shared cache; mlflow.org is blocked). Built from the reviewed bank (`data/DBX-MLP.json`, `data/explanations/DBX-MLP.json`) plus the docs; keep claims the bank already verified, re-check anything new yourself (earlier writers still had ~15 unchecked claims each).
Professional ML-engineer level. `data/study/DBX-MLA.json` (associate) already teaches MLflow tracking, feature tables, aliases, metrics and basic serving: build on it, do not repeat it.
Settled facts (from the reviewed bank): open-source Hyperopt is unmaintained and not in ML Runtime after 16.4 LTS (teach Optuna with MLflowStorage/MlflowSparkStudy and Ray; Hyperopt only as legacy); `xgboost.spark` is Public Preview (do not teach as an answer); Lakehouse Monitoring is now called data profiling (use the new name, old name once); Online tables are now Online Feature Stores (Lakebase-backed); bundles are Declarative Automation Bundles; PSI bands 0.1/0.2 are stated on the monitor-output page; AI Functions batch inference and protobuf tensor input are Public Preview; inference tables are legacy (Unity Gateway inference tables are current); creating a registered model takes USE CATALOG, USE SCHEMA and CREATE MODEL, adding a version takes ownership or CREATE MODEL VERSION; aliases replace stages; canary/blue-green have no docs page (general practice, implemented with served entities and traffic_config). `nested=True`, `mlflow.parentRunId`, `log_figure/log_dict/log_table` and `code_paths` are standard MLflow behavior not on any docs page: say so. No Preview/Beta/deprecated as correct answers, no numeric limits.
Shape per day: see `data/study/DBX-MLA.json` and `data/study/DBX-DAA.json` (day, domain, title, services, concepts[{heading,body}], examPoints, quiz[2], recap).
3-4 concepts of 120-190 words, 3 examPoints, quiz = 2 questions with 4 choices, `answer` is a 0-3 integer index (spread the indexes), correct choice never the longest (ties count), no letter references in explanations. `domain` is the string "D1".."D3" (`null` on the final day). Recompute every numeric example.

| Day | Domain | Tasks | Topic |
|---|---|---|---|
| 1 | D1 | T1.1-T1.3 | when SparkML is right, ML pipelines, estimators and transformers for a use case |
| 2 | D1 | T1.4-T1.7 | tuning and evaluating SparkML, batch/streaming scoring, SparkML vs single-node for inference |
| 3 | D1 | T1.8, T1.14 | scaling distributed training with SparkML and pandas function APIs; group-specific training and inference |
| 4 | D1 | T1.9, T1.10 | distributed tuning with Optuna + MLflow and with Ray |
| 5 | D1 | T1.11-T1.13 | vertical vs horizontal scaling, model vs data parallelism, Ray vs Spark |
| 6 | D1 | T1.15-T1.17 | MLflow nested runs, custom logging, custom model objects with real-time feature engineering |
| 7 | D1 | T1.18, T1.19 | point-in-time correctness, automated feature pipelines with the FeatureEngineering client |
| 8 | D1 | T1.20-T1.22 | Online Feature Stores, streaming feature computation, on-demand features and feature serving |
| 9 | D2 | T2.1, T2.2 | deploy-code lifecycle pipelines, mapping Databricks features to lifecycle activities |
| 10 | D2 | T2.3-T2.6 | unit and integration testing, per-environment tests, organizing functions and tests |
| 11 | D2 | T2.7, T2.8 | scalable environments, ML assets in Declarative Automation Bundles |
| 12 | D2 | T2.9, T2.10 | automated retraining triggers and top-model selection |
| 13 | D2 | T2.11, T2.12 | drift tests from the drift metrics table, choosing table type and monitor feature |
| 14 | D2 | T2.13, T2.14 | building monitors (snapshot, time series, inference), monitoring pipeline components |
| 15 | D2 | T2.15-T2.17 | alerting on drift, baseline vs consecutive windows, performance trends from inference tables |
| 16 | D2 | T2.18-T2.20 | custom metrics, granularity and slicing, endpoint health metrics |
| 17 | D3 | T3.1, T3.2 | deployment strategies and rollout with Model Serving |
| 18 | D3 | T3.3-T3.5 | custom PyFunc models with artifacts in Unity Catalog, querying via REST and the Deployments SDK, deploying custom models |
| 19 | null | all | final review: decision cheat-sheet across the 3 domains, weights from `data/exam-specs.json`, 2 quiz questions |

Writers: w1 days 1-5, w2 days 6-9, w3 days 10-14, w4 days 15-19. Each writes ONLY `tools/study/drafts/DBX-MLP/wN.json` (a JSON list of day objects).
