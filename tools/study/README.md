# Study guide (`study.html`)

Day-by-day study plans for the 12 AWS exams, imported in 2026-10 from the old study-tracker pages
(`extract.py`, one-off). `data/study/<EXAM>.json` is now the source of truth; edit it directly
(no qgen batches: these are teaching notes, not question-bank items).

## Data
`{"exam", "days": [{day, domain, title, services, concepts:[{heading, body}], examPoints, quiz:[{q, choices,
answer, explain}], recap}]}`
- `domain` is the exam's `D1..Dn` code from `exam-specs.json`; the final review day has `null`.
- Quiz choices are shown in file order with letters A-D, and some explanations refer to choices by
  letter, so never reorder choices.
- After editing run `python3 tools/build_data_index.py` (the page fetches `data/study/<EXAM>.json?v=<hash>`)
  and `python3 tools/study_test.py`.
- 2026-10-22 availability review: retired services (CodeGuru Reviewer/Security, Incident Manager,
  Audit Manager, CloudTrail Lake, Application Discovery Service, Migration Hub, Snowball Edge,
  OpsWorks, Timestream for LiveAnalytics) were replaced or annotated. Re-check together with the
  question bank (TODO.md section 1).

## Page
- `#exam=SAA-C03&day=3`; prev/next and a day list grouped by domain; "Practice Dn questions" opens
  the question bank filtered to the day's domain.
- Progress (studied days, last day opened) is in localStorage `aws_qbank_study_v1`, read and written
  only through `StudyStore` in `js/study.js`.
- Body text goes through `text()` in `js/study.js`; the glossary tooltips (planned) hook in there.

## Planned backend (not built; design only, 2026-10-22)
Goal: let other people get a daily study reminder and keep progress across devices, while
collecting as little personal data as possible. Nothing is stored that can be computed: today's
day is `(today - startDate) + 1`, and titles/recaps come from `data/study/`.

```
study.html (GitHub Pages, static)
  guest: progress in localStorage (same shape as below)
  sign-in: Cognito user pool, passwordless email OTP (also proves the address is theirs)
    -> API Gateway (HTTP API) -> Lambda -> DynamoDB (ap-northeast-2)
       PK USER#<sub> | PROFILE       {email, tz, createdAt}
                     | SUB#<EXAM>    {startDate, weekdays, sendHour}
                     | PROG#<EXAM>   {done, lastDay, updatedAt}   <- what StudyStore holds today
EventBridge Scheduler (hourly) -> Lambda: subscriptions whose local sendHour is now
  -> compute day -> SES mail: day link + recap + one-click unsubscribe (List-Unsubscribe)
```
- Reading stays sign-in free; only reminders and cross-device sync need an account.
- Sync: server `updatedAt` vs local; merge `done` as a set union, newest `lastDay` wins.
- Needs before launch: an own domain (SES DKIM; github.io cannot), SES production access,
  a privacy notice, account deletion endpoint, deleting inactive accounts after a set period,
  and a personal (not company) AWS account.
