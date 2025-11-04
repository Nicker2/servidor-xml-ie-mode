# Visualizador de XML Local para Modo IE

Este é um pequeno servidor web local feito em Python (Flask) para resolver o problema de visualização de arquivos XML locais que dependem de folhas de estilo (.xsl) e só funcionam corretamente no Modo IE do Microsoft Edge.

## 🚀 O Problema
1.  O Edge, por padrão, não abre arquivos XML locais (`file:///...`) com estilos .xsl corretamente.
2.  O Modo IE do Edge resolve isso, mas não é prático adicionar cada arquivo XML manualmente à lista de sites do Modo IE.
3.  Precisávamos de uma forma de ver os XMLs mais recentes primeiro.

## ✅ A Solução
Este servidor local (`app.py`) cria um "site" em `http://127.0.0.1:8000` que:
* É 100% local e não é acessível pela rede.
* Lista dinamicamente todos os arquivos `.xml` na mesma pasta.
* Ordena a lista, mostrando o arquivo mais recente no topo (com data e hora).
* Serve os arquivos `.xsl` necessários para a renderização.

Ao adicionar apenas `http://127.0.0.1:8000` à lista do Modo IE do Edge, todos os XMLs abertos a partir dele funcionam perfeitamente.

## ⚙️ Como Usar

1.  **Instalar dependências** (Flask):
    `pip install Flask`

2.  **Estrutura de Pastas:**
    Coloque os arquivos `.xml` e `.xsl` na pasta raiz, junto com o `app.py`.
    ```
    /Visualizador-XML/
    ├── app.py
    ├── arquivo1.xml
    ├── estilo.xsl
    ├── templates/
    │   └── index.html
    └── static/
        └── style.css
    ```

3.  **Rodar o Servidor:**
    `python app.py`

4.  **Configurar o Edge** (Apenas uma vez):
    * Ir para `Configurações` > `Navegador padrão`
    * Adicionar `http://127.0.0.1:8000` à lista de "Páginas do modo Internet Explorer".

5.  **Acessar:**
    Abra `http://127.0.0.1:8000` no Edge.
