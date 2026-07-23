#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de geração de relatório de progresso do aluno no Vault Obsidian.
Sincroniza estatísticas com o 00_dashboard.md e a pasta 00_central/.
"""

import os
import sys

# Garantir UTF-8 no stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def gerar_relatorio():
    print("=" * 60)
    print("📊 GERADOR DE RELATÓRIO DE PROGRESSO DO VAULT OBSIDIAN")
    print("=" * 60)
    
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
    print("=" * 60)
    print("💡 Acesse '00_dashboard.md' no Obsidian para ver o painel dinâmico.")
    print("=" * 60)

if __name__ == "__main__":
    gerar_relatorio()
