---
tags:
  - anotacao-aula
  - caderno-aluno
created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
modulo: <% tp.system.prompt("Qual o módulo?", "01_fundamentos") %>
---

# 📝 Anotação de Aula: <% tp.file.title %>

> [!NOTE] Resumo Didático da Aula
> 📅 **Data:** <% tp.file.creation_date("DD/MM/YYYY HH:mm") %>

## 🧠 Conceitos Teóricos Principais
<% tp.file.cursor() %>

## 💻 Snippets & Testes de Código (Execute Code)
```python
# Teste de código executável no Obsidian
print("Aprendendo Python com IA!")
```

## 📚 Referências & Leitura Recomendada
- [[00_hub_referencias_academicas|Hub Central de Referências Acadêmicas]]
