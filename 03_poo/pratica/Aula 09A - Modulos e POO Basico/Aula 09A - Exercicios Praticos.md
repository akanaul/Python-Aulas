---
aliases: ["🧪 Exercícios Práticos — Aula 09A: Módulos e POO Básico"]
tags: [exercicio, pratica, issue-09a, python]
---

# 🧪 Exercícios Práticos — Aula 09A: Módulos e POO Básico

### 📌 Do que se trata este Exercício?
Neste exercício, você iniciará a construção de modelos orientados a objetos em Python, compreendendo o método construtor `__init__`, o parâmetro `self` e o encapsulamento de atributos.

**Objetivo Prático:**
1. Abra o arquivo `aula_09a_exercicios_manual.py` na sua IDE.
2. Modele a classe `ContaBancaria` com os atributos `titular` e `saldo`.
3. Crie os métodos `depositar(valor)` e `sacar(valor)`, garantindo validações de saldo insuficiente antes de permitir o saque.

Clique em **Run** no bloco abaixo para avaliar sua classe de POO Básico!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #09a)
> 📌 **Exercício Avaliado:** Issue #09a
> 📁 **Arquivo de Trabalho na IDE:** `03_poo/pratica/Aula 09A - Modulos e POO Basico/aula_09a_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #09a...")
print("📁 Arquivo Alvo na IDE: 03_poo/pratica/Aula 09A - Modulos e POO Basico/aula_09a_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "09a"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 03_poo/pratica/Aula 09A - Modulos e POO Basico/aula_09a_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-09a): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-09a
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
