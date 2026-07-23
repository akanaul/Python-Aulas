---
aliases: ["🧪 Mini-Projeto 1 — Gerador de Ficha de Motorista"]
tags: [exercicio, pratica, issue-projeto1, python]
---

# 🧪 Mini-Projeto 1 — Gerador de Ficha de Motorista

### 📌 Do que se trata este Mini-Projeto?
Este é o **Mini-Projeto Integrador do Módulo 01**. Você construirá um aplicativo de console em Python puro para cadastrar, validar e gerar fichas cadastrais completas de motoristas de caminhão.

**Objetivo do Projeto:**
1. Abra o arquivo `projeto_manual.py` na pasta `Mini-Projeto 1` na sua IDE.
2. Programe a coleta e validação de dados do motorista (Nome, CPF, CNH, Categoria, Experiência em Anos).
3. Aplique as regras de negócio: CNH categoria 'D' ou 'E' para caminhões pesados, no mínimo 2 anos de experiência e validação defensiva contra erros de digitação.
4. Exiba a ficha cadastral formatada em formato tabular.

Clique no botão **Run** no bloco abaixo para rodar a suíte completa de testes do Mini-Projeto 1!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #projeto1)
> 📌 **Exercício Avaliado:** Issue #projeto1
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

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 01_fundamentos/pratica/Mini-Projeto 1 - Gerador de Ficha de Motorista/projeto_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-projeto1): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-projeto1
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
