---
sticker: "📈"
---
# 📈 Meu Diário de Progresso Pessoal

> [!TIP]
> Pressione `Alt+N` e use o **Template de Diário de Progresso** para planejar metas semanais nesta pasta.

```dataview
TABLE file.ctime AS "Data", tags AS "Tags"
FROM "meu_caderno_aluno/diario_progresso"
WHERE file.name != "diario_progresso"
SORT file.ctime DESC
```
