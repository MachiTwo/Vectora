---
title: "Instalação do Vectora"
description: "Guia de instalação local com uv, pip ou pipx em Python 3.10+"
slug: "installation"
tags:
  - installation
  - setup
  - uv
  - pip
  - python
  - fastapi
  - local-first
date: 2026-05-03
weight: 2.1
---

{{< lang-toggle >}}

{{< section-toggle >}}

Vectora roda localmente em sua máquina com Python 3.10+. Esta página cobre a instalação via `uv` (recomendado), `pip` e `pipx`. Para instalação via Docker, veja [Local Deployment](./local-deployment.md).

## Pré-requisitos

Antes de instalar Vectora, confirme que você tem:

- **Python 3.10 ou superior** — `python --version`
- **uv** (recomendado) ou **pip** — `uv --version` ou `pip --version`
- **Git** — para clonar o repositório — `git --version`
- **4GB RAM** mínimo (8GB recomendado para VCR + LanceDB)
- **2GB de espaço em disco** para modelos e índices

## Opção 1: Instalar com uv (Recomendado)

`uv` é um gerenciador de pacotes Python em Rust, 10-100x mais rápido que pip. É a forma recomendada de instalar Vectora.

### Instalar uv

```bash
# Linux / macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Via pip (qualquer SO)
pip install uv
```

### Clonar e Instalar Vectora

```bash
# Clonar repositório
git clone https://github.com/Kaffyn/Vectora.git
cd Vectora

# Criar ambiente virtual e instalar dependências
uv sync

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### Verificar Instalação

```bash
# Verificar que a CLI está disponível
vectora --version

# Testar que o servidor FastAPI sobe
vectora serve --port 8000
# Deve imprimir: "Vectora API running at http://localhost:8000"
```

## Opção 2: Instalar com pip

```bash
# Clonar repositório
git clone https://github.com/Kaffyn/Vectora.git
cd Vectora

# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Verificar
vectora --version
```

## Opção 3: Instalar com pipx (CLI global)

`pipx` instala a CLI de Vectora em ambiente isolado, disponível globalmente sem ativar virtualenv:

```bash
# Instalar pipx
pip install pipx
pipx ensurepath

# Instalar Vectora via pipx
pipx install vectora

# Verificar
vectora --version
```

## Configuração Inicial

Após instalar, configure as credenciais necessárias:

```bash
# Configurar VoyageAI (para embeddings)
vectora config set voyageai.api_key sk-voyage-xxx

# Opcionalmente, configurar LLM externo (Claude, GPT-4, etc.)
vectora config set anthropic.api_key sk-ant-xxx

# Ver configuração atual
vectora config show
```

### Arquivo de Configuração

Alternativa: crie um arquivo `.env` na raiz do projeto:

```bash
# .env
VOYAGEAI_API_KEY=sk-voyage-xxx
ANTHROPIC_API_KEY=sk-ant-xxx        # Opcional
OPENAI_API_KEY=sk-xxx               # Opcional

# Database (usado automaticamente se não definido)
LANCEDB_PATH=./data/lancedb
POSTGRES_URL=postgresql://localhost:5432/vectora
REDIS_URL=redis://localhost:6379
```

## Primeira Execução

```bash
# Iniciar servidor FastAPI (modo desenvolvimento)
vectora serve

# Servidor sobe em: http://localhost:8000
# Health check: http://localhost:8000/health
# API Docs: http://localhost:8000/docs
```

Você deve ver:

```text
Vectora v0.1.0 starting...
  VCR (XLM-RoBERTa): loaded
  LanceDB: initialized at ./data/lancedb
  Redis: connecting to redis://localhost:6379
  FastAPI: running at http://localhost:8000
```

## Verificar Componentes

```bash
# Status de todos os componentes
vectora status

# Output esperado:
# VCR:      running (latency: 7ms)
# LanceDB:  running (0 indices)
# Redis:    connected
# FastAPI:  running at :8000
```

## Troubleshooting

### Python 3.10 não encontrado

```bash
# No macOS com Homebrew:
brew install python@3.11

# No Ubuntu:
sudo apt install python3.11 python3.11-venv
```

### uv: command not found

```bash
# Adicionar uv ao PATH após instalação
source ~/.bashrc  # Linux
source ~/.zshrc   # macOS
```

### Erro de permissão (Windows)

Execute o terminal (PowerShell ou cmd) como administrador, ou use:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Porta 8000 já em uso

```bash
vectora serve --port 8001
```

## External Linking

| Conceito             | Recurso                                                      | Link                                                      |
| -------------------- | ------------------------------------------------------------ | --------------------------------------------------------- |
| **uv**               | Rust-based Python package manager                            | [astral.sh/uv](https://astral.sh/uv)                      |
| **Python Downloads** | Python 3.10+ downloads                                       | [python.org/downloads](https://www.python.org/downloads/) |
| **pipx**             | Install and run Python applications in isolated environments | [pipx.pypa.io](https://pipx.pypa.io/)                     |
| **FastAPI**          | Modern Python web framework                                  | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)     |
| **VoyageAI**         | Embeddings provider para RAG                                 | [voyageai.com](https://www.voyageai.com/)                 |
