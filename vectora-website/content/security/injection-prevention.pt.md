---
title: "Prevenção de Injeção: Segurança de Input"
slug: injection-prevention
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - fastapi
  - injection
  - pydantic
  - postgresql
  - security
  - sql-injection
  - vectora
---

{{< lang-toggle >}}

{{< section-toggle >}}

O Vectora previne injeção em três camadas: validação Pydantic no boundary da API (bloqueia inputs malformados antes de qualquer lógica), queries PostgreSQL parametrizadas (elimina SQL injection), e sanitização de paths antes de qualquer operação de arquivo.

## Camada 1: Validação Pydantic

Todo input da API é validado por modelos Pydantic antes de atingir qualquer handler. Campos inválidos retornam HTTP 422 imediatamente.

```python
from pydantic import BaseModel, Field, field_validator
import re

class SearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=1000)
    top_k: int = Field(default=10, ge=1, le=100)
    strategy: str = Field(
        default="auto",
        pattern="^(auto|semantic|structural|hybrid)$",
    )
    filters: dict | None = None

    @field_validator("query")
    @classmethod
    def sanitize_query(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Query não pode ser vazia")
        return v

class IndexRequest(BaseModel):
    paths: list[str] = Field(min_length=1, max_length=50)
    exclude: list[str] = Field(default_factory=list, max_length=100)
    language: str | None = Field(default=None, pattern="^[a-z]+$")

    @field_validator("paths", "exclude", mode="before")
    @classmethod
    def validate_paths(cls, paths: list[str]) -> list[str]:
        for path in paths:
            if ".." in path or path.startswith("/"):
                raise ValueError(f"Path inválido: {path}")
        return paths
```

Pydantic rejeita automaticamente tipos errados, strings além do limite e valores fora do padrão regex.

## Camada 2: SQL Parametrizado

Todas as queries PostgreSQL usam placeholders parametrizados — nunca concatenação de string. O pg8000 passa os parâmetros separadamente do SQL, tornando SQL injection estruturalmente impossível.

```python
# CORRETO: parametrizado
def get_user_by_email(email: str) -> dict | None:
    cursor.execute(
        "SELECT id, email, role FROM users WHERE email = %s",
        (email,),
    )

# CORRETO: múltiplos parâmetros
def log_vcr_decision(session_id, query, strategy, faithfulness, latency_ms):
    cursor.execute(
        """
        INSERT INTO vcr_logs (session_id, query, strategy_used, faithfulness, latency_ms)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (session_id, query, strategy, faithfulness, latency_ms),
    )

# ERRADO: concatenação (nunca fazer)
# cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
```

## Camada 3: Sanitização de Paths de Arquivo

Antes de qualquer operação de indexação, caminhos de arquivo são validados para prevenir path traversal.

```python
import os
from pathlib import Path

ALLOWED_BASE = Path("/workspace").resolve()

def safe_path(user_provided: str) -> Path:
    requested = (ALLOWED_BASE / user_provided).resolve()
    if not str(requested).startswith(str(ALLOWED_BASE)):
        raise ValueError(f"Path traversal detectado: {user_provided}")
    return requested

def index_path(user_path: str) -> None:
    safe = safe_path(user_path)
    if not safe.exists():
        raise FileNotFoundError(f"Path não encontrado: {safe}")
    # proceder com indexação
```

## Camada 4: Sanitização de Queries para LanceDB

Filtros passados para LanceDB são validados antes de uso. O LanceDB usa SQL-like syntax para `.where()` — inputs não sanitizados poderiam quebrar a query.

```python
ALLOWED_FILTER_FIELDS = {"file", "language", "start_line", "end_line"}
ALLOWED_OPERATORS = {"=", "LIKE", ">", "<", ">=", "<="}

def build_safe_filter(field: str, operator: str, value: str) -> str:
    if field not in ALLOWED_FILTER_FIELDS:
        raise ValueError(f"Campo de filtro inválido: {field}")
    if operator not in ALLOWED_OPERATORS:
        raise ValueError(f"Operador inválido: {operator}")

    # Sanitiza o valor: remove aspas simples
    safe_value = value.replace("'", "''")
    return f"{field} {operator} '{safe_value}'"
```

## Limitação de Tamanho de Input

Rate limiting e limites de tamanho previnem ataques de DoS via inputs gigantes:

```python
@app.post("/api/v1/search")
async def search(
    request: Request,
    body: SearchRequest,
    user: dict = Depends(require_auth),
) -> SearchResponse:
    content_length = request.headers.get("content-length", "0")
    if int(content_length) > 10_000:
        raise HTTPException(status_code=413, detail="Request body muito grande")
    ...
```

O FastAPI também tem `max_upload_size` configurável via middleware para uploads de arquivos.

## Testes de Segurança

```python
# tests/security/test_injection.py
import pytest

@pytest.mark.integration
async def test_sql_injection_in_login():
    result = await login("' OR '1'='1", "password")
    assert result is None

@pytest.mark.unit
def test_path_traversal_rejected():
    with pytest.raises(ValueError, match="Path traversal"):
        safe_path("../../etc/passwd")

@pytest.mark.unit
def test_query_length_limit():
    long_query = "a" * 1001
    with pytest.raises(ValidationError):
        SearchRequest(query=long_query)
```

## External Linking

| Conceito                | Recurso                        | Link                                                                                                     |
| ----------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **OWASP Injection**     | Injection attack prevention    | [owasp.org/www-community/Injection_Flaws](https://owasp.org/www-community/Injection_Flaws)               |
| **SQL Injection**       | OWASP SQL Injection            | [owasp.org/www-community/attacks/SQL_Injection](https://owasp.org/www-community/attacks/SQL_Injection)   |
| **Path Traversal**      | Path traversal attack          | [owasp.org/www-community/attacks/Path_Traversal](https://owasp.org/www-community/attacks/Path_Traversal) |
| **Pydantic Validation** | Input validation with Pydantic | [docs.pydantic.dev/latest/concepts/validators](https://docs.pydantic.dev/latest/concepts/validators/)    |
