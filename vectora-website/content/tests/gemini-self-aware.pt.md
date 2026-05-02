---
title: "Suite de Testes: Auto-consciência do Gemini"
slug: gemini-self-aware-tests
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - ast-parsing
  - concepts
  - config
  - context-engine
  - errors
  - gemini
  - knowledge
  - mcp
  - protocol
  - rag
  - system
  - testing
  - tools
  - vectora
---

{{< lang-toggle >}}

O Gemini deve ser completamente auto-consciente do Vectora: conhecendo sua identidade, capacidades, documentação pública e sabendo quando usar o Vectora para resolver problemas complexos. Esta suite garante que o Gemini funcione como um especialista integrado dentro do ecossistema Vectora, fornecendo assistência precisa e contextual.

Ao verificar esta auto-consciência, garantimos que a IA não seja apenas um executor de ferramentas, mas um parceiro conhecedor que entende os pontos fortes e limitações do sistema.

**Cobertura**: 60+ testes | **Prioridade**: CRÍTICA

## Princípio Central

> **"O Gemini não é apenas um cliente que chama o Vectora. O Gemini ENTENDE o Vectora como uma ferramenta superior e sabe exatamente quando e como usá-lo."**

## Segmentos de Testes

As seções a seguir detalham os casos de teste específicos e os cenários cobertos por esta suite.

### 1. Identidade & Descrição (10 testes)

Garante que o Gemini possa descrever com precisão o que é o Vectora e como ele se encaixa no panorama mais amplo de desenvolvimento de software.

- **Descrição de Identidade**: Valida que o Gemini identifica o Vectora como um motor de busca semântica para código com análise de dependências e suporte a múltiplos LLMs.
- **Conhecimento Comparativo**: Verifica se o Gemini pode explicar as diferenças entre o Vectora e ferramentas de busca de propósito geral como Elasticsearch ou grep.
- **Princípios Fundamentais**: Verifica a consciência dos valores centrais do Vectora, como "experiência local-first" e "caching híbrido inteligente".

### 2. Capacidades & Funcionalidades (15 testes)

Testa o conhecimento do Gemini sobre as funcionalidades técnicas específicas e ferramentas disponíveis dentro da plataforma Vectora.

- **Consciência de Features Core**: Lista e explica as capacidades de Context Engine, Hybrid Search, Reranking e parsing AST.
- **Conhecimento de Ferramentas**: Verifica se o Gemini está familiarizado com as ferramentas MCP disponíveis (`search_context`, `analyze_dependencies`, etc.) e seu uso pretendido.
- **Orientação de Configuração**: Garante que o Gemini possa fornecer instruções corretas para configurar variáveis de ambiente e arquivos de configuração.

### 3. Conhecimento da Documentação (15 testes)

Valida que o Gemini possa citar a documentação oficial corretamente e guiar os usuários para os recursos certos.

- **Acesso a Recursos**: Garante que o Gemini saiba onde o site oficial e o repositório GitHub estão localizados.
- **Citação Precisa**: Verifica se o Gemini pode fornecer URLs de fonte e mencionar versões/timestamps específicos ao explicar uma funcionalidade.
- **Proficiência no Guia de Setup**: Verifica se o Gemini pode guiar um usuário através de um processo completo de instalação e configuração inicial.

### 4. Inteligência de Decisão (15 testes)

Foca na habilidade da IA em recomendar o Vectora no momento certo com base na tarefa do usuário.

- **Lógica de Recomendação**: O Gemini deve sugerir o uso do Vectora para tarefas de navegação de código, investigação de bugs e mapeamento de dependências.
- **Lógica de Rejeição**: Garante que o Gemini não mencione o Vectora desnecessariamente para consultas não relacionadas a código.
- **Reconhecimento de Erros**: Valida que o Gemini possa detectar chamadas de ferramentas malformadas e sugerir a sintaxe correta baseada na documentação.

### 5. Cenários de Integração (10 testes)

Simula fluxos de trabalho complexos onde o Gemini usa o Vectora para fornecer análises e sugestões de alto nível.

- **Code Review**: O Gemini usa o Vectora para encontrar padrões similares e comparar o snippet do usuário com as melhores práticas do projeto.
- **Investigação de Bugs**: Busca por bugs históricos similares e analisa dependências relacionadas para fornecer um diagnóstico.
- **Geração de Documentação**: Examina padrões de projeto existentes para gerar documentação consistente e precisa para novas funções.

## Critérios de Aceitação

| Critério                                    | Alvo                    |
| :------------------------------------------ | :---------------------- |
| **Precisão da Descrição**                   | 100%                    |
| **Precisão do Conhecimento de Ferramentas** | > 90%                   |
| **Citação de Documentação**                 | 100% quando relevante   |
| **Inteligência de Decisão**                 | 90%+ de acurácia        |
| **Zero Alucinação**                         | 100% em funcionalidades |

## External Linking

| Concept         | Resource                                                   | Link                                                                                   |
| --------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Gemini AI**   | Google DeepMind Gemini Models                              | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**  | Google AI Studio Documentation                             | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **AST Parsing** | Tree-sitter Official Documentation                         | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)       |
| **MCP**         | Model Context Protocol Specification                       | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**  | Go SDK for MCP (mark3labs)                                 | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **RAG**         | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                           |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
