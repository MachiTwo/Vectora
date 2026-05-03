---
title: "Monitoramento de Performance"
slug: "langchain/langsmith/performance-monitoring"
description: "Latência, tokens, custos e métricas de performance"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langsmith", "monitoring", "performance", "latency", "tokens", "costs"]
---

{{< lang-toggle >}}

LangSmith fornece métricas em tempo real sobre performance, custos e confiabilidade de agentes em produção.

## Métricas Principais

### Latência

- **Total**: Tempo do início ao fim
- **LLM**: Tempo da chamada ao modelo
- **Tools**: Tempo de execução de tools
- **Network**: Overhead de rede

### Tokens

- **Input Tokens**: Tokens enviados
- **Output Tokens**: Tokens gerados
- **Total**: Soma dos dois

### Custos

- **Por request**: Custo individual
- **Agregado**: Total por período
- **Por agente**: Análise por projeto

## Dashboard de Monitoramento

```
LangSmith Dashboard
├─ Real-time Metrics
│  ├─ Requests/min
│  ├─ Avg Latency
│  ├─ Error Rate
│  └─ Total Cost
├─ Traces
│  └─ Inspecionar execuções individuais
└─ Evaluations
   └─ Resultados de testes
```

## Alertas e Thresholds

Configure alertas para anomalias:

```python
# Latência alta
if avg_latency > 5000:  # ms
    send_alert("Agent latency exceeds 5s")

# Taxa de erro
if error_rate > 0.05:  # 5%
    send_alert("Error rate above 5%")

# Custo anômalo
if daily_cost > budget:
    send_alert("Budget exceeded")
```

## Análise de Custos

Entenda gastos por:

- **Modelo**: Claude Opus vs Haiku
- **Agente**: Qual agente custa mais?
- **Período**: Comparar semanas/meses
- **User**: Custo por usuário final

## External Linking

| Conceito            | Recurso            | Link                                                                                                                               |
| ------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Performance Metrics | Monitoring Guide   | [https://docs.langchain.com/langsmith/observability/metrics](https://docs.langchain.com/langsmith/observability/metrics)           |
| Latency             | Tracking Latency   | [https://docs.langchain.com/langsmith/observability/runs](https://docs.langchain.com/langsmith/observability/runs)                 |
| Token Counting      | Token Usage        | [https://docs.langchain.com/langsmith/observability/costs](https://docs.langchain.com/langsmith/observability/costs)               |
| Cost Analysis       | Cost Tracking      | [https://www.langchain.com/articles/llm-monitoring-observability](https://www.langchain.com/articles/llm-monitoring-observability) |
| Prometheus          | Metrics Collection | [https://prometheus.io/docs/introduction/overview/](https://prometheus.io/docs/introduction/overview/)                             |
