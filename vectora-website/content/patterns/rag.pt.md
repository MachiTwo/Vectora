---
title: "Connected RAG: O Poder do Contexto Estruturado"
slug: rag
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - auth
  - concepts
  - config
  - context-engine
  - embeddings
  - rag
  - reranker
  - system
  - vectora
  - voyage
---

{{< lang-toggle >}}

Você já perguntou a um agente de IA sobre uma função no seu projeto e ele respondeu algo que parecia certo, mas que ignorava completamente como aquela função era usada no resto do sistema? Isso é o sintoma clássico do **RAG fragmentado**.

O Vectora resolve esse problema através do **Connected RAG**, uma abordagem que não apenas busca trechos de texto, mas reconstrói as relações lógicas e estruturais do seu código antes de enviá-las ao modelo de linguagem.

## O que é RAG?

O RAG (Retrieval-Augmented Generation) é a técnica de fornecer dados externos (como seus arquivos de código) para um LLM no momento da pergunta. Em vez de o modelo "adivinhar" baseado no que aprendeu no treino, ele consulta seus documentos e responde baseado neles.

```text
Consulta ("Como autenticar?")
    ↓
Recuperação (Busca na base de código)
    ↓
Aumentação (Enriquece o prompt com contexto)
    ↓
Geração (LLM responde com base no contexto)
```

Embora pareça perfeito, o RAG tradicional é perigoso quando aplicado ao desenvolvimento de software, pois ignora a natureza interconectada do código.

## O Problema: RAG Tradicional vs. Código

Diferente de documentos de texto simples, o código possui dependências implícitas e fluxos de dados que não podem ser capturados apenas por similaridade semântica de palavras.

| Aspecto       | RAG Tradicional                | Problema para Código                       |
| :------------ | :----------------------------- | :----------------------------------------- |
| **Busca**     | Similaridade semântica simples | Ignora dependências e referências cruzadas |
| **Contexto**  | Fragmentos isolados de texto   | LLM não vê o fluxo de execução completo    |
| **Resultado** | "Top 5 blocos de texto"        | O modelo perde a visão arquitetural        |
| **Precisão**  | Adequada para documentos       | Frequentemente gera código incompleto      |

No RAG tradicional, se você busca por "login", o sistema pode retornar a função `loginUser`, mas esquecer do middleware de autenticação, dos testes unitários e da configuração de segredos necessária para que a função funcione.

## A Solução: Connected RAG (Context Engine)

No Vectora, o RAG é orquestrado por um **Context Engine** que entende a árvore de decisão e a estrutura do projeto.

### 1. Busca Multimodal

Combinamos três estratégias diferentes para garantir que nada seja esquecido:

- **Embeddings (Voyage 4)**: Captura a intenção semântica da consulta.
- **AST Analysis**: Utiliza o Tree-sitter para entender a estrutura sintática (quem chama quem).
- **Keyword Grep**: Garante que termos técnicos específicos sejam localizados com precisão.

### 2. Multi-hop Reasoning

O motor de contexto não faz apenas uma busca. Ele realiza "saltos" lógicos para encontrar informações relacionadas. Se a busca inicial encontra uma interface, o motor automaticamente busca suas implementações e dependências, reconstruindo o grafo de conhecimento necessário para a tarefa.

### 3. Composição Estruturada

O contexto retornado ao agente não é apenas uma lista de strings. É um objeto organizado contendo o arquivo principal, suas dependências diretas, locais de uso e testes relacionados, permitindo que o LLM tome decisões com consciência arquitetural.

## Por que o Connected RAG importa?

Quando o contexto é devidamente conectado, os resultados são drasticamente superiores.

- **Redução de Alucinações**: O agente para de inventar imports ou funções que não existem.
- **Economia de Tokens**: Em vez de enviar arquivos inteiros (dump), enviamos apenas os trechos cirúrgicos necessários.
- **Consistência**: As sugestões de refatoração respeitam os padrões de design já estabelecidos no projeto.

## External Linking

| Concept               | Resource                                                   | Link                                                                             |
| --------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **RAG**               | Retrieval-Augmented Generation for Knowledge-Intensive NLP | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)                     |
| **AST Parsing**       | Tree-sitter Official Documentation                         | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/) |
| **Voyage AI**         | High-performance embeddings for RAG                        | [www.voyageai.com/](https://www.voyageai.com/)                                   |
| **Voyage Embeddings** | Voyage Embeddings Documentation                            | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)   |
| **Voyage Reranker**   | Voyage Reranker API                                        | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)       |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
