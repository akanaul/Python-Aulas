"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 00
Mindset Vibe Coding Ético, Copilotos de IA e Fundamentos do Git Flow
Issue #00
"""

from typing import Dict, Any, List

def verificar_ambiente_vibe_coding() -> Dict[str, Any]:
    """
    Retorna o status do ambiente de desenvolvimento agêntico e ética em Vibe Coding.
    
    Passo a Passo:
    1. Define um dicionário com os parâmetros do ecossistema.
    2. Retorna a confirmação de que o interpretador e copiloto estão ativos.
    """
    return {
        "status": "configurado",
        "modo": "vibe_coding_etico",
        "copiloto_ativo": True,
        "git_flow": "habilitado"
    }

def listar_regras_eticas() -> List[str]:
    """
    Retorna a lista de boas práticas éticas em Vibe Coding.
    """
    return [
        "Auditar o código gerado pela IA antes do commit",
        "Garantir 100% de cobertura de testes unitários",
        "Não commitar chaves de API ou dados sensíveis",
        "Manter o ambiente virtual (venv) ativado"
    ]

if __name__ == "__main__":
    print("📌 [TESTE MANUAL GABARITO IA - AULA 00]")
    print("Status:", verificar_ambiente_vibe_coding())
    print("Regras Éticas:", listar_regras_eticas())
