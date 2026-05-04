---
title: "Agent Client Protocol (ACP)"
slug: "langchain/acp"
description: "Protocolo para integração agente-editor"
date: 2026-05-03
type: docs
sidebar:
  open: true
breadcrumbs: true
tags: ["langchain", "acp", "protocol", "editor", "ide", "integration"]
---

{{< lang-toggle >}}

ACP (Agent Client Protocol) é um protocolo que **padroniza comunicação entre agentes de código e editores/IDEs**.

## ACP vs MCP

| Aspecto | MCP | ACP |
|--------|-----|-----|
| **Propósito** | Agente → Ferramentas externas | Agente ↔ Editor |
| **Exemplo** | LangChain chama API via MCP | Claude Code em VS Code via ACP |
| **Comunição** | Bidirecional (ferramentas) | Bidirecional (editor) |
| **Use case** | Integração com serviços | Integração com IDEs |

**MCP:** "Chame minha ferramenta"  
**ACP:** "Controle meu editor"

## Como Funciona

ACP opera em modo **stdio** - o servidor ACP lê requisições da entrada padrão e escreve respostas na saída padrão:

```
Editor (Cliente ACP)
    ↕ stdin/stdout
Agente (Servidor ACP)
    ↕ Controla editor
IDE Features
```

**Fluxo típico:**
1. Editor inicia agente (servidor ACP)
2. Editor envia: `{"method": "editText", "params": {...}}`
3. Agente processa
4. Agente retorna: `{"result": {...}}`

## Implementação Básica

### Servidor ACP (Agente)

```python
import json
import sys

class ACPServer:
    def __init__(self):
        self.tabs = {}  # Arquivos abertos
    
    async def handle_request(self, request):
        method = request["method"]
        params = request.get("params", {})
        
        if method == "getActivePath":
            return {"path": self.get_active_path()}
        
        elif method == "readFile":
            path = params["path"]
            with open(path) as f:
                return {"content": f.read()}
        
        elif method == "editText":
            path = params["path"]
            edits = params["edits"]  # [{range, text}, ...]
            return self.apply_edits(path, edits)
        
        elif method == "executeTerminal":
            command = params["command"]
            return {"output": os.popen(command).read()}
        
        else:
            return {"error": f"Unknown method: {method}"}

# Loop principal
while True:
    line = sys.stdin.readline()
    if not line:
        break
    
    request = json.loads(line)
    response = await server.handle_request(request)
    
    sys.stdout.write(json.dumps(response) + "\n")
    sys.stdout.flush()
```

### Cliente ACP (Editor)

```typescript
// Exemplo: VS Code Extension
import { spawn } from "child_process";

class ACPClient {
    private process = spawn("python", ["./acp_server.py"]);
    
    async request(method: string, params?: any) {
        const request = { method, params };
        this.process.stdin.write(JSON.stringify(request) + "\n");
        
        return new Promise((resolve) => {
            this.process.stdout.on("data", (data) => {
                const response = JSON.parse(data.toString());
                resolve(response);
            });
        });
    }
    
    async readFile(path: string) {
        return this.request("readFile", { path });
    }
    
    async editText(path: string, edits: any[]) {
        return this.request("editText", { path, edits });
    }
}
```

## Métodos Padrão

### Leitura de Contexto

```python
"getActivePath"          # Caminho do arquivo aberto
"getActiveSelection"     # Texto selecionado
"getActiveLineNumber"    # Linha atual
"getOpenTabs"           # Lista de abas abertas
"readFile"              # Ler arquivo
"getFileRange"          # Ler parte de arquivo
```

### Modificação de Código

```python
"editText"              # Editar arquivo
"insertText"            # Inserir texto
"deleteRange"           # Deletar intervalo
"replaceText"           # Substituir
"createFile"            # Criar arquivo
"deleteFile"            # Deletar arquivo
```

### Execução

```python
"executeTerminal"       # Rodar comando
"executeTest"           # Rodar testes
"executeDebug"          # Debug
"executeFormat"         # Formatar código
```

### Notificações

```python
"showMessage"           # Mensagem ao usuário
"showError"             # Erro
"showWarning"           # Aviso
"openFile"              # Abrir arquivo
"focusFile"             # Focar arquivo
```

## Exemplo Prático: Agente de Refactoring

```python
class RefactoringAgent:
    def __init__(self, acp_client):
        self.acp = acp_client
    
    async def refactor_function(self, function_name: str):
        # 1. Ler arquivo ativo
        active_path = await self.acp.request("getActivePath")
        file_content = await self.acp.request("readFile", 
            {"path": active_path})
        
        # 2. Encontrar função
        start_line = find_function(file_content, function_name)
        func_body = extract_function(file_content, start_line)
        
        # 3. Analisar com LLM
        refactored = await llm.invoke(f"""
        Refatore esta função seguindo best practices:
        
        {func_body}
        
        Retorne apenas o código refatorado.
        """)
        
        # 4. Aplicar mudanças no editor
        edits = [{
            "range": {"start": start_line, "end": start_line + len(func_body)},
            "text": refactored
        }]
        
        await self.acp.request("editText", 
            {"path": active_path, "edits": edits})
        
        # 5. Notificar usuário
        await self.acp.request("showMessage", 
            {"text": f"✅ Refactored {function_name}"})
```

## Editores Suportados

### VS Code
Via [Claude Code extension](https://github.com/anthropics/claude-code)

```json
{
    "name": "claude-code",
    "publisher": "Anthropic",
    "version": "1.0.0"
}
```

### JetBrains IDEs
PyCharm, IntelliJ, WebStorm, etc.

### Zed
Editor moderno com ACP built-in

### Neovim
Via plugin ACP

## Padrão: Vectora como ACP Client

```python
# Vectora pode atuar como cliente ACP
class VectoraACPClient:
    def __init__(self, editor_process):
        self.editor = ACPClient(editor_process)
    
    async def analyze_current_file(self):
        # Ler arquivo aberto no editor
        content = await self.editor.readFile(
            await self.editor.request("getActivePath"))
        
        # Analisar com VCR
        analysis = await vectora_vcr.analyze(content)
        
        # Retornar contexto ao editor via gutter hints
        await self.editor.request("showAnalysis", analysis)
```

## External Linking

| Conceito | Recurso | Link |
|----------|---------|------|
| ACP Official | Agent Client Protocol | [https://modelcontextprotocol.io/clients](https://modelcontextprotocol.io/clients) |
| ACP Spec | Protocol Details | [https://modelcontextprotocol.io/client-guides](https://modelcontextprotocol.io/client-guides) |
| Claude Code | VS Code Extension | [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code) |
| Editor Support | Supported IDEs | [https://modelcontextprotocol.io/servers](https://modelcontextprotocol.io/servers) |
| Building Servers | ACP Server Guide | [https://modelcontextprotocol.io/server-guides](https://modelcontextprotocol.io/server-guides) |
