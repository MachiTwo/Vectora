# 📋 ISSUES - Padrão de Qualidade & Delegação

Este arquivo define o padrão de qualidade para criação, documentação e delegação de issues no Vectora.

---

## 📐 Padrão de Arquivo

### Nomenclatura
- **Formato:** `NNN-titulo-em-lowercase-com-hifen.md`
- **Número:** 3 dígitos, ordem crescente (001, 002, 003...)
- **Título:** Lowercase, separado por hífen, descritivo e conciso
- **Exemplo:** `001-implementar-authmiddleware.md`

### Estrutura Obrigatória

```markdown
# [NNN] Título da Issue (em português)

**Número:** NNN  
**Status:** OPEN / IN_PROGRESS / BLOCKED / REVIEW / DONE  
**Prioridade:** 🔴 CRÍTICA / 🟡 ALTA / 🟠 MÉDIA / 🟢 BAIXA  
**Delegado a:** [FUNCTION] (ex: Lead Engineer, TCO, CMO)  
**Esforço Estimado:** X-Y horas  
**Deadline:** Data (dd de mês)  
**Criado em:** Data  
**Atualizado em:** Data  

---

## 📝 Descrição

[Parágrafo claro explicando o problema, contexto e impacto]

---

## 🎯 Objetivo

[O que precisa ser feito e por que]

---

## ✅ Critério de Aceitação

- [ ] Critério 1
- [ ] Critério 2
- [ ] Critério 3
- [ ] Todos testes passam
- [ ] Documentação atualizada
- [ ] Code review aprovado

---

## 📋 Tarefas / Subtasks

### Subtask 1: Descrição
- [ ] Ação 1
- [ ] Ação 2

### Subtask 2: Descrição
- [ ] Ação 1
- [ ] Ação 2

---

## 🔗 Dependências

- Depende de: [Issue XXX]
- Bloqueia: [Issue YYY]
- Relacionada: [Issue ZZZ]

---

## 📚 Referências

- [Link para arquivo] - Descrição
- [Link para documentação] - Descrição

---

## 💬 Notas

[Qualquer informação adicional, insights, ou decisões tomadas]

---

## 📊 Progresso

| Data       | Status | Nota         |
| ---------- | ------ | ------------ |
| 28/04/2026 | OPEN   | Issue criada |
| -          | -      | -            |
```

---

## 🎯 Padrão de Qualidade

### Obrigatório para TODAS as Issues

✅ **Números (3 dígitos):** 001, 002, 003... em ordem crescente  
✅ **Status claro:** OPEN, IN_PROGRESS, BLOCKED, REVIEW, DONE  
✅ **Delegado a:** Uma pessoa/role específica (não "time inteiro")  
✅ **Esforço estimado:** Sempre em horas ou dias  
✅ **Critério de aceitação:** Mínimo 3-5 critérios objetivos  
✅ **Subtasks:** Quebra em ações concretas  
✅ **Dependências:** Explicita se depende de outras issues  
✅ **Referências:** Links para código, docs, outros arquivos  

### Proibido

❌ Emojis decorativos (só use para prioridade: 🔴🟡🟠🟢)  
❌ Vagueza ("melhorar code", "fazer mais rápido")  
❌ Sem delegação clara  
❌ Critério de aceitação mal definido  
❌ Tarefas sem deadline  

---

## 👥 Delegação - Quem Pode Receber Issues

### Leadership
- **CEO** - Hiring, strategy, OKRs, go-to-market
- **TCO** - Architecture reviews, code quality, standards
- **CMO** - Marketing, growth, branding
- **Product Manager** - Feature prioritization, roadmap

### Engineering
- **Lead Engineer** - Implementation, delivery, architecture decisions
- **Backend Engineer** - Cloud APIs, databases, scaling
- **Desktop Engineer** - CLI, tray, cross-platform
- **Data Engineer** - MongoDB, schemas, indexing
- **AI/ML Engineer** - Models, quantization, optimization
- **AI Backend Engineer** - Vectora Cognitive Runtime server, inference
- **Security Engineer** - Auth, encryption, audit
- **DevOps Engineer** - CI/CD, infrastructure, monitoring
- **QA Engineer** - Testing, coverage, validation
- **Frontend Engineer** - Dashboard, UI, React
- **Interactions Engineer** - Plugins, extensions, MCP

### Other
- **Librarian** - Documentation, Hugo, SEO
- **Developer Advocate** - Community, tutorials, evangelism
- **Product Marketing** - Release notes, campaigns, copy

---

## 📋 Ciclo de Vida da Issue

```
OPEN → IN_PROGRESS → REVIEW → DONE
              ↓
           BLOCKED (volta para IN_PROGRESS)
```

### Transições

**OPEN → IN_PROGRESS:**
- Designado começou a trabalhar
- Update: "Iniciado em [data], tempo atual XX%"

**IN_PROGRESS → REVIEW:**
- Trabalho completo, passando em testes locais
- PR aberto ou está aguardando review

**REVIEW → DONE:**
- Code review aprovado
- All tests passing
- Merged to main ou live

**IN_PROGRESS → BLOCKED:**
- Depende de outra issue
- Aguardando feedback/input
- Update: "Bloqueado por Issue XXX"

---

## 🔄 Update Protocol

**Toda semana (segunda-feira):**
- [ ] Update status de issues em progresso
- [ ] Move para BLOCKED se necessário
- [ ] Adiciona nota de progresso na tabela de progresso

**Na transição de status:**
- [ ] Atualiza campo "Atualizado em"
- [ ] Adiciona entrada na tabela de progresso
- [ ] Comenta no Paperclip/Slack

---

## 📊 Prioridade - Legenda

| Símbolo | Nível   | Tempo Limite | Exemplo                     |
| ------- | ------- | ------------ | --------------------------- |
| 🔴       | CRÍTICA | ≤ 1 semana   | Security hole, auth broken  |
| 🟡       | ALTA    | ≤ 2 semanas  | Feature importante, blocker |
| 🟠       | MÉDIA   | ≤ 1 mês      | Enhancement, nice-to-have   |
| 🟢       | BAIXA   | Sem urgência | Tech debt, doc improvements |

---

## 💡 Exemplos de Boas Issues

### ✅ BOA

```markdown
# [001] Implementar AuthMiddleware

**Delegado a:** Lead Engineer  
**Prioridade:** 🔴 CRÍTICA  
**Esforço:** 6-8h  
**Deadline:** 30 de abril  

## Objetivo
API Cloud não valida JWT/API Key. QUALQUER cliente consegue chamar /api/* endpoints.

## Critério de Aceitação
- [ ] GET /api/anything sem auth → 401 Unauthorized
- [ ] GET /api/anything com JWT válido → 200 OK
- [ ] GET /api/anything com API Key válido → 200 OK
- [ ] All tests pass
```

### ❌ MÁ

```markdown
# [001] Melhorar Auth

**Delegado a:** engineering team  
**Prioridade:** High  

## Descrição
Precisa fazer auth melhor.

## Critério
- Auth funciona
```

---

## 🚀 Como Criar Issue

1. **Copie** o template acima
2. **Preencha** todos campos obrigatórios
3. **Numere** em ordem crescente (001, 002...)
4. **Salve** como `NNN-titulo-em-lowercase.md`
5. **Valide** contra checklist de qualidade
6. **Delegue** a pessoa específica
7. **Commit** com mensagem: `[ISSUE NNN] Criar issue: titulo`

---

## 📚 Referências

- [CONTRIBUTORS.md](../CONTRIBUTORS.md) - Team structure
- [TASK-ANTIGRAVITY.md](../TASK-ANTIGRAVITY.md) - Technical breakdown
- [ISSUES.md](../ISSUES.md) - 5 bugs críticos (migrar para pasta issues/)

---

**Última atualização:** 28/04/2026  
**Mantido por:** TCO Kaffyn
