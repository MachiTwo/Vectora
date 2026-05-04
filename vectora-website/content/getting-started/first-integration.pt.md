---
title: "Primeira Integração com Vectora"
description: "Conectar Vectora via REST API, MCP e JSON-RPC em 5 minutos"
slug: "first-integration"
tags:
  - integration
  - rest-api
  - mcp
  - json-rpc
  - vscode
  - quickstart
  - fastapi
date: 2026-05-03
weight: 2.2
---

{{< lang-toggle >}}

{{< section-toggle >}}

Com Vectora rodando em `http://localhost:8000`, você pode integrar com seu editor ou aplicação via três protocolos: REST API (endpoints HTTP padrão), MCP (Model Context Protocol para editores de AI) e JSON-RPC 2.0 (para integrações programáticas). Este guia mostra os três em 5 minutos cada.

## Pré-requisito

Vectora deve estar rodando:

```bash
vectora serve
# http://localhost:8000 deve responder
curl http://localhost:8000/health
```

## Integração 1: REST API (HTTP)

A REST API é a forma mais direta de integrar com Vectora. Use para scripts, CI/CD e integrações customizadas.

### Busca Semântica

```bash
curl -X POST http://localhost:8000/api/v1/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Como validar tokens JWT?",
    "top_k": 5,
    "strategy": "semantic"
  }'
```

Resposta:

```json
{
  "results": [
    {
      "file": "src/auth/jwt.py",
      "lines": "1-45",
      "score": 0.94,
      "content": "def validate_token(token: str) -> dict:\n    ..."
    }
  ],
  "metadata": {
    "total_latency_ms": 258,
    "precision": 0.91
  }
}
```

### Executar Agente

```bash
curl -X POST http://localhost:8000/api/v1/agent/run \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Refatora a função validate_token para usar Pydantic v2",
    "context_strategy": "auto",
    "max_iterations": 5
  }'
```

### Autenticação

Para endpoints protegidos, use JWT Bearer token:

```bash
# Obter token
TOKEN=$(curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "dev", "password": "sua-senha"}' \
  | jq -r '.access_token')

# Usar token em chamadas
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/v1/agent/run ...
```

## Integração 2: MCP (Model Context Protocol)

MCP é usado para integrar Vectora com editores de AI (VS Code + Claude, JetBrains, Zed) e outros agentes.

### Configurar MCP no VS Code (Claude Code)

Adicione ao arquivo de configuração do Claude Code (`~/.claude/config.json`):

```json
{
  "mcp_servers": {
    "vectora": {
      "command": "vectora",
      "args": ["mcp", "--port", "8001"],
      "env": {
        "VECTORA_URL": "http://localhost:8000"
      }
    }
  }
}
```

Reinicie o VS Code. Vectora aparecerá como ferramenta disponível no Claude Code.

### Ferramentas MCP Disponíveis

| Ferramenta        | Descrição                       |
| ----------------- | ------------------------------- |
| `vectora_search`  | Busca semântica no codebase     |
| `vectora_agent`   | Executar agente com Deep Agents |
| `vectora_index`   | Indexar arquivos no LanceDB     |
| `vectora_context` | Buscar contexto estruturado     |
| `vectora_explain` | Explicar decisão do VCR         |

### Exemplo de Uso MCP

Após configurar, Claude Code pode usar Vectora diretamente:

```text
Você: Como o módulo de autenticação funciona neste projeto?

Claude: [chama vectora_search internamente]

Resultado: Encontrei 3 arquivos relevantes:
- src/auth/jwt.py — Validação de tokens JWT
- src/auth/rbac.py — Sistema de permissões RBAC
- src/middleware/auth.py — Middleware de autenticação FastAPI
```

## Integração 3: JSON-RPC 2.0

JSON-RPC 2.0 é usado para integrações programáticas com controle explícito de chamadas.

### Chamada Básica

```python
import requests

def jsonrpc_call(method: str, params: dict) -> dict:
    response = requests.post(
        "http://localhost:8000/rpc",
        json={
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
    )
    return response.json()["result"]

# Busca semântica
result = jsonrpc_call("vectora.search", {
    "query": "Como validar tokens JWT?",
    "top_k": 5
})

# Executar agente
result = jsonrpc_call("vectora.agent.run", {
    "query": "Refatora a função validate_token",
    "context_strategy": "auto"
})
```

### Métodos JSON-RPC Disponíveis

| Método                 | Descrição                    |
| ---------------------- | ---------------------------- |
| `vectora.search`       | Busca semântica              |
| `vectora.agent.run`    | Executar agente completo     |
| `vectora.index.add`    | Adicionar arquivos ao índice |
| `vectora.vcr.validate` | Validar decisão via VCR      |
| `vectora.health`       | Status dos componentes       |

### Batch Requests

JSON-RPC suporta múltiplas chamadas em uma só requisição:

```python
response = requests.post(
    "http://localhost:8000/rpc",
    json=[
        {"jsonrpc": "2.0", "method": "vectora.search", "params": {"query": "auth"}, "id": 1},
        {"jsonrpc": "2.0", "method": "vectora.search", "params": {"query": "jwt"}, "id": 2},
    ]
)
# Retorna lista de resultados
```

## Integração com VS Code (Extensão Vectora)

A extensão oficial de VS Code usa ACP (Agent Client Protocol) para comunicação em tempo real:

1. Instale a extensão "Vectora" no VS Code Marketplace
2. Configure: `Ctrl+Shift+P` → "Vectora: Connect" → `http://localhost:8000`
3. Use: `Ctrl+Shift+V` para abrir o painel Vectora

A extensão autentica automaticamente com JWT herdado do backend.

## External Linking

| Conceito               | Recurso                              | Link                                                                                   |
| ---------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **MCP**                | Model Context Protocol specification | [modelcontextprotocol.io/docs](https://modelcontextprotocol.io/docs)                   |
| **JSON-RPC 2.0**       | JSON-RPC 2.0 specification           | [jsonrpc.org/specification](https://www.jsonrpc.org/specification)                     |
| **FastAPI REST**       | FastAPI endpoint documentation       | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)                                  |
| **VS Code Extensions** | VS Code Extension Marketplace        | [marketplace.visualstudio.com](https://marketplace.visualstudio.com/)                  |
| **JWT**                | JSON Web Token standard RFC 7519     | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519) |
