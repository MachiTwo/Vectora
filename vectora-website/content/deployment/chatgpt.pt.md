---
title: "ChatGPT"
slug: chatgpt
date: "2026-04-27T10:00:00-03:00"
type: docs
tags:
  - ai
  - chatgpt
  - concepts
  - config
  - deployment
  - openai
  - plugin
  - plugins
  - privacy
  - protocol
  - security
  - tools
  - vectora
---

{{< lang-toggle >}}

A integração do Vectora com o ChatGPT é realizada através de um Custom GPT ou um Plugin oficial da OpenAI. Esta integração permite que o ChatGPT utilize as ferramentas do Vectora Cloud para buscar contexto em sua base de código e realizar revisões técnicas diretamente na interface de chat da OpenAI.

Diferente das extensões de IDE, o plugin do ChatGPT interage exclusivamente com a API REST do Vectora Cloud via protocolo HTTP seguro.

## Configuração do Manifest

Toda integração com o ChatGPT exige um arquivo `ai-plugin.json` que descreve as capacidades da ferramenta, os endpoints disponíveis e os detalhes de autenticação. Este arquivo deve estar acessível publicamente na rota `/.well-known/ai-plugin.json`.

O manifest define como o modelo de linguagem deve interpretar as ferramentas de busca semântica e quais permissões de acesso ao workspace são necessárias.

## Autenticação via OAuth

Para garantir a segurança dos dados dos usuários, o Vectora utiliza o fluxo OAuth 2.0 para autenticar as requisições vindas da OpenAI. Isso garante que o ChatGPT só possa acessar os namespaces e repositórios que o usuário autorizou explicitamente.

As credenciais de OAuth (Client ID e Secret) são configuradas no painel administrativo do Vectora Cloud e vinculadas ao perfil do plugin no portal da OpenAI.

## Registro no Portal da OpenAI

A implantação final envolve o registro do domínio da API no portal de desenvolvedores da OpenAI. Durante este processo, a OpenAI valida a acessibilidade do manifest e a conformidade dos endpoints com a especificação OpenAPI (Swagger).

```text
Passos para Registro:
1. Acesse o portal de desenvolvedores da OpenAI.
2. Selecione "Develop your own plugin".
3. Insira o domínio do seu servidor Vectora Cloud.
4. Valide o arquivo de manifest e a especificação OpenAPI.
```

## Verificação e Publicação

Após o registro inicial, o plugin pode ser instalado por usuários específicos via link de convite ou submetido para a Plugin Store oficial da OpenAI. O processo de revisão da OpenAI garante que a integração segue as diretrizes de segurança e privacidade da plataforma.

A cada atualização da API do Vectora, a especificação OpenAPI deve ser sincronizada para que o ChatGPT conheça novas ferramentas de análise ou melhorias no motor de busca.

## External Linking

| Concept             | Resource                                        | Link                                                                                   |
| ------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------- |
| **OpenAI**          | OpenAI API Documentation                        | [platform.openai.com/docs/](https://platform.openai.com/docs/)                         |
| **OAuth 2.0**       | RFC 6749: The OAuth 2.0 Authorization Framework | [datatracker.ietf.org/doc/html/rfc6749](https://datatracker.ietf.org/doc/html/rfc6749) |
| **OpenAPI**         | OpenAPI Specification                           | [swagger.io/specification/](https://swagger.io/specification/)                         |
| **REST API Design** | RESTful API Best Practices                      | [restfulapi.net/](https://restfulapi.net/)                                             |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
