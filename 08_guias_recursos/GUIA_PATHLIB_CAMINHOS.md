# 🛣️ Guia Definitivo de Caminhos de Arquivos com `pathlib` (Cross-Platform)

Nunca mais passe raiva com `FileNotFoundError` ou caminhos quebrados no Windows, Linux ou macOS.

---

## 📌 A Regra de Ouro dos Caminhos em Python

> [!IMPORTANT]
> **NUNCA escreva caminhos absolutos fixos** como `C:\Users\Lenovo\Documents\...` no seu código.
> Se você mudar o projeto de pasta ou enviar para outro computador, o script vai quebrar.

### 💡 A Solução Padrão com `pathlib.Path` (Python 3.12 / 3.13)

Sempre encontre o diretório do seu script atual usando `Path(__file__).resolve().parent`:

```python
from pathlib import Path

# 1. Encontrar a pasta onde ESTE arquivo .py está salvo:
PASTA_ATUAL = Path(__file__).resolve().parent

# 2. Navegar para a pasta raiz do projeto (duas pastas acima):
PASTA_RAIZ = PASTA_ATUAL.parents[1]  # ou PASTA_ATUAL.parent.parent

# 3. Montar o caminho seguro até a pasta _dados_exemplo/:
ARQUIVO_CSV = PASTA_RAIZ / "_dados_exemplo" / "entregas_exemplo.csv"

print(f"Caminho Absoluto Seguro: {ARQUIVO_CSV}")
print(f"O arquivo existe? {ARQUIVO_CSV.exists()}")
```

---

## 🛠️ Como Usar os Dados de Exemplo do Curso (`_dados_exemplo/`)

O repositório do curso possui uma pasta com arquivos prontos em `_dados_exemplo/`:

| Arquivo | Tipo | Como ler com `pathlib`? |
| :--- | :--- | :--- |
| `entregas_exemplo.csv` | CSV | `pd.read_csv(PASTA_RAIZ / "_dados_exemplo" / "entregas_exemplo.csv")` |
| `entregas_exemplo.xlsx` | Excel | `pd.read_excel(PASTA_RAIZ / "_dados_exemplo" / "entregas_exemplo.xlsx")` |
| `motoristas_exemplo.json` | JSON | `json.loads((PASTA_RAIZ / "_dados_exemplo" / "motoristas_exemplo.json").read_text(encoding="utf-8"))` |
| `config_email_exemplo.txt` | Texto | `(PASTA_RAIZ / "_dados_exemplo" / "config_email_exemplo.txt").read_text(encoding="utf-8")` |

---

## ⚡ Tabela Rápida de Métodos Úteis do `pathlib.Path`

```python
p = Path("dados/relatorio.csv")

p.name          # "relatorio.csv" (nome completo)
p.stem          # "relatorio"     (nome sem extensão)
p.suffix        # ".csv"          (apenas a extensão)
p.parent        # Path("dados")   (pasta pai)
p.exists()      # True / False    (verifica se o arquivo existe)
p.is_file()     # True / False    (verifica se é um arquivo)
p.is_dir()      # True / False    (verifica se é uma pasta)
p.mkdir(exist_ok=True)  # Cria a pasta caso ela não exista
```
