"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 01
Setup Completo e Primeiros Passos em Python
Issue #01
"""

from typing import Dict, Any

def obter_configuracao_sistema() -> Dict[str, Any]:
    """
    Retorna os dados de configuração inicial do interpretador e ambiente virtual.
    """
    return {
        "python_version": "3.12",
        "venv_ativo": True,
        "ide": "VS Code / Antigravity",
        "status": "pronto"
    }

def calcular_boas_vindas(nome: str) -> str:
    """
    Retorna a mensagem de boas-vindas formatada.
    """
    return f"Bem-vindo(a) ao Curso Python + IA, {nome}!"

if __name__ == "__main__":
    print(obter_configuracao_sistema())
    print(calcular_boas_vindas("Dev"))
