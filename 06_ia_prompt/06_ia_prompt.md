---
sticker: "🤖"
tags:
  - moc
  - modulo-06
  - ia
  - prompt-engineering
---
# 🤖 Módulo 06: Inteligência Artificial & Engenharia de Prompt Avançada

> [!TUTOR] Visão Geral do Módulo 06
> Eleve seu nível como desenvolvedor Vibe Coding: domine as técnicas de Few-Shot Prompting, Chain of Thought (CoT), encadeamento de sub-prompts, debugging guiado por IA e arquiteturas de automação resilientes.

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

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

## 🗺️ Mapa de Conteúdo (Dataview)

```dataview
TABLE file.folder AS "Subpasta", file.mtime AS "Última Edição"
FROM "06_ia_prompt"
SORT file.name ASC
```

---

## 📚 Conteúdo Teórico & Referências
- [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
- [[central_avaliador_exercicios|🧪 Central de Verificação de Exercícios]]
