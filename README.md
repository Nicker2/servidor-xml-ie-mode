<div align="center">

# 🌐 Leitor de XML
### Solução de Renderização XSLT para Arquivos Locais

<img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
<img src="https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/Status-Stable-success?style=for-the-badge" alt="Status">
<img src="https://img.shields.io/badge/Focus-Productivity-orange?style=for-the-badge" alt="Focus">

<br />

<p align="center">
  <b>Visualize arquivos XML locais com folhas de estilo (XSL) sem erros de segurança do navegador.</b><br>
  <i>Transforme sua pasta local em um servidor web instantâneo.</i>
</p>

</div>

---

## 🧐 O que é isso? (Para não técnicos)
Sabe quando você tenta abrir um arquivo **XML** no seu computador (aqueles de notas fiscais ou relatórios médicos) e ele abre em branco ou aparece todo "quebrado" ou então como um monte de códigos, sem a formatação bonita que deveria ter?

Isso acontece porque os navegadores modernos (Chrome, Edge) bloqueiam, por segurança, que arquivos locais carreguem seus estilos visuais.

**Este projeto resolve isso:** Ele cria um pequeno "site interno" no seu computador. Ao abrir os arquivos através dele, o navegador entende que é seguro e mostra o documento **perfeitamente formatado**.

> **Nota Importante:** Com esta implementação, **você geralmente NÃO precisa mais usar o "Modo Internet Explorer"** ou configurações complexas de compatibilidade. O servidor contorna a restrição de segurança original (`CORS/file://`), permitindo que o XML abra normalmente no Edge ou Chrome padrão.

---

## ⚡ O Problema vs. A Solução

| Cenário | Comportamento |
| :--- | :--- |
| **Padrão (Sem este App)** | O Edge bloqueia o XSL ao abrir via `file:///`. O XML carrega sem estilo ou exibe tela em branco. |
| **Modo IE (Manual)** | Funciona, mas exige adicionar *cada arquivo* ou pasta manualmente à lista de exceções. Trabalhoso e pouco prático. |
| **Com este servidor** | ✅ **Automático.** Transforma o acesso em `http://`, permitindo renderização perfeita em navegadores modernos sem configurações extras. |

---

## 🛠️ Stack Tecnológica

A aplicação foi construída visando leveza e facilidade de manutenção.

| Tecnologia | Função | Badge |
| :--- | :--- | :--- |
| **Python** | Linguagem Core | ![Python](https://img.shields.io/badge/python-3670A0?style=flat-square&logo=python&logoColor=white) |
| **Flask** | Servidor Web | ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat-square&logo=flask&logoColor=white) |
| **HTML5** | Estrutura da Interface | ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat-square&logo=html5&logoColor=white) |
| **CSS3** | Estilização da Lista | ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=flat-square&logo=css3&logoColor=white) |

---

## 🚀 Como Usar

Siga os passos abaixo para iniciar seu visualizador em menos de 2 minutos.

### 1. Instalação e Preparação

Certifique-se de ter o [Python](https://www.python.org/) instalado. Em seguida, instale a biblioteca Flask:

```bash
pip install Flask

```

### 2. Organização dos Arquivos

Crie uma pasta para o projeto e organize seus arquivos conforme a estrutura abaixo. O script listará automaticamente qualquer `.xml` colocado na raiz.

```text
/Visualizador-XML/
├── app.py                # O script do servidor (código fornecido)
├── nota_fiscal.xml       # Seus arquivos XML
├── relatorio.xml
├── estilo.xsl            # Seu arquivo de estilo (obrigatório para o XML)
├── templates/
│   └── index.html        # Interface de listagem
└── static/
    └── style.css         # Estilo da interface de listagem

```

### 3. Rodando a Aplicação

No seu terminal (CMD ou PowerShell), navegue até a pasta e execute:

```bash
python app.py

```

Você verá uma mensagem indicando que o servidor está rodando (geralmente em `Running on http://127.0.0.1:8000`).

### 4. Acessando

1. Abra seu navegador (Edge, Chrome, Firefox).
2. Acesse o endereço: **`http://127.0.0.1:8000`**
3. Clique no arquivo desejado na lista.

---

## ⚙️ Detalhes Técnicos e Code Snippets

O coração da aplicação reside no tratamento de rotas do Flask para servir tanto o XML quanto o XSL corretamente.

<details>
<summary><b>🔍 Ver Lógica de Ordenação (Python)</b></summary>

O sistema prioriza automaticamente os arquivos mais recentes para facilitar o fluxo de trabalho diário:

```python
# Trecho de app.py
@app.route('/')
def index():
    # ... código de listagem ...
    
    # Ordena: Mais recente primeiro
    sorted_file_details = sorted(
        file_details,
        key=lambda item: item['raw_time'],
        reverse=True
    )
    return render_template('index.html', files_list=sorted_file_details)

```

</details>

<details>
<summary><b>🛡️ Ver Lógica de Segurança e Rotas</b></summary>

Para garantir segurança, o servidor entrega apenas extensões permitidas na rota dinâmica:

```python
@app.route('/<filename>')
def serve_xml(filename):
    # Permite apenas .xml e .xsl
    if filename.endswith('.xml') or filename.endswith('.xsl'):
        return send_from_directory(XML_FOLDER, filename)
    
    return "Arquivo não encontrado ou tipo não permitido.", 404

```

</details>

---

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver ideias para melhorar a interface de listagem ou adicionar suporte a novos formatos:

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona NovaFeature'`)
4. Push para a Branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

---

<div align="center">
<sub>Desenvolvido para agilizar processos em ambientes hospitalares e corporativos.</sub>
</div>
