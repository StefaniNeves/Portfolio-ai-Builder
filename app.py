
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, render_template_string, request
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

FAQ_PATH = Path(__file__).parent / "faq.json"

with open(FAQ_PATH, "r", encoding="utf-8") as file:
    FAQ = json.load(file)

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

HTML_PAGE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Assistente de Atendimento com IA</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f5f7;
            margin: 0;
            padding: 30px 15px;
        }
        .container {
            max-width: 650px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 2px 12px #00000012;
        }
        h1 { color: #333; }
        textarea {
            width: 100%;
            box-sizing: border-box;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 8px;
            min-height: 100px;
        }
        button {
            margin-top: 12px;
            padding: 12px 20px;
            background: #e82136;
            color: white;
            border: none;
            border-radius: 7px;
            cursor: pointer;
        }
        .answer {
            margin-top: 22px;
            padding: 15px;
            background: #f1f5f9;
            border-radius: 8px;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Assistente de Atendimento com IA</h1>
        <p>Digite sua dúvida para receber orientação.</p>

        <form method="POST">
            <textarea name="question"
                placeholder="Digite sua pergunta..."
                required>{{ question }}</textarea>
            <button type="submit">Enviar pergunta</button>
        </form>

        {% if answer %}
        <div class="answer">
            <strong>Resposta:</strong>
            <p>{{ answer }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""


def search_faq(question):
    words = {
        word.lower().strip(".,!?;:")
        for word in question.split()
        if len(word) > 2
    }

    results = []

    for item in FAQ:
        text = (
            item["pergunta"] + " " + item["resposta"]
        ).lower()

        score = sum(1 for word in words if word in text)
        if score > 0:
            results.append((score, item))

    results.sort(key=lambda result: result[0], reverse=True)

    return [item for score, item in results[:3]]


def generate_answer(question, matches):
    if not matches:
        return (
            "Não encontrei informações suficientes "
            "na base de conhecimento. Procure um atendente."
        )

    context = "\n".join(
        f"Pergunta: {item['pergunta']}\n"
        f"Resposta: {item['resposta']}"
        for item in matches
    )

    if client is None:
        return (
            "A configuração da IA ainda não foi realizada. "
            "Informações encontradas na FAQ:\n\n"
            + "\n".join(item["resposta"] for item in matches)
        )

    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um assistente de atendimento. "
                        "Responda em português brasileiro. "
                        "Use somente as informações fornecidas. "
                        "Não invente respostas. "
                        "Se não houver informação suficiente, "
                        "oriente o usuário a procurar um atendente."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Contexto disponível:\n{context}\n\n"
                        f"Pergunta do usuário: {question}"
                    )
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception:
        return (
            "Não foi possível consultar a inteligência artificial. "
            "Verifique a conexão e a configuração da API."
        )


@app.route("/", methods=["GET", "POST"])
def home():
    question = ""
    answer = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()

        if question:
            matches = search_faq(question)
            answer = generate_answer(question, matches)

    return render_template_string(
        HTML_PAGE,
        question=question,
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=False)
