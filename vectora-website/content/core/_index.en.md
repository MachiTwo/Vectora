---
title: "Core: Vectora's Intelligent System"
slug: core
date: 2026-04-25T23:00:00-03:00
type: docs
sidebar:
  open: true
tags:
  - agentic-framework
  - ai
  - architecture
  - concepts
  - context-engine
  - core
  - gemini
  - state
  - system
  - vectora
draft: false
---

{{< lang-toggle >}}

The Core is where Vectora "thinks" and acts. It contains the components that make Vectora an intelligent and self-correcting agent, not just a passive code search system.

By integrating advanced reasoning with deep context awareness, the Core ensures that every interaction is grounded in the reality of your codebase.

## Principal Components

Vectora's intelligence is built on two primary engines that work in tandem to provide accurate and actionable insights.

### Agentic Framework

Vectora's distributed nervous system — a 5-layer state machine that validates, executes, and recovers from failures at every step. Gemini powers the machine, but the machine controls Gemini, not the other way around.

**Learn how**: [→ Agentic Framework](./agentic-framework.md)

### Context Engine

Vectora's intelligent context curator. A 5-step pipeline that decides **what, how, and when** to fetch context in the codebase, filtering noise and avoiding overfetch.

**Learn how**: [→ Context Engine](./context-engine.md)

### Vectora Decision Engine (Vectora Cognitive Runtime)

The Core's tactical brain. Vectora Cognitive Runtime is the local inference layer that orchestrates the decision policy between the Agentic Framework and the Context Engine, ensuring every action is secure, auditable, and hallucination-free.

**Learn how**: [→ Vectora Cognitive Runtime Architecture](../models/vectora-decision-engine.md)

## How They Work Together

The Agentic Framework feeds the decision machine, while the Context Engine provides the fuel: relevant context at the right time. Together, they transform queries into precise answers and reliable code modifications.

## External Linking

| Concept              | Resource                       | Link                                                                                 |
| -------------------- | ------------------------------ | ------------------------------------------------------------------------------------ |
| **Gemini AI**        | Google DeepMind Gemini Models  | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/) |
| **Gemini API**       | Google AI Studio Documentation | [ai.google.dev/docs](https://ai.google.dev/docs)                                     |
| **Anthropic Claude** | Claude Documentation           | [docs.anthropic.com/](https://docs.anthropic.com/)                                   |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
