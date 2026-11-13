import os
from .base import ProviderNotConfigured

class GeminiProvider:
    name = "Gemini / Google"
    def generate(self, prompt: str) -> str:
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise ProviderNotConfigured("GEMINI_API_KEY is not configured")
        try:
            from google import genai
        except ImportError as exc:
            raise ProviderNotConfigured("Install google-genai to use Gemini") from exc
        client = genai.Client(api_key=key)
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-2.0-flash"), contents=prompt
        )
        return response.text or "No text returned."
