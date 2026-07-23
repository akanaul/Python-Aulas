---
tags: [python312, estruturas-dados, listas, dicionarios, tuplas, conjuntos]
---
# 📘 03. Estruturas de Dados Modernas (Python 3.12 / 3.13)

## 📌 1. Listas e List Comprehensions
Listas são sequências mutáveis e ordenadas.

```python
veiculos = ["Caminhão 01", "Van 02", "Carreta 03"]

# Adicionar e Remover
veiculos.append("VUC 04")
veiculos.remove("Van 02")

# List Comprehension Moderna
veiculos_maiusculos = [v.upper() for v in veiculos if "Caminhão" in v]
```

---

## 📌 2. Dicionários e Dict Comprehensions
Dicionários armazenam pares chave-valor otimizados por tabela hash.

```python
motorista = {
    "id": 101,
    "nome": "Carlos Silva",
    "rotas_concluidas": 48,
    "ativo": True
}

# Obter valor com fallback seguro (get)
status_str = motorista.get("status", "desconhecido")

# Dict Comprehension
precos_com_desconto = {item: preco * 0.9 for item, preco in {"pneu": 500, "oleo": 120}.items()}
```

---

## 📌 3. Tuplas (Imutáveis) e NamedTuples
```python
# Tupla simples (imutável)
coordenada = (-23.5505, -46.6333)

# Desempacotamento moderno (Unpacking)
lat, lng = coordenada
```

---

## 📌 4. Conjuntos (Sets — Elementos Únicos)
```python
# Remoção automática de duplicatas
codigos_brutos = [101, 102, 101, 103, 102, 104]
codigos_unicos = set(codigos_brutos) # {101, 102, 103, 104}

# Operações de conjunto (Interseção, União)
rotas_sp = {"R-01", "R-02", "R-03"}
rotas_rj = {"R-03", "R-04", "R-05"}

rotas_comuns = rotas_sp & rotas_rj # {'R-03'}
```
