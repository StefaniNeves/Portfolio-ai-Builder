# 🤖 Assistente de Atendimento com Inteligência Artificial

Aplicação web desenvolvida em Python que utiliza Inteligência Artificial Generativa para auxiliar no atendimento ao cliente, consultando uma base de conhecimento com perguntas frequentes (FAQ).

O projeto integra Flask e a API da OpenAI para oferecer respostas contextualizadas.

> **Atenção:** este pacote é uma estrutura de referência. Substitua o `faq.json` de exemplo pela base de conhecimento original do seu projeto e confira as funcionalidades antes de publicar.

## 🎯 Objetivo

Desenvolver uma solução de atendimento inteligente capaz de receber perguntas em linguagem natural e fornecer respostas com base em informações previamente cadastradas.

## ✨ Funcionalidades

- Interface web para interação com o assistente.
- Envio de perguntas em linguagem natural.
- Integração com a API da OpenAI.
- Consulta contextualizada a uma base de conhecimento em JSON.
- Validação de perguntas vazias.
- Tratamento de erros durante o atendimento.
- Testes automatizados com Pytest.

## 🛠️ Tecnologias

- Python
- Flask
- OpenAI API
- JSON
- HTML5, CSS3 e JavaScript
- Pytest
- Git e GitHub

## 📁 Estrutura

```text
01_assistente_atendimento_ia/
├── app.py
├── faq.json
├── requirements.txt
├── .env.example
├── .gitignore
├── test_app.py
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── screenshots/
```

## ⚙️ Como executar

### 1. Pré-requisitos

- Python 3.10 ou superior
- Uma chave de API da OpenAI

### 2. Criar e ativar ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` nesta pasta, usando `.env.example` como modelo:

```env
OPENAI_API_KEY=sua_chave_de_api
OPENAI_MODEL=gpt-4o-mini
```

Não publique o arquivo `.env` nem compartilhe sua chave de API.

### 5. Executar

```bash
python app.py
```

Acesse `http://127.0.0.1:5000` no navegador.

## 🧪 Testes

Execute:

```bash
pytest -v
```

Os testes verificam a página inicial, a validação de perguntas e o endpoint de atendimento. A resposta da IA é simulada nos testes para evitar chamadas e custos da API.

## 🔄 Fluxo de funcionamento

1. O usuário envia uma pergunta pela interface.
2. O Flask recebe a solicitação no endpoint `/perguntar`.
3. A aplicação valida a entrada e carrega a base FAQ.
4. A FAQ é enviada como contexto para a API da OpenAI.
5. O modelo gera uma resposta contextualizada.
6. A resposta é devolvida à interface.

## 📸 Demonstração

Adicione capturas reais da aplicação na pasta `screenshots/`, por exemplo:

- `tela-inicial.png`
- `pergunta-enviada.png`
- `resposta-ia.png`

Quando as imagens estiverem disponíveis, você poderá incluí-las aqui:

```markdown
![Tela inicial](screenshots/tela-inicial.png)
```

## 🔐 Segurança

- Credenciais são configuradas por variáveis de ambiente.
- `.env` está listado no `.gitignore`.
- Não inclua chaves, tokens ou dados pessoais no repositório.

## 🚀 Melhorias futuras

- Histórico de conversas.
- Persistência em banco de dados.
- Recuperação de informações mais robusta.
- Autenticação de usuários.
- Monitoramento de uso e custos.
- Implantação em ambiente de produção.

## 👩‍💻 Autora

**Stefani Neves**  
Estudante de Ciência da Computação — Universidade Federal do Cariri (UFCA).

- GitHub: [StefaniNeves](https://github.com/StefaniNeves)
- LinkedIn: [Stefani Neves](https://linkedin.com/in/stefani-neves-1aa819333)

---

Projeto de portfólio com foco em Inteligência Artificial, desenvolvimento de software e integração de APIs.
