from __future__ import annotations
from typing import Any
from app.providers.base import build_business_prompt, ProviderNotConfigured

class AgentOrchestrator:
    """Runs selected LLM providers independently and reports partial failures."""
    def __init__(self, providers: list[Any] | None = None):
        self.providers = providers or []

    def run(self, metrics: dict[str, Any]) -> dict[str, Any]:
        prompt = build_business_prompt(metrics)
        results: list[dict[str, str]] = []
        for provider in self.providers:
            try:
                results.append({"provider": provider.name, "status": "success",
                                "analysis": provider.generate(prompt)})
            except (ProviderNotConfigured, Exception) as exc:
                results.append({"provider": provider.name, "status": "error",
                                "error": str(exc)})
        return {"mode": "live" if any(r["status"] == "success" for r in results) else "not_configured",
                "results": results}
