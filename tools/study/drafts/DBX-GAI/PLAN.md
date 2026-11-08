# DBX-GAI study guide plan (19 days)
Rules: `tools/study/README.md` (data shape) and `tools/qgen/DATABRICKS.md` (DBX-GAI + DBX-MLA + DBX-DEA sections). Sources: tasks in `data/exam-tasks.json` ("DBX-GAI"), docs.databricks.com only (`python3 tools/learn_fetch.py --grep "<terms>" <url>`, shared cache; mlflow.org is blocked). Built from the reviewed bank (`data/DBX-GAI.json`, `data/explanations/DBX-GAI.json`) plus the docs; keep claims the bank already verified, re-check anything new yourself (earlier writers still had ~15 unchecked claims each).
GenAI-engineer associate level. `data/study/DBX-MLA.json` and `DBX-MLP.json` cover classic ML serving/MLflow: do not repeat them.
Settled facts (from the reviewed bank): Vector Search is now Databricks AI Search (python package `databricks.ai_search`, older snippets `databricks.vector_search`; name old once); AI Gateway is now Unity Gateway (docs still say 'AI Gateway inference tables' in places); Genie spaces are Genie Agents; Knowledge Assistant and Supervisor Agent are Legacy, Information Extraction is Legacy + Beta (teach current products: Agent Runtime/AgentKit, Genie Agents, Agent Bricks CLI, `ai_parse_document` + `ai_extract`); Beta (never taught as an answer): MLflow Prompt Registry, production monitoring of agents, AI Search full-text search and query payload logging, `ai_prep_search`/`ai_search`/`ai_enrich`/`ai_transcribe`/`ai_decide`, review queues and external-model budgets, the system.ai dbsql/sandbox/web_search MCP servers; Public Preview: AI Guardrails for serving endpoints, on-behalf-of-user auth on Model Serving, the Genie multi-agent page, Qwen3 embedding, custom Vega-style items; only the Genie One MCP server is GA; request logs and assessment logs are deprecated; managed agent memory is Legacy; Agent Framework pages now recommend the Agent Bricks CLI and Databricks Apps for new agents while Model Serving deploy is still documented. Parent-child, sentence-window and contextual-prefix chunking, LangChain LCEL, precision/recall/MRR/NDCG, and most legal/safety principles are generic: say so. No numeric limits beyond what a stem states.
Shape per day: see `data/study/DBX-MLA.json` (day, domain, title, services, concepts[{heading,body}], examPoints, quiz[2], recap).
3-4 concepts of 120-190 words, 3 examPoints, quiz = 2 questions with 4 choices, `answer` is a 0-3 integer index (spread the indexes), correct choice never the longest (ties count), no letter references in explanations. `domain` is the string "D1".."D6" (`null` on the final day). Recompute every numeric example.

| Day | Domain | Tasks | Topic |
|---|---|---|---|
| 1 | D1 | T1.1-T1.3 | prompts that elicit a format, model tasks for business needs, chain components |
| 2 | D1 | T1.4-T1.6 | business goals to inputs/outputs, tools for multi-stage reasoning, current agent building blocks (Agent Runtime/AgentKit, Genie Agents, Agent Bricks CLI, AI functions) |
| 3 | D2 | T2.1-T2.3 | chunking by structure and model limits, filtering noise, parsing packages |
| 4 | D2 | T2.4-T2.6 | writing chunks to Delta in Unity Catalog, choosing source documents, retrieval metrics |
| 5 | D2 | T2.7, T2.8 | advanced chunking designs, re-ranking |
| 6 | D3 | T3.1-T3.3 | LangChain-style tooling, qualitative assessment, chunking by evaluation |
| 7 | D3 | T3.4-T3.6 | prompt augmentation, adjusting a baseline response, guardrails |
| 8 | D3 | T3.7-T3.10 | LLM selection, embedding context length, model hub and model cards, metrics from experiments |
| 9 | D3 | T3.11-T3.13 | MLflow and Agent Framework, evaluation vs monitoring phases, Genie conversational API |
| 10 | D4 | T4.1-T4.3 | pyfunc chains with pre/post-processing, access from serving endpoints, simple chains |
| 11 | D4 | T4.4-T4.6 | RAG elements (flavor, signature, input example), registering in Unity Catalog, creating and querying AI Search |
| 12 | D4 | T4.7-T4.9 | Foundation Model APIs, ai_query batch inference, AI Search configuration by size/latency/cost |
| 13 | D4 | T4.10-T4.12 | persistent datastore for memory, CI/CD for index and agent components |
| 14 | D4 | T4.13-T4.15 | MCP integration, prompt versioning and lifecycle (Registry is Beta: teach generic practice), user-facing interfaces |
| 15 | D5 | T5.1-T5.4 | masking, guardrails against malicious input, licensing, problematic text |
| 16 | D6 | T6.1-T6.3 | LLM choice by metrics, metrics to monitor, MLflow scoring and tracing |
| 17 | D6 | T6.4-T6.6 | inference logging for RAG, cost control, inference tables and agent monitoring |
| 18 | D6 | T6.7-T6.10 | judges needing ground truth, Unity Gateway usage and rate limits, custom scorers, SME feedback |
| 19 | null | all | final review: decision cheat-sheet across the 6 domains, weights from `data/exam-specs.json`, 2 quiz questions |

Writers: w1 days 1-5, w2 days 6-9, w3 days 10-14, w4 days 15-19. Each writes ONLY `tools/study/drafts/DBX-GAI/wN.json` (a JSON list of day objects).
