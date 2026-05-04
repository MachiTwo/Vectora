---
title: "JWT Setup: Tokens de Autenticação"
slug: jwt-setup
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - auth
  - authentication
  - fastapi
  - jwt
  - python
  - security
  - sessions
  - vectora
---

{{< lang-toggle >}}

{{< section-toggle >}}

O Vectora usa JWT HS256 para autenticação stateless. Access tokens expiram em 1 hora, refresh tokens em 7 dias. A validação é feita localmente sem consulta ao banco — o payload contém `user_id`, `role` e `jti` (JWT ID único para revogação).

## Dependências

```bash
uv add PyJWT python-jose[cryptography]
```

## Geração de Tokens

```python
import jwt
import uuid
from datetime import datetime, timedelta, timezone

SECRET_KEY = "sua-chave-secreta-minimo-32-chars"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7

def create_access_token(user_id: str, role: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "role": role,
        "iat": now,
        "exp": now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        "jti": str(uuid.uuid4()),
        "type": "access",
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(user_id: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "iat": now,
        "exp": now + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS),
        "jti": str(uuid.uuid4()),
        "type": "refresh",
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
```

## Validação de Tokens

```python
def verify_jwt(token: str) -> dict | None:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def verify_access_token(token: str) -> dict | None:
    payload = verify_jwt(token)
    if not payload:
        return None
    if payload.get("type") != "access":
        return None
    return payload
```

## Endpoint de Login

```python
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(prefix="/auth")

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int = ACCESS_TOKEN_EXPIRE_MINUTES * 60

@router.post("/login", response_model=TokenResponse)
async def login(body: LoginRequest) -> TokenResponse:
    user = get_user_by_email(body.email)
    if not user or not verify_password(body.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos",
        )
    if not user["is_active"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Conta desativada",
        )

    access_token = create_access_token(user["id"], user["role"])
    refresh_token = create_refresh_token(user["id"])

    save_session(user["id"], access_token, refresh_token)

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
    )
```

## Endpoint de Refresh

```python
class RefreshRequest(BaseModel):
    refresh_token: str

@router.post("/refresh", response_model=TokenResponse)
async def refresh(body: RefreshRequest) -> TokenResponse:
    payload = verify_jwt(body.refresh_token)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token inválido",
        )

    user = get_user_by_id(payload["sub"])
    if not user or not user["is_active"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
        )

    access_token = create_access_token(user["id"], user["role"])
    new_refresh_token = create_refresh_token(user["id"])

    revoke_session_by_refresh(body.refresh_token)
    save_session(user["id"], access_token, new_refresh_token)

    return TokenResponse(
        access_token=access_token,
        refresh_token=new_refresh_token,
    )
```

## Endpoint /auth/me

```python
@router.get("/me")
async def get_me(user: dict = Depends(require_auth)) -> dict:
    db_user = get_user_by_id(user["sub"])
    return {
        "id": db_user["id"],
        "email": db_user["email"],
        "role": db_user["role"],
    }
```

## Configuração via Variáveis de Ambiente

```bash
# .env
JWT_SECRET_KEY=sua-chave-secreta-aqui-minimo-32-chars
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
JWT_REFRESH_TOKEN_EXPIRE_DAYS=7
```

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60
    jwt_refresh_token_expire_days: int = 7

    class Config:
        env_file = ".env"
```

## Segurança

- Use `SECRET_KEY` com pelo menos 32 caracteres aleatórios. Gere com: `python -c "import secrets; print(secrets.token_hex(32))"`
- Nunca exponha o `SECRET_KEY` em logs ou respostas da API
- Sempre valide o campo `type` para distinguir access de refresh tokens
- Implemente revogação via `jti` no PostgreSQL para logout seguro

## External Linking

| Conceito              | Recurso                      | Link                                                                                                                |
| --------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **JWT RFC 7519**      | JSON Web Token specification | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)                              |
| **PyJWT**             | Python JWT library           | [pyjwt.readthedocs.io](https://pyjwt.readthedocs.io/)                                                               |
| **HS256**             | HMAC with SHA-256            | [datatracker.ietf.org/doc/html/rfc7518#section-3.2](https://datatracker.ietf.org/doc/html/rfc7518#section-3.2)      |
| **FastAPI Security**  | OAuth2 + JWT with FastAPI    | [fastapi.tiangolo.com/tutorial/security/oauth2-jwt](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)     |
| **Pydantic Settings** | Environment configuration    | [docs.pydantic.dev/latest/concepts/pydantic_settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) |
