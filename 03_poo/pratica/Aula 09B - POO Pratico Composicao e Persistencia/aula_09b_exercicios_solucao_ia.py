"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 09B
Composição de Objetos e Persistência JSON
Issue #09b
"""

import json
from typing import List, Dict, Any

class ItemCarga:
    def __init__(self, descricao: str, peso: float):
        self.descricao = descricao
        self.peso = peso

    def to_dict(self) -> Dict[str, Any]:
        return {"descricao": self.descricao, "peso": self.peso}

class RomaneioCarga:
    def __init__(self, codigo: str):
        self.codigo = codigo
        self.itens: List[ItemCarga] = []

    def adicionar_item(self, item: ItemCarga):
        self.itens.append(item)

    def salvar_json(self, filepath: str):
        data = {
            "codigo": self.codigo,
            "itens": [i.to_dict() for i in self.itens]
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    r = RomaneioCarga("ROM-001")
    r.adicionar_item(ItemCarga("Caixas de Ferramentas", 150.0))
    print("Romaneio pronto com", len(r.itens), "item.")
