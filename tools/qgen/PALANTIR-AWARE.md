# Foundry Aware: source notes (PLTR, not registered yet)

Source: course pages on learn.palantir.com, copied by the owner on 2026-11-12 (the site answers 403 to this
environment). Exam facts (lesson "Conclusions and Certification Exam", copied 2026-11-12): 60 multiple-choice questions,
120 minutes, open note and open website, retakes allowed, free (certification.palantir.com, "Foundation" level).
Not published: pass mark, domains, weights. Registered as `PLTR-AWARE` on 2026-11-12 (225 questions, b01-b09).

## Foundry & AIP Aware program ("course of courses")
- About 8 hours; 7 courses (2 theoretical, 5 hands-on: basics up to a working real-world solution per module).
- Aim: build on Foundry & AIP, scope use cases, position Foundry & AIP within an enterprise IT landscape.
- For technical and non-technical users; completing it makes a participant eligible for the "Foundry Aware" exam.
- Order: a 15-minute conceptual introduction, then hands-on building (zero to an operational tool that
  harmonizes several data sources and solves a logistics problem).
- A later section highlights two developer building blocks: Data Connection (ingest from external systems) and
  Workshop (applications with quick release cycles).

## Program structure (copied 2026-11-12; 15 lessons, 7 courses)
1. Getting Acquainted with Foundry & AIP: Introduction to Foundry & AIP for Enterprise Organizations (theory);
   Speedrun: Your first End-to-End Workflow.
2. Building Blocks for Developers: Deep Dive: Creating your first Data Connection; Deep Dive: Building your first
   Application.
3. Applying Foundry & AIP in the Real World: Scoping Use Cases for Foundry & AIP (theory); Speedrun: Mining your
   first Business Process; Speedrun: Your first Agentic AIP Workflow.
4. Wrapping Up: Conclusions and Certification Exam (lesson that leads to the exam).
Planned domains if registered (own split, equal weights, `weightsAssumed`): D1 = section 1, D2 = section 2,
D3 = section 3.

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

## Sources

Facts in questions are checked on palantir.com/docs (reachable); course-only concepts (e.g. "AI labor",
"decision-centric systems") have no docs page, so the explanation must say they are course vocabulary.
