import os
from dotenv import load_dotenv
load_dotenv()

from app.core.analysis import analyze_sales
from app.core.demo import build_demo_analysis
from app.core.orchestrator import AgentOrchestrator
from app.providers.openai_provider import OpenAIProvider
from app.providers.anthropic_provider import ClaudeProvider
from app.providers.gemini_provider import GeminiProvider


def analyze_business(records: list[dict], use_ai: bool = False) -> dict:
    metrics = analyze_sales(records)
    response = {"metrics": metrics, "ai": {"mode": "not_requested", "results": []}}
    if use_ai:
        mode = os.getenv("AI_MODE", "demo").strip().lower()
        if mode == "live":
            response["ai"] = AgentOrchestrator([
                OpenAIProvider(), ClaudeProvider(), GeminiProvider()
            ]).run(metrics)
        else:
            response["ai"] = build_demo_analysis(metrics)
    return response
