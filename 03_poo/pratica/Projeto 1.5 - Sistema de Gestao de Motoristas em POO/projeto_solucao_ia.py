"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — MINI-PROJETO 1.5
Sistema Completo de Gestão de Motoristas em POO
Issue #projeto1_5
"""

from typing import List, Dict, Any

class MotoristaPOO:
    def __init__(self, cpf: str, nome: str, categoria_cnh: str):
        self.cpf = cpf
        self.nome = nome
        self.categoria_cnh = categoria_cnh
        self.viagens_realizadas = 0

    def registrar_viagem(self):
        self.viagens_realizadas += 1

    def to_dict(self) -> Dict[str, Any]:
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "categoria_cnh": self.categoria_cnh,
            "viagens": self.viagens_realizadas
        }

if __name__ == "__main__":
    m = MotoristaPOO("123.456.789-00", "Roberto Alves", "E")
    m.registrar_viagem()
    print("Motorista POO:", m.to_dict())
