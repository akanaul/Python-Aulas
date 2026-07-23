---
aliases: ["Aula 10 — Manipulação de Arquivos TXT, CSV e Pathlib"]
tags: [aula, bloco-4, python, arquivos, csv, txt, pathlib]
---
> 💡 **O que você vai aprender:** Ler, escrever e manipular arquivos de texto e tabelas CSV usando o módulo moderno `pathlib` e tratamento de erros.
> ⏱️ **Duração estimada:** 2h30 | 📅 **Bloco:** 4

---

## 🎯 Objetivos da Aula
- Dominar a leitura e escrita de arquivos TXT e CSV.
- Utilizar `pathlib.Path` para criar caminhos cross-platform (Windows / Mac / Linux) sem `FileNotFoundError`.
- Manipular dados de exemplo da pasta `_dados_exemplo/`.

---

## 🛣️ Manipulação Segura de Caminhos com `pathlib.Path`

> [!IMPORTANT]
> **NUNCA escreva caminhos absolutos fixos** como `C:\Users\...` no seu código. Use `Path(__file__).resolve().parent` para ancorar caminhos a partir da pasta do próprio arquivo `.py`!

```python
from pathlib import Path

# Encontrar a pasta raiz do repositório (subindo 3 níveis)

> [!TUTOR] 🚀 Guia Prático de Estudo da Aula (Ciclo de 4 Passos em 1-Clique)
> 1. 📖 **Conceito:** Leia as explicações e tire dúvidas com a IA no **Modo Tutor**.
> 2. 👨‍💻 **Código:** Edite e desenvolva sua solução no arquivo `*_manual.py`.
> 3. ⚡ **Testar no Obsidian (1-Clique):** Clique em **Run** no bloco abaixo para validar:
> ```python run
> import subprocess
> res = subprocess.run(["python", "avaliar_exercicio.py", "--issue", "10"], capture_output=True, text=True)
> print(res.stdout)
> ```
> 4. 🔀 **Enviar PR:** Se aprovado pela IA, envie o Pull Request no GitHub para o Tutor (@akanaul)!

PASTA_ATUAL = Path(__file__).resolve().parent
PASTA_RAIZ = PASTA_ATUAL.parents[2]

# Caminho seguro até a pasta _dados_exemplo/
ARQUIVO_CSV = PASTA_RAIZ / "_dados_exemplo" / "entregas_exemplo.csv"
ARQUIVO_TXT = PASTA_RAIZ / "_dados_exemplo" / "config_email_exemplo.txt"

print(f"Caminho Seguro: {ARQUIVO_CSV}")
print(f"O arquivo existe? {ARQUIVO_CSV.exists()}")
```

---

## 📄 Leitura e Escrita de Arquivos TXT

```python
from pathlib import Path

# LER todo o conteúdo do arquivo de texto com UTF-8
conteudo = ARQUIVO_TXT.read_text(encoding="utf-8")
print("Conteúdo do TXT:")
print(conteudo)

# ESCREVER ou SOBRESCREVER um arquivo TXT
novo_arquivo = PASTA_ATUAL / "log_execucao.txt"
novo_arquivo.write_text("Processamento concluído com sucesso.\nStatus: OK", encoding="utf-8")
```

---

## 📊 Leitura e Processamento de CSV Nativamente

```python
import csv
from pathlib import Path

# Leitura de CSV usando csv.DictReader
if ARQUIVO_CSV.exists():
    with open(ARQUIVO_CSV, mode="r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)
        for linha in leitor:
            print(f"Entrega #{linha.get('ID', 'N/A')}: Cliente {linha.get('Cliente', 'N/A')} - Status: {linha.get('Status', 'N/A')}")
```

---

## 🏋️ Exercícios
> 📌 **Issue Relacionada no GitHub:** `# Issue #10`
> 📁 **Arquivo de Trabalho (Manual):** `04_bibliotecas_arquivos/Aula 10 - Arquivos txt e csv/aula_10_exercicios_manual.py`
> 🧪 **Comando de Teste:** `python avaliar_exercicio.py --issue 10`

---

## 🔀 Aprendizado Ativo de Git, Issue & Pull Request

> 📌 **Issue Oficial no GitHub:** `# Issue #10`
> 🔀 **Branch de Desenvolvimento:** `git checkout -b feature/issue-10-arquivos-txt-csv`
> 📁 **Arquivo de Trabalho (Manual):** `aula_10_exercicios_manual.py`
> 🧪 **Teste Automatizado & Pré-Aprovação IA:** `python avaliar_exercicio.py --issue 10`
> 🚀 **Envio de Pull Request (PR):** `git push origin feature/issue-10-arquivos-txt-csv` e abra o PR no GitHub para a revisão final do Tutor (@akanaul)!

---

## 📝 Anotações Pessoais do Aluno sobre esta Aula

> [!TIP] **Criar Nota de Estudo Relacionada**
> Quer guardar resumos ou anotações próprias sobre esta aula?
> Pressione Alt + N no Templater e selecione **Template de Anotação do Aluno** para salvar automaticamente em [[meu_caderno_aluno/anotacoes_aulas/anotacoes_aulas|meu_caderno_aluno/anotacoes_aulas/]]!