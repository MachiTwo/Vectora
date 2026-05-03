---
title: "Tracing de Queries e Decisões"
slug: "langchain/langsmith/trace-queries"
description: "Captura e análise de traces de decisões de agentes"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langsmith", "tracing", "queries", "debugging", "agent-decisions"]
---

{{< lang-toggle >}}

LangSmith captura automaticamente toda execução de agentes. Você pode inspecionar inputs, outputs, decisões LLM e chamadas de tools.

## Traces Automáticos

Todos os runnables são tracejados automaticamente:

```python
# Isso cria um trace em LangSmith automaticamente
result = agent.invoke({
    "user_input": "Qual é o preço do Bitcoin?",
    "session_id": "user_123"
})

# Acesso em: smith.langchain.com → Projects → vectora-agents → Traces
```

## Inspecionar Traces

Cada trace mostra:

- **Input**: Dados enviados ao agente
- **LLM Call**: Prompt e resposta do modelo
- **Tool Calls**: Ferramentas executadas
- **Output**: Resultado final
- **Latency**: Tempo total

## Traces de Agentes com Tool Use

Quando o agente chama tools:

```
┌─ User Input ─┐
│              ↓
│        [Agent Thinks]
│              ↓
│        [Choose Tool]
│              ↓
│        [Execute Tool]
│              ↓
│        [Process Result]
│              ↓
└─ Final Output ┘

LangSmith captura CADA etapa acima
```

## Tags e Metadata

Adicione contexto aos traces:

```python
from langsmith import trace

@trace(name="search_agent")
def search_agent(query):
    # Seu código
    return result

# Ou com metadata
chain.invoke(
    {"input": data},
    config={
        "tags": ["search", "production"],
        "metadata": {"user_id": "123", "session": "abc"}
    }
)
```

## External Linking

| Conceito            | Recurso             | Link                                                                                                                     |
| ------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Tracing Guide       | Trace Queries       | [https://docs.langchain.com/langsmith/observability/tracing](https://docs.langchain.com/langsmith/observability/tracing) |
| Runs                | Trace Runs          | [https://docs.langchain.com/langsmith/observability/runs](https://docs.langchain.com/langsmith/observability/runs)       |
| Agent Debugging     | Agent Traces        | [https://www.langchain.com/articles/agent-observability](https://www.langchain.com/articles/agent-observability)         |
| Distributed Tracing | OpenTelemetry       | [https://opentelemetry.io/docs/concepts/signals/traces/](https://opentelemetry.io/docs/concepts/signals/traces/)         |
| Dashboard           | LangSmith Dashboard | [https://smith.langchain.com/](https://smith.langchain.com/)                                                             |
