---
title: "Suite de Testes: Integração com Extensão VS Code"
slug: vscode-integration-tests
date: "2026-04-23T22:00:00-03:00"
type: docs
sidebar:
  open: true
tags:
  - ai
  - concepts
  - extension
  - integration
  - mcp
  - persistence
  - protocol
  - testing
  - tools
  - vectora
  - vscode
---

{{< lang-toggle >}}

A extensão do VS Code deve integrar perfeitamente com o Vectora, fornecendo uma experiência de usuário intuitiva e tempos de resposta rápidos. Esta suite valida que a extensão melhora a produtividade do desenvolvedor ao fornecer inteligência de código superior sem interromper o fluxo natural de trabalho de codificação.

Ao verificar o comportamento da extensão, garantimos que o Vectora permaneça um cidadão de primeira classe dentro do ambiente de desenvolvimento mais popular.

**Cobertura**: 100+ testes | **Prioridade**: CRÍTICA

## Princípios Centrais

A extensão é projetada em torno de vários princípios fundamentais para garantir que ela agregue valor sem fricção.

1. **Integração Fluida**: Opera sem interromper o foco ou o fluxo de trabalho atual do desenvolvedor.
2. **Feedback Instantâneo**: Resultados são entregues em menos de 500ms para manter uma sensação de responsividade.
3. **Clareza Visual**: Fornece uma UI clara e intuitiva que segue as diretrizes de design do VS Code.
4. **Padrões Inteligentes**: Utiliza automaticamente as ferramentas do Vectora quando apropriado para o contexto atual.

## Segmentos de Testes

As seções a seguir detalham os casos de teste específicos e os cenários cobertos por esta suite.

### 1. Ativação & Inicialização da Extensão (15 testes)

Garante que a extensão carregue corretamente e estabeleça uma conexão estável com o backend.

- **Ativação com Sucesso**: Verifica se a barra de status mostra "Vectora: Ready" e se todos os comandos estão registrados.
- **Conexão com Servidor MCP**: Valida que a conexão com o servidor MCP do Vectora seja estabelecida em menos de 2 segundos.
- **Componentes de UI**: Confirma que o painel lateral, ícones e itens da paleta de comandos sejam inicializados corretamente.

### 2. Busca & Navegação (25 testes)

Foca na experiência principal de busca e na habilidade de navegar pelos achados.

- **Busca Rápida**: Testa a busca por texto selecionado no editor com resultados aparecendo em menos de 300ms.
- **Busca Avançada**: Valida a funcionalidade do diálogo de busca dedicado e suas opções de filtragem.
- **Interação com Resultados**: Confirma que clicar em um resultado de busca abra o arquivo correto e destaque a linha específica.
- **Paginação**: Garante que grandes conjuntos de resultados possam ser explorados sem degradar a performance da interface.

### 3. Análise de Arquivo & Código (20 testes cada)

Testa os recursos de análise profunda que fornecem insights estruturais e contextuais.

- **Análise Automatizada**: Valida o comando "Analyze File", cobrindo insights de estrutura, complexidade e cobertura de testes.
- **Hover Inline**: Verifica se passar o mouse sobre símbolos de código fornece documentação e informações de uso precisas.
- **Visualização de Dependências**: Testa a geração e exibição de grafos de chamadas entrantes/saintes.
- **Busca por Similaridade**: Garante que a descoberta de padrões de código similares funcione em todo o projeto.

### 4. Diagnósticos & Quick Fixes (15 testes)

Valida a habilidade da extensão em identificar e ajudar a corrigir problemas de código.

- **Diagnósticos Inline**: Confirma que linhas onduladas apareçam para problemas identificados com explicações claras ao passar o mouse.
- **Sugestões de Correção Rápida**: Verifica se correções acionáveis (ex: "Adicionar Documentação") são oferecidas e aplicadas corretamente.
- **Processamento em Lote**: Testa a habilidade de aplicar múltiplas correções sugeridas dentro de um único arquivo.

### 5. Configurações & Preferências (10 testes)

Garante que as preferências do usuário sejam respeitadas e persistidas corretamente.

- **UI de Configurações**: Valida o painel de configurações para URLs de servidor, limites de resultados e alternâncias de auto-análise.
- **Persistência**: Confirma que configurações personalizadas sejam mantidas entre reinicializações do VS Code.

## SLAs de Performance

A tabela a seguir resume as metas de performance para a extensão do VS Code.

| Operação                            | Latência Alvo |
| :---------------------------------- | :------------ |
| **Exibição de Resultados de Busca** | < 300ms       |
| **Análise de Arquivo**              | < 500ms       |
| **Descoberta de Similaridade**      | < 800ms       |
| **Grafos de Dependência**           | < 1s          |
| **Interação de UI**                 | 60 FPS        |

## External Linking

| Concept        | Resource                             | Link                                                                                   |
| -------------- | ------------------------------------ | -------------------------------------------------------------------------------------- |
| **MCP**        | Model Context Protocol Specification | [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification) |
| **MCP Go SDK** | Go SDK for MCP (mark3labs)           | [github.com/mark3labs/mcp-go](https://github.com/mark3labs/mcp-go)                     |
| **TypeScript** | Official TypeScript Handbook         | [www.typescriptlang.org/docs/](https://www.typescriptlang.org/docs/)                   |

---

_Parte do ecossistema Vectora_ · [Open Source (MIT)](https://github.com/Kaffyn/Vectora) · [Contribuidores](https://github.com/Kaffyn/Vectora/graphs/contributors)
