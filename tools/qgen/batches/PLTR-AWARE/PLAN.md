# PLTR-AWARE plan (Foundry Aware, 225 questions, b01-b09, 25 each)

Exam: Foundry Aware (Palantir foundation level). 60 multiple-choice questions, 120 min, open book, free.
Domains = the three sections of the Foundry & AIP Aware course (`tools/qgen/PALANTIR-AWARE.md`), equal weights.
Level: FOUNDATIONAL. Test understanding of what each part of the platform is for and which one fits a need;
no deep configuration trivia, no code syntax, no UI click paths (PALANTIR.md rule 4). Single answer, 4 options.
Sources: palantir.com/docs only (fetch with `tools/learn_fetch.py`, list pages as `# src:` lines). Course-only
vocabulary ("decision-centric systems", "AI labor", "enterprise autonomy", "north/south of the Ontology",
"progressive automation") has no docs page or only partial: G: says it is the course's framing and keys must still
be defensible from docs. Do not copy PLTR-DE/PLTR-APD/PLTR-AIE questions: grep their batches for your scenario first.
Writer report: max 150 words. Reviewer report: max 200 words.

## D1 Getting Acquainted with Foundry & AIP (75)
- b01 T1.1 (12) + T1.2 (13): platform value proposition, high-level architecture (data, logic, actions layers),
  operational vs analytical use; the Ontology concept: object types, properties, link types, action types as the
  shared model that humans, apps and AI agents read and write. Owns "what the Ontology is / why"; design details
  (primary keys, link cardinality) belong to b05.
- b02 T1.3 (13) + T1.4 (12): data sources, logic sources (models, functions), systems of action (writeback);
  analytics and workflows, automations (concept), products and SDKs (OSDK, concept); AI stack (LLMs via AIP,
  evals concept), security and governance (projects, roles, markings at concept level), Global Branching,
  Apollo (software delivery). Owns branching, markings, Apollo. Automate configuration belongs to b09.
- b03 T1.5 (25): the end-to-end speedrun path: bring several sources in, clean/harmonize them with Pipeline
  Builder, build objects, put a Workshop app in users' hands, iterate quickly. Owns Pipeline Builder and the
  "zero to production" flow; leaves Data Connection details to b04 and Workshop widgets to b06.

## D2 Building Blocks for Developers (75)
- b04 T2.1 (25): Data Connection: sources (S3, relational DB via JDBC, REST), agent vs direct connection,
  egress policies (why needed, direct connection), certificates, syncs (batch sync, output dataset/folder),
  viewing imported data, permissions to create sources. Owns egress policies and syncs.
- b05 T2.2 (10) + T2.3 (15): REST API ingest in code: external transforms / source imports in Code Repositories,
  commit and build a dataset (concept level, no syntax). Ontology design for an app: object type backed by a
  dataset, primary key, title property, property types, link types, action types (create/modify), writeback.
- b06 T2.4 (25): Workshop: widgets, variables, events, object sets/filters, forms that call actions,
  layouts, sharing/permissions to use the app, iterating and releasing. Owns all Workshop questions.

## D3 Applying Foundry & AIP in the Real World (75)
- b07 T3.1 (25): scoping use cases: good fit vs poor fit (operational decisions, many sources, writeback,
  people + AI acting on shared data), starting small with a valuable workflow, measuring outcomes, positioning
  Foundry & AIP next to existing ERP/CRM/warehouse/BI systems (integrate, not rip-and-replace).
- b08 T3.2 (12) + T3.3 (13): process mining with Machinery (process graphs, states, transitions, bottlenecks,
  using it to find where to act) and AIP Logic (no-code LLM functions on Ontology objects, tools, outputs,
  testing). Owns Machinery and AIP Logic.
- b09 T3.3 (25): agentic workflows: AIP agents (docs name the builder "AIP Chatbot Studio" where shown),
  tools and Ontology context, actions with human review, Automate triggers/effects, AIP Evals for testing
  LLM-backed functions, guardrails and permissions (agents act within user/service permissions). Owns Evals,
  Automate configuration and agents.
