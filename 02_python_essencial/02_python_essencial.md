---
sticker: "⚡"
tags:
  - moc
  - modulo-02
  - python-essencial
---
# 🐍 Módulo 02: Python Essencial

> [!TUTOR] Visão Geral do Módulo 02
> Domine as estruturas de dados fundamentais do Python (Strings, Listas, Tuplas, Dicionários, Conjuntos) e crie funções reutilizáveis e limpas fundamentadas no **PEP 484 (Type Hints)**.
> 
> 📚 **Fundamentação Acadêmica:** Consulte a **[PEP 484 — Type Hints](https://peps.python.org/pep-0484/)** e a **[PEP 257 — Docstrings](https://peps.python.org/pep-0257/)**.

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #04)
> 📌 **Exercício Avaliado:** Issue #04 — Strings e Formatação
> 📁 **Arquivo de Trabalho na IDE:** `02_python_essencial/pratica/Aula 04 - Strings e Formatacao/aula_04_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #04...")
print("📁 Arquivo Alvo na IDE: 02_python_essencial/pratica/Aula 04 - Strings e Formatacao/aula_04_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "04"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #05)
> 📌 **Exercício Avaliado:** Issue #05 — Listas, Tuplas e Ranges
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

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #06)
> 📌 **Exercício Avaliado:** Issue #06 — Dicionários e Conjuntos
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

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #07)
> 📌 **Exercício Avaliado:** Issue #07 — Funções, Decoradores e Geradores
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

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #08)
> 📌 **Exercício Avaliado:** Issue #08 — Vibe Coding e Engenharia de Prompt
> 📁 **Arquivo de Trabalho na IDE:** `02_python_essencial/pratica/Aula 08 - Vibe Coding e Engenharia de Prompt/aula_08_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #08...")
print("📁 Arquivo Alvo na IDE: 02_python_essencial/pratica/Aula 08 - Vibe Coding e Engenharia de Prompt/aula_08_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "08"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #projeto2)
> 📌 **Exercício Avaliado:** Issue #projeto2 — Mini-Projeto 2: Analisador de Rotas
> 📁 **Arquivo de Trabalho na IDE:** `02_python_essencial/pratica/Mini-Projeto 2 - Analisador de Rotas/projeto_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #projeto2...")
print("📁 Arquivo Alvo na IDE: 02_python_essencial/pratica/Mini-Projeto 2 - Analisador de Rotas/projeto_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "projeto2"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🗺️ Mapa de Conteúdo (Dataview)

```dataview
TABLE file.folder AS "Subpasta", file.mtime AS "Última Edição"
FROM "02_python_essencial"
SORT file.name ASC
```

---

## 📚 Conteúdo Teórico & Referências
- [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
- [[central_avaliador_exercicios|🧪 Central de Verificação de Exercícios]]
