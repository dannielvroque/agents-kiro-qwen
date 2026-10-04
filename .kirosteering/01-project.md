---
inclusion: always
---
# Contexto do Produto — SaaS de Gestão + Automação por WhatsApp

## 1. Visão do produto

Construir um SaaS para pequenos negócios que centraliza gestão comercial e operacional, usando o WhatsApp como principal interface de interação e o dashboard como visão de gestão.

A proposta não é vender “um bot de WhatsApp” nem vender n8n. O produto vende resultado:
- menos tarefas manuais;
- atendimento mais rápido;
- leads organizados;
- propostas e follow-ups;
- agenda;
- clientes;
- marketing;
- visão do negócio;
- automação de rotinas.

O usuário deve conseguir conversar com o sistema pelo WhatsApp para registrar, consultar e executar tarefas, sem precisar alimentar manualmente um CRM o tempo todo.

## 2. Primeiro caso de validação

A primeira POC deve ser construída para a Bruna, fotógrafa.

Contexto de uso:
- trabalha como fotógrafa;
- concilia trabalho e família;
- é mãe de dois filhos;
- trabalha com o marido, Lucas;
- precisa cuidar de edição;
- agenda;
- cobrança;
- atendimento;
- organização dos clientes;
- e outras tarefas do negócio.

A situação da Bruna representa o problema que queremos atacar: uma pequena empreendedora que precisa fazer muitas funções e tem pouco tempo para manter sistemas manualmente.

A POC deve priorizar redução de trabalho operacional e não quantidade de funcionalidades.

## 3. Hipótese de produto

O sistema deve funcionar como um “funcionário digital” do negócio.

Exemplos de interação:

“Cadastrei a Maria, ela quer um ensaio dia 15.”

“Quem ainda não respondeu o orçamento?”

“Faz um follow-up com quem recebeu orçamento há 3 dias.”

“Quanto tenho para receber esta semana?”

“Marca João para terça.”

“Cria uma proposta para esse cliente.”

A IA interpreta a intenção e o n8n executa o processo correspondente.

## 4. Primeiro vertical

Fotografia é o primeiro vertical de validação.

O produto, entretanto, deve ser construído com motor genérico o suficiente para que os mesmos conceitos possam virar templates para outros pequenos negócios posteriormente.

Não criar um sistema inteiro “hardcoded para fotógrafos”.

## 5. Módulos possíveis

O produto pode evoluir para módulos ativáveis por tenant:
- CRM/clientes;
- leads;
- WhatsApp;
- propostas/orçamentos;
- follow-up;
- agenda;
- cobranças;
- marketing;
- tarefas;
- relatórios;
- IA.

Planos podem combinar módulos, volume e recursos.

## 6. Princípio n8n-first / code-last

A maior prioridade técnica é reduzir código digitável e código operacional.

Antes de criar código:
1. verificar se n8n resolve;
2. verificar node existente;
3. verificar HTTP/API;
4. verificar expressão;
5. verificar workflow/sub-workflow;
6. verificar se a funcionalidade pode ser configuração;
7. só então considerar pequeno código;
8. código próprio do SaaS apenas quando necessário.

Não criar uma API, worker ou microsserviço apenas para substituir uma automação que o n8n resolve de forma confiável.

## 7. O que deve ser SaaS próprio

Código próprio deve concentrar-se no produto:
- autenticação;
- tenants;
- usuários;
- permissões;
- planos;
- billing;
- configurações;
- dashboard;
- métricas;
- API própria;
- controles de acesso;
- dados e regras críticas.

Automação operacional deve preferencialmente ficar no n8n.

## 8. Estratégia de evolução

POC Bruna → medir uso → descobrir tarefas repetitivas → criar workflows reutilizáveis → criar configuração por tenant → transformar em produto → templates verticais → SaaS.

Não construir dezenas de módulos antes de validar o primeiro fluxo real.

## 9. Critério de sucesso

A POC deve responder:
- quais tarefas realmente consomem tempo;
- quais podem ser automatizadas;
- quais exigem intervenção humana;
- quais informações precisam ser registradas;
- quais workflows se repetem;
- quais funcionalidades têm valor percebido;
- quanto trabalho manual foi eliminado.

O produto deve crescer pela repetição observada, não por uma lista arbitrária de features.
