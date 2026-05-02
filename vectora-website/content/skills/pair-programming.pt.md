---
title: "Skill: Pair Programming"
slug: pair-programming
date: "2026-04-24T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - agents
  - ai
  - architecture
  - ast-parsing
  - auth
  - concepts
  - config
  - embeddings
  - gemini
  - guardian
  - mcp
  - pair-programming
  - protocol
  - rag
  - security
  - skills
  - tools
  - vectora
  - voyage
  - yaml
---

{{< lang-toggle >}}

A Skill de Pair Programming transforma o Vectora em um validador de código inteligente que trabalha em tempo real ao lado do modelo principal. Enquanto o Claude ou o Gemini escreve código, o Vectora auxilia, valida contra a base de código existente e sugere melhorias — criando uma verdadeira parceria colaborativa entre dois agentes.

Ao atuar como navegador e revisor, o Vectora garante que o código gerado pela IA adira aos padrões do projeto e às melhores práticas.

## Conceito: Vectora como Code Reviewer

O Vectora monitora o processo de geração de código e fornece feedback imediato com base no contexto histórico do projeto e nas regras definidas.

```text
Claude: "Preciso autenticar usuários via JWT."
  ↓
Claude gera código de autenticação.
  ↓
Vectora (Pair Programming Skill):
   Valida sintaxe Go.
   Detecta 3 padrões similares em internal/auth/.
   Aviso: Falta chamada para Guardian.ValidateAccess().
   Sugestão: Use a função existente em internal/auth/guardian.go.
   Refator: Extrair validateToken() como uma função reutilizável.
   Resultado: Código aprovado com sugestões.
```

## Métodos de Ativação

Você pode utilizar a skill de Pair Programming através de chamadas explícitas de ferramentas ou monitoramento automatizado em background.

### Ferramenta MCP Explícita

O modelo principal pode invocar a skill diretamente fornecendo o snippet de código e o contexto.

```text
Claude: /pair_programming {language} {code_snippet}
```

### Integração Automática

O Vectora pode ser configurado para acionar a skill automaticamente sempre que a geração ou refatoração de código for detectada.

```yaml
skills:
  pair_programming:
    enabled: true
    auto_mode: true
    validation_level: "strict"
```

## Dimensões de Validação

A skill realiza uma análise multi-camada do código proposto para garantir alta qualidade e consistência.

### 1. Conformidade com Padrões

O Vectora compara o novo código com padrões estabelecidos no repositório para evitar duplicação e garantir consistência na nomenclatura e estrutura.

### 2. Validação de Arquitetura em Camadas

Garante que o código respeite a hierarquia de dependências do projeto. Por exemplo, verifica se a lógica core não depende acidentalmente das camadas de API ou servidor.

### 3. Checklist de Segurança

Toda função que toca em dados sensíveis é verificada quanto à sanitização de input, logs seguros (sem credenciais em logs) e controle de acesso adequado através do módulo Guardian.

### 4. Detecção de Código Duplicado

Identifica se uma lógica similar já existe em outro lugar do projeto, sugerindo a reutilização de funções existentes em vez de criar implementações redundantes.

### 5. Revisão de Dependências

Analisa novas dependências externas e sugere alternativas nativas ou já existentes no projeto para manter o grafo de dependências limpo.

## Fluxo de Interação

Quando um snippet de código é submetido, a skill retorna um relatório de análise abrangente.

1. **Checagem de Sintaxe**: Validação básica da correção do código para a linguagem especificada.
2. **Padrões Similares**: Lista de arquivos e linhas existentes que implementam lógica similar.
3. **Checagem de Arquitetura**: Validação do isolamento de camadas e regras de dependência.
4. **Avisos de Segurança**: Identificação de potenciais vulnerabilidades ou validações ausentes.
5. **Sugestões de Refatoração**: Conselhos acionáveis sobre como melhorar a estrutura do código.

## Configuração do Projeto

A skill de Pair Programming pode ser personalizada no arquivo `vectora.config.yaml` para atender aos requisitos específicos do seu projeto.

```yaml
# vectora.config.yaml
skills:
  pair_programming:
    enabled: true
    checks:
      syntax: true
      architecture: true
      security: true
      duplicates: true
    refactoring:
      suggest_extractions: true
    similar_patterns:
      threshold: 0.85
```

## External Linking

| Concept              | Resource                             | Link                                                                                   |
| -------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **Anthropic Claude** | Claude Documentation                 | [docs.anthropic.com/](https://docs.anthropic.com/)                                     |
| **MCP**              | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**       | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **AST Parsing**      | Tree-sitter Official Documentation   | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)       |
| **Gemini AI**        | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**       | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
