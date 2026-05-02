---
title: SSO (Vectora Auth)
slug: sso
date: "2026-04-23T00:00:00-03:00"
type: docs
tags:
  - ai
  - auth
  - concepts
  - config
  - go
  - integration
  - json
  - jwt
  - mcp
  - oauth
  - oidc
  - protocol
  - saml
  - security
  - sso
  - system
  - tools
  - vectora
---

{{< lang-toggle >}}

**Vectora Auth** is Vectora's independent identity system. It allows organizations to manage access to code intelligence in a sovereign and isolated manner.

## Standalone Identity

Unlike previous versions, Vectora now operates its own identity provider or allows connection to external providers (BYOI - Bring Your Own Identity).

## SSO Options

Vectora supports integration with the main providers on the market via standard protocols:

1. **OAuth2 / OpenID Connect (OIDC)**: Connect Vectora directly to Google Workspace, GitHub Enterprise, Okta, or Auth0.
2. **SAML 2.0**: Robust integration with Microsoft Azure AD and other enterprise providers.

## Provider Configuration

To configure an external provider, add the credentials to your configuration file or environment variables:

```env
VECTORA_AUTH_METHOD=oidc
VECTORA_OIDC_ISSUER=https://accounts.google.com
VECTORA_OIDC_CLIENT_ID=your_client_id
VECTORA_OIDC_CLIENT_SECRET=your_client_secret
```

## Authentication Flow

The login process is simplified to ensure a smooth developer experience.

1. The user requests access via CLI or Interface.
2. Vectora redirects to the configured SSO provider.
3. After logging in, Vectora issues a locally signed **Vectora JWT**.
4. This token is used for all interactions with the search engine and MCP tools.

## External Linking

| Concept            | Resource                                        | Link                                                                                                   |
| ------------------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **MCP**            | Model Context Protocol Specification            | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification)                 |
| **MCP Go SDK**     | Go SDK for MCP (mark3labs)                      | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                                     |
| **OpenID Connect** | OIDC Core 1.0 Specification                     | [openid.net/specs/openid-connect-core-1_0.html](https://openid.net/specs/openid-connect-core-1_0.html) |
| **JWT**            | RFC 7519: JSON Web Token Standard               | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519)                 |
| **OAuth 2.0**      | RFC 6749: The OAuth 2.0 Authorization Framework | [datatracker.ietf.org/doc/html/rfc6749](https://datatracker.ietf.org/doc/html/rfc6749)                 |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
