---
title: Models
slug: models
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - byok
  - concepts
  - config
  - embeddings
  - gemini
  - integration
  - models
  - privacy
  - rag
  - reranker
  - vectora
  - voyage
---

{{< lang-toggle >}}

Vectora funciona com modelos de AI específicos e otimizados para programação, interação com o usuário, busca semântica e decisões táticas.

## Vectora Decision Engine (Vectora Cognitive Runtime)

A inteligência decisiva local do Vectora. Baseado no SmolLM com fine-tuning proprietário, o Vectora Cognitive Runtime roda via **ONNX Runtime** diretamente no desktop do usuário. Ele decide o roteamento tático das consultas com latência zero, recorrendo à nuvem apenas em integrações específicas que não permitem execução local.

## Gemini 3 Flash

O Agente de Programação e Interação do Vectora. É o motor que conversa com o desenvolvedor, escreve, refatora e analisa código em tempo real. O Gemini 3 Flash utiliza as IAs especializadas da Voyage para recuperar o contexto exato necessário para cada tarefa, garantindo respostas técnicas precisas em milissegundos.

## Voyage AI

A suite Voyage (Voyage 4 e Rerank 2.5) fornece as IAs especializadas usadas pelo Gemini para o RAG (Retrieval-Augmented Generation). O modelo Voyage 4 é ciente de estruturas de código (AST), garantindo que as buscas encontrem funcionalidades logicamente relacionadas.

## Modos de Operação

| Recurso              | Modo BYOK (Free)                | Modo Managed (Plus)      |
| :------------------- | :------------------------------ | :----------------------- |
| **Modelos Padrão**   | Gemini + Voyage                 | Gemini + Voyage          |
| **Gestão de Chaves** | Você fornece (BYOK)             | Gerenciado pela Vectora  |
| **Custo de IA**      | Pago ao provedor (ou Free tier) | Incluso no plano Vectora |
| **Configuração**     | Manual (`vectora config`)       | Automática (Zero Config) |
| **Privacidade**      | Chaves locais                   | Chaves gerenciadas       |

## Próximas Leituras

- [Vectora Cognitive Runtime Architecture](./vectora-decision-engine.md) — SmolLM + ONNX
- [Gemini Configuration](./gemini.md) — Setup Google AI
- [Voyage Configuration](./voyage.md) — Setup Voyage AI
- [Conceitos](../concepts/embeddings.md) — Como embeddings funcionam

---

## External Linking

| Concept               | Resource                            | Link                                                                                 |
| --------------------- | ----------------------------------- | ------------------------------------------------------------------------------------ |
| **Voyage AI**         | High-performance embeddings for RAG | [www.voyageai.com/](https://www.voyageai.com/)                                       |
| **Voyage Embeddings** | Voyage Embeddings Documentation     | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)       |
| **Voyage Reranker**   | Voyage Reranker API                 | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)           |
| **Gemini AI**         | Google DeepMind Gemini Models       | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/) |
| **Gemini API**        | Google AI Studio Documentation      | [ai.google.dev/docs](https://ai.google.dev/docs)                                     |
| **Anthropic Claude**  | Claude Documentation                | [docs.anthropic.com/](https://docs.anthropic.com/)                                   |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
