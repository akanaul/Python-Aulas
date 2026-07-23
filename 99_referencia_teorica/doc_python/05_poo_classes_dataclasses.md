---
tags: [python312, poo, classes, dataclasses]
---
# 📘 05. Programação Orientada a Objetos e Dataclasses (Python 3.12 / 3.13)

## 📌 1. Classe Tradicional com Encapsulamento
```python
class Motorista:
    def __init__(self, nome: str, cnh: str, ativo: bool = True) -> None:
        self.nome = nome
        self._cnh = cnh  # Atributo protegido
        self.ativo = ativo

    def desativar(self) -> None:
        self.ativo = False
```

---

## 📌 2. Modern `@dataclass` (Boilerplate-free Data Containers)
```python
from dataclasses import dataclass, field

@dataclass(slots=True) # slots=True otimiza memória no Python 3.10+
class Veiculo:
    placa: str
    modelo: str
    capacidade_kg: float
    manutencoes: list[str] = field(default_factory=list)

    def adicionar_manutencao(self, item: str) -> None:
        self.manutencoes.append(item)
```
