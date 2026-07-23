---
aliases: ["Aula 4 — Strings e Formatação"]
tags: [aula, bloco-2, python]
---

> 💡 **O que você vai aprender:** Como manipular textos, fatiar informações (slicing) e usar Formatação Avançada de f-strings (f"{val:.2f}", alinhamentos, datas) no Python 3.12+.
> ⏱️ **Duração estimada:** 2h | 📅 **Bloco:** 2

---

## 🎯 Objetivos da Aula
- Extrair informações de chaves de NFe usando índices e slicing.
- Dominar f-strings avançadas (novidades de alinhamento e formatação de números).
- Conhecer métodos de string úteis como `.strip()`, `.upper()`, `.replace()`.

---

## 🔗 Conexão com os Projetos Reais
> 💼 **AutoMDFText:** A formatação de strings é usada para construir os comandos do teclado (por ex., formatando a placa para maiúsculo antes de digitar).
> 📊 **AutoPickingPy:** Slicing ajuda a extrair o número do pedido e o código do produto que vêm grudados nas células do Excel.

---

## 📖 Conceito
Strings (textos) são como **cargas fracionadas**. Muitas vezes recebemos uma informação gigante (ex: Chave da NFe com 44 dígitos) e precisamos "fatiar" para separar UF, CNPJ e número.
As **f-strings** são os **Etiquetadores Automáticos**: eles colocam os dados nas caixas do jeito certinho que o cliente quer, alinhado, com casas decimais formatadas e data padrão.

---

## 💻 Exemplos

### Exemplo 1 — Básico (Slicing)

```python
# Chave NFe fictícia
nfe_key = "35230912345678000199550010009998881234567890"

uf_code = nfe_key[0:2] # Pega '35' (SP)
doc_model = nfe_key[20:22] # Pega '55'

print(f"UF: {uf_code}, Modelo: {doc_model}")
```

### Exemplo 2 — Aplicado à Logística (F-strings Avançadas)

```python
import datetime

driver = "carlos alberto"
freight_cost = 1450.8
delivery_date = datetime.datetime.now()

# Formatação Avançada (alinhamento, moedas e datas)
print(f"Motorista: {driver.title():<20} | Status: Ativo") 
# :<20 garante alinhamento de 20 espaços à esquerda
print(f"Custo do Frete: R$ {freight_cost:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")) 
# Novidade nas f-strings: aceitam expressões mais complexas internamente
print(f"Data de Expedição: {delivery_date:%d/%m/%Y às %H:%M}")
```

### Exemplo 3 — Com IA (Antigravity)
> 🤖 **Prompt sugerido:**
> "Quais são as novidades de formatação das f-strings no Python 3.12? Como posso usá-las para criar um relatório tabular de estoque bem alinhado?"

---

## 📋 Referência Rápida
| Recurso | Sintaxe | Exemplo |
|---|---|---|
| Slicing | `string[inicio:fim]` | `nfe[0:2]` |
| Uppercase/Lowercase | `.upper()` / `.lower()` | `"placa".upper()` |
| Remover espaços | `.strip()` | `"  dado  ".strip()` |
| Casas Decimais | `f"{valor:.2f}"` | `f"{10.5:.2f}" -> 10.50` |
| Alinhamento | `f"{texto:>10}"` | `Alinha à direita` |

---

## ⚠️ Erros Comuns
| Erro | Causa | Solução |
|---|---|---|
| IndexError | Tentar acessar posição que não existe | Verifique o tamanho com `len(string)` |
| Confusão f-string | Esquecer o `f` antes das aspas | Sempre inicie com `f"texto {var}"` |

---

## 🏋️ Exercícios
> 📁 Arquivo de prática: `exercicios/aula_04_exercicios.py`

**Exercício 1 — [Nível: Básico]**
Dada a string `codigo = "  PROD-999-BR  "`, limpe os espaços laterais e troque "BR" por "US".

**Exercício 2 — [Nível: Intermediário]**
A partir do texto `placa_veiculo = "ABC1234"`, extraia as letras (posição 0 a 3) e os números (posição 3 em diante) usando slicing.

**Exercício 3 — [Nível: Desafio]**
Crie uma variável para nome de produto, outra para valor unitário e outra para quantidade. Imprima uma linha de cupom fiscal usando f-strings para alinhar o nome do produto e formatar o valor total com 2 casas decimais.

---

## 🎯 Conexão com a Próxima Aula
Com os textos dominados, está na hora de aprender a transportar MÚLTIPLOS itens de uma vez. Veremos Listas, Tuplas, Ranges e a magia dos Iteradores!

---
#aula #bloco-2 #python


---

## 🔀 Aprendizado Ativo de Git, Issue & Pull Request

> 📌 **Issue Oficial no GitHub:** # Issue #04
> 🔀 **Branch de Desenvolvimento:** git checkout -b feature/issue-04-strings-formatacao
> 📁 **Arquivo de Trabalho (Manual):** aula_04_exercicios_manual.py
> 🧪 **Teste Automatizado & Pré-Aprovação IA:** python avaliar_exercicio.py --issue 04
> 🚀 **Envio de Pull Request (PR):** git push origin feature/issue-04-strings-formatacao e abra o PR no GitHub para a revisão final do Tutor (@akanaul)!

---

## 📝 Anotações Pessoais do Aluno sobre esta Aula

> [!TIP] **Criar Nota de Estudo Relacionada**
> Quer guardar resumos ou anotações próprias sobre esta aula?
> Pressione Alt + N no Templater e selecione **Template de Anotação do Aluno** para salvar automaticamente em [[meu_caderno_aluno/anotacoes_aulas/anotacoes_aulas|meu_caderno_aluno/anotacoes_aulas/]]!
