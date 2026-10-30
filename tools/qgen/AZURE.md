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

### AI-901 Microsoft Azure AI Fundamentals (added 2026-10-29)
Sources: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-901 ("Skills measured as
of April 15, 2026", page updated 2026-07-13) and https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/
("The English language version of this certification was updated on April 15, 2026"). AI-901 replaces AI-900 (retired
2026-06-30).

| Item | Value |
|---|---|
| Length | Not on the exam page; Learn's exam-duration page gives Fundamentals exams 45 minutes |
| Questions | Not published. This bank assumes 45 (mock length only) |
| Pass mark | Scaled score 700 or greater |
| Domains | D1 Identify AI concepts and capabilities 40-45%, D2 Implement AI solutions by using Microsoft Foundry 55-60%; `exam-specs.json` stores the midpoints |
| Audience | Beginning AI developers: conceptual AI knowledge plus basic Python and familiarity with Azure resources |
| Preview features | "Most questions cover features that are general availability (GA). The exam may contain questions on Preview features if those features are commonly used." Key answers stay on GA features; when a feature is preview, say so in the explanation |

### AI-103 Developing AI Apps and Agents on Azure (added 2026-10-30)
Sources: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103 ("Skills measured as
of April 16, 2026") and https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/
(Microsoft Certified: Azure AI Apps and Agents Developer Associate). AI-103 replaces AI-102 (retired 2026-06-30).

| Item | Value |
|---|---|
| Length | 120 minutes ("You will have 120 minutes to complete this assessment") |
| Questions | Not published. This bank assumes 50 (mock length only) |
| Pass mark | Scaled score 700 or greater |
| Domains | D1 Plan and manage an Azure AI solution 25-30%, D2 Implement generative AI and agentic solutions 30-35%, D3 computer vision 10-15%, D4 text analysis 10-15%, D5 information extraction 10-15%; `exam-specs.json` stores the midpoints |
| Item types | "You may have interactive components"; this bank only has multiple choice |
| Preview features | Same note as AI-901: mostly GA, commonly used preview features possible. Key answers stay on GA features |

## Codes and task ids
- `AZ-900` (Azure Fundamentals), vendor `azure`, level `foundational`.
- `AI-901` (Azure AI Fundamentals), vendor `azure`, level `foundational`; tasks T1.1-T1.3 and T2.1-T2.4 are the guide's 7
  skill groups in order.
- `AI-103` (Azure AI Apps and Agents Developer – Associate), vendor `azure`, level `associate`; tasks T1.1-T5.2 are
  the guide's 14 skill groups in order.
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
- AI-901 is a fundamentals exam for beginning developers: stems mix concepts (responsible AI, workloads, how generative
  models work) with light hands-on Foundry scenarios (deploy a model, write a prompt, a small Python client, a single agent,
  Content Understanding analyzers). Use current names checked on Learn: Microsoft Foundry (formerly Azure AI Foundry),
  Foundry Tools (formerly Azure AI services), Azure Speech / Azure Language / Azure Content Understanding in Foundry
  Tools, Foundry Agent Service. Keep code to a few lines; never test SDK syntax trivia Learn does not show.
  Checked during the AI-901 reviews (2026-10-29): "Guardrails (previously content filters)"; roles Foundry User (formerly
  Azure AI User), do not use Azure AI Developer or Cognitive Services* roles for Foundry projects; agents use agents +
  conversations + responses (classic threads/messages/runs deprecated, retire 2027-03-31); Azure Language key phrases,
  sentiment/opinion mining and summarization are "legacy" (retire 2029-03-31; PII, language detection, NER are core);
  Language Studio retires 2027-03-20; Image Analysis v3.2/v4.0 and Custom Vision retire 2028-09-25 (never key them);
  dall-e-3 retired 2026-03-04, GPT-image-2 and the GPT-image-2.5 models are GA while GPT-image-1/1-mini/1.5 are limited-access preview; Realtime API
  with gpt-realtime and Voice Live API are GA, gpt-audio chat completions uses a preview API version.
- AI-103 is a developer associate exam: stems are build/configure/troubleshoot scenarios in Microsoft Foundry (models,
  agents, RAG with Azure AI Search, evaluation, tracing, guardrails, Content Understanding, Speech, Language,
  Translator). Short code (Python SDK, REST) and settings are fine when shown on Learn. Apply every AI-901 naming and
  status fact recorded above; check GA vs preview for each keyed feature (Foundry changes fast).
- AZ-900 is a fundamentals exam: stems test choosing and describing services, not CLI flags or portal clicks.
- AZ-104 is an administrator exam: stems are hands-on scenarios (configure, troubleshoot, interpret). Concrete settings,
  role names, `az`/PowerShell commands, ARM/Bicep snippets and portal blades are fine when each detail is checked on
  Learn; keep snippets short (a few lines in backticks) and never test memorised syntax trivia that Learn does not show.
  Keep scenarios short and concrete (a small company, a specific need) and distractors real Azure services.
- Write in the detailed style of CLAUDE.md (G/W/X/T), and cite the Learn page you checked in your report (not in
  the question text).
