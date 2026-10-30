# DP-900 batch plan (topics owned per batch)

Exam: DP-900 Microsoft Azure Data Fundamentals. Skills as of 2026-07-21. 45 minutes, pass 700.
Target 225 (D1 64, D2 54, D3 42, D4 65). Fundamentals: describe and choose; no portal clicks, no CLI; SQL snippets only
as short recognizable statements. Keys GA with current names (Microsoft Fabric, Azure Databricks, Azure Cosmos DB,
Azure Database for PostgreSQL/MySQL flexible server; Azure Database for MariaDB is retired — never key it).
Shared hot spots belong to ONE batch only; others may use them as distractors but not as the tested concept.

| Batch | Tasks | Count | Owns | Leave to |
|---|---|---|---|---|
| b01 | T1.1 ways to represent data, T1.2 storage options | 32 | structured / semi-structured / unstructured data, file formats (CSV, JSON, XML, Parquet, Avro, ORC, binary), data store types (relational, document, key-value, column-family, graph, object/blob), choosing an Azure datastore for a use case at concept level | Cosmos DB APIs (b06), Blob tiers (b05) |
| b02 | T1.3 data workloads, T1.4 roles | 32 | transactional (OLTP, ACID) vs analytical (OLAP) workloads, data warehouse vs data lake at workload level, batch vs interactive analysis at concept level, DBA / data engineer / data analyst responsibilities | lakehouse/Fabric details (b07), streaming (b08) |
| b03 | T2.1 relational concepts | 27 | tables/rows/columns, primary and foreign keys, normalization and why, SQL statement types (DDL, DML, DQL/DCL) and common statements (SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, JOIN), database objects (views, stored procedures, indexes) | Azure services (b04) |
| b04 | T2.2 relational Azure services | 27 | Azure SQL Database (single, elastic pool), Azure SQL Managed Instance, SQL Server on Azure VMs (IaaS vs PaaS trade-offs, compatibility), Azure Database for PostgreSQL and MySQL flexible server | normalization/SQL (b03) |
| b05 | T3.1 Azure storage | 20 | Blob storage (containers, block/page/append blobs, access tiers hot/cool/cold/archive), Data Lake Storage Gen2 hierarchical namespace, Azure Files (SMB/NFS shares), Azure Table storage | Cosmos DB for Table (b06) |
| b06 | T3.2 Azure Cosmos DB | 22 | Cosmos DB use cases (global distribution, low latency, multi-model), APIs (NoSQL, MongoDB, PostgreSQL, Apache Cassandra, Apache Gremlin, Table) and when to choose each | Table storage (b05) |
| b07 | T4.1 large-scale analytics | 25 | ingestion and processing (ETL vs ELT, pipelines), analytical stores (data warehouse, data lake, lakehouse, OneLake, Delta format), Microsoft Fabric workloads (Data Factory, lakehouse, warehouse), Azure Databricks | real-time (b08), Power BI (b09) |
| b08 | T4.2 real-time analytics | 18 | batch vs streaming data, Microsoft Fabric Real-Time Intelligence (eventstreams, Eventhouse/KQL database), Azure Stream Analytics, Event Hubs as a source, Spark Structured Streaming | batch pipelines (b07) |
| b09 | T4.3 Power BI | 22 | Power BI capabilities (Desktop, service, reports, dashboards, apps), data models (tables, relationships, measures, calculated columns, hierarchies, star schema), choosing visualizations (table, matrix, bar/column, line, pie, card, map, scatter) | lakehouse modeling (b07) |
