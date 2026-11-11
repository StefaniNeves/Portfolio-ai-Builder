import app as modulo


def test_pagina_inicial():
    cliente = modulo.app.test_client()
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert b"Assistente de Atendimento" in resposta.data


def test_pergunta_vazia():
    cliente = modulo.app.test_client()
    resposta = cliente.post("/perguntar", json={"pergunta": ""})
    assert resposta.status_code == 400
    assert "erro" in resposta.get_json()


def test_pergunta_com_resposta_simulada(monkeypatch):
    cliente = modulo.app.test_client()
    monkeypatch.setattr(
        modulo,
        "gerar_resposta",
        lambda pergunta: "Nosso atendimento funciona das 8h às 18h."
    )

    resposta = cliente.post(
        "/perguntar",
        json={"pergunta": "Qual o horário de atendimento?"}
    )

    assert resposta.status_code == 200
    assert resposta.get_json()["resposta"] == (
        "Nosso atendimento funciona das 8h às 18h."
    )


def test_pergunta_sem_conteudo_json():
    cliente = modulo.app.test_client()
    resposta = cliente.post("/perguntar", json={})
    assert resposta.status_code == 400


def test_carregar_faq():
    dados = modulo.carregar_faq()
    assert isinstance(dados, list)
    if dados:
        assert "pergunta" in dados[0]
        assert "resposta" in dados[0]
