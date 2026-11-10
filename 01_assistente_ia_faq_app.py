
import os
import json
from pathlib import Path

from flask import Flask, request, render_template_string
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

FAQ_PATH = Path(__file__).with_name("faq.json")
FAQ = json.loads(FAQ_PATH.read_text(encoding="utf-8"))

PAGE = """
<!doctype html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <title>Assistente de Atendimento com IA</title>
</head>
<body>
    <h1>Assistente de Atendimento com IA</h1>
    <form method="post">
        <textarea name="question" required
        placeholder="Digite sua dúvida"></textarea>
        <button type="submit">Enviar</button>
    </form>
    {% if answer %}
        <h3>Resposta:</h3>
        <p>{{ answer }}</p>
    {% endif %}
</body>
</html>
"""

def retrieve_context(question):
    words = {
        word.lower().strip(".,!?;:")
        for word in question.split()
        if len(word) > 3
    }

    scored = []

    for item in FAQ:
        content = (
            item["pergunta"] + " " + item["resposta"]
        ).lower()

        score = sum(1 for word in words if word in content)
        scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)

    matches = [
        item for score, item in scored[:3] if score > 0
    ]

    if not matches:
        return "Nenhuma informação específica encontrada."

    return "\n".join(
        f"Pergunta: {item['pergunta']}\n"
        f"Informação: {item['resposta']}"
        for item in matches
    )

@app.route("/", methods=["GET", "POST"])
def home():
    question = ""
    answer = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()

        if question:
            context = retrieve_context(question)

            try:
                result = client.chat.completions.create(
                    model=os.getenv(
                        "OPENAI_MODEL", "gpt-4o-mini"
                    ),
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "Você é um assistente cordial. "
                                "Responda em português brasileiro. "
                                "Use somente o contexto fornecido. "
                                "Não invente informações. "
                                "Se faltar informação, recomende "
                                "atendimento humano."
                            )
                        },
                        {
                            "role": "user",
                            "content": (
                                f"Contexto:\n{context}\n\n"
                                f"Dúvida: {question}"
                            )
                        }
                    ],
                    temperature=0.2
                )

                answer = (
                    result.choices[0].message.content
                    or "Não foi possível gerar uma resposta."
                )

            except Exception as exc:
                answer = (
                    "Erro ao consultar a IA. "
                    "Verifique a configuração da API. "
                    f"Detalhe: {type(exc).__name__}"
                )

    return render_template_string(
        PAGE,
        question=question,
        answer=answer
    )

if __name__ == "__main__":
    app.run(debug=True)
