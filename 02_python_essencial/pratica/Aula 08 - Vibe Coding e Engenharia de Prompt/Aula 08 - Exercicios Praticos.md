---
aliases: ["🧪 Exercícios Práticos — Aula 08: Vibe Coding e Engenharia de Prompt"]
tags: [exercicio, pratica, issue-08, python]
---

# 🧪 Exercícios Práticos — Aula 08: Vibe Coding e Engenharia de Prompt

### 📌 Do que se trata este Exercício?
Neste exercício, você aplicará a metodologia de Engenharia de Prompt **C-T-R-F (Contexto, Tarefa, Restrição, Formato)** para solicitar e refatorar código com auxílio da IA.

**Objetivo Prático:**
1. Abra o arquivo `aula_08_exercicios_manual.py` na sua IDE.
2. Construa um prompt estruturado C-T-R-F solicitando uma função de filtragem de compras que remova duplicados mantendo a ordem original.
3. Audite o código retornado pela IA, verifique se ele respeita a restrição de usar apenas a biblioteca padrão do Python e adicione tratamento defensivo contra erros de entrada.

Clique em **Run** no bloco abaixo para avaliar seu exercício de Vibe Coding!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #08)
> 📌 **Exercício Avaliado:** Issue #08
> 📁 **Arquivo de Trabalho na IDE:** `02_python_essencial/pratica/Aula 08 - Vibe Coding e Engenharia de Prompt/aula_08_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #08...")
print("📁 Arquivo Alvo na IDE: 02_python_essencial/pratica/Aula 08 - Vibe Coding e Engenharia de Prompt/aula_08_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "08"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 02_python_essencial/pratica/Aula 08 - Vibe Coding e Engenharia de Prompt/aula_08_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-08): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-08
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
