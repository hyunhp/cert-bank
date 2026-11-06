# GCP-PSE study guide plan (23 days)
Rules: `tools/study/README.md` (data shape) and `tools/qgen/GCP.md` (GCP-PSE section: names, renames, preview rule). Sources: the exam guide
(read 2026-11-06) and docs.cloud.google.com only (`python3 tools/learn_fetch.py --grep "<terms>" <url>`, shared cache). Built from the reviewed bank
(`data/GCP-PSE.json`, `data/explanations/GCP-PSE.json`) plus the docs; keep claims the bank already verified, re-check anything new (the PDE guide reviewers still fixed
about 15 claims per writer that had not been re-checked: run the docs check yourself).
Shape per day: see `data/study/GCP-PCA.json` and `data/study/GCP-PDE.json` (day, domain, title, services, concepts[{heading,body}], examPoints, quiz[2], recap).
3-4 concepts of 120-190 words, 3 examPoints, quiz = 2 questions with 4 choices, `answer` is a 0-3 integer index, correct choice never the longest, no letter references in explanations.

| Day | Domain | Tasks | Topic |
|---|---|---|---|
| 1 | D1 | T1.1 | Cloud Identity: Google Cloud Directory Sync, SSO with a third-party IdP, super admin protection, user lifecycle automation, groups via API |
| 2 | D1 | T1.2 | service accounts: default SAs, securing and auditing keys, disabling key creation, short-lived credentials |
| 3 | D1 | T1.1, T1.2 | federation and impersonation: Workforce Identity Federation, Workload Identity Federation, service account impersonation |
| 4 | D1 | T1.3 | authentication: password and session policy at architecture level, SAML and OAuth, token types, 2-step verification |
| 5 | D1 | T1.4 | authorization I: privileged roles, separation of duties, IAM vs ACL, IAM conditions, deny policies, groups, Privileged Access Manager |
| 6 | D1 | T1.4, T1.5 | authorization II and hierarchy: Access Context Manager, Policy Intelligence, Principal Access Boundary, folders/projects at scale, org policies, inheritance |
| 7 | D2 | T2.1 | perimeter I: Cloud NGFW rules, policies, layer 7 inspection; Cloud Armor; IAP; load balancers; Certificate Authority Service |
| 8 | D2 | T2.1 | perimeter II: public vs private IP, Secure Web Proxy, Cloud DNS security, restricting and monitoring APIs |
| 9 | D2 | T2.2 | VPC Service Controls: perimeters, access levels, ingress/egress rules, dry run |
| 10 | D2 | T2.2 | segmentation: VPC security properties, peering, Shared VPC, firewall rules, N-tier isolation |
| 11 | D2 | T2.3 | private connectivity: Private Google Access, restricted Google access, Private Service Connect, HA VPN, Interconnect and MACsec, Cloud NAT |
| 12 | D3 | T3.1 | Sensitive Data Protection: discovery, redaction, pseudonymization, format-preserving encryption |
| 13 | D3 | T3.1 | restricting data access (BigQuery, Cloud Storage, Cloud SQL), Secret Manager, instance metadata |
| 14 | D3 | T3.2 | encryption at rest: default vs CMEK vs EKM, software vs HSM keys, rotation, revocation, import, Autokey |
| 15 | D3 | T3.2 | encryption in transit and in use: TLS/SSL policies, Confidential Computing, Cloud Storage lifecycle policies |
| 16 | D3 | T3.3 | securing AI workloads: privacy controls, IaaS vs PaaS training, Model Armor, Gemini Enterprise Agent Platform controls |
| 17 | D4 | T4.1 | supply chain: CVE scanning in CI/CD, Artifact Analysis, Binary Authorization, hardened images, VM patch management |
| 18 | D4 | T4.1 | posture and drift: CSPM in Security Command Center, custom organization policies, Security Health Analytics custom modules |
| 19 | D4 | T4.2 | network logs: Cloud NGFW logging, VPC Flow Logs, Packet Mirroring, Cloud IDS, Log Analytics (Observability Analytics) |
| 20 | D4 | T4.2 | audit logs and detection: Cloud Audit Logs, sinks and aggregated sinks, access to logs, SIEM export, Security Command Center |
| 21 | D5 | T5.1 | shared responsibility, scoping, mapping requirements to controls, Assured Workloads |
| 22 | D5 | T5.1 | Access Transparency, Access Approval, data and service regionalization, evidence |
| 23 | null | all | final review: decision cheat-sheet across the 5 domains, 2 quiz questions |

Writers: w1 days 1-6, w2 days 7-11, w3 days 12-16, w4 days 17-23. Each writes ONLY `tools/study/drafts/GCP-PSE/wN.json` (a JSON list of day objects).
