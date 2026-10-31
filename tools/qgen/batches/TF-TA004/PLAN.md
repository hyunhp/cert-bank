# TF-TA004 batch plan (one batch per exam section, topics owned per batch)
Exam: Terraform Associate (004), content list read 2026-10-31. Target 250 (31 per section). Rules and facts: `tools/qgen/TERRAFORM.md`. About 15-20% "(Select TWO)".
HCL/CLI snippets in stems welcome and must be valid for Terraform 1.12. Before writing, read the published questions of the exam (`data/TF-TA004.json`) and use
new scenarios. Hot spots belong to ONE batch only; others may use them as distractors.

| Batch | Tasks | Count | Owns | Leave to |
|---|---|---|---|---|
| b01 | D1 T1.1-T1.3 | 31 | what IaC is, declarative vs imperative, advantages (repeatability, versioning, review, drift reduction), multi-cloud, hybrid and service-agnostic workflows, provider-based extensibility | everything product-specific below |
| b02 | D2 T2.1-T2.4 | 31 | required_providers and version constraints (~>, >=), dependency lock file, provider aliases and multiple providers, how providers work (plugins, registry), why Terraform keeps state and what it holds | init behavior (b03), backends/locking/drift (b06) |
| b03 | D3 T3.1-T3.7 | 31 | write/plan/apply workflow, init (-upgrade, -reconfigure, -migrate-state), validate, plan (-out, -target, -refresh-only, -destroy), apply (auto-approve, saved plans), destroy, fmt (-check, -recursive) | provider constraints (b02), state subcommands (b07) |
| b04 | D4 T4.1-T4.5 | 31 | resource vs data blocks, attribute references, count/for_each, variables (types, defaults, validation, precedence of tfvars/-var/env), outputs, complex types (list/set/map/object/tuple), expressions, functions, conditionals, for expressions, splat, dynamic blocks | T4.6-T4.8 (b05 is modules; D4 T4.6-T4.8 questions go in b04 too if room, see below) |
| b05 | D5 T5.1-T5.4 + D4 T4.6-T4.8 | 31 | modules: sources (registry, git, local), version argument, inputs/outputs, variable scope, module composition (D5, 20); depends_on and create_before_destroy lifecycle, preconditions/postconditions/checks, sensitive values, ephemeral values and write-only arguments, Vault integration (D4, 11) | T4.1-T4.5 (b04) |
| b06 | D6 T6.1-T6.4 | 31 | local backend, state locking, remote backend block (S3-style, HCP Terraform cloud block), drift and refresh-only, moved and removed blocks, replace, state security | import/state subcommands (b07) |
| b07 | D7 T7.1-T7.3 | 31 | import block and `terraform import`, generated configuration, state list/show/mv/rm, TF_LOG levels and TF_LOG_PATH, troubleshooting scenarios | backends and drift (b06) |
| b08 | D8 T8.1-T8.4 | 31 | HCP Terraform workspaces and projects, CLI-driven vs VCS-driven vs API-driven workflows, remote operations, variable sets, private registry, run triggers, policy enforcement (Sentinel/OPA), teams, drift detection, `terraform login`, `cloud` block, Terraform Enterprise vs Community distinctions | open-source CLI workflow (b03) |

Waves (about 4 writers at a time): b01, b02, b03, b04; then b05, b06, b07, b08.
