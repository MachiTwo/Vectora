---
title: "Gerenciamento de Memória"
slug: "langchain/deep-agents/memory"
description: "Gerenciamento de memória, contexto e persistência em Deep Agents"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["deep-agents", "memory", "context", "persistence"]
---

{{< lang-toggle >}}

Deep Agents oferece gerenciamento automático de memória com persistência no filesystem, ideal para agentes de longa duração.

## Tipos de Memória

### Short-term Memory

Contexto da conversa atual (context window):

```python
agent = Agent(
    name="chat_agent",
    memory_type="short_term",
    context_window=4096  # tokens
)

result = agent.execute("Qual é meu nome?")
# Dentro desta conversa, lembra
```

### Long-term Memory

Persistida no filesystem:

```python
agent = Agent(
    name="researcher",
    memory_type="long_term",
    memory_dir="~/.deep-agents/researcher"
)

# Conversa 1
agent.execute("Pesquise sobre IA")

# Conversa 2 (dias depois)
result = agent.execute("Resume o que pesquisou antes")
# Ainda lembra da pesquisa anterior
```

### Hybrid Memory

Combina short e long-term:

```python
agent = Agent(
    memory_type="hybrid",
    short_term_size=4096,
    long_term_dir="~/.agent-memory"
)
```

## Persistência no Filesystem

Automaticamente salva:

```
~/.deep-agents/
├── research_agent/
│   ├── conversations/
│   │   ├── conv_2026-05-01.json
│   │   └── conv_2026-05-02.json
│   ├── memory.db
│   └── state.json
```

## Resumização Automática

Quando contexto fica grande, resume automaticamente:

```python
agent = Agent(
    auto_summarize=True,
    summarize_threshold=0.8,  # 80% do context
    summarization_model="claude-3-haiku"
)

# Internamente: [antigo] → [resumo] → [novo]
```

## Limpeza de Memória

Gerenciar espaço:

```bash
deep-agents clean research_agent --days 7
# Remove conversas com mais de 7 dias
```

## External Linking

| Conceito           | Recurso            | Link                                                                                                                               |
| ------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Deep Agents Memory | Memory Guide       | [https://docs.langchain.com/oss/python/deepagents/memory](https://docs.langchain.com/oss/python/deepagents/memory)                 |
| LangChain Memory   | Memory Systems     | [https://docs.langchain.com/oss/python/langchain/memory](https://docs.langchain.com/oss/python/langchain/memory)                   |
| File System        | Filesystem Backend | [https://docs.langchain.com/oss/python/deepagents/data-locations](https://docs.langchain.com/oss/python/deepagents/data-locations) |
| Context Management | Context Window     | [https://docs.langchain.com/oss/python/langchain/](https://docs.langchain.com/oss/python/langchain/)                               |
| Summarization      | Text Summarization | [https://docs.langchain.com/oss/python/langchain/memory](https://docs.langchain.com/oss/python/langchain/memory)                   |
