# Curso Python + IA para Automação

Este repositório/vault contém todos os materiais, exercícios automatizados e anotações do curso de Python + IA focado em automação prática do dia a dia.

---

## 📘 Guia de Início Rápido

Antes de começar, consulte o **[[MANUAL_DO_ALUNO|📘 Manual Oficial do Aluno]]** para entender o método Vibe Coding Ético e o ciclo de aprendizado em 4 passos:
1. **Estudo no Obsidian:** Leitura da aula com o copiloto de IA no Modo Tutor.
2. **Desenvolvimento na IDE:** Criação de branch Git (`git checkout -b feature/issue-XX`) e edição do script `*_manual.py`.
3. **Avaliação Automatizada:** Validação com `python avaliar_exercicio.py --issue XX`.
4. **Commit & Merge:** Salvamento do progresso (`git commit` & `git merge main`).

---

## 🗺️ Estrutura de Módulos do Curso

- `01_fundamentos/` — Lógica, Variáveis, Operadores, Condicionais e Loops.
- `02_python_essencial/` — Strings, Listas, Tuplas, Dicionários e Funções com Type Hints.
- `03_poo/` — Programação Orientada a Objetos, Classes e Composição.
- `04_bibliotecas_arquivos/` — Manipulação de TXT, CSV, Excel (`openpyxl`/`pandas`) e E-mails HTML.
- `05_automacao_desktop/` — Automação de Interface Desktop com PyAutoGUI.
- `06_ia_prompt/` — Vibe Coding Ético, Chain-of-Thought e Auditoria Sênior de Código.
- `07_bonus_selenium/` — Automação Web Dual (Selenium 4 + Chrome DevTools MCP).
- `08_guias_recursos/` — Guias de Git, Plugins do Obsidian, IDE e Resolução de Erros.
- `99_referencia_teorica/` — Referências teóricas aprofundadas.

---

## 🛡️ Proteção do Vault Obsidian em 1 Segundo

Caso abra o vault em uma nova instalação e queira garantir que todos os **19 plugins** fiquem ativos sem Modo Restrito:
```bash
python setup_vault.py
```

---

## 🧪 Testes Automatizados

Para validar os exercícios de todos os módulos:
```bash
python -m unittest discover testes
```
