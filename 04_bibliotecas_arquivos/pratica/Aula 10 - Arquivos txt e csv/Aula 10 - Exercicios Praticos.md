---
aliases: ["🧪 Exercícios Práticos — Aula 10: Arquivos TXT, CSV e Pathlib"]
tags: [exercicio, pratica, issue-10, python]
---

# 🧪 Exercícios Práticos — Aula 10: Arquivos TXT, CSV e Pathlib

### 📌 Do que se trata este Exercício?
Neste exercício, você aprenderá a ler e escrever arquivos de texto simples (.txt) e planilhas tabulares (.csv) utilizando caminhos relativos seguros com `pathlib.Path`.

**Objetivo Prático:**
1. Abra o arquivo `aula_10_exercicios_manual.py` na sua IDE.
2. Escreva logs de execução em um arquivo TXT especificando `encoding="utf-8"`.
3. Leia um arquivo CSV de cadastro de clientes usando `csv.DictReader`, filtre os registros de uma cidade específica e salve o resultado em um novo CSV usando `csv.DictWriter`.

Clique no botão **Run** abaixo para testar a leitura e escrita de arquivos!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #10)
> 📌 **Exercício Avaliado:** Issue #10
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

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 04_bibliotecas_arquivos/pratica/Aula 10 - Arquivos txt e csv/aula_10_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-10): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-10
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
