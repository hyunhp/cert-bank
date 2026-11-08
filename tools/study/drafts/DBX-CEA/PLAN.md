# DBX-CEA study guide plan (16 days)
Rules: `tools/study/README.md` (data shape) and `tools/qgen/DATABRICKS.md` (DBX-CEA + DBX-GAI sections). Sources: tasks in `data/exam-tasks.json` ("DBX-CEA"), the exam guide text at `/tmp/claude-0/g/ctx.txt`, docs.databricks.com only (`python3 tools/learn_fetch.py --grep "<terms>" <url>`, shared cache; mlflow.org is blocked). Built from the reviewed bank (`data/DBX-CEA.json`, `data/explanations/DBX-CEA.json`) plus the docs; keep claims the bank already verified, re-check anything new yourself.
Context-engineering level. `data/study/DBX-GAI.json` (GenAI engineer guide) teaches RAG, prompts, MCP and evaluation basics: build on it, do not repeat it; teach the context-management decisions (what to load, when, in what form).
Settled facts (from the reviewed bank): the docs do NOT define context poisoning/distraction/confusion/clash, compaction, progressive disclosure of tools, tool-result clearing, just-in-time retrieval, over-/under-retrieval, intent resolution, sub-agent dispatch/context propagation, or long-horizon strategies: label each as the exam guide's term or generally accepted context-engineering practice, never as a Databricks feature. Documented Databricks facts: Genie One MCP (`system.ai.genie_one_mcp`) is GA, Genie Agent MCP calls bypass Unity Gateway; the system.ai dbsql/sandbox/web_search MCP servers are Beta; Genie Ontology and the Genie multi-agent page are Public Preview (never an answer); agent sessions and memory are Lakebase-backed (stateful-agents page; memory is scoped to a subject; episodic/derived memory mapping; store permissions; managed agent memory is Legacy); Databricks AI Search (formerly Vector Search) full-text search and query payload logging are Beta, tag assignment automation is Beta, ABAC is Beta; `system.certification_status` is a GA label that does not block reads; Genie Code skills (SKILL.md, loaded only when relevant) are documented at genie-code/skills; MLflow Tracing records latency, token usage and cost per step; reasoning-model `budget_tokens` must be below `max_tokens` and newer Claude models reject `budget_tokens` (adaptive/effort instead); on-behalf-of-user auth is Public Preview. Genie guidance: text instructions are a last resort, curated example queries/trusted assets, column descriptions and filter SQL expressions beat entity matching for coded values. No numeric limits.
Shape per day: see `data/study/DBX-MLA.json` (day, domain, title, services, concepts[{heading,body}], examPoints, quiz[2], recap).
3-4 concepts of 120-190 words, 3 examPoints, quiz = 2 questions with 4 choices, `answer` is a 0-3 integer index (spread the indexes), correct choice never the longest (ties count), no letter references in explanations. `domain` is the string "D1".."D7" (`null` on the final day).

| Day | Domain | Tasks | Topic |
|---|---|---|---|
| 1 | D1 | T1.1-T1.4 | matching an agent failure to a context technique, proactive strategies, failure modes, choosing the product (UC, Lakebase, MCP, MLflow 3) |
| 2 | D1 | T1.5-T1.7 | attention budget, reasoning modes and token budget, context degradation over long interactions |
| 3 | D2 | T2.1-T2.4 | Genie instructions/sample questions/trusted assets, few-shot under a token budget, targeted prompt revision, cost-performance via experiment tracking |
| 4 | D3 | T3.1-T3.3 | UC metadata gaps, curating objects into Genie, diagnosing AI Search configuration |
| 5 | D3 | T3.4-T3.6 | RAG over a governed corpus, chunking, scoping context elements |
| 6 | D3 | T3.7-T3.9 | pre-inference vs just-in-time retrieval, retrieval failure modes via eval logs, constraining retrieval to authoritative assets |
| 7 | D4 | T4.1-T4.3 | memory source mismatch, Delta-backed state vs scratchpad, AI Search vs structured retrieval over memories |
| 8 | D4 | T4.4-T4.6 | comparing runs in MLflow 3, static vs dynamic retrieval, over-/under-retrieval |
| 9 | D4 | T4.7, T4.8 | persistent memory across sessions on Lakebase, resolving intent before retrieval |
| 10 | D5 | T5.1-T5.3 | progressive disclosure of MCP tools, ambiguous tool descriptions, controlling tool information in context |
| 11 | D5 | T5.4-T5.6 | deep message history and tool results, UC functions as tools, Genie Code skills |
| 12 | D6 | T6.1-T6.3 | spotting when compaction is needed, compaction and summarization techniques |
| 13 | D6 | T6.4, T6.5 | what to keep and drop, trimming trade-offs |
| 14 | D7 | T7.1-T7.3 | when to split work across agents, dispatch and context handoff |
| 15 | D7 | T7.4-T7.6 | sub-agent output schemas, shared context, long-horizon strategies |
| 16 | null | all | final review: decision cheat-sheet across the 7 domains, weights from `data/exam-specs.json`, 2 quiz questions |

(Check `data/exam-tasks.json` and `/tmp/claude-0/g/ctx.txt` for the exact wording of each task: if a task id here does not match the topic text, follow the task text and tell the coordinator.)
Writers: w1 days 1-5, w2 days 6-9, w3 days 10-13, w4 days 14-16. Each writes ONLY `tools/study/drafts/DBX-CEA/wN.json` (a JSON list of day objects).
