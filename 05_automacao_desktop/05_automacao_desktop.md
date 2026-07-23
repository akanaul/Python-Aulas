---
sticker: "🖥️"
tags:
  - moc
  - modulo-05
  - automacao-desktop
  - rpa
---
# 🖥️ Módulo 05: Automação Desktop (RPA & Visão Computacional)

> [!TUTOR] Visão Geral do Módulo 05
> Automatize a interação com aplicativos desktop e sistemas legados simulando ações humanas com PyAutoGUI: controle de mouse, teclado, área de transferência com pyperclip, travão de emergência (FAILSAFE) e visão computacional com OpenCV (locateCenterOnScreen).

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

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

## 🗺️ Mapa de Conteúdo (Dataview)

```dataview
TABLE file.folder AS "Subpasta", file.mtime AS "Última Edição"
FROM "05_automacao_desktop"
SORT file.name ASC
```

---

## 📚 Conteúdo Teórico & Referências
- [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
- [[central_avaliador_exercicios|🧪 Central de Verificação de Exercícios]]
