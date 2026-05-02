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

Vectora for macOS is officially distributed via **Homebrew**, facilitating the installation, update, and management of the unified binary (CLI + Core) on Intel and Apple Silicon systems.

By using Homebrew, you ensure that system dependencies are managed automatically and that `vectora` is always available in your `PATH`.

## Installation

To install Vectora via Homebrew, you need to add the official Kaffyn tap and run the installation command:

### Installation Commands

```bash
# Add the official repository
brew tap kaffyn/vectora

# Install Vectora
brew install vectora
```

## Version Management

Homebrew makes maintaining Vectora easy, allowing you to check for new versions and update with a single command.

### Update

To update to the latest version published on GitHub Releases:

```bash
brew update
brew upgrade vectora
```

### Uninstallation

In case you need to remove Vectora and its system configurations:

```bash
brew uninstall vectora
brew untap kaffyn/vectora
```

## Supported Architectures

The Vectora formula in Homebrew automatically detects your architecture and downloads the optimized binary:

- **macOS Apple Silicon (arm64)**: Native for M1, M2, M3 chips.
- **macOS Intel (amd64)**: Compatible with Intel-based Macs.

## Integrity Verification

Homebrew automatically checks the SHA256 checksum of each downloaded release against the values published in the formula repository, ensuring the binary has not been altered.

## External Linking

| Concept              | Resource             | Link                                               |
| -------------------- | -------------------- | -------------------------------------------------- |
| **Anthropic Claude** | Claude Documentation | [docs.anthropic.com/](https://docs.anthropic.com/) |

---

**Vectora v0.1.0** · [GitHub](https://github.com/Kaffyn/Vectora) · [License (MIT)](https://github.com/Kaffyn/Vectora/blob/master/LICENSE) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)

_Part of the Vectora AI Agent ecosystem. Built with [ADK](https://adk.dev/), [Claude](https://claude.ai/) and [Go](https://golang.org/)._

© 2026 Vectora Contributors. All rights reserved.

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
