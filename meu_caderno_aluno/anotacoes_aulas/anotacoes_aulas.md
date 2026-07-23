---
sticker: "📝"
---
# 📝 Minhas Anotações de Aulas

> [!TIP]
> Pressione `Alt+N` e use o **Template de Anotação do Aluno** para adicionar novas notas nesta pasta.

```dataview
TABLE file.ctime AS "Criado Em", tags AS "Tags"
FROM "meu_caderno_aluno/anotacoes_aulas"
WHERE file.name != "anotacoes_aulas"
SORT file.ctime DESC
```
