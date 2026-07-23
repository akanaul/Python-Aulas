---
aliases: ["🧪 Exercícios Práticos — Aula 13: PyAutoGUI Básico (RPA Desktop)"]
tags: [exercicio, pratica, issue-13, python]
---

# 🧪 Exercícios Práticos — Aula 13: PyAutoGUI Básico (RPA Desktop)

### 📌 Do que se trata este Exercício?
Neste exercício, você iniciará a automação de processos robóticos (RPA) para sistemas desktop simulando ações de mouse, teclado e clipboard.

**Objetivo Prático:**
1. Abra o arquivo `aula_13_exercicios_manual.py` na sua IDE.
2. Configure obrigatoriamente os parâmetros de segurança `pyautogui.FAILSAFE = True` e `pyautogui.PAUSE = 0.5`.
3. Escreva um fluxo que mova o cursor para coordenadas específicas da tela, clique em campos de texto e utilize `pyperclip` para colar textos com acentuação em português (`Ctrl+V`).

Clique no botão **Run** abaixo para testar sua automação desktop básica!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #13)
> 📌 **Exercício Avaliado:** Issue #13
> 📁 **Arquivo de Trabalho na IDE:** `05_automacao_desktop/pratica/Aula 13 - PyAutoGUI Basico/aula_13_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #13...")
print("📁 Arquivo Alvo na IDE: 05_automacao_desktop/pratica/Aula 13 - PyAutoGUI Basico/aula_13_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "13"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 05_automacao_desktop/pratica/Aula 13 - PyAutoGUI Basico/aula_13_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-13): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-13
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
