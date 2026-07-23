# 📋 Plano de Estudos, Kanban e Tarefas

---
kanban-plugin: basic
---

## 📋 A Fazer
- [ ] [[01 - Fundamentos/Aula 00 - Mindset Vibe Coding Etico/Aula 00 - Mindset Vibe Coding Etico e Copilotos|Aula 00 — Mindset Vibe Coding Ético & Copilotos]] #aula
- [ ] [[01 - Fundamentos/Aula 01 - Setup e Primeiros Passos/Aula 1 - Setup Completo e Primeiros Passos|Aula 1 — Setup Completo e Primeiros Passos]] #aula
- [ ] [[01 - Fundamentos/Aula 02 - Variaveis e Operadores/Aula 2 - Variáveis e Operadores|Aula 2 — Variáveis e Operadores]] #aula
- [ ] [[01 - Fundamentos/Aula 03 - Condicionais e Loops/Aula 3 - Condicionais e Loops|Aula 3 — Condicionais e Loops]] #aula
- [ ] [[02 - Python Essencial/Aula 04 - Strings e Formatacao/Aula 4 - Strings e Formatação|Aula 4 — Strings e Formatação]] #aula
- [ ] [[02 - Python Essencial/Aula 05 - Listas Tuplas e Ranges/Aula 5 - Listas Tuplas e Ranges|Aula 5 — Listas, Tuplas e Ranges]] #aula
- [ ] [[02 - Python Essencial/Aula 06 - Dicionarios e Conjuntos/Aula 6 - Dicionarios e Conjuntos|Aula 6 — Dicionários e Conjuntos]] #aula
- [ ] [[02 - Python Essencial/Aula 07 - Funcoes/Aula 7 - Funções|Aula 7 — Funções]] #aula
- [ ] [[07 - Bonus Selenium/Aula Bonus - Selenium A Proxima Fronteira/Aula Bonus - Selenium A Proxima Fronteira|Aula Bônus — Selenium & DevTools MCP]] #aula #exercicio #issue-07

## ⚡ Em Andamento (Branch Git)

## 🧪 Em Testes (avaliar_exercicio)

## ✅ Concluído (Merge Main)

---

## 📅 Visão Geral de Tarefas Pendentes (Dataview Tasks)

```dataview
TASK
WHERE !completed
SORT file.name ASC
```


---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #all)
> 📌 **Exercício Avaliado:** Issue #all — Suíte Geral de Testes do Vault
> 📁 **Arquivo de Trabalho na IDE:** `avaliar_exercicio.py --all`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #all...")
print("📁 Arquivo Alvo na IDE: avaliar_exercicio.py --all")
res = subprocess.run([sys.executable, script_path, "--issue", "all"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```
