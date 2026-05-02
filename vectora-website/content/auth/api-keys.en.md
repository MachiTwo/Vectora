---
title: API Keys
slug: api-keys
date: "2026-04-23T00:00:00-03:00"
type: docs
tags:
  - adk
  - agents
  - ai
  - api-keys
  - auth
  - build
  - claude
  - concepts
  - deployment
  - gcp
  - github-actions
  - go
  - integration
  - json
  - jwt
  - rbac
  - reference
  - security
  - sso
  - tools
  - tutorial
  - vectora
---

{{< lang-toggle >}}

Vectora API Keys are used for programmatic authentication and integration with third-party tools that do not support interactive SSO flows.

## Overview

Unlike JWT, which is intended for short-lived sessions, API Keys are persistent and allow controlled access to specific Vectora namespaces.

## Security

Vectora uses one-way hashing (SHA-256) to store your keys. This means that even if the database is compromised, your original keys cannot be recovered.

## How to Use

To authenticate a REST request using an API Key, send the `X-API-Key` header:

```bash
curl -X POST https://api.vectora.app/v1/search \
  -H "X-API-Key: vca_live_xxxxxxxxxxxx" \
  -H "Content-Type: application/json" \
  -d '{"query": "how does auth work?"}'
```

## Key Management

You can manage your keys through the Vectora CLI:

```bash
vectora auth keys create --name "GitHub Actions" --namespace "prod"

# List active keys
vectora auth keys list

# Revoke a key
vectora auth keys revoke <key_id>
```

## External Linking

| Concept              | Resource                                       | Link                                                                                   |
| -------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Anthropic Claude** | Claude Documentation                           | [docs.anthropic.com/](https://docs.anthropic.com/)                                     |
| **JWT**              | RFC 7519: JSON Web Token Standard              | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519) |
| **RBAC**             | NIST Role-Based Access Control Standard        | [csrc.nist.gov/projects/rbac](https://csrc.nist.gov/projects/rbac)                     |
| **REST API Design**  | RESTful API Best Practices                     | [restfulapi.net/](https://restfulapi.net/)                                             |
| **GitHub Actions**   | Automate your workflow from idea to production | [docs.github.com/en/actions](https://docs.github.com/en/actions)                       |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
