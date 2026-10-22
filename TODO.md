# TODO

## Support page (started 2026-10-22)
- `support.html` live with KakaoPay (domestic). Ko-fi (international, PayPal payout) url still empty: owner will send it.
- Toss ID (toss.me) closed 2024-08-01; KakaoBank has no receive link; Naver Pay receive link unconfirmed (owner to check the app).

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
- CLF-C02 (Cloud Practitioner) 14-day guide — DONE (main, PR #2), independently fact-checked. Domains live inside
  `data/study/CLF-C02.json`, NOT in exam-specs.json (qbank/mock tests iterate specs; no CLF questions).
- Palantir study guides PLTR-DE/AIE/APD (17 days: 2 per domain + final) — DONE 2026-10-22, built only from the
  reviewed PLTR bank + PALANTIR.md facts, independently reviewed. Study page and question bank both use
  vendor tabs → level segments → named exam chips; question bank section filters sit in a shaded panel.
- 2026-10-22 polish (PR #5, #6): level segment always shown (Palantir shows "Associate"; Specialist is hands-on,
  out of scope); study-guide link text vendor-neutral; README rewritten user-facing in EN (README.md) + KO
  (README.ko.md) with a Ctrl/Cmd-click tip (GitHub strips target=_blank, so links can't force a new tab).
- Open: only P5 backend. Everything else in this section is done.
- Kendra/Q Business availability notes on 19 AIB/AIF/AIP questions — DONE (explain batches AIF-C01/e14, AIP-C01/e16).
- P4 cutover — DONE 2026-10-22: old 9am progress routine deleted; new routine "학습 가이드 리마인드" weekdays 06:50 KST
  (13 exam links incl. CLF-C02; Gmail connector attached by owner); 26 old artifacts deleted.
- Rulesets for main: set up by owner 2026-10-22 (PR required). Work on a branch, open a PR, merge via API.
- P5 backend (Cognito OTP, API GW/Lambda/DynamoDB, Scheduler, SES) — design only, later. Needs own domain +
  personal AWS account.
Known test noise (also on main before this work): `bookmark_backup_test` "toast shown" 17/18,
`diagrams/check.py` exit 1. Playwright here: `pip install playwright==1.56.0` (matches /opt/pw-browsers chromium-1194).

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
Amazon Quick; AppStream 2.0 renamed WorkSpaces Applications (2025-11-06). Study guides are annotated; question-bank
items in AIB/AIF/AIP that mention Kendra or Q Business still need availability notes via explain batches.

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
