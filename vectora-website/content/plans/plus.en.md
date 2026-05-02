---
title: Plus
slug: plus
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - auth
  - byok
  - cicd
  - claude
  - concepts
  - concurrency
  - config
  - embeddings
  - errors
  - gemini
  - git
  - github-actions
  - go
  - guardian
  - json
  - mcp
  - metrics
  - openai
  - prometheus
  - protocol
  - rag
  - reranker
  - security
  - sso
  - vectora
  - voyage
  - yaml
---

{{< lang-toggle >}}

> [!NOTE] > **Plus is a Vectora Cloud plan**. If you are using Vectora Desktop (open source), this plan does not apply. Desktop is free forever. Plus is for Cloud SaaS.

The **Plus** plan is for teams scaling on Vectora Cloud. We offer two modes: **BYOK** (priority support and increased limits) or **Plus** (with included AI credits and managed storage).

**$29/month** per workspace (up to 50 users) - _Plus Plan includes base credits_

## What is Included

## Everything in Free, PLUS

| Feature                               | Free       | Plus         |
| ------------------------------------- | ---------- | ------------ |
| **Unlimited Namespaces**              | [x]        | [x]          |
| **Searches/month**                    | 30K        | Unlimited    |
| **Embedding Tokens/month**            | 1.5M       | Unlimited    |
| **LLM Tokens/month**                  | 1.5M       | Unlimited    |
| **Concurrent Users**                  | 1          | 50           |
| **Rate Limiting**                     | 60 req/min | 2000 req/min |
| **Webhooks**                          | -          | [x]          |
| **Custom Domain**                     | -          | [x]          |
| **API Tokens**                        | -          | [x]          |
| **Advanced Metrics**                  | -          | [x]          |
| **Priority Support**                  | -          | [x]          |
| **99.9% SLA**                         | -          | [x]          |
| **Custom Reranker**                   | -          | [x]          |
| **Managed Vectora Cognitive Runtime** | -          | [x]          |

## Premium Models

Access to more models (BYOK or Managed Plus):

| Component                     | Free              | Plus                   |
| ----------------------------- | ----------------- | ---------------------- |
| **Embedding**                 | Voyage 4          | Voyage 4 + Claude 3    |
| **Reranking**                 | Voyage Rerank 2.5 | + Custom (Cohere, etc) |
| **Vectora Cognitive Runtime** | Local Inference   | Managed Plus Cloud     |
| **LLM**                       | Gemini Flash      | + Claude, GPT-4        |

## Plus Limits

```yaml
plus_tier_limits:
  rate_limiting:
    requests_per_minute: 2000
    concurrent_users: 50

  storage:
    vector_index: unlimited
    embeddings_cache: 5GB
    logs_retention: 90 days

  performance:
    search_latency: <500ms (p99)
    max_file_size: 500MB
    max_chunks_per_query: 100
```

## Webhooks

Automate workflows with webhooks:

```bash
POST https://your-domain.vectora.app/webhooks/index
Authorization: Bearer sk-...
Content-Type: application/json

{
  "event": "repository.push",
  "branch": "main",
  "files_changed": 12
}

# Vectora will automatically reindex
```

## Available Events

| Event                 | Trigger                 |
| --------------------- | ----------------------- |
| `index.completed`     | After indexing finishes |
| `search.high_latency` | Search > 1s             |
| `quota.warning`       | 80% of quota reached    |
| `error.security`      | Guardian blocked access |
| `user.login`          | New user login          |

## Custom Domain

Access your server via a customized domain:

```bash
# Default (free)
https://api.vectora.app/project-abc123

# Custom (plus)
https://vectora.your-domain.com
# Or
https://code-search.your-domain.com
```

## CNAME Setup

```bash
# Your domain:
code-search.your-domain.com CNAME vectora-plus.cloud.app
```

## API Tokens

Create tokens for automation and CI/CD:

```bash
# Create token
vectora auth token create \
  --name "CI/CD Pipeline" \
  --ttl 365d \
  --scopes "search,index"

# Output: sk-proj-abc123xyz...

# Use in pipeline
curl -H "Authorization: Bearer sk-proj-abc123xyz..." \
  https://your-domain.vectora.com/search
```

## Available Scopes

```text
- search # Searches
- index # Indexing
- configure # Change config
- user # Manage users
- billing # View invoices
```

## Advanced Metrics

Dashboard with detailed metrics:

```text
Plus Users Dashboard
├─ Search Performance
│ ├─ p50 latency: 120ms
│ ├─ p95 latency: 280ms
│ ├─ p99 latency: 450ms
│ └─ Error rate: 0.1%
├─ Indexing Performance
│ ├─ Files indexed: 2,847
│ ├─ Chunks: 45,231
│ ├─ Index size: 150MB
│ └─ Last index: 2h ago
├─ User Activity
│ ├─ Active users: 23
│ ├─ Searches (24h): 1,234
│ ├─ Top queries: [...]
│ └─ Most used files: [...]
└─ Billing
   ├─ Current usage: $24.32
   ├─ Monthly limit: $100
   └─ Next billing: 2026-05-19
```

Export in CSV, JSON, or Prometheus.

## Priority Support

- **Email support**: <4h response time
- **Direct Slack channel**: For critical issues
- **Monthly office hours**: With Vectora team
- **Custom onboarding**: Setup + training

## Transparent Pricing

## Calculation

- **Base**: $29/month
- **Excess users**: $0.50/month per user (above 50)
- **Excess storage**: $0.10/GB/month (above 5GB)

```text
Example:
- 12 users: $29 (included up to 50)
- 120 users: $29 + (70 × $0.50) = $64
```

## No Surprises

- No setup fee
- Cancellation anytime
- No long-term contract
- Automatic billing

## Upgrade from Free

```bash
# Via CLI
vectora upgrade --plan plus --stripe-token sk_...

# Via dashboard
# https://console.vectora.app/settings/billing
```

## Automatic Migration

- All data preserved
- No downtime
- Namespaces maintained
- Settings intact

## Comparison: Free vs Pro

| Feature              | Free       | Plus         | Team      |
| -------------------- | ---------- | ------------ | --------- |
| **Price**            | Free       | $29/month    | Custom    |
| **Users**            | 1          | 50           | Unlimited |
| **Rate Limit**       | 60 req/min | 2000 req/min | Custom    |
| **Tokens/month**     | 1.5M       | Unlimited    | Unlimited |
| **Webhooks**         |            |              |           |
| **Custom Domain**    |            |              |           |
| **SLA**              |            | 99.9%        | 99.99%    |
| **Priority Support** |            |              |           |
| **SSO/LDAP**         |            |              |           |
| **On-Premise**       |            |              |           |

## Ideal Use Cases for Plus

- **Growing startups**: 5-50 devs, multiple projects
- **Agencies**: Manage projects from different clients
- **Remote teams**: Need 24/7 reliability
- **CI/CD Automation**: Webhooks for pipelines
- **Custom domain**: Own branding

## FAQ Plus

**Q: Can I downgrade to Free later?**
A: Yes, anytime. Your data is preserved.

**Q: How much does it cost with 100 users?**
A: $29 + (50 × $0.50) = $54/month

**Q: Does it include technical support?**
A: Yes, email <4h + priority Slack.

**Q: Can I use it in production?**
A: Yes, with 99.9% SLA (guaranteed uptime).

---

> **Next**: [Team Plan](./team.md)

---

## External Linking

| Concept               | Resource                             | Link                                                                                   |
| --------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **Anthropic Claude**  | Claude Documentation                 | [docs.anthropic.com/](https://docs.anthropic.com/)                                     |
| **Voyage AI**         | High-performance embeddings for RAG  | [www.voyageai.com/](https://www.voyageai.com/)                                         |
| **Voyage Embeddings** | Voyage Embeddings Documentation      | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)         |
| **Voyage Reranker**   | Voyage Reranker API                  | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)             |
| **MCP**               | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**        | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [License (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Part of the Vectora AI Agent ecosystem. Built with [ADK](https://adk.dev/), [Claude](https://claude.ai/) and [Go](https://golang.org/)._

© 2026 Vectora Contributors. All rights reserved.

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
