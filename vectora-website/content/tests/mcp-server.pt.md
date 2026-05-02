---
title: "Suite de Testes: Servidor MCP"
slug: mcp-server-tests
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - compliance
  - concepts
  - errors
  - json-rpc
  - mcp
  - protocol
  - testing
  - tools
  - vectora
---

{{< lang-toggle >}}

O servidor MCP deve ser robusto, rápido, confiável e 100% conforme à especificação JSON-RPC 2.0. Ele deve suportar requisições concorrentes, grandes payloads e recuperação graciosa de erros. Esta suite valida a implementação completa do Model Context Protocol no Vectora.

Ao verificar a conformidade com o protocolo, garantimos que o Vectora se integre perfeitamente com uma ampla gama de agentes e ferramentas externas.

**Cobertura**: 80+ testes | **Prioridade**: ALTA

## Segmentos de Testes

As seções a seguir detalham os casos de teste específicos e os cenários cobertos por esta suite.

### 1. Conformidade JSON-RPC 2.0 (20 testes)

Garante que o servidor adira estritamente ao padrão JSON-RPC 2.0 em toda a comunicação.

- **Formato de Requisição Válido**: Confirma que requisições formatadas corretamente são processadas e respondidas com IDs correspondentes.
- **Rejeição de Requisição Inválida**: Verifica se requisições malformadas são rejeitadas com os códigos de erro corretos (-32600).
- **Tratamento de Notificações**: Garante que requisições sem ID sejam processadas corretamente sem gerar uma resposta.
- **Requisições em Lote (Batch)**: Valida que múltiplas requisições em um único payload sejam processadas e retornadas em um array.

### 2. Operações de Ferramentas (25 testes)

Valida a funcionalidade principal de expor e invocar ferramentas através da interface MCP.

- **Descoberta de Ferramentas**: Confirma que `tools/list` retorna os schemas, descrições e conjuntos de parâmetros corretos para todas as ferramentas.
- **Invocação de Ferramenta**: Verifica se `tools/call` aciona a lógica pretendida e retorna resultados no formato especificado.
- **Validação de Parâmetros**: Garante que tipos de parâmetros incorretos ou parâmetros obrigatórios ausentes acionem erros de validação.

### 3. Performance & Concorrência (15 testes)

Monitora a responsividade e estabilidade do servidor sob várias condições de carga.

- **Resposta de Baixa Latência**: Alvo de tempo médio de resposta inferior a 100ms para requisições simples.
- **Requisições Concorrentes**: Valida que o servidor possa lidar com 10+ requisições simultâneas sem degradação de performance.
- **Tratamento de Payloads Grandes**: Garante que payloads JSON grandes (até 10MB) sejam processados corretamente sem vazamentos de memória.

### 4. Confiabilidade & Resiliência (20 testes)

Testa a habilidade do servidor em manter as operações e se recuperar de condições inesperadas.

- **Resiliência de Conexão**: Verifica se o servidor detecta problemas intermitentes de rede e permite a reconexão.
- **Recuperação de Erros**: Garante que uma falha em uma única chamada de ferramenta não derrube todo o processo do servidor.
- **Degradação Graciosa**: Confirma que, se uma ferramenta ficar indisponível, as outras continuem funcionando corretamente.

## SLAs de Performance

A tabela a seguir resume as metas de performance para o servidor MCP.

| Métrica                      | Alvo    |
| :--------------------------- | :------ |
| **Latência p50**             | < 50ms  |
| **Latência p95**             | < 200ms |
| **Latência p99**             | < 500ms |
| **Requisições Concorrentes** | 100+    |
| **Taxa de Sucesso**          | 99.9%   |

## Guia de Execução

Para rodar os testes de conformidade e performance do servidor MCP, utilize os seguintes comandos:

```bash
# Rodar todos os testes MCP
go test -v ./tests/mcp-server/...

# Rodar especificamente conformidade JSON-RPC
go test -v -run JSONRPCCompliance ./tests/mcp-server/...

# Rodar com detecção de race condition
go test -v -race ./tests/mcp-server/...
```

## External Linking

| Concept        | Resource                             | Link                                                                                   |
| -------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **MCP**        | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK** | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **JSON-RPC**   | JSON-RPC 2.0 Specification           | [www.jsonrpc.org/specification](https://www.jsonrpc.org/specification)                 |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
