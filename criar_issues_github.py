#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Criação Automatizada de Issues no GitHub via REST API Nativa.

Povoa o repositório oficial do professor no GitHub com as 21 issues de exercícios e mini-projetos
sem necessidade de nenhuma biblioteca externa (utiliza urllib.request nativo do Python).

Uso:
    python criar_issues_github.py --repo SEU_USUARIO/NOME_DO_REPO --token SEU_GITHUB_PAT
    python criar_issues_github.py (modo interativo)
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error

# Garantir UTF-8 no stdout do Windows
if hasattr(sys.stdout, "reconfigure"):
    reconfig = getattr(sys.stdout, "reconfigure", None)
    if callable(reconfig):
        reconfig(encoding="utf-8")

ISSUES_CATALOG = [
    {
        "title": "[EXERCÍCIO] Issue #00 - Mindset Vibe Coding Ético",
        "body": "## 🎯 Objetivo\nImplementar os conceitos de Vibe Coding Ético.\n\n## 📁 Arquivo Alvo (Manual)\n`01_fundamentos/Aula 00 - Mindset Vibe Coding Etico/aula_00_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 00`",
        "labels": ["exercicio", "modulo-01"]
    },
    {
        "title": "[EXERCÍCIO] Issue #01 - Setup Completo e Primeiros Passos",
        "body": "## 🎯 Objetivo\nValidar variáveis básicas e primeiros passos.\n\n## 📁 Arquivo Alvo (Manual)\n`01_fundamentos/Aula 01 - Setup e Primeiros Passos/aula_01_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 01`",
        "labels": ["exercicio", "modulo-01"]
    },
    {
        "title": "[EXERCÍCIO] Issue #02 - Variáveis e Operadores",
        "body": "## 🎯 Objetivo\nPraticar operadores aritméticos e lógicos.\n\n## 📁 Arquivo Alvo (Manual)\n`01_fundamentos/Aula 02 - Variáveis e Operadores/aula_02_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 02`",
        "labels": ["exercicio", "modulo-01"]
    },
    {
        "title": "[EXERCÍCIO] Issue #03 - Condicionais e Loops",
        "body": "## 🎯 Objetivo\nCriar estruturas condicionais e loops de repetição.\n\n## 📁 Arquivo Alvo (Manual)\n`01_fundamentos/Aula 03 - Condicionais e Loops/aula_03_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 03`",
        "labels": ["exercicio", "modulo-01"]
    },
    {
        "title": "[MINI-PROJETO] Issue #MINI-1 - Gerador de Ficha de Motorista",
        "body": "## 🎯 Objetivo\nConstruir o gerador de fichas cadastrais com validação.\n\n## 📁 Arquivo Alvo (Manual)\n`01_fundamentos/Mini-Projeto 1 - Gerador de Ficha de Motorista/projeto_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue mini-1`",
        "labels": ["mini-projeto", "modulo-01"]
    },
    {
        "title": "[EXERCÍCIO] Issue #04 - Strings e Formatação",
        "body": "## 🎯 Objetivo\nManipular f-strings, métodos de string e higienização.\n\n## 📁 Arquivo Alvo (Manual)\n`02_python_essencial/Aula 04 - Strings e Formatação/aula_04_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 04`",
        "labels": ["exercicio", "modulo-02"]
    },
    {
        "title": "[EXERCÍCIO] Issue #05 - Listas, Tuplas e Ranges",
        "body": "## 🎯 Objetivo\nManipular sequências, iteração e ordenação.\n\n## 📁 Arquivo Alvo (Manual)\n`02_python_essencial/Aula 05 - Listas Tuplas e Ranges/aula_05_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 05`",
        "labels": ["exercicio", "modulo-02"]
    },
    {
        "title": "[EXERCÍCIO] Issue #06 - Dicionários e Conjuntos",
        "body": "## 🎯 Objetivo\nTrabalhar com estruturas chave-valor e remoção de duplicatas.\n\n## 📁 Arquivo Alvo (Manual)\n`02_python_essencial/Aula 06 - Dicionarios e Conjuntos/aula_06_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 06`",
        "labels": ["exercicio", "modulo-02"]
    },
    {
        "title": "[EXERCÍCIO] Issue #07 - Funções com Type Hints e PEP 8",
        "body": "## 🎯 Objetivo\nConstruir funções reutilizáveis com anotações de tipo.\n\n## 📁 Arquivo Alvo (Manual)\n`02_python_essencial/Aula 07 - Funções/aula_07_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 07`",
        "labels": ["exercicio", "modulo-02"]
    },
    {
        "title": "[MINI-PROJETO] Issue #MINI-2 - Analisador de Rotas",
        "body": "## 🎯 Objetivo\nConstruir o analisador de rotas e custos de transporte.\n\n## 📁 Arquivo Alvo (Manual)\n`02_python_essencial/Mini-Projeto 2 - Analisador de Rotas/`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue mini-2`",
        "labels": ["mini-projeto", "modulo-02"]
    },
    {
        "title": "[EXERCÍCIO] Issue #08 - Vibe Coding & Engenharia de Prompt",
        "body": "## 🎯 Objetivo\nPraticar a formulação de prompts e auditoria com a IA.\n\n## 📁 Arquivo Alvo (Manual)\n`06_ia_prompt/Aula 08 - Vibe Coding e Engenharia de Prompt/aula_08_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 08`",
        "labels": ["exercicio", "modulo-06"]
    },
    {
        "title": "[EXERCÍCIO] Issue #09A - Módulos e POO Básico",
        "body": "## 🎯 Objetivo\nModelar classes simples e importar módulos.\n\n## 📁 Arquivo Alvo (Manual)\n`03_poo/Aula 09A - Modulos e POO Basico/aula_09a_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 09a`",
        "labels": ["exercicio", "modulo-03"]
    },
    {
        "title": "[EXERCÍCIO] Issue #09B - POO Prático e Persistência",
        "body": "## 🎯 Objetivo\nConstruir composição de objetos e salvar em JSON.\n\n## 📁 Arquivo Alvo (Manual)\n`03_poo/Aula 09B - POO Pratico Composicao e Persistencia/aula_09b_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 09b`",
        "labels": ["exercicio", "modulo-03"]
    },
    {
        "title": "[MINI-PROJETO] Issue #MINI-1.5 - Sistema de Cadastro",
        "body": "## 🎯 Objetivo\nImplementar a persistência POO no cadastro de motoristas.\n\n## 📁 Arquivo Alvo (Manual)\n`03_poo/Mini-Projeto 1.5 - Sistema de Cadastro de Motoristas/`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue mini-1.5`",
        "labels": ["mini-projeto", "modulo-03"]
    },
    {
        "title": "[EXERCÍCIO] Issue #10 - Arquivos TXT e CSV",
        "body": "## 🎯 Objetivo\nLer, processar e salvar registros em arquivos TXT e CSV.\n\n## 📁 Arquivo Alvo (Manual)\n`04_bibliotecas_arquivos/Aula 10 - Arquivos txt e csv/aula_10_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 10`",
        "labels": ["exercicio", "modulo-04"]
    },
    {
        "title": "[EXERCÍCIO] Issue #11 - Excel com openpyxl e pandas",
        "body": "## 🎯 Objetivo\nManipular planilhas Excel, fórmulas e DataFrames.\n\n## 📁 Arquivo Alvo (Manual)\n`04_bibliotecas_arquivos/Aula 11 - Excel com openpyxl e pandas/aula_11_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 11`",
        "labels": ["exercicio", "modulo-04"]
    },
    {
        "title": "[EXERCÍCIO] Issue #12 - E-mail Automático e Agendamento",
        "body": "## 🎯 Objetivo\nEnviar notificações HTML automáticas por e-mail.\n\n## 📁 Arquivo Alvo (Manual)\n`04_bibliotecas_arquivos/Aula 12 - Email Automatico e Agendamento/aula_12_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 12`",
        "labels": ["exercicio", "modulo-04"]
    },
    {
        "title": "[MINI-PROJETO] Issue #MINI-3 - Relatório KPI de Entregas",
        "body": "## 🎯 Objetivo\nGerar o relatório consolidado de KPIs com pandas e openpyxl.\n\n## 📁 Arquivo Alvo (Manual)\n`04_bibliotecas_arquivos/Mini-Projeto 3 - Relatorio KPI de Entregas/`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue mini-3`",
        "labels": ["mini-projeto", "modulo-04"]
    },
    {
        "title": "[EXERCÍCIO] Issue #13 - PyAutoGUI Básico",
        "body": "## 🎯 Objetivo\nAutomatizar cliques e digitação no desktop.\n\n## 📁 Arquivo Alvo (Manual)\n`05_automacao_desktop/Aula 13 - PyAutoGUI Basico/aula_13_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 13`",
        "labels": ["exercicio", "modulo-05"]
    },
    {
        "title": "[EXERCÍCIO] Issue #14 - PyAutoGUI Avançado",
        "body": "## 🎯 Objetivo\nTrabalhar com localização visual de imagens e Failsafe.\n\n## 📁 Arquivo Alvo (Manual)\n`05_automacao_desktop/Aula 14 - PyAutoGUI Avancado/aula_14_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 14`",
        "labels": ["exercicio", "modulo-05"]
    },
    {
        "title": "[MINI-PROJETO] Issue #MINI-4 - Robô de Preenchimento",
        "body": "## 🎯 Objetivo\nConstruir o robô de preenchimento automático desktop.\n\n## 📁 Arquivo Alvo (Manual)\n`05_automacao_desktop/Mini-Projeto 4 - Robo de Preenchimento/`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue mini-4`",
        "labels": ["mini-projeto", "modulo-05"]
    },
    {
        "title": "[EXERCÍCIO] Issue #15 - Prompt Engineering Avançado",
        "body": "## 🎯 Objetivo\nAplicar Few-Shot e Chain-of-Thought em projetos complexos.\n\n## 📁 Arquivo Alvo (Manual)\n`06_ia_prompt/Aula 15 - Prompt Engineering Avancado/aula_15_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 15`",
        "labels": ["exercicio", "modulo-06"]
    },
    {
        "title": "[EXERCÍCIO] Issue #16 - Revisão Geral e Autonomia",
        "body": "## 🎯 Objetivo\nConsolidar todos os aprendizados e preparar o portfólio.\n\n## 📁 Arquivo Alvo (Manual)\n`06_ia_prompt/Aula 16 - Revisao Geral e Proximos Passos/aula_16_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue 16`",
        "labels": ["exercicio", "modulo-06"]
    },
    {
        "title": "[EXERCÍCIO] Issue #07-BONUS - Selenium Web Tradicional",
        "body": "## 🎯 Objetivo\nNavegação web e extração de dados com Selenium 4.\n\n## 📁 Arquivo Alvo (Manual)\n`07_bonus_selenium/Aula Bonus - Selenium A Proxima Fronteira/aula_bonus_selenium_exercicios_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue bonus`",
        "labels": ["exercicio", "modulo-07"]
    },
    {
        "title": "[EXERCÍCIO] Issue #07-DEVTOOLS - Chrome DevTools MCP",
        "body": "## 🎯 Objetivo\nExtração web resiliente e inspeção de DOM via Chrome DevTools MCP.\n\n## 📁 Arquivo Alvo (Manual)\n`07_bonus_selenium/Aula Bonus - Selenium A Proxima Fronteira/devtools_mcp_manual.py`\n\n## 🧪 Teste Automatizado\n`python avaliar_exercicio.py --issue devtools`",
        "labels": ["exercicio", "modulo-07"]
    }
]

def setup_git_remote(repo: str):
    """Configura a URL do git remote origin se necessário."""
    remote_url = f"https://github.com/{repo}.git"
    try:
        res = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"📌 Adicionando remote origin -> {remote_url}")
            subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
        else:
            print(f"📌 Remote origin já existente: {res.stdout.strip()}")
    except Exception as e:
        print(f"⚠️ Alerta ao configurar remote: {e}")

def create_issue_api(repo: str, token: str, issue: dict) -> bool:
    """Cria uma issue no GitHub utilizando a API REST oficial."""
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Python-Git-Course-Script"
    }
    payload = {
        "title": issue["title"],
        "body": issue["body"],
        "labels": issue["labels"]
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            if response.status in (200, 201):
                res_body = json.loads(response.read().decode("utf-8"))
                print(f"   ✅ Issue #{res_body.get('number')} criada: {res_body.get('html_url')}")
                return True
    except urllib.error.HTTPError as e:
        print(f"   ❌ Erro HTTP ({e.code}): {e.reason}")
        try:
            err_json = json.loads(e.read().decode("utf-8"))
            print(f"      Mensagem: {err_json.get('message')}")
        except Exception:
            pass
    except Exception as e:
        print(f"   ❌ Erro na requisição: {e}")
    return False

def main():
    parser = argparse.ArgumentParser(
        description="Gerador Automático de Issues no GitHub via API REST Nativa"
    )
    parser.add_argument("--repo", type=str, help="Repositório alvo no formato USUARIO/NOME_REPO")
    parser.add_argument("--token", type=str, help="Personal Access Token (PAT) do GitHub")
    args = parser.parse_args()

    print("=" * 65)
    print("🚀 GERADOR AUTOMÁTICO DE ISSUES NO GITHUB (VIA API REST)")
    print("=" * 65)

    repo = args.repo or os.environ.get("GITHUB_REPOSITORY")
    token = args.token or os.environ.get("GITHUB_TOKEN")

    if not repo:
        repo = input("📌 Digite o Repositório no formato USUARIO/REPO (ex: meu-usuario/curso-python): ").strip()
    if not token:
        token = input("🔑 Digite seu GitHub Personal Access Token (PAT): ").strip()

    if not repo or not token:
        print("❌ Repositório e Token são obrigatórios. Operação cancelada.")
        print("💡 Nota: As especificações em texto continuam disponíveis em '.github/ISSUES.md'.")
        print("=" * 65)
        sys.exit(1)

    setup_git_remote(repo)

    print(f"\n📌 Publicando {len(ISSUES_CATALOG)} Issues em '{repo}'...\n")

    sucesso = 0
    for idx, item in enumerate(ISSUES_CATALOG, 1):
        print(f"⏳ ({idx}/{len(ISSUES_CATALOG)}) Criando: {item['title']}...")
        if create_issue_api(repo, token, item):
            sucesso += 1

    print("\n" + "=" * 65)
    print(f"🎉 Processo Concluído! {sucesso} de {len(ISSUES_CATALOG)} Issues criadas com sucesso.")
    print("=" * 65)

if __name__ == "__main__":
    main()
