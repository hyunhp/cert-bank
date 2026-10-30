# GCP-GAIL batch plan (topics owned per batch)

Exam: Google Cloud Generative AI Leader, exam guide read 2026-10-30. 90 minutes, 50-60 multiple choice questions, pass
mark not published. Target 226 (D1 68, D2 79, D3 45, D4 34). Rules: `tools/qgen/GCP.md` (guide's product names, nothing
preview, no model versions, prices, limits or plan names, business-level stems, unreachable hosts listed there).
Fundamentals style: describe and choose; scenarios are business needs (a retailer, a bank, a support team), never
commands or console steps. Multi-answer about 15-20%.
Shared hot spots belong to ONE batch only; others may use them as distractors but not as the tested concept.

| Batch | Tasks | Count | Owns | Leave to |
|---|---|---|---|---|
| b01 | T1.1 | 28 | core concepts (AI vs ML vs gen AI, NLP, foundation models, multimodal models, diffusion models, LLMs, tokens), ML approaches (supervised, unsupervised, reinforcement), prompt tuning vs prompt engineering at definition level, the ML lifecycle stages (data ingestion, preparation, training, deployment, management) and the Google Cloud tool for each stage | choosing a model (b02), prompt techniques (b10) |
| b02 | T1.1, T1.2 | 22 | choosing a foundation model for a use case (modality, context window, security, availability, cost, performance, fine-tuning, customization) at concept level, gen AI use cases that create / summarize / discover / automate (text, image, code, video, data analysis, personalization); data types and business implications: data quality and accessibility (completeness, consistency, relevance, availability, cost, format), structured vs unstructured, labeled vs unlabeled | Google's model families (b03) |
| b03 | T1.3, T1.4 | 18 | the five layers of the gen AI landscape (infrastructure, models, platforms, agents, applications) and their business implications; Gemini, Gemma, Imagen, Veo: what each is for | Model Garden and Agent Platform (b07) |
| b04 | T2.1 | 15 | Google Cloud's strengths: AI-first approach, enterprise-ready platform (responsible, secure, private, reliable, scalable), integration across Google products, open approach, AI-optimized infrastructure (hypercomputer, TPUs, GPUs), data control and governance, democratizing AI (low-code/no-code, pre-trained models, APIs) | specific products (b05-b08) |
| b05 | T2.2 | 18 | the Gemini app and Gems, Gemini Enterprise (multimodal search, custom agents, notebooks), Gemini for Google Workspace: what each does and who it is for | Agent Platform (b07) |
| b06 | T2.3 | 14 | external search offerings (Agent Search, Google Search), Customer Engagement Suite (Conversational Agents, Agent Assist, Conversational Insights, Contact Center as a Service): use case and business value | RAG internals (b11), building agents (b07) |
| b07 | T2.4 | 16 | Agent Platform for developers: Model Garden, Agent Search, AutoML; Google Cloud's RAG offerings (prebuilt RAG with Agent Search, RAG APIs); building custom agents on Agent Platform | agent tooling (b08), grounding concepts (b11) |
| b08 | T2.5 | 16 | how agents use tools (extensions, functions, data stores, plugins) to reach the outside world, matching Google Cloud services and pre-built AI APIs to agent tooling (Cloud Storage, databases, Cloud Run, Speech-to-Text, Text-to-Speech, Translation, Document AI, Vision, Video Intelligence, Natural Language), Agent Studio vs Google AI Studio | building agents on Agent Platform (b07) |
| b09 | T3.1 | 16 | foundation model limits (data dependency, knowledge cutoff, bias, fairness, hallucination, edge cases), Google-recommended practices (grounding, RAG, prompt engineering, fine-tuning, human in the loop), monitoring and evaluation (automatic model upgrades, KPIs, versioning, drift, performance tracking, Feature Store) | prompting detail (b10), grounding detail (b11) |
| b10 | T3.2 | 14 | prompt engineering: purpose, zero-/one-/few-shot, role prompting, prompt chaining, chain-of-thought, ReAct: which technique for which task | limits and practices (b09) |
| b11 | T3.3 | 15 | grounding with enterprise, third-party and world data, how RAG changes output, Google grounding offerings (pre-built RAG with Agent Search, RAG APIs, Grounding with Google Search), sampling parameters and settings (token count, temperature, top-p, safety settings, output length) | RAG product details (b07) |
| b12 | T4.1, T4.2 | 23 | steps to implement a gen AI solution (solution types, business and technical factors, choosing the right solution, integrating into the organization, measuring impact); secure AI: security through the ML lifecycle, Google's Secure AI Framework (SAIF), Google Cloud security tools (secure-by-design infrastructure, IAM, Security Command Center, workload monitoring) | responsible AI (b13) |
| b13 | T4.3 | 11 | responsible AI and transparency, privacy (risks, anonymization vs pseudonymization), data quality, bias and fairness, accountability and explainability | secure AI (b12) |

Waves (about 4 writers at a time): b01, b04, b07, b10; then b02, b05, b08, b11; then b03, b06, b09, b12; then b13.
