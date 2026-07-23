#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gerador Automático de Notas para o Caderno do Aluno (meu_caderno_aluno/).

Este script é usado pelos Agentes de IA e pelo próprio aluno para registrar
automaticamente dúvidas, anotações de aulas e diagnósticos de erros usando os templates oficiais.

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
    
    slug_titulo = titulo.lower().replace(" ", "_").replace("/", "_")
    
    if tipo in ("duvida", "duvidas"):
        pasta_destino = os.path.join(caderno_dir, "duvidas")
        nome_arquivo = f"duvida_{slug_titulo}_{data_str}.md"
        tag = "duvida"
        header = f"# ❓ Dúvida: {titulo}\n\n> [!TUTOR] Gerado Automática via Agente de IA\n📅 **Data:** {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
    elif tipo in ("erro", "diagnostico", "bug"):
        pasta_destino = os.path.join(caderno_dir, "diagnostico_erros")
        nome_arquivo = f"erro_{slug_titulo}_{data_str}.md"
        tag = "diagnostico"
        header = f"# 🚑 Diagnóstico de Erro: {titulo}\n\n> [!CAUTION] Registro de Depuração Automatizado\n📅 **Data:** {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
    elif tipo in ("aula", "anotacao"):
        pasta_destino = os.path.join(caderno_dir, "anotacoes_aulas")
        nome_arquivo = f"nota_{slug_titulo}_{data_str}.md"
        tag = "anotacao"
        header = f"# 📝 Anotação: {titulo}\n\n> [!TIP] Resumo Automatizado via Agente de IA\n📅 **Data:** {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
    else:
        pasta_destino = os.path.join(caderno_dir, "anotacoes_aulas")
        nome_arquivo = f"nota_{slug_titulo}_{data_str}.md"
        tag = "estudo"
        header = f"# 📝 Registro: {titulo}\n\n"

    os.makedirs(pasta_destino, exist_ok=True)
    caminho_final = os.path.join(pasta_destino, nome_arquivo)
    
    frontmatter = f"---\ntags: [{tag}, auto-agente, python]\ncreated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n---\n"
    
    conteudo_completo = f"{frontmatter}{header}{conteudo}\n"
    
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
