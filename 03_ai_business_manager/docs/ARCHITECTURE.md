# Arquitetura

```mermaid
flowchart TD
  U[Usuário / CSV] --> D[Dashboard Streamlit]
  U --> API[FastAPI /analyze]
  D --> S[Serviço de análise]
  API --> S
  S --> M[Métricas determinísticas de vendas]
  S --> O[Orquestrador de agentes - opcional]
  O --> GPT[OpenAI GPT]
  O --> CL[Anthropic Claude]
  O --> GE[Google Gemini]
  N[Webhook n8n] --> NC[Nó Code: métricas]
  NC --> NR[Resposta JSON]
  M --> OUT[Métricas + resultados dos provedores]
  GPT --> OUT
  CL --> OUT
  GE --> OUT
```

A camada de cálculos determinísticos funciona sem uma chave de API de modelos de linguagem. A camada de provedores é opcional, e eventuais falhas de cada provedor são informadas separadamente. As respostas dos provedores servem como apoio à análise e não executam ações automaticamente. O fluxo do n8n demonstra, de forma independente, uma automação de métricas de vendas acionada por webhook.

## Limites de confiança e segurança
- As chaves de API são carregadas por variáveis de ambiente e nunca devem ser enviadas ao repositório.
- Os arquivos CSV enviados pelo usuário são processados em memória pelo dashboard.
- As respostas geradas por IA podem conter imprecisões; as recomendações devem ser revisadas por uma pessoa.
- Os dados de exemplo são sintéticos e não devem ser apresentados como resultados reais de impacto em uma empresa.
