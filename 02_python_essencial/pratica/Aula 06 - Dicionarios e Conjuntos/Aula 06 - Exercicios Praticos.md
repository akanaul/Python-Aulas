---
aliases: ["🧪 Exercícios Práticos — Aula 06: Dicionários e Conjuntos"]
tags: [exercicio, pratica, issue-06, python]
---

# 🧪 Exercícios Práticos — Aula 06: Dicionários e Conjuntos

### 📌 Do que se trata este Exercício?
Neste exercício, você utilizará a estrutura de chave-valor dos Dicionários (`dict`) e a eliminação de duplicatas de Conjuntos (`set`).

**Objetivo Prático:**
1. Abra o arquivo `aula_06_exercicios_manual.py` na sua IDE.
2. Desenvolva um cadastro de produtos usando dicionários e faça o acesso seguro a chaves usando `.get(chave, valor_padrao)` para evitar exceções `KeyError`.
3. Crie uma função que receba uma lista de tags de pesquisa com repetições e utilize `set()` para retornar apenas os termos únicos, realizando operações de intersecção (`&`) entre preferências de dois usuários.

Clique no botão **Run** para avaliar sua solução de dicionários e sets!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #06)
> 📌 **Exercício Avaliado:** Issue #06
> 📁 **Arquivo de Trabalho na IDE:** `02_python_essencial/pratica/Aula 06 - Dicionarios e Conjuntos/aula_06_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #06...")
print("📁 Arquivo Alvo na IDE: 02_python_essencial/pratica/Aula 06 - Dicionarios e Conjuntos/aula_06_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "06"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 02_python_essencial/pratica/Aula 06 - Dicionarios e Conjuntos/aula_06_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-06): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-06
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
