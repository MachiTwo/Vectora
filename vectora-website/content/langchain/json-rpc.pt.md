---
title: "JSON-RPC para Comunicação Interna"
slug: "langchain/json-rpc"
description: "Protocolo JSON-RPC para chamadas entre componentes"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "json-rpc", "protocol", "rpc", "communication", "internal"]
---

{{< lang-toggle >}}

JSON-RPC é um **protocolo leve de chamada de funções remotas** baseado em JSON, usado para comunicação interna entre componentes de agentes.

## JSON-RPC vs MCP vs ACP

| Protocolo | Escopo | Caso de Uso |
|-----------|--------|-----------|
| **JSON-RPC** | Interno | Componente A ↔ Componente B |
| **MCP** | Integração | Agente → Ferramentas externas |
| **ACP** | Interface | Agente ↔ Editor |

**JSON-RPC:** "Chame minha função"  
**MCP:** "Use minha ferramenta"  
**ACP:** "Controle meu editor"

## Especificação Básica

### Request

```json
{
    "jsonrpc": "2.0",
    "method": "analyze_code",
    "params": {
        "code": "def hello(): print('world')",
        "language": "python"
    },
    "id": 1
}
```

### Response (Sucesso)

```json
{
    "jsonrpc": "2.0",
    "result": {
        "complexity": "low",
        "issues": []
    },
    "id": 1
}
```

### Response (Erro)

```json
{
    "jsonrpc": "2.0",
    "error": {
        "code": -32602,
        "message": "Invalid params",
        "data": "Missing required parameter: code"
    },
    "id": 1
}
```

## Implementação em Python

### Servidor JSON-RPC

```python
from jsonrpc import JsonRPC, dispatcher
from aiohttp import web

# Registrar métodos
@dispatcher.add_method
async def analyze_code(code: str, language: str):
    """Analisa código"""
    return {
        "complexity": calculate_complexity(code),
        "issues": find_issues(code, language)
    }

@dispatcher.add_method
async def format_code(code: str):
    """Formata código"""
    return format_with_black(code)

# Endpoint HTTP
async def jsonrpc_handler(request):
    request_data = await request.json()
    response = dispatcher.call(request_data)
    return web.json_response(response)

# Setup
app = web.Application()
app.router.add_post('/jsonrpc', jsonrpc_handler)
web.run_app(app)
```

### Cliente JSON-RPC

```python
import aiohttp
import json

class JSONRPCClient:
    def __init__(self, url: str):
        self.url = url
        self.id = 0
    
    async def call(self, method: str, params: dict):
        self.id += 1
        
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self.id
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=request) as resp:
                response = await resp.json()
        
        if "error" in response:
            raise Exception(response["error"]["message"])
        
        return response["result"]

# Uso
client = JSONRPCClient("http://localhost:8000/jsonrpc")
result = await client.call("analyze_code", {
    "code": "def hello(): pass",
    "language": "python"
})
```

## Padrão: Vectora com JSON-RPC

Vectora pode expor seu VCR e Search via JSON-RPC:

```python
# Servidor JSON-RPC do Vectora
@dispatcher.add_method
async def vectora_search(query: str, bucket: str, top_k: int = 5):
    """Busca no índice Vectora"""
    results = await vectora.search(query, bucket, top_k)
    return [
        {"content": r.content, "score": r.score}
        for r in results
    ]

@dispatcher.add_method
async def vectora_vcr_analyze(text: str):
    """Analisa com VCR (pre-thinking)"""
    analysis = await vectora.vcr.analyze(text)
    return {
        "intent": analysis.intent,
        "entities": analysis.entities,
        "confidence": analysis.confidence
    }

@dispatcher.add_method
async def vectora_rerank(query: str, documents: list):
    """Reranking local com Voyage"""
    scored = await vectora.reranker.rank(query, documents)
    return [
        {"doc": d, "score": s}
        for d, s in zip(documents, scored)
    ]
```

### Cliente LangChain usando Vectora JSON-RPC

```python
from langchain.tools import tool

# Ferramenta que chama Vectora via JSON-RPC
@tool
async def search_vectora(query: str, bucket: str = "knowledge"):
    """Busca na base de conhecimento Vectora"""
    
    client = JSONRPCClient("http://vectora-server:8000/jsonrpc")
    results = await client.call("vectora_search", {
        "query": query,
        "bucket": bucket,
        "top_k": 5
    })
    
    return "\n".join([r["content"] for r in results])

# Usar em agente
agent = create_agent(
    model="claude-3-opus",
    tools=[search_vectora]
)
```

## Métodos Comuns em Agentes

```python
@dispatcher.add_method
async def list_tools():
    """Lista ferramentas disponíveis"""
    return [...]

@dispatcher.add_method
async def call_tool(name: str, args: dict):
    """Executa ferramenta"""
    return {...}

@dispatcher.add_method
async def get_context(user_id: str):
    """Retorna contexto do usuário"""
    return {...}

@dispatcher.add_method
async def store_message(user_id: str, message: dict):
    """Salva mensagem"""
    return {"stored": True}

@dispatcher.add_method
async def get_history(user_id: str, limit: int = 10):
    """Retorna histórico de conversa"""
    return [...]
```

## Batch Requests

Chamar múltiplos métodos:

```python
# Request
[
    {"jsonrpc": "2.0", "method": "analyze_code", "params": {...}, "id": 1},
    {"jsonrpc": "2.0", "method": "format_code", "params": {...}, "id": 2},
    {"jsonrpc": "2.0", "method": "get_context", "params": {...}, "id": 3}
]

# Response
[
    {"jsonrpc": "2.0", "result": {...}, "id": 1},
    {"jsonrpc": "2.0", "result": {...}, "id": 2},
    {"jsonrpc": "2.0", "result": {...}, "id": 3}
]
```

## Notificações (Fire-and-forget)

Sem esperar resposta:

```json
{
    "jsonrpc": "2.0",
    "method": "log_event",
    "params": {
        "event": "user_action",
        "timestamp": "2026-05-03T10:00:00Z"
    }
}
```

Note: **sem `id`** - não há resposta

## External Linking

| Conceito | Recurso | Link |
|----------|---------|------|
| JSON-RPC Spec | Official Spec | [https://www.jsonrpc.org/](https://www.jsonrpc.org/) |
| JSON-RPC 2.0 | Version 2.0 Spec | [https://www.jsonrpc.org/specification](https://www.jsonrpc.org/specification) |
| Python Library | python-jsonrpc | [https://github.com/pavlov99/json-rpc](https://github.com/pavlov99/json-rpc) |
| FastAPI Integration | Starlette JSON-RPC | [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/) |
| WebSocket Support | Async JSON-RPC | [https://websockets.readthedocs.io/](https://websockets.readthedocs.io/) |
