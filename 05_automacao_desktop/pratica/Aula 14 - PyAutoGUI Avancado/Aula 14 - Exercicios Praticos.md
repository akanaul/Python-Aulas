---
aliases: ["🧪 Exercícios Práticos — Aula 14: PyAutoGUI Avançado (Visão Computacional)"]
tags: [exercicio, pratica, issue-14, python]
---

# 🧪 Exercícios Práticos — Aula 14: PyAutoGUI Avançado (Visão Computacional)

### 📌 Do que se trata este Exercício?
Neste exercício, você tornará sua automação desktop imune a mudanças de posição de janelas através da Visão Computacional (`locateCenterOnScreen` + `OpenCV`).

**Objetivo Prático:**
1. Abra o arquivo `aula_14_exercicios_manual.py` na sua IDE.
2. Tire um recorte de imagem (`.png`) de um botão e escreva uma função de busca com tolerância `confidence=0.8` e `grayscale=True`.
3. Adicione um laço de retentativas com timeout para aguardar a imagem surgir na tela, tratando a exceção `pyautogui.ImageNotFoundException`.

Clique no botão **Run** no bloco abaixo para avaliar sua automação visual!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #14)
> 📌 **Exercício Avaliado:** Issue #14
> 📁 **Arquivo de Trabalho na IDE:** `05_automacao_desktop/pratica/Aula 14 - PyAutoGUI Avancado/aula_14_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #14...")
print("📁 Arquivo Alvo na IDE: 05_automacao_desktop/pratica/Aula 14 - PyAutoGUI Avancado/aula_14_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "14"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 05_automacao_desktop/pratica/Aula 14 - PyAutoGUI Avancado/aula_14_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-14): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-14
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
