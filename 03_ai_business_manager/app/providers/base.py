from __future__ import annotations
from typing import Protocol, Any

class LLMProvider(Protocol):
    name: str
    def generate(self, prompt: str) -> str: ...

class ProviderNotConfigured(RuntimeError):
    pass


def build_business_prompt(metrics: dict[str, Any]) -> str:
    """Build a constrained prompt; metrics are supplied as JSON-like data."""
    import json
    return (
        "You are a careful business analyst. Analyze the sales metrics below. "
        "Separate observed facts from hypotheses, do not invent missing data, "
        "give three actionable recommendations, and state one limitation. "
        "Return concise Markdown in Brazilian Portuguese.\n\nMETRICS:\n"
        + json.dumps(metrics, ensure_ascii=False, indent=2)
    )
