"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 02
Variáveis, Tipos de Dados e Operadores Aritméticos/Lógicos
Issue #02
"""

from typing import Dict, Union

def processar_dados_motorista(nome: str, idade: int, km_rodados: float, valor_por_km: float) -> Dict[str, Union[str, int, float, bool]]:
    """
    Processa e calcula o faturamento bruto e elegibilidade de um motorista.
    """
    faturamento = round(km_rodados * valor_por_km, 2)
    pode_dirigir = idade >= 18
    
    return {
        "nome": nome,
        "idade": idade,
        "faturamento_bruto": faturamento,
        "maior_de_idade": pode_dirigir
    }

if __name__ == "__main__":
    res = processar_dados_motorista("Carlos", 35, 120.5, 2.50)
    print("Faturamento Motorista:", res)
