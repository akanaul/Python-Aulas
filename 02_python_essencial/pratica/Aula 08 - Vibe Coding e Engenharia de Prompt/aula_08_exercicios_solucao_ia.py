"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 08
Engenharia de Prompt C-T-R-F (Contexto, Tarefa, Requisitos, Formato)
Issue #08
"""

from typing import Dict, Any

def estruturar_prompt_ctrf(contexto: str, tarefa: str, requisitos: list, formato: str) -> Dict[str, Any]:
    """
    Monta um dicionário estruturado de prompt para o agente agêntico.
    """
    return {
        "contexto": contexto.strip(),
        "tarefa": tarefa.strip(),
        "requisitos": [r.strip() for r in requisitos],
        "formato": formato.strip()
    }

if __name__ == "__main__":
    p = estruturar_prompt_ctrf("Automação de Fretes", "Calcular rota otimizada", ["Usar Python 3.12", "Retornar JSON"], "JSON")
    print("Prompt Estruturado:", p)
