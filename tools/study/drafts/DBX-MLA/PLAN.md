# DBX-MLA study guide plan (19 days)
Rules: `tools/study/README.md` (data shape) and `tools/qgen/DATABRICKS.md` (DBX-MLA + DBX-DEA sections: names, legacy/Preview kept out). Sources: exam guide tasks in `data/exam-tasks.json` ("DBX-MLA"), docs.databricks.com and spark.apache.org only (`python3 tools/learn_fetch.py --grep "<terms>" <url>`, shared cache; mlflow.org is blocked). Built from the reviewed bank (`data/DBX-MLA.json`, `data/explanations/DBX-MLA.json`) plus the docs; keep claims the bank already verified, re-check anything new yourself (earlier writers still had ~15 unchecked claims each).
ML-practitioner level: choose the right feature, metric, tuning method or deployment mode. `data/study/DBX-DEA.json` covers the engineer side: do not repeat it.
Facts settled by the bank (do not contradict): open-source Hyperopt is unmaintained and not in ML Runtime after 16.4 LTS (teach Optuna/Ray Tune; Hyperopt only as legacy); AutoML is documented but removed from ML Runtime 18.0; Feature Store docs recommend Feature Views while feature tables remain (workspace feature store and workspace model registry are legacy; UC models use aliases, no stages); `dbutils.data.summarize` is Public Preview; `ai_query` batch inference, inference tables, real-time mode are not taught as answers; Delta Live Tables is now Lakeflow Spark Declarative Pipelines (docs have no model-inference page: streaming inference = Structured Streaming + spark_udf). No numeric limits, no runtime version numbers beyond the two above.
Shape per day: see `data/study/DBX-DEA.json` and `data/study/DBX-DAA.json` (day, domain, title, services, concepts[{heading,body}], examPoints, quiz[2], recap).
3-4 concepts of 120-190 words, 3 examPoints, quiz = 2 questions with 4 choices, `answer` is a 0-3 integer index (spread the indexes), correct choice never the longest (ties count), no letter references in explanations. `domain` is the string "D1".."D4" (`null` on the final day). Metric and statistics facts use generally accepted definitions: recompute every numeric example.

| Day | Domain | Tasks | Topic |
|---|---|---|---|
| 1 | D1 | T1.1, T1.2 | MLOps strategy, ML Runtime advantages |
| 2 | D1 | T1.3, T1.4 | AutoML: model and feature selection, benefits |
| 3 | D1 | T1.5-T1.7 | feature tables in Unity Catalog vs workspace, create and write |
| 4 | D1 | T1.8-T1.10 | train and score with feature tables, online vs offline |
| 5 | D1 | T1.11-T1.13 | MLflow Client API, manual logging, MLflow UI |
| 6 | D1 | T1.14, T1.15 | registering models in Unity Catalog, UC vs workspace registry |
| 7 | D1 | T1.16-T1.18 | code vs model promotion, model tags, aliases (champion/challenger) |
| 8 | D2 | T2.1, T2.2 | summary statistics, outlier removal (std dev, IQR) |
| 9 | D2 | T2.3, T2.4 | visualizations, comparing features |
| 10 | D2 | T2.5-T2.7 | imputation, one-hot encoding |
| 11 | D2 | T2.8, T2.9 | one-hot suitability, log transformation |
| 12 | D3 | T3.1-T3.4 | algorithm selection, imbalance, estimators vs transformers, pipelines |
| 13 | D3 | T3.5-T3.7 | hyperparameter tuning: search strategies, Optuna/Ray Tune, parallelizing single-node models |
| 14 | D3 | T3.8-T3.10 | cross-validation vs train-validation split, number of models |
| 15 | D3 | T3.11-T3.13 | classification and regression metrics, choosing a metric |
| 16 | D3 | T3.14, T3.15 | exponentiating log targets, bias-variance and complexity |
| 17 | D4 | T4.1-T4.3 | serving modes, custom model endpoints, pandas/Spark batch inference |
| 18 | D4 | T4.4-T4.6 | streaming inference, real-time endpoints, traffic split |
| 19 | null | all | final review: decision cheat-sheet across the 4 domains, weights from `data/exam-specs.json`, 2 quiz questions |

Writers: w1 days 1-5, w2 days 6-10, w3 days 11-15, w4 days 16-19. Each writes ONLY `tools/study/drafts/DBX-MLA/wN.json` (a JSON list of day objects).
