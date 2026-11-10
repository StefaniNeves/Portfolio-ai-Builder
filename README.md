🤖 Assistente de Atendimento com Inteligência Artificial

Projeto de portfólio desenvolvido por Stefani Rodrigues Neves, estudante de Ciência da Computação na Universidade Federal do Cariri (UFCA).

O objetivo é demonstrar como a Inteligência Artificial pode ser aplicada na criação de soluções para automatizar e melhorar processos de atendimento ao cliente.

📌 Sobre o projeto

O Assistente de Atendimento com IA é uma aplicação web desenvolvida em Python que combina uma base de conhecimento (FAQ) com um modelo de linguagem da OpenAI para responder às dúvidas dos usuários.

A aplicação identifica informações relevantes na base de conhecimento e utiliza essas informações como contexto para gerar respostas com inteligência artificial.

🚀 Funcionalidades

- Interface web para envio de perguntas.
- Consulta a uma base de conhecimento em JSON.
- Busca de informações relevantes por palavras-chave.
- Geração de respostas utilizando a API da OpenAI.
- Respostas alternativas quando a IA não está configurada.
- Tratamento de falhas na comunicação com a API.
- Orientação para atendimento humano quando não há informações suficientes.

🛠️ Tecnologias utilizadas

- Python — linguagem principal.
- Flask — desenvolvimento da aplicação web.
- OpenAI API — geração de respostas com inteligência artificial.
- JSON — armazenamento da base de conhecimento.
- python-dotenv — gerenciamento de variáveis de ambiente.
- Unittest — criação de testes automatizados.
- Git e GitHub — versionamento e organização do projeto.

📂 Estrutura do projeto

portfolio-ai-builder/
│
├── app.py
├── faq.json
├── test_app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

⚙️ Como executar o projeto

1. Pré-requisitos

- Python 3.10 ou superior.
- Uma chave de API da OpenAI para utilizar as respostas geradas por IA.

2. Instalar as dependências

Clone o repositório:

git clone https://github.com/StefaniNeves/portfolio-ai-builder.git

Entre na pasta do projeto:

cd portfolio-ai-builder

Instale as dependências:

pip install -r requirements.txt

3. Configurar a API

Crie um arquivo chamado ".env" na raiz do projeto.

Adicione suas configurações:

OPENAI_API_KEY=sua_chave_de_api
OPENAI_MODEL=gpt-4o-mini

Substitua o valor de exemplo pela sua própria chave de API.

Importante: nunca publique sua chave de API no GitHub ou compartilhe suas credenciais.

Sem a chave configurada, o aplicativo ainda pode apresentar as informações encontradas na FAQ, mas não utilizará a geração de respostas pela OpenAI.

4. Executar a aplicação

No terminal, execute:

python app.py

Depois, acesse no navegador:

http://127.0.0.1:5000

🧪 Testes automatizados

O projeto possui testes desenvolvidos com a biblioteca "unittest", verificando:

- Carregamento da página inicial.
- Busca de perguntas cadastradas na FAQ.
- Identificação de perguntas sem informações correspondentes.

Para executar os testes, utilize:

python -m unittest test_app.py

💡 Aprendizados e objetivos

Este projeto foi desenvolvido como uma oportunidade de praticar conceitos de desenvolvimento de aplicações com inteligência artificial, incluindo:

- Integração com APIs de modelos de linguagem.
- Engenharia de prompts.
- Recuperação de informações a partir de uma base de conhecimento.
- Desenvolvimento de aplicações web com Python.
- Organização e documentação de projetos.
- Criação de testes automatizados.

🔮 Melhorias futuras

- Aprimorar o mecanismo de busca semântica.
- Expandir a base de conhecimento.
- Implementar histórico de conversas.
- Integrar um banco de dados.
- Desenvolver uma interface mais interativa.
- Disponibilizar a aplicação em ambiente de nuvem.

👩‍💻 Autora

Stefani Rodrigues Neves

Estudante de Bacharelado em Ciência da Computação — UFCA.

GitHub: "@StefaniNeves" (https://github.com/StefaniNeves)
