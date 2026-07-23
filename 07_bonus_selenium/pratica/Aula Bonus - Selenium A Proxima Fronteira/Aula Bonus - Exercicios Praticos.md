---
aliases: ["🧪 Exercícios Práticos — Aula Bônus: Selenium 4 e Chrome DevTools MCP"]
tags: [exercicio, pratica, issue-devtools, python]
---

# 🧪 Exercícios Práticos — Aula Bônus: Selenium 4 e Chrome DevTools MCP

### 📌 Do que se trata este Exercício?
Neste exercício bônus, você dominará a automação web profissional com Selenium 4 em modo headless e inspeção de DOM com Chrome DevTools MCP.

**Objetivo Prático:**
1. Abra o arquivo `devtools_mcp_manual.py` na sua IDE.
2. Configure o Selenium 4 para abrir o navegador Chrome em modo headless (`--headless=new`).
3. Utilize `WebDriverWait` para aguardar elementos dinâmicos, preencha formulários web e trate exceções `TimeoutException` e `NoSuchElementException` em um bloco `try / finally: driver.quit()`.

Clique no botão **Run** abaixo para testar sua automação web Selenium!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #devtools)
> 📌 **Exercício Avaliado:** Issue #devtools
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

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 07_bonus_selenium/pratica/Aula Bonus - Selenium A Proxima Fronteira/devtools_mcp_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-devtools): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-devtools
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
