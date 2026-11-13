# Testes e reprodução do projeto

Instale as dependências e execute os testes automatizados:

```bash
python -m pip install -r requirements.txt
pytest -q
```

Inicie a API:

```bash
uvicorn app.api.main:app --reload
```

Acesse `http://127.0.0.1:8000/docs` para abrir a documentação interativa da API. Envie o conteúdo do arquivo `examples/request.json` para o endpoint `POST /analyze`.

Inicie o dashboard em outro terminal:

```bash
streamlit run dashboard/app.py
```

Os testes automatizados verificam os cálculos determinísticos das métricas e o comportamento da API. Eles não validam credenciais reais de provedores externos de modelos de linguagem nem comprovam que um cenário do Make ou do n8n foi executado na sua conta.
