# Vectora Cognitive Runtime

Vectora Cognitive Runtime é um encoder de texto especializado em decisão contextual que intercepta queries do usuário, enriquece com contexto estruturado, decide qual estratégia usar (Agent Mode vs Tool Mode vs Web Search), e orquestra toda a pipeline de RAG. Usa XLM-RoBERTa-small como base pré-treinada multilíngue, fine-tuned com LoRA para classificação binária/multiclasse. Integrado ao backend Go via subprocess (Phase 1) ou gRPC (Phase 4+).

## Stack

Vectora Cognitive Runtime usa PyTorch como framework de deep learning, Hugging Face Transformers para carregar e fine-tunar modelos, PEFT (LoRA) para efficient fine-tuning sem armazenar pesos completos duplicados. Modelo base é XLM-RoBERTa-small (24M parâmetros, multilíngue nativo para 101 idiomas incluindo PT-BR), fine-tuned com dados sintéticos (Phase 1) e traces reais em produção (Phase 2+).

- **Framework:** PyTorch 2.1+ (training + inference Phase 1)
- **Model Base:** XLM-RoBERTa-small (24M params, 101 langs)
- **Fine-Tuning:** PEFT with LoRA (r=8, alpha=16) — apenas ~2M params adicionais
- **Deployment Phase 1:** PyTorch native (transformers library)
- **Deployment Phase 4+:** ONNX Runtime (opcional, para edge/mobile)
- **Training Data:** Synthetic (Phase 1) → Real production traces (Phase 2+)
- **Target Metrics:** Decision accuracy >= 85%, confidence calibration reliable, fallback rate < 5%

## Mapa Mental

Pipeline completo: recebe query → enriquece com chunks de LanceDB + contexto de memory → XLM-RoBERTa-small + classification head → output JSON `{action, parameters, confidence, recovery_hint}`. Decision pode ser Agent Mode (full RAG), Tool Mode (retorna chunks), Web Search, ou Recovery (expand context). Se confidence baixa, fallback automático.

```
User Query (multilíngue)
    |
    +-- Enrich: LanceDB chunks + memory context
    |
    V
[XLM-RoBERTa-small encoder]
    |
    +-- [Classification Head]
    |    └─ 4 outputs: Agent Mode | Tool Mode | Web Search | Recovery
    |
    +-- Output: {action, params, confidence}
    |
    V
Confidence >= threshold?
    |
    +-- YES: Execute strategy
    |
    +-- NO: Recovery (expand_search, retry LLM, fallback)
    |
    V
Cache decision + store in memory
    |
    V
Response to Backend (JSON)
```

**Decisões suportadas:**

- `agent_mode`: Full RAG pipeline (busca → rerank → contexto → LLM)
- `tool_mode`: Retorna chunks + ferramentas estruturadas (knowledge.store, memory.query, rerank)
- `web_search`: Integra web search (SerpAPI) antes de RAG
- `recovery`: Expande busca, retenta com contexto diferente, fallback para padrão

## Estrutura

Subdiretório `vectora/vectora-cognitive-runtime/` com scripts para training, source code para runtime e inference, data para datasets sintéticos e reais, models para checkpoints durante training.

```
vectora/vectora-cognitive-runtime/
├── scripts/
│   ├── download_base.py               (Download XLM-RoBERTa-small)
│   ├── build_dataset.py               (Synthetic Phase 1 | Real Phase 2+)
│   ├── train.py                       (Fine-tune com LoRA)
│   ├── eval.py                        (Evaluate accuracy, confidence calibration)
│   └── export_onnx.py                 (Export to ONNX — Phase 4+ optional)
├── src/
│   ├── model.py                       (XLM-RoBERTa-small + classification head)
│   ├── decision.py                    (Decision logic: Agent/Tool/Web/Recovery)
│   ├── recovery.py                    (Fallback strategies quando confidence < threshold)
│   ├── inference.py                   (Inference loop — Phase 1)
│   ├── server.py                      (gRPC server — Phase 4+)
│   └── __init__.py
├── data/
│   ├── raw/
│   │   ├── synthetic_queries.jsonl    (Phase 1: synthetic training data)
│   │   └── production_traces.jsonl    (Phase 2+: real traces from production)
│   └── processed/
│       ├── train_set.jsonl            (Tokenized, ready for training)
│       ├── val_set.jsonl              (Validation set)
│       └── test_set.jsonl             (Test set for evaluation)
├── models/
│   ├── checkpoints/
│   │   ├── lora_r8_a16_epoch1/        (LoRA checkpoint após epoch 1)
│   │   ├── lora_r8_a16_epoch3/        (LoRA checkpoint após epoch 3)
│   │   └── lora_r8_a16_final/         (Final LoRA weights)
│   └── exports/
│       └── vcr-policy-v1.onnx         (Phase 4+: ONNX quantized)
├── evaluation/
│   ├── golden_queries.jsonl           (Hand-curated test cases)
│   ├── metrics.py                     (Calculate accuracy, precision, recall, F1)
│   └── test_production_readiness.py   (Benchmark antes de deploy)
├── config.yaml                        (Model hyperparameters, paths)
├── requirements.txt                   (Python dependencies)
├── .env.example                       (Environment variables template)
├── Makefile                           (Build targets: train, eval, export)
└── README.md
```

---

## Workflow: Development → Training → Inference

### Setup Inicial

```bash
cd vectora/vectora-cognitive-runtime

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download base model (one-time)
python scripts/download_base.py
```

### Phase 1: Synthetic Data Training

Treina VCR com dados sintéticos gerados (queries simuladas + decisões esperadas).

```bash
# 1. Build synthetic dataset
python scripts/build_dataset.py --synthetic --output data/processed/

# 2. Train com LoRA (r=8, alpha=16)
#    - Fine-tunes apenas ~2M additional params
#    - Salva checkpoints a cada epoch
python scripts/train.py \
  --model FacebookAI/xlm-roberta-small \
  --dataset data/processed/train_set.jsonl \
  --val_dataset data/processed/val_set.jsonl \
  --epochs 3 \
  --batch_size 32 \
  --lora_r 8 \
  --lora_alpha 16

# 3. Evaluate no test set
python scripts/eval.py \
  --model models/checkpoints/lora_r8_a16_final/ \
  --test_dataset data/processed/test_set.jsonl

# 4. Ready for Phase 2
```

### Phase 2+: Real Production Data

Quando backend está rodando em produção, coletar traces reais.

```bash
# 1. Collect production traces
#    (Backend logs: query, context, ground_truth_decision)

# 2. Build dataset from real traces
python scripts/build_dataset.py \
  --real \
  --traces data/raw/production_traces.jsonl \
  --output data/processed/

# 3. Fine-tune com real data (continua do Phase 1)
python scripts/train.py \
  --model FacebookAI/xlm-roberta-small \
  --lora_checkpoint models/checkpoints/lora_r8_a16_final/ \
  --dataset data/processed/train_set.jsonl \
  --val_dataset data/processed/val_set.jsonl \
  --epochs 5 \
  --batch_size 16 \
  --learning_rate 1e-4

# 4. Evaluate e deploy se accuracy OK
python scripts/eval.py --model models/checkpoints/lora_r8_a16_final/
```

---

## Inference: Backend Integration

### Phase 1: Python Subprocess

Backend Go chama VCR via subprocess.

```python
# vectora-cognitive-runtime/src/inference.py
import json
import sys
import torch
from transformers import AutoTokenizer, AutoModel
from peft import PeftModel

# Load base model + LoRA weights
model = AutoModel.from_pretrained("FacebookAI/xlm-roberta-small")
model = PeftModel.from_pretrained(model, "models/checkpoints/lora_r8_a16_final/")
tokenizer = AutoTokenizer.from_pretrained("FacebookAI/xlm-roberta-small")
model.eval()

# Read input from stdin (JSON)
input_data = json.loads(sys.stdin.read())
query = input_data["query"]
context = " ".join(input_data["context"])
combined = f"{query} [SEP] {context}"

# Tokenize
inputs = tokenizer(
    combined,
    return_tensors="pt",
    padding=True,
    truncation=True,
    max_length=512
)

# Inference
with torch.no_grad():
    outputs = model(**inputs)
    cls_output = outputs.last_hidden_state[:, 0, :]  # [CLS] token
    logits = classifier(cls_output)

    decision_id = logits.argmax(dim=-1).item()
    confidence = logits.softmax(dim=-1).max().item()

    # Map decision_id to action
    action_map = {
        0: "agent_mode",
        1: "tool_mode",
        2: "web_search",
        3: "recovery"
    }

# Output to stdout (JSON)
output = {
    "action": action_map[decision_id],
    "confidence": float(confidence),
    "decision_id": decision_id
}
print(json.dumps(output))
```

Backend Go integration:

```go
// backend/internal/core/vcr/service.go
func (s *VCRService) Decide(ctx context.Context, query string, context []string) (*Decision, error) {
	cmd := exec.CommandContext(ctx, "python", "vectora-cognitive-runtime/src/inference.py")

	input := map[string]interface{}{
		"query":   query,
		"context": context,
	}

	inputJSON, _ := json.Marshal(input)
	cmd.Stdin = bytes.NewReader(inputJSON)

	output, err := cmd.Output()
	if err != nil {
		return nil, err
	}

	var result Decision
	json.Unmarshal(output, &result)
	return &result, nil
}
```

### Phase 4+: gRPC Server (Optional)

Para melhor performance em produção, VCR roda como servidor gRPC separado.

```bash
python src/server.py --port 50051
```

Backend Go chama via gRPC:

```go
client := pb.NewVCRServiceClient(conn)
response, err := client.Decide(ctx, &pb.DecideRequest{
	Query:   "React hooks",
	Context: []string{"useState", "useEffect"},
})
```

---

## Multilingual Support

XLM-RoBERTa-small suporta 101 idiomas nativamente. Fine-tuning funciona para qualquer idioma.

**Treinar com dados multilíngues (Phase 2+):**

```bash
python scripts/build_dataset.py \
  --real \
  --traces data/raw/production_traces_multilang.jsonl \
  --languages pt-br,en,es,fr \
  --output data/processed/
```

---

## Deployment Options

### Option A: PyTorch (Phase 1 — Recommended)

Simples, nativo, sem conversão.

**Vantagens:**

- Setup mínimo
- Fine-tuning direto
- Debugging fácil

**Uso:**

```bash
python src/inference.py < input.json > output.json
```

### Option B: ONNX (Phase 4+ — Optional)

Quantizado, para edge/mobile.

**Export:**

```bash
python scripts/export_onnx.py \
  --model models/checkpoints/lora_r8_a16_final/ \
  --quantize int8 \
  --output models/exports/vcr-policy-v1.onnx
```

---

## License

Apache 2.0
