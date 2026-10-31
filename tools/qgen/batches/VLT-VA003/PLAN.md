# VLT-VA003 batch plan (one batch per exam section, topics owned per batch)
Exam: Vault Associate (003), content list read 2026-10-31. Target 250 (28 per section). Rules and facts: `tools/qgen/VAULT.md`. About 15-20% "(Select TWO)".
Narrow sections (D4 3 tasks, D6 2 tasks, D9 2 tasks) need 28 questions each: vary the angle (use case, CLI vs API vs UI, troubleshooting, what happens when, trade-offs,
Community vs Enterprise vs HCP Vault where the docs say so) so scenarios do not repeat. Before writing, read the published questions of the exam (`data/VLT-VA003.json`)
and use new scenarios. Hot spots belong to ONE batch only; others may use them as distractors.

| Batch | Tasks | Count | Owns | Leave to |
|---|---|---|---|---|
| b01 | D1 T1.1-T1.6 | 28 | purpose of auth methods, choosing (userpass, LDAP, OIDC/JWT, AppRole, Kubernetes, AWS/GCP/Azure, GitHub, TLS certs), human vs machine, entities/aliases/groups (internal/external), authenticating with CLI/API/UI, enabling/configuring auth methods, `vault login`, `VAULT_TOKEN` | Vault Agent auto-auth (b09), token details (b03) |
| b02 | D2 T2.1-T2.5 | 28 | policy purpose (deny by default, least privilege), path syntax (exact, glob `*`, `+`, segments), capabilities (create, read, update, delete, list, sudo, deny, patch), choosing policies from requirements, templated policies, `vault policy write/read/list`, root and default policies, how multiple policies combine | token creation (b03) |
| b03 | D3 T3.1-T3.6 | 28 | service vs batch tokens, root tokens (generate-root, revoke), accessors, token TTL/max TTL/periodic tokens, orphan tokens and parent-child revocation, creating tokens (`vault token create` options, roles), token hierarchy | lease semantics (b04) |
| b04 | D4 T4.1-T4.3 | 28 | lease IDs and prefixes, lease duration, renew (increment, renewable), revoke (single, prefix, force), what happens when a token or lease expires/is revoked, dynamic secret lifecycle, `vault lease` commands and API | token TTL mechanics (b03) |
| b05 | D5 T5.1-T5.8 | 28 | choosing and enabling secrets engines (KV v1/v2, database, AWS, PKI, SSH, transit at purpose level, cubbyhole, identity), static vs dynamic secrets, response wrapping, short-lived credentials, `vault secrets enable`, `vault kv put/get`, API/UI access, paths and mount points | transit mechanics (b06), leases (b04) |
| b06 | D6 T6.1-T6.2 | 28 | transit encrypt/decrypt (ciphertext prefix `vault:v1:`), key versions, rotating keys, min_decryption_version, rewrap, key types, why data stays outside Vault, convergent encryption, encryption as a service use cases, API/CLI | choosing secrets engines (b05) |
| b07 | D7 T7.1-T7.3 | 28 | how Vault encrypts data (barrier, encryption key, root key/unseal key chain), seal/unseal states and behavior, what a sealed Vault can/cannot do, initialization, environment variables (VAULT_ADDR, VAULT_TOKEN, VAULT_NAMESPACE, VAULT_FORMAT, VAULT_SKIP_VERIFY, VAULT_CACERT), `vault status` | Shamir details, auto-unseal, storage (b08) |
| b08 | D8 T8.1-T8.5 | 28 | cluster strategy, storage backends (Integrated Storage/Raft, Consul), Shamir secret sharing (key shares and threshold), auto-unseal, recovery keys, DR vs performance replication (Enterprise), self-managed vs HCP Vault | seal concepts (b07) |
| b09 | D9 T9.1-T9.2 | 28 | Vault Agent (auto-auth, sink, caching, templating), Vault Secrets Operator (Kubernetes CRDs, syncing secrets to Kubernetes Secrets), when to use Agent vs Secrets Operator vs direct API, Agent and VSO authentication | auth method choice (b01) |

Waves (about 4 writers at a time): b01, b02, b03, b04; then b05, b06, b07, b08; then b09.
