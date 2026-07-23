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

# Garantir codificação UTF-8 no stdout do Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def run_tests(test_pattern: str = "test_*.py") -> bool:
    """Executa a suíte de testes unitários e retorna True se todos passarem."""
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="testes", pattern=test_pattern)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result.wasSuccessful()

def main():
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
        print("🎉 ✅ SOLUÇÃO ACEITA! PARABÉNS!")
        print("=" * 65)
        print("Sua implementação atendeu a 100% dos requisitos e passou nos testes automatizados.")
        print("\n🔀 Próximos Passos recomendados no Git:")
        print(f"   1. git add .")
        print(f"   2. git commit -m \"fix(issue-{args.issue}): solucao aceita nos testes automatizados\"")
        print(f"   3. git checkout main")
        print(f"   4. git merge feature/issue-{args.issue}")
        print("=" * 65)
        sys.exit(0)
    else:
        print("⚠️ ❌ SOLUÇÃO RECUSADA — AJUSTES NECESSÁRIOS")
        print("=" * 65)
        print("Seu código ainda não passou em todos os testes automatizados.")
        print("\n💡 Dicas do Mentor (Modo Tutor):")
        print("   - Leia atentamente a mensagem de falha/erro acima.")
        print("   - Verifique a assinatura de funções, nomes de variáveis e valores de retorno.")
        print("   - Lembre-se: no arquivo *_manual.py, foque na lógica passo a passo antes de rodar novamente.")
        print("\n🔄 Após ajustar o código, rode este comando novamente:")
        print(f"   python avaliar_exercicio.py --issue {args.issue}")
        print("=" * 65)
        sys.exit(1)

if __name__ == "__main__":
    main()
