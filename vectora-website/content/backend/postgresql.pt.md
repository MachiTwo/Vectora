---
title: "PostgreSQL: Banco Relacional do Vectora"
slug: postgresql
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - auth
  - backend
  - database
  - pg8000
  - postgresql
  - rbac
  - sessions
  - storage
  - vectora
  - vcr
---

{{< lang-toggle >}}

{{< section-toggle >}}

PostgreSQL é o banco relacional principal do Vectora. Armazena usuários, tokens JWT, permissões RBAC, sessões e logs de decisão do VCR. Acesso via `pg8000` — driver Python puro sem dependência de libpq ou extensões C.

## Conexão

```python
import pg8000.native

def get_connection() -> pg8000.native.Connection:
    return pg8000.native.Connection(
        host="localhost",
        port=5432,
        database="vectora",
        user="vectora",
        password="sua-senha",
    )
```

Para produção, use um pool de conexões:

```python
from pg8000.dbapi import connect
from contextlib import contextmanager

_pool: list = []
MAX_POOL = 10

@contextmanager
def db_conn():
    conn = connect(
        host="localhost",
        database="vectora",
        user="vectora",
        password="sua-senha",
    )
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
```

## Schema

### Tabela: users

```sql
CREATE TABLE users (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email       TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role        TEXT NOT NULL DEFAULT 'viewer'
                CHECK (role IN ('viewer', 'developer', 'operator', 'admin', 'superadmin')),
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    is_active   BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE INDEX idx_users_email ON users (email);
```

### Tabela: sessions

```sql
CREATE TABLE sessions (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id         UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    access_token    TEXT UNIQUE NOT NULL,
    refresh_token   TEXT UNIQUE NOT NULL,
    expires_at      TIMESTAMPTZ NOT NULL,
    refresh_expires_at TIMESTAMPTZ NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    revoked         BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE INDEX idx_sessions_access_token ON sessions (access_token);
CREATE INDEX idx_sessions_user_id ON sessions (user_id);
```

### Tabela: vcr_logs

```sql
CREATE TABLE vcr_logs (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id      UUID REFERENCES sessions(id),
    query           TEXT NOT NULL,
    strategy_used   TEXT NOT NULL,
    faithfulness    FLOAT NOT NULL,
    latency_ms      FLOAT NOT NULL,
    top_k_returned  INT NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_vcr_logs_session ON vcr_logs (session_id);
CREATE INDEX idx_vcr_logs_created ON vcr_logs (created_at);
```

### Tabela: agent_runs

```sql
CREATE TABLE agent_runs (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id      UUID REFERENCES sessions(id),
    query           TEXT NOT NULL,
    result          TEXT,
    steps           JSONB NOT NULL DEFAULT '[]',
    iterations      INT NOT NULL DEFAULT 0,
    total_latency_ms FLOAT,
    status          TEXT NOT NULL DEFAULT 'running'
                    CHECK (status IN ('running', 'success', 'error', 'timeout')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    finished_at     TIMESTAMPTZ
);
```

## Operações CRUD

### Criar usuário

```python
import hashlib
import uuid

def create_user(email: str, password: str, role: str = "developer") -> dict:
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    with db_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO users (email, password_hash, role)
            VALUES (%s, %s, %s)
            RETURNING id, email, role, created_at
            """,
            (email, password_hash, role),
        )
        row = cursor.fetchone()
    return {"id": str(row[0]), "email": row[1], "role": row[2]}
```

### Buscar usuário por email

```python
def get_user_by_email(email: str) -> dict | None:
    with db_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, email, password_hash, role, is_active FROM users WHERE email = %s",
            (email,),
        )
        row = cursor.fetchone()
    if not row:
        return None
    return {
        "id": str(row[0]),
        "email": row[1],
        "password_hash": row[2],
        "role": row[3],
        "is_active": row[4],
    }
```

### Registrar log VCR

```python
def log_vcr_decision(
    session_id: str,
    query: str,
    strategy: str,
    faithfulness: float,
    latency_ms: float,
    top_k: int,
) -> None:
    with db_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO vcr_logs
                (session_id, query, strategy_used, faithfulness, latency_ms, top_k_returned)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (session_id, query, strategy, faithfulness, latency_ms, top_k),
        )
```

## Migrações

O Vectora usa migrações SQL versionadas em `vectora/db/migrations/`:

```text
migrations/
  001_create_users.sql
  002_create_sessions.sql
  003_create_vcr_logs.sql
  004_create_agent_runs.sql
```

Aplicar todas as migrações:

```bash
for f in vectora/db/migrations/*.sql; do
  psql -h localhost -U vectora -d vectora -f "$f"
done
```

## Setup via Docker

```yaml
# docker-compose.yml
services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: vectora
      POSTGRES_USER: vectora
      POSTGRES_PASSWORD: sua-senha
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U vectora"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

## External Linking

| Conceito               | Recurso                      | Link                                                                                          |
| ---------------------- | ---------------------------- | --------------------------------------------------------------------------------------------- |
| **PostgreSQL 16**      | Release notes e documentação | [postgresql.org/docs/16](https://www.postgresql.org/docs/16/)                                 |
| **pg8000**             | Python driver puro sem libpq | [github.com/tlocke/pg8000](https://github.com/tlocke/pg8000)                                  |
| **UUID v4**            | RFC 4122: UUID standard      | [datatracker.ietf.org/doc/html/rfc4122](https://datatracker.ietf.org/doc/html/rfc4122)        |
| **JSONB**              | PostgreSQL JSON binary type  | [postgresql.org/docs/16/datatype-json](https://www.postgresql.org/docs/16/datatype-json.html) |
| **Connection Pooling** | PgBouncer documentation      | [pgbouncer.org](https://www.pgbouncer.org/)                                                   |
