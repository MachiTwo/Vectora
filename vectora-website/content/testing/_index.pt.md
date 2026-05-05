---
title: "Testing: Estratégia de Testes do Vectora"
slug: testing
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - e2e
  - performance
  - pytest
  - quality
  - testing
  - vectora
draft: false
---

{{< lang-toggle >}}

{{< section-toggle >}}

O Vectora usa pytest como framework principal, com três camadas de testes: unitários (componentes isolados), de integração (banco de dados real, sem mocks) e E2E (pipeline completo via API). Testes de integração obrigatoriamente usam PostgreSQL e Redis reais — não mocks.

## Estrutura de Testes

```text
tests/
  unit/
    test_vcr.py           # VCR: validate_plan, score_relevance
    test_jwt.py           # Token generation e validation
    test_rbac.py          # Permission checking
    test_chunker.py       # Code chunking logic
  integration/
    test_search.py        # Pipeline completo: embed -> HNSW -> rerank
    test_agent.py         # Agent execution com LanceDB real
    test_auth.py          # Login, refresh, revogação
  e2e/
    test_api_search.py    # REST API endpoints via httpx
    test_api_agent.py     # Agent + streaming SSE
  performance/
    test_search_latency.py # < 500ms p95
    test_rerank_latency.py # < 10ms p99
  conftest.py             # Fixtures compartilhadas
```

## Configuração do pytest

```ini
# pytest.ini
[pytest]
testpaths = tests
asyncio_mode = auto
markers =
    unit: Testes unitários (rápidos, sem infra)
    integration: Testes de integração (requerem PostgreSQL + Redis)
    e2e: Testes end-to-end (requerem servidor rodando)
    slow: Testes lentos (performance, carga)
```

## Fixtures Principais

```python
# tests/conftest.py
import pytest
import pg8000.native
import redis

@pytest.fixture(scope="session")
def pg_conn():
    conn = pg8000.native.Connection(
        host="localhost",
        database="vectora_test",
        user="vectora",
        password="test-password",
    )
    yield conn
    conn.close()

@pytest.fixture(scope="session")
def redis_client():
    r = redis.Redis(host="localhost", port=6379, db=1)
    yield r
    r.flushdb()

@pytest.fixture
def test_user(pg_conn):
    user = create_user(
        email="test@vectora.dev",
        password="test-password-123",
        role="developer",
    )
    yield user
    delete_user(user["id"])

@pytest.fixture
def auth_token(test_user):
    return create_access_token(test_user["id"], test_user["role"])
```

## Testes Unitários

```python
# tests/unit/test_vcr.py
import pytest
from vectora.vcr import LocalReranker

@pytest.mark.unit
def test_reranker_returns_top_k():
    reranker = LocalReranker(model_path="models/vcr_reranker_int8.pt")
    candidates = [
        {"content": "def validate_token(token: str) -> dict: ..."},
        {"content": "def create_user(email: str) -> User: ..."},
        {"content": "def validate_email(email: str) -> bool: ..."},
    ]
    results = reranker.rerank("validate JWT token", candidates, top_k=2)
    assert len(results) == 2
    assert results[0]["rerank_score"] >= results[1]["rerank_score"]

@pytest.mark.unit
def test_jwt_payload_contains_required_fields():
    from vectora.auth import create_access_token
    token = create_access_token("user-123", "developer")
    payload = decode_token(token)
    assert "sub" in payload
    assert "role" in payload
    assert "jti" in payload
    assert payload["type"] == "access"
```

## Testes de Integração

Testes de integração rodam contra banco real. Sem mocks de PostgreSQL, Redis ou LanceDB.

```python
# tests/integration/test_search.py
import pytest

@pytest.mark.integration
async def test_search_pipeline_returns_results(auth_token):
    pipeline = SearchPipeline()
    results = await pipeline.search(
        query="Como validar tokens JWT?",
        top_k=10,
    )
    assert len(results) > 0
    assert all("file" in r for r in results)
    assert all("rerank_score" in r for r in results)
    assert results[0]["rerank_score"] >= results[-1]["rerank_score"]

@pytest.mark.integration
async def test_embedding_cache_hit(redis_client):
    query = "test embedding cache"
    embed_with_cache([query])
    key = f"embed:{hashlib.sha256(query.encode()).hexdigest()}"
    assert redis_client.exists(key)
    second_call_result = embed_with_cache([query])
    assert second_call_result is not None
```

## Testes E2E

```python
# tests/e2e/test_api_search.py
import pytest
import httpx

BASE_URL = "http://localhost:8000"

@pytest.mark.e2e
async def test_search_endpoint_requires_auth():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/api/v1/search",
            json={"query": "jwt validation"},
        )
    assert response.status_code == 401

@pytest.mark.e2e
async def test_search_endpoint_returns_results(auth_token):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/api/v1/search",
            json={"query": "Como validar tokens JWT?", "top_k": 5},
            headers={"Authorization": f"Bearer {auth_token}"},
        )
    assert response.status_code == 200
    data = response.json()
    assert len(data["results"]) > 0
    assert data["metadata"]["total_latency_ms"] < 500
```

## Testes de Performance

```python
# tests/performance/test_search_latency.py
import pytest
import time

@pytest.mark.slow
async def test_search_p95_under_500ms(auth_token):
    pipeline = SearchPipeline()
    latencies = []

    for _ in range(100):
        start = time.monotonic()
        await pipeline.search("jwt validation", top_k=10)
        latencies.append((time.monotonic() - start) * 1000)

    latencies.sort()
    p95 = latencies[int(len(latencies) * 0.95)]
    assert p95 < 500, f"P95 latência: {p95:.1f}ms (target: 500ms)"

@pytest.mark.slow
async def test_reranker_p99_under_10ms():
    reranker = LocalReranker(model_path="models/vcr_reranker_int8.pt")
    candidates = [{"content": f"code snippet {i}"} for i in range(100)]
    latencies = []

    for _ in range(50):
        start = time.monotonic()
        reranker.rerank("query", candidates, top_k=10)
        latencies.append((time.monotonic() - start) * 1000)

    latencies.sort()
    p99 = latencies[int(len(latencies) * 0.99)]
    assert p99 < 10, f"P99 latência: {p99:.1f}ms (target: 10ms)"
```

## Executar Testes

```bash
# Unitários (rápido, sem infra)
uv run pytest tests/unit/ -v

# Integração (requer PostgreSQL + Redis)
uv run pytest tests/integration/ -v --tb=short

# E2E (requer servidor rodando)
uv run pytest tests/e2e/ -v

# Performance (lento)
uv run pytest tests/performance/ -v -m slow

# Todos
uv run pytest tests/ -v --tb=short

# Com cobertura
uv run pytest tests/unit/ tests/integration/ --cov=vectora --cov-report=term-missing
```

## External Linking

| Conceito           | Recurso                       | Link                                                                    |
| ------------------ | ----------------------------- | ----------------------------------------------------------------------- |
| **pytest**         | pytest documentation          | [docs.pytest.org](https://docs.pytest.org/)                             |
| **pytest-asyncio** | Async test support            | [pytest-asyncio.readthedocs.io](https://pytest-asyncio.readthedocs.io/) |
| **httpx**          | Async HTTP client for testing | [www.python-httpx.org](https://www.python-httpx.org/)                   |
| **pytest-cov**     | Coverage plugin               | [pytest-cov.readthedocs.io](https://pytest-cov.readthedocs.io/)         |
