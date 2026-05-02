# Vectora: Ecossistema de Governança de Contexto e IA Tática

## O que é o Vectora

O Vectora é um ecossistema de Governança de Contexto e IA Tática, operando como um Sub-Agente de Tier 2 projetado especificamente para engenharia de software. Ele atua como uma camada intermediária via protocolo MCP, interceptando chamadas, validando segurança em tempo real e entregando contexto ultrapreciso para agentes principais (como Claude Code, Gemini CLI e Cursor), garantindo que a execução seja fundamentada em dados reais e protegida por políticas de segurança locais.

## Objetivo

O objetivo do Vectora é fornecer uma infraestrutura de decisão tática que elimine alucinações e vazamentos de dados em agentes de IA. Através da fórmula que combina modelos de inferência rápida, um framework de orquestração ativa e recuperação de contexto governada, o Vectora busca transformar LLMs genéricas em agentes funcionais capazes de operar em repositórios complexos com precisão cirúrgica e conformidade total.

---

## O Ecossistema Vectora

### Desktop

Atua como o nó de execução local, incluindo o Tray Manager para gerenciamento em segundo plano e suporte nativo ao protocolo MCP. É responsável por rodar a inferência de políticas localmente e garantir a integração direta com as ferramentas de desenvolvimento do usuário.

### Cloud

Fornece um backend escalável para equipes, permitindo a persistência de estado global e o gerenciamento multi-tenant. É otimizado para a stack Gemini e Voyage, oferecendo infraestrutura gerenciada para busca vetorial e sincronização de contexto entre diferentes ambientes.

### Integrations

Conjunto de plugins e conectores nativos para IDEs e ferramentas de linha de comando, incluindo VSCode, Claude Code, Gemini CLI e ChatGPT. Serve como o hub de conexão que permite ao Vectora alimentar diversos agentes com contexto estruturado.

### Dashboard

Console administrativo centralizado para gestão de planos, faturamento, análise de métricas operacionais e auditoria de chamadas. Permite a visualização clara do consumo de tokens e da eficácia das decisões tomadas pelos agentes.

### Vectora Cognitive Runtime (Vectora Decision Engine)

O cérebro tático do sistema. Consiste em um modelo de linguagem pequeno (SmolLM2) que executa localmente via ONNX Runtime para realizar roteamento tático, validação de fidelidade (anti-alucinação) e aplicação de regras de governança local sem enviar dados sensíveis para a nuvem.

### Docs

Base de conhecimento centralizada que utiliza o tema Hextra (Hugo). Contém a documentação técnica exaustiva, guias de implementação, especificações de protocolos e referências de ferramentas para desenvolvedores e contribuidores do ecossistema.
