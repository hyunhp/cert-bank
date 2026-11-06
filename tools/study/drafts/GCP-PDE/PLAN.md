# GCP-PDE study guide plan (22 days)
Rules: `tools/study/README.md` (data shape) and `tools/qgen/GCP.md` (GCP-PDE section: names, renames, preview rule). Sources: the exam guide
(read 2026-11-06) and docs.cloud.google.com only (`python3 tools/learn_fetch.py --grep "<terms>" <url>`, shared cache). Built from the reviewed bank
(`data/GCP-PDE.json`, `data/explanations/GCP-PDE.json`) plus the docs; keep claims the bank already verified, re-check anything new.
Shape per day: see `data/study/GCP-PCA.json` (day, domain, title, services, concepts[{heading,body}], examPoints, quiz[2], recap). 3-4 concepts, quiz = 2 questions, 4 choices each.

| Day | Domain | Tasks | Topic |
|---|---|---|---|
| 1 | D1 | T1.1 | security and compliance for data: IAM, org policies, CMEK, Sensitive Data Protection, residency, project/dataset/table layout, dev vs prod |
| 2 | D1 | T1.2 | reliability and fidelity: cleaning and validation (Dataform, Dataflow, Data Fusion), pipeline monitoring, DR and fault tolerance, ACID vs availability |
| 3 | D1 | T1.3 | flexibility and portability: requirements to architecture, open formats and BigLake, multi-cloud, staging, cataloging, profiling |
| 4 | D1 | T1.4 | migrations: planning and validation, BigQuery Data Transfer Service, Database Migration Service, Datastream, Transfer Appliance, networking |
| 5 | D2 | T2.1 | planning pipelines: sources and sinks, transformation and orchestration logic, networking, encryption |
| 6 | D2 | T2.2 | streaming I: Pub/Sub (subscriptions, ordering, dead-letter, exactly-once) and Dataflow job basics, Streaming Engine, autoscaling, update/drain |
| 7 | D2 | T2.2 | streaming II: Beam model, windows, triggers, watermarks, late data, exactly-once vs at-least-once, BigQuery write methods |
| 8 | D2 | T2.2 | batch processing: Dataproc (Spark, Hadoop), Kafka integration, Data Fusion, templates |
| 9 | D2 | T2.2 | BigQuery transformations, stored procedures, AI data enrichment, acquisition and import |
| 10 | D2 | T2.3 | deployment and operation: Cloud Composer, Workflows, CI/CD for pipelines |
| 11 | D3 | T3.1 | selecting storage systems: Bigtable, Spanner, AlloyDB, Cloud SQL, Firestore, Memorystore, Cloud Storage classes and lifecycle |
| 12 | D3 | T3.2 | data warehouse design in BigQuery: partitioning, clustering, nesting, normalization, access patterns |
| 13 | D3 | T3.3 | data lake: BigLake, external and Iceberg tables, discovery, access, cost controls, monitoring |
| 14 | D3 | T3.4 | data platform and governance: Dataplex / catalog (Knowledge Catalog), data products, federated governance, lineage, quality |
| 15 | D4 | T4.1 | preparing data for visualization: BI Engine, materialized views, precalculated fields, slow queries, masking and column security |
| 16 | D4 | T4.2 | preparing data for AI and ML: BigQuery ML, features, embeddings and RAG data |
| 17 | D4 | T4.3 | sharing data: BigQuery sharing (Analytics Hub), authorized views and datasets, publishing reports |
| 18 | D5 | T5.1 | optimizing resources: cost per business need, persistent vs job-based clusters, availability for critical jobs |
| 19 | D5 | T5.2, T5.3 | automation and repeatability, DAG design, BigQuery Editions, slots and reservations, interactive vs batch jobs |
| 20 | D5 | T5.4 | monitoring and troubleshooting: Cloud Monitoring and Logging, INFORMATION_SCHEMA, quotas, billing, job errors |
| 21 | D5 | T5.5 | failures and mitigation: fault tolerance, restarts, multi-region, replication and failover, corruption and missing data |
| 22 | null | all | final review: decision cheat-sheet across the 5 domains, 2 quiz questions |

Writers: w1 days 1-4, w2 days 5-10, w3 days 11-17, w4 days 18-22. Each writes ONLY `tools/study/drafts/GCP-PDE/wN.json` (a JSON list of day objects).
