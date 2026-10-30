# Google Cloud exams — facts and writing rules

Read this before any `GCP-*` work. Facts come from the exam page (cloud.google.com/learn/certification/...), the
exam guide PDF it links (services.google.com/fh/files/misc/...) and the product docs on docs.cloud.google.com only.
Read docs with `python3 tools/learn_fetch.py --grep "<terms>" <url>` (shared cache).

## Exams

### GCP-ACE Associate Cloud Engineer (added 2026-10-30)
Sources: https://cloud.google.com/learn/certification/cloud-engineer and the standard exam guide
https://services.google.com/fh/files/misc/associate_cloud_engineer_exam_guide_english.pdf (read 2026-10-30). The exam
page says: "This exam was updated to reflect recent branding changes. Refer to the exam guide to review product names
used on the exam."

| Item | Value |
|---|---|
| Length | 2 hours |
| Questions | "50-60 multiple choice and multiple select questions". This bank assumes 55 (mock length only) |
| Pass mark | Not published (pass/fail). `exam-specs.json` has `passMarkUnpublished: true`; the mock uses the 80% target |
| Domains | D1 setting up a cloud solution environment ~20%, D2 planning and implementing ~30%, D3 ensuring successful operation ~30%, D4 configuring access and security ~20% |
| Prerequisites | None; 6+ months hands-on recommended |

## Codes and task ids
- Google Cloud exams have no codes: this bank uses `GCP-` + an abbreviation. Vendor `gcp`, tab "Google Cloud".
- `GCP-ACE` (Associate Cloud Engineer), level `associate`; tasks T1.1-T4.2 are the guide's 12 numbered sections
  (1.1, 1.2, 2.1-2.4, 3.1-3.4, 4.1, 4.2), recorded in `tools/qgen/tasks.json` (Korean) and `data/exam-tasks.json`.

## Writing rules
- Use the product names of the current exam guide: Cloud Run functions (not Cloud Functions), Google Cloud
  Observability (Cloud Monitoring, Cloud Logging), Cloud Next Generation Firewall (Cloud NGFW) policies, Google Cloud
  Hyperdisk, Gemini Enterprise Agent Platform (formerly Vertex AI; Agent Runtime formerly Vertex AI Agent Engine,
  Workbench formerly Vertex AI Workbench), Gemini Cloud Assist, Google Cloud Managed Service for Apache Kafka /
  Prometheus. When docs still show an old name, use the guide's name and mention the old one once in G: if helpful.
- ACE is hands-on: scenarios about a small team running projects. `gcloud`, `gsutil`/`gcloud storage`, `kubectl` and
  `bq` commands are fine when each flag is checked on docs.cloud.google.com; keep snippets short and test what a
  command does, not memorised flag trivia the docs don't show. Prefer `gcloud storage` over `gsutil` (docs call
  gsutil legacy).
- No prices or free-tier numbers. "Estimating costs" questions use the Pricing Calculator, storage classes'
  minimum storage durations and retrieval fees as concepts, never dollar amounts.
- Nothing in preview is keyed; check the docs' "Preview" banner. Retired products are never the right answer:
  Container Registry shut down 2025-03-18 (use Artifact Registry); Cloud Deployment Manager reached end of support
  2026-03-31 (use Infrastructure Manager or Terraform).
- IAM: basic roles (Owner/Editor/Viewer) are discouraged in production; prefer predefined roles; custom roles exist at
  organization or project level (not folder). Verify each role name (`roles/...`) on the docs before keying it.
- Write in the detailed style of CLAUDE.md (G/W/X/T) and list the docs pages relied on as `# src:` lines.
