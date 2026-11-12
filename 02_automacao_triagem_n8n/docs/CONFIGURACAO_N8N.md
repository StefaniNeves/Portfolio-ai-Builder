# Configuração no n8n

## 1. Importar o workflow

1. Abra o n8n.
2. Use **Import from File**.
3. Selecione `workflow/automacao_triagem_solicitacoes_ia.json`.
4. Salve o workflow.

## 2. Criar a credencial da OpenAI

O workflow usa o node HTTP Request para chamar a API de Chat Completions.

1. No node **Classificar com OpenAI**, abra a área de credenciais.
2. Crie uma credencial do tipo **Header Auth** (em algumas versões, o tipo pode aparecer como credencial de autenticação por cabeçalho).
3. Configure o nome do cabeçalho como `Authorization`.
4. Configure o valor como `Bearer SUA_CHAVE_DA_OPENAI`.
5. Salve a credencial e selecione-a no node.

Não escreva a chave no workflow JSON e não faça commit de credenciais. A documentação oficial do n8n descreve as credenciais OpenAI e o node HTTP Request:
- https://docs.n8n.io/integrations/builtin/credentials/openai/
- https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httpRequest/

## 3. Executar em modo de teste

1. Abra o node Webhook.
2. Clique em **Listen for Test Event** ou execute o workflow.
3. Copie a Test URL.
4. Envie uma requisição POST com `Content-Type: application/json`.
5. Consulte os dados de execução no editor.

## 4. Usar em produção

Depois de testar:
1. Salve o workflow.
2. Ative o workflow.
3. Use a Production URL do Webhook.
4. Proteja o endpoint com autenticação e HTTPS quando aplicável.

A URL de teste e a URL de produção têm comportamentos diferentes. Consulte https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/ para detalhes.

## Observações

- A chave da API deve ser válida e ter acesso ao modelo configurado.
- A disponibilidade do modelo pode mudar conforme a conta e a API.
- Chamadas à API podem gerar custos.
- Não compartilhe dados sensíveis nos testes.
