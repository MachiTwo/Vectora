---
title: "Frontend: React 19 + TypeScript"
slug: frontend
date: "2026-05-03T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - frontend
  - react
  - typescript
  - ui
  - vectora
draft: false
---

{{< lang-toggle >}}

{{< section-toggle >}}

O frontend do Vectora é uma SPA React 19 com TypeScript, Vite e TanStack Query. Comunica com o backend via REST API em `http://localhost:8000`. Autenticação via JWT Bearer — o token é armazenado em memória (não em localStorage) para prevenir XSS.

## Stack

| Tecnologia          | Versão | Responsabilidade             |
| ------------------- | ------ | ---------------------------- |
| **React**           | 19     | Componentes e estado UI      |
| **TypeScript**      | 5.x    | Tipagem estática             |
| **Vite**            | 6.x    | Build tool e dev server      |
| **TanStack Query**  | 5.x    | Server state, cache, refetch |
| **TanStack Router** | 1.x    | Type-safe routing            |

## Estrutura de Diretórios

```text
vectora/frontend/
  src/
    api/          # Clientes HTTP (search, agent, auth)
    components/   # Componentes reutilizáveis
    hooks/        # Hooks customizados (useSearch, useAgent)
    pages/        # Páginas (Search, AgentRun, Settings)
    store/        # Estado global (auth token)
    types/        # TypeScript types compartilhados
  index.html
  vite.config.ts
  tsconfig.json
```

## Cliente API

Todas as chamadas HTTP passam por um cliente base com injeção automática do Bearer token.

```typescript
const BASE_URL = "http://localhost:8000";

let accessToken: string | null = null;

export function setToken(token: string): void {
  accessToken = token;
}

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
    ...(accessToken ? { Authorization: `Bearer ${accessToken}` } : {}),
  };

  const response = await fetch(`${BASE_URL}${path}`, {
    ...options,
    headers,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new ApiError(response.status, error.detail ?? "Unknown error");
  }

  return response.json() as Promise<T>;
}
```

## Hook de Busca

```typescript
import { useMutation } from "@tanstack/react-query";

interface SearchResult {
  id: string;
  file: string;
  lines: string;
  score: number;
  content: string;
}

interface SearchResponse {
  results: SearchResult[];
  metadata: {
    total_latency_ms: number;
    strategy_used: string;
  };
}

export function useSearch() {
  return useMutation({
    mutationFn: (query: string) =>
      request<SearchResponse>("/api/v1/search", {
        method: "POST",
        body: JSON.stringify({ query, top_k: 10, strategy: "auto" }),
      }),
  });
}
```

## Hook de Agente com Streaming

```typescript
export function useAgentStream(onChunk: (chunk: string) => void) {
  const stream = async (query: string) => {
    const response = await fetch(`${BASE_URL}/api/v1/agent/run/stream`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
      },
      body: JSON.stringify({ query }),
    });

    const reader = response.body!.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      const lines = decoder.decode(value).split("\n");
      for (const line of lines) {
        if (line.startsWith("data: ")) {
          const data = JSON.parse(line.slice(6));
          if (data.type === "response") onChunk(data.content);
        }
      }
    }
  };

  return { stream };
}
```

## Autenticação

O token JWT é armazenado em memória (variável de módulo) — não em `localStorage` ou cookies. Isso previne acesso via XSS mas requer novo login após reload da página.

```typescript
import { useMutation } from "@tanstack/react-query";

export function useLogin() {
  return useMutation({
    mutationFn: async (credentials: { email: string; password: string }) => {
      const data = await request<{ access_token: string }>("/auth/login", {
        method: "POST",
        body: JSON.stringify(credentials),
      });
      setToken(data.access_token);
      return data;
    },
  });
}
```

## Desenvolvimento

```bash
cd vectora/frontend
npm install
npm run dev      # http://localhost:5173
npm run build    # dist/
npm run typecheck # tsc --noEmit
```

O proxy Vite redireciona `/api/*` para `http://localhost:8000` em desenvolvimento, evitando CORS.

```typescript
// vite.config.ts
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/api": "http://localhost:8000",
      "/auth": "http://localhost:8000",
      "/vcr": "http://localhost:8000",
    },
  },
});
```

## External Linking

| Conceito            | Recurso                  | Link                                                                                                      |
| ------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------- |
| **React 19**        | React documentation      | [react.dev](https://react.dev/)                                                                           |
| **TanStack Query**  | Server state management  | [tanstack.com/query](https://tanstack.com/query/latest)                                                   |
| **TanStack Router** | Type-safe routing        | [tanstack.com/router](https://tanstack.com/router/latest)                                                 |
| **Vite**            | Build tool documentation | [vitejs.dev](https://vitejs.dev/)                                                                         |
| **SSE**             | Server-Sent Events       | [html.spec.whatwg.org/server-sent-events](https://html.spec.whatwg.org/multipage/server-sent-events.html) |
