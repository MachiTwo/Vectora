---
title: Integração Paperclip
slug: paperclip
description: Plugin Vectora para orquestração de agentes multi-IA com Paperclip
keywords: [paperclip, agent orchestration, integration, plugin, vectora]
tags: [integration, plugin, orchestration, paperclip, ai-agent]
---

{{< lang-toggle >}}

A **Integração Paperclip** conecta o Vectora Decision Engine (Vectora Cognitive Runtime) ao Paperclip, uma plataforma open-source de orquestração de agentes IA. Através do plugin `@vectora/plugin-paperclip`, o Vectora Cognitive Runtime funciona como um policy orchestrator inteligente dentro de ambientes multi-agentes gerenciados pelo Paperclip.

## Arquitetura da Integração

```text
Paperclip Agent (orquestra)
    ↓
[Vectora Cognitive Runtime Policy Router] ← Decide routing inteligente
    ↓
[Vectora Tools]
  - vectora_search (busca semântica)
  - vectora_explain (explicação de código)
  - vectora_suggest (sugestões com IA)
  - vectora_health_check (monitoramento)
    ↓
[Decision Log] ← Auditável, estruturado em JSON
```

## Componentes Principais

### 1. Plugin Manifest

O arquivo `src/manifest.ts` declara:

- **ID**: `@vectora/plugin-paperclip`
- **Versão**: 0.1.0
- **Capacidades**: agent.tools.register, http.outbound, events.subscribe, ui.dashboardWidget, state, activity.log.write

### 2. Worker RPC

O `src/worker.ts` implementa handlers para:

- Inicialização com validação de configuração
- Registro de ferramentas (tools)
- Subscripção a eventos (task.created, task.completed)
- Sincronização de contexto bidirecional

### 3. Ferramentas Registradas

#### vectora_search

Busca semântica na base de conhecimento Vectora com suporte a contexto.

**Entrada:**

```typescript
{
  query: string; // Obrigatório: query de busca
  context?: string; // Opcional: contexto para guiar
  top_k?: number; // Opcional: quantos resultados (padrão: 5)
}
```

**Saída:**

```typescript
{
  results: [{
    id: string;
    content: string;
    score: number;
    metadata?: Record<string, unknown>;
  }];
  total: number;
  query: string;
}
```

#### vectora_explain

Explicação detalhada de snippets de código.

**Entrada:**

```typescript
{
  code: string; // Obrigatório: código a explicar
  language?: string; // Opcional: linguagem (typescript, python, go, etc)
}
```

**Saída:**

```typescript
{
  explanation: string;
  complexity: "simple" | "moderate" | "complex";
  language: string;
  estimatedReadTime: number;
}
```

#### vectora_suggest

Sugestões de conclusão de código com IA.

**Entrada:**

```typescript
{
  partial: string; // Obrigatório: código parcial
  count?: number; // Opcional: quantas sugestões (padrão: 3)
}
```

**Saída:**

```typescript
[{
  code: string;
  description: string;
  confidence: number;
}]
```

#### vectora_health_check

Status de saúde e conectividade do Vectora Cognitive Runtime.

**Saída:**

```typescript
{
  healthy: boolean;
  timestamp: string;
  apiUrl: string;
  latency: number;
}
```

## Configuração

O plugin requer as seguintes variáveis:

| Campo               | Tipo    | Obrigatório | Padrão | Descrição                                 |
| ------------------- | ------- | ----------- | ------ | ----------------------------------------- |
| `vectora_api_url`   | string  | Sim         | -      | URL base da API Vectora                   |
| `vectora_api_key`   | string  | Sim         | -      | Token de autenticação                     |
| `auto_sync_context` | boolean | Não         | true   | Sincronizar contexto automaticamente      |
| `decision_logging`  | boolean | Não         | true   | Log de decisões Vectora Cognitive Runtime |
| `agent_timeout_ms`  | number  | Não         | 30000  | Timeout para operações (5000-120000)      |

### Exemplo de Inicialização

```typescript
import { worker } from "@vectora/paperclip";

await worker.init({
  vectora_api_url: "https://api.vectora.cloud",
  vectora_api_key: process.env.VECTORA_API_KEY,
  auto_sync_context: true,
  decision_logging: true,
  agent_timeout_ms: 30000,
});
```

## Sincronização de Contexto

A integração oferece sincronização **bidirecional** entre:

- **Paperclip Projects** (lado orquestrador)
- **Vectora Namespaces** (lado knowledge base)

Quando habilitada (`auto_sync_context: true`):

1. Contexto de projeto Paperclip é capturado
2. Mapeado para namespace Vectora
3. Metadata e embeddings sincronizados
4. Operações registradas para auditoria

### Estrutura de Dados Sincronizados

```typescript
interface ContextSyncData {
  projectId: string;
  namespace: string;
  metadata: Record<string, unknown>;
  lastSyncAt: string;
}
```

## Log de Decisões

Quando `decision_logging: true`, cada decisão Vectora Cognitive Runtime é registrada com estrutura:

```json
{
  "traceId": "vectora-cognitive-runtime_20260427_abc123",
  "timestamp": "2026-04-27T15:30:01Z",
  "decision": {
    "action": "dispatch_to_gemini",
    "target": "gemini",
    "parameters": {
      "temperature": 0.2,
      "max_tokens": 1500
    },
    "confidence": 0.91
  },
  "observation": {
    "contextSufficiency": 0.94,
    "hallucinationRisk": 0.07
  }
}
```

Logs são:

- Escritos no activity log do Paperclip
- Persistidos para análise pós-implementação
- Disponíveis via API de auditoria
- Criptografados em repouso

## Monitoramento e Observabilidade

### Health Checks

O plugin oferece verificação de saúde via `vectora_health_check`:

```typescript
const health = await worker.healthCheck();

if (health.healthy) {
  console.log(`Latência: ${health.latency}ms`);
}
```

**Métricas rastreadas:**

- Conectividade com API Vectora
- Latência de inferência
- Taxa de sucesso de operações
- Erros por tipo

### Eventos Monitorados

O plugin subscreve eventos Paperclip:

- `agent.task.created` - Nova tarefa criada
- `agent.task.completed` - Tarefa completada

## Troubleshooting

### Plugin falha na inicialização

Verifique:

1. URL da API Vectora está correta e acessível
2. API key tem permissões válidas
3. Conectividade de rede até Vectora Cloud
4. Configuração corresponde ao schema

### Chamadas de tools fazem timeout

Se `agent_timeout_ms` for excedido:

1. Aumente o timeout (até 120000ms)
2. Verifique latência de rede
3. Consulte status da API Vectora em `/health/ready`

### Falhas na sincronização de contexto

Garanta:

1. `auto_sync_context` está habilitada
2. IDs de projeto correspondem a namespaces Vectora
3. Permissões suficientes na API key
4. Espaço em disco disponível

## Casos de Uso

### Multi-Agent Company com Vectora Cognitive Runtime

```typescript
// Paperclip orquestra múltiplos agentes
// Vectora Cognitive Runtime como policy coordinator (roteador inteligente)
const company = await paperclip.createCompany({
  name: "AI Engineering Team",
  agents: [
    { role: "code_reviewer", model: "gemini" },
    { role: "architect", model: "voyage" },
    { role: "tester", model: "claude" },
  ],
  policyCoordinator: vectoraVectora Cognitive Runtime,
});

// Vectora Cognitive Runtime decide automaticamente qual agente usar baseado em query
```

### Search Augmentation Workflow

```typescript
// User query
const query = "como validar JWT em Go?";

// Vectora Cognitive Runtime enriquece com busca
const searchResults = await worker.vectoraSearch(query, "security context", 5);

// Passa para Gemini com contexto aumentado
const response = await gemini.generate({
  prompt: query,
  context: searchResults.results.map((r) => r.content).join("\n"),
});
```

### Code Generation with Suggestions

```typescript
// User partial code
const partial = "const validateEmail = (email: string) => {";

// Vectora Cognitive Runtime sugere completions
const suggestions = await worker.vectoraSuggest(partial, 3);

// Apresenta opções ao usuário
suggestions.forEach((s) => {
  console.log(` ${s.code} (confiança: ${s.confidence})`);
});
```

## Roadmap Futuro

### Fase 10: Continuous Training Loop

- Coleta automática de traces de produção
- Retreinamento mensal com novos dados
- A/B testing de novas políticas

### Fase 11: Observabilidade em Tempo Real

- Dashboard Grafana com métricas Vectora Cognitive Runtime
- Alertas automáticos (hallucination_rate > 5%)
- Breakdown por decision_type

### Fase 12: Multi-Tenant Policy Variants

- Políticas customizadas por cliente enterprise
- Fine-tuning específico de domínio (healthcare, finance)

## External Linking

| Concept           | Resource                                | Link                                                                                   |
| ----------------- | --------------------------------------- | -------------------------------------------------------------------------------------- |
| **TypeScript**    | Official TypeScript Handbook            | [www.typescriptlang.org/docs/](https://www.typescriptlang.org/docs/)                   |
| **Gemini AI**     | Google DeepMind Gemini Models           | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**    | Google AI Studio Documentation          | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **Observability** | Control Theory and System Observability | [en.wikipedia.org/wiki/Observability](https://en.wikipedia.org/wiki/Observability)     |
| **JWT**           | RFC 7519: JSON Web Token Standard       | [datatracker.ietf.org/doc/html/rfc7519](https://datatracker.ietf.org/doc/html/rfc7519) |
| **Voyage AI**     | High-performance embeddings for RAG     | [www.voyageai.com/](https://www.voyageai.com/)                                         |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
