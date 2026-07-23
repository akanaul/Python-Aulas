---
tags: [python312, funcoes, type-hints, pep695]
---
# 📘 04. Funções, Type Hints Modernos e PEP 695 (Python 3.12 / 3.13)

## 📌 1. Declaração de Funções com Type Hints
```python
def calcular_frete(peso_kg: float, distancia_km: float, taxa_base: float = 15.0) -> float:
    """Calcula o valor total do frete baseado em peso e distância."""
    return taxa_base + (peso_kg * 0.5) + (distancia_km * 0.8)
```

---

## 📌 2. Nova Sintaxe de Tipos Genericos (PEP 695 no Python 3.12+)
O Python 3.12 introduziu a palavra-chave `type` para criar aliases de tipo limpos e genéricos sem precisar importar `TypeVar` de `typing`:

```python
# Alias de tipo moderno no Python 3.12+
type RegistroID = int | str
type ListaDeDados[T] = list[T]

def extrair_primeiro[T](items: list[T]) -> T:
    return items[0]
```
