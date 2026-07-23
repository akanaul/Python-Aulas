---
aliases: ["🧪 Mini-Projeto 1.5 — Sistema de Cadastro de Motoristas POO"]
tags: [exercicio, pratica, issue-projeto1_5, python]
---

# 🧪 Mini-Projeto 1.5 — Sistema de Cadastro de Motoristas POO

### 📌 Do que se trata este Mini-Projeto?
Este é o **Mini-Projeto de Evolução Arquitetural do Módulo 03**. Você refatorará a aplicação de cadastro de motoristas para uma arquitetura profissional 100% Orientada a Objetos com persistência de dados.

**Objetivo do Projeto:**
1. Abra o arquivo `projeto_manual.py` na pasta `Mini-Projeto 1.5` na sua IDE.
2. Implemente as classes `Motorista` e `GerenciadorFrotas`.
3. Garanta a validação de CNH, salvamento automático dos cadastros em arquivos JSON na pasta do projeto e recarga dos registros ao reiniciar o script.

Clique em **Run** no bloco abaixo para rodar os testes da suíte POO!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #projeto1_5)
> 📌 **Exercício Avaliado:** Issue #projeto1_5
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

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 03_poo/pratica/Mini-Projeto 1.5 - Sistema de Cadastro de Motoristas/projeto_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-projeto1_5): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-projeto1_5
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
