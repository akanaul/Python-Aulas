---
sticker: "🗺️"
tags: [moc, indice, curso, python]
---
# 🗺️ Índice Geral & Mapa de Aprendizado (MOC)

> [!TUTOR] Mapa de Navegação Interativo do Curso
> Este MOC (*Map of Content*) reúne todas as aulas, exercícios práticos e mini-projetos do curso, permitindo navegar rapidamente com o **Hover Editor** (`Ctrl+passar o mouse`).

---

## ⚡ 1-Clique: Avaliar Progresso Geral do Curso
```python run
import subprocess
res = subprocess.run(["python", "avaliar_exercicio.py", "--progresso"], capture_output=True, text=True)
print(res.stdout)
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
