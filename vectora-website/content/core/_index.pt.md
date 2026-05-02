---
title: "Core: Sistema Inteligente do Vectora"
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

O Core é onde o Vectora "pensa" e age. Ele contém os componentes que tornam o Vectora um agente inteligente e auto-corrigível, indo além de um simples sistema de busca de código passivo.

Ao integrar raciocínio avançado com uma profunda consciência de contexto, o Core garante que cada interação seja fundamentada na realidade da sua base de código.

## Componentes Principais

A inteligência do Vectora é construída sobre dois motores principais que trabalham em conjunto para fornecer insights precisos e acionáveis.

### Agentic Framework

O sistema nervoso distribuído do Vectora — uma máquina de estado de 5 camadas que valida, executa e recupera de falhas em cada etapa. O Gemini alimenta a máquina, mas a máquina controla o Gemini, não o contrário.

**Saiba como**: [→ Agentic Framework](./agentic-framework.md)

### Context Engine

O curador inteligente de contexto do Vectora. Um pipeline de 5 etapas que decide **o quê, como e quando** buscar contexto no codebase, filtrando ruído e evitando o excesso de dados (overfetch).

**Saiba como**: [→ Context Engine](./context-engine.md)

### Vectora Decision Engine (Vectora Cognitive Runtime)

O cérebro tático do Core. O Vectora Cognitive Runtime é a camada de inferência local que orquestra a política de decisão entre o Agentic Framework e o Context Engine, garantindo que cada ação seja segura, auditável e livre de alucinações.

**Saiba como**: [→ Vectora Cognitive Runtime Architecture](../models/vectora-decision-engine.md)

## Como Trabalham Juntos

O Agentic Framework alimenta a máquina de decisão, enquanto o Context Engine fornece o combustível: contexto relevante no momento certo. Juntos, eles transformam consultas simples em respostas precisas e modificações de código confiáveis.

## External Linking

| Concept              | Resource                       | Link                                                                                 |
| -------------------- | ------------------------------ | ------------------------------------------------------------------------------------ |
| **Gemini AI**        | Google DeepMind Gemini Models  | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/) |
| **Gemini API**       | Google AI Studio Documentation | [ai.google.dev/docs](https://ai.google.dev/docs)                                     |
| **Anthropic Claude** | Claude Documentation           | [docs.anthropic.com/](https://docs.anthropic.com/)                                   |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
