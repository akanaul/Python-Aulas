#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Avaliador Automatizado de Exercícios, Gatekeeper Git e Gerador de Relatório de Progresso.

Este script é a ferramenta central do aluno no curso:
1. Avalia exercícios e testes unitários (python avaliar_exercicio.py --issue XX).
2. Gera relatórios de progresso do vault (python avaliar_exercicio.py --progresso).
3. Protege e verifica o vault do Obsidian em background.

Uso:
    python avaliar_exercicio.py --issue 07
    python avaliar_exercicio.py --all
    python avaliar_exercicio.py --progresso
"""

import argparse
import os
import sys
import unittest

# Importar auto-restaurador do vault
try:
    from setup_vault import auto_heal_vault
except ImportError:
    auto_heal_vault = lambda: None

# Garantir codificação UTF-8 no stdout do Windows
if hasattr(sys.stdout, "reconfigure"):
    reconfig = getattr(sys.stdout, "reconfigure", None)
    if callable(reconfig):
        reconfig(encoding="utf-8")


def gerar_relatorio_progresso():
    """Gera relatório de progresso de notas de aula e exercícios no vault."""
    print("=" * 65)
    print("📊 RELATÓRIO DE PROGRESSO DO VAULT OBSIDIAN")
    print("=" * 65)
    
    modulos = [
        "01_fundamentos",
        "02_python_essencial",
        "03_poo",
        "04_bibliotecas_arquivos",
        "05_automacao_desktop",
        "06_ia_prompt",
        "07_bonus_selenium"
    ]
    
    total_aulas = 0
    total_exercicios = 0
    
    for mod in modulos:
        if os.path.exists(mod):
            for root, dirs, files in os.walk(mod):
                for f in files:
                    if f.endswith(".md"):
                        total_aulas += 1
                    elif f.endswith("_manual.py") or f == "projeto_manual.py":
                        total_exercicios += 1
                        
    print(f"✅ Total de Notas de Aulas / Módulos Mapeados: {total_aulas}")
    print(f"✅ Total de Exercícios Práticos Mapeados: {total_exercicios}")
    print("=" * 65)
    print("💡 Acesse '00_dashboard.md' no Obsidian para ver o painel dinâmico.")
    print("=" * 65)


def run_tests(test_pattern: str = "test_*.py") -> bool:
    """Executa a suíte de testes unitários e retorna True se todos passarem."""
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="testes", pattern=test_pattern)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()


def main():
    auto_heal_vault()
    parser = argparse.ArgumentParser(
        description="Avaliador Automatizado e Gerador de Progresso (Curso Python + IA)"
    )
    parser.add_argument(
        "--issue",
        type=str,
        help="Número ou ID da Issue/Exercício a avaliar (ex: 07, devtools, mini-1)",
        default=None
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Avaliar todas as issues e testes unitários do repositório"
    )
    parser.add_argument(
        "--progresso", "--status",
        action="store_true",
        help="Exibir relatório estatístico do progresso do aluno no vault"
    )
    args = parser.parse_args()

    if args.progresso:
        gerar_relatorio_progresso()
        sys.exit(0)

    print("=" * 65)
    print("🧪 AVALIADOR AUTOMATIZADO DE EXERCÍCIOS & GATEKEEPER GIT")
    print("=" * 65)

    if args.all or not args.issue or args.issue in ("all", "todos"):
        pattern = "test_*.py"
        target_name = "Todos os Módulos"
        issue_id = "all"
    else:
        pattern = f"*test*{args.issue}*.py"
        target_name = f"Issue #{args.issue}"
        issue_id = args.issue

    print(f"📌 Avaliando: {target_name}")
    print("⏳ Executando testes unitários...\n")

    try:
        success = run_tests(pattern)
    except Exception as e:
        print(f"\n❌ ERRO NA EXECUÇÃO DOS TESTES: {e}")
        success = False

    print("\n" + "=" * 65)
    if success:
        print("🎉 ✅ PRÉ-APROVADO PELA IA! (REVISÃO 1 DE 2 OK)")
        print("=" * 65)
        print("Sua implementação passou em 100% dos testes automatizados locais.")
        print("\n🔀 Próximos Passos (Revisão 2 - Professor/Tutor Humano):")
        print("   1. Salve suas alterações no Git local:")
        print(f"      git add .")
        print(f"      git commit -m \"fix(issue-{issue_id}): solucao pre-aprovada pela IA\"")
        print("   2. Envie a branch para o SEU fork no GitHub:")
        print(f"      git push origin feature/issue-{issue_id}")
        print("   3. Abra um Pull Request (PR) do seu fork para o REPOSITÓRIO OFICIAL DO PROFESSOR.")
        print("   4. O Professor/Tutor revisará seu código no GitHub e fará o MERGE oficial!")
        print("=" * 65)
        sys.exit(0)
    else:
        print("⚠️ ❌ RECUSADO PELA IA — AJUSTES NECESSÁRIOS")
        print("=" * 65)
        print("Seu código em *_manual.py ainda não passou nos testes automatizados.")
        print("\n💡 Dicas do Mentor (Modo Tutor):")
        print("   - Leia atentamente a mensagem de erro da falha acima.")
        print("   - Lembre-se: o arquivo *_ia.py serve apenas como referência didática de comparação.")
        print("   - Trabalhe passo a passo na lógica do arquivo *_manual.py antes de tentar novamente.")
        print("\n🔄 Após ajustar o código, rode novamente:")
        print(f"   python avaliar_exercicio.py --issue {issue_id}")
        print("=" * 65)
        sys.exit(1)


if __name__ == "__main__":
    main()
