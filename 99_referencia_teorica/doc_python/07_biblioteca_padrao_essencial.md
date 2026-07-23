---
tags: [python312, stdlib, os, sys, subprocess, re, datetime]
---
# 📘 07. Biblioteca Padrão Essencial (Python 3.12 / 3.13)

## 📌 1. Automação de Sistema (`os`, `sys`, `subprocess`)
```python
import sys
import subprocess

# Informações da plataforma e versão do Python
print(f"Executando no Python {sys.version} em {sys.platform}")

# Execução segura de comandos no SO
res = subprocess.run(["git", "--version"], capture_output=True, text=True, check=True)
print(res.stdout.strip())
```

---

## 📌 2. Expressões Regulares (`re`)
```python
import re

texto = "Placa do veículo: ABC-1234 gravada na nota."
match = re.search(r'([A-Z]{3}-\d{4})', texto)
if match:
    placa = match.group(1) # "ABC-1234"
```

---

## 📌 3. Data e Hora (`datetime`)
```python
from datetime import datetime, timedelta

agora = datetime.now()
prazo_entrega = agora + timedelta(days=3)

print(f"Data Atual: {agora.strftime('%d/%m/%Y %H:%M')}")
print(f"Prazo Limite: {prazo_entrega.strftime('%d/%m/%Y')}")
```
