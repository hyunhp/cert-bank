# SC-900 batch plan (topics owned per batch)

Exam: SC-900 Microsoft Security, Compliance, and Identity Fundamentals. Skills as of 2026-10-21. 45 minutes, pass 700.
Target 225 (D1 28, D2 62, D3 84, D4 51). Fundamentals: describe and choose capabilities; no portal clicks, no CLI.
Keys must be GA and use current names (Microsoft Entra, Microsoft Defender XDR, Microsoft Purview, Microsoft Sentinel).
Shared hot spots belong to ONE batch only; others may use them as distractors but not as the tested concept.

| Batch | Tasks | Count | Owns | Leave to |
|---|---|---|---|---|
| b01 | T1.1 security and compliance concepts, T1.2 identity concepts | 28 | shared responsibility, defense in depth, Zero Trust principles, encryption vs hashing, GRC (data residency, sovereignty, privacy), identity as perimeter, authentication vs authorization, identity providers, directory services/AD DS, federation | Entra features (b02/b03) |
| b02 | T2.1 Entra ID and identity types, T2.2 authentication | 31 | Entra ID editions/what it is, users/guests/devices, workload identities (service principals, managed identities), hybrid identity (Connect/Cloud Sync, PHS/PTA/federation), authentication methods (passwordless, Windows Hello, FIDO2, Authenticator, passkeys), MFA, SSPR, password protection | Conditional Access, roles, governance, ID Protection (b03) |
| b03 | T2.3 access management, T2.4 identity protection and governance | 31 | Conditional Access (signals, decisions), Entra roles vs Azure RBAC, Entra ID Governance (entitlement management, lifecycle workflows), access reviews, PIM, Entra ID Protection (user/sign-in risk) | Defender for Identity (b06) |
| b04 | T3.1 core infrastructure security in Azure | 28 | DDoS Protection tiers, Azure Firewall, WAF, VNet segmentation, NSGs, Azure Bastion, Key Vault | Defender for Cloud (b05) |
| b05 | T3.2 Defender for Cloud, T3.3 Sentinel | 28 | Defender for Cloud (CSPM, secure score, recommendations, regulatory compliance standards, workload protection plans), SIEM vs SOAR, Sentinel (data connectors, analytics rules, incidents, playbooks, hunting, workbooks) | Defender XDR products (b06) |
| b06 | T3.4 Defender XDR | 28 | Defender XDR (incidents, unified portal), Defender for Office 365, Endpoint, Cloud Apps (CASB), Identity, Vulnerability Management, Threat Intelligence, Defender portal | Sentinel (b05) |
| b07 | T4.1 Service Trust Portal and privacy, T4.2 Purview compliance management | 25 | Service Trust Portal offerings, Microsoft privacy principles, Purview portal, Compliance Manager (assessments, improvement actions), compliance score | labels/DLP/retention (b08) |
| b08 | T4.3 information protection, lifecycle, governance; T4.4 insider risk, eDiscovery, audit | 26 | data classification (sensitive info types, trainable classifiers), Content explorer vs Activity explorer, sensitivity labels and policies, DLP, records management, retention policies/labels, insider risk management, eDiscovery, Audit (Standard/Premium) | Compliance Manager (b07) |
