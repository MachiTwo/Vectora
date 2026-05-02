---
title: "Infrastructure: Camada de Suporte"
slug: infrastructure
date: 2026-04-25T23:00:00-03:00
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - concepts
  - embeddings
  - guardian
  - infrastructure
  - mongodb-atlas
  - multi-tenant
  - persistence
  - privacy
  - rag
  - reranker
  - security
  - state
  - system
  - trust-folder
  - vector-search
  - vectora
  - voyage
draft: false
---

{{< lang-toggle >}}

A Infrastructure representa tudo o que é necessário para "rodar o Vectora" — armazenamento, isolamento de dados, segurança e persistência. É a base que permite que o Core e o Search funcionem de forma confiável e segura.

Ao fornecer um ambiente robusto e escalável, a camada de infraestrutura garante que seus dados estejam sempre acessíveis, protegidos e devidamente contextualizados.

## Componentes Principais

A infraestrutura é construída sobre vários componentes fundamentais que gerenciam o ciclo de vida dos dados e o controle de acesso.

### Namespaces

Isolamento multi-tenant em nível de índice vetorial. Cada namespace do usuário contém seus próprios projetos (workspaces), impedindo a contaminação cruzada de dados e garantindo privacidade estrita.

**Saiba como**: [→ Namespaces](./namespaces.md)

### State Persistence

Memória de curto prazo (iterações atuais) e longo prazo (histórico no MongoDB Atlas). Garante que o Vectora "lembre" do contexto da conversa e dos aprendizados acumulados ao longo do tempo.

**Saiba como**: [→ State Persistence](./state-persistence.md)

### Trust Folder

Sandbox de sistema de arquivos com prevenção de directory traversal, vazamento de segredos e validação de caminhos. O componente Guardian valida cada tentativa de acesso.

**Saiba como**: [→ Trust Folder](./trust-folder.md)

## Arquitetura de Armazenamento

O Vectora utiliza um modelo de armazenamento hierárquico para organizar os dados de forma eficiente e segura.

```text
MongoDB Atlas
├── Namespaces (isolamento multi-tenant)
│   ├── Vetores (Voyage 4, HNSW indexado)
│   ├── Metadados (AST, dependências, idioma)
│   ├── Estado operacional (sessões, memória)
│   └── Logs de auditoria (compliance, rastreabilidade)
```

## External Linking

| Concept               | Resource                            | Link                                                                                                       |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**     | Atlas Vector Search Documentation   | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **AST Parsing**       | Tree-sitter Official Documentation  | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **Voyage AI**         | High-performance embeddings for RAG | [www.voyageai.com/](https://www.voyageai.com/)                                                             |
| **Voyage Embeddings** | Voyage Embeddings Documentation     | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)                             |
| **Voyage Reranker**   | Voyage Reranker API                 | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)                                 |
| **Secure Coding**     | OWASP Secure Coding Practices       | [owasp.org/www-project-secure-coding-practices/](https://owasp.org/www-project-secure-coding-practices/)   |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
