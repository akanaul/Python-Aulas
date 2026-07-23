---
aliases: ["🧪 Exercícios Práticos — Aula 04: Strings e Formatação"]
tags: [exercicio, pratica, issue-04, python]
---

# 🧪 Exercícios Práticos — Aula 04: Strings e Formatação

### 📌 Do que se trata este Exercício?
Neste exercício, você dominará métodos de manipulação de texto (`str`), fatiamento (`[início:fim:passo]`) e formatação tabular com f-strings.

**Objetivo Prático:**
1. Abra o arquivo `aula_04_exercicios_manual.py` na sua IDE.
2. Crie uma função sanitizadora que receba um cadastro de cliente com espaços extras, converta o nome para maiúsculas (`upper`), remova caracteres especiais de CPFs e aplique máscara de formatação `XXX.XXX.XXX-XX`.
3. Formate a saída de dados em uma tabela legível usando especificadores como `<20` e `>10`.

Clique em **Run** no bloco abaixo para testar o sanitizador de strings!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #04)
> 📌 **Exercício Avaliado:** Issue #04
> 📁 **Arquivo de Trabalho na IDE:** `02_python_essencial/pratica/Aula 04 - Strings e Formatacao/aula_04_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #04...")
print("📁 Arquivo Alvo na IDE: 02_python_essencial/pratica/Aula 04 - Strings e Formatacao/aula_04_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "04"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 02_python_essencial/pratica/Aula 04 - Strings e Formatacao/aula_04_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-04): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-04
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
