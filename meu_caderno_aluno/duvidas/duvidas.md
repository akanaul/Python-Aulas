---
sticker: "❓"
---
# ❓ Minha Central de Dúvidas

> [!TIP]
> Pressione `Alt+N` e use o **Template de Dúvida de Estudo** para registrar novas dúvidas nesta pasta.

```dataview
TABLE file.ctime AS "Data", tags AS "Tags"
FROM "meu_caderno_aluno/duvidas"
WHERE file.name != "duvidas"
SORT file.ctime DESC
```
