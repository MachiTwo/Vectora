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
    model="claude-3-opus",  # ou claude-3-sonnet, claude-3-haiku
    api_key=os.getenv("ANTHROPIC_API_KEY")
)
```

Variáveis de ambiente:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
export DEEPAGENTS_MODEL=claude-3-opus
```

### OpenAI

GPT-4 e GPT-3.5:

```python
agent = Agent(
    model="gpt-4",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

### Google Gemini

Gemini Pro:

```python
agent = Agent(
    model="gemini-pro",
    api_key=os.getenv("GOOGLE_API_KEY")
)
```

## Configuração Multi-Provedor

Rota para o melhor provedor por tarefa:

```python
from deepagents import routing

router = routing.MultiProviderRouter({
    "complex_analysis": "claude-3-opus",
    "simple_chat": "claude-3-haiku",
    "code_gen": "gpt-4",
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
    model="claude-3-opus",
    fallback=["gpt-4", "gemini-pro"],
    max_retries=3
)
```

## External Linking

| Conceito         | Recurso              | Link                                                                                                                   |
| ---------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Deep Agents Docs | Provider Setup       | [https://docs.langchain.com/oss/python/deepagents/](https://docs.langchain.com/oss/python/deepagents/)                 |
| Claude API       | Anthropic Claude     | [https://docs.anthropic.com/](https://docs.anthropic.com/)                                                             |
| Gemini API       | Google AI Studio     | [https://ai.google.dev/docs](https://ai.google.dev/docs)                                                               |
| OpenAI API       | OpenAI Documentation | [https://platform.openai.com/docs/](https://platform.openai.com/docs/)                                                 |
| Environment Vars | Configuration Guide  | [https://docs.langchain.com/oss/python/deepagents/overview](https://docs.langchain.com/oss/python/deepagents/overview) |
