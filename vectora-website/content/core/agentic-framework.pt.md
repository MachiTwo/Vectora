---
title: "Agentic Framework: O Sistema Nervoso do Vectora"
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
  - system
  - tools
  - vectora
---

{{< lang-toggle >}}

> [!IMPORTANT] > **Redefinição Crítica**: O Agentic Framework **não é um módulo isolado**, nem uma pasta específica no código. Ele é o **sistema nervoso distribuído** do Vectora — a inteligência que permeia cada camada, observando, validando, corrigindo e orquestrando o comportamento do modelo de IA em tempo real.

Diferente de sistemas RAG tradicionais que apenas enviam dados para uma LLM, o Agentic Framework torna o Vectora auto-consciente e auto-corretivo, garantindo que as respostas sejam precisas, seguras e contextualizadas.

## O Que Agentic Framework Realmente É

O framework atua como uma camada cognitiva distribuída que gerencia o ciclo de vida de cada interação entre o usuário e o sub-agente.

- **Observação em Tempo Real**: O modelo "assiste" o resultado de cada chamada de ferramenta e ajusta seu raciocínio imediatamente.
- **Meta-cognição**: O sistema avalia sua própria confiança e decide autonomamente quando deve delegar tarefas, corrigir erros ou pedir clarificações.
- **Auto-correção**: Implementa uma escada de recuperação (Recovery Ladder) para tratar falhas de precisão ou erros de API sem interromper o fluxo do usuário.
- **Memória de Execução**: Cada decisão e erro é persistido, permitindo auditoria completa e aprendizado sobre o comportamento do agente.

## Camada Cognitiva vs Fluxo Passivo

| Conceito         | Visão Agentic (Vectora)                        | Fluxo Tradicional (Passivo)       |
| :--------------- | :--------------------------------------------- | :-------------------------------- |
| **Orquestração** | Distribuída entre prompt, tools e estado       | Sequencial e rígida (hardcoded)   |
| **Recuperação**  | Escada de estratégias por custo (Retry/Rerank) | Try/catch genérico com erro final |
| **Estado**       | Imutável com trilha de auditoria completa      | Variáveis globais mutáveis        |
| **Contexto**     | Pipeline ativo de compactação e reshaping      | Acúmulo de mensagens até o limite |

## As 5 Camadas do Agentic Framework

A arquitetura é dividida em cinco camadas lógicas que garantem a integridade operacional do sistema.

```mermaid
graph TD
    A[Loop Principal do Agente] --> Vectora Cognitive Runtime[Vectora Cognitive Runtime: Policy Orchestrator]
    Vectora Cognitive Runtime --> B[Camada 1: Context Pipeline]
    Vectora Cognitive Runtime --> C[Camada 2: Streaming Execution]
    Vectora Cognitive Runtime --> D[Camada 3: Recovery Ladder]
    Vectora Cognitive Runtime --> E[Camada 4: Termination Conditions]
    Vectora Cognitive Runtime --> F[Camada 5: State Threading]

    B --> B1[Compactação e Trimming]
    C --> C1[Execução Concorrente de Tools]
    D --> D1[Estratégias de Auto-correção]
    E --> E1[Estados Terminais Tipados]
    F --> F1[Estado Imutável e Auditoria]
```

O **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** é o motor de inferência local que alimenta o Agentic Framework. Ele decide, em cada iteração do loop principal, qual política de recuperação adotar ou se as condições de término foram atingidas, baseando-se em decisões estruturadas e auditáveis.

### 1. Context Pipeline

Gerencia o limite de tokens do modelo sem perder informação crítica. Utiliza técnicas de `applyToolResultBudget` para limitar outputs de ferramentas e `autoCompact` para resumir históricos longos quando o contexto atinge 95% da janela permitida.

### 2. Streaming Execution

Reduz a latência percebida executando ferramentas enquanto o modelo ainda está gerando a resposta. Isso permite que o Vectora apresente resultados parciais e valide dados em tempo real, diminuindo o tempo total de resposta em até 60%.

### 3. Recovery Ladder (Escada de Recuperação)

Quando uma operação falha ou a precisão da busca é baixa (< 0.65), o framework aciona estratégias ordenadas por custo.

1. **Retry com Parâmetros Ajustados**: Tenta novamente a mesma ferramenta com um prompt refinado.
2. **Rerank com Modelo Pesado**: Utiliza modelos de reranking mais potentes para desempatar resultados ambíguos.
3. **Bloqueio e Alerta**: Se um evento de segurança for detectado, o [Guardian](../security-engine) interrompe a execução imediatamente.

### 4. Condições de Término Tipadas

O framework define estados finais claros para evitar loops infinitos ou respostas incompletas, como `completed`, `max_turns` (limite de iterações) e `blocking_limit` (violação de política).

### 5. State Threading

O estado do agente é tratado como imutável. Cada iteração reconstrói um novo `AgentState` que contém todo o histórico de mensagens, ferramentas pendentes e a trilha de auditoria (audit trail) das decisões tomadas pelo framework.

## Métricas de Performance e SLAs

O Agentic Framework monitora métricas vitais em cada iteração para garantir que o sistema opere dentro dos padrões de qualidade definidos.

- **Retrieval Precision**: Alvo ≥ 0.65. Se cair, o sistema dispara refinamento de query automaticamente.
- **Tool Accuracy**: Alvo ≥ 0.95. Garante que as ferramentas estão retornando dados válidos.
- **Confidence Score**: Avaliação interna do Gemini sobre a precisão da resposta final.
- **Latência P95**: Alvo < 2000ms para iterações de processamento local.

## External Linking

| Concept        | Resource                                                   | Link                                                                                 |
| -------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Gemini AI**  | Google DeepMind Gemini Models                              | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/) |
| **Gemini API** | Google AI Studio Documentation                             | [ai.google.dev/docs](https://ai.google.dev/docs)                                     |
| **RAG**        | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                         |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
