---
aliases: ["🧪 Mini-Projeto 2 — Analisador de Rotas Logísticas"]
tags: [exercicio, pratica, issue-projeto2, python]
---

# 🧪 Mini-Projeto 2 — Analisador de Rotas Logísticas

### 📌 Do que se trata este Mini-Projeto?
Este é o **Mini-Projeto Integrador do Módulo 02**. Você desenvolverá um Analisador de Desempenho de Rotas Logísticas que recebe um lote de dados de viagens, filtra rotas ineficientes, calcula estatísticas e gera um resumo executivo.

**Objetivo do Projeto:**
1. Abra o arquivo `projeto_manual.py` na pasta `Mini-Projeto 2` na sua IDE.
2. Utilize listas, dicionários e `set` para eliminar rotas duplicadas e calcular o consumo médio de combustível por quilômetro.
3. Crie funções modularizadas com Type Hints e Docstrings (PEP 257) e retorne o relatório estatístico formatado.

Clique no botão **Run** abaixo para testar o Mini-Projeto 2 completo!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #projeto2)
> 📌 **Exercício Avaliado:** Issue #projeto2
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

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 02_python_essencial/pratica/Mini-Projeto 2 - Analisador de Rotas/projeto_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-projeto2): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-projeto2
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
