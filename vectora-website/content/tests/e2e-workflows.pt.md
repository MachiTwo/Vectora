---
title: "Suite de Testes: Workflows Ponta-a-Ponta"
slug: e2e-workflows
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - auth
  - concepts
  - e2e
  - embeddings
  - errors
  - gemini
  - integration
  - mcp
  - mongodb-atlas
  - persistence
  - protocol
  - system
  - testing
  - tools
  - vector-search
  - vectora
  - workflows
---

{{< lang-toggle >}}

Workflows completos ponta-a-ponta devem funcionar corretamente desde a inicialização até o resultado final, passando por múltiplos componentes e integrações sem falhas. Esta suite valida cenários reais de usuário através de toda a stack do Vectora, garantindo que o sistema se comporte como esperado para o usuário final.

Ao testar o ciclo de vida completo de uma requisição, garantimos que os componentes individuais interajam corretamente e atendam às nossas metas de performance.

**Cobertura**: 100+ testes | **Prioridade**: ALTA

## Fluxo Completo Gemini CLI

Garante que os usuários possam interagir com o Vectora de forma transparente através da interface de linha de comando do Gemini.

- Inicialização da CLI e autenticação (8 testes)
- Consulta do contexto do Vectora através do Gemini (10 testes)
- Persistência de conversas multi-turn (8 testes)
- Consciência de contexto entre reinicializações de sessão (8 testes)
- Recuperação graciosa de erros em falhas de rede (5 testes)

**SLA**: Resposta completa de consulta em < 3 segundos.

## Workflow da Extensão VS Code

Valida a experiência no ambiente de desenvolvimento integrado, garantindo que as ferramentas estejam disponíveis exatamente onde o código está.

- Inicialização da extensão e carregamento da barra lateral (8 testes)
- Seleção de código e busca contextual (10 testes)
- Exibição de resultados inline e navegação (8 testes)
- Aplicação de melhorias/refatorações sugeridas (8 testes)
- Workflows abrangendo múltiplos arquivos abertos (8 testes)

**SLA**: Resultados exibidos em < 500ms a partir da seleção.

## Fluxo do Protocolo MCP

Testa a confiabilidade da implementação do Model Context Protocol para integração com agentes externos.

- Conexão do cliente e estabelecimento de sessão (8 testes)
- Listagem de ferramentas e validação de schema (5 testes)
- Invocação de ferramentas com vários conjuntos de parâmetros (10 testes)
- Entrega de resultados e serialização (8 testes)
- Tratamento de erros JSON-RPC e conformidade com o protocolo (8 testes)

**SLA**: Resposta de invocação de ferramenta em < 1 segundo.

## Fluxo de Persistência & Sync de Dados

Garante que os dados sejam gerenciados corretamente entre os ambientes local e cloud.

- Criação de embeddings e armazenamento local (10 testes)
- Lógica de hit/miss de cache local (8 testes)
- Sincronização em background para o MongoDB Atlas (8 testes)
- Capacidade de consulta offline e reconciliação posterior (8 testes)

**SLA**: Sincronização completa em < 5s para mais de 100 documentos.

## Consultas Complexas Multi-etapa

Testa a habilidade do sistema em lidar com requisições avançadas que exigem a coordenação entre múltiplas ferramentas.

- Análise profunda de dependências e visualização (8 testes)
- Descoberta de testes relacionados para blocos de código específicos (8 testes)
- Geração automática de documentação a partir do contexto (8 testes)
- Sugestões de melhoria baseadas em padrões do projeto (8 testes)

**SLA**: Resultados de consultas complexas entregues em < 2 segundos.

## SLAs de E2E (Acordos de Nível de Serviço)

A tabela a seguir resume nossas metas de performance para os principais workflows de usuário.

| Workflow                      | Alvo            |
| :---------------------------- | :-------------- |
| **Consulta CLI**              | < 3s (total)    |
| **Busca VS Code**             | < 500ms         |
| **Chamada de Ferramenta MCP** | < 1s            |
| **Sync de Cache**             | < 5s (100 docs) |
| **Consulta Complexa**         | < 2s            |

## Abordagem de Testes & Cenários

Nossos testes de E2E cobrem tanto cenários de "happy path" quanto vários casos de borda para garantir a robustez.

- **Ferramentas Utilizadas**: Testes de integração com provedores mockados, testes de UI com Playwright para o VS Code e testes de conformidade JSON-RPC para o MCP.
- **Cenários**:
  - Falhas parciais (ex: um componente secundário offline).
  - Conectividade de rede intermitente.
  - Tokens de autenticação expirados ou inválidos.
  - Tratamento de esgotamento de limites de taxa e quotas.
  - Modificações de dados concorrentes e resolução de conflitos.

## External Linking

| Concept           | Resource                             | Link                                                                                                       |
| ----------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation    | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **MCP**           | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**    | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |
| **Gemini AI**     | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)                       |
| **Gemini API**    | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                                           |
| **JSON-RPC**      | JSON-RPC 2.0 Specification           | [www.jsonrpc.org/specification](https://www.jsonrpc.org/specification)                                     |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
