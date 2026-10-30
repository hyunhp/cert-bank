# TODO

## Now (warm start — keep this section current; update it with every merge)
Updated 2026-10-30.
- In progress: **GCP-CDL study guide** (bank merged: 226 questions, b01-b11). If the session was cleared: start from `main`,
  branch `gcp-cdl-study`, two writers + two reviewers on scratch JSON as for GCP-GAIL (facts from the reviewed bank and
  cloud.google.com / docs.cloud.google.com only; about 15 days, one per exam-guide section group; D6 shorter), a
  `STUDY_EXAMS` entry (vendor `gcp`, foundational) in `js/study.js`, stamp_version, build_data_index, glossary `gcp-*` terms
  (Sonnet review), README study-days column, tests, merge. Open gaps: Gemini app and Gems (GAIL T2.2, blocked hosts);
  CDL golden signals / CapEx-OpEx / data-type definitions use generally accepted meanings (no reachable Google page).
- Done this cycle (all merged): Google Cloud vendor + GCP-ACE bank and study guide; GCP-GAIL bank and study guide; GCP-CDL bank; AI-901, AI-103, AZ-305, SC-900, DP-900 banks, study guides and glossary terms; Resume button;
  docs cache + `qgen check --siblings` + PLAN.md workflow; tech-debt pass.
- Next: Microsoft list is covered for now (AI-500 has no skills list yet, AZ-401 is beta). www.databricks.com is still
  blocked; learn.palantir.com / certification.palantir.com answer 403 (site side). Google Cloud exam pages, guide PDFs
  (services.google.com) and docs.cloud.google.com are reachable.
- Working style the owner asked for: merge reviewed work once all tests pass (merge permission rule is set), then
  report; start question writers in waves of about 4 (a 5-hour usage limit stopped 10 parallel writers once); reviewers
  start as each writer finishes; Sonnet for glossary/format checks; reports short.
- Token baseline: with the cache/PLAN workflow reviewers use ~50-75k tokens per batch (90-160k before), writers ~75-110k.

## AWS exam versions (checked 2026-10-27)
Notices live in `data/exam-specs.json` ("update"), shown above the section filters and in mock setup.
- SAP-C02 -> SAP-C03: DONE 2026-10-27 from the official guide (docs.aws.amazon.com, 2026-10-27): 5 domains
  25/25/15/15/20, 18 tasks, 65 scored + 10 unscored, passing 720 (time not in the guide; 180 min assumed).
  All 396 SAP-C02 questions classified against the C03 skills: 388 shared with their new task (shares.json "tasks"
  rule, data/exam-shared-tasks.json), 8 excluded (Service Catalog, Migration Hub, Snowball Edge, VMware Cloud on
  AWS, Well-Architected Tool). 13 updated in SAP-C02/f02 (AWS Transform MGN, Security Hub CSPM, re-keyed discovery
  and AWS Batch questions). 120 new in batches/SAP-C03/b01-b06 (AI/ML integration, responsible AI and post-quantum,
  AI cost/evaluation/monitoring, and every skill that had no question), each reviewed and deduplicated across
  batches. Pool 508, then 505 (2026-10-29: the 3 Migration Evaluator questions excluded, see section 1), now 509. SAP-C03 study guide DONE 2026-10-29 (38 days, below). Open: after 2026-11-16 decide whether to
  hide SAP-C02.
  Bedrock Guardrails org-level enforcement (AWS Organizations Bedrock policy, GA 2026-04): DONE 2026-10-29, 4 questions
  in batches/SAP-C03/b07 (Q006460-Q006463: per-Region management-account guardrail + version + resource policy, member
  ApplyGuardrail permission, declarative-policy inheritance, model exclusions and selective guarding), reviewed. Pool 509.
- DVA-C02 -> DVA-C03: DONE 2026-10-27 from the official guide (docs.aws.amazon.com, developer-associate-03, 2026-10-27):
  same 4 domains 30/26/22/22, 12 tasks (new T2.3 AI service security; C02 T2.3 merged into T2.2, T3.2+T3.3 into
  T3.2, T3.4 became T3.3), 50 scored + 15 unscored, passing 720 (time not in the guide; 130 min assumed). Last C02 day
  2026-11-30; C03 exam and registration from 2026-12-01. All 395 DVA-C02 questions classified: 390 shared with their
  C03 task (shares.json "tasks"), 5 excluded (Amazon Q Developer, CodeGuru Profiler, App Runner: not in the C03
  in-scope list). 80 new in batches/DVA-C03/b01-b04 (AI service security; Kiro and Bedrock integration; AI tools for
  tests, CI/CD, troubleshooting and optimization; container builds/deploys, signed URLs, probes, alerts), each
  reviewed and deduplicated across batches. Pool 470. Kiro facts checked only via raw.githubusercontent.com
  (kirodotdev README/demo repo): kiro.dev and aws.amazon.com are blocked here; re-check the Kiro questions
  (b02, b03) if Kiro docs become reachable. DVA-C03 study guide DONE 2026-10-29 (30 days, below). Open: after
  2026-12-01 decide whether to hide DVA-C02.
- MLA-C01 -> MLA-C02: DONE 2026-10-23. MLA-C02 registered (same four domains, 28/24/24/24; same twelve tasks, so
  `tasksFrom: MLA-C01`); `tools/qgen/shares.json` shares 389 MLA-C01 questions (6 excluded: SageMaker Neo / model
  compression, removed in C02) and 80 new GenAI questions in batches/MLA-C02/b01-b04 (vector stores and RAG data,
  FM selection/customization/evaluation, FM deployment/agents/CI-CD, FM monitoring/cost/guardrails), each reviewed.
  Task titles came from AWS's C01/C02 comparison page via secondary sources: re-check against the GA guide (2027-01-14)
  and then drop MLA-C01 from the site.
- ANS-C01: retires 2026-12-31, no successor. Keep the bank (credentials stay valid 3 years); consider hiding it later.
- No change found for CLF-C02, AIF-C01, AIB-C01 (new, beta from 2026-09-29), SAA-C03, DEA-C01, SOA-C03, DOP-C02,
  AIP-C01, SCS-C03 (only three language versions end 2026-12-31).


- `support.html` live with KakaoPay (domestic; QR on computers, app link on phones, `tools/support_test.py`), merged in PR #9/#11; repo Sponsor button via `.github/FUNDING.yml` -> support.html. Ko-fi (international, PayPal payout) live 2026-10-27: https://ko-fi.com/hyunhopark.
- Toss ID (toss.me) closed 2024-08-01; KakaoBank has no receive link; Naver Pay dropped (owner, 2026-10-22).
- No ads (owner decision 2026-10-22: AdSense considered and dropped; the support page and README promise "no ads").

## Study guide (started 2026-10-22) — terse handoff
- SAP-C03 (38 days, 5 domains) and DVA-C03 (30 days) — DONE 2026-10-29. Plans cover every skill of the official C03
  guides (docs.aws.amazon.com, read 2026-10-29); five writers drew on the reviewed C03 batches and the C02 guides, then
  four independent reviewers checked each claim against docs.aws.amazon.com (35 fixes, e.g. Migration Evaluator ->
  AWS Transform assessment, Aurora Serverless v2 scales to 0 ACU, Cognito email MFA). Glossary tags extended (SAP-C03
  37 terms, DVA-C03 27). C02 guides left unchanged.
Rules/design: `tools/study/README.md`. Private owner notes (routines, artifact links): owner's private doc "cert-bank 학습 가이드 이관 인계 메모" (source of truth) + local copy `.handoff/SESSION.md`
(git-ignored, local only; ask owner if missing).
Phases:
- P1 data `data/study/<EXAM>.json` 12 exams/349 days — DONE (main, PR #1).
- P1.5 retired-service review — DONE. Also fixed: Firehose name, Cognito refresh token not JWT, CMK name,
  FIS name, DNSSEC KSK (KMS us-east-1, no CloudHSM), DX MTU (priv 9001/transit 8500/VPN 1446), Entra ID,
  Bedrock InvokeModel = CloudTrail management event.
- P2 `study.html` + `js/study.js` — DONE (main). No timeline (owner dropped it). Progress via `StudyStore` only.
- P3 glossary popovers + level tabs + default exam — DONE (main, PR #2). 233 terms; owner wants fewer-but-useful
  marks (a "≥1 mark every day" pass was tried and reverted: weak/basic terms).
- CLF-C02 (Cloud Practitioner) 14-day guide — DONE (main, PR #2), independently fact-checked.
- CLF-C02 question bank 2026-10-23: exam registered in exam-specs/tasks; 325/325 questions in b01-b14 (each batch
  written by its own writer and independently fact-checked before ingest; reviewers replaced ~15 near-duplicates and
  fixed e.g. the AWS CAF phases: Envision, Align, Launch, Scale). Pool complete; add more only for new topics.
  Support plans are mid-change (new plans Dec 2025; Developer/Business/Enterprise On-Ramp end 2027-01-01): keep
  plan-tier claims out of keyed answers until the old plans are gone.
- Palantir study guides PLTR-DE/AIE/APD (17 days: 2 per domain + final) — DONE 2026-10-22, built only from the
  reviewed PLTR bank + PALANTIR.md facts, independently reviewed. Study page and question bank both use
  vendor tabs → level segments → named exam chips; question bank section filters sit in a shaded panel.
- 2026-10-22 polish (PR #5, #6): level segment always shown (Palantir shows "Associate"; Specialist is hands-on,
  out of scope); study-guide link text vendor-neutral; README rewritten user-facing in EN (README.md) + KO
  (README.ko.md) with a Ctrl/Cmd-click tip (GitHub strips target=_blank, so links can't force a new tab).
- Nothing open in this section (P5 backend dropped by the owner on 2026-10-22: not planned).
- Kendra/Q Business availability notes on 19 AIB/AIF/AIP questions — DONE (explain batches AIF-C01/e14, AIP-C01/e16).
- P4 cutover — DONE 2026-10-22: old 9am progress routine deleted; new routine "학습 가이드 리마인드" weekdays 06:50 KST
  (13 exam links incl. CLF-C02; Gmail connector attached by owner); 26 old artifacts deleted.
- Rulesets for main: set up by owner 2026-10-22 (PR required). Work on a branch, open a PR, merge via API.
- P5 backend (Cognito OTP, API GW/Lambda/DynamoDB, Scheduler, SES): dropped 2026-10-22, not planned; the design
  notes in `tools/study/README.md` stay for reference only.
Test noise fixed 2026-10-22: `bookmark_backup_test` "toast shown" (the test read the toast after it had gone; now
records toasts as they appear) and `diagrams/check.py` (5 layout errors fixed in `tools/diagrams/src`). All suites
should pass; a failure is real. Playwright here: `pip install playwright==1.56.0` (matches /opt/pw-browsers chromium-1194).

## Microsoft Azure (started 2026-10-29)
Owner chose Azure as the third vendor (2026-10-29); learn.microsoft.com is allowed in the environment's network
settings. Rules and checked facts: `tools/qgen/AZURE.md`. AZ-900 registered (vendor `azure`, 3 domains, weights are
the midpoints of the published ranges, 45 questions assumed). Pilot DONE 2026-10-29: 60 questions (b01-b03, 20 per
domain, 9 multi-answer), each batch reviewed against Learn (17 fixes, incl. 3 near-duplicates across batches rewritten).
Note: the AZ-900 Learn training unit still says region pairs fail over automatically; the reliability docs say they
do not, and the bank follows the reliability docs (AZURE.md).
AZ-900 at target DONE 2026-10-29: 225 questions (b01-b11, 35 multi-answer, every task 18-22). b04-b11 (165) were
written in parallel by subtopic and each independently reviewed against Learn; reviewers replaced ~25 near-duplicates
of published or sibling questions and simplified over-deep ones to fundamentals level. Lesson: parallel writers in the
same task drift into the same scenarios (Spot for rendering, month-end scale-up); ingest reviewed batches as they
finish and tell the remaining reviewers what was just published.
AZ-900 study guide DONE 2026-10-29: 14 days (D1 3, D2 6, D3 4, final), two writers + independent Learn review
(10 fixes). Glossary: only 8 vendor-neutral terms tagged AZ-900; most existing definitions name AWS services, so
Azure-specific terms (resource group, management group, Azure RBAC, Microsoft Entra ID ...) still need drafting + review.
AZ-104 DONE 2026-10-29: registered (5 domains, midpoint weights, 50 questions assumed, 100 min), 250 questions in
b01-b15 (one batch per skill group so parallel writers could not collide; each independently reviewed against Learn, ~110
fixes incl. 3 wrong keys and ~15 cross-batch duplicates), study guide 32 days. Five explanations had markdown tables
(converted, e01; qgen check now rejects tables); ``` fences now render as code blocks (29 older DVA explanations used them).
Azure glossary: 36 Azure terms (az-* ids, separate from the AWS-worded entries). 2026-10-29: +20 for AZ-104 (NSG, peering,
SAS, private/service endpoints, LRS..GZRS, service tags, UDR, Recovery Services vault, KQL, scale/availability sets, Bicep,
Bastion, DCR, SSPR, Key Vault, gateway transit, private DNS zone, ExpressRoute; 7 also tagged AZ-900), Learn-reviewed
(7 fixes). AZ-104 now 38 tagged terms (31 of 32 days marked), AZ-900 31.
Next Azure exams (checked on Learn 2026-10-29; every guide says "A score of 700 or greater is required to pass"):
- Retired: AI-102 (2026-06-30, successor AI-103), AI-900 (2026-06-30, successor AI-901), AZ-204 (2026-07-31) and
  AZ-500 (certification retired 2026-08-31); Learn names no successor for AZ-204/AZ-500 (the retirement posts are on
  techcommunity.microsoft.com, blocked here).
- Live: AI-901 Azure AI Fundamentals (skills as of 2026-04-15; AI concepts 40-45%, Microsoft Foundry solutions 55-60%;
  45 min per the exam-duration page); AI-103 Developing AI Apps and Agents on Azure (2026-04-16; 5 domains, 120 min,
  interactive items); AZ-305 (2026-04-17; 4 domains, requires AZ-104, case studies); DP-900 (2026-07-21, 45 min);
  SC-900 (2026-10-21, 45 min). New: AI-500 multi-agent expert (no skills list yet), AZ-401 agentic DevOps (beta).
- Recommended order: AI-901 (pairs with AIF-C01, no labs), then AI-103 (pairs with AIP-C01/MLA-C02), then AZ-305
  or SC-900/DP-900.
AI-901 DONE 2026-10-29: registered (2 domains, midpoint weights 42.5/57.5, 45 questions assumed, 45 min), 225 questions in
b01-b09 (one batch per skill group or half of one, 38 multi-answer), each independently reviewed against Learn (~110 fixes:
~20 near-duplicates across batches, fundamentals depth for SDK/API trivia in b07-b09, preview paths replaced by GA ones,
e.g. gpt-audio chat completions -> gpt-realtime). Reviewed batches were ingested as they finished and later reviewers
were told what had just been published, which caught most cross-batch overlap. AI-901 study guide DONE 2026-10-30: 13 days (D1 5, D2 7, final), two writers +
two independent Learn reviewers (17 fixes); glossary +10 terms (few-shot, fine-tuning, multimodal, system message, SLM,
transformer, SSML, DefaultAzureCredential, NER, OCR; Learn-reviewed) and 16 vendor-neutral/az-* terms tagged AI-901. Foundry changes fast (agents classic retire 2027-03-31, Azure Language legacy features 2029-03-31, Language
Studio 2027-03-20, Image Analysis/Custom Vision 2028-09-25), re-check with section 1.
AI-103 DONE 2026-10-30: registered (5 domains, midpoint weights, 50 questions assumed, 120 min), 243 questions in b01-b10
(every domain at its target; 39 multi-answer), each batch independently reviewed against Learn (~100 fixes, ~25 cross-batch
overlaps replaced as batches were ingested one by one). Facts found: Azure OpenAI On Your Data retired 2026-10-14 (Foundry
IQ knowledge base or classic RAG instead); Foundry portal workflows retire 2026-12-01 (Microsoft Agent Framework);
Connected Agents gone from the new Agent Service (a2a tool v1.0 GA); Sora 2 video is preview, no GA video model (2 stems
say so); Memory, agent guardrails, many agent evaluators, agent Monitor tab metrics are preview; sku capacity units per TPM
differ by model. AI-103 study guide DONE 2026-10-30: 20 days (D1 5, D2 6, D3 3, D4 2, D5 3, final), two writers +
two Learn reviewers (22 fixes); glossary +9 Azure terms (RRF, semantic ranker, TPM/RPM, Application Insights, skillset, A2A,
NMT, WER, Content Credentials; reviewed with Sonnet) and 28 existing terms tagged AI-103.
AZ-305 DONE 2026-10-30: registered (4 domains, midpoint weights, 50 questions assumed, 100 min assumed, new `expert`
level segment), 251 questions in b01-b10 written from PLAN.md (topics owned per batch) and reviewed (19 fixes; no
cross-batch overlaps thanks to PLAN.md and `qgen check --siblings`). Reviewers used ~50-75k tokens per batch vs 90-160k
before the token-savings changes. AZ-305 study guide DONE 2026-10-30: 22 days (D1 6, D2 5, D3 4, D4 6, final), two
writers + two Learn reviewers (16 fixes); glossary +9 Azure terms (DTU/vCore, Hyperscale, failover group, RU/s, PIM,
Managed HSM, Virtual WAN, Cloud Adoption Framework, Global Reach; Sonnet-reviewed) and 32 existing terms tagged AZ-305.
SC-900 DONE 2026-10-30: registered (4 domains, midpoint weights, 45 questions, 45 min), 225 questions in b01-b08 from
PLAN.md, reviewed (30 fixes, 0 cross-batch overlaps; e.g. retired "approved client app" grant, eDiscovery (Standard/Premium)
classic retired 2025-08-31, Sentinel moving to the Defender portal after 2027-03-31 kept out of keys). Writers were
started in waves of 4 to stay under the usage limit. SC-900 study guide DONE 2026-10-30: 14 days (D1 2, D2 4, D3 5, D4 2, final), two
writers + two Learn reviewers (15 fixes); glossary +10 Azure terms (SIEM/SOAR, Zero Trust, CSPM/CWPP, CASB, XDR/EDR, DLP,
sensitivity label, federation, FIDO2/passkey, SSO; Sonnet-reviewed) and 16 existing terms tagged SC-900.
DP-900 DONE 2026-10-30: registered, 225 questions in b01-b09 from PLAN.md, reviewed (about 25 fixes, 0 cross-batch
overlaps). Learn facts kept out of keys: Cosmos DB for PostgreSQL on a retirement path (5 APIs taught), Synapse dropped
from the DP-900 module (Fabric + Databricks), Q&A visual retires 2027-02, preview Fabric features; "Azure Data Lake
Storage" (no Gen2) and "Azure DocumentDB" (vCore MongoDB) names as on Learn.
DP-900 study guide DONE 2026-10-30: 14 days (D1 4, D2 3, D3 2, D4 4, final), two writers + two Learn reviewers (about 15
fixes: ORC dropped, SELECT is DML, Session "most widely used" not default, no item-type claims); glossary +10 Azure terms
(normalization, foreign key, DDL/DML, Delta Lake, OneLake, hierarchical namespace, consistency levels, DAX, DirectQuery,
eventstream; Sonnet-reviewed) and acid, star-schema tagged DP-900.

## Google Cloud (started 2026-10-30)
Rules and facts: `tools/qgen/GCP.md`. Vendor `gcp` (tab "Google Cloud"); exams have no codes, so this bank uses `GCP-`.
`exam-specs.json` `passMarkUnpublished: true` (Google publishes no pass mark): the mock says so and aims at 80%.
GCP-ACE DONE 2026-10-30: Associate Cloud Engineer, guide read 2026-10-30 (4 sections ~20/30/30/20%, 12 tasks; 2 h;
50-60 questions, 55 assumed), 250 questions in b01-b11 from PLAN.md, each reviewed (about 40 fixes, e.g. Rapid storage
class, spend cap budgets, VPC Flow Logs now records dropped traffic, Extended release channel, Helm charts as OCI in
Docker-format repos). Docs changes kept out of keys or reflected: Admin/Writer/Reader are the basic roles and
Owner/Editor/Viewer are "legacy basic roles" (f01/e01 fixed 4 earlier questions), Log Analytics is now Observability
Analytics, `gcloud run deploy --function` for Cloud Run functions, Deployment Manager end of support 2026-03-31.
`learn_fetch.py` fix: a stray end tag no longer closes `<main>` (Google docs pages were cut off at tab panels).
GCP-ACE study guide DONE 2026-10-30: 22 days (D1 4, D2 8, D3 7, D4 2, final), three writers + three reviewers (about 25
fixes, e.g. G2 custom machine types, OS Login roles on project/instance, Cloud NGFW implied actions, Cloud TPU API
deprecated, 24 h metric-absence limit); retake waiting periods left out (support.google.com is blocked). Glossary +11
`gcp-*` terms (Sonnet-reviewed). e02 fixed Q008135 (G2 custom types). Study page vendor tabs use the "GCP" short name
on phones like the question bank.

GCP-GAIL bank DONE 2026-10-30: Generative AI Leader (foundational, business-level; 90 min, 50-60 questions, 55 assumed;
D1 30 / D2 35 / D3 20 / D4 15; pass mark not published), 226 questions in b01-b13 from PLAN.md, each reviewed (about 60
fixes). Docs facts kept out of keys or reflected: Video Intelligence API deprecated (shutdown 2027-09-14) so a Gemini
model is the answer; Customer Engagement Suite is now "Gemini Enterprise for Customer Experience" and Dialogflow CX
evolved into CX Agent Studio (questions use the guide's names, G: mentions the new ones); Model Monitoring v2 and several
SCC AI features are Preview (not keyed); SAIF pages unreachable so SAIF questions stay at purpose level; diffusion,
structured/unstructured and labeled/unlabeled data use generally accepted definitions; "extensions" and "plugins" are not
defined on reachable pages. Gap: Gemini app and Gems (T2.2), see Now.
GCP-GAIL study guide DONE 2026-10-30: 15 days (D1 4, D2 5, D3 3, D4 2, final), two writers + two reviewers (about 30 fixes,
e.g. Veo list has no video editing, Model Monitoring v1 only, SAIF at purpose level, no AI Protection vulnerability claim,
Video Intelligence deprecated); retake waiting periods left out (support.google.com blocked). Glossary +13 `gcp-*` terms
(Sonnet-reviewed) and 11 existing terms tagged GCP-GAIL.

GCP-CDL bank DONE 2026-10-30: Cloud Digital Leader (foundational, business-level; new version live 2026-08-12; 90 min,
50-60 questions, 55 assumed; D1-D5 18% each, D6 10%; pass mark not published), 226 questions in b01-b11 from PLAN.md, each
reviewed (about 55 fixes). Docs facts reflected: guide labels replatform "move and improve" while Google's migration docs
say "lift and optimize" (questions describe the action, same answer under both labels); GKE Enterprise has no reachable
definition page (no "formerly Anthos" claim); "compliance resource manager" matches no Google page (the question keys the
Compliance resource center); Looker/BigQuery/Pub/Sub/Dataflow claims softened to what pages say; first-/second-/third-party
data, supply-chain stages, golden signals, CapEx/OpEx, SLI/SLO/SLA use generally accepted definitions, stated in G:.

## Future: other certifications (researched 2026-10-29, not started)
Ideas the owner asked to keep for later. Each needs its vendor's guide and docs hosts allowed in the environment's
network settings (only docs.aws.amazon.com, learn.microsoft.com and cloud.google.com/learn pages are reachable now).
- Palantir Foundry Aware: the entry-level exam of the 2026 framework. Format, cost and proctoring not confirmed
  (community posts conflict); learn.palantir.com / certification.palantir.com are blocked here.
- Google Cloud: Generative AI Leader (50-60 multiple choice, 90 min; pairs with AIF/AIB), Professional Cloud
  Architect (Associate Cloud Engineer done, see the Google Cloud section).
- Databricks Certified Data Engineer Associate (45 multiple choice, 90 min, revised 2026-05-04; pairs with
  DEA-C01 / PLTR-DE). Needs databricks.com and docs.databricks.com.
- HashiCorp Terraform Associate 004 (live 2026-01-08; multiple choice incl. multi-select). Needs
  developer.hashicorp.com.
- Out of scope (hands-on, not multiple choice): Kubernetes CKA/CKAD, Palantir Specialist.

## Palantir (started 2026-10-14)
State 2026-10-15: PLTR-AIE 400, PLTR-DE 400 (b01-b50 each), PLTR-APD 400 (b01-b50: pilot + six rounds + capstone). Rules and checked facts in
`tools/qgen/PALANTIR.md`.
Done 2026-10-15:
- Guides re-read: DE/AIE unchanged (95 q, 70%, no weights); APD guide read (85 q, 3 h, 70%, 8 domains), exam added.
- Doc review of the recurring platform claims (transactions, file syncs, restricted views, markings). Four DE
  questions contradicted the docs and were rewritten in `PLTR-DE/f01.txt` (pinned ids).
- Old Pages address `/aws_qbank/`: owner decided not to redirect (2026-10-15); `/cert-bank/` is the only address.
Next:
- Doc review, second pass done 2026-10-16 (Automate identity/scoping/retries, object and property security
  policies, restricted-view column limits, virtual tables): 5 more questions fixed (PLTR-DE f02, PLTR-APD f01).
- D6/D8 precise review done 2026-10-16 (165 control-naming questions, NOT stems, AI FDE items): 3 more fixed.
  Total 12 questions corrected by doc review. Palantir work is closed; reopen only when a guide changes or a
  learner reports an error (record the doc URL with the fix, as in PALANTIR.md).
- Re-check the guides before each phase; if weights appear, replace the equal weights and drop `weightsAssumed`.

State on 2026-09-30: 4,502+ questions in 12 exams, all with detailed explanations (`data/explanations/<EXAM>.json`).
Done the same day (see git log): bookmarks load only needed exams, explanations split from exam files, section
(domain/task) filter chips with per-domain accuracy (localStorage only) and "one section only" mock exams,
`qgen check` guards superseded blocks, `.claude/agents` has explanation-writer / batch-reviewer / question-writer /
fix-writer. Reinforcement batches (each fact-checked by an independent reviewer before ingest): AIF D4 +30,
AIP D3 +30, AIB D3 +20, and +20 in the security/governance domain of DEA (D4), SAA (D1), DVA (D2), SOA (D4),
MLA (D4), SAP (T1.2/T1.4/T2.3/T3.2), DOP (D6), ANS (D4), SCS (D6). Pools are now 356-445 per exam.

## 0. Open idea: answer-position/length stats after the reinforcement
`python3 tools/qgen/qgen.py report` is clean (no length bias flags over the limit); nothing to do unless new
batches are added.

## 1. Keep availability notes current
Explanations mention services closed to new customers (verified 2026-09-30 against the AWS "service availability
change" pages): CloudTrail Lake (2026-05-31), Audit Manager (2026-04-30), Incident Manager / Migration Hub /
Application Discovery Service / Snowball Edge (2025-11-07), Glacier vaults (2025-12-15), CodeGuru Security
(ended 2025-11-20), S3 Select (2024-07), Timestream for LiveAnalytics (2025-06-20), QLDB (ended 2025-07-31).
Also moved to maintenance on 2026-04-30 (closed to new customers): App Runner, ARC readiness check, Glue Ray jobs,
IoT FleetWise, Comprehend topic modeling / event detection / prompt safety, Rekognition streaming events and batch
image content moderation, SNS Message Data Protection. Sunset: RDS Custom for Oracle, WorkMail, WorkSpaces Thin
Client, AWS Service Management Connector (mention removed from Q001823). App Runner and ARC readiness check already
carry an availability note in their explanations. Re-check every few months; the original Security Hub is now
"Security Hub CSPM" (don't state a rename date).

Found 2026-10-22 (study-guide review): Amazon Q Business closed to new customers 2026-07-31 (successor Amazon Quick)
and Amazon Kendra 2026-07-30 (successor Bedrock Knowledge Bases); QuickSight now offered as Quick Sight inside
Amazon Quick; AppStream 2.0 renamed WorkSpaces Applications (2025-11-06). Study guides and the AIB/AIF/AIP
question-bank items are annotated (explain batches AIF-C01/e14, AIP-C01/e16).

Re-check 2026-10-22 (AWS "Service Availability Updates" of 2026-06-30 and 2026-09-29, service docs):
- Amazon Bedrock Agents (launched 2023-11) renamed **Amazon Bedrock Agents Classic**, closed to new customers
  2026-07-30 (maintenance: existing customers keep using it). New agent work goes to **Amazon Bedrock AgentCore**.
  Exam guides may still say "Bedrock Agents"; where it is the keyed answer it stays the intended answer.
- Amazon Cognito Sync and AWS Directory Service Simple AD: closed to new customers 2026-07-30 (successors: AppSync
  with DynamoDB; AWS Managed Microsoft AD). AWS IoT Device Defender Detect: closed to new customers 2026-08-31.
- Amazon Mechanical Turk: end of support 2026-09-29 (closed); SageMaker Ground Truth and Augmented AI (A2I) still
  run with private or vendor workforces, but the Mechanical Turk (public) workforce option is gone.
  SageMaker Ground Truth Plus: end of support 2026-06-30.
- Amazon DevOps Guru: closed to new customers 2026-10-29, end of support 2027-09-30 (use CloudWatch anomaly
  detection / alarms; AWS also points to Amazon DevOps Agent for investigations).
- Amazon Pinpoint: closed to new customers 2025-05-20, end of support 2026-10-30 (engagement features to Amazon
  Connect, email to SES; SMS/voice/push APIs continue as AWS End User Messaging).
- Also closed 2026-10-29: WorkSpaces Secure Browser, Chime SDK SIP media application, standalone Infrastructure
  Composer console (end of support 2026-12-07; the VS Code Toolkit experience stays). Not mentioned in the bank.
Found 2026-10-29 (C03 study-guide review, docs.aws.amazon.com) — DONE the same day:
- AWS X-Ray SDKs and daemon in maintenance mode since 2026-02-25 (security fixes only; AWS recommends OpenTelemetry/ADOT).
  Note added to the 8 questions that mention the SDK (explain batches SAA-C03/e14, AIP-C01/e19, SOA-C03/e14,
  DVA-C02/e14, SAP-C02/e17) and to DVA-C02 study days 22 and 25.
- AWS Copilot CLI end of support 2026-06-12: no question mentions it; the DVA-C03 study guide (day 20) notes it.
- AWS Migration Evaluator is still live (AWS Transform assessments import its Quick Insights files) but its docs URLs
  are gone and SAP-C03 does not list it in scope; AWS Transform assessments build the TCO business case. The 3
  questions keyed to it (Q001176, Q001177, Q003045) stay in SAP-C02 with a note (SAP-C02/e17) and were excluded from
  SAP-C03 (shares.json + `qgen share SAP-C03`, which now also removes newly excluded ids). SAP-C02 study day 28 notes it.
Annotated in explain batches AIB-C01/e17, AIF-C01/e15, AIP-C01/e17-e18, MLA-C01/e14, SOA-C03/e13, DEA-C01/e14,
SAP-C02/e16. Next re-check: around 2027-01 (after the Q4 availability update).

## 2. Reveal frame cost (no action needed)
Profiling (4x CPU) shows the ~100 ms frame is one ~45-70 ms Layout on any reveal, independent of list size; it is the
explanation text layout itself (`.explain{contain:layout style}` already cut it ~25 %). Re-measured 2026-10-28 with an
in-page click (Playwright's `pg.click()` adds its own scrolling/hit-testing to the measured frames, ~30 ms of noise):
plain reveals 17-67 ms, diagram reveals 50-150 ms (big SVG + icons + getBBox label measurement; varies with machine
load). Diagram styles are now injected during the idle warm-up and the diagram renders one frame after the text
(small gain); `content-visibility` on cards and splitting edge drawing into another frame did not help.
`loading_perf_test.py` now clicks in-page, allows 100 ms for plain and 200 ms for diagram reveals, re-measures once on
fresh cards after a failed round (one-off VM spikes), and checks the warm-up directly (sprite + styles present).

## 3. First-load latency (measured 2026-10-29)
Playwright, 390x844, 4x CPU, gzip like GitHub Pages; "first card" = navigation to first question card.
Before: 4G (9 Mbps/85 ms) 1.1-1.5 s, slow 3G (1.6 Mbps/150 ms) 2.8-2.9 s. Causes: the Google Fonts stylesheet was
render-blocking (the page script and every data fetch waited ~0.8 s on 3G), and the exam file and the domain/task files
(exam-specs/-domains/-tasks/-shared-tasks) were fetched one after the other. Fixed (fonts non-blocking with preconnect,
display=swap fallback; exam file + meta in parallel): 4G 0.9-1.2 s, 3G 2.35 s (SAP-C03, 509 questions, 2.9 s: 132 KB gzip
exam file). Remaining cost grows with pool size: the exam file (~0.26 KB gzip per question) and all cards render at once
(~130 ms long task at 4x CPU for 500 cards; `content-visibility:auto` keeps layout cheap). Revealing an answer before the
idle prefetch of `data/explanations/<EXAM>.json` (up to 331 KB gzip) finishes waits 1.5-2.2 s on slow 3G. Ideas if pools
pass ~700: render the first ~50 cards then the rest on idle, or split explanation files per domain.

## Tooling notes
- Tech-debt pass (2026-10-30): tests matched only AWS exam file names (`[A-Z]{3}-C\d{2}`), so 7 Palantir/Azure exams
  were never loaded by mock_e2e/loading_perf/diagram tests; now any exam code. New drift checks: index.html EXAMS and
  EXAM_LEVEL must match exam-specs.json (vendor_tabs_test), js/study.js STUDY_EXAMS must list every guide (study_test).
  Removed the stale, unused `data/_manifest.json` (broke the `_` rule) and 1.8 MB of one-off tool output
  (tools/hardened, tools/explanations, tools/distractor_rewrites, factual_fixes.json, rebalance_answers.py; in git
  history). fetch() in mock.js/study.js now checks r.ok. `.handoff/` is in .gitignore.
- Subagent token savings (2026-10-30, owner request): `tools/learn_fetch.py` shared docs cache (main article text only,
  `--grep` for the relevant lines); batches carry `# src:` lines for reviewers; `qgen check --siblings` catches
  overlaps between parallel batches before review; `expand-exam` writes `PLAN.md` (topics owned per batch) first, uses
  25-30-question batches, Sonnet for format-only work, and ingests each batch as soon as it is reviewed; question
  writers no longer use worktree isolation (they wrote into stale worktrees and could not see new registrations);
  agent reports are capped (writers 150 words, reviewers 200). Foundry status facts moved to `tools/qgen/AZURE-status.md`.
- `tools/diagrams/build_assets.py` reuses icons already in `assets/aws-icons.svg` when the icon pack is missing, so
  it works on any PC; only brand-new icons need the pack (path as first argument).
- Windows cp949: file I/O in tools now passes `encoding="utf-8"`; `qgen.py` and `diagrams/check.py` reconfigure stdout.
  If a new script prints or reads non-ASCII, do the same.
