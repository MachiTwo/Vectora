---
title: "Deep Agents como ACP Server"
slug: "langchain/deep-agents/acp-deployment"
description: "Rodar agentes como servidores ACP em editores"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["deep-agents", "acp", "editor", "deployment", "integration"]
---

{{< lang-toggle >}}

Deep Agents pode operar em **modo ACP server**, permitindo que editores (VS Code, JetBrains, Zed) controlem agentes diretamente através do protocolo Agent Client Protocol.

## Modo ACP: Arquitetura

```text
Editor (VS Code, JetBrains, Zed)
    ↓ stdin/stdout
Deep Agent (ACP Server)
    ├─ Planning Engine
    ├─ Tool Executor
    └─ Filesystem State
```

**Fluxo:**

1. Editor envia comando ACP (ex: `editText`)
2. Agent recebe via stdin
3. Agent executa ação (plan, search, modify)
4. Agent retorna resultado via stdout
5. Editor atualiza UI

## Configurar Deep Agent como ACP Server

### Passo 1: Criar Agent

```python
from deepagents import Agent
from deepagents.acp import ACPServer

# Criar agente com VCR integration
agent = Agent(
    name="vectora-agent",
    model="claude-sonnet-4-6",
    tools=["search_vectora", "rerank", "execute_code"],
    enable_vcr=True
)

# Criar servidor ACP
acp_server = ACPServer(agent=agent)

if __name__ == "__main__":
    acp_server.run()  # Lê stdin, escreve stdout
```

### Passo 2: Configurar no Editor

**VS Code (.vscode/settings.json):**

```json
{
  "deepagents.enable": true,
  "deepagents.agentPath": "/path/to/agent.py",
  "deepagents.model": "claude-sonnet-4-6",
  "deepagents.tools": ["search", "edit", "execute"]
}
```

**JetBrains (Settings → Languages → Python → Deep Agents):**

```text
✓ Enable Deep Agents
  Agent: vectora-agent
  Model: claude-sonnet-4-6
  Tools: search, edit, execute
```

## Exemplo: Refactoring Agent

```python
from deepagents import Agent
from deepagents.acp import ACPServer
import json
import sys

class RefactoringAgent(Agent):
    async def acp_refactor_function(self, params):
        """Refactor uma função inteira"""
        file_path = params["file_path"]
        function_name = params["function_name"]

        # 1. Ler arquivo do editor
        with open(file_path) as f:
            content = f.read()

        # 2. Encontrar função
        start_line = find_function_line(content, function_name)
        func_body = extract_function(content, start_line)

        # 3. Analisar com VCR
        analysis = await self.vcr.analyze(func_body)

        # 4. Propor refactoring
        refactored = await self.llm.invoke(f"""
        Refatore esta função seguindo best practices.
        Análise VCR: {analysis}

        Código original:
        {func_body}

        Retorne apenas o código refatorado.
        """)

        # 5. Retornar para editor
        return {
            "original": func_body,
            "refactored": refactored,
            "line_range": (start_line, start_line + len(func_body.split('\n')))
        }

# Expor via ACP
acp_server = ACPServer(agent=RefactoringAgent())

if __name__ == "__main__":
    # Ler requisição ACP do editor via stdin
    while True:
        line = sys.stdin.readline()
        if not line:
            break

        request = json.loads(line)
        method = request.get("method")
        params = request.get("params", {})

        # Rotear para método ACP correspondente
        if method == "refactor_function":
            result = asyncio.run(acp_server.agent.acp_refactor_function(params))
        elif method == "analyze_file":
            result = asyncio.run(acp_server.agent.acp_analyze_file(params))
        else:
            result = {"error": f"Unknown method: {method}"}

        # Enviar resposta de volta ao editor
        sys.stdout.write(json.dumps(result) + "\n")
        sys.stdout.flush()
```

## Métodos ACP Standard

### Leitura

```python
async def acp_read_file(params):
    """Ler arquivo inteiro"""
    path = params["path"]
    with open(path) as f:
        return {"content": f.read()}

async def acp_get_active_path(params):
    """Retornar caminho do arquivo em foco"""
    return {"path": self.current_file}

async def acp_get_selection(params):
    """Retornar texto selecionado"""
    return {"selected_text": self.selection}
```

### Escrita

```python
async def acp_edit_text(params):
    """Editar arquivo"""
    path = params["path"]
    edits = params["edits"]  # [{"range": [...], "text": "..."}]

    # Aplicar edits
    content = read_file(path)
    for edit in edits:
        start_line = edit["range"]["start"]
        end_line = edit["range"]["end"]
        content = apply_edit(content, start_line, end_line, edit["text"])

    write_file(path, content)
    return {"success": True}

async def acp_create_file(params):
    """Criar arquivo novo"""
    path = params["path"]
    content = params.get("content", "")
    with open(path, "w") as f:
        f.write(content)
    return {"path": path}
```

### Execução

```python
async def acp_execute_terminal(params):
    """Executar comando no terminal"""
    command = params["command"]
    result = subprocess.run(command, capture_output=True, text=True)
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }

async def acp_execute_test(params):
    """Rodar testes"""
    path = params.get("test_path")
    result = subprocess.run(
        ["pytest", path, "-v"],
        capture_output=True,
        text=True
    )
    return {"output": result.stdout}
```

## Modo: CLI vs ACP vs Hybrid

### 1. CLI Mode (Padrão)

```bash
deep-agents run --agent vectora-agent
# Inicia TUI interativo local
```

### 2. ACP Server Mode (Editor Integration)

```bash
deep-agents acp --agent vectora-agent
# Lê stdin, escreve stdout
# Para ser usado por editor
```

### 3. Hybrid Mode

```bash
deep-agents hybrid --agent vectora-agent --port 8000
# Simultaneamente:
# - TUI local (terminal)
# - ACP server (stdin/stdout)
# - HTTP API (port 8000)
```

## Configuração Avançada

### With VCR Analysis

```python
from deepagents import Agent
from deepagents.acp import ACPServer

agent = Agent(
    name="vectora-acp",
    model="claude-sonnet-4-6",
    enable_vcr=True,
    vcr_config={
        "api_key": "vectora-key",
        "bucket": "code-context"
    }
)

acp_server = ACPServer(
    agent=agent,
    acp_methods=[
        "refactor_function",
        "analyze_code",
        "generate_tests",
        "document_code"
    ]
)
```

### With Streaming

```python
async def acp_analyze_code_streaming(params):
    """Analisar código com streaming"""
    code = params["code"]

    # Retornar streaming response
    async for chunk in self.llm.astream(
        f"Analise este código:\n{code}"
    ):
        yield {
            "type": "chunk",
            "content": chunk.content
        }

    yield {"type": "done"}
```

## Deploy: VS Code Extension

### package.json

```json
{
  "name": "deep-agents",
  "version": "1.0.0",
  "engines": { "vscode": "^1.80.0" },
  "activationEvents": ["onCommand:deepagents.start"],
  "contributes": {
    "commands": [
      {
        "command": "deepagents.start",
        "title": "Start Deep Agent"
      }
    ]
  }
}
```

### extension.ts

```typescript
import { spawn } from "child_process";
import { window, workspace } from "vscode";

export function activate(context: any) {
  let disposable = window.onDidChangeActiveTextEditor(async (editor) => {
    if (!editor) return;

    // Iniciar agente ACP
    const agent = spawn("python", ["./acp_agent.py"]);

    // Enviar arquivo atual
    const request = {
      method: "analyze_file",
      params: { path: editor.document.fileName },
    };

    agent.stdin.write(JSON.stringify(request) + "\n");

    // Receber análise
    agent.stdout.on("data", (data) => {
      const response = JSON.parse(data.toString());
      window.showInformationMessage(`Analysis: ${response.insights}`);
    });
  });

  context.subscriptions.push(disposable);
}
```

## Monitoramento

```python
class ACPMonitor:
    def __init__(self, acp_server):
        self.server = acp_server
        self.requests = []
        self.errors = []

    def log_request(self, method, params, result):
        """Log requisição ACP"""
        self.requests.append({
            "timestamp": datetime.now(),
            "method": method,
            "params": params,
            "result": result
        })

    def log_error(self, method, error):
        """Log erro"""
        self.errors.append({
            "timestamp": datetime.now(),
            "method": method,
            "error": str(error)
        })

    def get_stats(self):
        """Estatísticas de uso"""
        return {
            "total_requests": len(self.requests),
            "total_errors": len(self.errors),
            "methods_used": list(set(r["method"] for r in self.requests)),
            "error_rate": len(self.errors) / len(self.requests) if self.requests else 0
        }

# Usar com servidor
monitor = ACPMonitor(acp_server)
acp_server.on_request = monitor.log_request
acp_server.on_error = monitor.log_error
```

## Melhores Práticas

1. **Validação de Input:** Validar todos os `params` antes de processar
2. **Error Handling:** Sempre retornar `{"error": "..."}` em caso de falha
3. **Streaming:** Use streaming para operações longas
4. **State Management:** Manter estado no filesystem para durabilidade
5. **Logging:** Log todas as requisições e erros
6. **Performance:** Cache resultados quando possível

## External Linking

| Conceito          | Recurso            | Link                                                                                                         |
| ----------------- | ------------------ | ------------------------------------------------------------------------------------------------------------ |
| ACP Protocol      | Official Spec      | [https://modelcontextprotocol.io/clients](https://modelcontextprotocol.io/clients)                           |
| Deep Agents CLI   | Command Reference  | [https://docs.langchain.com/oss/python/deepagents/cli](https://docs.langchain.com/oss/python/deepagents/cli) |
| VS Code Extension | Extension API      | [https://code.visualstudio.com/api](https://code.visualstudio.com/api)                                       |
| JetBrains Plugin  | Plugin Development | [https://plugins.jetbrains.com/docs](https://plugins.jetbrains.com/docs)                                     |
| Zed Extensions    | Extension Guide    | [https://zed.dev/docs/extensions](https://zed.dev/docs/extensions)                                           |
