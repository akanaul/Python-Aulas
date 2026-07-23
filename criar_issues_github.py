#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Criação Automatizada de Issues no GitHub.

Povoa o repositório oficial do professor com todas as issues de exercícios e mini-projetos
mapeados para que os alunos possam fazer o fork e submeter Pull Requests (PRs).

Uso:
    python criar_issues_github.py
"""

import subprocess
import sys
import shutil

# Garantir UTF-8 no stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ISSUES_LIST = [
    {
        "title": "[EXERCÍCIO] Issue #00 - Mindset Vibe Coding Ético",
        "body": "## 🎯 Objetivo\nImplementar os conceitos de Vibe Coding Ético.\n\n## 📁 Arquivo Alvo (Manual)\n`01_fundamentos/Aula 00 - Mindset Vibe Coding Etico/aula_00_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 00`",
        "labels": "exercicio, modulo-01"
    },
    {
        "title": "[EXERCÍCIO] Issue #01 - Setup Completo e Primeiros Passos",
        "body": "## 🎯 Objetivo\nValidar variáveis básicas e primeiros passos.\n\n## 📁 Arquivo Alvo (Manual)\n`01_fundamentos/Aula 01 - Setup e Primeiros Passos/aula_01_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 01`",
        "labels": "exercicio, modulo-01"
    },
    {
        "title": "[EXERCÍCIO] Issue #02 - Variáveis e Operadores",
        "body": "## 🎯 Objetivo\nPraticar operadores aritméticos e lógicos.\n\n## 📁 Arquivo Alvo (Manual)\n`01_fundamentos/Aula 02 - Variáveis e Operadores/aula_02_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 02`",
        "labels": "exercicio, modulo-01"
    },
    {
        "title": "[EXERCÍCIO] Issue #03 - Condicionais e Loops",
        "body": "## 🎯 Objetivo\nCriar estruturas condicionais e loops de repetição.\n\n## 📁 Arquivo Alvo (Manual)\n`01_fundamentos/Aula 03 - Condicionais e Loops/aula_03_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 03`",
        "labels": "exercicio, modulo-01"
    },
    {
        "title": "[MINI-PROJETO] Issue #MINI-1 - Gerador de Ficha de Motorista",
        "body": "## 🎯 Objetivo\nConstruir o gerador de fichas cadastrais com validação.\n\n## 📁 Arquivo Alvo (Manual)\n`01_fundamentos/Mini-Projeto 1 - Gerador de Ficha de Motorista/projeto_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue mini-1`",
        "labels": "mini-projeto, modulo-01"
    },
    {
        "title": "[EXERCÍCIO] Issue #04 - Strings e Formatação",
        "body": "## 🎯 Objetivo\nManipular f-strings, métodos de string e higienização.\n\n## 📁 Arquivo Alvo (Manual)\n`02_python_essencial/Aula 04 - Strings e Formatação/aula_04_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 04`",
        "labels": "exercicio, modulo-02"
    },
    {
        "title": "[EXERCÍCIO] Issue #05 - Listas, Tuplas e Ranges",
        "body": "## 🎯 Objetivo\nManipular sequências, iteração e ordenação.\n\n## 📁 Arquivo Alvo (Manual)\n`02_python_essencial/Aula 05 - Listas Tuplas e Ranges/aula_05_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 05`",
        "labels": "exercicio, modulo-02"
    },
    {
        "title": "[EXERCÍCIO] Issue #06 - Dicionários e Conjuntos",
        "body": "## 🎯 Objetivo\nTrabalhar com estruturas chave-valor e remoção de duplicatas.\n\n## 📁 Arquivo Alvo (Manual)\n`02_python_essencial/Aula 06 - Dicionarios e Conjuntos/aula_06_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 06`",
        "labels": "exercicio, modulo-02"
    },
    {
        "title": "[EXERCÍCIO] Issue #07 - Funções com Type Hints e PEP 8",
        "body": "## 🎯 Objetivo\nConstruir funções reutilizáveis com anotações de tipo.\n\n## 📁 Arquivo Alvo (Manual)\n`02_python_essencial/Aula 07 - Funções/aula_07_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 07`",
        "labels": "exercicio, modulo-02"
    },
    {
        "title": "[EXERCÍCIO] Issue #07-DEVTOOLS - Chrome DevTools MCP",
        "body": "## 🎯 Objetivo\nPraticar extração web assistida por IA via Chrome DevTools MCP.\n\n## 📁 Arquivo Alvo (Manual)\n`07_bonus_selenium/Aula Bonus - Selenium A Proxima Fronteira/devtools_mcp_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue devtools`",
        "labels": "exercicio, modulo-07"
    }
]

def main():
    print("=" * 65)
    print("🚀 CRIADOR AUTOMÁTICO DE ISSUES NO GITHUB")
    print("=" * 65)

    gh_cli = shutil.which("gh")
    if not gh_cli:
        print("⚠️ GitHub CLI ('gh') não encontrado no sistema.")
        print("💡 As especificações completas das issues estão salvas em '.github/ISSUES.md'.")
        print("=" * 65)
        sys.exit(0)

    print(f"📌 {len(ISSUES_LIST)} Issues encontradas no catálogo. Criando no GitHub...\n")

    for item in ISSUES_LIST:
        print(f"⏳ Criando: {item['title']}...")
        cmd = [
            "gh", "issue", "create",
            "--title", item["title"],
            "--body", item["body"],
            "--label", item["labels"]
        ]
        try:
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                print(f"   ✅ Criada com sucesso: {res.stdout.strip()}")
            else:
                print(f"   ⚠️ Alerta ao criar: {res.stderr.strip()}")
        except Exception as e:
            print(f"   ❌ Erro de execução: {e}")

    print("\n" + "=" * 65)
    print("🎉 Todas as Issues foram processadas!")
    print("=" * 65)

if __name__ == "__main__":
    main()
