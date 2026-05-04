---
title: "CLI: Interface de Linha de Comando"
slug: cli
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - cli
  - python
  - system-tray
  - tui
  - typer
  - vectora
draft: false
---

{{< lang-toggle >}}

{{< section-toggle >}}

O CLI do Vectora é construído com Typer (Python) e oferece três interfaces: comandos de terminal padrão, um TUI interativo (Textual) para exploração visual, e um system tray (Windows) para acesso rápido em modo local.

## Instalação e Uso Básico

```bash
# Instalar
uv tool install vectora

# Verificar instalação
vectora --version
vectora --help
```

## Comandos Principais

### Busca Semântica

```bash
# Busca básica
vectora search "Como validar tokens JWT?"

# Busca com filtros
vectora search "auth middleware" --namespace src/auth --language python

# Busca com estratégia específica
vectora search "connection pool" --strategy semantic --top-k 5

# Saída em JSON
vectora search "validate token" --output json
```

### Agente

```bash
# Executar agente
vectora agent run "Refatora validate_token para usar Pydantic v2"

# Agente com streaming (mostra raciocínio em tempo real)
vectora agent run "Explique a arquitetura de auth" --stream

# Limitar iterações
vectora agent run "Crie testes para jwt.py" --max-iterations 3
```

### Indexação

```bash
# Indexar diretório
vectora index src/

# Indexar com exclusões
vectora index . --exclude node_modules --exclude "*.pyc"

# Re-indexar (force)
vectora index src/ --force

# Status do índice
vectora index status
```

### Servidor

```bash
# Iniciar servidor FastAPI
vectora serve

# Servidor com hot-reload (desenvolvimento)
vectora serve --reload

# Servidor em porta específica
vectora serve --port 8080

# Verificar saúde do servidor
vectora health
```

### Configuração

```bash
# Ver configuração atual
vectora config show

# Definir valor
vectora config set voyage_api_key sk-voyage-xxx
vectora config set postgres_host localhost

# Resetar configuração
vectora config reset
```

## TUI Interativo

O TUI (Terminal User Interface) usa Textual para exploração visual do codebase.

```bash
# Abrir TUI
vectora tui
```

Funcionalidades do TUI:

- Busca semântica com preview em tempo real
- Navegação por resultados com teclado
- Visualização de chunks com syntax highlighting
- Painel de métricas do VCR (faithfulness, latência)

Atalhos de teclado no TUI:

| Tecla     | Ação                   |
| --------- | ---------------------- |
| `/`       | Foco na barra de busca |
| `Enter`   | Executar busca         |
| `Tab`     | Alternar entre painéis |
| `j` / `k` | Navegar resultados     |
| `q`       | Fechar TUI             |

## System Tray (Windows)

Em modo local (sem servidor ativo), o Vectora fica disponível via ícone na bandeja do sistema Windows.

```bash
# Iniciar em modo tray
vectora tray start

# Parar tray
vectora tray stop
```

O tray permite:

- Iniciar/parar o servidor FastAPI com um clique
- Acessar a interface web em `http://localhost:8000`
- Ver status dos componentes (PostgreSQL, Redis, LanceDB)
- Configurar a chave de API VoyageAI

O módulo tray é implementado em `vectora/internal/tray/` usando `pystray` e é crítico para o modo de uso local no Windows — não remover ou desabilitar.

## Saída e Formatos

```bash
# Saída padrão (tabela)
vectora search "jwt validation"

# Saída JSON (para scripts)
vectora search "jwt validation" --output json | jq '.results[0].file'

# Saída compacta
vectora search "jwt validation" --output compact
```

## External Linking

| Conceito    | Recurso                   | Link                                                                          |
| ----------- | ------------------------- | ----------------------------------------------------------------------------- |
| **Typer**   | CLI framework para Python | [typer.tiangolo.com](https://typer.tiangolo.com/)                             |
| **Textual** | TUI framework Python      | [textual.textualize.io](https://textual.textualize.io/)                       |
| **pystray** | System tray Python        | [github.com/moses-palmer/pystray](https://github.com/moses-palmer/pystray)    |
| **Rich**    | Terminal formatting       | [rich.readthedocs.io](https://rich.readthedocs.io/)                           |
| **uv tool** | Python tool installation  | [docs.astral.sh/uv/concepts/tools](https://docs.astral.sh/uv/concepts/tools/) |
