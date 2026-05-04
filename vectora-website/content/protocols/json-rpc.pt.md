---
title: "JSON-RPC 2.0: Protocolo de Integração Programática"
slug: json-rpc
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - json-rpc
  - protocol
  - integration
  - batch
  - editor-plugins
  - vectora
  - typescript
  - kotlin
---

{{< lang-toggle >}}

{{< section-toggle >}}

JSON-RPC 2.0 é o protocolo de integração programática do Vectora, exposto em `/rpc`. Ideal para editor plugins (TypeScript, Kotlin), batch queries e integrações que precisam de chamadas síncronas com controle de ID. Suporta requests individuais e batch em uma única requisição HTTP.

## Especificação Base

JSON-RPC 2.0 é um protocolo stateless de chamada remota que usa JSON como formato de transporte.

Estrutura de uma requisição:

```json
{
  "jsonrpc": "2.0",
  "method": "vectora.search",
  "params": {
    "query": "Como validar tokens JWT?",
    "top_k": 10
  },
  "id": 1
}
```

Estrutura de uma resposta de sucesso:

```json
{
  "jsonrpc": "2.0",
  "result": {
    "results": [...]
  },
  "id": 1
}
```

Estrutura de uma resposta de erro:

```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32602,
    "message": "Invalid params",
    "data": { "field": "query", "issue": "required" }
  },
  "id": 1
}
```

## Endpoint

```text
POST http://localhost:8000/rpc
Content-Type: application/json
Authorization: Bearer <token>
```

## Métodos Disponíveis

### vectora.search

Busca semântica no codebase:

```json
{
  "jsonrpc": "2.0",
  "method": "vectora.search",
  "params": {
    "query": "Como validar tokens JWT?",
    "top_k": 10,
    "strategy": "auto"
  },
  "id": 1
}
```

### vectora.agent.run

Executar agente completo:

```json
{
  "jsonrpc": "2.0",
  "method": "vectora.agent.run",
  "params": {
    "query": "Refatora validate_token para Pydantic v2",
    "max_iterations": 5
  },
  "id": 2
}
```

### vectora.index.add

Adicionar arquivos ao índice LanceDB:

```json
{
  "jsonrpc": "2.0",
  "method": "vectora.index.add",
  "params": {
    "paths": ["src/auth/jwt.py", "src/auth/guards.py"]
  },
  "id": 3
}
```

### vectora.vcr.validate

Validar query/resposta via VCR:

```json
{
  "jsonrpc": "2.0",
  "method": "vectora.vcr.validate",
  "params": {
    "type": "plan",
    "query": "Como validar JWT?",
    "context": "FastAPI project"
  },
  "id": 4
}
```

### vectora.health

Status dos componentes:

```json
{
  "jsonrpc": "2.0",
  "method": "vectora.health",
  "params": {},
  "id": 5
}
```

## Batch Requests

JSON-RPC 2.0 suporta múltiplas chamadas em um único POST:

```json
[
  {
    "jsonrpc": "2.0",
    "method": "vectora.search",
    "params": { "query": "validate JWT", "top_k": 5 },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "vectora.search",
    "params": { "query": "RBAC permissions", "top_k": 5 },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "vectora.health",
    "params": {},
    "id": 3
  }
]
```

Resposta batch (ordem pode variar):

```json
[
  { "jsonrpc": "2.0", "result": { "results": [...] }, "id": 1 },
  { "jsonrpc": "2.0", "result": { "results": [...] }, "id": 2 },
  { "jsonrpc": "2.0", "result": { "status": "healthy" }, "id": 3 }
]
```

## Códigos de Erro

| Código   | Mensagem         | Descrição                      |
| -------- | ---------------- | ------------------------------ |
| `-32700` | Parse error      | JSON inválido                  |
| `-32600` | Invalid Request  | Estrutura JSON-RPC inválida    |
| `-32601` | Method not found | Método não existe              |
| `-32602` | Invalid params   | Parâmetros incorretos          |
| `-32603` | Internal error   | Erro interno do servidor       |
| `-32001` | Auth required    | Token JWT ausente ou inválido  |
| `-32002` | Rate limit       | Limite de requisições atingido |

## Implementação em Editor Plugins

### TypeScript (VS Code Extension)

```typescript
// vectora-vscode/src/client.ts
async function jsonrpcCall<T>(method: string, params: Record<string, unknown>): Promise<T> {
  const response = await fetch("http://localhost:8000/rpc", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({
      jsonrpc: "2.0",
      method,
      params,
      id: Date.now(),
    }),
  });

  const data = await response.json();

  if (data.error) {
    throw new Error(`JSON-RPC Error ${data.error.code}: ${data.error.message}`);
  }

  return data.result as T;
}

// Uso
const results = await jsonrpcCall<SearchResult>("vectora.search", {
  query: "validate JWT token",
  top_k: 5,
});
```

### Kotlin (JetBrains Plugin)

```kotlin
// vectora-jetbrains/src/client/VectoraClient.kt
class VectoraClient(private val baseUrl: String, private val token: String) {

    suspend fun search(query: String, topK: Int = 10): SearchResult {
        return jsonrpcCall("vectora.search", mapOf(
            "query" to query,
            "top_k" to topK
        ))
    }

    private suspend inline fun <reified T> jsonrpcCall(
        method: String,
        params: Map<String, Any>
    ): T {
        val request = JsonRpcRequest(
            method = method,
            params = params,
            id = System.currentTimeMillis()
        )
        val response = httpClient.post("$baseUrl/rpc") {
            headers { append("Authorization", "Bearer $token") }
            setBody(Json.encodeToString(request))
        }
        val jsonRpcResponse = Json.decodeFromString<JsonRpcResponse<T>>(response.body())
        return jsonRpcResponse.result ?: throw VectoraException(jsonRpcResponse.error)
    }
}
```

### Python

```python
import requests

def jsonrpc_call(method: str, params: dict, token: str) -> dict:
    response = requests.post(
        "http://localhost:8000/rpc",
        headers={"Authorization": f"Bearer {token}"},
        json={"jsonrpc": "2.0", "method": method, "params": params, "id": 1},
    )
    data = response.json()
    if "error" in data:
        raise Exception(f"JSON-RPC Error {data['error']['code']}: {data['error']['message']}")
    return data["result"]

# Batch request
def jsonrpc_batch(calls: list[tuple[str, dict]], token: str) -> list[dict]:
    payload = [
        {"jsonrpc": "2.0", "method": method, "params": params, "id": i}
        for i, (method, params) in enumerate(calls)
    ]
    response = requests.post(
        "http://localhost:8000/rpc",
        headers={"Authorization": f"Bearer {token}"},
        json=payload,
    )
    return sorted(response.json(), key=lambda r: r["id"])
```

## External Linking

| Conceito         | Recurso                                  | Link                                                                                                             |
| ---------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **JSON-RPC 2.0** | Especificação oficial                    | [jsonrpc.org/specification](https://www.jsonrpc.org/specification)                                               |
| **FastAPI**      | Framework para implementação do endpoint | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)                                                            |
| **MCP**          | Alternativa para editor integration      | [modelcontextprotocol.io](https://modelcontextprotocol.io/)                                                      |
| **Fetch API**    | Web API para requisições HTTP            | [developer.mozilla.org/en-US/docs/Web/API/Fetch_API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) |
| **ktor**         | HTTP client para Kotlin/JetBrains        | [ktor.io/docs/client](https://ktor.io/docs/client-create-new-application.html)                                   |
