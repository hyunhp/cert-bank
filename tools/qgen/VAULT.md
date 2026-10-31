# HashiCorp Vault exams — facts and writing rules

Read this before any `VLT-*` work (also `tools/qgen/TERRAFORM.md`: same vendor tab and question types). Facts come from the exam pages and
developer.hashicorp.com only (`python3 tools/learn_fetch.py "<url>"` on /vault/docs, /vault/api-docs, /vault/tutorials; read cached pages directly or use a
single-regex --grep). Vendor `hashicorp` (tab "HashiCorp"); exam code `VLT-` plus the exam initials and version.

## VLT-VA003 HashiCorp Certified: Vault Associate (003) (added 2026-10-31)
Sources: https://developer.hashicorp.com/certifications/vault-associate, the content list
https://developer.hashicorp.com/vault/tutorials/associate-cert-003/associate-review-003 and the sample questions page `.../associate-questions-003` (read 2026-10-31).

| Item | Value |
|---|---|
| Format | 1 hour, online proctored; English; USD 70.50; valid 2 years; Vault 1.19 tested |
| Question types | true or false, multiple choice, multiple answer (same as the Terraform Associate) |
| Questions / pass mark / weights | Not published. `questions: 50` is a mock assumption; `passMarkUnpublished` and `weightsAssumed` (equal weights) |
| Objectives | 9 sections, 40 sub-objectives = tasks T1.1-T9.2 in `data/exam-tasks.json` (1 auth methods 6, 2 policies 5, 3 tokens 6, 4 leases 3, 5 secrets engines 8, 6 encryption as a service 2, 7 architecture fundamentals 3, 8 deployment architecture 5, 9 access management architecture 2) |
| Audience | Cloud engineer (security, development or operations) with foundational Vault knowledge |

Writing rules:
- Block header: `@ VLT-VA003 D3 T3.1 applied use-case` (level word, then a type such as use-case, definition, troubleshooting, tradeoff, comparison).
- True/false items become "Which statement is accurate?" questions (single answer). About 15-20% "(Select TWO)" multi-answer.
- Stems carry only short inline snippets (qgen joins stem lines): one CLI command, one policy path stanza, one API path; multi-line policy HCL goes in G:.
  Snippets must be valid for Vault 1.19. Test the practitioner's decision or prediction (which policy, which token type, what happens on revoke), not trivia.
- Names: HCP Vault (HashiCorp-managed), Vault Enterprise, Vault Community, Vault Agent, Vault Secrets Operator. No prices, plan/tier names, limits or quotas as keys.
- Nothing beta, experimental or deprecated in keys (check the docs page banner); Enterprise-only features may appear only when the question says so.
- Hot spots: token TTL/renewal (b03) vs lease renewal/revocation (b04); transit as a secrets engine choice (b05) vs encrypt/decrypt/rotate/rewrap mechanics (b06);
  seal/unseal concept and environment variables (b07) vs Shamir, auto-unseal, storage backends, replication and cluster strategy (b08); auth method choice (b01)
  vs Vault Agent auto-auth and Secrets Operator (b09).
