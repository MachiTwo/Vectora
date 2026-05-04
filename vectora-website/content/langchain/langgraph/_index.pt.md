---
title: "LangGraph: Orquestração de Agentes Stateful"
slug: "langchain/langgraph"
description: "Framework para construir agentes com estado e decision loops"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langgraph", "agents", "stateful", "graphs", "orchestration"]
---

{{< lang-toggle >}}

LangGraph é um biblioteca que permite construir agentes complexos e stateful como grafos. Cada nó é um passo, cada aresta é uma transição, e o estado flui através do grafo.

## Por que LangGraph?

LangChain fornece abstrações de alto nível, mas às vezes você precisa de controle fino sobre:

- Flow de controle (loops, condicionalismo)
- Persistência de estado entre steps
- Human-in-the-loop
- Retry e error recovery

LangGraph fornece essas garantias através do modelo de grafos.

## Conceitos Principais

### Nodes

Cada nó é uma função que recebe o estado atual e retorna um novo estado:

```python
def node_a(state):
    # Processar estado
    return {"new_key": "new_value"}
```

### Edges

Conexões entre nós. Podem ser:

- **Determinísticas** - Sempre vai para o próximo nó
- **Condicionais** - Branch baseado no estado

### State

O estado é um dicionário compartilhado que flui através do grafo:

```python
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    messages: list
    next: str
```

## Arquitetura de um Agente

```
[Input]
   ↓
[LLM Node] (agent reasoning)
   ↓
[Tool Executor] (conditional)
   ↓
[Output Node] (format response)
   ↓
[Output]
```

## Vantagens

✅ **Stateful** - Mantém estado entre steps  
✅ **Durable** - Pode pausar/resumir execução  
✅ **Human-in-the-loop** - Suporta aprovação humana  
✅ **Streaming** - Respostas em tempo real  
✅ **LangSmith integration** - Debugging nativo

## Comparação com Deep Agents

| Aspecto            | LangGraph                           | Deep Agents                          |
| ------------------ | ----------------------------------- | ------------------------------------ |
| **Modelo**         | Graph-based (nós + edges)           | Planning-based (intents + execution) |
| **Controle**       | Explicito (você constrói o grafo)   | Implícito (agente planeja)           |
| **Persistência**   | Threads + Checkpoints               | Filesystem backend                   |
| **Interface**      | Code-first (Python)                 | CLI + TUI interactive                |
| **Editor**         | Via ACP (integração)                | ACP nativo no TUI                    |
| **Use case**       | Workflows estruturados, multi-agent | Explorativo, autonomous agents       |
| **Latência**       | Baixa (direto)                      | Média (planning overhead)            |
| **Learning curve** | Média (programação)                 | Baixa (TUI intuitivo)                |

**Quando usar LangGraph:**

- ✅ Workflows bem-definidos
- ✅ Controle fino necessário
- ✅ Multi-agent coordination
- ✅ Human-in-the-loop estruturado
- ✅ Integração com ferramentas específicas

**Quando usar Deep Agents:**

- ✅ Agentes autônomos exploradores
- ✅ Interatividade TUI importante
- ✅ Rapid prototyping
- ✅ Editor integration (ACP)
- ✅ Aprendizado contínuo do agente

## External Linking

| Conceito       | Recurso                | Link                                                                                                           |
| -------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------- |
| LangGraph Home | LangGraph Official     | [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)                                     |
| LangGraph Docs | Official Documentation | [https://docs.langchain.com/oss/python/langgraph/](https://docs.langchain.com/oss/python/langgraph/)           |
| API Reference  | LangGraph API          | [https://reference.langchain.com/python/langgraph](https://reference.langchain.com/python/langgraph)           |
| GitHub         | LangGraph Repository   | [https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)                         |
| Blog           | LangGraph Release      | [https://blog.langchain.com/langchain-langgraph-1dot0/](https://blog.langchain.com/langchain-langgraph-1dot0/) |
