---
sticker: "🗺️"
tags: [moc, indice, curso, python]
---
# 🗺️ Índice Geral & Mapa de Aprendizado (MOC)

> [!TUTOR] Mapa de Navegação Interativo do Curso
> Este MOC (*Map of Content*) reúne todas as aulas, exercícios práticos e mini-projetos do curso, permitindo navegar rapidamente com o **Hover Editor** (`Ctrl+passar o mouse`).

---

## ⚡ 1-Clique: Avaliar Progresso Geral do Curso
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

---

## 📚 Módulos Oficiais do Curso

```dataview
TABLE 
    file.folder AS "Módulo / Pasta",
    choice(completed, "✅ Concluído", "⚡ Em Progresso") AS "Status",
    file.ctime AS "Data de Mapeamento"
FROM #aula OR #exercicio
SORT file.name ASC
```

---

## 🔀 Mapa das 25 Issues do GitHub & Exercícios Práticos

| Módulo | Issue | Aula / Exercício | Arquivo Manual | Comando de Avaliação |
| :--- | :--- | :--- | :--- | :--- |
| **01 Fundamentos** | `#00` | Mindset & Setup | `aula_00_manual.py` | `python avaliar_exercicio.py --issue 00` |
| **01 Fundamentos** | `#01` | Tipos & Variáveis | `aula_01_manual.py` | `python avaliar_exercicio.py --issue 01` |
| **01 Fundamentos** | `#02` | Operadores | `aula_02_manual.py` | `python avaliar_exercicio.py --issue 02` |
| **01 Fundamentos** | `#03` | Strings | `aula_03_manual.py` | `python avaliar_exercicio.py --issue 03` |
| **02 Essencial** | `#04` | Condicionais | `aula_04_manual.py` | `python avaliar_exercicio.py --issue 04` |
| **02 Essencial** | `#05` | Loops `for` / `while` | `aula_05_manual.py` | `python avaliar_exercicio.py --issue 05` |
| **02 Essencial** | `#06` | Funções | `aula_06_manual.py` | `python avaliar_exercicio.py --issue 06` |
| **02 Essencial** | `#07` | Listas & Dics | `aula_07_manual.py` | `python avaliar_exercicio.py --issue 07` |
| **03 POO** | `#09A` | Classes | `aula_09a_manual.py` | `python avaliar_exercicio.py --issue 09a` |
| **03 POO** | `#09B` | Encapsulamento | `aula_09b_manual.py` | `python avaliar_exercicio.py --issue 09b` |
| **04 Arquivos** | `#10` | Pathlib, TXT & CSV | `aula_10_manual.py` | `python avaliar_exercicio.py --issue 10` |
| **04 Arquivos** | `#11` | Excel openpyxl/pandas | `aula_11_manual.py` | `python avaliar_exercicio.py --issue 11` |
| **04 Arquivos** | `#12` | Automação de E-mails | `aula_12_manual.py` | `python avaliar_exercicio.py --issue 12` |
| **05 Desktop** | `#13` | PyAutoGUI Mouse/Teclado | `aula_13_manual.py` | `python avaliar_exercicio.py --issue 13` |
| **05 Desktop** | `#14` | Reconhecimento de Imagens | `aula_14_manual.py` | `python avaliar_exercicio.py --issue 14` |
| **06 IA Prompt** | `#08` | Engenharia de Prompt | `aula_08_manual.py` | `python avaliar_exercicio.py --issue 08` |
| **06 IA Prompt** | `#15` | Pipelines com IA | `aula_15_manual.py` | `python avaliar_exercicio.py --issue 15` |
| **06 IA Prompt** | `#16` | Revisão & Autonomia | `aula_16_manual.py` | `python avaliar_exercicio.py --issue 16` |
| **07 Selenium** | `#devtools` | DevTools MCP | `devtools_manual.py` | `python avaliar_exercicio.py --issue devtools` |
| **07 Selenium** | `#selenium` | Selenium WebDriver | `selenium_manual.py` | `python avaliar_exercicio.py --issue selenium` |
| **Projetos** | `#mini-1` | Mini-Projeto 1 | `projeto_1_manual.py` | `python avaliar_exercicio.py --issue mini-1` |
| **Projetos** | `#mini-2` | Mini-Projeto 2 | `projeto_2_manual.py` | `python avaliar_exercicio.py --issue mini-2` |
| **Projetos** | `#mini-3` | Mini-Projeto 3 | `projeto_3_manual.py` | `python avaliar_exercicio.py --issue mini-3` |
| **Projetos** | `#mini-4` | Mini-Projeto 4 | `projeto_4_manual.py` | `python avaliar_exercicio.py --issue mini-4` |

---

## 🔗 Links Rápidos
- [[00 - Dashboard|📊 Dashboard Principal]]
- [[MANUAL_DO_ALUNO|📘 Manual do Aluno]]
- [[00_central/plano_de_estudos|📋 Plano de Estudos (Kanban)]]
- [[00_central/central_flashcards|📇 Central de Flashcards]]
- [[meu_caderno_aluno/meu_caderno_aluno|📓 Meu Caderno de Estudos]]
