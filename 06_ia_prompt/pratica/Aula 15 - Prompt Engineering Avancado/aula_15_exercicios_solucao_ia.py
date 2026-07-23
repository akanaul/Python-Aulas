"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 15
Prompt Engineering Avançado: Few-Shot, Chain-of-Thought e System Instructions
Issue #15
"""

from typing import Dict, List, Any

def construir_prompt_few_shot(exemplos: List[Dict[str, str]], entrada_usuario: str) -> str:
    """
    Constrói a estrutura de prompt com técnica Few-Shot.
    """
    prompt = "Você é um assistente logístico. Classifique o status:

"
    for ex in exemplos:
        prompt += f"Entrada: {ex['entrada']}
Saída: {ex['saida']}
---
"
    prompt += f"Entrada: {entrada_usuario}
Saída:"
    return prompt

if __name__ == "__main__":
    exs = [{"entrada": "Carga chegou em SP", "saida": "Entregue"}]
    print(construir_prompt_few_shot(exs, "Carga a caminho de BH"))
