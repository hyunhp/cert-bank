# DBX-ASD study guide plan (17 days)
Rules: `tools/study/README.md` (data shape) and `tools/qgen/DATABRICKS.md` (DBX-ASD + DBX-DEA sections). Sources: tasks in `data/exam-tasks.json` ("DBX-ASD"), spark.apache.org (docs/latest = Spark 4.3.0; find current pages, some old URLs 404) and docs.databricks.com only (`python3 tools/learn_fetch.py --grep "<terms>" <url>`, shared cache). Built from the reviewed bank (`data/DBX-ASD.json`, `data/explanations/DBX-ASD.json`) plus the docs; keep claims the bank already verified, re-check anything new yourself (earlier writers still had ~15 unchecked claims each).
Developer level (PySpark first, Spark SQL where natural). `data/study/DBX-DEA.json` and `DBX-DEP.json` cover the Databricks-engineer side: do not repeat them, teach plain Apache Spark.
Settled facts (from the reviewed bank): Spark 4 enables ANSI mode by default (casts and parses can raise errors; `try_*` functions exist); `spark.sql.crossJoin.enabled` is true by default since 3.0; `DataFrame.cache()` default storage level is MEMORY_AND_DISK_DESER; `spark.task.maxFailures` default is 4; Trigger once is deprecated (use availableNow), continuous trigger is experimental; `pyspark.mllib` is in maintenance mode; `applyInPandasWithState` (3.4, Connect 3.5), `transformWithStateInPandas` (4.0.0), `mapGroupsWithState` is legacy; `dropDuplicatesWithinWatermark` (3.5); Spark Connect (3.4); standalone mode does not support cluster mode for Python applications; `_SUCCESS` marker depends on the committer. No Preview/Beta/deprecated features as correct answers; no numeric limits beyond the defaults above.
Shape per day: see `data/study/DBX-DAA.json` and `data/study/DBX-MLA.json` (day, domain, title, services, concepts[{heading,body}], examPoints, quiz[2], recap).
3-4 concepts of 120-190 words, 3 examPoints, quiz = 2 questions with 4 choices, `answer` is a 0-3 integer index (spread the indexes), correct choice never the longest (ties count), no letter references in explanations. `domain` is the string "D1".."D7" (`null` on the final day). Recompute every numeric example.

| Day | Domain | Tasks | Topic |
|---|---|---|---|
| 1 | D1 | T1.1, T1.2 | advantages and challenges of Spark; cluster, driver, executors, cores, memory |
| 2 | D1 | T1.3, T1.4 | DataFrame vs Dataset, SparkSession lifecycle, caching and storage levels, GC; job/stage/task hierarchy |
| 3 | D1 | T1.5-T1.7 | partitioning and shuffles; actions, transformations, lazy evaluation; Spark modules |
| 4 | D2 | T2.1, T2.2 | reading and writing JDBC and files; SQL on files; save modes |
| 5 | D2 | T2.3, T2.4 | persistent tables with sorting, partitioning, bucketing; temporary and global temp views |
| 6 | D3 | T3.1, T3.2 | column and row manipulation; deduplication and validation |
| 7 | D3 | T3.3, T3.4 | aggregations (count, approx_count_distinct, mean, summary); dates and epochs |
| 8 | D3 | T3.5, T3.10 | joins, union, cross joins; broadcast joins |
| 9 | D3 | T3.6, T3.7 | schemas on read/write; sort, iterate, print schema, convert to lists |
| 10 | D3 | T3.8, T3.9 | UDFs and stateful operators; broadcast variables and accumulators |
| 11 | D4 | T4.1 | partitioning, repartition, coalesce, skew, shuffle reduction |
| 12 | D4 | T4.2, T4.3 | Adaptive Query Execution; driver/executor logs, monitoring, out-of-memory diagnosis |
| 13 | D5 | T5.1, T5.2 | Structured Streaming engine; streaming DataFrames, output modes, sinks |
| 14 | D5 | T5.3, T5.4 | window and aggregation on streams; streaming deduplication with and without watermark |
| 15 | D6 | T6.1, T6.2 | Spark Connect; deployment modes (client, cluster, local) |
| 16 | D7 | T7.1, T7.2 | pandas API on Spark; pandas UDFs |
| 17 | null | all | final review: decision cheat-sheet across the 7 domains, weights from `data/exam-specs.json`, 2 quiz questions |

Writers: w1 days 1-5, w2 days 6-10, w3 days 11-14, w4 days 15-17. Each writes ONLY `tools/study/drafts/DBX-ASD/wN.json` (a JSON list of day objects).
