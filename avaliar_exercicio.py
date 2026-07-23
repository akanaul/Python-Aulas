#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Avaliador Automatizado de Exercícios, Gatekeeper Git, Gerador de Relatório e Diagnóstico de Erros.

Este script é a ferramenta central do aluno no curso:
1. Avalia exercícios e testes unitários (python avaliar_exercicio.py --issue XX).
2. Exibe diagnósticos detalhados em falhas (qual parte do exercício falhou e por quê).
3. Salva a nota de erro no caderno do aluno (meu_caderno_aluno/diagnostico_erros/).
4. Gera relatórios de progresso do vault (python avaliar_exercicio.py --progresso).

Uso:
    python avaliar_exercicio.py --issue 07
    python avaliar_exercicio.py --all
    python avaliar_exercicio.py --progresso
"""

import argparse
import datetime
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
    print("💡 Acesse '00 - Dashboard.md' no Obsidian para ver o painel dinâmico.")
    print("=" * 65)


def salvar_nota_diagnostico_erro(issue_id: str, falhas_detalhadas: list):
    """Cria automaticamente uma nota de erro no caderno do aluno meu_caderno_aluno/diagnostico_erros/."""
    caderno_dir = os.path.join("meu_caderno_aluno", "diagnostico_erros")
    os.makedirs(caderno_dir, exist_ok=True)
    
    now = datetime.datetime.now()
    timestamp_str = now.strftime("%Y%m%d_%H%M%S")
    data_formatada = now.strftime("%d/%m/%Y %H:%M:%S")
    
    filename = f"erro_issue_{issue_id}_{timestamp_str}.md"
    filepath = os.path.join(caderno_dir, filename)
    
    detalhes_md = ""
    for idx, falha in enumerate(falhas_detalhadas, 1):
        detalhes_md += f"### Falha #{idx}: `{falha['teste']}`\n"
        detalhes_md += f"- ❌ **Causa do Erro:** `{falha['erro']}`\n"
        detalhes_md += f"- 💡 **Dica do Mentor:** {falha['dica']}\n\n"
        detalhes_md += f"```text\n{falha['traceback']}\n```\n\n---\n\n"

    content = f"""---
tags:
  - caderno-aluno
  - diagnostico-erro
  - issue-{issue_id}
data: {data_formatada}
---
# ⚠️ Diagnóstico de Erro — Issue #{issue_id}

> [!CAUTION] Registrado pelo Avaliador Automatizado da IA em {data_formatada}

## 📌 Detalhes das Falhas Encontradas

{detalhes_md}

## 📝 Anotações Pessoais do Aluno / Tutor
- **O que aprendi com este erro:** 
- **Solução aplicada:** 
"""

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath
    except Exception as e:
        print(f"⚠️ Não foi possível salvar a nota de erro no caderno: {e}")
        return None


def run_tests(test_pattern: str = "test_*.py"):
    """Executa a suíte de testes unitários e retorna (success, result)."""
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="testes", pattern=test_pattern)
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(suite)
    return result.wasSuccessful(), result


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
    parser.add_argument(
        "--audit", "--debug",
        action="store_true",
        help="Modo Depuração & Bug Hunting: exibe diagnóstico detalhado de falhas de lógica"
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
        success, result = run_tests(pattern)
    except Exception as e:
        print(f"\n❌ ERRO NA EXECUÇÃO DOS TESTES: {e}")
        success, result = False, None

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
        
        falhas_detalhadas = []
        if result:
            todas_falhas = result.failures + result.errors
            print(f"\n🔍 DIAGNÓSTICO DETALHADO ({len(todas_falhas)} falha(s) identificada(s)):\n")
            
            for idx, (test_case, tb_text) in enumerate(todas_falhas, 1):
                test_name = str(test_case)
                linhas_tb = tb_text.strip().splitlines()
                causa_erro = linhas_tb[-1] if linhas_tb else "Falha desconhecida no teste"
                
                dica_mentor = "Revise a sintaxe e a lógica do arquivo *_manual.py usando a IA no Modo Tutor."
                if "SyntaxError" in causa_erro:
                    dica_mentor = "Verifique parênteses, aspas ou dois-pontos (:) não fechados no script."
                elif "AssertionError" in causa_erro:
                    dica_mentor = "O resultado retornado pela sua função difere do comportamento esperado."
                elif "FileNotFoundError" in causa_erro:
                    dica_mentor = "Verifique se o arquivo ou caminho especificado realmente existe."
                
                print(f"📌 [{idx}/{len(todas_falhas)}] Teste: {test_name}")
                print(f"   ❌ Causa do Erro: {causa_erro}")
                print(f"   💡 Dica do Mentor: {dica_mentor}\n")
                
                falhas_detalhadas.append({
                    "teste": test_name,
                    "erro": causa_erro,
                    "dica": dica_mentor,
                    "traceback": tb_text
                })
                
            nota_salva = salvar_nota_diagnostico_erro(issue_id, falhas_detalhadas)
            if nota_salva:
                rel_path = os.path.relpath(nota_salva)
                print("=" * 65)
                print(f"📝 NOTA DE DIAGNÓSTICO DO ERRO SALVA NO SEU CADERNO DE ALUNO!")
                print(f"📄 Arquivo: {rel_path}")
                print(f"💡 Abra o arquivo no Obsidian para revisar com seu Tutor ou IA.")
                print("=" * 65)

        print("\n🛠️ CHECKLIST DE DEBBUGGING AUTÔNOMO (5 PASSOS PARA VOCÊ RESOLVER):")
        print("   1. 📍 Localize a linha do erro no arquivo *_manual.py.")
        print("   2. 🔎 Imprima valores com print() antes da linha para inspecionar.")
        print("   3. 📖 Consulte o Manual Python 3.12 em '99_referencia_teorica/doc_python/'.")
        print("   4. 🤖 Use o Antigravity no MODO TUTOR (peça dicas de lógica, não a resposta).")
        print("   5. ⚡ Clique em Run no Obsidian para reavaliar!")
        print("\n🔄 Após ajustar o código, rode novamente:")
        print(f"   python avaliar_exercicio.py --issue {issue_id}")
        print("=" * 65)
        sys.exit(1)


if __name__ == "__main__":
    main()
