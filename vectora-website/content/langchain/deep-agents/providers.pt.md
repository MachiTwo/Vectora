---
title: "Provedores LLM no Deep Agents"
slug: "langchain/deep-agents/providers"
description: "Configuração de diferentes provedores de LLM"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["deep-agents", "providers", "llm", "configuration"]
---

{{< lang-toggle >}}

Deep Agents suporta múltiplos provedores de LLM com configuração simples via variáveis de ambiente ou código.

## Provedores Suportados

### Anthropic Claude

Recomendado para máxima performance em agentes:

```python
from deepagents import Agent

agent = Agent(
    name="research",
    model="claude-sonnet-4-6",  # ou claude-opus-4-7, claude-haiku-4-5-20251001
    api_key=os.getenv("ANTHROPIC_API_KEY")
)
```

Variáveis de ambiente:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export DEEPAGENTS_MODEL=claude-3-opus
```

### OpenAI

GPT-4o como alternativa:

```python
agent = Agent(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

## Configuração Multi-Provedor

Rota para o melhor provedor por tarefa:

```python
from deepagents import routing

router = routing.MultiProviderRouter({
    "complex_analysis": "claude-opus-4-7",
    "simple_chat": "claude-haiku-4-5-20251001",
    "code_gen": "gpt-4o",
})

result = agent.execute(
    task="Analise código Python",
    provider=router.select("code_gen")
)
```

## Fallback Strategy

Automaticamente tenta próximo provedor em caso de erro:

```python
agent = Agent(
    model="claude-opus-4-7",
    fallback=["gpt-4o"],
    max_retries=3
)
```

## External Linking

| Conceito             | Recurso                      | Link                                                                                            |
| -------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------- |
| **LangChain Agents** | LangChain agent docs         | [python.langchain.com/docs/concepts/agents](https://python.langchain.com/docs/concepts/agents/) |
| **Claude API**       | Anthropic documentation      | [docs.anthropic.com](https://docs.anthropic.com/)                                               |
| **OpenAI API**       | OpenAI documentation         | [platform.openai.com/docs](https://platform.openai.com/docs/)                                   |
| **LangGraph**        | Stateful agent orchestration | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/)                   |
