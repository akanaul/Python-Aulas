---
sticker: "📊"
tags:
  - moc
  - modulo-04
  - bibliotecas
  - arquivos
---
# 📊 Módulo 04: Bibliotecas & Manipulação de Arquivos

> [!TUTOR] Visão Geral do Módulo 04
> Conecte seus scripts Python ao mundo real: manipule arquivos de texto, tabelas CSV, planilhas Excel com openpyxl e pandas, automatize o envio de e-mails via smtplib e agende tarefas operacionais com schedule.

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

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

## 🗺️ Mapa de Conteúdo (Dataview)

```dataview
TABLE file.folder AS "Subpasta", file.mtime AS "Última Edição"
FROM "04_bibliotecas_arquivos"
SORT file.name ASC
```

---

## 📚 Conteúdo Teórico & Referências
- [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
- [[central_avaliador_exercicios|🧪 Central de Verificação de Exercícios]]
