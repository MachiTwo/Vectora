---
title: Trace
description: Entenda o conceito de Trace como o diário de bordo estruturado para execuções agenticas e gerenciamento de contexto.
slug: trace
tags:
  - agentic
  - ai
  - architecture
  - auth
  - concepts
  - context
  - integration
  - observability
  - openai
  - plugins
  - state
  - system
  - tools
  - trace
  - vectora
---

{{< lang-toggle >}}

O Trace é o registro sequencial e estruturado de todos os eventos que ocorrem durante a execução de um agente de inteligência artificial. Ele serve como a fonte de verdade para depuração, auditoria e otimização de fluxos de trabalho autônomos.

Enquanto um modelo de linguagem (LLM) atua como o cérebro da operação, o Trace funciona como o diário de bordo da missão. Ele captura não apenas as entradas e saídas, mas todo o processo de raciocínio, chamadas de ferramentas e mudanças de estado que levaram ao resultado final.

## Arquitetura do Trace

Um Trace bem estruturado permite que desenvolvedores e sistemas de monitoramento reconstruam exatamente o que aconteceu em qualquer ponto da execução. Isso é fundamental para entender o comportamento de agentes em ambientes complexos onde múltiplas ferramentas e subagentes interagem.

O sistema de Trace do Vectora é projetado para ser extensível, permitindo que plugins e integrações externas adicionem seus próprios metadados e logs específicos ao fluxo principal de execução.

## Componentes Típicos

Um Trace completo é composto por diversos elementos que detalham a jornada do agente desde o início da sessão até a conclusão da tarefa.

- **Cabeçalho da Sessão (Session Header)**: Contém metadados globais como ID da sessão, timestamp de início, diretório de trabalho atual (CWD) e a versão do formato do Trace.
- **Mensagens (Messages)**: Registro de interações entre Usuário, Assistente e resultados de Ferramentas, incluindo contagem de tokens e custos associados.
- **Chamadas de Ferramentas (Tool Calls)**: Detalha qual ferramenta foi invocada, com quais argumentos e qual foi o resultado exato retornado.
- **Mudanças de Modelo (Model Changes)**: Registra trocas de modelo durante a sessão (ex: alternar de Claude para GPT-4o conforme a complexidade da tarefa).
- **Níveis de Raciocínio (Thinking Levels)**: Monitora mudanças no nível de raciocínio ou esforço computacional (low, medium, high) aplicado pelo agente.
- **Compactações (Compactions)**: Documenta quando e como contextos antigos foram resumidos para economizar tokens e manter a janela de contexto relevante.
- **Bifurcações (Branches)**: Registra ramificações da conversa onde diferentes caminhos foram explorados pelo agente antes de uma decisão final.
- **Entradas Customizadas**: Dados específicos injetados por extensões ou plugins integrados ao sistema.

## External Linking

| Concept              | Resource                                     | Link                                                                                                     |
| -------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Trace**            | Distributed Tracing Concepts (OpenTelemetry) | [opentelemetry.io/docs/concepts/signals/traces/](https://opentelemetry.io/docs/concepts/signals/traces/) |
| **Anthropic Claude** | Claude Documentation                         | [docs.anthropic.com/](https://docs.anthropic.com/)                                                       |
| **OpenAI**           | OpenAI API Documentation                     | [platform.openai.com/docs/](https://platform.openai.com/docs/)                                           |
| **Observability**    | Control Theory and System Observability      | [en.wikipedia.org/wiki/Observability](https://en.wikipedia.org/wiki/Observability)                       |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
