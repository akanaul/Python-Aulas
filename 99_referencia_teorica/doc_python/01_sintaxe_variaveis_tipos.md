---
tags: [python312, sintaxe, variaveis, tipos]
---
# 📘 01. Sintaxe Básica, Variáveis e Tipos de Dados (Python 3.12 / 3.13)

## 📌 1. Tipos Primitivos Integrados
Em Python, tudo é um objeto. Os tipos primitivos básicos são:

```python
# Inteiros e Flutuantes
idade: int = 28
preco_unitario: float = 49.90

# Textos (Strings UTF-8)
nome_motorista: str = "Carlos Eduardo"

# Booleanos
ativo: bool = True

# Nulo
observacao: str | None = None
```

---

## 📌 2. Conversão de Tipos (Casting)
```python
texto_numero = "150"
quantidade = int(texto_numero)  # 150
valor_decimal = float(quantidade) # 150.0
str_valor = str(valor_decimal) # "150.0"
```

---

## 📌 3. f-strings Avançadas no Python 3.12+
No Python 3.12+, as f-strings permitem reusar aspas internas e colocar expressões complexas sem erro de sintaxe:

```python
dados = {"nome": "Caminhão 01", "capacidade": 12000}
# Aspas duplas permitidas dentro da f-string no Python 3.12+
status_fmt = f"Veículo: {dados['nome']} com capacidade de {dados['capacidade'] / 1000:.1f}t"
print(status_fmt)
```
