---
title: "LangSmith: Observabilidade em Produção"
slug: "langchain/langsmith"
description: "Tracing, debugging e observability para agentes em produção"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langsmith", "observability", "tracing", "debugging", "monitoring"]
---

{{< lang-toggle >}}

LangSmith é a plataforma de observabilidade nativa da LangChain para debug, tracing e monitoramento de agentes em produção. Ela fornece visibilidade completa sobre decisões de agentes, performance e custos.

## O que é LangSmith?

LangSmith oferece:

- **Tracing** - Capture completo de execução de agents e chains
- **Debugging** - Inspect detalhado de inputs/outputs
- **Performance** - Métricas de latência, tokens e custos
- **Testing** - Dataset management e evaluations
- **Monitoring** - Alertas e dashboards em produção

## Arquitetura de Observabilidade

```
Agente Vectora
    ↓
LangSmith SDK
    ↓
Tracing Backend
    ↓
LangSmith Dashboard
    ↓
Métricas & Análise
```

## Recursos Principais

### Execution Traces

Cada chamada ao agente é capturada completamente:

- Input/Output de cada step
- Decisões do LLM
- Execução de tools
- Erros e retries

### Performance Analytics

Acompanhe em tempo real:

- Latência por operação
- Tokens consumidos
- Custo por request
- Taxa de erro

## External Linking

| Conceito            | Recurso                      | Link                                                                                                                               |
| ------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| LangSmith Home      | LangSmith Official           | [https://www.langchain.com/langsmith/observability](https://www.langchain.com/langsmith/observability)                             |
| LangSmith Docs      | Observability Documentation  | [https://docs.langchain.com/langsmith/observability](https://docs.langchain.com/langsmith/observability)                           |
| Agent Observability | Agent Monitoring             | [https://www.langchain.com/articles/agent-observability](https://www.langchain.com/articles/agent-observability)                   |
| LLM Monitoring      | Monitoring and Observability | [https://www.langchain.com/articles/llm-monitoring-observability](https://www.langchain.com/articles/llm-monitoring-observability) |
| Setup Guide         | LangSmith Setup              | [https://docs.langchain.com/langsmith/](https://docs.langchain.com/langsmith/)                                                     |
