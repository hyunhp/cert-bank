# Microsoft Azure question rules (AZ-*)

Read this before writing, reviewing or fixing any `AZ-*` batch. It records what the official pages say
(checked 2026-10-29) and the rules this bank adds on top. Every fact must be checkable on
learn.microsoft.com (the only Microsoft host allowed in this environment).

## Official facts the site mirrors
Sources: study guide https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900
("Skills measured as of July 20, 2026", page updated 2026-06-22) and the certification page
https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/.

| Item | Value |
|---|---|
| Exam | AZ-900 Microsoft Azure Fundamentals |
| Length | 45 minutes ("You will have 45 minutes to complete this assessment") |
| Questions | Not published. This bank assumes 45 (`questions` in `exam-specs.json`), used only for mock length |
| Pass mark | Scaled score 700 or greater (`passingScore`) |
| Domains | D1 Describe cloud concepts 25-30%, D2 Describe Azure architecture and services 35-40%, D3 Describe Azure management and governance 30-35%. Ranges are published; `exam-specs.json` stores the midpoints (27.5 / 37.5 / 32.5) |
| Question types | The real exam also uses yes/no series, drag-and-drop and hotspot items. This bank only has single- and multi-answer multiple choice; turn those skills into normal scenario questions |
| Preview features | "Most questions cover features that are general availability (GA)": key answers must be GA features |

### AZ-104 Microsoft Azure Administrator (added 2026-10-29)
Sources: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104 ("Skills measured as
of April 17, 2026", page updated 2026-03-19) and https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/.

| Item | Value |
|---|---|
| Length | 100 minutes ("You will have 100 minutes to complete this assessment") |
| Questions | Not published. This bank assumes 50 (mock length only) |
| Pass mark | Scaled score 700 or greater |
| Domains | D1 identities and governance 20-25%, D2 storage 15-20%, D3 compute 20-25%, D4 virtual networking 15-20%, D5 monitor and maintain 10-15%; `exam-specs.json` stores the midpoints |
| Item types | The real exam may include interactive components (labs, case studies); this bank only has multiple choice |

## Codes and task ids
- `AZ-900` (Azure Fundamentals), vendor `azure`, level `foundational`.
- `AZ-104` (Azure Administrator – Associate), vendor `azure`, level `associate`; tasks T1.1-T5.2 are the guide's 15 skill
  groups in order.
- Domains D1-D3 follow the study guide's order and names exactly.
- The guide's skill groups ("Describe cloud computing", ...) are this bank's tasks T1.1-T3.4, in guide order,
  recorded in `tools/qgen/tasks.json` (Korean) and `data/exam-tasks.json` (English, the guide's wording).

## Writing rules
- Use current product names: **Microsoft Entra ID** (never Azure AD / Azure Active Directory, except to say
  "formerly Azure AD" once in a background section), Microsoft Entra Domain Services, Microsoft Defender for Cloud
  (not Azure Security Center), Microsoft Purview, Microsoft Cost Management, Azure Monitor (Log Analytics,
  alerts, Application Insights).
- Retired or retiring, never a key answer: Basic SKU public IPs and Basic Load Balancer (retired 2025-09-30);
  Azure Blueprints (preview, retiring 2027-01-31, phased from 2026-07-31; successor Deployment Stacks and
  Template Specs). Do not test preview-only features.
- No prices, SLA percentages or quotas unless the reviewed Learn page states them and they are stable; prefer
  describing the effect ("pay only while the VM runs") over numbers.
- Region pairs: Microsoft's own page warns that deploying into a pair does not by itself give high availability or
  failover; never imply automatic failover from pairing alone. Many newer regions are nonpaired and use
  availability zones.
- AZ-900 is a fundamentals exam: stems test choosing and describing services, not CLI flags or portal clicks.
- AZ-104 is an administrator exam: stems are hands-on scenarios (configure, troubleshoot, interpret). Concrete settings,
  role names, `az`/PowerShell commands, ARM/Bicep snippets and portal blades are fine when each detail is checked on
  Learn; keep snippets short (a few lines in backticks) and never test memorised syntax trivia that Learn does not show.
  Keep scenarios short and concrete (a small company, a specific need) and distractors real Azure services.
- Write in the detailed style of CLAUDE.md (G/W/X/T), and cite the Learn page you checked in your report (not in
  the question text).
