---
title: Patterns - Architectural Paradigms
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

Vectora's operational patterns define how different components of the ecosystem combine to solve complex engineering and artificial intelligence problems.

## Vectora Cognitive Runtime-Orchestrated Architectural Paradigms

The **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** is the engine that orchestrates the execution of these patterns. It decides, in real-time, when to trigger a sub-agent, how to validate Connected RAG, and which events should be captured by Trace to ensure 360-degree tactical governance.

## Available Patterns

Detailed below are the main paradigms natively supported by the system, focused on productivity and observability.

### Connected RAG

Connected RAG goes beyond simple retrieval and generation. It integrates a validation loop against the live codebase, ensuring that suggested code not only makes semantic sense but is also syntactically valid within the project context.

**Learn more**: [→ Connected RAG](./rag.en.md)

### Sub-Agents (Tier 2)

This pattern focuses on the governance of subordinate agents with limited authority. A master agent can delegate tasks to specialized sub-agents, maintaining full control over permissions and ensuring a clear audit trail.

**Learn more**: [→ Sub-Agents](./sub-agents.en.md)

### Trace

Trace is the structured logbook of all agentic execution. It allows for complete observability of the model's thought process, tool calls, and context changes, facilitating the debugging of complex behaviors.

**Learn more**: [→ Trace](./trace.en.md)

## Usage Matrix

This matrix assists in choosing the most suitable pattern for each technical need within the ecosystem.

| Pattern           | Use Case                  | Example                       |
| :---------------- | :------------------------ | :---------------------------- |
| **Connected RAG** | Contextual and valid code | Complex function refactoring  |
| **Sub-Agents**    | Multi-domain tasks        | Code review + test generation |
| **Trace**         | Debugging and auditing    | Agent decision analysis       |

## External Linking

| Concept           | Resource                                                   | Link                                                                                                     |
| ----------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Trace**         | Distributed Tracing Concepts (OpenTelemetry)               | [opentelemetry.io/docs/concepts/signals/traces/](https://opentelemetry.io/docs/concepts/signals/traces/) |
| **RAG**           | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                                             |
| **Observability** | Control Theory and System Observability                    | [en.wikipedia.org/wiki/Observability](https://en.wikipedia.org/wiki/Observability)                       |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
