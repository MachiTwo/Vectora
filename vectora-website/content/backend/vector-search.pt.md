---
title: Busca Vetorial
slug: vector-search
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - concepts
  - embeddings
  - mongodb-atlas
  - rag
  - reranker
  - security
  - vector-search
  - vectora
  - voyage
---

{{< lang-toggle >}}

A busca vetorial é o mecanismo central que permite ao Vectora recuperar contexto semanticamente relevante em bases de código complexas. Diferente das buscas textuais tradicionais baseadas em palavras-chave, a busca vetorial opera no espaço semântico, capturando a similaridade funcional entre conceitos de código.

Ao transformar trechos de código em vetores matemáticos, conseguimos encontrar relações que vão além da sintaxe literal, identificando lógicas equivalentes escritas de formas diferentes.

## Fundamentos de Busca Vetorial

O processo de busca vetorial no Vectora segue um pipeline rigoroso para garantir precisão e velocidade.

1. **Embedding**: O código é transformado em vetores numéricos usando o modelo `voyage-4`.
2. **Indexação**: Os vetores são armazenados no MongoDB Atlas com um índice HNSW (Hierarchical Navigable Small World).
3. **Consulta**: A query do usuário é convertida em embedding e comparada contra o índice.
4. **Filtragem**: Os resultados são filtrados por namespace e metadados antes de serem entregues ao agente.

```mermaid
graph LR
    A[Código Fonte] --> B[Parser AST + Chunking]
    B --> C[Embedding via Voyage 4]
    C --> D[Índice HNSW no MongoDB Atlas]
    E[Query do Usuário] --> F[Embedding da Query]
    F --> D
    D --> G[Filtragem por Namespace]
    G --> Vectora Cognitive Runtime[Vectora Cognitive Runtime: Tactical Validation]
    Vectora Cognitive Runtime --> H[Contexto para o LLM]
```

O **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** intercepta os resultados da busca vetorial para realizar uma **Validação Tática** (meta-cognição). Ele analisa se os snippets recuperados são de fato relevantes para a intenção do usuário, descartando ruídos e prevenindo alucinações de contexto antes da injeção na LLM.

## Por Que Busca Vetorial para Código

Buscas lexicais falham em cenários de engenharia de software porque termos como `validateToken` e `checkJWT` são semanticamente idênticos, mas textualmente diferentes.

Especialmente com o modelo `voyage-4`, capturamos:

- **Similaridade funcional**: Implementações diferentes que resolvem o mesmo problema.
- **Padrões arquiteturais**: Relações entre serviços, controladores e modelos.
- **Contexto semântico**: O significado real por trás de comentários e docstrings.

## Arquitetura de Busca no Vectora

Utilizamos o MongoDB Atlas como backend unificado para vetores e metadados, garantindo consistência atômica e alta escalabilidade.

| Componente          | Implementação               | Benefício                            |
| :------------------ | :-------------------------- | :----------------------------------- |
| **Índice Vetorial** | HNSW com métrica de cosseno | Busca ANN com latência sub-50ms      |
| **Filtragem**       | Payload filtering nativo    | Isolamento estrito entre namespaces  |
| **Escalabilidade**  | Sharding automático         | Suporta bilhões de vetores de código |

## Pipeline de Indexação

Antes da indexação, o Vectora realiza um **Chunking Guiado por AST** usando Tree-sitter para identificar unidades semânticas coerentes, como funções e classes inteiras, evitando quebras no meio da lógica.

### Geração de Embeddings

Cada chunk é processado pela API do Voyage AI, gerando um vetor de 1024 dimensões otimizado para compreensão de código. Esses vetores são então inseridos no Atlas em operações atômicas junto com seus metadados estruturais.

### Fluxo de Consulta

Quando um agente solicita contexto, a query passa por um cache de embeddings antes de atingir o MongoDB. O parâmetro `ef_search` é ajustado dinamicamente: queries de refatoração crítica usam precisão máxima, enquanto navegação geral prioriza latência.

## Isolamento e Segurança

O isolamento por namespace é garantido no nível da consulta vetorial. Todas as buscas incluem filtros obrigatórios que impedem que dados de projetos diferentes se misturem, mesmo em ambientes multi-tenant.

## External Linking

| Concept               | Resource                                                 | Link                                                                                                       |
| --------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**     | Atlas Vector Search Documentation                        | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **AST Parsing**       | Tree-sitter Official Documentation                       | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **Voyage AI**         | High-performance embeddings for RAG                      | [www.voyageai.com/](https://www.voyageai.com/)                                                             |
| **Voyage Embeddings** | Voyage Embeddings Documentation                          | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)                             |
| **Voyage Reranker**   | Voyage Reranker API                                      | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)                                 |
| **HNSW**              | Efficient and robust approximate nearest neighbor search | [arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)                                               |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
