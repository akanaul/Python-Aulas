---
aliases: ["🧪 Exercícios Práticos — Aula 16: Revisão Geral e Síntese Arquitetural"]
tags: [exercicio, pratica, issue-16, python]
---

# 🧪 Exercícios Práticos — Aula 16: Revisão Geral e Síntese Arquitetural

### 📌 Do que se trata este Exercício?
Neste exercício final da jornada Dev+IA, você construirá o gerenciador integrador que consolida todo o conhecimento adquirido no curso.

**Objetivo Prático:**
1. Abra o arquivo `aula_16_exercicios_manual.py` na sua IDE.
2. Implemente a classe `GerenciadorAutomacao` que registra o status de execução de cada módulo e exporta um relatório consolidado em JSON.
3. Valide a árvore de decisão arquitetural para saber quando usar files, pandas, PyAutoGUI ou Selenium.

Clique em **Run** no bloco abaixo para rodar o teste final do Módulo 06!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #16)
> 📌 **Exercício Avaliado:** Issue #16
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

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 06_ia_prompt/pratica/Aula 16 - Revisao Geral e Proximos Passos/aula_16_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-16): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-16
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
