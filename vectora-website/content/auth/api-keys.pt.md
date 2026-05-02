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

As API Keys do Vectora são usadas para autenticação programática e integração com ferramentas de terceiros que não suportam fluxos interativos de SSO.

## Visão Geral

Diferente do JWT, que é destinado a sessões de curta duração, as API Keys são persistentes e permitem o acesso controlado a namespaces específicos do Vectora.

## Segurança

O Vectora utiliza hashing unidirecional (SHA-256) para armazenar suas chaves. Isso significa que, mesmo se o banco de dados for comprometido, suas chaves originais não podem ser recuperadas.

## Como Usar

Para autenticar uma requisição REST usando uma API Key, envie o cabeçalho `X-API-Key`:

```bash
curl -X POST https://api.vectora.app/v1/search \
  -H "X-API-Key: vca_live_xxxxxxxxxxxx" \
  -H "Content-Type: application/json" \
  -d '{"query": "como funciona o auth?"}'
```

## Gestão de Chaves

Você pode gerenciar suas chaves através da CLI do Vectora:

```bash
vectora auth keys create --name "GitHub Actions" --namespace "prod"

# Listar chaves ativas
vectora auth keys list

# Revogar uma chave
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

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
