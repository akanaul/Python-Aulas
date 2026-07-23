#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gerador Automático de Notas para o Caderno do Aluno (meu_caderno_aluno/).

Este script é usado pelos Agentes de IA e pelo próprio aluno para registrar
automaticamente dúvidas, anotações de aulas e diagnósticos de erros usando os templates oficiais.
Suporta metadados para Dataview e Spaced Repetition (#flashcard).

Uso:
    python gerar_nota_agente.py --tipo duvida --titulo "Como usar pathlib" --conteudo "..."
    python gerar_nota_agente.py --tipo erro --titulo "SyntaxError em f-string" --conteudo "..."
    python gerar_nota_agente.py --tipo aula --titulo "Anotacoes Aula 10" --conteudo "..."
"""

import argparse
import datetime
import os
import sys

# Garantir codificação UTF-8 no stdout do Windows
if hasattr(sys.stdout, "reconfigure"):
    reconfig = getattr(sys.stdout, "reconfigure", None)
    if callable(reconfig):
        reconfig(encoding="utf-8")

def criar_nota(tipo: str, titulo: str, conteudo: str) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caderno_dir = os.path.join(base_dir, "meu_caderno_aluno")
    data_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    data_formatada = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    created_iso = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    slug_titulo = titulo.lower().replace(" ", "_").replace("/", "_")
    
    if tipo in ("duvida", "duvidas"):
        pasta_destino = os.path.join(caderno_dir, "duvidas")
        nome_arquivo = f"duvida_{slug_titulo}_{data_str}.md"
        tags_list = ["duvida", "caderno-aluno", "python"]
        status = "resolvido"
        header = f"# ❓ Dúvida: {titulo}\n\n> [!TUTOR] Gerado Automática via Agente de IA\n📅 **Data:** {data_formatada}\n\n"
    elif tipo in ("erro", "diagnostico", "bug"):
        pasta_destino = os.path.join(caderno_dir, "diagnostico_erros")
        nome_arquivo = f"erro_{slug_titulo}_{data_str}.md"
        tags_list = ["diagnostico-erro", "caderno-aluno", "flashcard"]
        status = "pendente"
        header = f"# 🚑 Diagnóstico de Erro: {titulo}\n\n> [!CAUTION] Registro de Depuração Automatizado\n📅 **Data:** {data_formatada}\n\n"
    elif tipo in ("aula", "anotacao"):
        pasta_destino = os.path.join(caderno_dir, "anotacoes_aulas")
        nome_arquivo = f"nota_{slug_titulo}_{data_str}.md"
        tags_list = ["anotacao-aula", "caderno-aluno", "estudo"]
        status = "concluido"
        header = f"# 📝 Anotação: {titulo}\n\n> [!NOTE] Resumo Automatizado via Agente de IA\n📅 **Data:** {data_formatada}\n\n"
    else:
        pasta_destino = os.path.join(caderno_dir, "anotacoes_aulas")
        nome_arquivo = f"nota_{slug_titulo}_{data_str}.md"
        tags_list = ["estudo", "caderno-aluno"]
        status = "geral"
        header = f"# 📝 Registro: {titulo}\n\n"

    os.makedirs(pasta_destino, exist_ok=True)
    caminho_final = os.path.join(pasta_destino, nome_arquivo)
    
    tags_str = ", ".join(tags_list)
    frontmatter = f"---\ntags:\n"
    for tag in tags_list:
        frontmatter += f"  - {tag}\n"
    frontmatter += f"created: \"{created_iso}\"\nstatus: \"{status}\"\n---\n"
    
    conteudo_completo = f"{frontmatter}\n{header}{conteudo}\n\n## 📚 Referências Acadêmicas\n- [[00_hub_referencias_academicas|Hub de Referências Acadêmicas]]\n"
    
    with open(caminho_final, "w", encoding="utf-8") as f:
        f.write(conteudo_completo)
        
    return caminho_final

def main():
    parser = argparse.ArgumentParser(description="Gerador de Notas do Agente para o Caderno do Aluno")
    parser.add_argument("--tipo", choices=["duvida", "erro", "aula", "anotacao"], required=True, help="Tipo de nota a gerar")
    parser.add_argument("--titulo", required=True, help="Título sucinto do tópico ou erro")
    parser.add_argument("--conteudo", required=True, help="Conteúdo explicativo da nota em Markdown")
    
    args = parser.parse_args()
    caminho = criar_nota(args.tipo, args.titulo, args.conteudo)
    print(f"✅ Nota criada com sucesso em: {caminho}")

if __name__ == "__main__":
    main()
