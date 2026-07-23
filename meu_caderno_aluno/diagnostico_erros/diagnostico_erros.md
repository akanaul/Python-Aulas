---
sticker: "🚑"
---
# 🚑 Meu Registro de Diagnóstico de Erros

> [!TIP]
> Pressione `Alt+N` e use o **Template de Diagnóstico de Erro** para registrar bugs e correções nesta pasta.

```dataview
TABLE file.ctime AS "Data do Bug", tags AS "Tags"
FROM "meu_caderno_aluno/diagnostico_erros"
WHERE file.name != "diagnostico_erros"
SORT file.ctime DESC
```
