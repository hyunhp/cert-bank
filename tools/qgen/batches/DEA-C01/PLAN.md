# DEA-C01 hard set (b08-b09), 2026-11-17

Why: the owner scored 78% on this site's DEA mock but 45% on AWS's official Skill Builder practice set.
Compared with that set, our DEA questions are short (stems 32 words, options 9 words), multi-answer is only
"(Select TWO)", and several tested concepts are thin. These two batches are an exam-realistic, harder layer.
The official set is a style and topic calibration only: never reuse its wording, scenarios or option sets.

## Style for every question in b08-b09 (level `advanced`)
- Stem 60-90 words: a concrete company situation with 2-3 binding constraints (latency, cost, operational
  overhead, compliance window, "without changing the existing schema", retention period, ...). The question line
  names the deciding criterion ("LEAST operational overhead", "MOST cost-effective", "within 12 hours").
- Every option 15-30 words, written as a complete, specific approach that a real engineer could build on AWS.
  Each wrong option must be workable in general and fail exactly one stated constraint (not a made-up feature).
  Correct options must not be the longest (length-bias gate): keep all options about the same length.
- Multi-answer: about 20% of each batch. Mix "(Select TWO)" (5 choices) and "(Select THREE)" (6 choices, A-F;
  qgen supports it since 2026-11-17). At least 2 "(Select THREE)" per batch.
- Detailed explanations (G/W/X/T, see tools/qgen/batches/ANS-C01/e01.txt). G: teaches the mechanism behind the
  deciding constraint. Every fact checked on docs.aws.amazon.com (`python3 tools/learn_fetch.py --grep ...`),
  with `# src:` lines. Mix scenario types: mostly use-case and troubleshooting, some tradeoff.

## b08: D1 Data Ingestion and Transformation (20) + D3 Data Operations and Support (10)
Owns (only b08 writes these):
- Kinesis Data Streams + Lambda: parallelization factor, enhanced fan-out, resharding, batch window / batch size,
  bisect on error, IteratorAge diagnosis (T1.1, T3.3).
- SQS message lifecycle: retention period (max 14 days), visibility timeout, purge, maxReceiveCount + DLQ,
  delay queues, which events remove a message (T1.1, T3.3).
- Amazon Data Firehose: Lambda transformation, record format conversion to Parquet/ORC with a Glue table,
  buffering hints, dynamic partitioning (T1.2).
- AWS Glue job monitoring and DPU sizing: job run monitoring / job metrics, auto scaling, worker types, Flex (T3.3).
- Amazon AppFlow SaaS ingestion (on-event vs scheduled flows) and EventBridge Scheduler / Lambda for existing cron
  code (T1.1, T1.3).
- Compute for transforms: Lambda + EFS shared NFS storage, EKS pod ephemeral storage vs network storage (T1.2).
- Orchestration choices: Step Functions vs MWAA vs Glue workflows under operational-overhead limits (T1.3).
- Data quality in pipelines: Glue Data Quality rules and actions (T3.4); Athena query troubleshooting (T3.2).
Leave to b09: anything Redshift, S3 storage classes/lifecycle, Secrets Manager/Parameter Store, IAM roles for
Glue, Lake Formation, Macie, encryption.

## b09: D2 Data Store Management (16) + D4 Data Security and Governance (11) + D3 (3)
Owns (only b09 writes these):
- Redshift: SUPER + PartiQL for nested JSON, data sharing with Redshift Serverless consumers, Spectrum (and the
  S3 storage classes it cannot read), COPY from S3 with SSE-KMS vs SSE-C / client-side encryption, UNLOAD,
  materialized views, distribution/sort key choices under a stated workload (T2.1, T2.4, T3.2, T4.3).
- S3 lifecycle and storage classes against retrieval windows: Glacier Instant / Flexible (hours) / Deep Archive
  (up to 48 h), Intelligent-Tiering archive tiers, expiration (T2.3).
- Store choice under constraints: DynamoDB vs OpenSearch (full-text) vs Aurora vs Redshift (T2.1).
- Glue Data Catalog: crawlers, partition projection, schema evolution with Iceberg tables (T2.2, T2.4).
- Credentials: Secrets Manager rotation vs Parameter Store; IAM database authentication engine support (T4.1).
- Authorization: Glue/Lambda service roles and least-privilege S3 actions/resources; Lake Formation data filters
  and LF-tags (T4.2, T4.5).
- Macie findings to EventBridge, CloudTrail / CloudTrail Lake for audit (T4.4, T4.5).
Leave to b08: Kinesis, SQS, Firehose, Glue job monitoring, AppFlow, EventBridge Scheduler, Lambda+EFS, EKS storage.

# DEA-C01 expert tier (b10-b11), 2026-11-17

Owner asked for the hardest fair questions possible ("극상 난이도"). Level `expert` (new; red badge). 20 per batch.
Hard must still be fair: every fact on docs.aws.amazon.com, one best answer, no trivia for its own sake.

## What makes a question expert-level here (use at least three per question)
- Long scenario (90-140 words) with 3-4 binding constraints, one of them stated only in the details
  (an existing configuration, a compliance clause, a team skill limit) that eliminates the "obvious" answer.
- Numbers that must be worked: records/s and record size vs shard or partition throughput, file counts vs small-file
  overhead, retention or retrieval windows vs SLA, cost per unit across two designs, concurrency math
  (shards x parallelization factor), DPU-hours. Use only documented limits and prices that drive the design.
- Two-service interplay: the failure or the fix is in the seam (Lambda event source mapping + Kinesis, Firehose +
  Glue table schema, Lake Formation + Glue crawler, Redshift + S3 encryption, Step Functions + Glue job states).
- Troubleshooting from evidence: a metric pattern, an error message or a log line; the answer is the root cause,
  not a generic "scale up".
- Options that differ only in a configuration detail (which parameter, which order of steps, which scope), all of
  them real settings. No option may be eliminated by a single keyword.
- Multi-answer ~30% of the batch, half of them "(Select THREE)" with 6 choices.

## Quality gate (reviewer must do this)
- Blind solve: the reviewer answers every question from the stem and options before reading K:/W:/X:, and flags any
  where its answer differs; those are rewritten until the key is unambiguous or replaced.
- Every number in a stem is checked against the docs (quotas, defaults, retrieval times) with `# src:` lines.

## b10: D1 (12) + D3 (8)   streaming, transformation, orchestration, operations
Kinesis/MSK/Firehose throughput and ordering math, Lambda event source mappings (batching, parallelization,
partial batch failure, on-failure destinations), Glue Spark tuning (DPUs, shuffle, skew, bookmarks), Step
Functions + Glue/EMR orchestration and retries, data quality gates, Athena performance (partition projection,
file sizes, CTAS), CloudWatch evidence.
## b11: D2 (10) + D4 (10)   stores, catalog, lifecycle, security, governance
Redshift (distribution/sort keys under a query mix, WLM/concurrency scaling, data sharing, Spectrum, SUPER),
DynamoDB capacity/partition math and GSIs, S3 lifecycle/storage-class cost math with minimum durations and
retrieval fees, Iceberg/Glue schema evolution, KMS key policies and grants across accounts, Lake Formation
cross-account sharing and LF-tags, Macie/CloudTrail evidence, encryption in transit/at rest seams.
No overlap with b08/b09 or published DEA-C01 questions (check --siblings).
