# Microsoft Foundry / Azure AI status facts (AI-901, AI-103)

Facts that reviewers confirmed on learn.microsoft.com while building the AI-901 and AI-103 banks. Foundry changes
fast: a keyed answer must rest on a GA feature, so re-check a fact here on Learn (`python3 tools/learn_fetch.py
--grep ...`) when it is older than a few months, and add new findings with their date. AZ-900/AZ-104 writers do not
need this file.

Checked during the AI-901 reviews (2026-10-29): "Guardrails (previously content filters)"; roles Foundry User (formerly
Azure AI User), do not use Azure AI Developer or Cognitive Services* roles for Foundry projects; agents use agents +
conversations + responses (classic threads/messages/runs deprecated, retire 2027-03-31); Azure Language key phrases,
sentiment/opinion mining and summarization are "legacy" (retire 2029-03-31; PII, language detection, NER are core);
Language Studio retires 2027-03-20; Image Analysis v3.2/v4.0 and Custom Vision retire 2028-09-25 (never key them);
dall-e-3 retired 2026-03-04, GPT-image-2 and the GPT-image-2.5 models are GA while GPT-image-1/1-mini/1.5 are limited-access preview; Realtime API
with gpt-realtime and Voice Live API are GA, gpt-audio chat completions uses a preview API version.
Checked during the AI-103 reviews (2026-10-30): Azure OpenAI On Your Data retired 2026-10-14; Foundry portal workflows
retire 2026-12-01 (use Microsoft Agent Framework; Python/.NET not labelled preview); Connected Agents not in the new
Agent Service, a2a tool (A2A v1.0) GA; Memory, agent guardrails, Task Adherence/Intent Resolution/Task Completion
evaluators, the agent Monitor tab metrics, AI Red Teaming Agent and Sora 2 are preview; Foundry IQ knowledge bases are
GA in Search REST 2026-04-01 only with minimal extractive retrieval (query planning/answer synthesis preview); model
router GA (session affinity and routing metadata preview); Translator text API 2026-06-06 GA with NMT or LLM choice;
LLM Speech GA; Content Understanding pro mode existed only in a retired preview API; capacity units per TPM vary by model.
