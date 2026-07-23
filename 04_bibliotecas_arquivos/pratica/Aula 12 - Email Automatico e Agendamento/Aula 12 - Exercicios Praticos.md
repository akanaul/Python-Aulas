---
aliases: ["🧪 Exercícios Práticos — Aula 12: Email Automático e Agendamento"]
tags: [exercicio, pratica, issue-12, python]
---

# 🧪 Exercícios Práticos — Aula 12: Email Automático e Agendamento

### 📌 Do que se trata este Exercício?
Neste exercício, você tornará suas automações autônomas construindo rotinas de disparo de e-mails (`smtplib`, `EmailMessage`) e agendamento de tarefas (`schedule`).

**Objetivo Prático:**
1. Abra o arquivo `aula_12_exercicios_manual.py` na sua IDE.
2. Monte uma mensagem de e-mail estruturada usando `EmailMessage`, anexando um arquivo PDF ou CSV com detecção de tipo MIME.
3. Configure regras de execução com `schedule.every()` para rodar uma função de relatório periodicamente com tratamento de exceções de conexão SMTP.

Clique em **Run** abaixo para testar o envio de e-mails e agendamento!

---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #12)
> 📌 **Exercício Avaliado:** Issue #12
> 📁 **Arquivo de Trabalho na IDE:** `04_bibliotecas_arquivos/pratica/Aula 12 - Email Automatico e Agendamento/aula_12_exercicios_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #12...")
print("📁 Arquivo Alvo na IDE: 04_bibliotecas_arquivos/pratica/Aula 12 - Email Automatico e Agendamento/aula_12_exercicios_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "12"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```

---

## 🔀 Workflow de Envio do Pull Request (PR)

Após passar em 100% nos testes automatizados acima:

```bash
# 1. Adicionar alterações ao staging
git add 04_bibliotecas_arquivos/pratica/Aula 12 - Email Automatico e Agendamento/aula_12_exercicios_manual.py

# 2. Registrar o commit
git commit -m "fix(issue-12): resolucao dos exercicios praticos"

# 3. Enviar para o repositório remoto
git push origin feature/issue-12
```

> 🚀 **Passo Final:** Abra o **Pull Request (PR)** no GitHub para revisão do Tutor!
