---
title: Implantação
slug: deployment
date: "2026-04-18T22:30:00-03:00"
type: docs
tags:
  - adk
  - agents
  - ai
  - chatgpt
  - claude
  - cloud
  - concepts
  - config
  - deployment
  - docker
  - embeddings
  - gemini
  - go
  - integration
  - mcp
  - mongodb
  - mongodb-atlas
  - openai
  - persistence
  - plugins
  - rag
  - reference
  - reranker
  - vector-search
  - vectora
  - voyage
---

{{< lang-toggle >}}

O Vectora foi projetado para ser implantado de forma flexível, desde máquinas locais até instâncias gerenciadas em nuvem (Fly.io).

O binário `vectora-cloud` é otimizado para ambientes de container, removendo dependências de interface gráfica e focando na performance da API e do motor de busca.

## Opções de Infraestrutura

Escolha a base tecnológica para rodar ou distribuir o motor principal do Vectora:

- [**Fly.io**](./flyio.md): Recomendado para produção em nuvem com auto-scaling.
- [**Docker**](./docker.md): Ideal para ambientes isolados e suporte a Desktop em container.
- [**Homebrew**](./homebrew.md): Instalação e gestão nativa para usuários de macOS.
- [**GitHub Releases**](./github-releases.md): Binários manuais para Windows, Linux e macOS.
- **Binário Nativo**: Para uso local direto via CLI e Systray (Desktop).

## Implantação de Integrações

Cada integração do Vectora possui seu próprio fluxo de deploy e publicação:

- [**VS Code**](./vscode.md): Publicação no Visual Studio Marketplace e Open VSX.
- [**ChatGPT**](./chatgpt.md): Configuração de Plugin e Manifest para OpenAI.
- [**Claude**](./claude.md): Integração via MCP e registro no Claude Desktop.
- [**Codex**](./codex.md): Implantação do adaptador de compatibilidade via NPM.
- [**Gemini**](./gemini.md): Deploy da bridge de contexto no Google Cloud Run.

## Requisitos de Infraestrutura

Para uma implantação estável, certifique-se de ter:

- **MongoDB Atlas**: Recomendado para persistência de vetores e metadados.
- **Chaves de API**: `GOOGLE_API_KEY` (Gemini) e `VOYAGE_API_KEY` (Voyage AI).
- **Vectora Cognitive Runtime (ONNX Runtime)**: O motor de decisão requer o runtime ONNX para inferência local de baixa latência.
- **Recursos**: Mínimo de 512MB RAM e 0.5 CPU por instância.

## External Linking

| Concept               | Resource                            | Link                                                                                                       |
| --------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**     | Atlas Vector Search Documentation   | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **Anthropic Claude**  | Claude Documentation                | [docs.anthropic.com/](https://docs.anthropic.com/)                                                         |
| **Voyage AI**         | High-performance embeddings for RAG | [www.voyageai.com/](https://www.voyageai.com/)                                                             |
| **Voyage Embeddings** | Voyage Embeddings Documentation     | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)                             |
| **Voyage Reranker**   | Voyage Reranker API                 | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)                                 |
| **Docker**            | Docker Documentation                | [docs.docker.com/](https://docs.docker.com/)                                                               |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
