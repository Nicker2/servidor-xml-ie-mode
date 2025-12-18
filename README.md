<div align="center">

# 🌐 Visualizador de XML Local para Modo IE
### Solução leve para renderização de XML + XSL local no Microsoft Edge

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=none)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Server-000000?style=for-the-badge&logo=flask&logoColor=white)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)

<p align="center">
  <a href="#-o-problema">O Problema</a> •
  <a href="#-a-solução">A Solução</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-como-usar">Como Usar</a> •
  <a href="#-troubleshooting">Troubleshooting</a>
</p>

</div>

---

## 🚀 O Problema

Desenvolvedores e analistas frequentemente enfrentam dificuldades ao visualizar arquivos XML locais que dependem de folhas de estilo **XSLT** (`.xsl`) nos navegadores modernos, devido a políticas de segurança rigorosas (CORS e *Local File Restrictions*).

> ❌ **O Cenário Comum:** Ao tentar abrir `file:///C:/relatorio.xml` no Edge, o estilo não é aplicado e o usuário vê apenas a árvore de código crua.
>
> ⚠️ **A Limitação do Modo IE:** Embora o "Modo IE" resolva a renderização, adicionar manualmente o caminho de cada arquivo local à lista de exceções é inviável e improdutivo.

## ✅ A Solução

Este projeto implementa um servidor web local (`app.py`) que atua como um *middleware* de visualização. Ele cria um ambiente controlado em `localhost` para servir os arquivos corretamente.

**Principais Funcionalidades:**

| Feature | Descrição |
| :--- | :--- |
| **🛡️ 100% Local** | Roda em `127.0.0.1`. Nenhuma informação sai da sua máquina. |
| **📂 Listagem Dinâmica** | Varre o diretório e lista automaticamente todos os arquivos `.xml`. |
| **📅 Ordenação Inteligente** | Exibe os arquivos mais recentes no topo (baseado na data de modificação). |
| **🎨 Renderização Full** | Serve corretamente os arquivos `.xsl` vinculados, permitindo visualização perfeita. |
| **⚡ Configuração Única** | Basta adicionar o `localhost` ao Modo IE uma única vez. |

---

## 🛠 Tech Stack

A aplicação foi construída utilizando tecnologias robustas e leves:

| Tecnologia | Uso no Projeto |
| :--- | :--- |
| <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> | Lógica de Backend e manipulação de arquivos. |
| <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" /> | Micro-framework para servir a aplicação web. |
| <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" /> | Estrutura da interface de listagem (`index.html`). |
| <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" /> | Estilização da interface (`style.css`). |

---

## ⚙️ Como Usar

Siga os passos abaixo para configurar o ambiente.

### 1. Pré-requisitos
Certifique-se de ter o Python instalado e instale o Flask:

```bash
pip install Flask

```

### 2. Estrutura de Diretórios

Mantenha a organização dos arquivos conforme a árvore abaixo para garantir o funcionamento do `send_from_directory`:

```text
/Visualizador-XML/
├── app.py                # Script do Servidor (Lógica principal)
├── arquivo_exemplo.xml   # Seus arquivos XML
├── estilo.xsl            # Suas folhas de estilo
├── templates/
│   └── index.html        # Frontend da lista de arquivos
└── static/
    └── style.css         # Estilos da lista

```

### 3. Executando o Servidor

No terminal, navegue até a pasta do projeto e execute:

```bash
python app.py

```

*O servidor iniciará em `http://127.0.0.1:8000`.*

### 4. Configuração do Edge (Passo Único)

Para que a renderização do XSL funcione, precisamos instruir o Edge a tratar este endereço como "Legacy":

1. Abra o Edge e vá para `Configurações` > `Navegador padrão`.
2. Na seção **"Páginas do modo Internet Explorer"**, clique em **Adicionar**.
3. Insira a URL: `http://127.0.0.1:8000`
4. Clique em **Adicionar** novamente.

> 💡 **Pronto!** Agora, basta acessar o link no navegador. O ícone do Internet Explorer aparecerá na barra de endereços, indicando que o modo de compatibilidade está ativo.

---

## 🧩 Detalhes da Implementação

Para curiosos ou desenvolvedores que desejam entender a lógica de segurança aplicada:

<details>
<summary><b>🔍 Clique para ver a lógica do Backend (app.py)</b></summary>




O script possui uma validação de segurança para impedir que arquivos sensíveis do sistema sejam servidos. Apenas `.xml` e `.xsl` são permitidos na rota dinâmica.

```python
@app.route('/<filename>')
def serve_xml(filename):
    # Security Check: Permite apenas XML e XSL
    if filename.endswith('.xml') or filename.endswith('.xsl'):
        return send_from_directory(XML_FOLDER, filename)
    
    # Bloqueia qualquer outra extensão
    return "Arquivo não encontrado ou tipo não permitido.", 404

```

A listagem de arquivos utiliza `os.path.getctime` para capturar a data de criação e ordenar a lista de forma decrescente:

```python
sorted_file_details = sorted(
    file_details,
    key=lambda item: item['raw_time'],
    reverse=True # Mais recentes primeiro
)

```

</details>

<details>
<summary><b>🛠 Troubleshooting (Problemas Comuns)</b></summary>

| Erro | Possível Causa | Solução |
| --- | --- | --- |
| **Erro 404 ao abrir arquivo** | Nome do arquivo incorreto ou extensão não suportada. | Verifique se o arquivo termina estritamente em `.xml` ou `.xsl`. |
| **Estilo não carrega** | Caminho no XML está errado. | Certifique-se de que a tag `<?xml-stylesheet type="text/xsl" href="estilo.xsl"?>` aponta para o arquivo correto na mesma pasta. |
| **Porta em uso** | Porta 8000 ocupada. | Edite a linha `app.run(port=8000)` no `app.py` para outra porta (ex: 8080) e atualize a configuração no Edge. |

</details>

---

<div align="center">

**Desenvolvido para facilitar a rotina de desenvolvimento e análise de dados.**





<sub>Livre para uso e modificação.</sub>

</div>


