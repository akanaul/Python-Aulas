---
aliases: ["Aula 2 — Variáveis e Operadores"]
tags: [aula, bloco-1, python]
---

> 💡 **O que você vai aprender:** Como armazenar dados e usar os operadores (aritméticos, de atribuição, comparação, lógicos, identidade e associação) para tomar decisões logísticas.
> ⏱️ **Duração estimada:** 2h | 📅 **Bloco:** 1

---

## 🎯 Objetivos da Aula
- Dominar os tipos primitivos (int, float, str, bool).
- Utilizar todos os grupos de operadores do Python.
- Aplicar regras de identidade (`is`) e associação (`in`).

---

## 🔗 Conexão com os Projetos Reais
> 💼 **AutoMDFText:** Operadores lógicos validam se os campos do formulário estão preenchidos antes de enviar os dados.
> 📊 **AutoPickingPy:** Operadores aritméticos são usados para calcular o saldo de estoque ao alocar produtos.

---

## 📖 Conceito
Variáveis são como as **gaiolas** ou **paletes** onde guardamos a mercadoria. Dependendo do que é (líquido, sólido, inflamável), usamos um tipo diferente (int para caixas, float para peso).
Os **Operadores** são como as empilhadeiras e balanças: eles somam cargas, comparam pesos máximos permitidos e verificam se uma caixa pertence a um lote específico.

---

## 💻 Exemplos

### Exemplo 1 — Básico

```python
# Aritméticos e Atribuição
boxes = 150
boxes += 50  # Recebimento de mais 50
print(boxes) # 200
```

### Exemplo 2 — Aplicado à Logística

```python
# Comparação, Lógicos, Identidade e Associação
max_weight = 12000.0
current_weight = 11500.5
is_overweight = current_weight > max_weight

truck_status = "loaded"
can_dispatch = not is_overweight and truck_status == "loaded"

restricted_zones = ["Z-SP", "Z-RJ", "Z-MG"]
destination = "Z-RJ"
needs_special_permit = destination in restricted_zones # Associação (in)

print(f"Dispatch authorized? {can_dispatch}")
print(f"Special permit? {needs_special_permit}")
```

### Exemplo 3 — Com IA (Antigravity)
> 🤖 **Prompt sugerido:**
> "Quais são as diferenças de performance entre usar `==` e o operador de identidade `is` em Python para comparar variáveis?"

---

## 📋 Referência Rápida
| Grupo | Operadores | Exemplo |
|---|---|---|
| Aritméticos | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `total = a + b` |
| Atribuição | `=`, `+=`, `-=`, `*=` | `stock += 10` |
| Comparação | `==`, `!=`, `>`, `<`, `>=`, `<=` | `weight > 100` |
| Lógicos | `and`, `or`, `not` | `a and not b` |
| Identidade | `is`, `is not` | `status is None` |
| Associação | `in`, `not in` | `"SP" in route` |

---

## ⚠️ Erros Comuns
| Erro | Causa | Solução |
|---|---|---|
| TypeError | Somar string com int (ex: `"5" + 2`) | Converter antes: `int("5") + 2` |
| Confusão | Usar `=` (atribuição) em vez de `==` (comparação) em if | Revise o uso de `==` para testar igualdade. |

---

## 🏋️ Exercícios
> 📁 Arquivo de prática: `exercicios/aula_02_exercicios.py`

**Exercício 1 — [Nível: Básico]**
Crie um programa que calcule o peso total de 3 paletes. Palete 1: 300.5kg, Palete 2: 450.2kg, Palete 3: 200.0kg.

**Exercício 2 — [Nível: Intermediário]**
Use o operador `in` para verificar se a placa "XYZ-1234" está em uma lista de placas liberadas para entrar na doca.

**Exercício 3 — [Nível: Desafio]**
Combine operadores lógicos para determinar se um motorista pode pegar a carga. Regra: O motorista deve ter licença válida (`True`) E o caminhão não pode estar em manutenção (`False`).

---

## 🎯 Conexão com a Próxima Aula
Agora que sabemos verificar condições (maior, menor, igual), vamos aprender a criar fluxos automáticos de decisão e repetição usando `if` e `for/while`, além de conhecer a estrutura `match/case`!

---
#aula #bloco-1 #python


---

## 🔀 Aprendizado Ativo de Git, Issue & Pull Request

> 📌 **Issue Oficial no GitHub:** # Issue #02
> 🔀 **Branch de Desenvolvimento:** git checkout -b feature/issue-02-variaveis-operadores
> 📁 **Arquivo de Trabalho (Manual):** aula_02_exercicios_manual.py
> 🧪 **Teste Automatizado & Pré-Aprovação IA:** python avaliar_exercicio.py --issue 02
> 🚀 **Envio de Pull Request (PR):** git push origin feature/issue-02-variaveis-operadores e abra o PR no GitHub para a revisão final do Tutor (@akanaul)!
