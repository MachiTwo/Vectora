---
title: "Gemini"
slug: gemini
date: "2026-04-27T10:00:00-03:00"
type: docs
tags:
  - ai
  - architecture
  - ast-parsing
  - auth
  - concepts
  - config
  - deployment
  - gemini
  - google
  - integration
  - security
  - tools
  - vectora
---

{{< lang-toggle >}}

A integração do Vectora com o Google Gemini permite que o motor de busca utilize os modelos de última geração da Google para raciocínio técnico e geração de código. A implantação desta integração foca na configuração segura das chaves de API do Google AI Studio e na orquestração de chamadas de contexto através do servidor Vectora Cloud.

O Vectora atua como um middleware inteligente que enriquece os prompts enviados ao Gemini com os fragmentos de código mais relevantes recuperados do seu repositório.

## Google AI Studio e Vertex AI

O Vectora suporta dois caminhos de implantação para a integração com Gemini: o Google AI Studio (para desenvolvedores individuais e prototipagem rápida) e a Vertex AI no Google Cloud Platform (para empresas que exigem conformidade e segurança de nível corporativo).

As chaves de API e as identidades de serviço devem ser configuradas no servidor Vectora para permitir o acesso autenticado aos modelos `gemini-1.5-pro` e `gemini-1.5-flash`.

## Vectora Cognitive Runtime: O Guardião da Saída

Embora o Gemini seja o motor de raciocínio, o **[Vectora Cognitive Runtime (Decision Engine)](/models/vectora-decision-engine/)** atua como o guardião tático de cada resposta gerada. O Vectora Cognitive Runtime observa a saída do Gemini em tempo real para:

- **Detectar Alucinações**: Valida se as alegações técnicas da resposta estão fundamentadas no contexto de código fornecido.
- **Avaliar Faithfulness**: Mede a fidelidade da resposta em relação aos fatos recuperados do backend.
- **Orquestrar Correções**: Se a confiança na resposta for baixa, o Vectora Cognitive Runtime pode instruir o Agentic Framework a realizar uma nova iteração com parâmetros refinados.

## Configuração de Proxy de Contexto

Para otimizar a latência, o Vectora implanta um proxy de contexto que realiza o pré-processamento dos dados antes de enviá-los ao Gemini. Este componente é implantado junto com o motor principal e gerencia o cache de tokens para reduzir custos de API.

Este proxy garante que o contexto enviado ao Gemini esteja sempre dentro dos limites da janela de contexto do modelo, realizando truncamento inteligente baseado na relevância AST.

## Publicação no Workspace do Google

Para integrações que estendem o Google Workspace (como Google Docs ou Sheets), o Vectora fornece um pacote de integração pronto para deploy no Google Apps Script. Isso permite que você faça perguntas sobre seu código diretamente de dentro das ferramentas de produtividade do Google.

O deploy desta camada é feito através da ferramenta `clasp`, que sincroniza o código local da integração com o ambiente de execução do Google.

## Deploy via Docker e Cloud Run

A maneira recomendada de implantar a integração Gemini em escala é através do Google Cloud Run. Utilizando a imagem Docker oficial do Vectora, você pode rodar um serviço serverless que escala a zero quando não está em uso, minimizando custos fixos.

```bash
# Exemplo de deploy no Cloud Run
gcloud run deploy vectora-gemini-bridge \
  --image gcr.io/seu-projeto/vectora-cloud:latest \
  --set-env-vars GOOGLE_API_KEY=seu_token \
  --platform managed
```

Esta arquitetura garante alta disponibilidade e integração nativa com o ecossistema de monitoramento do Google Cloud (Stackdriver).

## External Linking

| Concept         | Resource                           | Link                                                                                 |
| --------------- | ---------------------------------- | ------------------------------------------------------------------------------------ |
| **Gemini AI**   | Google DeepMind Gemini Models      | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/) |
| **Gemini API**  | Google AI Studio Documentation     | [ai.google.dev/docs](https://ai.google.dev/docs)                                     |
| **AST Parsing** | Tree-sitter Official Documentation | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)     |
| **Docker**      | Docker Documentation               | [docs.docker.com/](https://docs.docker.com/)                                         |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
