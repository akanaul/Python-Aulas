# 📇 Central de Flashcards & Active Recall (Spaced Repetition)

Bem-vindo(a) à **Central de Flashcards e Revisão Espaçada**! Aqui você pratica a retenção de longo prazo dos conceitos de Python, IA e Automação através do plugin `obsidian-spaced-repetition`.

> [!TUTOR] Como Funciona a Revisão Espaçada?
> O plugin identifica perguntas e respostas com a tag `#flashcard` ou blocos de texto oculto com `==omissão de texto==` (cloze deletion). Ele agenda revisões diárias nos intervalos ideais para fixar o conhecimento na sua memória sem decoreba!

---

## 📇 Flashcards de Fixação Rápida

### Python Essencial
Qual é a diferença entre uma Lista `[ ]` e uma Tupla `( )` em Python? #flashcard/python
?
Listas são ==mutáveis== (podem ser alteradas após a criação), enquanto Tuplas são ==imutáveis== (seus valores não mudam).

Como converter uma string `"123"` para um número inteiro em Python? #flashcard/python
?
Utiliza-se a função nativa ==`int("123")`==.

---

### Automação & Arquivos
Qual biblioteca nativa do Python é recomendada para manipular caminhos de arquivos de forma multiplataforma? #flashcard/automacao
?
A biblioteca ==`pathlib`== (ex: `from pathlib import Path`).

O que significa a sigla TDD em desenvolvimento de software? #flashcard/automacao
?
==Test-Driven Development== (Desenvolvimento Guiado por Testes).

---

### IA & Engenharia de Prompt
O que é o conceito de Vibe Coding Ético? #flashcard/prompt
?
É usar assistentes de IA como copilotos de produtividade mantendo a ==supervisão humana, entendimento do código e responsabilidade sobre os testes==.

---

## 📊 Tabela Dinâmica de Cartões Cadastrados (Dataview)

```dataview
TABLE file.folder AS "Módulo", tags AS "Tags de Revisão"
FROM #flashcard OR #flashcard/python OR #flashcard/automacao OR #flashcard/prompt
SORT file.name ASC
```
