# Guia de automação com Make

Este documento é um guia para implementar e reproduzir a automação. Ele não significa que um cenário já tenha sido criado ou executado na sua conta do Make.

## Cenário: enviar registros de vendas para a API

1. Crie um cenário no Make.
2. Adicione o gatilho **Webhooks > Custom webhook** e copie a URL gerada.
3. Adicione o módulo **HTTP > Make a request**.
4. Configure o método como `POST`, o tipo de conteúdo como `application/json` e informe o endereço do endpoint `/analyze` da API FastAPI publicada (ou de um túnel local temporário durante o desenvolvimento).
5. Mapeie o array `records` recebido e envie `{"records": [...], "use_ai": false}`.
6. Adicione um roteador ou módulo de notificação para encaminhar o resumo a um destino autorizado.
7. Faça um teste usando `examples/request.json`, confira o histórico de execução e registre sua própria captura de tela.

Mantenha as credenciais no gerenciador de conexões do Make. Não inclua informações secretas em capturas de tela nem no GitHub. Registre a data, os dados usados no teste, o resultado e eventuais erros no arquivo de evidências do projeto.
