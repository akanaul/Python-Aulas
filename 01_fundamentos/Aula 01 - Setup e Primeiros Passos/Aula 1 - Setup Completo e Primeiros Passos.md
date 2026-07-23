---
aliases: ["Aula 1 — Setup Completo e Primeiros Passos"]
tags: [aula, bloco-1, python]
---

> 💡 **O que você vai aprender:** Como configurar seu ambiente de desenvolvimento, usar o VSCode, e rodar seus primeiros comandos Python seguindo as boas práticas do PEP 8.
> ⏱️ **Duração estimada:** 2h | 📅 **Bloco:** 1

---

## 🎯 Objetivos da Aula
- Instalar e configurar o Python e VSCode.
- Entender a importância da indentação e PEP 8.
- Escrever o clássico "Hello, World!" com contexto logístico.
- Conhecer a Antigravity (nossa IA copiloto).

---

## 🔗 Conexão com os Projetos Reais
> 💼 **AutoMDFText:** A estrutura básica do script e organização das pastas que veremos hoje é a mesma usada para organizar os arquivos de texto e logs do robô.
> 📊 **AutoPickingPy:** Usaremos o VSCode configurado hoje para ler e manipular as planilhas de picking no futuro.

---

## 📖 Conceito
Pense no **Setup do Python** como a preparação de uma doca para recebimento de carretas. Se o pátio não estiver sinalizado (VSCode configurado) e as regras não estiverem claras (PEP 8), os caminhões (códigos) vão bater ou descarregar errado.
**PEP 8** é o manual de operações da doca. Ele diz como os nomes de variáveis devem ser escritos, quantos espaços usar e como manter tudo organizado.

---

## 💻 Exemplos

### Exemplo 1 — Básico

```python
# Saudação inicial para o operador
print("Hello, Logistics!")
```

### Exemplo 2 — Aplicado à Logística e PEP 8

```python
# Seguindo a PEP 8 (snake_case para variáveis)
driver_name = "João Silva"
truck_plate = "ABC-1234"
route_active = True

print(f"Driver {driver_name} with truck {truck_plate} is ready for dispatch.")
```

### Exemplo 3 — Com IA (Antigravity)
> 🤖 **Prompt sugerido:**
> "Como configurar o VSCode para formatar automaticamente meu código Python seguindo as regras do PEP 8 usando o Black?"

---

## 📋 Referência Rápida
| Conceito | Sintaxe / Regra | Exemplo |
|---|---|---|
| Print | `print()` | `print("Hello")` |
| PEP 8 (Variáveis) | snake_case | `delivery_status = "pending"` |
| PEP 8 (Constantes) | UPPER_CASE | `MAX_WEIGHT = 5000` |

---

## ⚠️ Erros Comuns
| Erro | Causa | Solução |
|---|---|---|
| IndentationError | Espaços irregulares (ex: misturar tab e espaço) | Use sempre 4 espaços no VSCode |
| SyntaxError | Faltou parênteses no print | Verifique o fechamento: `print(...)` |

---

## 🏋️ Exercícios
> 📁 Arquivo de prática: `exercicios/aula_01_exercicios.py`

**Exercício 1 — [Nível: Básico]**
Crie um script que imprima o nome da sua transportadora fictícia e o status do sistema.

**Exercício 2 — [Nível: Intermediário]**
Declare variáveis usando as regras do PEP 8 para representar a placa de um veículo, o nome do motorista e se ele está em rota. Imprima essas variáveis.

**Exercício 3 — [Nível: Desafio]**
Crie um mini-relatório usando `print()` para desenhar um cabeçalho simples usando caracteres como `-` e `|`.

---

## 🎯 Conexão com a Próxima Aula
Na próxima aula, vamos entender como armazenar informações (variáveis) de forma mais profunda e como fazer operações matemáticas com elas (peso de carga, cubagem, etc.).

---
#aula #bloco-1 #python


---

## 🔀 Aprendizado Ativo de Git, Issue & Pull Request

> 📌 **Issue Oficial no GitHub:** # Issue #01
> 🔀 **Branch de Desenvolvimento:** git checkout -b feature/issue-01-setup-passos
> 📁 **Arquivo de Trabalho (Manual):** aula_01_exercicios_manual.py
> 🧪 **Teste Automatizado & Pré-Aprovação IA:** python avaliar_exercicio.py --issue 01
> 🚀 **Envio de Pull Request (PR):** git push origin feature/issue-01-setup-passos e abra o PR no GitHub para a revisão final do Tutor (@akanaul)!

---

## 📝 Anotações Pessoais do Aluno sobre esta Aula

> [!TIP] **Criar Nota de Estudo Relacionada**
> Quer guardar resumos ou anotações próprias sobre esta aula?
> Pressione Alt + N no Templater e selecione **Template de Anotação do Aluno** para salvar automaticamente em [[meu_caderno_aluno/anotacoes_aulas/anotacoes_aulas|meu_caderno_aluno/anotacoes_aulas/]]!
