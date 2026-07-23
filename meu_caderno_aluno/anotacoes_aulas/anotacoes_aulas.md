---
sticker: "📝"
---
# 📝 Minhas Anotações de Aulas

> [!TIP]
> Pressione `Alt+N` e use o **Template de Anotação do Aluno** para adicionar novas notas nesta pasta.

```dataview
TABLE file.ctime AS "Criado Em", tags AS "Tags"
FROM "meu_caderno_aluno/anotacoes_aulas"
WHERE file.name != "anotacoes_aulas"
SORT file.ctime DESC
```


---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #all)
> 📌 **Exercício Avaliado:** Issue #all — Suíte Geral de Testes do Vault
> 📁 **Arquivo de Trabalho na IDE:** `avaliar_exercicio.py --all`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #all...")
print("📁 Arquivo Alvo na IDE: avaliar_exercicio.py --all")
res = subprocess.run([sys.executable, script_path, "--issue", "all"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```
