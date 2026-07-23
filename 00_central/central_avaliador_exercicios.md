---
sticker: "🧪"
tags:
  - central
  - avaliador
  - exercicios
---
# 🧪 Central de Verificação de Exercícios & Gatekeeper Git

> [!TUTOR] Hub Interativo de Testes & Execução dos Arquivos da IDE
> Bem-vindo(a) à **Central de Verificação de Exercícios**!
> Como você desenvolve seus scripts `.py` completos na IDE (Cursor / VS Code), este painel permite **executar os arquivos da IDE** e **rodar os avaliadores automatizados** com apenas **1 clique** diretamente dentro do Obsidian.

---

## ⚡ 1. Avaliador Automatizado 1-Clique por Módulo / Issue

Clique no botão **Run** no canto superior direito do bloco referente ao exercício em que você está trabalhando:

### 🟢 Módulo 01: Fundamentos (Lógica, Operadores & Condicionais)

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

### 🔵 Módulo 02: Python Essencial (Estruturas de Dados & Funções)

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

### 🟣 Módulo 03: POO (Programação Orientada a Objetos)

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #09a)
> 📌 **Exercício Avaliado:** Issue #09a — Módulos e POO Básico
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

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #09b)
> 📌 **Exercício Avaliado:** Issue #09b — POO Prático Composição e Persistência
> 📁 **Arquivo de Trabalho na IDE:** `03_poo/pratica/Aula 09B - POO Pratico Composicao e Persistencia/aula_09b_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #09b...")
print("📁 Arquivo Alvo na IDE: 03_poo/pratica/Aula 09B - POO Pratico Composicao e Persistencia/aula_09b_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "09b"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #projeto1_5)
> 📌 **Exercício Avaliado:** Issue #projeto1_5 — Mini-Projeto 1.5: Cadastrador de Motoristas POO
> 📁 **Arquivo de Trabalho na IDE:** `03_poo/pratica/Mini-Projeto 1.5 - Sistema de Cadastro de Motoristas/projeto_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #projeto1_5...")
print("📁 Arquivo Alvo na IDE: 03_poo/pratica/Mini-Projeto 1.5 - Sistema de Cadastro de Motoristas/projeto_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "projeto1_5"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

### 🟡 Módulo 04: Bibliotecas & Arquivos (Excel, CSV & Pathlib)

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #10)
> 📌 **Exercício Avaliado:** Issue #10 — Arquivos TXT e CSV
> 📁 **Arquivo de Trabalho na IDE:** `04_bibliotecas_arquivos/pratica/Aula 10 - Arquivos txt e csv/aula_10_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #10...")
print("📁 Arquivo Alvo na IDE: 04_bibliotecas_arquivos/pratica/Aula 10 - Arquivos txt e csv/aula_10_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "10"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #11)
> 📌 **Exercício Avaliado:** Issue #11 — Excel com openpyxl e pandas
> 📁 **Arquivo de Trabalho na IDE:** `04_bibliotecas_arquivos/pratica/Aula 11 - Excel com openpyxl e pandas/aula_11_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #11...")
print("📁 Arquivo Alvo na IDE: 04_bibliotecas_arquivos/pratica/Aula 11 - Excel com openpyxl e pandas/aula_11_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "11"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #12)
> 📌 **Exercício Avaliado:** Issue #12 — Email Automático e Agendamento
> 📁 **Arquivo de Trabalho na IDE:** `04_bibliotecas_arquivos/pratica/Aula 12 - Email Automatico e Agendamento/aula_12_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #12...")
print("📁 Arquivo Alvo na IDE: 04_bibliotecas_arquivos/pratica/Aula 12 - Email Automatico e Agendamento/aula_12_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "12"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #projeto3)
> 📌 **Exercício Avaliado:** Issue #projeto3 — Mini-Projeto 3: Relatório KPI de Entregas
> 📁 **Arquivo de Trabalho na IDE:** `04_bibliotecas_arquivos/pratica/Mini-Projeto 3 - Relatorio KPI de Entregas/projeto_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #projeto3...")
print("📁 Arquivo Alvo na IDE: 04_bibliotecas_arquivos/pratica/Mini-Projeto 3 - Relatorio KPI de Entregas/projeto_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "projeto3"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

### 🟧 Módulo 05: Automação Desktop (PyAutoGUI & Failsafe)

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #13)
> 📌 **Exercício Avaliado:** Issue #13 — PyAutoGUI Básico
> 📁 **Arquivo de Trabalho na IDE:** `05_automacao_desktop/pratica/Aula 13 - PyAutoGUI Basico/aula_13_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #13...")
print("📁 Arquivo Alvo na IDE: 05_automacao_desktop/pratica/Aula 13 - PyAutoGUI Basico/aula_13_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "13"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #14)
> 📌 **Exercício Avaliado:** Issue #14 — PyAutoGUI Avançado
> 📁 **Arquivo de Trabalho na IDE:** `05_automacao_desktop/pratica/Aula 14 - PyAutoGUI Avancado/aula_14_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #14...")
print("📁 Arquivo Alvo na IDE: 05_automacao_desktop/pratica/Aula 14 - PyAutoGUI Avancado/aula_14_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "14"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

### 🔴 Módulo 06: IA, Prompt Engineering & Auditoria

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #15)
> 📌 **Exercício Avaliado:** Issue #15 — Prompt Engineering Avançado
> 📁 **Arquivo de Trabalho na IDE:** `06_ia_prompt/pratica/Aula 15 - Prompt Engineering Avancado/aula_15_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #15...")
print("📁 Arquivo Alvo na IDE: 06_ia_prompt/pratica/Aula 15 - Prompt Engineering Avancado/aula_15_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "15"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #16)
> 📌 **Exercício Avaliado:** Issue #16 — Revisão Geral e Próximos Passos
> 📁 **Arquivo de Trabalho na IDE:** `06_ia_prompt/pratica/Aula 16 - Revisao Geral e Proximos Passos/aula_16_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #16...")
print("📁 Arquivo Alvo na IDE: 06_ia_prompt/pratica/Aula 16 - Revisao Geral e Proximos Passos/aula_16_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "16"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

### 🌐 Módulo 07: Automação Web Dual (Selenium & Chrome DevTools MCP)

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #devtools)
> 📌 **Exercício Avaliado:** Issue #devtools — Automação Web Dual (Selenium & Chrome DevTools MCP)
> 📁 **Arquivo de Trabalho na IDE:** `07_bonus_selenium/pratica/Aula Bonus - Selenium A Proxima Fronteira/devtools_mcp_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #devtools...")
print("📁 Arquivo Alvo na IDE: 07_bonus_selenium/pratica/Aula Bonus - Selenium A Proxima Fronteira/devtools_mcp_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "devtools"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

### 🏆 Avaliar Suíte Completa do Repositório (Todos os Módulos)

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

---

## 📌 Painéis Dinâmicos do Caderno do Aluno (Dataview)

### 🏆 Progresso Automático de Exercícios Concluídos (`meu_caderno_aluno/progresso`)
```dataview
TABLE created AS "Data de Conclusão", issue AS "Issue / Exercício", status AS "Status"
FROM "meu_caderno_aluno/progresso"
SORT created DESC
```

### 🚑 Diagnósticos de Erros & Issues (`meu_caderno_aluno/diagnostico_erros`)
```dataview
TABLE created AS "Data do Registro", issue AS "Issue", status AS "Status"
FROM "meu_caderno_aluno/diagnostico_erros"
SORT created DESC
```

---

## 📚 Referências de Apoio
- [[hub_mapeamento_issues|🗺️ Hub Central de Mapeamento 1-para-1 de Issues & Artefatos]]
- [[00 - Dashboard|Dashboard Principal]]
- [[MANUAL_DO_ALUNO|📘 Manual Oficial do Aluno]]
- [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
