---
aliases: ["🧪 Exercícios Práticos — Aula 07: Funções, Decoradores e Geradores"]
tags: [exercicio, pratica, issue-07, python]
---

# 🧪 Exercícios Práticos — Aula 07: Funções, Decoradores e Geradores

### 📌 Do que se trata este Exercício?
Neste exercício, você aperfeiçoará a modularização de código com funções (`def`), parâmetros opcionais, decoradores (`@wraps`) e geradores (`yield`).

**Objetivo Prático:**
1. Abra o arquivo `aula_07_exercicios_manual.py` na sua IDE.
2. Escreva uma função de cálculo financeiro com argumentos padrão e crie um decorador personalizado `@cronometrar` para medir o tempo de execução de scripts.
3. Desenvolva uma função geradora com `yield` para transmitir notificações em streaming, economizando uso de memória RAM.

Clique em **Run** no bloco abaixo para testar suas funções, decoradores e geradores!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #07)
> 📌 **Exercício Avaliado:** Issue #07
> 📁 **Arquivo de Trabalho na IDE:** `02_python_essencial/pratica/Aula 07 - Funcoes/aula_07_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #07...")
print("📁 Arquivo Alvo na IDE: 02_python_essencial/pratica/Aula 07 - Funcoes/aula_07_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "07"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 02_python_essencial/pratica/Aula 07 - Funcoes/aula_07_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-07): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-07
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
