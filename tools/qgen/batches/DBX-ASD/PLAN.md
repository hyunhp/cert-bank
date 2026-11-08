# DBX-ASD batch plan (topics owned per batch)
Exam: Databricks Certified Associate Developer for Apache Spark, guide (dated 2026-10-08) read 2026-11-08. Target 225 (D1 45, D2 45, D3 68, D4 23, D5 22, D6 11, D7 11), single answer only (the guide lists multiple choice only: no "Select TWO").
Rules and facts: `tools/qgen/DATABRICKS.md` (DBX-ASD section and DBX-DEA rules). Header `@ DBX-ASD Dx Tx.y <level> <kind>` (two tokens after the task id, e.g. "applied use-case").
Before writing, grep the published Databricks questions (data/DBX-*.json) on the same topic. Shared hot spots belong to ONE batch; others may use them as distractors.

| Batch | Tasks (count) | Total | Owns |
|---|---|---|---|
| b01 | T1.1 (7), T1.2 (7), T1.3 (7), T1.4 (6) | 27 | Spark advantages/challenges; architecture components (owned here); caching/storage levels/GC; job/stage/task hierarchy (owned here) |
| b02 | T1.5 (6), T1.6 (6), T1.7 (6), T2.1 (12) | 30 | shuffle partitions; lazy evaluation (owned here); modules (pandas API on Spark and MLlib only as names); JDBC and file read/write options; partitionBy |
| b03 | T2.2 (11), T2.3 (11), T2.4 (5) | 27 | save modes (owned here); saveAsTable, bucketing/sorting, partitioned tables; createOrReplaceTempView |
| b04 | T2.4 (6), T3.1 (7), T3.2 (7), T3.3 (7) | 27 | createOrReplaceTempView; withColumn/drop/explode/split (owned here); dropDuplicates and validation; count/approx_count_distinct/summary |
| b05 | T3.4 (7), T3.5 (7), T3.6 (7), T3.7 (7) | 28 | date functions (owned here); joins (owned here); read/write with explicit schemas; sort/collect/toPandas/printSchema |
| b06 | T3.8 (7), T3.9 (6), T3.10 (6), T4.1 (8), T4.2 (2) | 29 | UDFs and stateful operators/StateStore (check version); broadcast variables and accumulators; broadcast join (owned here); repartition/coalesce/skew; AQE (owned here) |
| b07 | T4.2 (6), T4.3 (7), T5.1 (6), T5.2 (6), T5.3 (5) | 30 | AQE (owned here); exactly-once and fault tolerance |
| b08 | T5.4 (5), T6.1 (6), T6.2 (5), T7.1 (6), T7.2 (5) | 27 | dropDuplicates vs dropDuplicatesWithinWatermark; Spark Connect features; deployment modes; pandas API on Spark advantages; pandas UDF types |

Waves (about 4 writers at a time): b01, b03, b05, b07; then b02, b04, b06, b08. Ingest each reviewed batch before the next review starts (reviewers replace duplicates of published questions).

Note: `qgen plan` rounds each domain on its own (half to even), so its per-domain "need" can differ by 1 from the largest-remainder counts above; this plan sums to exactly the target.
