---
tags: [python312, geradores, yield, memoria, eficiencia]
---
# 🐍 Referência Técnica Avançada — Geradores & Expressões Geradoras

## 📌 1. Por que usar Geradores? (Avaliação Preguiçosa / Lazy Evaluation)
Geradores produzem itens um por um sob demanda (streaming), consumindo **$O(1)$ de memória RAM**, ao contrário de listas que carregam todos os elementos na memória ($O(N)$).

---

## 📌 2. Comparativo de Consumo de Memória
```python
import sys

# Lista de 1 milhão de inteiros (aloca ~8 MB de RAM na memória)
lista = [x for x in range(1_000_000)]
print(f"Tamanho da Lista: {sys.getsizeof(lista) / 1024 / 1024:.2f} MB")

# Gerador equivalente (aloca ~200 Bytes fixos de RAM)
gerador = (x for x in range(1_000_000))
print(f"Tamanho do Gerador: {sys.getsizeof(gerador)} Bytes")
```

---

## 📌 3. Funções Geradoras com `yield`
```python
from typing import Generator

def ler_arquivo_gigante_em_blocos(caminho: str, tamanho_bloco: int = 1024) -> Generator[str, None, None]:
    """Lê um arquivo extenso em blocos sem estourar a memória RAM."""
    with open(caminho, mode="r", encoding="utf-8") as f:
        while True:
            bloco = f.read(tamanho_bloco)
            if not bloco:
                break
            yield bloco
```
