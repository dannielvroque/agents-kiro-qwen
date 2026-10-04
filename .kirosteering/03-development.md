---
inclusion: always
---
# Desenvolvimento — Low-Code / n8n-first

## 1. Regra máxima

MENOS CÓDIGO É UMA META DO PRODUTO.

O objetivo não é demonstrar capacidade de programação. O objetivo é entregar valor com a menor quantidade de código e operação possível.

## 2. Ordem obrigatória de solução

Antes de escrever código, avaliar:

1. configuração;
2. n8n node;
3. HTTP Request/API;
4. expressão n8n;
5. workflow;
6. sub-workflow;
7. template reutilizável;
8. pequeno trecho de código;
9. backend;
10. novo serviço.

Não pular diretamente para código.

## 3. Regra para Kiro e Qwen

Sempre que uma tarefa pedir código, perguntar:

“Por que isso não pode ser feito no n8n?”

Se puder:
- usar n8n;
- explicar o workflow;
- implementar/configurar o workflow.

Se não puder:
- explicar a limitação;
- criar o menor código necessário.

## 4. Evitar

- APIs criadas apenas para receber webhook e chamar outro serviço;
- CRUDs desnecessários;
- microsserviços;
- workers sem necessidade;
- abstrações excessivas;
- frameworks por preferência;
- código duplicando lógica de workflows;
- automações hardcoded por cliente;
- lógica de negócio espalhada em vários lugares.

## 5. Código próprio

Código deve existir principalmente para:
- produto SaaS;
- segurança;
- regras críticas;
- funcionalidades que exigem controle próprio;
- integrações que n8n não consegue atender adequadamente;
- processamento realmente incompatível com low-code.

## 6. Configuração > código

Quando duas empresas possuem o mesmo processo com pequenas diferenças, criar configuração por tenant.

Exemplo:
- horário de atendimento;
- serviços;
- preços;
- mensagens;
- regras de follow-up;
- prazo;
- templates;
- canais.

Não criar um código diferente para cada cliente.

## 7. Workflows n8n

Workflows devem:
- ter nomes claros;
- ter responsabilidade definida;
- ser reutilizáveis;
- evitar lógica duplicada;
- possuir tratamento de erro;
- registrar contexto do tenant;
- permitir investigação de execução;
- usar sub-workflows quando isso reduzir repetição.

O n8n possui recursos de logs/executions, retries, organização e sub-workflows que devem ser usados antes de criar mecanismos customizados. citeturn0search8turn0search11

## 8. IA

Preferir IA em tarefas onde linguagem natural agrega valor:
- interpretação;
- classificação;
- extração;
- geração de respostas;
- resumo.

Preferir lógica determinística para:
- valores;
- cobrança;
- permissões;
- agenda;
- status;
- gravações;
- operações críticas.

## 9. Debugging

Antes de alterar:
1. reproduzir;
2. olhar execução do workflow;
3. verificar entrada;
4. verificar saída de cada etapa;
5. verificar dados;
6. verificar integração;
7. identificar causa;
8. aplicar menor correção.

Não reescrever tudo.

## 10. Testes

Priorizar:
- isolamento entre tenants;
- workflows críticos;
- mensagens;
- agenda;
- propostas;
- cobranças;
- integrações;
- autenticação;
- permissões.

Testar o comportamento do workflow, não somente código.

## 11. Revisão

Classificar achados:
- bug real;
- risco real;
- melhoria importante;
- otimização;
- preferência de estilo.

Não inventar problemas.

## 12. Critério de qualidade

Uma solução é melhor quando:
- resolve o problema;
- usa menos código;
- usa menos componentes;
- é fácil de entender;
- é reutilizável;
- é observável;
- é segura;
- é simples de alterar.
