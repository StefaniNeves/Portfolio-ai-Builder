🤖 Automação de Triagem de Solicitações com IA

📌 Sobre o projeto

Este projeto demonstra uma automação de triagem de solicitações utilizando n8n e inteligência artificial.

O objetivo é receber mensagens de usuários, analisar seu conteúdo, identificar o assunto e classificar a prioridade da solicitação, retornando os dados em formato estruturado.

🎯 Objetivos

- Automatizar a classificação de solicitações.
- Identificar categorias e prioridades.
- Reduzir tarefas manuais de atendimento.
- Padronizar informações recebidas.
- Demonstrar a integração entre APIs e inteligência artificial.

🛠️ Tecnologias utilizadas

- n8n — automação de workflows.
- OpenAI API — análise e classificação de textos.
- Webhook — recebimento de solicitações via HTTP.
- JSON — organização dos dados de entrada e saída.

🔄 Fluxo da automação

1. O Webhook recebe uma solicitação.
2. Os dados são encaminhados para análise.
3. A inteligência artificial identifica a categoria e a prioridade.
4. O resultado é organizado em JSON.
5. A automação devolve uma resposta ao solicitante.

📥 Exemplo de entrada

{
  "nome": "Maria",
  "mensagem": "Meu pedido está atrasado e preciso de ajuda."
}

📤 Exemplo de resultado esperado

{
  "categoria": "Entrega",
  "prioridade": "Alta",
  "resumo": "Cliente relata atraso no pedido.",
  "encaminhamento": "Atendimento prioritário"
}

⚙️ Como importar

1. Acesse sua instância do n8n.
2. Abra o menu de workflows.
3. Selecione a opção de importar workflow.
4. Escolha o arquivo "workflow_triagem_ia_n8n.json".
5. Configure as credenciais da OpenAI.
6. Execute os testes antes de ativar o workflow.

🔐 Segurança

As credenciais da API devem ser configuradas diretamente no n8n. Nenhuma chave secreta deve ser publicada no GitHub.

👩‍💻 Autora

Stefani Rodrigues Neves

Estudante de Ciência da Computação — UFCA.

GitHub: "@StefaniNeves" (https://github.com/StefaniNeves)
