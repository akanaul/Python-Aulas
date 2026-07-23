# -*- coding: utf-8 -*-
"""
Exercícios - aula_08_exercicios_manual
Curso: Python + IA para Automação em Logística

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado.
- Use a IA Antigravity no MODO TUTOR (pedindo dicas de lógica).
"""

# -*- coding: utf-8 -*-
# Exercícios - aula_08_exercicios_manual
# Curso: Python + IA para Automação

# INSTRUÇÕES:


# INSTRUÇÕES:
# - O objetivo deste arquivo não é codificar do zero, mas interagir com o Antigravity (ou outra IA).
# - Copie os desafios, abra o chat da IA e teste diferentes prompts.
# - Analise a resposta da IA. Ela fez o que você queria? Se não, refine o prompt.

# Exercício 1 — Prompt de Explicação
# Copie o código abaixo e cole no chat da IA com o prompt:
# "Explique este código linha a linha para um iniciante em Python. Use analogias de logística."

# def _normalize_text(raw_text):
#     if not raw_text:
#         return ""
#     import unicodedata
#     nfkd_form = unicodedata.normalize('NFKD', raw_text.strip())
#     only_ascii = nfkd_form.encode('ASCII', 'ignore')
#     return only_ascii.decode('utf-8').upper()


# Exercício 2 — Prompt de Geração com Contexto
# Vá ao chat da IA e peça para ela criar um código do zero baseando-se nas regras abaixo:
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Contexto: Você precisa de uma função em Python para calcular o valor do frete extra de pernoite.
# Regras:
# 1. A função recebe `dias_viagem` e `taxa_pernoite` (padrão 150.0).
# 2. Se a viagem durar mais de 1 dia, subtrai 1 dia e multiplica pela taxa.
# 3. Retorna o valor extra total.
# 4. Exigência: Crie usando type hints e docstrings. Comentários em PT-BR, variáveis em inglês.


# Exercício 3 — Prompt de Debug
# O código abaixo possui um erro proposital. 
# Execute mentalmente ou no terminal e veja o erro (KeyError).
# Copie o código e o erro para a IA e use o prompt:
# "Meu código logístico está falhando com KeyError. Onde está o erro e como posso corrigi-lo usando uma abordagem mais segura para acessar dicionários (ex: .get)?"

# trucks_db = {
#     "BR-01": {"driver": "João", "status": "Manutenção"},
#     "BR-02": {"driver": "Maria", "status": "Rota"}
# }

# Simulando sistema buscando um caminhão que não existe
placa_buscada = "BR-99"
status_atual = trucks_db[placa_buscada]["status"]
print(f"O caminhão {placa_buscada} está em: {status_atual}")


# GABARITO / COMENTÁRIOS DA RESOLUÇÃO (O que esperar da IA):