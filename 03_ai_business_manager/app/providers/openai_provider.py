import os
from .base import ProviderNotConfigured

class OpenAIProvider:
    name = "GPT / OpenAI"
    def generate(self, prompt: str) -> str:
        key = os.getenv("OPENAI_API_KEY")
        if not key:
            raise ProviderNotConfigured("OPENAI_API_KEY is not configured")
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise ProviderNotConfigured("Install the openai package to use GPT") from exc
        response = OpenAI(api_key=key).chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}], temperature=0.2,
        )
        return response.choices[0].message.content or "No text returned."
