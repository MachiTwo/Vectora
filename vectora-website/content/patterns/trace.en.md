---
title: Trace
description: Understand the concept of Trace as a structured logbook for agentic executions and context management.
slug: trace
tags:
  - agentic
  - ai
  - auth
  - concepts
  - context
  - observability
  - openai
  - plugins
  - state
  - sub-agents
  - system
  - tools
  - trace
  - vectora
---

{{< lang-toggle >}}

A Trace is the sequential and structured record of all events that occur during the execution of an artificial intelligence agent. It serves as the source of truth for debugging, auditing, and optimizing autonomous workflows.

While a large language model (LLM) acts as the brain of the operation, the Trace functions as the mission's logbook. It captures not just inputs and outputs, but the entire reasoning process, tool calls, and state changes that led to the final result.

## Fundamental Concepts

A well-structured Trace allows developers and monitoring systems to reconstruct exactly what happened at any point in the execution. This is essential for understanding the behavior of agents in complex environments where multiple tools and sub-agents interact.

The Vectora Trace system is designed to be extensible, allowing external plugins and integrations to add their own specific metadata and logs to the main execution flow.

## Typical Components

A complete Trace is composed of several elements that detail the agent's journey from the start of the session to the completion of the task.

- **Session Header**: Contains global metadata such as session ID, start timestamp, current working directory (CWD), and the Trace format version.
- **Messages**: Record of interactions between User, Assistant, and Tool results, including token counts and associated costs.
- **Tool Calls**: Details which tool was invoked, with what arguments, and the exact result returned.
- **Model Changes**: Records model swaps during the session (e.g., switching from Claude to GPT-4o based on task complexity).
- **Thinking Levels**: Monitors changes in the level of reasoning or computational effort (low, medium, high) applied by the agent.
- **Compactions**: Documents when and how old contexts were summarized to save tokens and maintain a relevant context window.
- **Branches**: Records conversation forks where different paths were explored by the agent before a final decision.
- **Custom Entries**: Specific data injected by integrated extensions or plugins.

## External Linking

| Concept              | Resource                                     | Link                                                                                                     |
| -------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Trace**            | Distributed Tracing Concepts (OpenTelemetry) | [opentelemetry.io/docs/concepts/signals/traces/](https://opentelemetry.io/docs/concepts/signals/traces/) |
| **Anthropic Claude** | Claude Documentation                         | [docs.anthropic.com/](https://docs.anthropic.com/)                                                       |
| **OpenAI**           | OpenAI API Documentation                     | [platform.openai.com/docs/](https://platform.openai.com/docs/)                                           |
| **Observability**    | Control Theory and System Observability      | [en.wikipedia.org/wiki/Observability](https://en.wikipedia.org/wiki/Observability)                       |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
