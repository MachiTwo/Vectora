---
title: "VS Code"
slug: vscode
date: "2026-04-27T10:00:00-03:00"
type: docs
tags:
  - ai
  - auth
  - concepts
  - deployment
  - extension
  - marketplace
  - mcp
  - protocol
  - tools
  - vectora
  - vscode
---

{{< lang-toggle >}}

A extensão do Vectora para o Visual Studio Code é publicada no Visual Studio Marketplace e no Open VSX Registry. Diferente do binário Go do daemon, a extensão é construída em TypeScript e atua como uma interface visual que se comunica com o Servidor MCP local (Desktop) ou remoto (Cloud).

O processo de implantação da extensão envolve a compilação do código fonte, a geração do arquivo VSIX e a publicação oficial através das ferramentas de linha de comando da Microsoft.

## Marketplace da Microsoft

O Visual Studio Marketplace é a principal vitrine para extensões do VS Code. Para publicar, é necessário ter uma conta de desenvolvedor vinculada a uma organização no Azure DevOps e um Personal Access Token (PAT) com as permissões apropriadas.

A publicação é automatizada via CI/CD, mas pode ser realizada manualmente para lançamentos de pré-visualização ou testes internos usando a ferramenta `vsce`.

## Compilação e Empacotamento

Antes de publicar, a extensão deve ser compilada e empacotada. Este processo remove dependências de desenvolvimento e otimiza o código para execução dentro do VS Code.

```bash
# Navegar até o diretório da extensão
cd integrations/packages/vscode

# Instalar dependências
npm install

# Compilar e gerar o arquivo .vsix
npx vsce package
```

## Publicação com vsce

A publicação oficial é feita usando o comando `publish`. Certifique-se de que a versão no `package.json` foi incrementada seguindo as regras de versionamento semântico (SemVer).

```bash
# Publicar no Marketplace oficial
npx vsce publish

# Caso precise especificar o token manualmente
npx vsce publish -p <SEU_TOKEN_PAT>
```

## Ciclo de Lançamento e Open VSX

Além do Marketplace oficial, o Vectora também é publicado no Open VSX Registry, que atende a forks do VS Code como o VSCodium. O processo utiliza a ferramenta `ovsx`.

```bash
# Publicar no Open VSX
npx ovsx publish <NOME_DO_ARQUIVO>.vsix -p <TOKEN_OPEN_VSX>
```

Cada nova versão da extensão deve ser acompanhada por um `CHANGELOG.md` atualizado, descrevendo as melhorias no motor de busca e na integração com o Servidor MCP.

## External Linking

| Concept            | Resource                                       | Link                                                                                   |
| ------------------ | ---------------------------------------------- | -------------------------------------------------------------------------------------- |
| **MCP**            | Model Context Protocol Specification           | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK**     | Go SDK for MCP (mark3labs)                     | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **TypeScript**     | Official TypeScript Handbook                   | [www.typescriptlang.org/docs/](https://www.typescriptlang.org/docs/)                   |
| **GitHub Actions** | Automate your workflow from idea to production | [docs.github.com/en/actions](https://docs.github.com/en/actions)                       |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
