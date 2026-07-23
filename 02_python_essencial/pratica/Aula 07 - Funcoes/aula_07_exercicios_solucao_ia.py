"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 07
Funções, Decoradores, *args, **kwargs e Geradores
Issue #07
"""

from typing import List, Generator

def calcular_frete_total(*valores: float, taxa_fixa: float = 15.0) -> float:
    """
    Calcula o valor total do frete somando cargas dinâmicas e taxa fixa.
    """
    return round(sum(valores) + taxa_fixa, 2)

def gerador_codigos_rastreio(prefixo: str, quantidade: int) -> Generator[str, None, None]:
    """
    Gerador que produz códigos de rastreio sob demanda.
    """
    for i in range(1, quantidade + 1):
        yield f"{prefixo.upper()}{i:04d}BR"

if __name__ == "__main__":
    print("Frete:", calcular_frete_total(50.0, 30.0, 20.0))
    print("Códigos:", list(gerador_codigos_rastreio("TRK", 3)))
