# Foundry Aware: source notes (PLTR, not registered yet)

Source: course pages on learn.palantir.com, copied by the owner on 2026-11-12 (the site answers 403 to this
environment). Exam facts still unknown: question count, time, domains, weights, pass mark. Do not register a
`PLTR-*` Aware exam or write questions until the remaining items below are known.

## Foundry & AIP Aware program ("course of courses")
- About 8 hours; 7 courses (2 theoretical, 5 hands-on: basics up to a working real-world solution per module).
- Aim: build on Foundry & AIP, scope use cases, position Foundry & AIP within an enterprise IT landscape.
- For technical and non-technical users; completing it makes a participant eligible for the "Foundry Aware" exam.
- Order: a 15-minute conceptual introduction, then hands-on building (zero to an operational tool that
  harmonizes several data sources and solves a logistics problem).
- A later section highlights two developer building blocks: Data Connection (ingest from external systems) and
  Workshop (applications with quick release cycles).

## Course: Introduction to Foundry & AIP for Enterprise Organizations (22 lessons)
- Overview; Why Foundry & AIP: Enterprise Autonomy Vision; Linear to Decision-Centric Systems; AI Labor;
  High-Level Architecture of the Platform.
- S1 The Ontology: what it is; shared world for human + AI teams; three pillars of decision-centric systems.
- S2 South of the Ontology: data sources; logic sources; systems of action.
- S3 North of the Ontology: analytics and workflows; automations and progressive automation; products and SDKs.
- S4 AI infrastructure stack: common foundation for human + AI collaboration; evals in progressive automation;
  frontier models to enterprise outcomes.
- S5 Security, governance and deployment: security and governance layer; branching (safe change management for
  human and AI builders); Apollo (software delivery layer).

## Course: Deep Dive: Creating Your First Data Connection (45-60 min, copied 2026-11-12)
- Needs Foundry access and permission to create data sources and data egress policies; Palantir-provided sources.
- Setup: permissions, enabling an egress policy, a learning project and a course folder.
- Basic concepts; connecting an external system with Foundry.
- S3 source: open Data Connection, pick source type, create source, connection details, direct-connection egress
  policy, output folder, configure a data sync, view imported data.
- Relational database (Postgres): same steps plus configuring certificates.
- REST API: source, egress policy, code import configuration, a Code Repositories resource, external transform
  library, import the REST API source, code to access the data, commit and build the dataset.
- Wrap-up: considerations and best practices.

## Still needed (from the owner's browser)
- Only the names of all 7 courses in the Aware program (lesson details come from palantir.com/docs).
- The Foundry Aware exam page: question count, time, pass mark, proctoring, any topic list.
Facts in questions are checked on palantir.com/docs (reachable); course-only concepts (e.g. "AI labor",
"decision-centric systems") have no docs page, so the explanation must say they are course vocabulary.
