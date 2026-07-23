"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — MINI-PROJETO 1
Sistema de Ficha de Cadastro e Validação de Motoristas
Issue #projeto1
"""

from typing import Dict, Any

def cadastrar_motorista(nome: str, cnh: str, idade: int, veiculo: str) -> Dict[str, Any]:
    """
    Cadastra um motorista no sistema e valida os requisitos legais.
    """
    if idade < 21:
        raise ValueError("O motorista deve ter pelo menos 21 anos.")
    if len(cnh) < 9:
        raise ValueError("CNH inválida.")
        
    return {
        "nome": nome.strip().title(),
        "cnh": cnh.strip(),
        "idade": idade,
        "veiculo": veiculo.strip().upper(),
        "status": "ativo"
    }

if __name__ == "__main__":
    mot = cadastrar_motorista("João Silva", "123456789", 28, "Caminhão VUC")
    print("Motorista Cadastrado:", mot)
