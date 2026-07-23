"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — MINI-PROJETO 2
Calculadora de Rotas e Custos Logísticos
Issue #projeto2
"""

from typing import Dict, Any

def calcular_rota_logistica(distancia_km: float, consumo_kml: float, preco_combustivel: float, pedagio: float = 0.0) -> Dict[str, float]:
    """
    Calcula o custo total da viagem com combustível e pedágio.
    """
    if distancia_km <= 0 or consumo_kml <= 0:
        raise ValueError("Distância e consumo devem ser maiores que zero.")
        
    litros_necessarios = round(distancia_km / consumo_kml, 2)
    custo_combustivel = round(litros_necessarios * preco_combustivel, 2)
    custo_total = round(custo_combustivel + pedagio, 2)
    
    return {
        "litros_necessarios": litros_necessarios,
        "custo_combustivel": custo_combustivel,
        "pedagio": pedagio,
        "custo_total": custo_total
    }

if __name__ == "__main__":
    print(calcular_rota_logistica(450.0, 10.0, 5.80, 42.50))
