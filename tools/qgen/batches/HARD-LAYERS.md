# Hard layers for every live exam (owner 2026-11-17: "순서대로 해")

Each live exam gets 40 exam-level (level `advanced`) + 20 expert (level `expert`) questions, the same method as
DEA-C01, SAA-C03 and the foundational exams. Rules per level:
- associate/professional/specialty/expert exams: `batches/DEA-C01/PLAN.md` ("hard set" and "expert tier").
- foundational exams: `batches/FOUNDATIONAL-HARD.md`.
Tier gate (qgen `tier_of`): exam = stem >= 55 words AND average option >= 13 words (or Select THREE).
Vendor rules override these: Palantir = single answer, 4 options, no multi-answer (`tools/qgen/PALANTIR.md`);
Azure `AZURE.md`; Google Cloud `GCP.md`; Databricks `DATABRICKS.md`; Terraform `TERRAFORM.md`; Vault `VAULT.md`.
Process: one writer per exam writes both files (next two batch numbers), one reviewer per file (blind solve),
ingest serially, one PR per wave of 4 exams, changes.py, merge.

Order (lowest exam-level share first, retiring exams skipped: DVA-C02, MLA-C01, ANS-C01):
1 DP-900, PLTR-APD, PLTR-AWARE, TF-IEP002
2 TF-TA004, VLT-VA003, PLTR-DE, AIB-C01
3 AI-901, SC-900, DBX-MLA, DBX-DAA
4 PLTR-AIE, DBX-ASD, AZ-305, DBX-GAI
5 SCS-C03, SOA-C03, DBX-MLP, GCP-GAIL
6 DBX-DEA, MLA-C02, DOP-C02, AIP-C01
7 GCP-PDE, GCP-CDL, DVA-C03, GCP-ACE
8 GCP-PSE, AZ-104, AI-103, DBX-CEA
9 DBX-DEP, GCP-PCA, SAP-C03
Then: worst 1-cue questions (cue pass 2).
