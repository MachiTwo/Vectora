---
title: "Security: Modelo de Segurança do Vectora"
slug: security
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - auth
  - injection
  - jwt
  - privacy
  - rbac
  - security
  - vectora
draft: false
---

{{< lang-toggle >}}

{{< section-toggle >}}

O modelo de segurança do Vectora tem três pilares: autenticação JWT, autorização RBAC e privacidade de dados — nenhum código do usuário sai da máquina local. A API é protegida contra injeção, rate limiting por usuário e validação Pydantic em todos os endpoints.

## Pilares de Segurança

| Pilar             | Implementação        | Detalhe                                     |
| ----------------- | -------------------- | ------------------------------------------- |
| **Autenticação**  | JWT HS256            | Bearer token com expiração de 1h            |
| **Autorização**   | RBAC 5 níveis        | 15 permissões hierárquicas                  |
| **Privacidade**   | Local-first          | Código não sai da máquina                   |
| **Injeção**       | Validação Pydantic   | Input sanitizado em todos os endpoints      |
| **Rate Limiting** | Redis sliding window | 60 requests/minuto por usuário              |
| **TLS**           | HTTPS em produção    | Certificado Let's Encrypt via reverse proxy |

## Autenticação JWT

Todos os endpoints protegidos exigem `Authorization: Bearer <token>`. Tokens são assinados com HS256 e carregam `user_id`, `role` e `jti` (ID único para revogação).

Tokens de acesso expiram em 1 hora. Tokens de refresh expiram em 7 dias. A revogação é feita marcando o token como revogado no PostgreSQL via `jti`.

**[Ver JWT Setup](../auth/jwt-setup.md)**

## Autorização RBAC

O middleware FastAPI verifica a permissão necessária para cada endpoint antes de processar a request. A verificação usa o `role` do JWT — sem consulta ao banco por request.

**[Ver RBAC](../auth/rbac.md)**

## Privacidade de Dados

O código indexado nunca sai da máquina local:

- **Embeddings VoyageAI**: apenas o texto do chunk é enviado à API VoyageAI. O resultado (vetor numérico) é armazenado localmente no LanceDB.
- **LanceDB**: roda completamente em disco local, sem servidor externo.
- **LLM externo**: apenas a query e o contexto relevante (top-10 chunks) são enviados ao LLM. O restante do codebase não é transmitido.

**[Ver Privacidade de Dados](./data-privacy.md)**

## Prevenção de Injeção

Todos os inputs passam por validação Pydantic antes de atingir qualquer lógica de negócio. Queries SQL usam placeholders parametrizados — sem concatenação de string.

**[Ver Prevenção de Injeção](./injection-prevention.md)**

## Rate Limiting

Rate limiting é aplicado via middleware Redis, limitando cada usuário a 60 requests/minuto. Respostas excedem o limite com HTTP 429.

```python
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    user = extract_user_from_request(request)
    if user and not check_rate_limit(user["id"]):
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit exceeded. Try again in 60 seconds."},
        )
    return await call_next(request)
```

## Headers de Segurança

O servidor FastAPI retorna headers de segurança em todas as respostas:

```python
@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000"
    return response
```

## External Linking

| Conceito         | Recurso                        | Link                                                                                                         |
| ---------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| **OWASP Top 10** | Web application security risks | [owasp.org/www-project-top-ten](https://owasp.org/www-project-top-ten/)                                      |
| **JWT RFC 7519** | JSON Web Token specification   | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)                       |
| **RBAC NIST**    | Role-Based Access Control      | [csrc.nist.gov/projects/role-based-access-control](https://csrc.nist.gov/projects/role-based-access-control) |
| **Pydantic**     | Data validation                | [docs.pydantic.dev](https://docs.pydantic.dev/)                                                              |
