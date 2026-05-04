---
title: "REST API: Endpoints FastAPI do Vectora"
slug: rest-api
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - rest-api
  - fastapi
  - endpoints
  - http
  - jwt
  - authentication
  - vectora
  - openapi
---

{{< lang-toggle >}}

{{< section-toggle >}}

A REST API é o protocolo principal do Vectora, exposta via FastAPI em `http://localhost:8000`. Todos os endpoints seguem HTTP padrão com JSON request/response e autenticação JWT Bearer. A documentação interativa está disponível em `/docs` (Swagger UI).

## Base URL e Autenticação

```text
Base URL: http://localhost:8000

Autenticação: Bearer JWT
  Authorization: Bearer <token>

Documentação: http://localhost:8000/docs
```

### Obter Token JWT

```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "user@example.com", "password": "sua-senha"}'

# Resposta:
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIs...",
#   "token_type": "bearer",
#   "expires_in": 3600
# }
```

## Endpoints de Sistema

### Health Check

```http
GET /health
```

Resposta:

```json
{
  "status": "healthy",
  "components": {
    "vcr": { "status": "running", "latency_ms": 7.4 },
    "lancedb": { "status": "running", "indices": 1 },
    "postgres": { "status": "connected" },
    "redis": { "status": "connected" }
  },
  "version": "0.1.0"
}
```

### Ready Check

```http
GET /ready
```

Retorna `200 OK` quando todos os componentes estão prontos, `503` caso contrário.

## Endpoints de Busca

### Busca Semântica

```http
POST /api/v1/search
Authorization: Bearer <token>
Content-Type: application/json
```

Body:

```json
{
  "query": "Como validar tokens JWT?",
  "top_k": 10,
  "strategy": "auto",
  "filters": {
    "language": "python",
    "namespace": "src/auth"
  }
}
```

Resposta:

```json
{
  "results": [
    {
      "id": "src/auth/jwt.py:1-45",
      "file": "src/auth/jwt.py",
      "lines": "1-45",
      "score": 0.94,
      "content": "def validate_token(token: str) -> dict:\n    ..."
    }
  ],
  "metadata": {
    "total_searched": 10000,
    "total_latency_ms": 258,
    "strategy_used": "semantic",
    "precision": 0.91
  }
}
```

### Indexar Codebase

```http
POST /api/v1/search/index
Authorization: Bearer <token>
Content-Type: application/json
```

Body:

```json
{
  "paths": ["src/", "tests/"],
  "exclude": ["node_modules/", "*.pyc"],
  "language": "python"
}
```

## Endpoints de Agente

### Executar Agente

```http
POST /api/v1/agent/run
Authorization: Bearer <token>
Content-Type: application/json
```

Body:

```json
{
  "query": "Refatora a função validate_token para usar Pydantic v2",
  "context_strategy": "auto",
  "max_iterations": 5,
  "session_id": "sess_abc123"
}
```

Resposta:

```json
{
  "result": "A função foi refatorada com sucesso...",
  "steps": [
    {
      "tool": "search_codebase",
      "input": "validate_token function",
      "output": "def validate_token..."
    }
  ],
  "metadata": {
    "iterations": 3,
    "total_latency_ms": 1240,
    "vcr_validation": {
      "faithfulness": 0.91,
      "hallucination_risk": 0.05
    }
  }
}
```

### Streaming do Agente (SSE)

```http
POST /api/v1/agent/run/stream
Authorization: Bearer <token>
Content-Type: application/json
```

Resposta via Server-Sent Events:

```text
data: {"type": "thinking", "content": "Analisando o codebase..."}

data: {"type": "tool_call", "tool": "search_codebase", "input": "validate_token"}

data: {"type": "tool_result", "output": "def validate_token..."}

data: {"type": "response", "content": "A refatoração foi concluída..."}

data: {"type": "done", "metadata": {...}}
```

## Endpoints do VCR

### Validar Plano

```http
POST /vcr/validate-plan
Authorization: Bearer <token>
```

Body:

```json
{
  "query": "Como validar tokens JWT?",
  "context": "Projeto FastAPI com PostgreSQL"
}
```

### Scoring de Relevância

```http
POST /vcr/score-relevance
Authorization: Bearer <token>
```

Body:

```json
{
  "query": "validate JWT token",
  "candidates": [
    { "id": "1", "content": "def validate_token..." },
    { "id": "2", "content": "def create_token..." }
  ]
}
```

### Métricas (Prometheus)

```http
GET /vcr/metrics
```

Retorna métricas no formato Prometheus.

## Endpoints de Autenticação

### Login

```http
POST /auth/login
```

### Refresh Token

```http
POST /auth/refresh
Authorization: Bearer <refresh_token>
```

### Perfil do Usuário

```http
GET /auth/me
Authorization: Bearer <token>
```

## Códigos de Erro HTTP

| Código | Descrição                                    |
| ------ | -------------------------------------------- |
| `200`  | Sucesso                                      |
| `400`  | Request inválido (validação Pydantic falhou) |
| `401`  | Token ausente ou inválido                    |
| `403`  | Sem permissão (RBAC)                         |
| `404`  | Recurso não encontrado                       |
| `429`  | Rate limit atingido                          |
| `500`  | Erro interno do servidor                     |
| `503`  | Serviço indisponível (componente down)       |

## SDKs e Clientes

### Python

```python
import httpx

client = httpx.AsyncClient(
    base_url="http://localhost:8000",
    headers={"Authorization": f"Bearer {token}"},
)

result = await client.post("/api/v1/search", json={"query": "validate JWT"})
```

### CLI

```bash
# Busca via CLI
vectora search "Como validar tokens JWT?"

# Executar agente via CLI
vectora agent run "Refatora a função validate_token"
```

## External Linking

| Conceito         | Recurso                             | Link                                                                                                                     |
| ---------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **FastAPI**      | Framework web Python para REST APIs | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)                                                                    |
| **Pydantic v2**  | Validação de dados para FastAPI     | [docs.pydantic.dev](https://docs.pydantic.dev/)                                                                          |
| **JWT RFC 7519** | JSON Web Token standard             | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)                                   |
| **OpenAPI 3.0**  | API specification                   | [swagger.io/specification](https://swagger.io/specification/)                                                            |
| **SSE**          | Server-Sent Events specification    | [html.spec.whatwg.org/multipage/server-sent-events.html](https://html.spec.whatwg.org/multipage/server-sent-events.html) |
