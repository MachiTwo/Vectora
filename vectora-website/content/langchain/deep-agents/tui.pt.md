---
title: "Terminal UI (TUI) do Deep Agents"
slug: "langchain/deep-agents/tui"
description: "Interface de usuário no terminal para interagir com agentes"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["deep-agents", "tui", "terminal", "ui", "interface"]
---

{{< lang-toggle >}}

Deep Agents inclui uma rich TUI (Terminal User Interface) para interação interativa com agentes locais via CLI. Útil para desenvolvimento, debugging e uso local.

## Iniciando TUI

```bash
deep-agents interactive
```

Inicia a interface interativa no terminal:

```
╔════════════════════════════════════════╗
║       Deep Agents TUI                  ║
╠════════════════════════════════════════╣
║                                        ║
║  [1] Run Agent                         ║
║  [2] View Traces                       ║
║  [3] Edit Agent Config                 ║
║  [4] Manage Memory                     ║
║  [5] Agent Marketplace                 ║
║  [6] Settings                          ║
║  [0] Exit                              ║
║                                        ║
║  > Select option:                      ║
╚════════════════════════════════════════╝
```

## Executar Agent via TUI

Opção [1] abre interface para:

```
Agent: [research_agent          ]  ↓

Task: [                                    ]

[Run] [Cancel]

─ Output ─────────────────────────────────
Thinking...
> Searching for "Artificial Intelligence"
> Found 5 results
> Summarizing...

Response:
AI is a field of computer science...
```

## Visualizar Traces

Opção [2] mostra histórico:

```
─ Recent Traces ──────────────────────────
2026-05-03 14:32:15 | search_agent | ✓
2026-05-03 14:31:42 | research_agent | ✓
2026-05-03 14:25:18 | chat_agent | ✓

Select trace to inspect: [3]

─ Trace Details ──────────────────────────
Input: "What is AI?"
Tool: search
Status: Success
Output: [5 results found]
Duration: 245ms
```

## Customizar TUI

Tema e cores via configuração:

```yaml
# ~/.deep-agents/tui.yaml
theme: dark
colors:
  primary: blue
  success: green
  error: red
  warning: yellow
fonts:
  mono: Courier New
```

## ACP em TUI

Conectar a agentes remotos (ACP Protocol):

```bash
deep-agents interactive --acp

# Conecta-se a:
# - Agentes locais (Deep Agents)
# - Agentes Vectora via MCP
# - Outros agentes ACP-compatíveis
```

## External Linking

| Conceito         | Recurso                | Link                                                                                                         |
| ---------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Deep Agents TUI  | TUI Guide              | [https://docs.langchain.com/oss/python/deepagents/tui](https://docs.langchain.com/oss/python/deepagents/tui) |
| Deep Agents Docs | Official Documentation | [https://docs.langchain.com/oss/python/deepagents/](https://docs.langchain.com/oss/python/deepagents/)       |
| Rich Library     | Terminal Formatting    | [https://rich.readthedocs.io/](https://rich.readthedocs.io/)                                                 |
| Prompt Toolkit   | Interactive CLI        | [https://python-prompt-toolkit.readthedocs.io/](https://python-prompt-toolkit.readthedocs.io/)               |
| Click Framework  | Command Line Interface | [https://click.palletsprojects.com/](https://click.palletsprojects.com/)                                     |
