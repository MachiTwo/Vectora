---
title: "Auth: Autenticação e Autorização"
slug: auth
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - auth
  - authentication
  - authorization
  - jwt
  - rbac
  - security
  - vectora
draft: false
---

{{< lang-toggle >}}

{{< section-toggle >}}

O sistema de autenticação do Vectora usa JWT Bearer tokens para autenticação e RBAC (Role-Based Access Control) com 5 níveis hierárquicos para autorização. Tokens são validados em cada request via middleware FastAPI antes de atingir qualquer endpoint protegido.

## Fluxo de Autenticação

```text
POST /auth/login {email, password}
  |
  +-> Valida credenciais no PostgreSQL
  |
  +-> Gera access_token (JWT, 1h) + refresh_token (JWT, 7d)
  |
  +-> Persiste sessão no PostgreSQL
  |
  +-> Retorna {access_token, refresh_token, expires_in}

GET /api/v1/search
  Authorization: Bearer <access_token>
  |
  +-> Middleware extrai e valida JWT
  |
  +-> Carrega user + role do PostgreSQL
  |
  +-> Verifica permissão RBAC para o endpoint
  |
  +-> Passa para o handler
```

## JWT (JSON Web Tokens)

JWT Bearer é o mecanismo de autenticação stateless do Vectora. O token carrega o `user_id` e `role` assinados com HS256, verificados em cada request sem consulta ao banco.

Estrutura do payload:

```json
{
  "sub": "user-uuid-here",
  "role": "developer",
  "iat": 1746320000,
  "exp": 1746323600,
  "jti": "unique-token-id"
}
```

**[Ver JWT Setup](./jwt-setup.md)**

## RBAC (Role-Based Access Control)

O RBAC define 5 roles hierárquicos com 15 permissões distribuídas. Cada role herda as permissões do role anterior:

| Role         | Nível | Acesso                         |
| ------------ | ----- | ------------------------------ |
| `viewer`     | 1     | Leitura de resultados de busca |
| `developer`  | 2     | Busca + execução de agente     |
| `operator`   | 3     | Developer + indexação + VCR    |
| `admin`      | 4     | Operator + gestão de usuários  |
| `superadmin` | 5     | Admin + configuração global    |

**[Ver RBAC](./rbac.md)**

## Middleware FastAPI

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def require_auth(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict:
    token = credentials.credentials
    payload = verify_jwt(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
        )
    return payload
```

Uso nos endpoints:

```python
@app.post("/api/v1/search")
async def search(
    body: SearchRequest,
    user: dict = Depends(require_auth),
) -> SearchResponse:
    require_permission(user["role"], "search:execute")
    ...
```

## Endpoints de Auth

| Endpoint        | Método | Descrição                             |
| --------------- | ------ | ------------------------------------- |
| `/auth/login`   | POST   | Gera access + refresh token           |
| `/auth/refresh` | POST   | Renova access token via refresh token |
| `/auth/logout`  | POST   | Revoga sessão ativa                   |
| `/auth/me`      | GET    | Retorna dados do usuário autenticado  |

## External Linking

| Conceito             | Recurso                    | Link                                                                                                         |
| -------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **JWT RFC 7519**     | JSON Web Token standard    | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)                       |
| **RBAC**             | Role-Based Access Control  | [csrc.nist.gov/projects/role-based-access-control](https://csrc.nist.gov/projects/role-based-access-control) |
| **OAuth 2.0**        | Authorization framework    | [datatracker.ietf.org/doc/html/rfc6749](https://datatracker.ietf.org/doc/html/rfc6749)                       |
| **FastAPI Security** | FastAPI security utilities | [fastapi.tiangolo.com/tutorial/security](https://fastapi.tiangolo.com/tutorial/security/)                    |
