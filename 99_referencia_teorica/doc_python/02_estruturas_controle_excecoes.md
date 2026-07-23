---
tags: [python312, controle, condicionais, loops, excecoes]
---
# 📘 02. Estruturas de Controle e Exceções (Python 3.12 / 3.13)

## 📌 1. Condicionais (`if`, `elif`, `else`)
```python
estoque = 15

if estoque == 0:
    print("❌ Produto Esgotado")
elif estoque < 10:
    print("⚠️ Estoque Baixo")
else:
    print("✅ Estoque Ok")
```

---

## 📌 2. Loops (`for`, `while`, `enumerate`, `zip`)
```python
produtos = ["Caixa A", "Caixa B", "Caixa C"]
quantidades = [10, 25, 5]

for idx, (prod, qtd) in enumerate(zip(produtos, quantidades), start=1):
    print(f"Item #{idx}: {prod} -> {qtd} unidades")
```

---

## 📌 3. Tratamento de Exceções (`try`, `except`, `finally`)
```python
try:
    resultado = 100 / quantidade_informada
except ZeroDivisionError as err:
    print(f"❌ Erro de divisão por zero: {err}")
except ValueError as err:
    print(f"❌ Valor numérico inválido: {err}")
finally:
    print("🔄 Processo finalizado com segurança.")
```
