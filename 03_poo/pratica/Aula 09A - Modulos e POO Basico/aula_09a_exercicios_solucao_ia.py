"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 09A
Programação Orientada a Objetos: Classes, Objetos e Encapsulamento
Issue #09a
"""

class Veiculo:
    """Representa um veículo na frota logística."""
    def __init__(self, placa: str, modelo: str, capacidade_kg: float):
        self.placa = placa.upper()
        self.modelo = modelo
        self.capacidade_kg = capacidade_kg
        self._carga_atual_kg = 0.0

    def carregar(self, peso_kg: float) -> bool:
        if self._carga_atual_kg + peso_kg <= self.capacidade_kg:
            self._carga_atual_kg += peso_kg
            return True
        return False

    def obter_carga(self) -> float:
        return self._carga_atual_kg

if __name__ == "__main__":
    v = Veiculo("ABC-1234", "Volvo FH", 15000.0)
    print("Carregado 10t:", v.carregar(10000.0))
    print("Carga atual:", v.obter_carga())
