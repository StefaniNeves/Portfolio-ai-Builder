🤖 Assistente de Atendimento com Inteligência Artificial

Um assistente virtual de atendimento desenvolvido em Python, utilizando Flask e a API da OpenAI para interpretar perguntas e gerar respostas automaticamente. O projeto combina inteligência artificial com uma base de perguntas frequentes (FAQ) armazenada em JSON, oferecendo uma experiência simples e acessível de atendimento.

📌 Sobre o projeto

O Assistente de Atendimento com IA foi desenvolvido com o objetivo de demonstrar como a inteligência artificial pode ser aplicada na automação de atendimentos.

A aplicação permite que o usuário envie perguntas por meio de uma interface web e receba respostas geradas com o auxílio de um modelo de linguagem da OpenAI.

Além da integração com IA, o sistema utiliza uma base de perguntas frequentes para fornecer contexto às respostas, tornando o atendimento mais direcionado.

O projeto também apresenta conceitos importantes de desenvolvimento de software, como integração com APIs externas, organização de arquivos, manipulação de dados JSON, configuração de variáveis de ambiente e tratamento de erros.

🎯 Objetivos

- Desenvolver um assistente virtual utilizando inteligência artificial.
- Automatizar respostas para perguntas dos usuários.
- Integrar uma aplicação Python com a API da OpenAI.
- Utilizar uma base de conhecimento em formato JSON.
- Desenvolver uma interface web simples e intuitiva.
- Aplicar conceitos de desenvolvimento backend e frontend.
- Praticar organização de código, testes e documentação.

⚙️ Tecnologias utilizadas

Tecnologia| Aplicação no projeto
Python| Linguagem principal
Flask| Desenvolvimento da aplicação web
OpenAI API| Geração de respostas com inteligência artificial
HTML5| Estrutura da interface
CSS3| Estilização da interface
JSON| Armazenamento das perguntas frequentes
python-dotenv| Gerenciamento de variáveis de ambiente
Pytest| Execução de testes automatizados
Git e GitHub| Versionamento e hospedagem do projeto

📂 Estrutura do projeto

01_assistente_atendimento_ia/
│
├── app.py
├── faq.json
├── requirements.txt
├── .env.example
├── .gitignore
├── test_app.py
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── screenshots/
    └── README.txt

Descrição dos arquivos

- app.py: arquivo principal da aplicação. Responsável pelas rotas, integração com a API da OpenAI e processamento das perguntas.
- faq.json: armazena perguntas frequentes e suas respectivas respostas, utilizadas como base de conhecimento.
- requirements.txt: lista as bibliotecas necessárias para executar o projeto.
- .env.example: apresenta o modelo de configuração das variáveis de ambiente.
- .gitignore: define arquivos e pastas que não devem ser enviados ao GitHub.
- test_app.py: contém testes automatizados para verificar funcionalidades da aplicação.
- templates/index.html: estrutura da interface web.
- static/style.css: contém os estilos visuais da aplicação.
- screenshots/: diretório reservado para imagens da execução do sistema.
- Observação: As imagens desta seção são ilustrativas e representam uma demonstração visual da interface proposta para o projeto. Elas não correspondem a registros de uma execução real da aplicação.

🚀 Como executar o projeto

1. Pré-requisitos

Antes de começar, é necessário ter instalado:

- Python 3.10 ou superior.
- Git.
- Um editor de código, como Visual Studio Code.
- Uma chave de API da OpenAI.

2. Clonar o repositório

git clone https://github.com/StefaniNeves/01_assistente_atendimento_ia.git

Entre na pasta do projeto:

cd 01_assistente_atendimento_ia

3. Criar um ambiente virtual

python -m venv venv

Ative o ambiente virtual.

Windows:

venv\Scripts\activate

Linux e macOS:

source venv/bin/activate

4. Instalar as dependências

pip install -r requirements.txt

5. Configurar a chave da API

Crie um arquivo chamado ".env" na raiz do projeto, utilizando o ".env.example" como referência.

Configure as variáveis:

OPENAI_API_KEY=sua_chave_de_api_aqui
OPENAI_MODEL=gpt-4o-mini

Substitua o valor de "OPENAI_API_KEY" pela sua chave válida da OpenAI.

Importante: nunca compartilhe sua chave de API ou envie o arquivo ".env" para o GitHub.

6. Executar a aplicação

Com o ambiente virtual ativado e as dependências instaladas, execute:

python app.py

Acesse no navegador o endereço:

http://127.0.0.1:5000

💬 Como funciona

O funcionamento da aplicação pode ser dividido nas seguintes etapas:

1. O usuário acessa a interface web.
2. Digita uma pergunta no campo de atendimento.
3. A aplicação recebe a mensagem por meio de uma rota do Flask.
4. O sistema consulta a base de perguntas frequentes armazenada em JSON.
5. As informações relevantes são utilizadas como contexto para a inteligência artificial.
6. A aplicação envia a solicitação para a API da OpenAI.
7. O modelo processa a pergunta e gera uma resposta.
8. A resposta é apresentada ao usuário na interface.

🧪 Testes automatizados

O projeto possui testes automatizados utilizando o Pytest.

Para executar os testes, utilize:

pytest -v

Os testes ajudam a verificar o comportamento de partes importantes da aplicação, contribuindo para identificar possíveis erros e manter o funcionamento esperado do sistema.

🔐 Segurança e configuração

Alguns cuidados foram considerados na organização do projeto:

- Utilização de variáveis de ambiente para armazenar informações sensíveis.
- Arquivo ".gitignore" para evitar o envio de arquivos desnecessários.
- Separação entre código Python, interface e estilos.
- Uso de arquivo de exemplo para orientar a configuração do ambiente.

📚 Conhecimentos aplicados

Durante o desenvolvimento deste projeto, são trabalhados conceitos relacionados a:

- Programação em Python.
- Desenvolvimento de aplicações web com Flask.
- Integração com APIs REST.
- Requisições HTTP.
- Manipulação de arquivos JSON.
- Inteligência Artificial Generativa.
- Engenharia de prompts.
- Variáveis de ambiente.
- Testes automatizados.
- Organização e documentação de projetos.

🔮 Possíveis melhorias futuras

O projeto pode ser ampliado com novas funcionalidades, como:

- Histórico de conversas.
- Armazenamento de atendimentos em banco de dados.
- Cadastro de perguntas frequentes por meio de uma interface administrativa.
- Personalização das respostas conforme o contexto do atendimento.
- Integração com WhatsApp.
- Implementação de autenticação de usuários.
- Melhorias na interface e na experiência de utilização.

👩‍💻 Autoria

Projeto desenvolvido como parte dos estudos em Ciência da Computação, com foco na aplicação prática de Python, desenvolvimento web e integração com inteligência artificial.

Desenvolvedora: Stefani Neves

GitHub: "StefaniNeves" (https://github.com/StefaniNeves)

---

⭐ Projeto desenvolvido para fins de aprendizado e prática de desenvolvimento de soluções utilizando Inteligência Artificial.
