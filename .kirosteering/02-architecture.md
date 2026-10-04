---
inclusion: always
---
# Arquitetura — SaaS + n8n + WhatsApp + IA

## 1. Arquitetura de referência

Usuário → WhatsApp → IA/roteamento → n8n → PostgreSQL/APIs → resposta/ação.

Dashboard → Backend SaaS → PostgreSQL/configurações/métricas.

O n8n é o motor de automação e integração. O backend é o núcleo do produto SaaS.

## 2. Separação de responsabilidades

### SaaS
Responsável por:
- autenticação;
- tenants;
- usuários;
- permissões;
- planos;
- billing;
- configurações;
- dashboard;
- métricas;
- dados principais;
- API própria.

### n8n
Responsável por:
- workflows;
- webhooks;
- integrações;
- roteamento;
- notificações;
- follow-ups;
- sincronizações;
- automações;
- chamadas de IA;
- execução de processos de negócio que não precisam estar codificados no backend.

### IA
Responsável por:
- entender linguagem natural;
- classificar intenção;
- extrair dados;
- interpretar solicitações;
- decidir qual workflow/tool apropriado usar quando necessário.

A IA não deve ser responsável sozinha por regras críticas.

### PostgreSQL
Fonte de dados estruturados do SaaS.

## 3. Interface do produto

### WhatsApp
Principal interface operacional para o pequeno empreendedor.

Objetivo: permitir que o usuário registre e consulte informações sem precisar alimentar o dashboard manualmente.

### Dashboard
Interface de gestão e visualização:
- clientes;
- leads;
- agenda;
- propostas;
- cobranças;
- métricas;
- configurações;
- histórico.

WhatsApp executa/interage. Dashboard organiza/visualiza.

## 4. Multi-tenancy

Cada negócio é um tenant.

Entidades iniciais podem incluir:
- tenants
- users
- roles
- whatsapp_accounts
- whatsapp_numbers
- customers
- conversations
- messages
- leads
- appointments
- proposals
- payments
- tasks
- workflows
- integrations
- subscriptions
- usage
- audit_logs

Entidades de negócio devem possuir tenant_id ou relação segura com tenant.

Toda operação deve validar autorização.

Nunca confiar somente no tenant_id vindo do cliente.

## 5. Fluxo de exemplo

Mensagem:
“Cadastrei o João, ele quer orçamento para casamento em outubro.”

Fluxo preferencial:

WhatsApp
→ IA interpreta
→ n8n identifica intenção
→ extrai dados
→ valida campos
→ grava cliente/lead
→ cria oportunidade
→ registra evento
→ responde no WhatsApp.

Não criar um serviço backend apenas para executar essa sequência se n8n conseguir fazê-la de forma confiável.

## 6. Operações críticas

Operações como cobrança, alteração de dados importantes, confirmação de agenda e ações irreversíveis devem possuir validações determinísticas.

IA pode interpretar.
Workflow deve validar.
Sistema deve executar.

## 7. Reutilização

Preferir sub-workflows e templates reutilizáveis em vez de copiar lógica.

Um workflow desenvolvido para Bruna deve servir como base para outros fotógrafos quando possível.

Configurações específicas devem ser dados do tenant, não código duplicado.

## 8. Complexidade

Não criar microsserviços, filas, caches, Kubernetes ou componentes distribuídos sem necessidade medida.

A arquitetura inicial deve ser simples, barata e observável.

Escalar somente quando houver necessidade real.

## 9. Regra arquitetural

Sempre perguntar:

“Estamos construindo produto ou apenas programando uma automação que poderia ser um workflow n8n?”

Se for automação, preferir n8n.
Se for capacidade estrutural do SaaS, considerar código próprio.
