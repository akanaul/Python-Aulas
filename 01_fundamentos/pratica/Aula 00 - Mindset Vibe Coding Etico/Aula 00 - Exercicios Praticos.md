---
aliases: ["🧪 Exercícios Práticos — Aula 00: Mindset Vibe Coding Ético e Copilotos"]
tags: [exercicio, pratica, issue-00, python]
---

# 🧪 Exercícios Práticos — Aula 00: Mindset Vibe Coding Ético e Copilotos

### 📌 Do que se trata este Exercício?
Neste primeiro exercício prático, você aplicará o **Mindset do Vibe Coding Ético**. Como desenvolvedor, seu papel não é aceitar cegamente as sugestões da Inteligência Artificial, mas sim atuar como **Chef de Cozinha (ou Piloto)** auditando o trabalho do **Sous-Chef (IA)**.

**Objetivo Prático:**
1. Abra o arquivo `aula_00_exercicios_manual.py` na sua IDE (Cursor / VS Code).
2. Implemente a função de cálculo de comissão de vendas, corrigindo exceções de divisão por zero (`ZeroDivisionError`) através de estruturas defensivas `try / except / else / finally`.
3. Garanta que a função retorne o percentual correto arredondado com 2 casas decimais.

Após implementar na IDE, clique no botão **Run** no bloco 1-Clique abaixo para testar sua solução!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #00)
> 📌 **Exercício Avaliado:** Issue #00
> 📁 **Arquivo de Trabalho na IDE:** `01_fundamentos/pratica/Aula 00 - Mindset Vibe Coding Etico/aula_00_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #00...")
print("📁 Arquivo Alvo na IDE: 01_fundamentos/pratica/Aula 00 - Mindset Vibe Coding Etico/aula_00_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "00"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 01_fundamentos/pratica/Aula 00 - Mindset Vibe Coding Etico/aula_00_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-00): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-00
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
