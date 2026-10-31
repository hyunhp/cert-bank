# HashiCorp Terraform exams — facts and writing rules

Read this before any `TF-*` work. Facts come from the exam pages and developer.hashicorp.com only
(`python3 tools/learn_fetch.py --grep "<terms>" https://developer.hashicorp.com/terraform/...`: language, cli, cloud-docs (HCP Terraform), registry).
Vendor `hashicorp` (tab "HashiCorp", phone short name "HC"); exam codes have no official form, so this bank uses `TF-` plus the version.

## TF-TA004 HashiCorp Certified: Terraform Associate (004) (added 2026-10-31)
Sources: https://developer.hashicorp.com/certifications/terraform-associate, the exam content list
https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-review-004 and the sample questions page `.../associate-questions-004`
(all read 2026-10-31).

| Item | Value |
|---|---|
| Format | 1 hour, online proctored; English; USD 70.50; valid 2 years; Terraform 1.12 tested; includes HCP Terraform |
| Question types | "true or false, multiple choice, and multiple answer" (multiple answer states how many to pick, e.g. "Pick the 2 correct responses") |
| Questions / pass mark / weights | Not published. `questions: 50` is an assumption for the mock only; `passMarkUnpublished` and `weightsAssumed` (equal weights) |
| Objectives | 8 sections, 37 sub-objectives (1a-1c, 2a-2d, 3a-3g, 4a-4h, 5a-5d, 6a-6d, 7a-7c, 8a-8d) = tasks T1.1-T8.4 in `data/exam-tasks.json` |
| New in 004 | 4f depends_on and create_before_destroy, 4g custom conditions, 4h ephemeral values and write-only arguments, 8c workspaces and projects |
| Audience | Cloud engineer with foundational Terraform knowledge who can tell Terraform Enterprise features from Community edition |

Writing rules:
- Block header: `@ TF-TA004 D3 T3.4 applied use-case` (level word, then a type such as use-case, definition, troubleshooting, tradeoff, comparison).
- True/false items become "Which statement is accurate?" questions (single answer). About 15-20% "(Select TWO)" multi-answer, as the exam has.
- HCL and CLI snippets are expected and must be valid Terraform 1.12 syntax. `qgen` joins stem lines with spaces, so stems carry only short inline snippets
  (one block or one expression); multi-line HCL goes in G:. Test the practitioner's decision or prediction
  ("what does plan show", "which block", "which command"), not trivia.
- Tested version is Terraform 1.12: do not key features the docs mark as added after 1.12; check the version notes on each docs page.
- Names: HCP Terraform (formerly Terraform Cloud), Terraform Enterprise, `terraform` CLI, OpenTofu is out of scope. No prices, plan tiers/editions,
  limits or quotas as keys.
- Nothing beta, experimental or deprecated in keys (check the docs page banner).
- Hot spots: state fundamentals (why state exists, what it holds) belong to D2; backends, locking, drift, moved/removed/refresh-only belong to D6;
  sensitive/ephemeral/write-only/Vault belong to D4; `import` and `terraform state` subcommands and TF_LOG belong to D7; provider requirements and the lock file
  belong to D2, `terraform init` command behavior to D3.
