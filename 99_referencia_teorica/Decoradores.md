---
tags: [python312, decoradores, metaprogramacao, avançado]
---
# 🐍 Referência Técnica Avançada — Decoradores & Closures em Python 3.12

## 📌 1. Conceito Fundamental (Functions as First-Class Citizens)
Em Python, funções são objetos de primeira classe. Elas podem ser passadas como argumentos, atribuídas a variáveis e retornadas por outras funções.

Um **decorador** é uma função que aceita outra função como argumento e estende seu comportamento sem modificar explicitamente seu código fonte.

---

## 📌 2. Closures & Decorador Simples
```python
import functools
import time
from typing import Callable, Any

def cronometrar(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)  # Preserva nome e docstring da função original
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()
        print(f"⏱️ [{func.__name__}] Executado em {(fim - inicio) * 1000:.2f}ms")
        return resultado
    return wrapper

@cronometrar
def processar_lote_dados(tamanho: int) -> list[int]:
    return [x ** 2 for x in range(tamanho)]

# Uso:
processar_lote_dados(100_000)
```

---

## 📌 3. Decoradores com Parâmetros
Para criar um decorador que aceita argumentos próprios (ex: `@retry(tentativas=3)`):

```python
def retry(max_tentativas: int = 3, delay: float = 1.0):
    def decorador(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for tentativa in range(1, max_tentativas + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f"⚠️ Tentativa {tentativa}/{max_tentativas} falhou: {err}")
                    if tentativa == max_tentativas:
                        raise err
                    time.sleep(delay)
        return wrapper
    return decorador

@retry(max_tentativas=3, delay=0.5)
def conectar_banco_dados():
    raise ConnectionError("Falha temporária de conexão no servidor.")
```
