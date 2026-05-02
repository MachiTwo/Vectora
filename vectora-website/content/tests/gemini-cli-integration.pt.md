---
title: "Suite de Testes: Integração Gemini CLI"
slug: gemini-cli-integration-tests
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - cli
  - concepts
  - errors
  - gemini
  - gemini-cli
  - integration
  - mcp
  - protocol
  - state
  - system
  - testing
  - tools
  - vectora
---

{{< lang-toggle >}}

O Gemini CLI deve integrar perfeitamente com o Vectora via Model Context Protocol (MCP). Ele deve reconhecer inteligentemente quando utilizar as ferramentas do Vectora, lidar com a recuperação de dados de forma confiável e manter um fluxo de conversa fluido. Esta suite valida a inteligência de decisão, transparência e degradação graciosa.

Ao verificar esta integração, garantimos que a experiência de linha de comando para agentes de IA seja poderosa, confiável e consciente do contexto.

**Cobertura**: 100+ testes | **Prioridade**: CRÍTICA

## Princípios Centrais

A integração é construída sobre quatro princípios fundamentais que guiam o comportamento do sistema e a experiência do usuário.

1. **Inteligência de Decisão**: A CLI sabe precisamente quando chamar o Vectora com base na intenção do usuário.
2. **Transparência**: Os usuários podem ver quais ferramentas estão sendo chamadas e quais dados estão sendo recuperados.
3. **Degradação Graciosa**: Se o Vectora estiver indisponível, a CLI continua a funcionar com seu conhecimento base.
4. **Alta Performance**: Respostas finais são entregues em menos de 2 segundos para a maioria das consultas.

## Segmentos de Testes

As seções a seguir detalham os casos de teste específicos e os cenários cobertos por esta suite.

### 1. Inicialização & Setup da CLI (15 testes)

Garante que o ambiente esteja configurado corretamente e que a conexão entre a CLI e o Vectora esteja estável.

- **Disponibilidade do Vectora**: Detecta o binário do Vectora no PATH e estabelece uma conexão MCP via stdio.
- **Tratamento de Indisponibilidade**: Continua funcionando graciosamente com uma notificação clara se o Vectora não for encontrado.
- **Handshake MCP**: Valida o ciclo de requisição/resposta de `initialize` e garante que complete em menos de 2 segundos.
- **Descoberta de Ferramentas**: Verifica se todas as ferramentas esperadas (`search_context`, `analyze_dependencies`, etc.) estão expostas com schemas corretos.

### 2. Inteligência de Decisão (20 testes)

Foca na habilidade da IA em escolher a ferramenta certa para o trabalho com base na consulta em linguagem natural.

- **Consultas Relacionadas a Código**: Identifica corretamente pedidos de análise de código e aciona a ferramenta apropriada do Vectora.
- **Consultas Gerais**: Reconhece pedidos que não envolvem código e evita chamadas de ferramentas desnecessárias.
- **Consultas Ambíguas**: Oferece ao usuário a escolha entre buscar na base de código ou uma explicação geral.
- **Consciência de Contexto**: Mantém o contexto através de múltiplos turnos para resolver referências relativas (ex: "E quanto a _esta_ função?").

### 3. Invocação de Ferramentas & Tratamento de Erros (25 testes)

Valida a confiabilidade das chamadas individuais de ferramentas e a resiliência do sistema a erros.

- **Mapeamento de Parâmetros**: Garante que intenções em linguagem natural sejam mapeadas corretamente para parâmetros JSON-RPC.
- **Propagação de Erros**: Lida graciosamente e explica erros retornados pelo Vectora (ex: caminho de arquivo inválido).
- **Conjuntos de Resultados Grandes**: Testa a paginação e sumarização quando uma ferramenta retorna um alto volume de dados.
- **Timeouts**: Aciona notificações claras se uma ferramenta demorar mais de 10 segundos para responder.

### 4. Continuidade da Conversa (15 testes)

Garante que o estado seja preservado ao longo de uma investigação em múltiplas etapas.

- **Transporte de Contexto**: Verifica se as descobertas de uma etapa estão disponíveis para as etapas subsequentes de raciocínio.
- **Loops de Refinamento**: Permite que o usuário refine os resultados da busca com instruções de acompanhamento sem perder o progresso.

### 5. Formatação de Resposta (15 testes)

Foca na apresentação de dados no terminal para garantir que sejam legíveis e úteis.

- **Integração de Linguagem Natural**: Incorpora dados estruturados em respostas fluídas e úteis.
- **Highlighting de Código**: Garante que trechos de código sejam retornados com realce de sintaxe adequado e números de linha.
- **Sumarização**: Fornece resumos concisos por padrão com opções para ver os detalhes completos.

## SLAs de Performance

A tabela a seguir resume as metas de performance para a integração com a CLI.

| Cenário                          | Latência Alvo |
| :------------------------------- | :------------ |
| **Busca Simples**                | < 500ms       |
| **Análise Complexa**             | < 2s          |
| **Tempo de Resposta ao Usuário** | < 3s (total)  |
| **Tratamento de Erros**          | < 1s          |

## Critérios de Aceitação

| Critério                          | Alvo |
| :-------------------------------- | :--- |
| **Precisão de Decisão**           | 90%+ |
| **Taxa de Sucesso de Ferramenta** | 99%+ |
| **Qualidade de Formatação**       | 95%+ |
| **Recuperação de Erros**          | 100% |
| **Zero Crashes**                  | 100% |

## External Linking

| Concept        | Resource                             | Link                                                                                   |
| -------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **MCP**        | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK** | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **Gemini AI**  | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API** | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **JSON-RPC**   | JSON-RPC 2.0 Specification           | [www.jsonrpc.org/specification](https://www.jsonrpc.org/specification)                 |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
