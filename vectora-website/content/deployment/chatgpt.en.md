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
  - integration
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

The integration of Vectora with ChatGPT is performed through a Custom GPT or an official OpenAI Plugin. This integration allows ChatGPT to use Vectora Cloud tools to search for context in your codebase and perform technical reviews directly within the OpenAI chat interface.

Unlike IDE extensions, the ChatGPT plugin interacts exclusively with the Vectora Cloud REST API via secure HTTP protocol.

## Manifest Configuration

Every ChatGPT integration requires an `ai-plugin.json` file that describes the tool's capabilities, available endpoints, and authentication details. This file must be publicly accessible at the `/.well-known/ai-plugin.json` route.

The manifest defines how the language model should interpret semantic search tools and what workspace access permissions are required.

## OAuth Authentication

To ensure user data security, Vectora uses the OAuth 2.0 flow to authenticate requests from OpenAI. This ensures that ChatGPT can only access the namespaces and repositories that the user has explicitly authorized.

OAuth credentials (Client ID and Secret) are configured in the Vectora Cloud administrative panel and linked to the plugin profile in the OpenAI portal.

## OpenAI Portal Registration

The final deployment involves registering the API domain in the OpenAI developer portal. During this process, OpenAI validates the manifest accessibility and endpoint compliance with the OpenAPI (Swagger) specification.

```text
Registration Steps:
1. Access the OpenAI developer portal.
2. Select "Develop your own plugin".
3. Enter your Vectora Cloud server domain.
4. Validate the manifest file and OpenAPI specification.
```

## Verification and Publication

After initial registration, the plugin can be installed by specific users via invite link or submitted to the official OpenAI Plugin Store. OpenAI's review process ensures that the integration follows the platform's security and privacy guidelines.

With each Vectora API update, the OpenAPI specification must be synchronized so that ChatGPT knows about new analysis tools or improvements to the search engine.

## External Linking

| Concept             | Resource                                        | Link                                                                                   |
| ------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------- |
| **OpenAI**          | OpenAI API Documentation                        | [platform.openai.com/docs/](https://platform.openai.com/docs/)                         |
| **OAuth 2.0**       | RFC 6749: The OAuth 2.0 Authorization Framework | [datatracker.ietf.org/doc/html/rfc6749](https://datatracker.ietf.org/doc/html/rfc6749) |
| **OpenAPI**         | OpenAPI Specification                           | [swagger.io/specification/](https://swagger.io/specification/)                         |
| **REST API Design** | RESTful API Best Practices                      | [restfulapi.net/](https://restfulapi.net/)                                             |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
