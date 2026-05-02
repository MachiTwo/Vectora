---
title: "Docker"
slug: docker
date: "2026-04-18T22:30:00-03:00"
type: docs
tags:
  - ai
  - build
  - cloud
  - concepts
  - deployment
  - docker
  - guardian
  - mcp
  - mongodb-atlas
  - protocol
  - security
  - system
  - tools
  - trust-folder
  - vector-search
  - vectora
  - yaml
---

{{< lang-toggle >}}

O Docker é a maneira mais simples de rodar o Vectora Cloud em um ambiente isolado ou em servidores que não possuem o runtime Go instalado. Para usuários do Vectora Desktop, recomenda-se instalar o binário diretamente em sua máquina.

O uso de containers garante consistência entre diferentes ambientes e simplifica o gerenciamento de dependências como o MongoDB.

> [!NOTE] > **Imagens Docker são primordialmente para o Vectora Cloud**. O Vectora Desktop é instalado como um binário local (CLI `vectora` + Systray). Se você deseja rodá-lo em Docker para testes de desenvolvimento local, use a imagem `vectora:dev-desktop` (beta).

## Imagens Oficiais

O projeto mantém três tipos de imagens Docker, cada uma otimizada para casos de uso específicos.

1. **`vectora-cloud:latest`**: Otimizada para APIs de nuvem e Servidores MCP HTTP. Utiliza acesso a dados apenas via MongoDB e é destinada a ambientes de PRODUÇÃO.
2. **`vectora-cloud:dev`**: Uma versão de desenvolvimento com logs detalhados e recursos de recarregamento automático.
3. **`vectora:dev-desktop`** (beta): Modo desktop para testes em um ambiente de container (não recomendado para uso em produção).
4. **`vectora-cloud:managed`**: Versão premium que inclui modelos SmolLM pré-carregados para o Vectora Cognitive Runtime.

> [!IMPORTANT] > **Runtime ONNX**: Todas as imagens oficiais do Vectora incluem o runtime ONNX necessário para o funcionamento do **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)**. Isso permite que o cérebro tático realize inferências locais dentro do container sem chamadas externas.

## Rodando Vectora Cloud com Docker Compose

A maneira recomendada para rodar o Vectora Cloud localmente com todas as suas dependências é usando o Docker Compose. Isso permite que você gerencie o serviço Vectora e o banco de dados MongoDB como uma única unidade.

```yaml
version: "3.8"
services:
  vectora-cloud:
    image: vectora-cloud:latest
    ports:
      - "8080:8080"
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - VOYAGE_API_KEY=${VOYAGE_API_KEY}
      - VECTORA_DB_URL=mongodb://mongo:27017/vectora
      - VECTORA_MODE=cloud
    depends_on:
      - mongo
  mongo:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db
volumes:
  mongo-data:
```

## Guia de Seleção de Imagem

Escolha a imagem apropriada com base na sua estratégia de deploy e requisitos de acesso a dados.

| Caso de Uso               | Imagem                 | Protocolo         | Armazenamento de Dados |
| :------------------------ | :--------------------- | :---------------- | :--------------------- |
| **Produção em Nuvem**     | `vectora-cloud:latest` | Servidor MCP HTTP | MongoDB Atlas          |
| **Desenvolvimento Local** | `vectora-cloud:dev`    | HTTP + stdio      | MongoDB Local          |
| **Desktop em Container**  | `vectora:dev-desktop`  | MCP stdio         | Filesystem + BadgerDB  |

## Build Manual

Você pode construir as imagens localmente usando o `Makefile` fornecido. Certifique-se de estar na raiz do repositório antes de executar estes comandos.

```bash
# Construir a imagem Cloud
make docker-build-cloud

# Construir a imagem Desktop dev
make docker-build-desktop
```

## Diferenças Principais entre os Modos

O Vectora opera de forma diferente dependendo se está implantado no modo Cloud ou Desktop.

### Modo Vectora Cloud (Servidor HTTP)

No modo Cloud, o Vectora roda como um Servidor MCP HTTP na porta 8080. Ele interage exclusivamente com o MongoDB para armazenamento de dados e fornece ferramentas para gerenciamento de workspace e busca semântica. A segurança é imposta através da API Guardian e isolamento estrito de namespaces.

### Modo Vectora Desktop (Cliente stdio)

O modo Desktop roda como um cliente MCP stdio, acessando o sistema de arquivos local e usando o BadgerDB para cache. Ele fornece ferramentas para E/S de arquivos, globbing e comandos de shell locais. A segurança é gerenciada via sistema Trust Folder.

## External Linking

| Concept           | Resource                             | Link                                                                                                       |
| ----------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation    | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **Docker**        | Docker Documentation                 | [docs.docker.com/](https://docs.docker.com/)                                                               |
| **MCP**           | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                     |
| **MCP Go SDK**    | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                         |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
