---
aliases: ["🧪 Exercícios Práticos — Aula 15: Prompt Engineering Avançado"]
tags: [exercicio, pratica, issue-15, python]
---

# 🧪 Exercícios Práticos — Aula 15: Prompt Engineering Avançado

### 📌 Do que se trata este Exercício?
Neste exercício, você aplicará técnicas avançadas de Engenharia de Prompt: **Few-Shot Prompting**, **Chain of Thought (CoT)** e **Prompt Chaining**.

**Objetivo Prático:**
1. Abra o arquivo `aula_15_exercicios_manual.py` na sua IDE.
2. Crie um template de prompt Few-Shot com exemplos visuais de entrada/saída solicitando retornos em JSON estrito.
3. Desenvolva uma função defensiva em Python que extraia o JSON da resposta da IA tratando erros de `json.JSONDecodeError` e marcadores de código markdown.

Clique no botão **Run** abaixo para testar seus prompts avançados!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #15)
> 📌 **Exercício Avaliado:** Issue #15
> 📁 **Arquivo de Trabalho na IDE:** `06_ia_prompt/pratica/Aula 15 - Prompt Engineering Avancado/aula_15_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #15...")
print("📁 Arquivo Alvo na IDE: 06_ia_prompt/pratica/Aula 15 - Prompt Engineering Avancado/aula_15_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "15"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 06_ia_prompt/pratica/Aula 15 - Prompt Engineering Avancado/aula_15_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-15): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-15
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
