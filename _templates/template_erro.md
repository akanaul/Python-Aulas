---
tags:
  - diagnostico-erro
  - caderno-aluno
  - flashcard
created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
status: analisado
issue: <% tp.system.prompt("Qual a Issue/Exercício?", "01") %>
---

# 🚑 Diagnóstico de Erro: <% tp.file.title %>

> [!CAUTION] Registro de Depuração Automática
> 📅 **Data:** <% tp.file.creation_date("DD/MM/YYYY HH:mm") %>

## 📌 Causa do Erro Identificada
- **Mensagem / Traceback:**
```text
<% tp.file.cursor() %>
```

## 💡 Dica do Mentor & Solução
- **O que causou o erro:**
- **Como corrigir:**

## 🎴 Flashcard de Sintaxe / Fixação
- **Pergunta:** Como evitar esse erro em Python? #flashcard
- **Resposta:** 
