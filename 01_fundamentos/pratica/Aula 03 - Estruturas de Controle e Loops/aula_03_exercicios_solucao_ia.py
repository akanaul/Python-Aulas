"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 03
Estruturas Condicionais (if/elif/else) e Loops (for/while)
Issue #03
"""

from typing import List, Dict, Any

def classificar_eficiencia_entregas(entregas: List[float]) -> List[str]:
    """
    Classifica o desempenho de entregas com base no tempo gasto (em minutos).
    """
    classificacoes = []
    for tempo in entregas:
        if tempo <= 30.0:
            classificacoes.append("Excelente")
        elif tempo <= 60.0:
            classificacoes.append("Regular")
        else:
            classificacoes.append("Crítico")
    return classificacoes

def filtrar_entregas_pendentes(status_lista: List[str]) -> int:
    """
    Conta a quantidade de entregas com status 'pendente' utilizando while.
    """
    idx = 0
    count = 0
    while idx < len(status_lista):
        if status_lista[idx].lower() == "pendente":
            count += 1
        idx += 1
    return count

if __name__ == "__main__":
    tempos = [25.0, 45.0, 75.0]
    print("Classificações:", classificar_eficiencia_entregas(tempos))
