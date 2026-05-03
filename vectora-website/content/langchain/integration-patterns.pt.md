---
title: "Padrões de Integração com LangChain"
slug: "langchain/integration-patterns"
description: "Padrões de integração com VCR, routing multi-LLM e composição de tools"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "patterns", "integration", "vcr", "routing", "composition"]
---

{{< lang-toggle >}}

LangChain permite integração avançada com sistemas Vectora através de padrões bem estabelecidos para routing, composição de tools e orquestração com a camada VCR.

## Padrão: Routing Multi-LLM

Selecionar o melhor LLM para cada tarefa:

```python
from langchain.runnables import RunnableBranch

def route_by_complexity(input_data):
    if input_data["complexity"] > 0.7:
        return "claude-opus"
    return "claude-haiku"

router = RunnableBranch(
    (lambda x: x["complexity"] > 0.7, claude_opus),
    (lambda x: x["complexity"] <= 0.7, claude_haiku),
)
```

## Padrão: VCR Pre-thinking

Usar VCR para otimizar a query antes do agente principal:

```python
# Query → VCR Analysis → Tool Selection → LLM
chain = (
    user_input
    | vcr_analyzer  # Análise contextual
    | tool_selector  # Seleção de ferramentas
    | llm.with_tools(tools)  # LLM com ferramentas
    | output_parser
)
```

## Padrão: Tool Composition

Composição fluente de tools e chains:

```python
from langchain.tools import Tool

search_tool = Tool.from_function(search_fn)
calculate_tool = Tool.from_function(calc_fn)
format_tool = Tool.from_function(format_fn)

# Encadear: Buscar → Calcular → Formatar
chain = search_tool | calculate_tool | format_tool
```

## Padrão: Conditional Chain Execution

Executar diferentes chains baseado em contexto:

```python
def should_use_rag(state):
    return state.get("use_rag", False)

rag_chain = retriever | llm
direct_chain = llm

conditional = RunnableBranch(
    (should_use_rag, rag_chain),
    direct_chain
)
```

## External Linking

| Conceito           | Recurso            | Link                                                                                                             |
| ------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------- |
| LangChain Patterns | Pattern Guide      | [https://docs.langchain.com/oss/python/langchain/](https://docs.langchain.com/oss/python/langchain/)             |
| VCR Integration    | Pre-thinking Layer | [https://github.com/vectora/vectora/docs/vcr](https://github.com/vectora/vectora/docs/vcr)                       |
| Tool Composition   | Complex Tools      | [https://docs.langchain.com/oss/python/langchain/tools](https://docs.langchain.com/oss/python/langchain/tools)   |
| Multi-LLM Routing  | LLM Selection      | [https://docs.langchain.com/oss/python/langchain/chains](https://docs.langchain.com/oss/python/langchain/chains) |
| Chain Patterns     | Common Patterns    | [https://docs.langchain.com/oss/python/langchain/chains](https://docs.langchain.com/oss/python/langchain/chains) |
