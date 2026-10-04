---
inclusion: always
---
# Infraestrutura — SaaS Low-Code

## 1. Objetivo

Criar infraestrutura suficiente para suportar SaaS, n8n, WhatsApp, PostgreSQL, dashboard e integrações com segurança e observabilidade.

Não transformar um MVP em uma plataforma de infraestrutura complexa.

## 2. Princípio

Infraestrutura deve habilitar o produto, não criar trabalho adicional.

Antes de adicionar:
- serviço AWS;
- cluster;
- fila;
- cache;
- worker;
- Kubernetes;
- banco adicional;

perguntar se realmente existe necessidade.

## 3. n8n

n8n é componente central da operação.

A infraestrutura deve garantir:
- execução confiável;
- persistência;
- conectividade;
- secrets;
- logs;
- backups;
- recuperação;
- observabilidade.

Não duplicar a lógica dos workflows na infraestrutura.

## 4. AWS

Usar AWS como referência cloud.

Priorizar:
- segurança;
- custo controlado;
- simplicidade;
- automação;
- observabilidade.

Não usar serviço AWS apenas porque ele existe.

## 5. Terraform

Infraestrutura relevante deve ser reproduzível.

Priorizar:
- módulos simples;
- state seguro;
- least privilege;
- variáveis claras;
- tags;
- naming;
- revisão de mudanças.

Evitar módulos Terraform extremamente genéricos.

## 6. Docker

Usar quando facilitar:
- ambiente;
- deploy;
- reprodutibilidade;
- isolamento.

## 7. Kubernetes

Kubernetes não é requisito inicial.

Só usar quando:
- houver necessidade real de escala;
- disponibilidade;
- operação;
- isolamento;
- ou outro requisito que justifique sua complexidade.

Se uma solução simples resolver, preferir a simples.

## 8. CI/CD

Pipeline proporcional ao estágio do produto:
- validação;
- testes;
- segurança;
- build;
- deploy;
- rollback.

Não criar uma plataforma DevOps maior que o SaaS.

## 9. Segurança

Obrigatório:
- secrets fora do código;
- least privilege;
- criptografia;
- tenant isolation;
- backups;
- auditoria;
- controle de acesso;
- retenção;
- LGPD.

## 10. Observabilidade

Monitorar:
- falhas de workflows;
- tempo de execução;
- erros;
- uso;
- custo por tenant;
- chamadas de IA;
- WhatsApp;
- integrações;
- indisponibilidade.

O n8n permite inspecionar execuções e erros; usar essa capacidade antes de construir observabilidade customizada desnecessária. citeturn0search11

## 11. Escala

Escalar com base em dados reais.

Primeiro:
- validar;
- medir;
- identificar gargalo;
- então escalar.

Não construir arquitetura de 1000 clientes para uma POC de 1 cliente.
