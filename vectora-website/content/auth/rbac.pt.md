---
title: "RBAC: Controle de Acesso por Papel"
slug: rbac
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - auth
  - authorization
  - fastapi
  - permissions
  - rbac
  - roles
  - security
  - vectora
---

{{< lang-toggle >}}

{{< section-toggle >}}

O RBAC do Vectora define 5 roles hierárquicos com 15 permissões distribuídas. Cada role herda todas as permissões dos roles anteriores. A verificação é feita via middleware FastAPI usando o `role` extraído do JWT — sem consulta ao banco a cada request.

## Hierarquia de Roles

```text
superadmin (5)
  |__ admin (4)
        |__ operator (3)
              |__ developer (2)
                    |__ viewer (1)
```

## Permissões por Role

| Permissão        | viewer | developer | operator | admin | superadmin |
| ---------------- | ------ | --------- | -------- | ----- | ---------- |
| `search:read`    | x      | x         | x        | x     | x          |
| `search:execute` |        | x         | x        | x     | x          |
| `search:filter`  |        | x         | x        | x     | x          |
| `agent:run`      |        | x         | x        | x     | x          |
| `agent:stream`   |        | x         | x        | x     | x          |
| `index:read`     |        |           | x        | x     | x          |
| `index:write`    |        |           | x        | x     | x          |
| `index:delete`   |        |           | x        | x     | x          |
| `vcr:read`       |        |           | x        | x     | x          |
| `vcr:configure`  |        |           |          | x     | x          |
| `users:read`     |        |           |          | x     | x          |
| `users:write`    |        |           |          | x     | x          |
| `users:delete`   |        |           |          |       | x          |
| `system:config`  |        |           |          |       | x          |
| `system:audit`   |        |           |          |       | x          |

## Implementação

### Definição de permissões

```python
from enum import Enum

class Role(str, Enum):
    VIEWER = "viewer"
    DEVELOPER = "developer"
    OPERATOR = "operator"
    ADMIN = "admin"
    SUPERADMIN = "superadmin"

ROLE_HIERARCHY = {
    Role.VIEWER: 1,
    Role.DEVELOPER: 2,
    Role.OPERATOR: 3,
    Role.ADMIN: 4,
    Role.SUPERADMIN: 5,
}

PERMISSIONS: dict[str, Role] = {
    "search:read": Role.VIEWER,
    "search:execute": Role.DEVELOPER,
    "search:filter": Role.DEVELOPER,
    "agent:run": Role.DEVELOPER,
    "agent:stream": Role.DEVELOPER,
    "index:read": Role.OPERATOR,
    "index:write": Role.OPERATOR,
    "index:delete": Role.OPERATOR,
    "vcr:read": Role.OPERATOR,
    "vcr:configure": Role.ADMIN,
    "users:read": Role.ADMIN,
    "users:write": Role.ADMIN,
    "users:delete": Role.SUPERADMIN,
    "system:config": Role.SUPERADMIN,
    "system:audit": Role.SUPERADMIN,
}
```

### Verificação de permissão

```python
from fastapi import HTTPException, status

def has_permission(role: str, permission: str) -> bool:
    user_level = ROLE_HIERARCHY.get(Role(role), 0)
    required_role = PERMISSIONS.get(permission)
    if not required_role:
        return False
    required_level = ROLE_HIERARCHY[required_role]
    return user_level >= required_level

def require_permission(role: str, permission: str) -> None:
    if not has_permission(role, permission):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Permissão '{permission}' necessária",
        )
```

### Dependency FastAPI

```python
from fastapi import Depends
from functools import partial

def permission_required(permission: str):
    async def _check(user: dict = Depends(require_auth)) -> dict:
        require_permission(user["role"], permission)
        return user
    return _check

# Uso nos endpoints:
@app.post("/api/v1/search")
async def search(
    body: SearchRequest,
    user: dict = Depends(permission_required("search:execute")),
) -> SearchResponse:
    ...

@app.post("/api/v1/search/index")
async def index(
    body: IndexRequest,
    user: dict = Depends(permission_required("index:write")),
) -> dict:
    ...
```

## Gestão de Usuários (Admin)

### Atualizar role de usuário

```python
@app.patch("/auth/users/{user_id}/role")
async def update_user_role(
    user_id: str,
    role: Role,
    admin: dict = Depends(permission_required("users:write")),
) -> dict:
    if ROLE_HIERARCHY[role] >= ROLE_HIERARCHY[Role(admin["role"])]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Não é possível elevar um usuário ao seu próprio nível ou acima",
        )
    update_user_role_in_db(user_id, role)
    return {"user_id": user_id, "new_role": role}
```

A regra de não poder elevar acima do próprio nível previne escalada de privilégios — um admin não pode criar outro admin ou superadmin.

## Respostas HTTP por Erro de Auth

| Situação                | Código | Detalhe                      |
| ----------------------- | ------ | ---------------------------- |
| Token ausente           | `401`  | `Bearer token required`      |
| Token inválido/expirado | `401`  | `Token inválido ou expirado` |
| Role insuficiente       | `403`  | `Permissão 'X' necessária`   |
| Conta desativada        | `403`  | `Conta desativada`           |

## External Linking

| Conceito                         | Recurso                        | Link                                                                                                         |
| -------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| **RBAC**                         | NIST Role-Based Access Control | [csrc.nist.gov/projects/role-based-access-control](https://csrc.nist.gov/projects/role-based-access-control) |
| **Principle of Least Privilege** | OWASP guidance                 | [owasp.org/www-community/Access_Control](https://owasp.org/www-community/Access_Control)                     |
| **FastAPI Dependencies**         | Dependency injection system    | [fastapi.tiangolo.com/tutorial/dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)            |
| **JWT RFC 7519**                 | JSON Web Token standard        | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)                       |
