AI Business Manager — Inteligência Artificial para Análise de Negócios

Solução de análise comercial com Python, API REST, dashboard interativo e integração com provedores de Inteligência Artificial.

O AI Business Manager é um projeto desenvolvido para demonstrar como soluções de automação e Inteligência Artificial podem apoiar a análise de dados comerciais e a tomada de decisões orientadas por dados.

A aplicação recebe registros de vendas, calcula indicadores de desempenho, organiza informações comerciais e gera recomendações para apoiar a interpretação dos resultados.

O projeto também apresenta uma arquitetura preparada para trabalhar com diferentes provedores de modelos de linguagem, além de oferecer um modo de demonstração independente de serviços externos.

1. Objetivo do projeto

Desenvolver uma solução que demonstre a aplicação prática de Inteligência Artificial em processos de negócio, reunindo:

- Análise e interpretação de dados comerciais.
- Automação de tarefas de análise.
- Orquestração de provedores de IA.
- Desenvolvimento de APIs.
- Visualização de indicadores em dashboard.
- Estruturação de fluxos de automação.
- Testes e documentação técnica.

2. Funcionalidades

Análise comercial

- Cálculo de faturamento total.
- Identificação da quantidade de unidades vendidas.
- Cálculo do faturamento médio por registro.
- Análise de faturamento por categoria.
- Identificação dos cinco produtos com maior faturamento.

Inteligência Artificial

- Estrutura de integração com OpenAI, Anthropic e Google Gemini.
- Organização dos provedores por meio de adaptadores.
- Orquestração das chamadas aos provedores.
- Prompts específicos para análise comercial e revisão de respostas.
- Modo de demonstração com recomendações geradas por regras locais.

API REST

- API desenvolvida com FastAPI.
- Endpoint de verificação de disponibilidade ("GET /health").
- Endpoint de análise comercial ("POST /analyze").
- Recebimento de registros de vendas em formato JSON.

Dashboard

- Interface interativa desenvolvida com Streamlit.
- Carregamento de dados comerciais por arquivo CSV.
- Exibição de indicadores e resultados da análise.
- Apresentação de recomendações.

Automação

- Fluxo de automação em formato JSON para importação no n8n.
- Documentação de arquitetura e possibilidades de integração com Make.
- Estrutura preparada para expansão dos processos automatizados.

3. Arquitetura da solução

O projeto foi organizado em módulos para separar responsabilidades e facilitar manutenção e evolução.

Camada| Responsabilidade
API| Recebimento de requisições e disponibilização dos serviços
Core| Regras de negócio, cálculos e processamento das análises
Providers| Adaptadores para diferentes provedores de IA
Orchestrator| Coordenação das integrações com os modelos
Dashboard| Interface de visualização dos resultados
Data| Dados comerciais utilizados na demonstração
Prompts| Instruções utilizadas nas análises e revisões
Tests| Testes automatizados das funcionalidades
n8n| Definição do fluxo de automação

4. Tecnologias utilizadas

- Python 3.11+ — linguagem principal.
- FastAPI — desenvolvimento da API REST.
- Streamlit — construção do dashboard.
- Pandas — processamento e análise de dados.
- Pydantic — validação de dados.
- Pytest — testes automatizados.
- HTTPX — testes e requisições HTTP.
- OpenAI, Anthropic e Google Gemini — provedores de modelos de IA.
- n8n — estruturação de fluxos de automação.
- Docker — containerização da aplicação.
- GitHub Actions — automação do pipeline de testes.

5. Estrutura do projeto

03_ai_business_manager/
│
├── app/
│   ├── api/
│   │   └── main.py
│   │
│   ├── core/
│   │   ├── analysis.py
│   │   ├── demo.py
│   │   ├── orchestrator.py
│   │   └── service.py
│   │
│   └── providers/
│       ├── base.py
│       ├── openai_provider.py
│       ├── anthropic_provider.py
│       └── gemini_provider.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── sample_sales.csv
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── IMPACT_MEASUREMENT.md
│   ├── MAKE_AUTOMATION.md
│   ├── TESTING.md
│   ├── VIBE_CODING.md
│   └── WORK_LOG.md
│
├── examples/
│   └── request.json
│
├── n8n/
│   └── ai_business_manager_workflow.json
│
├── prompts/
│   ├── business_analyst.md
│   └── reviewer.md
│
├── scripts/
│   └── generate_sample_data.py
│
├── tests/
│   ├── test_analysis.py
│   ├── test_api.py
│   └── test_demo.py
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── requirements.txt
└── README.md

6. Como executar

Requisitos

- Python 3.11 ou superior.
- Git.

Instalação

git clone https://github.com/StefaniNeves/Portfolio-ai-Builder.git

cd Portfolio-ai-Builder/03_ai_business_manager

python -m venv .venv

Ativação do ambiente virtual:

Windows:

.venv\Scripts\Activate.ps1

Linux/macOS:

source .venv/bin/activate

Instalação das dependências:

pip install -r requirements.txt

Configuração do ambiente:

Crie um arquivo ".env" utilizando ".env.example" como referência.

Modo demonstração

O projeto disponibiliza um modo de demonstração que utiliza dados de exemplo e regras locais para calcular indicadores e gerar recomendações, sem exigir chaves de API externas.

Executar a API

uvicorn app.api.main:app --reload

API:
"http://127.0.0.1:8000"

Documentação interativa:
"http://127.0.0.1:8000/docs"

Executar o dashboard

streamlit run dashboard/app.py

Executar os testes

pytest -v

Executar com Docker

docker compose up --build

7. Integrações com provedores de IA

A arquitetura contempla adaptadores para três provedores:

Provedor| Integração
OpenAI| Adaptador dedicado
Anthropic| Adaptador dedicado
Google Gemini| Adaptador dedicado

As integrações utilizam variáveis de ambiente para configuração das credenciais e dos modelos.

O modo "demo" funciona independentemente desses serviços. O modo "live" utiliza os adaptadores configurados e depende de credenciais válidas, disponibilidade dos provedores e acesso aos modelos.

8. Testes e qualidade

O projeto inclui testes automatizados para verificar:

- Cálculos e regras de análise comercial.
- Funcionamento dos endpoints da API.
- Comportamento do modo demonstração.

Também possui configuração de GitHub Actions para execução automatizada dos testes.

9. Segurança e boas práticas

- Utilização de variáveis de ambiente para credenciais.
- Arquivo ".env.example" para documentar configurações.
- Separação entre regras de negócio e integrações externas.
- Organização modular dos componentes.
- Testes automatizados.
- Documentação técnica.
- Dados fictícios para demonstração.

10. Evolução e possibilidades de aplicação

A arquitetura permite evoluir a solução para cenários como:

- Análise de desempenho comercial.
- Identificação de produtos com maior faturamento.
- Geração automatizada de relatórios.
- Apoio à tomada de decisões empresariais.
- Integração com sistemas de gestão.
- Automação de processos utilizando ferramentas de workflow.
- Expansão para novos provedores de modelos de Inteligência Artificial.

11. Considerações técnicas

Este projeto é um protótipo de portfólio desenvolvido para demonstrar conhecimentos em construção de soluções com IA, automação e desenvolvimento de software.

Os dados utilizados na demonstração são fictícios. As recomendações do modo demo são geradas por regras locais, não por modelos de linguagem.

Os adaptadores dos provedores estão presentes no código, mas a execução de chamadas reais depende de credenciais e configuração. O fluxo n8n é disponibilizado para importação e configuração. As documentações de Make e Cursor descrevem possibilidades e procedimentos, não comprovam execuções dessas ferramentas.

A solução não implementa autenticação ou autorização para uso em produção e não deve ser considerada um sistema empresarial pronto para implantação.

---

Autoria

Stefani Neves

Projeto desenvolvido como parte de um portfólio voltado à construção de soluções com Inteligência Artificial, automação de processos e desenvolvimento de aplicações orientadas a negócios.

Repositório: "Portfolio AI Builder — GitHub" (https://github.com/StefaniNeves/Portfolio-ai-Builder)
