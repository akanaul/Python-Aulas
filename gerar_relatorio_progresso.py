#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gerador de Relatório de Progresso do Aluno.

Este script analisa as tarefas marcadas no vault e exibe um relatório consolidado em PT-BR.
"""

import os
import re

def calcular_progresso(vault_path: str = ".") -> dict:
    """Mapeia os marcadores de tarefas [x] vs [ ] no Dashboard."""
    dashboard_path = os.path.join(vault_path, "00 - Dashboard.md")
    if not os.path.exists(dashboard_path):
        return {"total": 0, "concluidas": 0, "percentual": 0}

    with open(dashboard_path, "r", encoding="utf-8") as f:
        content = f.read()

    tasks = re.findall(r"- \[(x| )\]", content)
    total = len(tasks)
    concluidas = sum(1 for t in tasks if t == "x")
    percentual = round((concluidas / total * 100)) if total > 0 else 0

    return {
        "total": total,
        "concluidas": concluidas,
        "percentual": percentual
    }

def main():
    print("=" * 60)
    print("📊 RELATÓRIO DE PROGRESSO DO ALUNADO — PYTHON + IA")
    print("=" * 60)

    dados = calcular_progresso()
    print(f"✅ Atividades Concluídas: {dados['concluidas']} de {dados['total']}")
    print(f"📈 Percentual Geral de Conclusão: {dados['percentual']}%")
    print("=" * 60)

if __name__ == "__main__":
    main()
