"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 14
Visão Computacional e Tratamento de Exceções em Automação Desktop
Issue #14
"""

from typing import Dict, Any

def localizar_elemento_com_seguranca(imagem_ref: str, tentativas: int = 3) -> Dict[str, Any]:
    """
    Simula o algoritmo de busca por imagem de referência com retry.
    """
    return {
        "imagem": imagem_ref,
        "tentativas_realizadas": tentativas,
        "encontrado": True,
        "coordenadas": (100, 200)
    }

if __name__ == "__main__":
    print(localizar_elemento_com_seguranca("botao_salvar.png"))
