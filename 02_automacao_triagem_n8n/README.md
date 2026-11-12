🤖 Automação de Triagem de Solicitações com Inteligência Artificial

📌 Sobre o projeto

Este projeto consiste em uma automação de triagem de solicitações utilizando Inteligência Artificial, desenvolvida com n8n e integrada à API da OpenAI.

A solução tem como objetivo receber solicitações, processar as informações enviadas e utilizar inteligência artificial para identificar a categoria, a prioridade e gerar um resumo do conteúdo recebido.

A automação busca demonstrar como ferramentas de integração e modelos de linguagem podem ser utilizados para otimizar processos de atendimento, organização e classificação de demandas.

🎯 Objetivos

- Automatizar o processo de recebimento e triagem de solicitações.
- Utilizar Inteligência Artificial para analisar mensagens.
- Classificar solicitações conforme sua categoria e prioridade.
- Gerar resumos para facilitar a compreensão das demandas.
- Integrar diferentes serviços por meio de requisições HTTP.
- Desenvolver uma solução utilizando ferramentas de automação e IA.

⚙️ Tecnologias utilizadas

Tecnologia| Aplicação
n8n| Criação e gerenciamento do fluxo de automação
OpenAI API| Análise e classificação das solicitações
Webhook| Recebimento das solicitações
HTTP Request| Comunicação com a API externa
JSON| Organização e transferência dos dados
Git e GitHub| Versionamento e documentação do projeto

📂 Estrutura do projeto

02_automacao_triagem_n8n/
│
├── README.md
├── LICENSE.txt
├── .gitignore
│
├── workflow/
│   └── automacao_triagem_solicitacoes_ia.json
│
├── docs/
│   ├── ARQUITETURA.md
│   ├── CONFIGURACAO_N8N.md
│   └── TESTES.md
│
├── examples/
│   ├── requisicao.json
│   └── resposta_esperada.json
│
└── screenshots/
    ├── 01-workflow-ilustrativo.png
    ├── 02-execucao-resultado-ilustrativo.png
    ├── 03-historico-execucoes-ilustrativo.png
    └── 04-envio-webhook-ilustrativo.png

🔄 Funcionamento da automação

O fluxo foi organizado para representar as seguintes etapas:

1. Recebimento da solicitação: um Webhook recebe os dados enviados pelo usuário ou por outro sistema.
2. Validação dos dados: as informações recebidas são organizadas e verificadas.
3. Integração com a OpenAI: os dados são enviados para o modelo de inteligência artificial.
4. Análise e classificação: a IA interpreta o conteúdo e identifica a categoria, a prioridade e um resumo da solicitação.
5. Retorno dos resultados: a automação organiza as informações em formato JSON para retornar o resultado do processamento.

🧠 Aplicação da Inteligência Artificial

A integração com a API da OpenAI permite utilizar um modelo de linguagem para interpretar o conteúdo das solicitações.

A análise tem como finalidade identificar informações importantes, como:

- Categoria da solicitação.
- Nível de prioridade.
- Resumo da mensagem.
- Informações relevantes para o encaminhamento da demanda.

A classificação depende das instruções fornecidas ao modelo e dos dados recebidos.

🚀 Como executar o projeto

1. Pré-requisitos

Para executar a automação, é necessário possuir:

- Uma conta no n8n.
- Acesso à API da OpenAI.
- Uma chave de API válida da OpenAI.
- Conhecimentos básicos sobre Webhooks e requisições HTTP.

O n8n pode ser utilizado pela plataforma em nuvem ou por uma instalação local.

2. Importar o workflow

1. Acesse o n8n.
2. Crie um novo workflow.
3. Abra o menu de opções de workflows.
4. Selecione a opção de importar workflow a partir de arquivo.
5. Escolha o arquivo "automacao_triagem_solicitacoes_ia.json", localizado na pasta "workflow".
6. Aguarde o carregamento dos nós da automação.

3. Configurar as credenciais

Configure a credencial de acesso à API da OpenAI no n8n.

Utilize sua própria chave de API e associe a credencial ao nó responsável pela comunicação com a OpenAI.

Importante: nunca compartilhe sua chave de API ou publique credenciais no GitHub.

4. Configurar o Webhook

Verifique as configurações do nó Webhook e identifique a URL disponibilizada pelo n8n.

Essa URL será utilizada para enviar as solicitações à automação.

5. Ativar e testar

Após configurar as credenciais e verificar os nós do workflow:

1. Salve o workflow.
2. Ative a automação, quando aplicável.
3. Utilize a URL de produção do Webhook.
4. Envie uma solicitação de teste.
5. Verifique a execução e o resultado retornado.

📥 Exemplo de entrada

O arquivo "examples/requisicao.json" contém um exemplo de dados que podem ser enviados para a automação.

Exemplo ilustrativo:

{
  "nome": "Maria",
  "email": "maria@email.com",
  "solicitacao": "Estou com dificuldades para acessar minha conta e preciso de ajuda."
}

📤 Exemplo de saída

O arquivo "examples/resposta_esperada.json" apresenta um exemplo do formato de resposta esperado.

Exemplo ilustrativo:

{
  "categoria": "Suporte técnico",
  "prioridade": "Alta",
  "resumo": "Usuária relata dificuldades para acessar sua conta e solicita suporte."
}

Os valores apresentados são exemplos de classificação. O resultado efetivo depende da mensagem enviada e da análise realizada pelo modelo de inteligência artificial.

🧪 Testes e validação

Para avaliar o funcionamento da automação, podem ser realizados testes com diferentes tipos de solicitações.

Alguns cenários sugeridos:

- Solicitações de suporte técnico.
- Dúvidas sobre serviços.
- Problemas de acesso.
- Solicitações com informações incompletas.
- Mensagens que exigem maior prioridade.

Durante os testes, devem ser observados:

- Recebimento correto dos dados pelo Webhook.
- Funcionamento da integração com a OpenAI.
- Classificação adequada das solicitações.
- Organização do resultado em JSON.
- Retorno de erros quando ocorrerem falhas no processamento.

Consulte "docs/TESTES.md" para obter mais informações sobre os cenários de validação.

🏗️ Arquitetura e documentação

A pasta "docs/" contém materiais complementares:

- ARQUITETURA.md: apresenta a organização e o fluxo de funcionamento da solução.
- CONFIGURACAO_N8N.md: reúne orientações para configuração e execução da automação.
- TESTES.md: descreve cenários de testes e validação.

🔐 Segurança

Alguns cuidados importantes para a utilização do projeto:

- Não publicar chaves de API no GitHub.
- Utilizar credenciais protegidas pelo próprio n8n.
- Evitar incluir dados pessoais reais nos exemplos.
- Verificar as permissões e o acesso aos Webhooks.
- Não compartilhar informações confidenciais nas solicitações enviadas à IA.

🖼️ Observação sobre as imagens

As imagens disponíveis na pasta "screenshots/" são ilustrativas e representam visualmente a proposta e o funcionamento do projeto. Elas não correspondem a capturas de uma execução real da automação.

🔮 Melhorias futuras

Algumas funcionalidades que podem ser implementadas em versões futuras:

- Armazenamento das solicitações em banco de dados.
- Encaminhamento automático para setores responsáveis.
- Criação de histórico de atendimentos.
- Integração com ferramentas de comunicação.
- Painel para acompanhamento das solicitações.
- Melhorias nas regras de classificação e prioridade.
- Implementação de mecanismos adicionais de tratamento de erros.

📚 Conhecimentos aplicados

O desenvolvimento deste projeto envolve conhecimentos relacionados a:

- Inteligência Artificial Generativa.
- Engenharia de prompts.
- Automação de processos.
- Integração com APIs.
- Webhooks.
- Requisições HTTP.
- Manipulação de dados JSON.
- Organização de workflows.
- Documentação técnica.
- Versionamento com Git e GitHub.

👩‍💻 Autoria

Projeto desenvolvido como parte dos estudos em Ciência da Computação, com foco na aplicação prática de automação de processos e integração com Inteligência Artificial.

Desenvolvedora: Stefani Neves

GitHub: "StefaniNeves" (https://github.com/StefaniNeves)

---

⭐ Projeto acadêmico desenvolvido para fins de aprendizado e prática de soluções utilizando automação e Inteligência Artificial.
