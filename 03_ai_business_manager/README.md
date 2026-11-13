# AI Business Manager — AI Builder Portfolio Project 03

A small business intelligence prototype that turns sales records into transparent metrics,
exposes them through a REST API, displays them in a dashboard, and can optionally request
independent analyses from GPT, Claude, and Gemini. An n8n workflow demonstrates a separate
webhook-based automation path.

> **Honesty note:** the included CSV is synthetic sample data. This repository does not claim
> production deployment, completed Make runs, measured customer impact, or successful live
> calls to all three LLM providers. Those require configuration and execution by the project
> author. Screenshots and evidence should be added only after real tests.

## Why this project exists

Small teams often spend time consolidating sales spreadsheets and preparing recurring
summaries. This prototype demonstrates one way to automate the first layer of analysis while
keeping calculations deterministic and AI recommendations reviewable by a human.

## Features

- Sales metrics: revenue, units sold, average revenue per record, category totals, top products.
- REST API built with FastAPI (`GET /health`, `POST /analyze`).
- Streamlit dashboard with CSV upload and charts.
- Optional provider adapters for OpenAI GPT, Anthropic Claude, and Google Gemini.
- Prompt templates with explicit constraints against invented facts.
- n8n webhook workflow that validates input and calculates sales metrics.
- Unit/API tests and GitHub Actions workflow.
- Guides for Make automation, Cursor evidence, testing, and impact measurement.

## Architecture

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the Mermaid diagram, components, and
trust boundaries.

## Repository structure

```text
ai_business_manager/
├── app/
│   ├── api/main.py
│   ├── core/                 # metrics, service, orchestration
│   └── providers/            # GPT, Claude, Gemini adapters
├── dashboard/app.py
├── data/sample_sales.csv
├── docs/                     # architecture, tests, impact, Make, Cursor, work log
├── examples/request.json
├── n8n/ai_business_manager_workflow.json
├── prompts/
├── scripts/
├── tests/
├── .github/workflows/tests.yml
├── .env.example
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Run locally

Requires Python 3.11 or newer.

```bash
git clone https://github.com/YOUR-USERNAME/ai-business-manager.git
cd ai-business-manager
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install dependencies and run tests:

```bash
python -m pip install -r requirements.txt
pytest -q
```

Start the API:

```bash
uvicorn app.api.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to inspect and test the endpoints.

Start the dashboard in a second terminal:

```bash
streamlit run dashboard/app.py
```

## Test the API

Send `examples/request.json` to `POST http://127.0.0.1:8000/analyze`, or use:

```bash
curl -X POST http://127.0.0.1:8000/analyze \\
  -H "Content-Type: application/json" \\
  --data @examples/request.json
```

The example sets `use_ai` to `false`, so the deterministic analysis works without paid API
credentials.

## Enable live LLM providers (optional)

1. Copy `.env.example` to `.env`.
2. Add the API keys for the providers you have access to.
3. Never commit `.env`; it is excluded by `.gitignore`.
4. Install dependencies and start the API/dashboard from the same environment.
5. Set `use_ai: true` in an API request or check the dashboard option.

Each provider is called independently. Missing keys or provider errors are returned per
provider instead of being presented as successful results. API usage may incur costs and is
subject to provider quotas and model availability. Do not share API keys with recruiters.

## n8n workflow

Import [`n8n/ai_business_manager_workflow.json`](n8n/ai_business_manager_workflow.json) into
n8n, activate it for a test environment, and send a POST request to its webhook with a
`records` array. The workflow validates numeric fields, calculates revenue metrics, and
returns JSON. See the workflow notes and capture an actual execution after testing it.

## Make and vibe coding

- [`docs/MAKE_AUTOMATION.md`](docs/MAKE_AUTOMATION.md): reproducible Make scenario guide.
- [`docs/VIBE_CODING.md`](docs/VIBE_CODING.md): how to document a real Cursor-assisted change.

These are implementation guides, not claims that those external steps have already been
performed. Add execution evidence only after completing them.

## Evidence and business impact

Use [`docs/WORK_LOG.md`](docs/WORK_LOG.md) to record actual runs. Follow
[`docs/IMPACT_MEASUREMENT.md`](docs/IMPACT_MEASUREMENT.md) to compare a manual baseline with
assisted processing. Do not report estimated time savings as measured impact. Do not use the
synthetic CSV as evidence of a real company's results.

Recommended evidence to add to the repository after running the project:

- `docs/evidence/dashboard-real-run.png`
- `docs/evidence/api-response-real-run.png`
- `docs/evidence/n8n-execution-real-run.png`
- `docs/evidence/make-execution-real-run.png`
- a short GIF/video showing the actual dashboard (with secrets and personal data removed)

## Limitations and responsible use

- The prototype is not a production system and has no authentication or role-based access.
- The sample dataset is synthetic; no real business data is included.
- AI output can be inaccurate, biased, or inconsistent across providers.
- Recommendations require human review; the system does not execute business actions.
- Provider adapters need valid credentials, network access, and compatible model access.
- The n8n workflow is included but must be imported and executed in the user's n8n instance.
- Make integration is documented as a reproducible exercise and must be built/tested separately.

## Project status

| Component | Repository status | What remains |
|---|---|---|
| Core sales metrics | Implemented | Run locally and verify |
| FastAPI | Implemented | Run locally and verify |
| Streamlit dashboard | Implemented | Run locally and capture evidence |
| GPT / Claude / Gemini adapters | Code included | Configure keys and test each provider |
| n8n workflow | JSON included | Import and execute in n8n |
| Make scenario | Guide included | Build and execute in Make |
| Cursor / vibe coding | Evidence guide included | Make and document a real change |
| Impact measurement | Method documented | Run a pilot and publish measured values |

## Author

**Stefani Neves** — Computer Science student. Add a short, accurate description of your own
contribution and the parts you personally implemented or validated before submitting the
portfolio.

---

This project is a portfolio prototype for demonstrating AI Builder concepts. It is not
affiliated with or endorsed by iFood.
