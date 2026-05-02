---
title: Team
slug: team
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - auth
  - aws
  - byok
  - caching
  - compliance
  - concepts
  - concurrency
  - config
  - deployment
  - docker
  - embeddings
  - gcp
  - go
  - grafana
  - guardian
  - integration
  - logging
  - mcp
  - mongodb-atlas
  - oidc
  - prometheus
  - protocol
  - security
  - sso
  - system
  - team
  - vector-db
  - vector-search
  - vectora
  - yaml
---

{{< lang-toggle >}}

> [!NOTE] > **Team is a Vectora Cloud plan**. Vectora Desktop (open source) is free forever. Team is for organizations that need Vectora Cloud with SSO, on-premise, and SLA.

The **Team** plan is for large organizations with enterprise requirements: SSO, on-premise, 24/7 support, and guaranteed SLA. Like Plus, it offers **BYOK** or **Managed** (fully managed) modes.

**Custom Pricing** - Contact [sales@vectora.app](mailto:sales@vectora.app)

## What is Included

## Everything in Pro, PLUS

| Feature                                           | Pro          | Team      |
| ------------------------------------------------- | ------------ | --------- |
| **Concurrent Users**                              | 50           | Unlimited |
| **Rate Limiting**                                 | 2000 req/min | Custom    |
| **Unlimited Tokens**                              | [x]          | [x]       |
| **Webhooks**                                      | [x]          | [x]       |
| **Custom Domain**                                 | [x]          | [x]       |
| **SSO (SAML/OIDC)**                               | -            | [x]       |
| **LDAP/Active Directory**                         | -            | [x]       |
| **Dedicated Instance**                            | -            | [x]       |
| **99.99% SLA**                                    | 99.9% (SLA)  | [x]       |
| **Dedicated Support**                             | -            | [x]       |
| **Custom Integrations**                           | -            | [x]       |
| **Advanced Compliance**                           | -            | [x]       |
| **Audit Logging (Detailed)**                      | -            | [x]       |
| **Managed Vectora Cognitive Runtime (Dedicated)** | -            | [x]       |

## Enterprise Features

## SSO & Identity Management

```yaml
saml:
  enabled: true
  provider: "Okta|Azure AD|Google|Custom"
  auto_provisioning: true
  group_sync: true

ldap:
  enabled: true
  server: "ldap://your-ad.company.com"
  base_dn: "ou=users,dc=company,dc=com"
  auto_sync: true
```

## Managed Deployment

Vectora runs on dedicated and optimized infrastructure:

**Included**:

- Isolated instance (Single-tenant)
- Managed MongoDB Atlas cluster
- Distributed Redis cache
- PostgreSQL for metadata
- Prometheus + Grafana monitoring
- Automated daily backups

## Advanced Compliance

```yaml
compliance:
  data_residency: "EU|US|Custom"
  encryption_at_rest: "AES-256"
  encryption_in_transit: "TLS 1.3"
  audit_retention: "7 years"
  gdpr_compliance: true
  hipaa_compliance: true
  soc2_compliance: true
```

## Pricing

## Pricing Model

```text
Base Fee: Custom
+ Per-Seat: $X per user/month (above N)
+ Custom Features: $Y per feature/month
```

### Configuration Example

```text
Organization: 500 people
Vectora Users: 100 devs
On-Premise: Yes
SSO: Azure AD
SLA: 99.99%

Estimate:
- Base: $10,000/month (on-prem + SSO + SLA)
- Seats (50-100): $50 × 50 = $2,500
- Custom Integration: $1,000
 ────────────────────
Total: ~$13,500/month
```

## Contact for Pricing

**<sales@vectora.app>**
**Slack Enterprise Channel**
**Demo & Proposal: 48h**

## Option 1: Managed Cloud (Standard)

Vectora hosts on enterprise-grade shared infrastructure with logical isolation.

## Option 2: Dedicated Managed Instance

Physical/logical isolated instance managed by Kaffyn:

```text
 Your namespace, your dedicated security
 Private endpoints (optional)
 Multi-region redundancy
 Automatic failover
 Daily encrypted backups
```

## SLA & Uptime

### 99.99% SLA (Team Plan)

```text
Availability: 99.99% per month
Downtime allowed: 4.3 minutes/month

Response Times:
- Severity 1 (Critical): <1 hour
- Severity 2 (High): <4 hours
- Severity 3 (Medium): <8 hours
- Severity 4 (Low): <24 hours
```

### Compensation

If we do not meet SLA:

```text
Uptime | Credit
──────────────┼────────
99.9%-99.99% | 10% month
99%-99.9% | 25% month
< 99% | 50% month
```

## Support

## Dedicated Support

- **24/7 Hotline**: Priority Phone + Slack
- **Dedicated Account Manager**: Your point of contact
- **Quarterly Business Reviews**: Strategy & optimization
- **Technical Consulting**: Architecture and best practices

## Support SLA

| Severity | Response | Resolution |
| -------- | -------- | ---------- |
| Critical | 15 min   | 4 hours    |
| High     | 1 hour   | 8 hours    |
| Medium   | 4 hours  | 24 hours   |
| Low      | 8 hours  | 5 days     |

## Custom Integrations

Team plans support custom integrations:

```yaml
custom_webhook:
  trigger: "index_completed"
  destination: "https://your-internal-system.com/webhook"
  headers:
    Authorization: "Bearer your-token"
  payload_transform: "custom.js"

# Example: Custom embedding model
custom_embedding:
  provider: "internal-huggingface"
  model: "your-model"
  endpoint: "https://ml.company.com/embed"
  auth: "api_key"
```

## Compliance & Security

## Certifications

- **SOC 2 Type II**
- **GDPR Compliant**
- **HIPAA Ready**
- **CCPA Compliant**
- **ISO 27001** (on-request)
- **FedRAMP Ready** (govtech)

## Data Security

```yaml
encryption:
  at_rest: "AES-256-GCM"
  in_transit: "TLS 1.3"
  key_management: "BYOK, Managed (Plus) or HSM"
  key_rotation: "automatic"

access_control:
  mfa: "required"
  ip_whitelist: "supported"
  network_isolation: "yes"
  audit_logging: "detailed"

compliance_reports:
  soc2_attestation: "annual"
  penetration_testing: "annual"
  vulnerability_scanning: "continuous"
```

## Migration from Pro

```bash
# Zero downtime upgrade
vectora upgrade --plan team

# Or contact sales@vectora.app for support
```

**Process**:

1. Contract signature
2. Infrastructure provisioning
3. Data migration (zero downtime)
4. SSO/LDAP setup
5. Training + onboarding

## Ideal Use Cases

## Enterprises

- Bank/Fintech with strict compliance
- Healthcare with HIPAA
- Government with data security
- Multi-tenant SaaS with customers

## Large Teams

- 200+ engineers
- Multiple regions
- Complex infrastructure
- Compliance requirements

## High-Scale

- 1B+ indexed chunks
- 10K+ requests/hour
- Real-time analytics
- Mission-critical operations

## Technical Specs (Team)

```yaml
performance:
  search_latency_p99: <200ms
  concurrent_users: unlimited
  rate_limit: customizable
  uptime: 99.99%

scale:
  max_chunks: unlimited
  max_file_size: 1GB
  max_index_size: unlimited
  storage: custom

regions:
  availability: multi-region redundancy
  failover: automatic
  geo_replication: yes
```

## Team FAQ

**Q: How much does it cost?**
A: Customized by organization. Contact <sales@vectora.app> for a proposal.

**Q: How long does on-prem deployment take?**
A: 2-4 weeks including setup, training, migration.

**Q: Can I use LDAP + Azure AD at the same time?**
A: Yes, we support multiple providers simultaneously.

**Q: Do you include backups?**
A: Yes, automated daily with 30-day retention (customizable).

**Q: What is the response time for critical issues?**
A: 15 min for assessment, 4 hours to resolve.

## Next Steps

1. **Schedule Demo**: [Calendly Link](https://calendly.com/vectora/team-demo)
2. **Technical Review**: Discuss requirements
3. **Proposal**: Custom pricing
4. **Onboarding**: Dedicated account manager

**<sales@vectora.app>**

---

> **Next**: [Security & Guardian](../security/guardian.md)

---

## External Linking

| Concept              | Resource                             | Link                                                                                                       |
| -------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**    | Atlas Vector Search Documentation    | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **MCP**              | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**       | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |
| **Anthropic Claude** | Claude Documentation                 | [docs.anthropic.com/](https://docs.anthropic.com/)                                                         |
| **Docker**           | Docker Documentation                 | [docs.docker.com/](https://docs.docker.com/)                                                               |
| **OpenID Connect**   | OIDC Core 1.0 Specification          | [openid.net/specs/openid-connect-core-1_0.html](https://openid.net/specs/openid-connect-core-1_0.html)     |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [License (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Part of the Vectora AI Agent ecosystem. Built with [ADK](https://adk.dev/), [Claude](https://claude.ai/) and [Go](https://golang.org/)._

© 2026 Vectora Contributors. All rights reserved.

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
