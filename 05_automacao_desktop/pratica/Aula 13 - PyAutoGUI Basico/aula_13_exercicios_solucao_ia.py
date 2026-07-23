"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 13
Automação Desktop com PyAutoGUI Básico
Issue #13
"""

from typing import Dict, Any

def simular_comando_automação(acao: str, x: int, y: int) -> Dict[str, Any]:
    """
    Simula uma instrução de automação de clique ou digitação de teclado.
    """
    return {
        "acao": acao,
        "posicao": (x, y),
        "executado": True
    }

if __name__ == "__main__":
    print(simular_comando_automação("click", 500, 300))
