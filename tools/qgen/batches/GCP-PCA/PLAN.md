# GCP-PCA batch plan (topics owned per batch)
Exam: Professional Cloud Architect, guide read 2026-10-31. Target 275 (D1 69, D2 48, D3 48, D4 41, D5 34, D6 34). Rules and
facts: `tools/qgen/GCP.md` (GCP-PCA section) and case digest `tools/qgen/GCP-PCA-cases.md`. About 15-20% "(Select TWO)";
about 25% case-study questions (one case per question, spread over the four cases). Professional depth: design decisions
and trade-offs, never commands or console steps. Before writing, read published GCP-ACE / GCP-CDL / GCP-GAIL questions on
the same product and use new scenarios. Shared hot spots belong to ONE batch only; others may use them as distractors.

| Batch | Tasks | Count | Owns | Leave to |
|---|---|---|---|---|
| b01 | T1.1, T1.5 | 24 | business use cases and requirements (functional vs non-functional), BCP, cost optimization trade-offs, integration patterns, data movement, disposition (build/buy/modify/deprecate), KPIs/ROI, future improvements, cloud-first | WAF/HA/DR (b02), product choice (b03) |
| b02 | T1.2, T1.4 | 24 | Well-Architected pillars, HA and fail-over design, scalability, performance and latency, Gemini Cloud Assist, backup and recovery (RTO/RPO); migration plan, Migration Center, methodologies, dependency/network planning, license and financial impact | requirements (b01), services (b03) |
| b03 | T1.3 | 21 | choosing network, storage, compute and data processing products: hybrid/multicloud integration, VPC/peering/Shared VPC/Private Service Connect at design level, object/file/database choice, GKE vs Cloud Run vs Cloud Run functions, spot/custom machine types, AI product choice (Gemini, Agent Builder, Model Garden, AI Hypercomputer) | configuration (b04, b05) |
| b04 | T2.1, T2.3 | 24 | network topologies: hybrid (VPN, Interconnect), multicloud, firewalls, intrusion protection, VPC design, load balancing; compute provisioning, spot vs standard, serverless networking, VMware Engine, IaC/patch management, container orchestration | storage (b05) |
| b05 | T2.2, T2.4, T2.5 | 24 | storage configuration: allocation, access, transfer/latency, retention/lifecycle, growth, backup; Agent Platform Pipelines, data integration, AI Hypercomputer GPUs/TPUs/consumption models; Google AI APIs (Search, Conversation, Vision, Image, Video, Audio), Gemini Enterprise agents and NotebookLM, Model Garden | design-level product choice (b03) |
| b06 | T3.1 | 28 | IAM, resource hierarchy, key management/CMEK/Cloud KMS, secrets, separation of duties, audit, VPC Service Controls, context-aware access, organization policy, hierarchical firewall policy, IAP, impersonation, Workload Identity Federation, Chrome Enterprise Premium, software supply chain, securing AI (Model Armor, Sensitive Data Protection) | compliance (b07) |
| b07 | T3.2, T4.1 | 28 | T3.2 (20): laws and regulation (health records, children's privacy, data sovereignty), PII/card data, SOC 2 style certifications, audits and logs; T4.1 (8): SDLC, CI/CD, root cause analysis, testing | rest of T4.1 (b08) |
| b08 | T4.1, T4.2 | 25 | T4.1 (13): troubleshooting, testing and validation, service catalog and provisioning, disaster recovery; T4.2 (12): stakeholder and change management, team skills, decision making | rest of T4.2 (b09) |
| b09 | T4.2, T5.1 | 25 | T4.2 (8): customer success, cost/resource optimization (CapEx/OpEx), business continuity; T5.1 (17): deployment, API management with Apigee, testing frameworks, data and system migration tooling, Gemini Cloud Assist | T5.2 (b10) |
| b10 | T5.2, T6.1, T6.2 | 27 | T5.2 (17): Cloud Shell/Cloud Code, SDKs (gcloud, gsutil, bq), emulators, IaC/Terraform, API best practices, client libraries; T6.1 (5) operational excellence pillar; T6.2 (5) Observability: monitoring, logging, profiling, alerting | T6.3-T6.6 (b11) |
| b11 | T6.1-T6.6 | 24 | operational excellence pillar, deployment and release management, supporting deployed solutions, quality control, reliability in production (chaos engineering, penetration and load testing); few extra T6.2 | covered in b10 |

Waves (about 4 writers at a time): b01, b03, b06, b09; then b02, b04, b07, b10; then b05, b08, b11.
