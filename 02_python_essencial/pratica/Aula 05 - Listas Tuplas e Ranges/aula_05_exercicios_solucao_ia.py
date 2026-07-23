"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 05
Estruturas de Dados Sequenciais: Listas, Tuplas e Ranges
Issue #05
"""

from typing import List, Tuple

def processar_pacotes_carga(pesos: List[float]) -> Tuple[float, float, int]:
    """
    Métrica de carga: retorna (peso_total, peso_medio, quantidade_pacotes).
    """
    if not pesos:
        return (0.0, 0.0, 0)
    peso_total = round(sum(pesos), 2)
    peso_medio = round(peso_total / len(pesos), 2)
    return (peso_total, peso_medio, len(pesos))

if __name__ == "__main__":
    print(processar_pacotes_carga([12.5, 45.0, 30.2]))
