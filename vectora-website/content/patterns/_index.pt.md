---
title: Patterns - Paradigmas Arquiteturais
slug: patterns
date: 2026-04-25T23:00:00-03:00
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - concepts
  - governance
  - patterns
  - rag
  - sub-agents
  - system
  - tools
  - trace
  - vectora
draft: false
---

{{< lang-toggle >}}

Os padrões operacionais do Vectora definem como diferentes componentes do ecossistema se combinam para resolver problemas complexos de engenharia e inteligência artificial.

## Paradigmas Arquiteturais Orquestrados pelo Vectora Cognitive Runtime

O **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** é o motor que orquestra a execução desses padrões. Ele decide, em tempo real, quando disparar um sub-agente, como validar o RAG Conectado e quais eventos devem ser capturados pelo Trace para garantir uma governança tática de 360 graus.

## Padrões Disponíveis

Abaixo estão detalhados os principais paradigmas suportados nativamente pelo sistema, focados em produtividade e observabilidade.

### RAG Conectado

O RAG Conectado vai além da simples recuperação e geração. Ele integra um loop de validação contra o codebase vivo, garantindo que o código sugerido não apenas faça sentido semântico, mas que também seja sintaticamente válido no contexto do projeto.

**Saiba mais**: [→ RAG Conectado](./rag.md)

### Sub-Agents (Tier 2)

Este padrão foca na governança de agentes subordinados com autoridade limitada. Um agente mestre pode delegar tarefas para sub-agentes especializados, mantendo controle total sobre as permissões e garantindo uma trilha de auditoria clara.

**Saiba mais**: [→ Sub-Agents](./sub-agents.md)

### Trace

O Trace é o diário de bordo estruturado de toda a execução agentica. Ele permite a observabilidade completa do fluxo de pensamento do modelo, chamadas de ferramentas e mudanças de contexto, facilitando a depuração de comportamentos complexos.

**Saiba mais**: [→ Trace](./trace.md)

## Matriz de Uso

Esta matriz auxilia na escolha do padrão mais adequado para cada necessidade técnica dentro do ecossistema.

| Padrão            | Caso de Uso                | Exemplo                              |
| :---------------- | :------------------------- | :----------------------------------- |
| **RAG Conectado** | Código contextual e válido | Refatoração de funções complexas     |
| **Sub-Agents**    | Tarefas multi-domínio      | Review de código + geração de testes |
| **Trace**         | Depuração e auditoria      | Análise de decisões do agente        |

## External Linking

| Concept           | Resource                                                   | Link                                                                                                     |
| ----------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Trace**         | Distributed Tracing Concepts (OpenTelemetry)               | [opentelemetry.io/docs/concepts/signals/traces/](https://opentelemetry.io/docs/concepts/signals/traces/) |
| **RAG**           | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                                             |
| **Observability** | Control Theory and System Observability                    | [en.wikipedia.org/wiki/Observability](https://en.wikipedia.org/wiki/Observability)                       |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
