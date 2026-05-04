---
title: "Vectora Cognitive Runtime (VCR)"
slug: vectora-cognitive-runtime
date: "2026-05-03T10:15:00-03:00"
draft: false
categories:
  - Deep Dive
tags:
  - vcr
  - pytorch
  - xlm-roberta
  - lora
  - fine-tuning
  - ai
  - architecture
  - concepts
  - context-engine
  - decision-engine
  - embeddings
  - rag
  - reranker
  - routing
  - security
  - state
  - system
  - tools
  - vectora
type: docs
sidebar:
  open: true
---

{{< lang-toggle >}}

{{< section-toggle >}}

O **Vectora Cognitive Runtime (VCR)** é o motor de decisão local do Vectora. Construído sobre PyTorch + XLM-RoBERTa-small com LoRA fine-tuning, VCR valida cada decisão do agente, calcula confiança e orquestra políticas de recuperação sem depender de nenhum serviço externo. Latência < 10ms p99 em CPU — sem GPU necessária.

## Papel na Arquitetura

VCR opera como camada de controle entre Deep Agents e Context Engine, validando decisões antes de executar ferramentas ou retornar respostas:

```text
Usuário / IDE
    |
    +-> Deep Agents (Planejamento LangChain)
    |
    +-> VCR Interceptor (Valida plano)
    |
    +-> Context Engine (Busca LanceDB)
    |
    +-> VCR Observer (Valida contexto)
    |
    +-> LLM Externo (Opcional: Claude, GPT-4)
    |
    +-> VCR Validator (Valida resposta)
    |
    +-> Resposta Final
```

VCR nunca bloqueia — ele produz decisões estruturadas que Deep Agents executa. Se VCR cair, Deep Agents usa políticas de fallback determinísticas.

## Especificação Técnica

| Componente          | Especificação                        |
| ------------------- | ------------------------------------ |
| **Modelo Base**     | `xlm-roberta-small` (Hugging Face)   |
| **Parâmetros**      | 110M (base) + ~2.2M LoRA adapters    |
| **Fine-tuning**     | LoRA (`r=16, alpha=32, dropout=0.1`) |
| **Runtime**         | PyTorch 2.1+ com quantização INT8    |
| **Latência Target** | <10ms p99 em CPU                     |
| **Memória**         | <500MB RAM (INT8 quantizado)         |
| **GPU**             | Opcional — CPU-only em produção      |
| **Framework**       | PyTorch + Transformers (HuggingFace) |

## Por Que XLM-RoBERTa-small?

XLM-RoBERTa-small foi escolhido por três motivos:

1. **Multilíngue**: Suporte nativo a 100 idiomas, incluindo PT-BR. Sem adaptação necessária.
2. **CPU-Friendly**: 110M parâmetros é suficiente para classificação tática sem necessitar GPU.
3. **Licença MIT**: Sem restrições de uso comercial ou redistribuição.

O modelo é fine-tunado com LoRA para maximizar accuracy em tarefas de classificação de relevância, roteamento de contexto e detecção de alucinações, sem treinar todos os pesos.

## Fine-tuning com LoRA

### Configuração LoRA

```python
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["query", "value"],
    lora_dropout=0.1,
    bias="none",
    task_type="SEQ_CLS",
)

model = get_peft_model(base_model, lora_config)
```

### Dataset de Treino

- **Volume**: 5k traces reais + 15k exemplos sintéticos de falha
- **Tarefas**: Classificação binária de relevância, detecção de alucinação, routing decisions
- **Formato**: Triplas (query, context, label) onde label é 0 (irrelevante) ou 1 (relevante)
- **Split**: 80% treino, 10% validação, 10% teste

### Processo de Treino

```python
training_args = TrainingArguments(
    output_dir="./vcr-model",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    learning_rate=2e-4,
    warmup_steps=100,
    evaluation_strategy="epoch",
    save_strategy="best",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
)

trainer.train()
```

## Quantização INT8

Após o fine-tuning, VCR é quantizado para INT8 para reduzir memória e aumentar throughput em CPU:

```python
import torch

# Dynamic quantization — sem dados de calibração necessários
quantized_model = torch.quantization.quantize_dynamic(
    model,
    {torch.nn.Linear},
    dtype=torch.qint8
)

# Salvar modelo quantizado
quantized_model.save_pretrained("vcr-model-int8")
```

Impacto:

| Métrica          | FP32 (base) | INT8 (quantizado) |
| ---------------- | ----------- | ----------------- |
| **Tamanho**      | ~450MB      | ~120MB            |
| **Latência p99** | ~25ms       | ~8ms              |
| **Accuracy**     | 88.2%       | 87.9% (queda <1%) |

## Capacidades Principais

### 1. Validação de Plano

Antes de Deep Agents executar um plano, VCR valida se o plano faz sentido dado o contexto disponível:

```python
vcr_decision = vcr.validate_plan(
    plan=agent_plan,
    context=current_context,
)
# Output: {"action": "execute", "confidence": 0.92, "trace_id": "vcr_xxx"}
```

### 2. Scoring de Relevância

VCR classifica candidatos de busca com score de relevância binário:

```python
scores = vcr.score_relevance(
    query="Como validar tokens JWT?",
    candidates=lancedb_top100_results
)
# Output: [{chunk_id: 1, score: 0.94}, {chunk_id: 2, score: 0.87}, ...]
top10 = [c for c in scores if c["score"] > 0.65][:10]
```

### 3. Detecção de Alucinação

VCR compara resposta do LLM externo com contexto injetado:

```python
validation = vcr.validate_response(
    response=llm_response,
    injected_context=context_chunks,
)
# Output: {"faithfulness": 0.89, "hallucination_risk": 0.11, "accept": True}
```

### 4. Políticas de Recuperação

Se confidence < threshold, VCR decide a política de recuperação:

```python
recovery = vcr.recovery_policy(
    confidence=0.45,
    context_precision=0.52,
)
# Output: {"action": "expand_search", "new_top_k": 200, "strategy": "hybrid"}
```

## Decisões Estruturadas (Output Schema)

VCR sempre retorna JSON auditável:

```json
{
  "trace_id": "vcr_20260503_a1b2c3",
  "timestamp": "2026-05-03T14:32:01Z",
  "decision": {
    "action": "execute_plan",
    "parameters": { "temperature": 0.3, "max_tokens": 1500 },
    "confidence": 0.91
  },
  "observation": {
    "context_sufficiency": 0.94,
    "hallucination_risk": 0.07,
    "requires_expansion": false
  },
  "recovery_hint": {
    "if_failed": "expand_search",
    "fallback_top_k": 200,
    "max_retry_attempts": 2
  },
  "metadata": {
    "model_version": "vcr-xlm-roberta-v1-int8",
    "inference_latency_ms": 7.4
  }
}
```

## Configuração

```yaml
# vectora.config.yaml
vcr:
  enabled: true
  model_path: "models/vcr-xlm-roberta-v1-int8"
  confidence_threshold: 0.70
  max_inference_ms: 15
  fallback_policy: "heuristics"
  logging: true
  metrics:
    prometheus: true
    port: 9090
```

## Endpoints FastAPI

VCR é exposto via FastAPI com endpoints REST:

- `POST /vcr/validate-plan` — Validar plano de execução
- `POST /vcr/score-relevance` — Scoring de candidatos de busca
- `POST /vcr/validate-response` — Detecção de alucinação
- `POST /vcr/recovery-policy` — Política de recuperação
- `GET /vcr/health` — Health check e status do modelo
- `GET /vcr/metrics` — Prometheus metrics

## Métricas de Sucesso

| Métrica                   | Target | Impacto                             |
| ------------------------- | ------ | ----------------------------------- |
| **Decision Accuracy**     | >=85%  | Roteamento preciso, menos loops     |
| **Inference Latency p99** | <=10ms | Zero degradação na UX               |
| **Faithfulness Score**    | >=0.80 | Respostas fundamentadas em contexto |
| **Hallucination Rate**    | <=5%   | Confiabilidade da resposta          |
| **Fallback Rate**         | <=3%   | Estabilidade em produção            |

## Segurança e Isolamento

- **Zero Chamadas de Rede**: VCR processa tudo localmente em PyTorch
- **Auditabilidade**: Cada decisão é logada como JSON estruturado
- **Resiliência**: Se VCR falhar, Deep Agents usa políticas de fallback hardcoded
- **Privacidade**: Nenhum dado de usuário é enviado a servidores externos durante inferência

## External Linking

| Conceito                | Recurso                                        | Link                                                                                           |
| ----------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **XLM-RoBERTa**         | Modelo multilíngue de código aberto            | [huggingface.co/xlm-roberta-small](https://huggingface.co/xlm-roberta-small)                   |
| **PyTorch**             | Framework de deep learning                     | [pytorch.org/docs](https://pytorch.org/docs)                                                   |
| **LoRA**                | Low-Rank Adaptation para fine-tuning eficiente | [arxiv.org/abs/2106.09685](https://arxiv.org/abs/2106.09685)                                   |
| **PEFT**                | HuggingFace PEFT library para LoRA             | [github.com/huggingface/peft](https://github.com/huggingface/peft)                             |
| **Quantização PyTorch** | Dynamic INT8 quantization                      | [pytorch.org/docs/stable/quantization.html](https://pytorch.org/docs/stable/quantization.html) |
