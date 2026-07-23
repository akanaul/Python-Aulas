---
aliases: ["🧪 Exercícios Práticos — Aula 05: Listas, Tuplas e Ranges"]
tags: [exercicio, pratica, issue-05, python]
---

# 🧪 Exercícios Práticos — Aula 05: Listas, Tuplas e Ranges

### 📌 Do que se trata este Exercício?
Neste exercício, você explorará a mutabilidade de Listas, a segurança e imutabilidade de Tuplas e a eficiência de memória dos `ranges`.

**Objetivo Prático:**
1. Abra o arquivo `aula_05_exercicios_manual.py` na sua IDE.
2. Implemente um gerenciador de fila de entregas onde novas tarefas são adicionadas com `.append()`, ordenadas em ordem alfabética com `.sort()` e removidas com `.pop()`.
3. Registre o histórico de entregas concluídas usando **tuplas imutáveis** `(id_entrega, cliente, status)` para impedir alterações acidentais.

Clique em **Run** abaixo para testar seu gerenciador de fila e tuplas!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #05)
> 📌 **Exercício Avaliado:** Issue #05
> 📁 **Arquivo de Trabalho na IDE:** `02_python_essencial/pratica/Aula 05 - Listas Tuplas e Ranges/aula_05_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #05...")
print("📁 Arquivo Alvo na IDE: 02_python_essencial/pratica/Aula 05 - Listas Tuplas e Ranges/aula_05_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "05"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 02_python_essencial/pratica/Aula 05 - Listas Tuplas e Ranges/aula_05_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-05): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-05
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
