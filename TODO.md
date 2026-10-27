# TODO

## AWS exam versions (checked 2026-10-27)
Notices live in `data/exam-specs.json` ("update"), shown above the section filters and in mock setup.
- SAP-C02 -> SAP-C03: DONE 2026-10-27 from the official guide (docs.aws.amazon.com, 2026-10-27): 5 domains
  25/25/15/15/20, 18 tasks, 65 scored + 10 unscored, passing 720 (time not in the guide; 180 min assumed).
  All 396 SAP-C02 questions classified against the C03 skills: 388 shared with their new task (shares.json "tasks"
  rule, data/exam-shared-tasks.json), 8 excluded (Service Catalog, Migration Hub, Snowball Edge, VMware Cloud on
  AWS, Well-Architected Tool). 13 updated in SAP-C02/f02 (AWS Transform MGN, Security Hub CSPM, re-keyed discovery
  and AWS Batch questions). 120 new in batches/SAP-C03/b01-b06 (AI/ML integration, responsible AI and post-quantum,
  AI cost/evaluation/monitoring, and every skill that had no question), each reviewed and deduplicated across
  batches. Pool 508. Open: SAP-C03 study guide; after 2026-11-16 decide whether to hide SAP-C02.
  Bedrock Guardrails org-level enforcement (AWS Organizations Bedrock policy) is GA since 2026-04: no question
  covers it yet, and no existing key is contradicted by it.
- DVA-C02 -> DVA-C03: NEXT. Last C02 day 2026-11-30, C03 from 2026-12-01. Official guide published 2026-10-27
  (developer-associate-03): same 4 domains, weights 30/26/22/22, 50 scored + 15 unscored, passing 720; new Task 2.3
  (AI service security) and Task 3.2 (automated testing). Same method as SAP-C03 (classify, share with tasks, write
  the gap).
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
Annotated in explain batches AIB-C01/e17, AIF-C01/e15, AIP-C01/e17-e18, MLA-C01/e14, SOA-C03/e13, DEA-C01/e14,
SAP-C02/e16. Next re-check: around 2027-01 (after the Q4 availability update).

## 2. Reveal frame cost (no action needed)
Profiling (4x CPU) shows the ~100 ms frame is one ~45-70 ms Layout on any reveal, independent of list size and of
diagrams (`injectStyles` is not the cause); it is the explanation text layout itself. `.explain{contain:layout style}`
already cut it ~25 %. `loading_perf_test.py` "no long frames on reveal" (100 ms limit) can still flake when the
company network needs re-authentication.

## Tooling notes
- `tools/diagrams/build_assets.py` reuses icons already in `assets/aws-icons.svg` when the icon pack is missing, so
  it works on any PC; only brand-new icons need the pack (path as first argument).
- Windows cp949: file I/O in tools now passes `encoding="utf-8"`; `qgen.py` and `diagrams/check.py` reconfigure stdout.
  If a new script prints or reads non-ASCII, do the same.
