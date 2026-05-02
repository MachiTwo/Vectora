---
title: "Skill: Auditoria de Segurança"
slug: security-audit
date: "2026-04-24T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - agents
  - ai
  - auth
  - compliance
  - concepts
  - guardian
  - mcp
  - openai
  - protocol
  - security
  - skills
  - system
  - vectora
---

{{< lang-toggle >}}

A skill de Auditoria de Segurança fornece uma análise abrangente de vulnerabilidades, detecção de vazamento de credenciais e avaliação geral de risco de segurança. Ela valida o código contra padrões comuns de segurança e garante que informações sensíveis nunca sejam expostas dentro da base de código.

Ao integrar verificações de segurança diretamente no ciclo de desenvolvimento, o Vectora ajuda os desenvolvedores a capturarem problemas críticos antes que eles cheguem à produção.

## Detecção de Vulnerabilidades

O Vectora faz o escaneamento de uma ampla gama de riscos de segurança, incluindo as categorias do OWASP Top 10.

- **Ataques de Injeção**: Valida inputs contra padrões de injeção SQL, NoSQL e de comando.
- **Cross-Site Scripting (XSS)**: Identifica potenciais vetores de ataque em componentes voltados para a web.
- **Controle de Acesso**: Verifica se a lógica de autenticação e autorização impõe corretamente as permissões do usuário.
- **Desserialização Insegura**: Detecta o manuseio inseguro de formatos de dados externos.

## Detecção de Credenciais & Segredos

A skill foca especificamente na exposição acidental de materiais sensíveis dentro de arquivos de código.

- **Chaves de API**: Escaneia por padrões comuns de chaves de serviço (ex: AWS, OpenAI, Stripe).
- **Credenciais de Banco de Dados**: Identifica strings de conexão e senhas hardcoded.
- **Tokens de Autenticação**: Detecta JWTs, tokens OAuth e outros identificadores de sessão.
- **Materiais de Criptografia**: Encontra chaves SSH, certificados e arquivos de chave privada.

## Melhores Práticas de Segurança

Para maximizar a eficácia da skill de Auditoria de Segurança, siga estas diretrizes de integração.

- **Auditoria Contínua**: Execute verificações de segurança em cada mudança importante de código ou pull request.
- **Prioridade de Sanitização**: Preste atenção especial aos componentes que lidam com input direto do usuário.
- **Integração com Guardian**: Utilize sempre o módulo interno Guardian do projeto para manter uma lógica de validação consistente.
- **Logs de Auditoria**: Garanta que todas as ações sensíveis à segurança sejam registradas nos logs de auditoria do sistema.

## Quando Usar

Esta skill deve ser utilizada durante fases críticas do ciclo de vida de desenvolvimento.

- Antes de commitar código que lida com autenticação ou dados sensíveis.
- Durante revisões formais de segurança ou auditorias arquiteturais.
- Ao adicionar novas dependências externas ou bibliotecas.
- Antes do deploy final para ambientes de produção.

## External Linking

| Concept           | Resource                                        | Link                                                                                                     |
| ----------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **MCP**           | Model Context Protocol Specification            | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                   |
| **MCP Go SDK**    | Go SDK for MCP (mark3labs)                      | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                       |
| **OpenAI**        | OpenAI API Documentation                        | [platform.openai.com/docs/](https://platform.openai.com/docs/)                                           |
| **Secure Coding** | OWASP Secure Coding Practices                   | [owasp.org/www-project-secure-coding-practices/](https://owasp.org/www-project-secure-coding-practices/) |
| **OAuth 2.0**     | RFC 6749: The OAuth 2.0 Authorization Framework | [datatracker.ietf.org/doc/html/rfc6749](https://datatracker.ietf.org/doc/html/rfc6749)                   |
| **JWT**           | RFC 7519: JSON Web Token Standard               | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)                   |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
