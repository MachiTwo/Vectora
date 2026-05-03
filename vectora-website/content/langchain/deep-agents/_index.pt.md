---
title: "Deep Agents: Framework para Tarefas Complexas"
slug: "langchain/deep-agents"
description: "Agent harness com planning, filesystem backend e subagents"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["deep-agents", "agents", "planning", "filesystem", "subagents"]
---

{{< lang-toggle >}}

Deep Agents é um framework open-source para construir agentes complexos com planejamento nativo, suporte a subagents e persistência de estado no filesystem. Ideal para tarefas que requerem planejamento multi-step.

## O que é Deep Agents?

Deep Agents fornece:

- **Agent Harness** - Orquestração robusta de agentes
- **Planning** - Planejamento automático de tarefas
- **Filesystem Backend** - Persistência local de estado
- **Subagents** - Hierarquia de agentes
- **ACP Protocol** - Protocolo de comunicação entre agentes

## Diferenças de LangGraph

| Aspecto      | LangGraph               | Deep Agents         |
| ------------ | ----------------------- | ------------------- |
| Grafo        | Explícito (nodes/edges) | Implícito (harness) |
| Planning     | Manual                  | Automático          |
| Persistência | Memória                 | Filesystem          |
| CLI          | Não                     | Sim (rich TUI)      |
| Subagents    | Sim                     | Nativo              |

## Arquitetura

```
┌─────────────────────────┐
│   User / Client (ACP)   │
└────────────┬────────────┘
             │
┌────────────▼────────────┐
│   Deep Agent Harness    │
├────────────────────────┤
│ Planning & Routing     │
│ State Management       │
│ Tool Execution         │
└────────────┬────────────┘
             │
      ┌──────┴──────┐
      │             │
   [Tool 1]     [Tool 2]
```

## Componentes Principais

### Agent Harness

Container para execução segura de agentes:

```python
from deepagents import Agent

agent = Agent(
    name="research_agent",
    tools=[search, summarize],
    model="claude-3-opus"
)
```

### Planning Engine

Quebra tarefas em subtarefas:

```python
# Agent automaticamente planeja
result = agent.execute("Pesquise e resuma as últimas notícias sobre IA")
# Internamente: [search] → [summarize] → [output]
```

## ACP Protocol

Communication protocol entre agentes:

```
Agent A                    Agent B
   │                          │
   └──── ACP Request ────────►│
   │                          │
   │◄──── ACP Response ───────┘
```

## External Linking

| Conceito         | Recurso                  | Link                                                                                                                   |
| ---------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Deep Agents Home | Official Website         | [https://www.langchain.com/deep-agents](https://www.langchain.com/deep-agents)                                         |
| Deep Agents Docs | Overview Documentation   | [https://docs.langchain.com/oss/python/deepagents/overview](https://docs.langchain.com/oss/python/deepagents/overview) |
| GitHub           | Deep Agents Repository   | [https://github.com/langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)                               |
| API Reference    | Deep Agents API          | [https://reference.langchain.com/python/deepagents](https://reference.langchain.com/python/deepagents)                 |
| Blog             | Deep Agents Announcement | [https://blog.langchain.com/deep-agents/](https://blog.langchain.com/deep-agents/)                                     |
