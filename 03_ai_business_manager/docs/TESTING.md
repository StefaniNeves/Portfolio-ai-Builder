# Testing and reproducibility

Run the automated tests:

```bash
python -m pip install -r requirements.txt
pytest -q
```

Run the API:

```bash
uvicorn app.api.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for interactive API documentation. Send the JSON in
`examples/request.json` to `POST /analyze`.

Run the dashboard in another terminal:

```bash
streamlit run dashboard/app.py
```

The automated tests cover deterministic metric calculations and API behavior. They do not
validate live third-party LLM credentials or prove a Make/n8n scenario has run in your account.
