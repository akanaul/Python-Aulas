---
sticker: "🌱"
tags:
  - moc
  - modulo-01
  - fundamentos
---
# 🧩 Módulo 01: Fundamentos de Python

> [!TUTOR] Visão Geral do Módulo 01
> Neste módulo inicial, você dominará os pilares da programação em Python: variáveis, tipos de dados, operadores matemáticos/lógicos, estruturas condicionais (`if/elif/else`) e laços de repetição (`while/for`).
> 
> 📚 **Fundamentação Acadêmica:** Consulte [[00_hub_referencias_academicas|Hub de Referências Acadêmicas]] e a **[PEP 8](https://peps.python.org/pep-0008/)** para regras de legibilidade.

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #00)
> 📌 **Exercício Avaliado:** Issue #00 — Mindset Vibe Coding Ético e Copilotos
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

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #01)
> 📌 **Exercício Avaliado:** Issue #01 — Setup Completo e Primeiros Passos
> 📁 **Arquivo de Trabalho na IDE:** `01_fundamentos/pratica/Aula 01 - Setup e Primeiros Passos/aula_01_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #01...")
print("📁 Arquivo Alvo na IDE: 01_fundamentos/pratica/Aula 01 - Setup e Primeiros Passos/aula_01_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "01"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #02)
> 📌 **Exercício Avaliado:** Issue #02 — Variáveis e Operadores
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

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #03)
> 📌 **Exercício Avaliado:** Issue #03 — Condicionais e Loops
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

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #projeto1)
> 📌 **Exercício Avaliado:** Issue #projeto1 — Mini-Projeto 1: Gerador de Ficha de Motorista
> 📁 **Arquivo de Trabalho na IDE:** `01_fundamentos/pratica/Mini-Projeto 1 - Gerador de Ficha de Motorista/projeto_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #projeto1...")
print("📁 Arquivo Alvo na IDE: 01_fundamentos/pratica/Mini-Projeto 1 - Gerador de Ficha de Motorista/projeto_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "projeto1"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🗺️ Mapa de Conteúdo (Dataview)

```dataview
TABLE file.folder AS "Subpasta", file.mtime AS "Última Edição"
FROM "01_fundamentos"
SORT file.name ASC
```

---

## 📚 Conteúdo Teórico & Referências
- [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
- [[central_avaliador_exercicios|🧪 Central de Verificação de Exercícios]]
