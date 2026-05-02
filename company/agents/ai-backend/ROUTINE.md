---
title: AI Backend Engineer - Daily/Weekly Routine
role: Vectora Cognitive Runtime AI Backend Engineer
focus: Vector search engine, embeddings, RAG pipeline
---

# AI Backend Engineer Routine

## Daily (10:00 AM UTC - Daily Standup)

**Status**: Async (secondary to 5 critical issues)

- [ ] Check Vectora Cognitive Runtime service health
- [ ] Monitor embedding pipeline
- [ ] Review any AI-related GitHub issues

---

## Weekly Schedule

### Q2 Focus: Vectora Cognitive Runtime (Vector Search Engine)

**Issue-Based Timeline** (after Critical 5 resolved):

**Week 1** (May 6-10):

- [ ] Finalize SmolLM2-135M ONNX quantization
- [ ] Benchmark token generation latency (target: < 2s)
- [ ] Optimize for CPU efficiency

**Week 2-3** (May 13-24):

- [ ] Implement vector search with Voyage embeddings
- [ ] Test similarity search: 10k vectors, < 50ms latency
- [ ] Build RAG pipeline with context retrieval

**Week 4** (May 27-31):

- [ ] Optimize MongoDB Vector Search indexes
- [ ] Performance testing: 1M vector corpus
- [ ] Prepare for production deployment

---

## KR Targets (from Issue #009)

**KR1**: SmolLM2-135M quantization complete

- Model loaded in ONNX
- Latency < 2s per token
- Mobile-ready (< 500MB)

**KR2**: Vector search implementation

- Similarity search working end-to-end
- 10k vectors, < 50ms search latency
- RAG pipeline operational

**KR3**: MongoDB Vector Search optimization

- Query latency 30% faster than baseline
- 1M vector corpus supported
- Index memory-efficient

---

## Tech Stack

- **Model**: SmolLM2-135M (Voyage AI)
- **Quantization**: ONNX Runtime
- **Vector Store**: MongoDB Vector Search
- **Language**: Python (FastAPI backend)
- **Framework**: Transformers, ONNX, llama-cpp-python

---

## Current State

**SmolLM2 Setup**:

```python
# Load quantized model
import onnxruntime as ort

model_path = "models/SmolLM2-135M-quantized.onnx"
session = ort.InferenceSession(model_path)

# Generate tokens
input_ids = tokenizer.encode("Your prompt")
output = session.run(None, {"input_ids": input_ids})
```

**Embedding Pipeline**:

```python
from voyageai import EmbeddingModel

voyage = EmbeddingModel("voyage-lite-02")
embeddings = voyage.embed(documents, model="voyage-lite-02")
```

---

## Monthly Milestones

**May 15**: SmolLM2 quantization complete + benchmarked
**May 31**: Vector search fully working + RAG pipeline
**June 15**: Production-ready with optimized indexes

---

## Resources

- **SmolLM2**: https://huggingface.co/HuggingFaceM4/SmolLM2-135M
- **Voyage AI**: https://www.voyageai.com/
- **ONNX Runtime**: https://onnxruntime.ai/
- **MongoDB Vector Search**: https://www.mongodb.com/docs/atlas/atlas-vector-search/

---

**Start**: After critical 5 issues (May 6)
**Priority**: MEDIUM (Vectora Cognitive Runtime is core, not blocking)
**Owner**: AI Backend Engineer
