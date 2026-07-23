---
sticker: "🐍"
tags: [python312, referencia, documentacao, offline]
---
# 🐍 Documentação Oficial & Guia de Referência — Python 3.12 / 3.13

> [!TUTOR] Manual Teórico de Consulta Rápida Offline
> Esta pasta contém a **documentação essencial do Python 3.12 / 3.13** convertida em arquivos Markdown formatados para o Obsidian, permitindo buscas instantâneas (`Ctrl+O` ou `Ctrl+Shift+F`) sem necessidade de conexão com a internet.

---

## 📚 Índice Completo da Documentação (Capítulos 01 a 08)

- [[99_referencia_teorica/doc_python/01_sintaxe_variaveis_tipos|01. Sintaxe Básica, Variáveis e Tipos de Dados]]
- [[99_referencia_teorica/doc_python/02_estruturas_controle_excecoes|02. Estruturas de Controle e Tratamento de Exceções]]
- [[99_referencia_teorica/doc_python/03_estruturas_dados_modernas|03. Estruturas de Dados Modernas (Listas, Dicionários, Tuplas, Conjuntos)]]
- [[99_referencia_teorica/doc_python/04_funcoes_type_hints_312|04. Funções, Type Hints Modernos (`type` Statement) e PEP 695]]
- [[99_referencia_teorica/doc_python/05_poo_classes_dataclasses|05. Programação Orientada a Objetos e `@dataclass`]]
- [[99_referencia_teorica/doc_python/06_arquivos_pathlib_json|06. Manipulação de Arquivos (`pathlib`, CSV, JSON)]]
- [[99_referencia_teorica/doc_python/07_biblioteca_padrao_essencial|07. Biblioteca Padrão Essencial (`os`, `sys`, `subprocess`, `re`, `datetime`)]]
- [[99_referencia_teorica/doc_python/08_pep8_e_novidades_python312|08. Boas Práticas (PEP 8) e Novidades do Python 3.12 / 3.13]]

---

## ⚡ Novidades de Destaque no Python 3.12 / 3.13

1. **Sintaxe de Tipos Genéricos (PEP 695):**
   ```python
   type Vetor[T] = list[T]
   def primeiro[T](lista: list[T]) -> T:
       return lista[0]
   ```
2. **f-strings Melhoradas:** Permitem aspas aninhadas e reutilização de aspas duplas dentro das expressões.
3. **Tracebacks Coloridos e Diagnósticos:** Mensagens de erro com indicação precisa da coluna e causa raiz.
