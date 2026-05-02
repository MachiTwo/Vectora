---
title: "Plano Free"
slug: free
date: "2026-04-18T22:30:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - byok
  - concepts
  - config
  - desktop
  - embeddings
  - free
  - gemini
  - guardian
  - mcp
  - open-source
  - pricing
  - protocol
  - rag
  - reranker
  - security
  - system
  - tools
  - trust-folder
  - vectora
  - voyage
---

{{< lang-toggle >}}

> [!NOTE] > **O Plano Free é para o Vectora Desktop**. Se você está procurando o Vectora Cloud (SaaS), consulte a seção de Preços Cloud. O Desktop Free é de código aberto e não tem limites de tempo, enquanto os tiers Cloud seguem um modelo de assinatura.

O plano **Free** do Vectora é totalmente **open-source** e não tem expiração de tempo. Você pode usar a versão Desktop localmente em qualquer base de código sem custo. Ele é projetado para desenvolvedores individuais, pequenas equipes, projetos educacionais e prototipagem rápida.

Ao usar o plano Free, você mantém o controle total sobre seus dados enquanto aproveita a análise de código avançada assistida por IA.

## Desktop Free vs Tiers Cloud

A tabela a seguir compara a versão Desktop local com os vários tiers gerenciados em nuvem oferecidos pelo Vectora.

| Recurso           | Desktop Free  | Cloud Free  | Cloud Plus         | Cloud Team    |
| :---------------- | :------------ | :---------- | :----------------- | :------------ |
| **Instalação**    | Binário Local | SaaS        | SaaS               | SaaS          |
| **Custo**         | Grátis        | Grátis\*    | $20/mês            | Personalizado |
| **Indexação**     | Ilimitada     | Até 10 docs | Ilimitada          | Ilimitada     |
| **Workspaces**    | 1 (Local)     | 1           | Ilimitados         | Ilimitados    |
| **Usuários**      | 1 (Você)      | 1           | Até 5              | Até 100       |
| **Buscas/dia**    | Ilimitadas    | 100         | 10K                | Ilimitadas    |
| **APIs Externas** | Com BYOK      | Limitadas   | Completa (50K/mês) | Completa      |
| **Protocolo**     | stdio MCP     | API HTTP    | API HTTP           | API HTTP      |

_\*Cloud Free: 60 req/min Gemini, 50 req/min Voyage. BYOK = Traga Suas Próprias Chaves._

## O Que Está Incluído (Desktop Free)

O tier Free fornece acesso ao motor principal do Vectora, permitindo uma análise semântica de alta qualidade.

### Recursos do Motor Core

- **Busca Semântica**: Acesso total à recuperação de código baseada em vetores.
- **Análise de Dependências**: Mapeamento avançado de relacionamentos de símbolos.
- **Indexação Completa**: Sem limites artificiais na indexação de projetos locais.
- **Trust Folder & Guardian**: Recursos padrão de segurança e sandbox.
- **Acesso Total ao CLI**: Conjunto completo de ferramentas de linha de comando.
- **Vectora Cognitive Runtime (Decision Engine)**: Cérebro tático local via ONNX Runtime para roteamento e orquestração.
- **Agentic Framework**: Suporte integrado para agentes autônomos.

### Suporte a IDE & Plataformas

- **Claude Code (MCP)**: Integração nativa via stdio.
- **Cursor (MCP)**: Suporte completo para o editor aprimorado por IA.
- **Extensão VS Code**: Acesso ao painel de busca semântica dedicado.
- **Vectora CLI**: Controle total sobre o índice do seu projeto.

## Modelos de IA (BYOK)

No plano Free, você traz suas próprias chaves de API para os principais provedores de IA, permitindo usar seus créditos existentes ou tiers gratuitos.

| Componente    | Opção Recomendada   | Custo    |
| :------------ | :------------------ | :------- |
| **Embedding** | Voyage 4            | Grátis\* |
| **Reranking** | Voyage Rerank 2.5   | Grátis\* |
| **LLM**       | Gemini 1.5 Flash    | Grátis\* |
| **Local**     | Ollama (all-MiniLM) | Grátis   |

_\*Tiers gratuitos dos provedores tipicamente têm limites: 60 req/min para Gemini e 50 req/min para Voyage._

## Limites de Uso & Performance

Embora a indexação seja ilimitada, o servidor local é otimizado para fluxos de trabalho de desenvolvimento de usuário único.

### Limites do Sistema

- **Usuários Simultâneos**: 1 (otimizado para um único desenvolvedor).
- **Buscas por Dia**: 1.000 (limite local recomendado).
- **Cache de Embeddings**: 500MB de armazenamento local.
- **Retenção de Logs**: 30 dias de histórico de auditoria.

### Metas de Performance

- **Latência de Busca**: Tipicamente <2s para consultas locais.
- **Tamanho Máx. de Arquivo**: 100MB por arquivo para indexação.
- **Máx. Chunks por Busca**: Retorna até 20 snippets relevantes.

## Como Começar

Siga estes passos rápidos para colocar o Vectora em funcionamento na sua máquina local.

### Instalação

```bash
npm install -g @kaffyn/vectora

# Verificar instalação
vectora --version
```

### Configuração Inicial

1. **Inicializar Projeto**: Navegue até a raiz do seu projeto e execute `vectora init --name "Meu Projeto"`.
2. **Obter Chaves**: Pegue suas chaves gratuitas no Google AI Studio e Voyage AI.
3. **Configurar**: Use `vectora config set` para fornecer suas chaves de API ao sistema.
4. **Indexar**: Execute `vectora index` para construir seu primeiro mapa semântico.
5. **Buscar**: Comece a consultar com `vectora search "Como funciona o login?"`.

## Solução de Problemas

Se você encontrar problemas durante o uso, considere os seguintes cenários comuns.

### "Cota Excedida"

Isso significa que você atingiu o limite mensal gratuito do seu provedor de IA (Gemini ou Voyage). Você pode esperar pelo reset no primeiro dia do mês ou fazer o upgrade da conta do seu provedor.

### "Limite de Taxa Excedido"

Você fez muitas requisições em um único minuto. Tente adicionar um pequeno atraso entre suas consultas ou scripts automatizados.

### "Usuários Simultâneos Excedidos"

O tier Free é projetado para uma única instância ativa (uma IDE ou um processo CLI por vez). Certifique-se de não ter múltiplos editores tentando acessar o mesmo servidor local simultaneamente.

## External Linking

| Concept               | Resource                             | Link                                                                                   |
| --------------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **Voyage AI**         | High-performance embeddings for RAG  | [www.voyageai.com/](https://www.voyageai.com/)                                         |
| **Voyage Embeddings** | Voyage Embeddings Documentation      | [docs.voyageai.com/docs/embeddings](https://docs.voyageai.com/docs/embeddings)         |
| **Voyage Reranker**   | Voyage Reranker API                  | [docs.voyageai.com/docs/reranker](https://docs.voyageai.com/docs/reranker)             |
| **Gemini AI**         | Google DeepMind Gemini Models        | [deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)   |
| **Gemini API**        | Google AI Studio Documentation       | [ai.google.dev/docs](https://ai.google.dev/docs)                                       |
| **MCP**               | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
