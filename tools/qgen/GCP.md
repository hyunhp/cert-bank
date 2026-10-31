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

### GCP-PCA Professional Cloud Architect (added 2026-10-31)
Sources: https://cloud.google.com/learn/certification/cloud-architect and the standard exam guide
https://services.google.com/fh/files/misc/professional_cloud_architect_exam_guide_english.pdf (read 2026-10-31); the four
case studies (v6.1) are linked from it: `.../v6.1_pca_{altostrat_media,cymbal_retail,ehr_healthcare,knightmotives_automotive}_case_study_english.pdf`.
The exam page says it "was updated to reflect recent branding changes. Refer to the exam guide to review product names".

| Item | Value |
|---|---|
| Length | 2 hours |
| Questions | "50-60 multiple choice and multiple select questions". This bank assumes 55 (mock length only) |
| Pass mark | Not published. `passMarkUnpublished: true` |
| Case studies | 2 per exam, 20-30% of the questions, 4 published (digest: `tools/qgen/GCP-PCA-cases.md`) |
| Sections | D1 design and plan ~25%, D2 manage and provision ~17.5%, D3 security and compliance ~17.5%, D4 analyze and optimize processes ~15%, D5 managing implementation ~12.5%, D6 solution and operations excellence ~12.5% |
| Tasks | 22: 1.1-1.5, 2.1-2.5, 3.1-3.2, 4.1-4.2, 5.1-5.2, 6.1-6.6 (`data/exam-tasks.json`) |
| Prerequisites | None; 3+ years industry, 1+ year designing on Google Cloud recommended. Cert valid 2 years |

Writing rules (in addition to the shared ones below):
- Professional depth: design decisions and trade-offs against business and technical requirements (availability, cost, latency,
  compliance, migration effort), not command syntax. No console click paths, no prices, limits or quotas.
- About 25% of questions build on one of the four case studies: the stem names the business and gives the one or two facts the
  decision needs, in own words (digest only; never copy the case text). Spread the cases; one case per question.
- Well-Architected Framework pillars (operational excellence, security, reliability, performance optimization, cost
  optimization, sustainability) frame the answers; use the guide's names: Gemini Enterprise Agent Platform / Agent Platform,
  Gemini Cloud Assist, Model Armor, Chrome Enterprise Premium, Migration Center, Cloud Run functions.
- Preview or deprecated features stay out of keys (Deployment Manager ended 2026-03-31; Infrastructure Manager or Terraform instead).
- Overlap: GCP-ACE (hands-on) and GCP-CDL / GCP-GAIL share product facts; read their published questions first, test the
  architect's choice (which design and why), not the console step.

### GCP-GAIL Generative AI Leader (added 2026-10-30)
Sources: https://cloud.google.com/learn/certification/generative-ai-leader and the exam guide
https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf (read 2026-10-30; the exam page
says "This exam was recently updated to reflect branding changes. Refer to the exam guide to review product names").

| Item | Value |
|---|---|
| Length | 90 minutes |
| Questions | "50-60 multiple choice questions". This bank assumes 55 (mock length only) |
| Pass mark | Not published (pass/fail). `passMarkUnpublished: true` |
| Domains | D1 fundamentals of gen AI ~30%, D2 Google Cloud's gen AI offerings ~35%, D3 techniques to improve model output ~20%, D4 business strategies ~15% |
| Prerequisites | None. Business-level: strategy and influence, "not technical implementation" |

### GCP-CDL Cloud Digital Leader (added 2026-10-30)
Sources: https://cloud.google.com/learn/certification/cloud-digital-leader and the exam guide
https://services.google.com/fh/files/misc/cloud_digital_leader_exam_guide_english.pdf ("launched on August 12, 2026"; the
exam page says "As of August 12, the new version of the exam is now live").

| Item | Value |
|---|---|
| Length | 90 minutes |
| Questions | "50-60 multiple choice and multiple select questions". This bank assumes 55 (mock length only) |
| Pass mark | Not published (pass/fail). `passMarkUnpublished: true` |
| Domains | D1 digital transformation ~18%, D2 data transformation ~18%, D3 AI ~18%, D4 modernize infrastructure and applications ~18%, D5 trust and security ~18%, D6 scaling with operations ~10% |
| Prerequisites | None; "experience collaborating with technical professionals" recommended |

## Codes and task ids
- Google Cloud exams have no codes: this bank uses `GCP-` + an abbreviation. Vendor `gcp`, tab "Google Cloud".
- `GCP-ACE` (Associate Cloud Engineer), level `associate`; tasks T1.1-T4.2 are the guide's 12 numbered sections
  (1.1, 1.2, 2.1-2.4, 3.1-3.4, 4.1, 4.2), recorded in `tools/qgen/tasks.json` (Korean) and `data/exam-tasks.json`.

- `GCP-GAIL` (Generative AI Leader), level `foundational`; tasks T1.1-T4.3 are the guide's 15 numbered sections (1.1-1.4,
  2.1-2.5, 3.1-3.3, 4.1-4.3), in `tools/qgen/tasks.json` (Korean) and `data/exam-tasks.json`. The guide repeats the
  data bullets of 1.1 under 1.2: questions about data types and quality go to T1.2.

- `GCP-CDL` (Cloud Digital Leader), level `foundational`; tasks T1.1-T6.2 are the guide's 14 numbered sections (1.1, 1.2,
  2.1-2.3, 3.1, 3.2, 4.1-4.3, 5.1, 5.2, 6.1, 6.2), in `tools/qgen/tasks.json` (Korean) and `data/exam-tasks.json`.

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
- Cloud Storage has five storage classes: Standard, Nearline, Coldline, Archive and Rapid (zonal buckets only); never
  write "all classes" when only the four location-flexible ones are meant.
- IAM: the basic roles are now Admin, Writer and Reader (`roles/admin`, `roles/writer`, `roles/reader`); Owner, Editor
  and Viewer are "legacy basic roles" (no IAM Conditions). Basic roles of either set are discouraged in production;
  prefer predefined roles; custom roles exist at
  organization or project level (not folder). Verify each role name (`roles/...`) on the docs before keying it.
- Write in the detailed style of CLAUDE.md (G/W/X/T) and list the docs pages relied on as `# src:` lines.
- GCP-GAIL is a business-level exam: stems are about choosing the right product, approach or practice for a business
  need, never commands, code or console steps. Product names follow the guide: Gemini Enterprise Agent Platform
  ("Agent Platform", formerly Vertex AI), Agent Search, Conversational Agents, Gemini Enterprise, Gemini for Google
  Workspace, Model Garden, Agent Studio, Google AI Studio, Secure AI Framework (SAIF). When docs still show an old
  name (Vertex AI, Dialogflow, Agentspace), use the guide's name and mention the old one once in G: if helpful.
- Gen AI products change fast: nothing in preview, no model version numbers, context-window sizes, prices, limits,
  regions or plan names in keyed answers. Test the capability and the reason to choose it.
- Unreachable hosts (network policy): workspace.google.com, ai.google.dev, deepmind.google, saif.google,
  support.google.com. Gemini for Workspace, Gemma, Imagen, Veo and SAIF facts come from cloud.google.com and
  docs.cloud.google.com pages (products/gemini-for-workspace, Model Garden and generative-ai model pages,
  transform/secure-ai-framework); claims those pages do not settle are left out.
- GCP-CDL is a business-level exam like GCP-GAIL: stems describe a business goal and ask which approach, product or
  benefit fits; no commands, flags or console steps. Use the guide's current names (Managed Service for Apache Spark,
  Gemini Enterprise Agent Platform / Agent Platform, Google Security Operations, Google Threat Intelligence, AI
  Protection, Model Armor, Cloud Run functions). Same rules as GCP-GAIL: nothing preview or deprecated keyed, no prices,
  limits, plan or tier names, no model versions. Product facts overlap GCP-ACE (hierarchy, storage classes, IAM) and
  GCP-GAIL (AI, security tools): test the business value and the reason to choose, not the configuration, and read
  `data/GCP-ACE.json` / `data/GCP-GAIL.json` questions before writing so scenarios are not repeated.
