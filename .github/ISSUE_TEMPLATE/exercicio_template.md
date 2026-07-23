---
name: "📋 Desafio de Exercício / Issue"
about: "Template padrão para resolução de exercícios do curso com testes automatizados e Git."
title: "[EXERCÍCIO] Issue #XX - [Nome do Módulo]"
labels: "exercicio, tdd, autoteste"
assignees: ""
---

# 🚀 Issue #XX — [Nome do Módulo]

## 🎯 Objetivo
Descrever o objetivo do exercício praticado neste módulo.

## 📁 Arquivos Alvo
- **Exercício Manual (Tutor):** `caminho/para/exercicio_manual.py`
- **Exercício IA (One-Shot):** `caminho/para/exercicio_ia.py`
- **Arquivo de Teste:** `testes/test_modulo_XX.py`

## 🔀 Workflow Git
1. Crie uma branch para esta issue:
   ```bash
   git checkout -b feature/issue-XX-nome
   ```
2. Desenvolva sua lógica no arquivo `_manual.py`.
3. Valide sua solução com o avaliador automatizado:
   ```bash
   python avaliar_exercicio.py --issue XX
   ```
4. Se o teste passar (`✅ SOLUÇÃO ACEITA`), faça o commit e o merge para a branch principal (`main`):
   ```bash
   git add .
   git commit -m "fix(issue-XX): solucao aceita no modulo XX"
   git checkout main
   git merge feature/issue-XX-nome
   ```

## 🧪 Critérios de Aceite
- [ ] O script passa em 100% dos testes unitários automatizados.
- [ ] O código segue as boas práticas PEP 8 (variáveis legíveis, funções coesas).
