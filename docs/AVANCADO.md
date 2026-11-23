# 🛠️ Detalhes técnicos

> Voltar para o [README](../README.md).

## Sumário

- [Rotas](#rotas)
- [Ordenação da lista](#ordenação-da-lista)
- [Segurança](#segurança)
- [Personalização](#personalização)
- [Arquivos do repositório](#arquivos-do-repositório)

---

## Rotas

`app.py` tem três rotas. A pasta servida (`XML_FOLDER`) é a pasta onde está o próprio `app.py`.

| Rota | O que faz |
| :--- | :--- |
| `/` | Lista os arquivos que terminam em `.xml` em `XML_FOLDER` (sem subpastas) e renderiza `templates/index.html`. |
| `/<filename>` | Entrega o arquivo se o nome terminar em `.xml` ou `.xsl`. Qualquer outro: `404` com "Arquivo não encontrado ou tipo não permitido." |
| `/static/<path>` | Entrega o `style.css` da página da lista. |

```python
@app.route('/<filename>')
def serve_xml(filename):
    # Permite que o servidor entregue arquivos .xml E .xsl
    if filename.endswith('.xml') or filename.endswith('.xsl'):
        return send_from_directory(XML_FOLDER, filename)
    return "Arquivo não encontrado ou tipo não permitido.", 404
```

Como o XML e o XSL saem do mesmo endereço (`http://127.0.0.1:8000/`), a instrução `<?xml-stylesheet type="text/xsl" href="estilo.xsl"?>` dentro do XML é resolvida pelo navegador como `http://127.0.0.1:8000/estilo.xsl`, sem o bloqueio que acontece em `file:///`.

---

## Ordenação da lista

Para cada `.xml`, o servidor guarda o nome, o horário bruto (`os.path.getctime`) e o horário formatado (`dd/mm/aaaa hh:mm:ss`), e ordena do mais recente para o mais antigo:

```python
sorted_file_details = sorted(
    file_details,
    key=lambda item: item['raw_time'],
    reverse=True
)
return render_template('index.html', files_list=sorted_file_details)
```

No Windows, `getctime` é a data de **criação** do arquivo naquela pasta.

A busca da página (`filterFiles()` em `index.html`) roda no navegador: esconde os itens cujo nome não contém o texto digitado, sem diferenciar maiúsculas.

---

## Segurança

- **Só local:** `app.run(port=8000, debug=True)` escuta apenas em `127.0.0.1`.
- **Modo debug ligado:** o Flask recarrega sozinho quando o `app.py` muda e mostra o depurador interativo em caso de erro. Esse depurador permite executar código, por isso o servidor **nunca** deve ser aberto para a rede (`host="0.0.0.0"`) com `debug=True`.
- **Sem sair da pasta:** `send_from_directory` recusa caminhos que tentam sair de `XML_FOLDER` (como `../`).
- **Extensões:** só `.xml` e `.xsl` (comparação sensível a maiúsculas: `.XML` não passa).

---

## Personalização

| O que mudar | Onde |
| :--- | :--- |
| Porta | `app.run(port=8000, ...)` no fim do `app.py`. |
| Pasta dos XML | `XML_FOLDER` no começo do `app.py`. |
| Título e textos da página | `templates/index.html`. |
| Cores e espaçamento da lista | `static/style.css`. |

---

## Arquivos do repositório

| Arquivo | Para que serve |
| :--- | :--- |
| `app.py` | Servidor Flask. |
| `templates/index.html` | Página da lista, com a caixa de busca. |
| `static/style.css` | Visual da lista. |
| `README.md`, `docs/`, `assets/` | Documentação. |
| `.gitignore` | Arquivos ignorados pelo Git. |
