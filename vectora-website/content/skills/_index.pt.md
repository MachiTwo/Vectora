---
title: "Vectora Skills"
slug: skills
date: "2026-04-24T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - agents
  - ai
  - architecture
  - concepts
  - config
  - gemini
  - integration
  - mcp
  - protocol
  - rag
  - rbac
  - security
  - skills
  - state
  - tools
  - vectora
  - yaml
---

{{< lang-toggle >}}

As Vectora Skills são módulos especializados de comportamento que transformam o Vectora de um simples motor de busca para um copilot inteligente que trabalha ao lado do modelo principal (Claude, Gemini, etc.). Estas skills fornecem análise profunda e validação em tempo real em várias dimensões do desenvolvimento.

Ao utilizar skills especializadas, o Vectora pode fornecer assistência mais direcionada, indo além da busca geral para uma participação ativa no ciclo de vida do desenvolvimento de software.

## O Que é uma Skill?

Uma **Skill** é um padrão de comportamento especializado que o Vectora oferece através de suas ferramentas MCP. Diferente de ferramentas de busca genéricas, as skills são:

- **Cientes de Contexto**: Elas entendem o projeto inteiro, não apenas resultados de busca isolados.
- **Validadores**: Elas checam a qualidade, segurança e performance do código em tempo real.
- **Interativas**: Elas mantêm um diálogo contínuo com o modelo de IA principal.
- **Rastreáveis**: Elas geram relatórios auditáveis de decisões e sugestões.

## As 11 Skills Principais

O Vectora está organizado em onze áreas de skills distintas para fornecer uma cobertura abrangente das tarefas de desenvolvimento.

### 1. [Pair Programming](./pair-programming/)

O Vectora atua como um engenheiro principal, auxiliando e validando o código enquanto ele é escrito.
**Ativação**: `/pair_programming`

### 2. [Enriquecimento de Contexto](./context-enrichment/)

Injeta automaticamente contexto relevante da base de código antes que o modelo gere uma resposta.
**Ativação**: `/enrich_context`

### 3. [Análise de Dependências](./dependency-analysis/)

Analisa relacionamentos entre módulos, detecta ciclos e identifica código órfão.
**Ativação**: `/analyze_dependencies`

### 4. [Auditoria de Segurança](./security-audit/)

Valida o código contra padrões de segurança, detectando segredos e vulnerabilidades.
**Ativação**: `/security_audit`

### 5. [Análise de Performance](./performance-analysis/)

Analisa latência, throughput e uso de recursos para código e consultas.
**Ativação**: `/analyze_performance`

### 6. [Cobertura de Testes](./test-coverage/)

Identifica código não testado e gera sugestões para casos de teste abrangentes.
**Ativação**: `/analyze_test_coverage`

### 7. [Validação de Arquitetura](./architecture-validation/)

Garante que o código adira aos princípios de design (SOLID, Clean Architecture).
**Ativação**: `/validate_architecture`

### 8. [Geração de Documentação](./documentation-generation/)

Gera automaticamente docs técnicos, diagramas Mermaid e ADRs.
**Ativação**: `/generate_documentation`

### 9. [Sugestões de Refatoração](./refactoring-suggestions/)

Analisa o código para sugerir melhorias em manutenibilidade e clareza (DRY).
**Ativação**: `/suggest_refactoring`

### 10. [Avaliação de Risco](./risk-assessment/)

Avalia o impacto potencial e o risco de regressão das mudanças propostas.
**Ativação**: `/assess_risk`

### 11. [Web Search Integration](./web-search/)

Integra busca web em tempo real para pesquisa técnica e consulta de documentações externas.
**Ativação**: `/web_search`

## Arquitetura da Camada de Skills

A camada de skills do Vectora situa-se entre o modelo de IA principal e o motor de busca core.

```mermaid
graph TD
    A["Modelo de IA Principal (Claude/Gemini)"] -- "Protocolo MCP" --> Vectora Cognitive Runtime["Vectora Cognitive Runtime: Tactical Orchestrator"]
    Vectora Cognitive Runtime -- "Seleciona Skill" --> B["Servidor MCP Vectora"]
    subgraph "Camada de Skills"
        B -- "Processa" --> C["Pair Programming"]
        B -- "Processa" --> D["Auditoria de Segurança"]
        B -- "Processa" --> E["Web Search"]
        B -- "Processa" --> F["...Outras Skills"]
    end
    C & D & E & F -- "Consulta" --> G["Vectora Core (Busca, RAG)"]
```

O **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** é o cérebro tático que reside entre o modelo de IA principal e as ferramentas. Ele analisa o prompt do usuário e o estado atual para decidir **qual skill** deve ser ativada, garantindo que o agente use a ferramenta mais precisa para cada tarefa.

## Configuração do Projeto

Habilite e configure skills específicas no seu arquivo `vectora.config.yaml`.

```yaml
skills:
  enabled: true
  pair_programming:
    enabled: true
    validation_level: "strict"
  security_audit:
    enabled: true
    fail_on_critical: true
```

## External Linking

| Concept        | Resource                                                   | Link                                                                                   |
| -------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **MCP**        | Model Context Protocol Specification                       | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK** | Go SDK for MCP (mark3labs)                                 | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **Gemini AI**  | Google DeepMind Gemini Models                              | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API** | Google AI Studio Documentation                             | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **RBAC**       | NIST Role-Based Access Control Standard                    | [csrc.nist.gov/projects/rbac](https://csrc.nist.gov/projects/rbac)                     |
| **RAG**        | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                           |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
