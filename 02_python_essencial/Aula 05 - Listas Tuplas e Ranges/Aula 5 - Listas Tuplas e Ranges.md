---
aliases: ["Aula 5 — Listas, Tuplas e Ranges"]
tags: [aula, bloco-2, python]
---

> 💡 **O que você vai aprender:** Como agrupar vários itens (SKUs, placas, valores), diferenciar listas de tuplas e usar iteradores nativos (`iter()`, `next()`) para controle avançado.
> ⏱️ **Duração estimada:** 2h | 📅 **Bloco:** 2

---

## 🎯 Objetivos da Aula
- Dominar as Listas (mutáveis) e seus métodos (`append`, `pop`, `sort`).
- Entender Tuplas (imutáveis) para dados que não podem mudar.
- Gerar sequências com `range()`.
- Compreender o conceito profundo de Iteradores no Python.

---

## 🔗 Conexão com os Projetos Reais
> 💼 **AutoMDFText:** Tuplas podem guardar as credenciais imutáveis do sistema, enquanto Listas guardam os números de manifesto a processar.
> 📊 **AutoPickingPy:** Ao ler linhas do Excel, extraímos os dados em formato de listas e iteramos sobre elas.

---

## 📖 Conceito
Listas são **Gaiolas de Picking**: você pode colocar caixas novas (`append`), tirar caixas (`pop`), ou reordenar tudo (`sort`).
Tuplas são **Containers Lacrados**: uma vez que você fechou e colocou o lacre, os itens lá dentro não mudam de lugar nem podem ser retirados (ideal para segurança e performance).
Iteradores (`iter` e `next`) são como a **Pistola de Leitura Bipadora**: eles processam um item da lista por vez, controlando quem é o "próximo".

---

## 💻 Exemplos

### Exemplo 1 — Básico (Listas e Tuplas)

```python
# Lista de SKUs (Pode mudar)
picking_list = ["SKU-001", "SKU-002", "SKU-003"]
picking_list.append("SKU-004") 
print(picking_list)

# Tupla de Coordenadas de Centro de Distribuição (Não muda)
cd_coordinates = (-23.5505, -46.6333)
# cd_coordinates[0] = -24.0 -> Vai gerar erro! (Tupla é imutável)
```

### Exemplo 2 — Aplicado à Logística (Iteradores e Range)

```python
# Range gerando portas de docas de 1 a 5
docas = list(range(1, 6))

# Usando iterador manual (como se fosse a pistola de bipe)
estoque = ["Palete A", "Palete B", "Palete C"]
bipador = iter(estoque)

print("Bipe 1:", next(bipador)) # Palete A
print("Bipe 2:", next(bipador)) # Palete B
```

### Exemplo 3 — Com IA (Antigravity)
> 🤖 **Prompt sugerido:**
> "Qual a diferença de performance entre Listas e Tuplas no Python? Explique como os iteradores (`next()`) ajudam a processar arquivos gigantes de estoque sem estourar a memória (RAM)."

---

## 📋 Referência Rápida
| Estrutura | Sintaxe | Característica |
|---|---|---|
| Lista | `[1, 2, 3]` | Mutável, métodos ricos |
| Tupla | `(1, 2, 3)` | Imutável, rápida, segura |
| Range | `range(10)` | Gera sequências numéricas |
| Iterator| `iter()`, `next()`| Consome elemento um por um |

---

## ⚠️ Erros Comuns
| Erro | Causa | Solução |
|---|---|---|
| StopIteration | Usar `next()` quando a lista já acabou | Tratar com try/except ou usar for-loop (que faz isso sozinho) |
| TypeError (Tuple) | Tentar alterar um item da tupla | Use Lista se os dados precisarem mudar |

---

## 🏋️ Exercícios
> 📁 Arquivo de prática: `exercicios/aula_05_exercicios.py`

**Exercício 1 — [Nível: Básico]**
Crie uma lista de 3 transportadoras. Adicione mais uma no final e remova a primeira.

**Exercício 2 — [Nível: Intermediário]**
Use o `range()` para imprimir os números de 10 a 0 em ordem decrescente (contagem regressiva para despacho).

**Exercício 3 — [Nível: Desafio]**
Crie um iterador (`iter()`) para uma lista de 3 pedidos pendentes e chame `next()` manualmente, imprimindo uma mensagem de "Pedido processado" a cada chamada.

---

## 🎯 Conexão com a Próxima Aula
Agora que você sabe agrupar dados simples, vamos elevar o nível. E se precisarmos associar "Chave da NFe" -> "Valor"? Para isso, conheceremos os incríveis Dicionários e Conjuntos (Sets).

---
#aula #bloco-2 #python


---

## 🔀 Aprendizado Ativo de Git, Issue & Pull Request

> 📌 **Issue Oficial no GitHub:** # Issue #05
> 🔀 **Branch de Desenvolvimento:** git checkout -b feature/issue-05-listas-tuplas
> 📁 **Arquivo de Trabalho (Manual):** aula_05_exercicios_manual.py
> 🧪 **Teste Automatizado & Pré-Aprovação IA:** python avaliar_exercicio.py --issue 05
> 🚀 **Envio de Pull Request (PR):** git push origin feature/issue-05-listas-tuplas e abra o PR no GitHub para a revisão final do Tutor (@akanaul)!

---

## 📝 Anotações Pessoais do Aluno sobre esta Aula

> [!TIP] **Criar Nota de Estudo Relacionada**
> Quer guardar resumos ou anotações próprias sobre esta aula?
> Pressione Alt + N no Templater e selecione **Template de Anotação do Aluno** para salvar automaticamente em [[meu_caderno_aluno/anotacoes_aulas/anotacoes_aulas|meu_caderno_aluno/anotacoes_aulas/]]!
