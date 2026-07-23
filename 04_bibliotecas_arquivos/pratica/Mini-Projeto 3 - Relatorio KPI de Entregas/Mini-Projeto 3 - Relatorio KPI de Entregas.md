---
aliases: ["🧪 Mini-Projeto 3 — Relatório KPI de Entregas Logísticas"]
tags: [exercicio, pratica, issue-projeto3, python]
---

# 🧪 Mini-Projeto 3 — Relatório KPI de Entregas Logísticas

### 📌 Do que se trata este Mini-Projeto?
Este é o **Mini-Projeto Integrador do Módulo 04**. Você construirá um pipeline completo de automação que lê dados brutos de logística, processa estatísticas de entrega, gera uma planilha Excel estilizada e envia o resumo executivo por e-mail.

**Objetivo do Projeto:**
1. Abra o arquivo `projeto_manual.py` na pasta `Mini-Projeto 3` na sua IDE.
2. Consolide o fluxo: Leitura CSV ➔ Análise Pandas ➔ Formatação OpenPyXL ➔ Disparo SMTP / Schedule.
3. Garanta tratamento defensivo para arquivos ausentes e permissões negadas.

Clique no botão **Run** abaixo para rodar os testes do Mini-Projeto 3!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #projeto3)
> 📌 **Exercício Avaliado:** Issue #projeto3
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

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 04_bibliotecas_arquivos/pratica/Mini-Projeto 3 - Relatorio KPI de Entregas/projeto_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-projeto3): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-projeto3
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
