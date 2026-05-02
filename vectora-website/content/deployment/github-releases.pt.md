---
title: GitHub Releases
slug: github-releases
date: "2026-04-19T10:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - binary
  - concepts
  - deployment
  - github
  - releases
  - security
  - system
  - tools
  - vectora
---

{{< lang-toggle >}}

O **GitHub Releases** é o repositório central de distribuição de binários do Vectora, onde cada versão estável é publicada com seus respectivos checksums de segurança.

Este método é ideal para usuários que desejam controle total sobre a versão instalada ou que operam em ambientes onde gerenciadores de pacotes não estão disponíveis.

## Acessando as Versões

Você pode encontrar todas as versões publicadas, incluindo notas de lançamento e artefatos de compilação, na página oficial do projeto.

### Link Oficial

As releases estão disponíveis em: [github.com/Kaffyn/Vectora/releases](https://github.com/Kaffyn/Vectora/releases)

## Escolhendo o Binário Correto

O Vectora é compilado para múltiplas plataformas e arquiteturas. Escolha o arquivo `.tar.gz` ou `.zip` que corresponde ao seu sistema operacional:

- **Windows**: `vectora-windows-amd64.zip` (Intel/AMD) ou `vectora-windows-arm64.zip`.
- **Linux**: `vectora-linux-amd64.tar.gz` ou arquiteturas ARM.
- **macOS**: `vectora-darwin-amd64.tar.gz` ou `vectora-darwin-arm64.tar.gz`.

## Verificação de Segurança

Para cada release, publicamos um arquivo `checksums.txt` contendo o hash SHA256 de todos os artefatos. É recomendável validar o download:

### Exemplo de Verificação (Linux/macOS)

```bash
# Gere o hash do arquivo baixado
sha256sum vectora-linux-amd64.tar.gz

# Compare com o valor presente no checksums.txt
```

## Instalação Manual

Após o download e verificação, extraia o binário e mova-o para um diretório presente no seu `PATH` (como `/usr/local/bin` no Linux/macOS ou um diretório configurado no Windows).

## External Linking

| Concept              | Resource             | Link                                               |
| -------------------- | -------------------- | -------------------------------------------------- |
| **Anthropic Claude** | Claude Documentation | [docs.anthropic.com/](https://docs.anthropic.com/) |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [Licença (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Parte do ecossistema Vectora AI Agent. Construído com [ADK](https://adk.dev/), [Claude](https://claude.ai/) e [Go](https://golang.org/)._

© 2026 Contribuidores do Vectora. Todos os direitos reservados.

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
