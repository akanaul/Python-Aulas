---
aliases: ["Aula 3 — Condicionais e Loops"]
tags: [aula, bloco-1, python]
---

> 💡 **O que você vai aprender:** Como criar regras de decisão usando if/else, estruturar repetições (for/while) e aplicar o poderoso Pattern Matching (`match/case`) do Python 3.10+.
> ⏱️ **Duração estimada:** 2h | 📅 **Bloco:** 1

---

## 🎯 Objetivos da Aula
- Dominar fluxos condicionais (`if`, `elif`, `else`).
- Entender a sintaxe moderna do `match`/`case` para roteamento de opções.
- Automatizar tarefas repetitivas usando `for` e `while`.
- Controlar loops com `break` e `continue`.

---

## 🔗 Conexão com os Projetos Reais
> 💼 **AutoMDFText:** O `if` é essencial para verificar se um erro ocorreu antes de tentar emitir o manifesto.
> 📊 **AutoPickingPy:** Loops `for` são o motor principal, repetindo a leitura de linhas na planilha de Excel.

---

## 📖 Conceito
Condicionais são como **cancelas e catracas** da portaria: se (if) o caminhão tiver autorização, abre a cancela; senão (else), pede para aguardar.
O `match/case` é como um **Painel de Triagem (Sorter)** que manda cada caixa para uma doca diferente dependendo do estado de destino de forma elegante.
Loops são a **esteira rolante**: passam por cada pacote repetidamente até que o caminhão (lista) esteja vazio.

---

## 💻 Exemplos

### Exemplo 1 — Básico (If/Else)

```python
temperature = -15.0

if temperature < -18.0:
    print("Alerta: Congelador muito frio!")
elif temperature > -10.0:
    print("Alerta: Risco de descongelamento!")
else:
    print("Temperatura da câmara fria normal.")
```

### Exemplo 2 — Aplicado à Logística (Match/Case & For)

```python
delivery_zones = ["Norte", "Sul", "Leste", "Oeste", "Desconhecida"]

for zone in delivery_zones:
    match zone:
        case "Norte":
            print(f"Roteirizando pacote {zone} para Doca A")
        case "Sul" | "Oeste": # Múltiplos casos na mesma linha
            print(f"Roteirizando pacote {zone} para Doca B")
        case "Leste":
            print(f"Roteirizando pacote {zone} para Doca C")
        case _: # Fallback (default)
            print(f"Erro: Zona {zone} não cadastrada. Segregar.")
            continue # Pula para o próximo pacote da esteira
```

### Exemplo 3 — Com IA (Antigravity)
> 🤖 **Prompt sugerido:**
> "Como posso substituir uma cadeia longa de if/elif por match/case no Python 3.12? Me dê um exemplo de validação de status de pedidos (Pendente, Faturado, Entregue)."

---

## 📋 Referência Rápida
| Comando | Uso | Exemplo |
|---|---|---|
| `if` / `elif` / `else` | Desvios condicionais básicos | `if weight > 100:` |
| `match` / `case` | Roteamento avançado de valores | `match status:` |
| `for` | Repetição sobre coleções (listas, etc) | `for item in box:` |
| `while` | Repetição baseada em condição | `while stock > 0:` |
| `break` / `continue`| Controle fino de loops | `if error: break` |

---

## ⚠️ Erros Comuns
| Erro | Causa | Solução |
|---|---|---|
| Loop Infinito | A condição do `while` nunca vira falsa | Garanta que as variáveis mudem dentro do loop (ex: `stock -= 1`) |
| IndentationError | Misturar códigos dentro/fora do if | Alinhe os blocos e use 4 espaços. |

---

## 🏋️ Exercícios
> 📁 Arquivo de prática: `exercicios/aula_03_exercicios.py`

**Exercício 1 — [Nível: Básico]**
Crie um loop que imprima os números das docas de 1 a 10.

**Exercício 2 — [Nível: Intermediário]**
Use um `while` para simular o descarregamento de um caminhão que começa com 50 paletes, removendo 5 por vez até zerar.

**Exercício 3 — [Nível: Desafio]**
Crie um sistema simples com `match/case` que recebe o tipo de veículo ("Moto", "Van", "Truck", "Carreta") e imprime o tipo de carga ideal para cada um.

---

## 🎯 Conexão com a Próxima Aula
Já controlamos o fluxo e repetimos tarefas! Agora vamos aprender a manipular textos avançados, notas fiscais, datas e códigos de barras usando o poder incrível das Strings e Formatações avançadas.

---
#aula #bloco-1 #python
