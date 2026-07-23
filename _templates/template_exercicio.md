---
data: <% tp.date.now("YYYY-MM-DD") %>
exercicio: "<% tp.file.title %>"
issue: "# Issue #XX"
status: pendente
tags: [exercicio, tdd, issue]
---
# <% tp.file.title %>

> [!EXERCICIO] Desafio Prático de Código
> **Issue Git Relacionada:** # Issue #XX
> **Arquivo de Trabalho:** `exercicio_manual.py`

## 🎯 Requisitos da Solução
- [ ] Implementar a função principal solicitada.
- [ ] Passar no teste automatizado: `python avaliar_exercicio.py --issue XX`

## 🔀 Branch Git
```bash
git checkout -b feature/issue-XX-exercicio
```

> [!TUTOR] Dicas do Mentor (Modo Tutor)
> Lembre-se de dividir o problema em pequenas partes antes de escrever o código.
