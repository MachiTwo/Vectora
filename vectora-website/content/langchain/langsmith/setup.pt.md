---
title: "Configurar LangSmith"
slug: "langchain/langsmith/setup"
description: "Configuração e ativação do LangSmith em projetos"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langsmith", "setup", "configuration", "environment"]
---

{{< lang-toggle >}}

Configurar LangSmith é simples: obtenha uma API key, defina variáveis de ambiente e ative o tracing.

## Obter API Key

1. Vá para [smith.langchain.com](https://smith.langchain.com/)
2. Crie uma conta (use seu email da empresa)
3. Copie a API key da seção Settings

## Variáveis de Ambiente

```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=your_api_key_here
export LANGCHAIN_PROJECT="vectora-agents"  # Nome do projeto
```

## Ativar Tracing no Código

```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your_key"

# Agora todos os runnables são automaticamente tracejados
from langchain.runnables import RunnableSequence

chain = prompt | llm | output_parser
result = chain.invoke({"input": "data"})  # Rastreado automaticamente
```

## Criar Projeto

Projetos isolam diferentes agentes:

```python
# Conecta ao projeto "vectora-agents"
os.environ["LANGCHAIN_PROJECT"] = "vectora-agents"

# Cada execução aparece em smith.langchain.com/projects/vectora-agents
```

## External Linking

| Conceito              | Recurso             | Link                                                                                                                     |
| --------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| LangSmith Setup       | Getting Started     | [https://docs.langchain.com/langsmith/setup](https://docs.langchain.com/langsmith/setup)                                 |
| Environment Variables | Configuration Guide | [https://docs.langchain.com/langsmith/setup/environment](https://docs.langchain.com/langsmith/setup/environment)         |
| API Keys              | Authentication      | [https://docs.langchain.com/langsmith/setup/keys](https://docs.langchain.com/langsmith/setup/keys)                       |
| Projects              | Project Management  | [https://docs.langchain.com/langsmith/setup/projects](https://docs.langchain.com/langsmith/setup/projects)               |
| Tracing               | Enable Tracing      | [https://docs.langchain.com/langsmith/observability/tracing](https://docs.langchain.com/langsmith/observability/tracing) |
