---
title: AI/ML Engineer - Daily/Weekly Routine
role: AI/ML Engineer
focus: Model optimization, quantization, performance tuning
---

# AI/ML Engineer Routine

## Daily (10:00 AM UTC - Daily Standup)

**Status**: Async (specialized research)

- [ ] Monitor model performance
- [ ] Track optimization experiments
- [ ] Review research papers on vector search

---

## Q2 Focus: Model Optimization

### SmolLM2-135M Optimization

**Target KR1** (from Issue #009):

- Quantized model in ONNX
- Token generation < 2s (CPU)
- Mobile-ready (< 500MB)

**Your Work**:

- [ ] ONNX quantization (int8/int4)
- [ ] Performance benchmarking
- [ ] Memory optimization
- [ ] Latency profiling

**Tools**:

- ONNX Runtime
- Quantization libraries (onnxruntime, transformers)
- Benchmarking tools (torch profiler)

---

## Weekly Schedule

**Week 1-2** (Apr 28 - May 10):

- [ ] Baseline performance of SmolLM2
- [ ] Try int8 quantization
- [ ] Test int4 (more aggressive)
- [ ] Profile memory usage
- [ ] Benchmark on CPU vs GPU

**Week 3-4** (May 13-31):

- [ ] Finalize quantization strategy
- [ ] Optimize for deployment
- [ ] Mobile compatibility check
- [ ] Document optimization results

---

## Embedding Model Research

**Voyage AI Integration**:

- Evaluate embedding models (voyage-lite-02 vs voyage-3)
- Test embedding quality vs speed trade-off
- Plan for local embedding (if needed)

---

## Metrics to Track

| Metric            | Target        | Current |
| ----------------- | ------------- | ------- |
| Token Latency     | < 2s          | TBD     |
| Model Size        | < 500MB       | TBD     |
| Quantization Loss | < 5% accuracy | TBD     |
| Memory Usage      | < 1GB         | TBD     |

---

## Resources

- **ONNX**: https://onnx.ai/
- **SmolLM2**: https://huggingface.co/HuggingFaceM4/SmolLM2-135M
- **Quantization**: https://huggingface.co/docs/transformers/quantization
- **Benchmarking**: https://pytorch.org/docs/stable/profiler.html

---

**Start**: Week of May 6
**Priority**: MEDIUM (AI is core to Vectora Cognitive Runtime)
**Owner**: AI/ML Engineer
