# GCP-PCA case study digest (own words, read 2026-10-31 from the v6.1 PDFs linked in GCP.md)
Use only these facts. Stems name the business and give the 1-2 facts the decision needs.

## Altostrat Media (media company, gen AI content platform)
- Podcasts, interviews, news, documentaries; large audio/video library in Cloud Storage; BigQuery warehouse; GKE platform; Cloud Run functions for event tasks (transcoding, metadata, recommendations).
- Some legacy on-premises systems (content ingestion, archival) to be modernized; Google Identity plus third-party IdPs; Cloud Monitoring plus Prometheus, alerts by email.
- Needs: reliable workflows across Google Cloud + on-premises; simpler infrastructure; optimize storage cost with high availability; natural-language 24/7 support chat; summaries and metadata extraction (NLP, vision); detect harmful content; trends and insights.
- Technical: CI/CD for containers with central management; secure high-performance hybrid connectivity for ingestion; Kubernetes on-premises and in cloud; AI that is auditable and explainable; LLM personalization; chatbots. Reliability and cost are top priorities.

## Cymbal Retail (online retailer, fast growth)
- Huge multi-vertical catalog; wants gen AI for catalog enrichment (attributes, descriptions, images from supplier data), conversational commerce with product discovery (virtual agents on web and app using Discovery AI), and a modernized stack.
- Today: mix of on-premises and cloud; MySQL, SQL Server, Redis, MongoDB; Kubernetes clusters; SFTP and batch ETL integrations; custom web catalog app on relational queries; IVR plus call-center agents who key in orders; open source monitoring (Grafana, Nagios, Elastic). Pain: manual error-prone processes, data silos, hard integrations.
- Needs: automate enrichment, better discoverability, engagement, conversion, lower call-center and data-center cost.
- Technical: attribute generation aligned to catalog structure; image variations and edits; natural-language product search; scale with growth; human-in-the-loop review UI before catalog updates; data security and compliance.

## EHR Healthcare (SaaS electronic health records)
- Software for medical offices, hospitals, insurers; growing fast; moving out of colocation (one data-center lease about to expire) to Google Cloud.
- Today: containerized web apps on Kubernetes clusters; MySQL, SQL Server, Redis, MongoDB; legacy file/API integrations with insurers on-premises that stay for now; Microsoft Active Directory; open source monitoring with ignored email alerts.
- Needs: onboard insurers quickly; at least 99.9% availability for customer-facing systems; centralized visibility and proactive action; insights and predictions from provider data; lower latency; regulatory compliance; lower admin cost.
- Technical: keep legacy interfaces with on-premises and cloud connectivity; consistent management of container environments (several); secure high-performance on-premises link; consistent logging, retention, monitoring, alerting; dynamically scale and provision environments; ingest data from new providers. Past outages: misconfiguration, spikes, inconsistent monitoring.

## KnightMotives Automotive (car maker: BEV, hybrid, ICE; autonomous driving)
- Hybrid and ICE cars lack the modern in-vehicle experience of the BEVs, hurting sales; wants a consistent AI-powered experience across models within five years; unreliable online build-to-order system strains dealers; dealers have no equipment budget.
- Today: mostly on-premises, some apps on major clouds; outdated mainframe supply chain and ERP; fragmented code bases and technical debt; connectivity challenges at plants and in rural areas; siloed data; obsolete AI infrastructure; past data breaches.
- Needs: personalized driver relationship; better build-to-order; monetize data; strong security; EU data protection compliance; upskill staff.
- Technical: hybrid cloud strategy and gradual legacy replacement; reliable connectivity for real-time AI; simulation environment for autonomous testing; data management platform with strict security and privacy; security framework, incident response plan; CRM and dealer tools (sales, service, inventory).
