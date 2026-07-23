#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Avaliador Automatizado de Exercícios e Gatekeeper Git.

Este script executa a suíte de testes unitários para a issue/exercício solicitada
e gera um relatório claro em PT-BR informando se a solução foi ACEITA ou RECUSADA,
além de fornecer dicas diagnósticas didáticas e comandos Git para o aluno.

Uso:
    python avaliar_exercicio.py --issue 07
    python avaliar_exercicio.py --all
"""

import argparse
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
        description="Avaliador Automatizado de Exercícios (Curso Python + IA)"
    )
    parser.add_argument(
        "--issue",
        type=str,
        help="Número ou ID da Issue/Exercício a avaliar (ex: 07, web, dashboard)",
        default="all"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Avaliar todas as issues e testes unitários do repositório"
    )
    args = parser.parse_args()

    print("=" * 65)
    print("🧪 AVALIADOR AUTOMATIZADO DE EXERCÍCIOS & GATEKEEPER GIT")
    print("=" * 65)

    if args.all or args.issue == "all" or args.issue == "todos":
        pattern = "test_*.py"
        target_name = "Todos os Módulos"
    else:
        pattern = f"*test*{args.issue}*.py"
        target_name = f"Issue #{args.issue}"

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
        print(f"      git commit -m \"fix(issue-{args.issue}): solucao pre-aprovada pela IA\"")
        print("   2. Envie a branch para o SEU fork no GitHub:")
        print(f"      git push origin feature/issue-{args.issue}")
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
        print(f"   python avaliar_exercicio.py --issue {args.issue}")
        print("=" * 65)
        sys.exit(1)

if __name__ == "__main__":
    main()
