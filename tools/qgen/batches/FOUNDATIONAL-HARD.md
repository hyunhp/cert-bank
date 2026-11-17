# Hard layers for foundational exams (CLF-C02, AIF-C01, AZ-900), 2026-11-17

Same goal as DEA-C01/SAA-C03 (`batches/DEA-C01/PLAN.md`), scaled to a foundational exam: the hardest *fair*
questions a foundational candidate can meet. No configuration-detail trivia the exam guide does not cover.
Tier gate (qgen `tier_of`): exam = stem >= 55 words AND average option >= 13 words (or Select THREE).

## exam-level batch (40, level `advanced`)
- Stem 55-85 words: a business situation (team, budget, compliance, skills) with 2 constraints; the question line
  names the deciding criterion (LEAST effort, MOST cost-effective, shared responsibility owner, ...).
- Options 13-25 words, each a real service/approach described by what it does; wrong ones are real and plausible,
  failing one stated constraint. Correct option never the longest. ~20% multi-answer, >= 2 Select THREE.
- Spread over all domains by official weight.
## expert batch (20, level `expert`)
- Stem 80-120 words with 3 constraints, one only in the details; closely related services side by side (e.g.
  Savings Plans vs Reserved Instances vs Spot; Shield Standard vs Advanced; Bedrock Guardrails vs Knowledge Bases vs
  fine-tuning; Azure Policy vs RBAC vs Blueprints successors; SLA composite math), worked numbers where the guide
  covers them (composite SLA, pricing model choice, support plan response times). ~30% multi-answer.
- Reviewer blind-solves every question.
Vendor rules still apply: AZ-900 -> `tools/qgen/AZURE.md` (learn.microsoft.com only).
