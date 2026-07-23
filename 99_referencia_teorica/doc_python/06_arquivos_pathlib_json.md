---
tags: [python312, arquivos, pathlib, json, csv]
---
# 📘 06. Manipulação de Arquivos (`pathlib`, CSV, JSON) (Python 3.12 / 3.13)

## 📌 1. Manipulação Moderna com `pathlib`
Em vez de manipular strings de caminhos com `os.path`, use `pathlib.Path`:

```python
from pathlib import Path

# Definir caminho relativo ou absoluto
base_dir = Path(__file__).parent
dados_dir = base_dir / "dados"
dados_dir.mkdir(exist_ok=True)

arquivo_txt = dados_dir / "relatorio.txt"
arquivo_txt.write_text("Relatório de Entregas\nData: 2026-07-23", encoding="utf-8")

conteudo = arquivo_txt.read_text(encoding="utf-8")
print(conteudo)
```

---

## 📌 2. Leitura e Escrita de JSON
```python
import json
from pathlib import Path

dados = {"servidor": "localhost", "porta": 8080, "status": "online"}
path_json = Path("config.json")

# Salvar JSON
path_json.write_text(json.dumps(dados, indent=2, ensure_ascii=False), encoding="utf-8")

# LER JSON
dados_carregados = json.loads(path_json.read_text(encoding="utf-8"))
print(dados_carregados["servidor"])
```
