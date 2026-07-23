---
aliases: ["🧪 Exercícios Práticos — Aula 09B: Composição e Persistência JSON"]
tags: [exercicio, pratica, issue-09b, python]
---

# 🧪 Exercícios Práticos — Aula 09B: Composição e Persistência JSON

### 📌 Do que se trata este Exercício?
Neste exercício, você avançará em POO conectando objetos através de **Composição** e salvando o estado dos objetos em disco com arquivos `.json` e `pathlib.Path`.

**Objetivo Prático:**
1. Abra o arquivo `aula_09b_exercicios_manual.py` na sua IDE.
2. Crie a classe `ItemProduto` e a classe `CarrinhoCompras` que guarda uma lista interna de instâncias de produtos.
3. Desenvolva os métodos `salvar_em_json(caminho)` e `carregar_de_json(caminho)` para serializar e re-instanciar os objetos da memória RAM para o disco de forma persistente.

Clique no botão **Run** abaixo para testar a composição e serialização JSON!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #09b)
> 📌 **Exercício Avaliado:** Issue #09b
> 📁 **Arquivo de Trabalho na IDE:** `03_poo/pratica/Aula 09B - POO Pratico Composicao e Persistencia/aula_09b_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #09b...")
print("📁 Arquivo Alvo na IDE: 03_poo/pratica/Aula 09B - POO Pratico Composicao e Persistencia/aula_09b_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "09b"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 03_poo/pratica/Aula 09B - POO Pratico Composicao e Persistencia/aula_09b_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-09b): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-09b
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
