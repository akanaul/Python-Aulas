---
sticker: "🌐"
tags:
  - moc
  - modulo-07
  - selenium
  - devtools-mcp
---
# 🌐 Módulo 07 (Bônus): Automação Web Dual (Selenium 4 & Chrome DevTools MCP)

> [!TUTOR] Visão Geral do Módulo Bônus
> Domine a automação web profissional: raspagem de dados, interação com formulários web em modo headless com Selenium 4 e inspeção inteligente de páginas com Chrome DevTools MCP.

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

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

## 🗺️ Mapa de Conteúdo (Dataview)

```dataview
TABLE file.folder AS "Subpasta", file.mtime AS "Última Edição"
FROM "07_bonus_selenium"
SORT file.name ASC
```

---

## 📚 Conteúdo Teórico & Referências
- [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
- [[central_avaliador_exercicios|🧪 Central de Verificação de Exercícios]]
