---
sticker: "📊"
---
# 📊 Dashboard - Curso Python + IA para Automação

> [!TUTOR] Bem-vindo(a) ao seu Dashboard de Aprendizado com IA
> "A automação de tarefas cotidianas, o raciocínio fundamentado em PEPs/normas oficiais e o uso inteligente da IA são as chaves para a máxima produtividade."
> 
> 🧪 **Central de Testes:** Acesse a [[central_avaliador_exercicios|🧪 Central de Verificação de Exercícios]] para avaliar seus arquivos `.py` da IDE em 1-clique.
> 📘 **Guia do Aluno:** Consulte o [[MANUAL_DO_ALUNO|📘 Manual Oficial do Aluno]] para entender o ciclo de aprendizado em 4 passos.
> 📚 **Referências de Apoio:**
> - [[00_hub_mapeamento_issues|🗺️ Hub Central de Mapeamento 1-para-1 de Issues & Artefatos]]
> - [[MANUAL_DO_ALUNO|📘 Manual Oficial do Aluno]]
> - [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
> - [[central_avaliador_exercicios|Central de Avaliação de Exercícios]]

> [!CAUTION] 🚨 Botão de Pânico / Auto-Recuperação do Obsidian em 1 Segundo
> **Os plugins parecem desativados ou o Obsidian entrou em Modo Restrito?**
> Execute o bloco abaixo ou rode `python setup_vault.py` no terminal:
> > [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #all)
> 📌 **Exercício Avaliado:** Issue #all — Suíte Geral de Testes do Vault
> 📁 **Arquivo de Trabalho na IDE:** `avaliar_exercicio.py --all`
> ⚡ Clique no botão **Run** no canto superior direito do bloco abaixo para testar sua solução:

```python run
import sys, os, subprocess

def find_vault_root():
    curr = os.path.abspath(os.getcwd())
    while curr:
        if os.path.exists(os.path.join(curr, "avaliar_exercicio.py")):
            return curr
        parent = os.path.dirname(curr)
        if parent == curr:
            break
        curr = parent
    user_home = os.path.expanduser("~")
    for root, dirs, files in os.walk(user_home):
        if "avaliar_exercicio.py" in files:
            return root
        if root.count(os.sep) - user_home.count(os.sep) >= 4:
            dirs.clear()
    return os.path.abspath(".")

vault_root = find_vault_root()
script_path = os.path.join(vault_root, "avaliar_exercicio.py")
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #all...")
print("📁 Arquivo Alvo na IDE: avaliar_exercicio.py --all")
res = subprocess.run([sys.executable, script_path, "--issue", "all"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

### 🧪 Testar Todos os Módulos do Repositório
> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #all)
> 📌 **Exercício Avaliado:** Issue #all — Suíte Geral de Testes do Vault
> 📁 **Arquivo de Trabalho na IDE:** `avaliar_exercicio.py --all`
> ⚡ Clique no botão **Run** no canto superior direito do bloco abaixo para testar sua solução:

```python run
import sys, os, subprocess

def find_vault_root():
    curr = os.path.abspath(os.getcwd())
    while curr:
        if os.path.exists(os.path.join(curr, "avaliar_exercicio.py")):
            return curr
        parent = os.path.dirname(curr)
        if parent == curr:
            break
        curr = parent
    user_home = os.path.expanduser("~")
    for root, dirs, files in os.walk(user_home):
        if "avaliar_exercicio.py" in files:
            return root
        if root.count(os.sep) - user_home.count(os.sep) >= 4:
            dirs.clear()
    return os.path.abspath(".")

vault_root = find_vault_root()
script_path = os.path.join(vault_root, "avaliar_exercicio.py")
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #all...")
print("📁 Arquivo Alvo na IDE: avaliar_exercicio.py --all")
res = subprocess.run([sys.executable, script_path, "--issue", "all"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 📌 Painéis Dinâmicos do Caderno do Aluno (Dataview)

### 🏆 Progresso Automático de Exercícios Concluídos (`meu_caderno_aluno/progresso`)
```dataview
TABLE created AS "Data de Conclusão", issue AS "Issue / Exercício", status AS "Status"
FROM "meu_caderno_aluno/progresso"
SORT created DESC
```

### ❓ Minhas Dúvidas Registradas pelo Agente (`meu_caderno_aluno/duvidas`)
```dataview
TABLE created AS "Data", status AS "Status", modulo AS "Módulo"
FROM "meu_caderno_aluno/duvidas"
SORT created DESC
```

### 🚑 Diagnósticos de Erros & Issues (`meu_caderno_aluno/diagnostico_erros`)
```dataview
TABLE created AS "Data", issue AS "Issue", status AS "Status"
FROM "meu_caderno_aluno/diagnostico_erros"
SORT created DESC
```

### 🎴 Flashcards de Revisão Espaçada (Spaced Repetition)
```dataview
LIST FROM #flashcard
SORT file.name ASC
LIMIT 10
```

---

## 🔰 Guia Visual dos 21 Plugins Ativos no Vault

| Plugin                    | O que faz no vault?                                                    | Como o aluno usa?                                                                          |     |
| :------------------------ | :--------------------------------------------------------------------- | :----------------------------------------------------------------------------------------- | --- |
| 🪟 **Hover Editor**       | Pré-visualização e edição flutuante ao passar o mouse sobre links.     | Passe o mouse sobre qualquer link `[[aula]]` para abrir a janela flutuante editável.       |     |
| 📊 **Data Files Editor**  | Editor visual de tabelas para arquivos CSV, JSON e YAML.               | Clique em arquivos `.csv` ou `.json` em `_dados_exemplo/` para ver e editar como planilha. |     |
| ⚡ **Execute Code**        | Executa blocos de código Python e comandos diretamente dentro da nota. | Clique no botão **Run** acima do bloco de código ` ```python run `.                        |     |
| 📁 **Make.md**            | Transforma pastas em notas de capa com stickers.                       | Clique em qualquer pasta (ex: `01_fundamentos`) para abrir a nota de capa.                 |     |
| 📊 **Dataview**           | Painéis dinâmicos e consultas automáticas.                             | Exibe automaticamente seu progresso nas tabelas deste Dashboard.                           |     |
| 📋 **Kanban**             | Quadro de tarefas estilo Trello.                                       | Acesse [[plano_de_estudos]] para arrastar suas tarefas.                                    |     |
| 📇 **Spaced Repetition**  | Cartões de memória e repetição espaçada.                               | Acesse a barra lateral do Obsidian ou pressione `Ctrl+P` -> *Spaced Repetition*.           |     |
| 📝 **Templater**          | Modelos padronizados com inserção dinâmica de metadados.               | Crie novas notas usando os modelos da pasta `_templates/`.                                 |     |
| 🎨 **Code Styler**        | Realce de sintaxe de código Python.                                    | Blocos de código ` ```python ` ficam coloridos e com numeração de linhas.                  |     |
| ⚡ **Various Complements** | Autocompletar inteligente enquanto digita.                             | Digite `python` ou `[!TUTOR]` e pressione `Tab` para autocompletar.                        |     |

---

## ⌨️ Atalhos de Teclado Essenciais (Cheat Sheet)

- `Ctrl + P` (ou `Cmd + P` no Mac): **Paleta de Comandos** (Busca rápida de qualquer ação do Obsidian).
- `Ctrl + O` (ou `Cmd + O` no Mac): **Abrir Arquivo Rápido** (Digite o nome de qualquer aula).
- `Ctrl + E`: Alternar entre **Modo Edição** e **Modo Leitura**.
- `Alt + N` / `Alt + E`: Criar nova nota com o **Template do Curso** via Templater.
