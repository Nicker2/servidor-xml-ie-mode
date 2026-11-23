# 📜 Histórico de alterações

> Voltar para o [README](../README.md). O projeto não tem números de versão; as entradas seguem as datas dos commits.

### 18/12/2025 — documentação

- README revisado com a comparação "duplo clique × Modo IE × Leitor de XML".

### 04/11/2025 — primeira versão

- Servidor Flask em `127.0.0.1:8000` que lista os `.xml` da pasta, do mais recente para o mais antigo, com data e hora.
- Rota de arquivos que entrega o `.xml` **e** o `.xsl` (o comentário no código registra que essa foi a correção que fez a folha de estilo carregar).
- Página da lista com caixa de busca e visual próprio (`templates/index.html` e `static/style.css`).
