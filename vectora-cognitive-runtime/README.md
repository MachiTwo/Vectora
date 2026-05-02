# Vectora Cognitive Runtime: Vectora Decision Engine (Python)

Vectora Cognitive Runtime é um Small Language Model (SLM) especializado em decisão contextual que intercepta queries do usuário, enriquece com contexto estruturado, decide qual estratégia usar (Agent Mode vs Tool Mode vs Web Search), e orquestra toda a pipeline de RAG. Funciona como micro LLM (~35MB ONNX INT4) rodando em CPU local com latência de 4-8ms. Integrado ao backend Go via subprocess (Phase 1) ou gRPC (Phase 4+).

## Stack

Vectora Cognitive Runtime usa PyTorch como framework de deep learning, Hugging Face Transformers para carregar modelos, PEFT para efficient fine-tuning via LoRA, e ONNX Runtime para inference otimizado. Modelo base é SmolLM2-135M-Instruct, fine-tuned com dados sintéticos (Phase 1) e traces reais (Phase 2+), quantizado para INT4 (~35MB), e calibrado para probabilidades acuradas (ECE <= 0.05).

- Framework: PyTorch 2.1+ (training), ONNX Runtime (inference)
- Model Base: SmolLM2-135M-Instruct (135M params)
- Fine-Tuning: PEFT with LoRA (r=16, alpha=32)
- Quantization: INT4 (35MB final)
- Inference: 4-8ms p95 (CPU)
- Training Data: Synthetic (Phase 1) -> Real traces (Phase 2+)
- Evaluation: Accuracy >= 85%, ECE <= 0.05, Fallback <= 2%

## Mapa Mental

Pipeline completo: receive query -> enrich com chunks + memory -> Vectora Cognitive Runtime inference (ONNX) -> output JSON {action, parameters, confidence, recovery_hint}. Decision pode ser Agent Mode, Tool Mode, Web Search, ou qual LLM usar. Se confidence < 0.70, recovery automático.

```
User Query
    |
    +-- Enrich: LanceDB + memory
    |
    V
[Vectora Cognitive Runtime ONNX INT4 - 4-8ms]
    |
    +-- Output: {action, params, confidence}
    |
    V
Confidence >= 0.70?
    |
    +-- YES: Execute decision
    |
    +-- NO: Recovery (expand_search, retry, fallback)
    |
    V
Cache + store in memory
    |
    V
Response to Agent
```

## Estrutura

Subdiretório /backend/vectora-cognitive-runtime/ com scripts para training, source code para runtime, data para datasets, models para checkpoints e final ONNX.

```
backend/vectora-cognitive-runtime/
├── scripts/
│   ├── download_base.py
│   ├── build_dataset.py
│   ├── train.py
│   ├── calibrate.py
│   ├── export_onnx.py
│   └── benchmark.py
├── src/
│   ├── feature_builder.py
│   ├── model.py
│   ├── decision.py
│   ├── recovery.py
│   └── __init__.py
├── data/
│   ├── raw/
│   │   └── production_traces.jsonl
│   └── processed/
│       ├── train_set.jsonl
│       ├── val_set.jsonl
│       └── test_set.jsonl
├── models/
│   ├── base/
│   │   └── SmolLM2-135M-Instruct/
│   ├── checkpoints/
│   │   ├── epoch_1/
│   │   ├── epoch_5/
│   │   └── final/
│   └── vectora-cognitive-runtime-policy-v1-int4.onnx
├── evaluation/
│   ├── golden_queries.jsonl
│   ├── metrics.py
│   └── test_production_readiness.py
├── inference.py
├── server.py (Phase 4+: gRPC)
├── requirements.txt
├── .env.example
├── config.yaml
└── README.md
```

---

## Training Pipeline

Phase 1 (Synthetic):
```bash
python scripts/download_base.py
python scripts/build_dataset.py --synthetic
python scripts/train.py
python scripts/calibrate.py
python scripts/export_onnx.py
```

Phase 2+ (Real Data):
```bash
python scripts/build_dataset.py --real --traces production_traces.jsonl
python scripts/train.py --epochs 10
python scripts/calibrate.py
python scripts/export_onnx.py
```

## License

Apache 2.0
