"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 11
Automação de Planilhas com openpyxl e pandas
Issue #11
"""

from typing import Dict, Any

def simular_analise_pandas(dados_pedidos: list) -> Dict[str, Any]:
    """
    Simula o cálculo de totalizador de faturamento de pedidos.
    """
    total = sum(p.get("valor", 0.0) for p in dados_pedidos)
    media = total / len(dados_pedidos) if dados_pedidos else 0.0
    return {"total_faturamento": round(total, 2), "media_pedido": round(media, 2)}

if __name__ == "__main__":
    pedidos = [{"valor": 100.0}, {"valor": 200.0}]
    print("Métricas Excel/pandas:", simular_analise_pandas(pedidos))
