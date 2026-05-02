---
title: "Trust Folder: Desktop Security Perimeter"
slug: trust-folder
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - compliance
  - concepts
  - config
  - desktop
  - mongodb-atlas
  - rbac
  - security
  - system
  - trust-folder
  - vector-search
  - vectora
  - yaml
---

{{< lang-toggle >}}

> [!NOTE] > **The Trust Folder is a feature exclusive to Vectora Desktop**. Vectora Cloud does not use a Trust Folder because it lacks direct access to the local filesystem — instead, it uses **Namespace isolation** in MongoDB Atlas. To learn more about cloud security, see [Infrastructure → Namespaces](../namespaces).

The Trust Folder is the **security perimeter** that limits which files Vectora Desktop can index, read, and process locally. It acts as a path-based sandbox, protecting against the accidental or malicious reading of sensitive files outside the project scope.

In the Desktop environment, the Trust Folder is mandatory to prevent the agent from indexing files such as `.env`, private SSH keys, or the user's personal data.

## The Problem of Unrestricted Access

Without a Trust Folder configuration, an AI agent could potentially access any file on the hard drive.

- **Secrets Exposure**: Automatic indexing of `/etc/passwd`, `~/.ssh/id_rsa`, or `.env` files.
- **Traversal Attacks**: Vulnerability to attempts to access files via relative paths like `../../sensitive/file.txt`.
- **Lack of Auditing**: Difficulty in tracking which files were processed by the AI engine.

With the Trust Folder, indexing is confined to specific directories (e.g., `./src`, `./docs`), blocking any attempt to "exit" the perimeter and generating detailed audit logs for every read attempt.

## Desktop vs Cloud: Trust Folder vs Namespace

The table below compares isolation mechanisms between the Desktop and Cloud versions of Vectora.

| Aspect        | Trust Folder (Desktop)              | Namespace (Cloud)          |
| :------------ | :---------------------------------- | :------------------------- |
| **Scope**     | Local filesystem                    | MongoDB Atlas collections  |
| **Isolation** | Path-based                          | Workspace/Tenant-based     |
| **Control**   | Local configuration (`config.yaml`) | Cloud Administrator / RBAC |
| **Security**  | Blocks Path Traversal               | Blocks Query Isolation     |
| **Audit**     | Local filesystem logs               | Cloud audit logs (Atlas)   |

## Trust Folder Configuration

Configuration is handled through the `vectora.config.yaml` file. You can define a single root directory or a list of trusted folders.

### Default Configuration (Root)

By default, Vectora trusts the project root where it was initialized.

```yaml
project:
  trust_folder: "." # Trusts everything within the current directory and subfolders
```

### Explicit Configuration (Recommended)

For higher security, it is recommended to list only the folders necessary for the agent's operation.

```yaml
project:
  trust_folders:
    - "./src"
    - "./docs"
    - "./packages"
  # Folders like node_modules, build, and .env files will be ignored
```

## Secure Path Resolution

Vectora resolves paths securely by normalizing relative paths to absolute ones and blocking attempts to exit the defined perimeter.

### Path Traversal Blocking Example

If the Trust Folder is set to `./src` and there is a read attempt for `../../../.env`:

1. The engine normalizes the path to `/absolute/path/.env`.
2. It verifies if this path is contained within `/absolute/path/to/src`.
3. If not, the operation is **BLOCKED**, and a security event is generated.

## Security Scenarios (What is prevented)

The Trust Folder protects the developer against several common attack vectors in AI environments.

- **Simple Path Traversal**: Prevents the LLM from requesting to read sensitive files outside the project.
- **Symlink Escape**: Detects and blocks symlinks that point outside the trusted directory.
- **Context Injection**: Blocks search commands injected into the prompt that try to access the OS filesystem (e.g., `/etc/passwd`).
- **CI/CD Exposure**: Ensures that CI runners index only the source code, ignoring infrastructure secrets present on the machine.

## Auditing and Monitoring

All file access attempts, whether permitted or denied, are recorded in the system audit log.

```bash
# Check blocked attempts in the last 24 hours
vectora audit --since 24h --filter "DENIED"
```

The generated log includes the timestamp, requested path, normalized path, active Trust Folder, and the reason for denial (e.g., `outside_trust_folder`).

## External Linking

| Concept            | Resource                                       | Link                                                                                                       |
| ------------------ | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas**  | Atlas Vector Search Documentation              | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **RBAC**           | NIST Role-Based Access Control Standard        | [csrc.nist.gov/projects/rbac](https://csrc.nist.gov/projects/rbac)                                         |
| **Secure Coding**  | OWASP Secure Coding Practices                  | [owasp.org/www-project-secure-coding-practices/](https://owasp.org/www-project-secure-coding-practices/)   |
| **GitHub Actions** | Automate your workflow from idea to production | [docs.github.com/en/actions](https://docs.github.com/en/actions)                                           |

---

_Part of the Vectora ecosystem_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contributors](https://github.com/Kaffyn/Vectora/graphs/contributors)
