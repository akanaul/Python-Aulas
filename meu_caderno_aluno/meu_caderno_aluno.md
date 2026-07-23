---
sticker: "📓"
tags:
  - moc
  - caderno
  - aluno
---
# 📓 Meu Caderno de Estudos — Espaço do Aluno

> [!TUTOR] Seu Espaço Pessoal no Vault
> Esta pasta foi criada exclusivamente para guardar as suas anotações pessoais, dúvidas sanadas pelo agente, registros de erros e diários de progresso.

---

## ⚡ Como Criar Novas Notas Rapidamente?

Pressione `Alt + N` no teclado para abrir o Templater e escolha o modelo desejado:
1. **Template de Dúvida** -> Salva em `duvidas/` com tags Dataview
2. **Template de Diagnóstico de Erro** -> Salva em `diagnostico_erros/` com `#flashcard`
3. **Template de Anotação de Aula** -> Salva em `anotacoes_aulas/` com `python run`
4. **Template de Exercício Resolvido** -> Salva a solução aprovada

---

## 📁 Painéis Dinâmicos do Caderno (Dataview)

### ❓ Minhas Dúvidas
```dataview
TABLE created AS "Data", status AS "Status"
FROM "meu_caderno_aluno/duvidas"
SORT created DESC
```

### 🚑 Diagnósticos de Erro
```dataview
TABLE created AS "Data", issue AS "Issue"
FROM "meu_caderno_aluno/diagnostico_erros"
SORT created DESC
```
