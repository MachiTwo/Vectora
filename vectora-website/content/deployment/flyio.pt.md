---
title: "Fly.io"
slug: flyio
date: "2026-04-27T10:00:00-03:00"
type: docs
tags:
  - ai
  - chatgpt
  - cloud
  - concepts
  - config
  - deployment
  - embeddings
  - flyio
  - gemini
  - integration
  - mcp
  - mongodb-atlas
  - persistence
  - protocol
  - rag
  - reference
  - security
  - vector-search
  - vectora
  - voyage
---

{{< lang-toggle >}}

O Fly.io é a plataforma recomendada para implantar o Vectora Cloud devido à sua baixa latência global e suporte nativo a containers Docker. Esta opção de implantação é exclusiva para a versão Cloud do Vectora, permitindo que você execute um servidor MCP gerenciado com escalonamento automático.

Ao implantar no Fly.io, o Vectora aproveita a infraestrutura de borda para garantir que as buscas vetoriais e o processamento de contexto sejam executados o mais próximo possível dos seus usuários ou da sua infraestrutura de CI/CD.

## Visão Geral da Implantação

A implantação no Fly.io utiliza o arquivo `fly.toml` para definir a configuração do serviço e o comando `fly deploy` para enviar a imagem Docker para os servidores da plataforma.

Diferente do modo Desktop, a instância Fly.io opera como um servidor MCP via HTTP, exigindo uma conexão ativa com o MongoDB Atlas para persistência de dados e armazenamento de vetores.

## Configuração do fly.toml

O arquivo `fly.toml` na raiz do projeto deve ser configurado para expor a porta 8080, que é a porta padrão onde o Vectora Cloud escuta as conexões MCP.

```toml
app = "vectora-cloud"
primary_region = "gru"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 1
  processes = ["app"]

[env]
  VECTORA_MODE = "cloud"
```

## Secrets e Segurança

Como o Vectora depende de provedores de IA (Google Gemini e Voyage AI), você deve configurar as chaves de API como segredos no Fly.io para garantir que elas não fiquem expostas no código-fonte.

Use o comando `fly secrets set` para configurar as variáveis obrigatórias:

```bash
fly secrets set GOOGLE_API_KEY=sua_chave_aqui
fly secrets set VOYAGE_API_KEY=sua_chave_aqui
fly secrets set VECTORA_DB_URL=mongodb+srv://user:pass@cluster.mongodb.net/vectora
```

## Processo de Deploy

Uma vez que as chaves de API e a URL do banco de dados estejam configuradas, você pode realizar o deploy da aplicação. O Fly.io construirá a imagem Docker usando o `Dockerfile` presente na raiz do repositório.

```bash
# Iniciar a configuração do app (apenas na primeira vez)
fly launch

# Realizar o deploy da nova versão
fly deploy
```

Após o deploy, sua instância do Vectora Cloud estará disponível em `https://vectora-cloud.fly.dev`, pronta para receber conexões de integrações como o VS Code ou o ChatGPT.

## External Linking

| Concept           | Resource                             | Link                                                                                                       |
| ----------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation    | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **MCP**           | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**    | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |
| **Gemini AI**     | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)                       |
| **Gemini API**    | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                                           |
| **Docker**        | Docker Documentation                 | [docs.docker.com/](https://docs.docker.com/)                                                               |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
