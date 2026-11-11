import json
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from openai import OpenAI

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
FAQ_PATH = BASE_DIR / "faq.json"

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI(api_key=api_key) if api_key else None


def carregar_faq():
    """Carrega e valida a base de perguntas frequentes."""
    try:
        with open(FAQ_PATH, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        if not isinstance(dados, list):
            raise ValueError("A base FAQ precisa ser uma lista.")

        for item in dados:
            if not isinstance(item, dict) or not item.get("pergunta") or not item.get("resposta"):
                raise ValueError("Cada item da FAQ precisa conter pergunta e resposta.")

        return dados
    except FileNotFoundError as erro:
        raise RuntimeError("Arquivo faq.json não encontrado.") from erro
    except json.JSONDecodeError as erro:
        raise RuntimeError("O arquivo faq.json contém JSON inválido.") from erro


def gerar_resposta(pergunta):
    """Gera uma resposta usando a FAQ como contexto para o modelo de linguagem."""
    if client is None:
        raise RuntimeError("A chave da API da OpenAI não foi configurada.")

    faq = carregar_faq()
    contexto = "\n".join(
        f"Pergunta: {item['pergunta']}\nResposta: {item['resposta']}"
        for item in faq
    )

    resposta = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um assistente de atendimento. Use a base de conhecimento "
                    "fornecida para responder. Não invente informações. Se a resposta "
                    "não estiver na base, informe educadamente que não encontrou "
                    "essa informação e oriente o usuário a procurar o atendimento."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Base de conhecimento:\n{contexto}\n\n"
                    f"Pergunta do cliente: {pergunta}"
                ),
            },
        ],
        temperature=0.2,
    )

    conteudo = resposta.choices[0].message.content
    return conteudo.strip() if conteudo else "Não foi possível gerar uma resposta."


@app.route("/", methods=["GET"])
def inicio():
    return render_template("index.html")


@app.route("/perguntar", methods=["POST"])
def perguntar():
    dados = request.get_json(silent=True) or {}
    pergunta = dados.get("pergunta", "")

    if not isinstance(pergunta, str) or not pergunta.strip():
        return jsonify({"erro": "Digite uma pergunta para continuar."}), 400

    try:
        resposta = gerar_resposta(pergunta.strip())
        return jsonify({"pergunta": pergunta.strip(), "resposta": resposta})
    except Exception:
        app.logger.exception("Erro ao processar pergunta.")
        return jsonify({
            "erro": "Não foi possível processar sua pergunta. Tente novamente."
        }), 500


if __name__ == "__main__":
    # debug=True é adequado apenas para desenvolvimento local.
    app.run(debug=True)
