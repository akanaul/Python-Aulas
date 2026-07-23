---
aliases: ["🧪 Exercícios Práticos — Aula 02: Variáveis e Operadores"]
tags: [exercicio, pratica, issue-02, python]
---

# 🧪 Exercícios Práticos — Aula 02: Variáveis e Operadores

### 📌 Do que se trata este Exercício?
Neste exercício, você aplicará o uso de variáveis, tipos numéricos (`int`, `float`), conversão defensiva e operadores matemáticos/lógicos.

**Objetivo Prático:**
1. Abra o arquivo `aula_02_exercicios_manual.py` na sua IDE.
2. Desenvolva uma calculadora de custo de frete rodoviário que receba a distância em km e o consumo do veículo, calculando o custo total do combustível.
3. Converta tipos de dados com conversão defensiva `try / except ValueError` para evitar travamentos caso o usuário digite texto em vez de números.

Clique em **Run** no bloco abaixo para avaliar sua calculadora de frete!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #02)
> 📌 **Exercício Avaliado:** Issue #02
> 📁 **Arquivo de Trabalho na IDE:** `01_fundamentos/pratica/Aula 02 - Variaveis e Operadores/aula_02_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #02...")
print("📁 Arquivo Alvo na IDE: 01_fundamentos/pratica/Aula 02 - Variaveis e Operadores/aula_02_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "02"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 01_fundamentos/pratica/Aula 02 - Variaveis e Operadores/aula_02_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-02): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-02
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
