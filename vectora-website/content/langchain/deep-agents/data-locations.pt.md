---
title: "Localizações de Dados"
slug: "langchain/deep-agents/data-locations"
description: "Onde dados são armazenados e como configurar localizações"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["deep-agents", "data", "storage", "locations", "configuration"]
---

{{< lang-toggle >}}

Deep Agents armazena dados de estado, conversas e memória no filesystem local. Você pode configurar onde tudo fica.

## Localizações Padrão

```
~/.deep-agents/                      # DEEPAGENTS_ROOT (padrão)
├── agents/
│   ├── research_agent/
│   │   ├── state.json               # Estado atual
│   │   ├── memory.db                # Memória persistida
│   │   └── conversations/
│   │       └── 2026-05-01.json
│   └── chat_agent/
└── config/
    └── agents.yaml                  # Configuração
```

## Personalizar Localizações

Via variáveis de ambiente:

```bash
export DEEPAGENTS_ROOT=/custom/path
export DEEPAGENTS_AGENTS_DIR=/custom/agents
export DEEPAGENTS_MEMORY_DIR=/custom/memory
export DEEPAGENTS_CONFIG_DIR=/custom/config
```

Via código:

```python
from deepagents import config

config.set_root_dir("/custom/deep-agents")
config.set_agents_dir("/custom/agents")
config.set_memory_dir("/custom/memory")

agent = Agent(name="research")
```

## Estrutura de Dados por Agente

```
my_agent/
├── state.json              # Estado atual do agente
├── config.yaml             # Configuração específica
├── memory.db               # Database SQLite (memória)
├── conversations/
│   ├── 2026-05-01.json
│   ├── 2026-05-02.json
│   └── 2026-05-03.json
├── traces/                 # Logs de execução
│   └── 2026-05-03.log
└── cache/                  # Cache de tool calls
    └── search_results.json
```

## Segurança e Permissões

Dados são isolados por agente:

```bash
~/.deep-agents/agents/research_agent
└── ACL: rw------- (600)
    # Apenas o usuário pode ler/escrever
```

## Sincronizar com Nuvem (Opcional)

Fazer backup de dados:

```bash
deep-agents backup research_agent
# Compacta e salva em ~/.deep-agents/backups/

deep-agents restore research_agent 2026-05-02
# Restaura de backup anterior
```

## External Linking

| Conceito              | Recurso           | Link                                                                                                                               |
| --------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Data Locations        | Storage Guide     | [https://docs.langchain.com/oss/python/deepagents/data-locations](https://docs.langchain.com/oss/python/deepagents/data-locations) |
| Filesystem Backend    | File System       | [https://docs.langchain.com/oss/python/deepagents/](https://docs.langchain.com/oss/python/deepagents/)                             |
| Environment Variables | Configuration     | [https://python-dotenv.readthedocs.io/](https://python-dotenv.readthedocs.io/)                                                     |
| Directory Structure   | File Organization | [https://docs.langchain.com/oss/python/deepagents/data-locations](https://docs.langchain.com/oss/python/deepagents/data-locations) |
| Path Management       | Python pathlib    | [https://docs.python.org/3/library/pathlib.html](https://docs.python.org/3/library/pathlib.html)                                   |
