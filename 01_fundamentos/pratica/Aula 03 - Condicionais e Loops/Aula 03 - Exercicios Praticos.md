---
aliases: ["🧪 Exercícios Práticos — Aula 03: Condicionais e Loops"]
tags: [exercicio, pratica, issue-03, python]
---

# 🧪 Exercícios Práticos — Aula 03: Condicionais e Loops

### 📌 Do que se trata este Exercício?
Neste exercício, você praticará o controle de fluxo com estruturas condicionais (`if/elif/else`), avaliação curto-circuito (`and`/`or`) e laços de repetição (`while/for`).

**Objetivo Prático:**
1. Abra o arquivo `aula_03_exercicios_manual.py` na sua IDE.
2. Crie um sistema de aprovação de crédito de frotas de transporte que valida a idade do motorista (>= 21 anos), pontuação da CNH (< 20 pontos) e saldo disponível em conta.
3. Adicione um laço `while` que permita até 3 retentativas de digitação em caso de dados inválidos.

Clique no botão **Run** abaixo para testar sua lógica de aprovação!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #03)
> 📌 **Exercício Avaliado:** Issue #03
> 📁 **Arquivo de Trabalho na IDE:** `01_fundamentos/pratica/Aula 03 - Condicionais e Loops/aula_03_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #03...")
print("📁 Arquivo Alvo na IDE: 01_fundamentos/pratica/Aula 03 - Condicionais e Loops/aula_03_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "03"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 01_fundamentos/pratica/Aula 03 - Condicionais e Loops/aula_03_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-03): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-03
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
