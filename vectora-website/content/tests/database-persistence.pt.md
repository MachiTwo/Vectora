---
title: "Suite de Testes: Banco de Dados & Persistência"
slug: database-persistence-tests
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - architecture
  - ast-parsing
  - concepts
  - database
  - embeddings
  - mongodb
  - mongodb-atlas
  - persistence
  - security
  - state
  - testing
  - vector-search
  - vectora
---

{{< lang-toggle >}}

Esta suite valida que o Vectora persiste dados corretamente, recupera-os eficientemente e sincroniza entre ambientes local e cloud sem perda de integridade. Garantir a confiabilidade dos dados é crítico para manter um motor de contexto preciso e útil.

Ao verificar a camada de persistência, garantimos que o código indexado e o estado da sessão do usuário permaneçam consistentes após reinicializações e entre múltiplos dispositivos.

**Cobertura**: 80+ testes | **Prioridade**: CRÍTICA

## Componentes Testados

A estratégia de testes de persistência cobre todos os módulos relacionados a dados dentro da arquitetura do Vectora.

- Conexão e pooling do MongoDB Atlas.
- Armazenamento de embeddings e recuperação vetorial.
- Persistência de chunks de código e integridade de metadados.
- Gestão de chaves de API e segurança.
- Sincronização de cache híbrido local/cloud.
- Data roaming e consistência entre dispositivos.
- Performance e precisão da indexação vetorial.

## Segmentos de Testes

As seções a seguir detalham os casos de teste específicos e os cenários cobertos por esta suite.

### 1. Conectividade MongoDB (15 testes)

Garante que a aplicação possa se comunicar de forma confiável com o banco de dados sob várias condições de rede.

- **Estabelecimento de Conexão**: Valida que as conexões são estabelecidas em menos de 2 segundos com o pooling adequado.
- **Lógica de Re-tentativa**: Verifica o backoff exponencial e a recuperação automática quando o banco de dados fica offline.
- **Pooling de Conexão**: Garante o uso eficiente de recursos sob alta carga concorrente (50+ requisições simultâneas).
- **Timeouts**: Valida que conexões travadas sejam terminadas graciosamente após 30 segundos.

### 2. Operações CRUD com Embeddings (20 testes)

Foca no ciclo de vida dos dados vetoriais e seus metadados associados na coleção de documentos.

- **Inserção de Vetor**: Valida que embeddings de 384 dimensões sejam salvos com IDs únicos e metadados completos.
- **Busca Vetorial**: Verifica que a busca por similaridade de cosseno retorne os top-K resultados relevantes em menos de 200ms.
- **Atualização de Vetor**: Garante que modificações em chunks de código recalculem corretamente os índices e incrementem versões.
- **Operações em Lote**: Testa a inserção atômica de 500+ documentos com rollback confiável em caso de falha.

### 3. Persistência de Chunks (15 testes)

Valida a relação entre os trechos de código bruto e sua representação processada.

- **Armazenamento de Chunks**: Cada chunk deve ter um ID único, embedding, intervalo de linhas e caminho do arquivo.
- **Recuperação Estrutural**: Verifica que os chunks possam ser recuperados com base em sua relação AST (ex: encontrar a classe pai).
- **Integridade**: Garante que não existam referências circulares no grafo de dependência de chunks.

### 4. Data Roaming & Sync (15 testes)

Garante uma experiência fluida ao usar o Vectora em diferentes máquinas ou em modo offline.

- **Sync de Cache Local**: Valida que buscas offline sejam enfileiradas e mescladas com a nuvem quando a conexão é restaurada.
- **Resolução de Conflitos**: Implementa estratégias de "última escrita vence" ou mesclagem automática para atualizações simultâneas.
- **Criptografia em Repouso**: Garante que os dados locais no `AppData` sejam criptografados usando AES-256 com chaves específicas do usuário.

### 5. Indexação Vetorial (10 testes)

Monitora a performance e precisão dos índices HNSW no MongoDB Atlas.

- **Criação de Índice**: Valida que os índices para mais de 10 mil documentos sejam construídos incrementalmente sem downtime.
- **Precisão de Busca**: Compara os resultados HNSW contra a busca por força bruta para garantir precisão >= 95%.

## Critérios de Aceitação

| Critério                       | Alvo                                    |
| :----------------------------- | :-------------------------------------- |
| **Taxa de Sucesso**            | 100%                                    |
| **Cobertura MongoDB**          | > 90%                                   |
| **Latência de Query (p95)**    | < 300ms                                 |
| **Latência de Inserção (p95)** | < 200ms                                 |
| **Taxa de Acerto de Cache**    | > 70%                                   |
| **Tempo de Sync**              | < 5s para 1000+ docs                    |
| **Integridade de Dados**       | Zero perda de dados em qualquer cenário |

## Guia de Execução

Para rodar os testes de banco de dados e persistência, utilize os seguintes comandos:

```bash
# Rodar todos os testes de persistência
go test -v ./tests/database/...

# Rodar com detecção de race condition
go test -v -race ./tests/database/...

# Rodar com relatório de cobertura
go test -v -cover ./tests/database/...
```

## External Linking

| Concept           | Resource                                                 | Link                                                                                                       |
| ----------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MongoDB Atlas** | Atlas Vector Search Documentation                        | [www.mongodb.com/docs/atlas/atlas-vector-search/](https://www.mongodb.com/docs/atlas/atlas-vector-search/) |
| **AST Parsing**   | Tree-sitter Official Documentation                       | [tree-sitter.github.io/tree-sitter/](https://tree-sitter.github.io/tree-sitter/)                           |
| **HNSW**          | Efficient and robust approximate nearest neighbor search | [arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)                                               |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
