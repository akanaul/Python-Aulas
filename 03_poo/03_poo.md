---
sticker: "🏗️"
tags:
  - moc
  - modulo-03
  - poo
---
# 🏗️ Módulo 03: Programação Orientada a Objetos (POO)

> [!TUTOR] Visão Geral do Módulo 03
> Aprenda a estruturar sistemas modulares e reutilizáveis através da Programação Orientada a Objetos em Python, utilizando classes, atributos, métodos, composição de objetos e persistência em arquivos JSON.

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

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

## 🗺️ Mapa de Conteúdo (Dataview)

```dataview
TABLE file.folder AS "Subpasta", file.mtime AS "Última Edição"
FROM "03_poo"
SORT file.name ASC
```

---

## 📚 Conteúdo Teórico & Referências
- [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
- [[central_avaliador_exercicios|🧪 Central de Verificação de Exercícios]]
