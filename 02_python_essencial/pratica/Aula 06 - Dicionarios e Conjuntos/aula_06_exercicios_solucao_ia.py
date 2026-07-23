"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 06
Dicionários, Chave-Valor e Conjuntos (Sets)
Issue #06
"""

from typing import List, Dict, Set

def agrupar_pedidos_por_cidade(pedidos: List[Dict[str, str]]) -> Dict[str, List[str]]:
    """
    Agrupa os IDs de pedidos por cidade de destino.
    """
    resultado = {}
    for p in pedidos:
        cidade = p["cidade"]
        pedido_id = p["id"]
        if cidade not in resultado:
            resultado[cidade] = []
        resultado[cidade].append(pedido_id)
    return resultado

def obter_cidades_unicas(pedidos: List[Dict[str, str]]) -> Set[str]:
    """
    Retorna o conjunto de cidades únicas de destino.
    """
    return {p["cidade"] for p in pedidos}

if __name__ == "__main__":
    dados = [{"id": "P1", "cidade": "São Paulo"}, {"id": "P2", "cidade": "Campinas"}, {"id": "P3", "cidade": "São Paulo"}]
    print("Agrupado:", agrupar_pedidos_por_cidade(dados))
