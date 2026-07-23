---
data: <% tp.file.creation_date("YYYY-MM-DD") %>
script: "[Nome do script.py]"
erro_tipo: "[Ex: KeyError, FileNotFoundError]"
status: pendente
tags: [erro, python, logistica]
---

# Registro de Erro: <% tp.file.title %>

## 🎯 O que eu estava tentando fazer
[Explique em linguagem de logística, ex: "Tentando ler a planilha de romaneio para extrair a coluna 'Destino' e preencher no sistema"]

## 💥 O Erro / Traceback Completo
```python
[Cole o traceback copiado do terminal ou gerado pela função get_last_error_summary do safe_logger.py]
```

## 🧠 Causa Raiz (explicada pela IA)
> **Dica:** Jogue o erro e seu código no Antigravity e peça: "Explique esse erro de forma simples para um iniciante, usando analogia com logística."

[Explicação simples da causa do erro]

## 🛠️ Como foi Solucionado (Código Antes vs Depois)

### ❌ Antes (Com Erro)
```python
# Seu código que estava falhando
```

### ✅ Depois (Resolvido)
```python
# A solução
```

## 🛡️ O que fazer para evitar no futuro
- [ ] Checar os dados da planilha antes do processamento (validação de schema)
- [ ] Usar bloco try/except apropriado
- [ ] [Outro aprendizado]
