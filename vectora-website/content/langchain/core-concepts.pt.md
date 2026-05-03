---
title: "Conceitos Principais do LangChain"
slug: "langchain/core-concepts"
description: "Runnables, tools, memory e retrieval no LangChain"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "concepts", "runnables", "tools", "memory", "retrieval"]
---

{{< lang-toggle >}}

Os conceitos principais do LangChain são os blocos de construção para qualquer aplicação com LLM. Eles podem ser compostos para criar workflows complexos.

## Runnables

Runnables são abstrações compostas que representam qualquer unidade de trabalho. Podem ser:

- Prompts
- LLMs
- Chains (sequências de runnables)
- Tools
- Custom functions

```python
from langchain.runnables import RunnableSequence

chain = prompt | llm | output_parser
result = chain.invoke({"input": "data"})
```

## Tools

Tools são funções que um agente pode chamar. LangChain fornece decoradores para defini-los:

```python
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Busca na web"""
    return results

@tool
def calculate(expression: str) -> str:
    """Calcula uma expressão matemática"""
    return eval(expression)
```

## Memory

Sistemas de memória permitem que agentes lembrem de conversas anteriores:

- **Buffer** - Histórico completo de mensagens
- **Summarization** - Resumir histórico antigo
- **Entity** - Rastrear entidades específicas
- **Vector Store** - Memória semântica

## Retrieval

Retrieval integra busca vetorial para RAG:

- Embeddings (via Voyage, OpenAI, etc)
- Vector stores (LanceDB, Pinecone, etc)
- Retrievers com reranking
- Chat history retrieval

## Padrão RAG

```
User Query
    ↓
Embeddings
    ↓
Vector Search
    ↓
Reranking
    ↓
Context Retrieval
    ↓
LLM com contexto
    ↓
Response
```

## External Linking

| Conceito            | Recurso                 | Link                                                                                                                   |
| ------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| LangChain Runnables | Runnables Documentation | [https://docs.langchain.com/oss/python/langchain/runnable](https://docs.langchain.com/oss/python/langchain/runnable)   |
| Tools               | LangChain Tools         | [https://docs.langchain.com/oss/python/langchain/tools](https://docs.langchain.com/oss/python/langchain/tools)         |
| Memory              | Memory Systems          | [https://docs.langchain.com/oss/python/langchain/memory](https://docs.langchain.com/oss/python/langchain/memory)       |
| Retrieval           | Retrieval and RAG       | [https://docs.langchain.com/oss/python/langchain/retrieval](https://docs.langchain.com/oss/python/langchain/retrieval) |
| Chains              | LangChain Chains        | [https://docs.langchain.com/oss/python/langchain/chains](https://docs.langchain.com/oss/python/langchain/chains)       |
