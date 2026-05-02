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

**GitHub Releases** is the central repository for Vectora binary distribution, where each stable version is published with its respective security checksums.

This method is ideal for users who want full control over the installed version or who operate in environments where package managers are not available.

## Accessing Versions

You can find all published versions, including release notes and build artifacts, on the project's official page.

### Official Link

Releases are available at: [github.com/Kaffyn/Vectora/releases](https://github.com/Kaffyn/Vectora/releases)

## Choosing the Correct Binary

Vectora is compiled for multiple platforms and architectures. Choose the `.tar.gz` or `.zip` file that matches your operating system:

- **Windows**: `vectora-windows-amd64.zip` (Intel/AMD) or `vectora-windows-arm64.zip`.
- **Linux**: `vectora-linux-amd64.tar.gz` or ARM architectures.
- **macOS**: `vectora-darwin-amd64.tar.gz` or `vectora-darwin-arm64.tar.gz`.

## Security Verification

For each release, we publish a `checksums.txt` file containing the SHA256 hash of all artifacts. It is recommended to validate the download:

### Verification Example (Linux/macOS)

```bash
# Generate the hash of the downloaded file
sha256sum vectora-linux-amd64.tar.gz

# Compare with the value present in checksums.txt
```

## Manual Installation

After download and verification, extract the binary and move it to a directory present in your `PATH` (such as `/usr/local/bin` on Linux/macOS or a configured directory on Windows).

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
