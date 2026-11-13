import os
from .base import ProviderNotConfigured

class ClaudeProvider:
    name = "Claude / Anthropic"
    def generate(self, prompt: str) -> str:
        key = os.getenv("ANTHROPIC_API_KEY")
        if not key:
            raise ProviderNotConfigured("ANTHROPIC_API_KEY is not configured")
        try:
            from anthropic import Anthropic
        except ImportError as exc:
            raise ProviderNotConfigured("Install the anthropic package to use Claude") from exc
        response = Anthropic(api_key=key).messages.create(
            model=os.getenv("ANTHROPIC_MODEL", "claude-3-5-haiku-latest"),
            max_tokens=1200, temperature=0.2,
            messages=[{"role": "user", "content": prompt}],
        )
        return "\n".join(block.text for block in response.content if hasattr(block, "text"))
