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

> [!NOTE] > **Team é um plano de Vectora Cloud**. Vectora Desktop (open source) é grátis para sempre. Team é para organizações que precisam de Vectora Cloud com SSO, on-premise, e SLA.

O plano **Team** é para grandes organizações com requisitos enterprise: SSO, on-premise, suporte 24/7, e SLA garantido. Assim como o Plus, oferece modos **BYOK** ou **Managed** (totalmente gerenciado).

**Pricing Customizado** - Contate [sales@vectora.app](mailto:sales@vectora.app)

## O Que Está Incluído

## Tudo do Pro, PLUS

| Feature                                           | Pro          | Team      |
| ------------------------------------------------- | ------------ | --------- |
| **Usuários Simultâneos**                          | 50           | Unlimited |
| **Rate Limiting**                                 | 2000 req/min | Custom    |
| **Tokens Unlimited**                              | [x]          | [x]       |
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
  server: "ldap://seu-ad.company.com"
  base_dn: "ou=users,dc=company,dc=com"
  auto_sync: true
```

## Managed Deployment

Vectora roda em infraestrutura dedicada e otimizada:

**Incluso**:

- Instância isolada (Single-tenant)
- MongoDB Atlas cluster gerenciado
- Redis cache distribuído
- PostgreSQL para metadata
- Prometheus + Grafana monitoring
- Daily backups automatizados

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

## Modelo de Pricing

```text
Base Fee: Customizado
+ Per-Seat: $X por usuário/mês (acima de N)
+ Custom Features: $Y por feature/mês
```

### Exemplo de Configuração

```text
Organização: 500 pessoas
Vectora Users: 100 devs
On-Premise: Sim
SSO: Azure AD
SLA: 99.99%

Estimativa:
- Base: $10,000/mês (on-prem + SSO + SLA)
- Seats (50-100): $50 × 50 = $2,500
- Custom Integration: $1,000
────────────────────
Total: ~$13,500/mês
```

## Contato para Pricing

**<sales@vectora.app>**
**Slack Enterprise Channel**
**Demo & Proposal: 48h**

## Option 1: Managed Cloud (Standard)

Vectora hospeda em infraestrutura enterprise-grade compartilhada com isolamento lógico.

## Option 2: Dedicated Managed Instance

Instância física/lógica isolada gerenciada pela Kaffyn:

```text
 Seu namespace, sua segurança dedicada
 Private endpoints (opcional)
 Redundância multi-region
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

Se não atingirmos SLA:

```text
Uptime | Credit
──────────────┼────────
99.9%-99.99% | 10% mês
99%-99.9% | 25% mês
< 99% | 50% mês
```

## Support

## Dedicated Support

- **24/7 Hotline**: Phone + Slack prioritário
- **Dedicated Account Manager**: Seu ponto de contato
- **Quarterly Business Reviews**: Strategy & optimization
- **Technical Consulting**: Arquitetura e best practices

## Support SLA

| Severity | Response | Resolution |
| -------- | -------- | ---------- |
| Critical | 15 min   | 4 hours    |
| High     | 1 hour   | 8 hours    |
| Medium   | 4 hours  | 24 hours   |
| Low      | 8 hours  | 5 days     |

## Custom Integrations

Team plans suportam integrações customizadas:

```yaml
custom_webhook:
  trigger: "index_completed"
  destination: "https://your-internal-system.com/webhook"
  headers:
    Authorization: "Bearer your-token"
  payload_transform: "custom.js"

# Exemplo: Custom embedding model
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

# Ou contate sales@vectora.app para suporte
```

**Processo**:

1. Assinatura contratual
2. Provisionamento de infraestrutura
3. Migração de dados (zero downtime)
4. SSO/LDAP setup
5. Training + onboarding

## Use Cases Ideais

## Enterprises

- Banco/Fintech com compliance rigoroso
- Healthcare com HIPAA
- Governo com segurança de dados
- SaaS multi-tenant com customers

## Large Teams

- 200+ engenheiros
- Múltiplas regiões
- Complex infrastructure
- Compliance requirements

## High-Scale

- 1B+ chunks indexados
- 10K+ requisições/hora
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

## FAQ Team

**P: Quanto custa?**
R: Customizado por org. Contate <sales@vectora.app> para proposta.

**P: Quanto tempo leva para deploy on-prem?**
R: 2-4 semanas incluindo setup, training, migração.

**P: Posso usar LDAP + Azure AD ao mesmo tempo?**
R: Sim, suportamos múltiplos provedores simultaneamente.

**P: Incluem backups?**
R: Sim, automated daily com retenção de 30 dias (customizável).

**P: Qual é o tempo de resposta para críticos?**
R: 15 min para assessment, 4 horas para resolve.

## Próximos Passos

1. **Schedule Demo**: [Calendly Link](https://calendly.com/vectora/team-demo)
2. **Technical Review**: Discuta requirements
3. **Proposal**: Pricing customizado
4. **Onboarding**: Dedicated account manager

**<sales@vectora.app>**

---

> **Próximo**: [Security & Guardian](../security/guardian.md)

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

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
