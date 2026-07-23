---
aliases: ["🧪 Exercícios Práticos — Aula 11: Excel com openpyxl e pandas"]
tags: [exercicio, pratica, issue-11, python]
---

# 🧪 Exercícios Práticos — Aula 11: Excel com openpyxl e pandas

### 📌 Do que se trata este Exercício?
Neste exercício, você automatizará a análise de dados em planilhas Excel utilizando a alta performance do `pandas` e a estilização visual detalhada do `openpyxl`.

**Objetivo Prático:**
1. Abra o arquivo `aula_11_exercicios_manual.py` na sua IDE.
2. Carregue uma planilha de vendas em um DataFrame do `pandas`, filtre produtos vendidos com preço > R$ 100 e calcule o faturamento total.
3. Crie uma nova planilha com `openpyxl`, aplique cor de fundo verde no cabeçalho, fonte em negrito e trate exceções `PermissionError` caso o arquivo esteja aberto no Excel.

Clique em **Run** no bloco abaixo para testar a automação Excel!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #11)
> 📌 **Exercício Avaliado:** Issue #11
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

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 04_bibliotecas_arquivos/pratica/Aula 11 - Excel com openpyxl e pandas/aula_11_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-11): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-11
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
