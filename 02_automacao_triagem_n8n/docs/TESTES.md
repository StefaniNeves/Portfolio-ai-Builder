# Roteiro de testes

Os casos abaixo devem ser executados no seu ambiente n8n depois de importar o workflow e configurar a credencial. Eles são um roteiro de validação, não evidência de que os testes já foram executados.

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Solicitação completa | `assunto` e `mensagem` preenchidos | Workflow chama a IA e retorna a estrutura de triagem |
| Campo assunto ausente | Sem `assunto` | Node de validação interrompe a execução com erro de campo obrigatório |
| Mensagem vazia | `mensagem` vazia | Node de validação interrompe a execução |
| Falha de autenticação | Credencial inválida | Resposta de falha e encaminhamento manual |
| Resposta inesperada | Conteúdo não interpretável como JSON | Resposta de falha sem classificação automática |

## Evidências

Após executar cada teste:
1. Abra a execução no n8n.
2. Registre uma captura de tela mostrando o workflow e o resultado.
3. Oculte e-mails, tokens, IDs privados e outros dados sensíveis.
4. Salve as imagens na pasta `screenshots/`.
5. Atualize o README com os testes que realmente foram executados.

Não marque um teste como aprovado sem executar no seu próprio ambiente.
