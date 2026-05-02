---
title: "Agentic Framework: Vectora's Nervous System"
slug: agentic-framework
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - agentic-framework
  - ai
  - architecture
  - auth
  - concepts
  - errors
  - gemini
  - guardian
  - orchestration
  - rag
  - security
  - state
  - sub-agents
  - system
  - tools
  - vectora
---

{{< lang-toggle >}}

> [!IMPORTANT] > **Critical Redefinition**: The Agentic Framework is **not an isolated module**, nor a specific folder in the code. It is the **distributed nervous system** of Vectora — the intelligence that permeates every layer, observing, validating, correcting, and orchestrating the AI model's behavior in real-time.

Unlike traditional RAG systems that merely pipe data to an LLM, the Agentic Framework makes Vectora self-aware and self-correcting, ensuring that responses are accurate, secure, and contextually grounded.

## What the Agentic Framework Really Is

The framework acts as a distributed cognitive layer that manages the lifecycle of every interaction between the user and the sub-agent.

- **Real-Time Observation**: The model "watches" the result of every tool call and adjusts its reasoning immediately.
- **Meta-cognition**: The system evaluates its own confidence and autonomously decides when to delegate tasks, correct errors, or seek clarification.
- **Auto-correction**: It implements a Recovery Ladder to handle precision drops or API errors without interrupting the user flow.
- **Execution Memory**: Every decision and error is persisted, allowing for full auditability and learning from agent behavior.

## Cognitive Layer vs. Passive Flow

| Concept           | Agentic View (Vectora)                       | Traditional Flow (Passive)         |
| :---------------- | :------------------------------------------- | :--------------------------------- |
| **Orchestration** | Distributed between prompt, tools, and state | Sequential and rigid (hardcoded)   |
| **Recovery**      | Cost-ordered strategy ladder (Retry/Rerank)  | Generic try/catch with final error |
| **State**         | Immutable with a full audit trail            | Mutable global variables           |
| **Context**       | Active compaction and reshaping pipeline     | Message accumulation until limit   |

## The 5 Layers of the Agentic Framework

The architecture is divided into five logical layers that ensure the system's operational integrity.

```mermaid
graph TD
    A[Main Agent Loop] --> Vectora Cognitive Runtime[Vectora Cognitive Runtime: Policy Orchestrator]
    Vectora Cognitive Runtime --> B[Layer 1: Context Pipeline]
    Vectora Cognitive Runtime --> C[Layer 2: Streaming Execution]
    Vectora Cognitive Runtime --> D[Layer 3: Recovery Ladder]
    Vectora Cognitive Runtime --> E[Layer 4: Termination Conditions]
    Vectora Cognitive Runtime --> F[Layer 5: State Threading]

    B --> B1[Compaction and Trimming]
    C --> C1[Concurrent Tool Execution]
    D --> D1[Self-correction Strategies]
    E --> E1[Typed Terminal States]
    F --> F1[Immutable State and Audit]
```

The **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** is the local inference engine that powers the Agentic Framework. At each iteration of the main loop, it decides which recovery policy to adopt or whether termination conditions have been met, based on structured and auditable decisions.

### 1. Context Pipeline

Manages the model's token limit without losing critical information. It uses techniques like `applyToolResultBudget` to cap tool outputs and `autoCompact` to summarize long histories when the context reaches 95% of the allowed window.

### 2. Streaming Execution

Reduces perceived latency by executing tools while the model is still generating the response. This allows Vectora to present partial results and validate data in real-time, decreasing total response time by up to 60%.

### 3. Recovery Ladder

When an operation fails or search precision is low (< 0.65), the framework triggers cost-ordered strategies.

1. **Retry with Refined Parameters**: Re-attempts the same tool with a refined prompt.
2. **Heavy Model Rerank**: Uses more powerful reranking models to resolve ambiguous results.
3. **Block and Alert**: If a security event is detected, the [Guardian](../security-engine) interrupts execution immediately.

### 4. Typed Termination Conditions

The framework defines clear final states to prevent infinite loops or incomplete responses, such as `completed`, `max_turns` (iteration limit), and `blocking_limit` (policy violation).

### 5. State Threading

Agent state is treated as immutable. Every iteration reconstructs a new `AgentState` containing the full message history, pending tools, and the audit trail of decisions made by the framework.

## Performance Metrics and SLAs

The Agentic Framework monitors vital metrics at every iteration to ensure the system operates within defined quality standards.

- **Retrieval Precision**: Target ≥ 0.65. If it drops, the system automatically triggers query refinement.
- **Tool Accuracy**: Target ≥ 0.95. Ensures that tools are returning valid and expected data.
- **Confidence Score**: Gemini's internal assessment of final answer accuracy.
- **P95 Latency**: Target < 2000ms for local processing iterations.

## External Linking

| Concept        | Resource                                                   | Link                                                                                 |
| -------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Gemini AI**  | Google DeepMind Gemini Models                              | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/) |
| **Gemini API** | Google AI Studio Documentation                             | [ai.google.dev/docs](https://ai.google.dev/docs)                                     |
| **RAG**        | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                         |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
