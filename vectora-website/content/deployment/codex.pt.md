---
title: "Codex"
slug: codex
date: "2026-04-27T10:00:00-03:00"
type: docs
tags:
  - ai
  - codex
  - concepts
  - config
  - deployment
  - gemini
  - integration
  - mcp
  - npm
  - openai
  - protocol
  - tools
  - vectora
  - voyage
---

{{< lang-toggle >}}

A integração do Vectora com o OpenAI Codex fornece suporte para modelos legados de análise de código que ainda são utilizados em pipelines de automação específicos. Esta integração atua como um tradutor entre as ferramentas de contexto do Vectora e a interface de completion do Codex, permitindo que scripts antigos aproveitem o novo motor de busca semântica.

A implantação do adaptador Codex é realizada através de um pacote Node.js que encapsula as chamadas de API e garante a compatibilidade de formatos entre os sistemas.

## Suporte Legado e APIs REST

O OpenAI Codex foi um dos pioneiros na análise de código por IA, e muitos sistemas internos ainda dependem de sua estrutura de resposta. O Vectora Cloud expõe um endpoint de compatibilidade que simula o comportamento do Codex, mas utilizando os modelos Gemini e Voyage internamente para maior precisão.

Esta ponte de compatibilidade é implantada como parte do serviço principal do Vectora Cloud, não exigindo infraestrutura adicional além da instância principal.

## Configuração de Endpoint

Para que suas aplicações legadas possam utilizar o Vectora como se fosse o OpenAI Codex, você deve alterar a URL base da API nas suas configurações de SDK. O Vectora emula as rotas `/completions` e `/edits` do Codex original.

```javascript
const openai = new OpenAI({
  apiKey: "VECTORA_TOKEN",
  baseURL: "https://api.vectora.app/v1/adapters/codex",
});
```

## Publicação via NPM

A biblioteca cliente do adaptador Codex para o Vectora é publicada no NPM sob o nome `@kaffyn/vectora-codex-adapter`. Ela fornece helpers para facilitar a migração de código existente para o ecossistema Vectora sem a necessidade de refatorações profundas.

A publicação deste pacote segue o fluxo padrão de integração contínua do Vectora, garantindo que novas funcionalidades do motor de busca sejam expostas de forma segura para o Codex.

## Limitações e Performance

Embora o adaptador forneça uma camada de compatibilidade, recomendamos que novas integrações utilizem diretamente o protocolo MCP ou a API nativa do Gemini. O modo Codex possui limitações inerentes ao seu formato de prompt fixo, o que pode reduzir a eficácia das ferramentas de busca dinâmica.

Em termos de performance, a camada de tradução adiciona uma latência mínima (<20ms), tornando-a viável para uso em pipelines de CI onde a estabilidade do formato é mais crítica do que a velocidade absoluta.

## External Linking

| Concept             | Resource                             | Link                                                                                   |
| ------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **OpenAI**          | OpenAI API Documentation             | [platform.openai.com/docs/](https://platform.openai.com/docs/)                         |
| **MCP**             | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**      | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **Gemini AI**       | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**      | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **REST API Design** | RESTful API Best Practices           | [restfulapi.net/](https://restfulapi.net/)                                             |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
