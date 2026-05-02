---
title: Homebrew (macOS)
slug: homebrew
date: "2026-04-19T10:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - concepts
  - deployment
  - homebrew
  - macos
  - package-manager
  - system
  - tools
  - vectora
---

{{< lang-toggle >}}

O Vectora para macOS é distribuído oficialmente via **Homebrew**, facilitando a instalação, atualização e gestão do binário unificado (CLI + Core) em sistemas Intel e Apple Silicon.

Ao utilizar o Homebrew, você garante que as dependências do sistema sejam gerenciadas automaticamente e que o `vectora` esteja sempre disponível no seu `PATH`.

## Instalação

Para instalar o Vectora via Homebrew, você precisa adicionar o tap oficial da Kaffyn e executar o comando de instalação:

### Comandos de Instalação

```bash
# Adiciona o repositório oficial
brew tap kaffyn/vectora

# Instala o Vectora
brew install vectora
```

## Gestão de Versões

O Homebrew facilita a manutenção do Vectora, permitindo que você verifique por novas versões e atualize com um único comando.

### Atualização

Para atualizar para a versão mais recente publicada no GitHub Releases:

```bash
brew update
brew upgrade vectora
```

### Desinstalação

Caso precise remover o Vectora e suas configurações de sistema:

```bash
brew uninstall vectora
brew untap kaffyn/vectora
```

## Arquiteturas Suportadas

A fórmula do Vectora no Homebrew detecta automaticamente sua arquitetura e baixa o binário otimizado:

- **macOS Apple Silicon (arm64)**: Nativo para chips M1, M2, M3.
- **macOS Intel (amd64)**: Compatível com Macs baseados em processadores Intel.

## Verificação de Integridade

O Homebrew verifica automaticamente o checksum SHA256 de cada release baixada contra os valores publicados no repositório de fórmulas, garantindo que o binário não foi alterado.

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
