---
title: "Deep Agents CLI"
slug: "langchain/deep-agents/cli"
description: "Comandos e interface de linha de comando do Deep Agents"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["deep-agents", "cli", "commands", "terminal"]
---

{{< lang-toggle >}}

Deep Agents inclui uma rich TUI (Terminal User Interface) para interação com agentes locais via CLI.

## Instalação

```bash
pip install deepagents
```

## Comandos Principais

### Run Agent

Execute um agente:

```bash
deep-agents run research_agent --input "Pesquise sobre AI"
```

### List Agents

Listar agentes disponíveis:

```bash
deep-agents list
```

### Create Agent

Criar novo agente:

```bash
deep-agents create --name my_agent --model claude-opus
```

### View State

Inspecionar estado do agente:

```bash
deep-agents state research_agent
```

## TUI Interativa

```bash
deep-agents interactive
```

Inicia interface interativa no terminal:

```
╔═══════════════════════════════════╗
║   Deep Agents Interactive        ║
╠═══════════════════════════════════╣
║ [1] Run Agent                    ║
║ [2] View Traces                  ║
║ [3] Edit Agent                   ║
║ [4] Exit                         ║
╚═══════════════════════════════════╝
```

## Configuração

Via variáveis de ambiente:

```bash
export DEEP_AGENTS_MODEL=claude-opus
export DEEP_AGENTS_DIR=~/.deep-agents
export LANGCHAIN_API_KEY=your_key
```

Ou arquivo `.deepagents.yaml`:

```yaml
agents:
  - name: research
    model: claude-opus
    tools: [search, summarize]
```

## External Linking

| Conceito         | Recurso             | Link                                                                                                                   |
| ---------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Deep Agents Docs | CLI Documentation   | [https://docs.langchain.com/oss/python/deepagents/](https://docs.langchain.com/oss/python/deepagents/)                 |
| CLI Reference    | Command Reference   | [https://docs.langchain.com/oss/python/deepagents/cli](https://docs.langchain.com/oss/python/deepagents/cli)           |
| Installation     | Install Deep Agents | [https://docs.langchain.com/oss/python/deepagents/overview](https://docs.langchain.com/oss/python/deepagents/overview) |
| Python Package   | PyPI                | [https://pypi.org/project/deepagents/](https://pypi.org/project/deepagents/)                                           |
| Terminal         | Click Framework     | [https://click.palletsprojects.com/](https://click.palletsprojects.com/)                                               |
