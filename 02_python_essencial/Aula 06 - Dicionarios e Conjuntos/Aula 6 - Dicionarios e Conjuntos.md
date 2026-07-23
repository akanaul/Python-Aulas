---
aliases: ["Aula 6 — Dicionários e Conjuntos"]
tags: [aula, bloco-2, python]
---

> 💡 **O que você vai aprender:** Como armazenar dados estruturados usando Dicionários (chave-valor) e garantir unicidade em alta velocidade usando Conjuntos (Sets).
> ⏱️ **Duração estimada:** 2h | 📅 **Bloco:** 2

---

## 🎯 Objetivos da Aula
- Mapear dados do mundo real com Dicionários (`{chave: valor}`).
- Entender os métodos vitais `.keys()`, `.values()`, `.items()`.
- Usar Conjuntos (`set`) para remover duplicidades de listas.
- Realizar operações de Teoria dos Conjuntos (União, Intersecção).

---

## 🔗 Conexão com os Projetos Reais
> 💼 **AutoMDFText:** Usamos dicionários para organizar os parâmetros da interface, como `{"x": 100, "y": 200, "texto": "1234"}`.
> 📊 **AutoPickingPy:** Dicionários mapeiam colunas do Excel, ex: `{"A": "Nome", "B": "Qtd"}`.

---

## 📖 Conceito
Dicionários são como as **Etiquetas de Identificação do Palete (SSCC)**: você lê a chave (código de barras) e o sistema te devolve o valor (conteúdo, peso, destino).
Conjuntos (Sets) são como o **Filtro da Portaria**: não importa quantas vezes o mesmo caminhão passe na câmera, o relatório do Set registrará a placa dele apenas UMA vez (único). Eles não têm ordem, mas garantem a não-duplicação.

---

## 💻 Exemplos

### Exemplo 1 — Básico (Dicionários)

```python
# Cadastro de um Caminhão
truck_info = {
    "plate": "XYZ-9090",
    "driver": "Ana Maria",
    "capacity_ton": 15
}

print(truck_info["driver"]) # Acessa pelo nome da chave
```

### Exemplo 2 — Aplicado à Logística (Dicionários avançados e Sets)

```python
# Sets removendo SKUs duplicados bipados por engano no WMS
scanned_skus = ["A1", "B2", "A1", "C3", "B2"]
unique_skus = set(scanned_skus)
print(f"Bipagens únicas: {unique_skus}") # {'A1', 'C3', 'B2'}

# Intersecção de rotas (quais cidades duas transportadoras atendem em comum?)
route_transp_A = {"SP", "RJ", "MG", "ES"}
route_transp_B = {"MG", "BA", "RJ", "SE"}
common_zones = route_transp_A.intersection(route_transp_B)

print(f"Atendem em comum: {common_zones}")
```

### Exemplo 3 — Com IA (Antigravity)
> 🤖 **Prompt sugerido:**
> "Como criar um dicionário aninhado (dicionário dentro de dicionário) para representar o layout de um armazém (Rua, Prédio, Nível)? Explique como acessar o 'Nível 3' da 'Rua A'."

---

## 📋 Referência Rápida
| Estrutura | Criação | Acesso / Uso |
|---|---|---|
| Dict | `d = {"id": 1}` | `d["id"]`, `d.get("id")` |
| Set | `s = {1, 2, 3}` | `s.add(4)`, `s.remove(2)` |
| Iterar Dict | `.items()` | `for k, v in d.items():` |
| Set União | `a \| b` ou `a.union(b)` | Une tudo sem repetir |

---

## ⚠️ Erros Comuns
| Erro | Causa | Solução |
|---|---|---|
| KeyError | Tentar acessar chave que não existe | Use `dict.get("chave", "Padrao")` |
| Set Erro | Achar que Set tem ordem | Nunca use `set[0]`. Sets não têm índice numérico. |

---

## 🏋️ Exercícios
> 📁 Arquivo de prática: `exercicios/aula_06_exercicios.py`

**Exercício 1 — [Nível: Básico]**
Crie um dicionário com o perfil do motorista: nome, idade, e se tem licença MOPP.

**Exercício 2 — [Nível: Intermediário]**
Dada uma lista cheia de números de notas fiscais repetidos, converta para `set` para extrair apenas as notas únicas e conte quantas são.

**Exercício 3 — [Nível: Desafio]**
Crie um dicionário com o estoque de 3 produtos. Use um `for` com `.items()` para imprimir "O produto {nome} tem {qtd} unidades no estoque".

---

## 🎯 Conexão com a Próxima Aula
Agora que estruturamos dados perfeitos, nossos códigos vão começar a ficar grandes. Na próxima aula, aprenderemos Funções (para modularizar), além dos superpoderosos Decoradores e Geradores do Python!

---
#aula #bloco-2 #python
