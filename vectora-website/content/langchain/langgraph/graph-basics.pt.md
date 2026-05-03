---
title: "Basics de Grafos no LangGraph"
slug: "langchain/langgraph/graph-basics"
description: "Nodes, edges, state e construção de grafos"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langgraph", "graphs", "nodes", "edges", "state"]
---

{{< lang-toggle >}}

Um grafo em LangGraph é composto de nós (nodes) conectados por arestas (edges), com estado fluindo entre eles.

## Estrutura Básica

```python
from langgraph.graph import StateGraph
from typing import TypedDict

# Define o estado
class State(TypedDict):
    messages: list[str]
    current_agent: str

# Cria o grafo
graph = StateGraph(State)

# Adiciona nós
graph.add_node("agent", agent_fn)
graph.add_node("tools", tools_fn)
graph.add_node("output", output_fn)

# Adiciona arestas
graph.add_edge("agent", "tools")
graph.add_edge("tools", "output")

# Define entrada/saída
graph.set_entry_point("agent")
graph.set_finish_point("output")

# Compila
app = graph.compile()
```

## Tipos de Nodes

### Processing Node

Processa estado e retorna novo estado:

```python
def process(state: State) -> State:
    return {"new_field": "value"}
```

### Conditional Node

Define branches no fluxo:

```python
def router(state: State) -> str:
    if condition:
        return "node_a"
    return "node_b"
```

## Tipos de Edges

### Direct Edge

```python
graph.add_edge("node_a", "node_b")
```

### Conditional Edge

```python
graph.add_conditional_edges("node_a", router_fn)
```

## External Linking

| Conceito           | Recurso                 | Link                                                                                                                         |
| ------------------ | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| LangGraph Docs     | LangGraph Documentation | [https://docs.langchain.com/oss/python/langgraph/](https://docs.langchain.com/oss/python/langgraph/)                         |
| Graph Construction | Building Graphs Guide   | [https://docs.langchain.com/oss/python/langgraph/how-tos/](https://docs.langchain.com/oss/python/langgraph/how-tos/)         |
| State Management   | Managing State          | [https://reference.langchain.com/python/langgraph](https://reference.langchain.com/python/langgraph)                         |
| GitHub Examples    | LangGraph Examples      | [https://github.com/langchain-ai/langgraph/tree/main/examples](https://github.com/langchain-ai/langgraph/tree/main/examples) |
| Python SDK         | LangGraph Python        | [https://pypi.org/project/langgraph/](https://pypi.org/project/langgraph/)                                                   |
