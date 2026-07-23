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
    created_iso = now.strftime("%Y-%m-%d %H:%M")
    
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
  - flashcard
  - issue-{issue_id}
created: "{created_iso}"
status: "pendente"
issue: "{issue_id}"
---

# ⚠️ Diagnóstico de Erro — Issue #{issue_id}

> [!CAUTION] Registrado pelo Avaliador Automatizado da IA em {data_formatada}

## 📌 Detalhes das Falhas Encontradas

{detalhes_md}

## 🎴 Flashcard para Revisão Espaçada (Spaced Repetition)
- **Como corrigir o erro na Issue #{issue_id}?** #flashcard
  - **Resposta:** Verificar causa `{falhas_detalhadas[0]['erro'] if falhas_detalhadas else 'Traceback'}` e aplicar refatoração segundo a dica do Mentor.

## 📚 Referências de Apoio
- [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
"""

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath
    except Exception as e:
        print(f"⚠️ Não foi possível salvar a nota de erro no caderno: {e}")
        return None


def salvar_nota_progresso_sucesso(issue_id: str):
    """Cria/Atualiza automaticamente uma nota de progresso de sucesso em meu_caderno_aluno/progresso/."""
    progresso_dir = os.path.join("meu_caderno_aluno", "progresso")
    os.makedirs(progresso_dir, exist_ok=True)
    
    now = datetime.datetime.now()
    data_formatada = now.strftime("%d/%m/%Y %H:%M:%S")
    created_iso = now.strftime("%Y-%m-%d %H:%M")
    
    filename = f"progresso_issue_{issue_id}.md"
    filepath = os.path.join(progresso_dir, filename)
    
    content = f"""---
tags:
  - caderno-aluno
  - progresso
  - issue-{issue_id}
created: "{created_iso}"
status: "concluido"
issue: "{issue_id}"
---

# 🎉 Progresso Registrado — Issue #{issue_id}

> [!SUCCESS] Exercício Pré-Aprovado pela IA em {data_formatada}
> Parabéns! Sua solução passou em 100% dos testes automatizados locais da **Issue #{issue_id}**.

## 📌 Resumo da Conclusão
- **Status:** ✅ 100% Aprovado
- **Módulo / Issue:** Issue #{issue_id}
- **Data de Aprovação:** {data_formatada}

## 🔀 Próximos Passos recomendados:
1. `git add .`
2. `git commit -m "fix(issue-{issue_id}): solucao pre-aprovada pela IA"`
3. `git push origin feature/issue-{issue_id}`
4. Abrir o Pull Request (PR) no GitHub para o Professor/Tutor!
"""

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath
    except Exception as e:
        print(f"⚠️ Não foi possível registrar o progresso no caderno: {e}")
        return None


def marcar_checklists_concluidos(issue_id: str):
    """Marca checklists (- [ ] -> - [x]) relacionados à issue aprovada no vault."""
    import re
    if not issue_id or issue_id in ("all", "todos"):
        return 0
    
    modificados = 0
    pattern_issue = re.compile(rf"- \[ \] (.*?\b(issue|aula|mini-projeto)?\s*#?{re.escape(issue_id)}\b.*)", re.IGNORECASE)
    
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".obsidian" in root or "venv" in root or ".trash" in root or "node_modules" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                filepath = os.path.join(root, f)
                try:
                    with open(filepath, "r", encoding="utf-8") as file:
                        content = file.read()
                    
                    if f"#{issue_id}" in content or f"Issue #{issue_id}" in content or f"issue-{issue_id}" in content:
                        new_content, count = pattern_issue.subn(r"- [x] \1", content)
                        if count > 0:
                            with open(filepath, "w", encoding="utf-8") as file:
                                file.write(new_content)
                            modificados += count
                except Exception:
                    pass
    return modificados


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
        
        nota_progresso = salvar_nota_progresso_sucesso(issue_id)
        if nota_progresso:
            rel_p = os.path.relpath(nota_progresso)
            print(f"📝 NOTA DE PROGRESSO REGISTRADA AUTOMATICAMENTE NO SEU CADERNO DE ALUNO!")
            print(f"📄 Arquivo: {rel_p}")
            
        chk_count = marcar_checklists_concluidos(issue_id)
        if chk_count > 0:
            print(f"☑️ CHECKLISTS ATUALIZADOS: {chk_count} item(ns) marcado(s) como concluído(s) (- [x]) no Vault!")
        
        print("\n🔀 TUTORIAL PASSO A PASSO DE GIT (PRÁTICA NO TERMINAL):")
        print("   💡 Pratique os comandos no seu terminal para fixar o aprendizado do Git Flow!\n")
        print(f"   1. Criar/Alternar para a branch da issue:")
        print(f"      git checkout -b feature/issue-{issue_id}")
        print(f"   2. Adicionar os arquivos alterados ao staging:")
        print(f"      git add .")
        print(f"   3. Registrar o commit convencional (vinculado à issue):")
        print(f"      git commit -m \"fix(issue-{issue_id}): resolucao aprovada nos testes #{issue_id}\"")
        print(f"   4. Enviar a branch para o repositório remoto no GitHub:")
        print(f"      git push origin feature/issue-{issue_id}")
        print(f"   5. Criar o Pull Request (PR) do seu fork para o repositório do Tutor!")
        print("\n🤖 Dica do Agente Antigravity:")
        print("   Se preferir que o Agente execute a sequência do Git por você (branch, commit e push), basta pedir no chat!")
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
        print("   3. 📖 Consulte o Hub Acadêmico e PEPs em '99_referencia_teorica/'.")
        print("   4. 🤖 Use o Antigravity no MODO TUTOR (peça dicas de lógica, não a resposta).")
        print("   5. ⚡ Reavaliação no terminal!")
        print("\n🔄 Após ajustar o código, rode novamente:")
        print(f"   python avaliar_exercicio.py --issue {issue_id}")
        print("=" * 65)
        sys.exit(1)


if __name__ == "__main__":
    main()
