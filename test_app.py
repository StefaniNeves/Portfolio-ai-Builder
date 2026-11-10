import unittest
import app as assistant


class TestAssistente(unittest.TestCase):

    def setUp(self):
        self.client = assistant.app.test_client()

    def test_pagina_inicial(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_busca_pergunta_faq(self):
        resultado = assistant.search_faq(
            "Quais são os horários de atendimento?"
        )
        self.assertGreater(len(resultado), 0)

    def test_pergunta_sem_resposta(self):
        resultado = assistant.search_faq(
            "Qual é a cor do planeta Marte?"
        )
        self.assertEqual(resultado, [])


if __name__ == "__main__":
    unittest.main()
