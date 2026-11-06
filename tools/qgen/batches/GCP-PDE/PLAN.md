# GCP-PDE batch plan (topics owned per batch)
Exam: Professional Data Engineer, guide read 2026-11-06. Target 225 (D1 50, D2 56, D3 45, D4 34, D5 40). Rules and facts:
`tools/qgen/GCP.md` (GCP-PDE section). About 15-20% "(Select TWO)". Professional depth: design decisions and trade-offs, never
commands or console steps. Before writing, read published GCP-ACE / GCP-PCA questions on the same product and use new scenarios.
Shared hot spots belong to ONE batch only; others may use them as distractors.

| Batch | Tasks | Count | Owns | Leave to |
|---|---|---|---|---|
| b01 | T1.1 (14), T1.2 (14) | 28 | IAM and organization policies for data, CMEK/Cloud KMS, PII strategies (Sensitive Data Protection), data residency, project/dataset/table layout for governance, dev vs prod; data cleaning and validation (Dataform, Dataflow, Data Fusion), orchestration monitoring, DR and fault tolerance, ACID vs availability | Dataplex and cataloging (b06), streaming internals (b03) |
| b02 | T1.3 (10), T1.4 (12), T2.1 (6) | 28 | mapping requirements to architecture, portability and multi-cloud (BigLake, open formats), staging/cataloging/profiling at design level; migration planning (BigQuery Data Transfer Service, Database Migration Service, Datastream, Transfer Appliance, networking); pipeline planning: sources, sinks, networking, encryption | pipeline building (b03, b04) |
| b03 | T2.1 (8), T2.2 (20) | 28 | streaming and Dataflow/Beam: Pub/Sub, windowing, triggers, watermarks, late data, exactly-once, templates, autoscaling; source/sink choice for streaming | batch and Spark (b04) |
| b04 | T2.2 (10), T2.3 (12), T3.1 (6) | 28 | batch transforms: Dataproc (Spark, Hadoop), Kafka integration, Data Fusion, BigQuery SQL/stored procedures, AI data enrichment, acquisition/import; Cloud Composer, Workflows, CI/CD for pipelines; storage selection fit (Bigtable, Spanner, AlloyDB, Cloud SQL, Firestore, Memorystore) | streaming (b03), warehouse (b05) |
| b05 | T3.1 (9), T3.2 (10), T3.3 (9) | 28 | access patterns and storage cost/lifecycle (Cloud Storage classes, Autoclass), BigQuery data model: partitioning, clustering, nesting/denormalization, normalization degree; data lake management with BigLake, Dataplex discovery, cost controls | platform and governance (b06) |
| b06 | T3.3 (1), T3.4 (10), T4.1 (14), T4.2 (3) | 28 | Dataplex Catalog, federated governance model, data mesh; BI: BI Engine, materialized views, precalculated fields, slow-query troubleshooting, masking and column-level security, Sensitive Data Protection; data prep for ML: BigQuery ML, features | sharing (b07) |
| b07 | T4.2 (7), T4.3 (10), T5.1 (8), T5.2 (3) | 28 | embeddings and RAG data prep, vector search in BigQuery; sharing: Analytics Hub, authorized views/datasets, publishing; cost minimization, persistent vs job-based Dataproc clusters, resource availability; Composer DAG design basics | capacity/reservations (b08) |
| b08 | T5.2 (5), T5.3 (8), T5.4 (8), T5.5 (8) | 29 | repeatable scheduling and DAG troubleshooting; BigQuery Editions, reservations, interactive vs batch jobs; Cloud Monitoring/Logging, quotas and billing issues, job troubleshooting; fault tolerance, restarts, multi-region, replication and failover (Cloud SQL, Memorystore), data corruption and missing data | everything else |

Waves (about 4 writers at a time): b01, b03, b05, b07; then b02, b04, b06, b08.
