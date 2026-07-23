---
tags: [python312, pep8, boas-praticas, novidades]
---
# 📘 08. Boas Práticas (PEP 8) e Novidades do Python 3.12 / 3.13

## 📌 1. Regras Principais da PEP 8
1. **Nomenclatura:**
   - Variáveis e Funções: `snake_case` (ex: `calcular_desconto`).
   - Classes: `PascalCase` (ex: `ProcessadorDeDados`).
   - Constantes: `CAPITAL_SNAKE_CASE` (ex: `TAXA_MAXIMA = 0.15`).
2. **Indentação:** 4 espaços por nível (nunca misturar tabs com espaços).
3. **Docstrings:** Use aspas triplas `"""Docstring"""` em todas as funções públicas e classes.

---

## 📌 2. Resumo das Novidades do Python 3.12 / 3.13
- **Mensagens de Erro Aprimoradas:** O Python agora aponta exatamente qual variável ou atributo foi digitado incorretamente e sugere a correção (`Did you mean...?`).
- **Desempenho Acelerado (Specializing Adaptive Interpreter):** Interpretador CPython até 15-20% mais rápido em loops e chamadas de métodos.
- **f-strings sem restrições:** Permite qualquer caractere válido em Python dentro das chaves de uma f-string.
