# -*- coding: utf-8 -*-
"""
Gabarito Oficial de Referência - aula_03_exercicios_gabarito
Curso: Python + IA para Automação em Logística
"""

# ======================================
# GABARITO MANUAL COMENTADO PASSO A PASSO
# ======================================

# Exercício 1
cargo_weight = 2100
# if cargo_weight > 2000:
#     print("Bloqueado por excesso")
# else:
#     print("Aprovado")

# Exercício 2
# for dock_number in range(1, 6):
#     print(f"Conferindo doca {dock_number}")

# Exercício 3
statuses = ["Em separação", "Faturado", "Em trânsito", "Entregue"]
# for status in statuses:
#     if status == "Faturado":
#         print("Ação: Imprimir DANFE")
#     else:
#         print(f"Status atual: {status}")

# Exercício 4
capacity = 100
current_load = 0

# while current_load < capacity:
#     current_load += 20
#     print(f"Carga atualizada: {current_load}kg")

# Exercício 5
zip_codes = ["01000-000", "13000-000", "", "22000-000"]

# for zip_code in zip_codes:
#     if zip_code == "":
#         print("Erro: CEP em branco encontrado. Interrompendo roteirização.")
#         break
        
#     if zip_code[0] == "0":
#         print(f"CEP {zip_code}: Região SP Capital")
#     else:
#         print(f"CEP {zip_code}: Outras Regiões")

# o a # ==============================================================================
# 🛑 REGRA DE OURO PARA O APRENDIZADO DE LOGÍSTICA:
# 1. Tente resolver cada exercício SOZINHO primeiro.
# 2. Se travar, use a dica do exercício ou peça ajuda ao Antigravity (IA copiloto)
#    usando os prompts de dica sugeridos (sem pedir a resposta direta!).
# 3. O GABARITO DETALHADO E COMENTADO está no final deste arquivo.
#    Consulte o gabarito APENAS se tiver tentado de verdade e continuar travado!
# ==============================================================================



# Contexto: Você precisa classificar e roteirizar cargas na expedição.

# Exercício 1 — [Nível: Básico]
# Crie uma variável cargo_weight = 2100.
# Faça um 'if' que verifique se a carga pesa mais que 2000. 
# Se sim, imprima "Bloqueado por excesso", senão, "Aprovado".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 2 — [Nível: Básico]
# Utilize um loop 'for' e a função range() para simular a conferência de 5 docas.
# Imprima: "Conferindo doca 1", "Conferindo doca 2", etc.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 3 — [Nível: Intermediário]
# Dada a lista de status: statuses = ["Em separação", "Faturado", "Em trânsito", "Entregue"]
# Faça um 'for' pela lista. Se o status for "Faturado", imprima "Ação: Imprimir DANFE".
# Senão, imprima o próprio status.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 4 — [Nível: Intermediário]
# Utilize um 'while' para simular o carregamento de caixas de 20kg.
# O caminhão tem capacidade de 100kg. Inicie current_load = 0.
# Enquanto a carga atual for menor que 100, adicione 20 e imprima a carga atual.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 5 — [Nível: Desafio]
# Dada uma lista de CEPs: zip_codes = ["01000-000", "13000-000", "", "22000-000"]
# Faça um 'for' loop.
# Se o CEP for vazio "", use 'break' para interromper o processo informando erro.
# Se começar com "0" (ex: zip_code[0] == "0"), imprima "Região SP Capital".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:




# ======================================
# GABARITO COMENTADO
# ======================================
# Exercício 1
cargo_weight = 2100
# if cargo_weight > 2000:
#     print("Bloqueado por excesso")
# else:
#     print("Aprovado")

# Exercício 2
# for dock_number in range(1, 6):
#     print(f"Conferindo doca {dock_number}")

# Exercício 3
statuses = ["Em separação", "Faturado", "Em trânsito", "Entregue"]
# for status in statuses:
#     if status == "Faturado":
#         print("Ação: Imprimir DANFE")
#     else:
#         print(f"Status atual: {status}")

# Exercício 4
capacity = 100
current_load = 0

# while current_load < capacity:
#     current_load += 20
#     print(f"Carga atualizada: {current_load}kg")

# Exercício 5
zip_codes = ["01000-000", "13000-000", "", "22000-000"]

# for zip_code in zip_codes:
#     if zip_code == "":
#         print("Erro: CEP em branco encontrado. Interrompendo roteirização.")
#         break
        
#     if zip_code[0] == "0":
#         print(f"CEP {zip_code}: Região SP Capital")
#     else:
#         print(f"CEP {zip_code}: Outras Regiões")

# o como você faria no Excel ou no papel.
# Dica de Código: Lembre-se da sintaxe vista na aula.

# 🤖 PROMPT TUTOR PARA A IA (Copie e cole se travar):
# "Atue como meu tutor de Python. Estou tentando resolver um exercício sobre [TEMA]. 
# Meu código até agora é este: [COLE AQUI]. 
# Não me dê a resposta direta. Aponte o erro e me dê uma dica de como consertar."

# ==============================================================================
# SEU CÓDIGO AQUI
# ==============================================================================

# ==============================================================================
# 🛑 REGRA DE OURO PARA O APRENDIZADO DE LOGÍSTICA:
# 1. Tente resolver cada exercício SOZINHO primeiro.
# 2. Se travar, use a dica do exercício ou peça ajuda ao Antigravity (IA copiloto)
#    usando os prompts de dica sugeridos (sem pedir a resposta direta!).
# 3. O GABARITO DETALHADO E COMENTADO está no final deste arquivo.
#    Consulte o gabarito APENAS se tiver tentado de verdade e continuar travado!
# ==============================================================================



# Contexto: Você precisa classificar e roteirizar cargas na expedição.

# Exercício 1 — [Nível: Básico]
# Crie uma variável cargo_weight = 2100.
# Faça um 'if' que verifique se a carga pesa mais que 2000. 
# Se sim, imprima "Bloqueado por excesso", senão, "Aprovado".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 2 — [Nível: Básico]
# Utilize um loop 'for' e a função range() para simular a conferência de 5 docas.
# Imprima: "Conferindo doca 1", "Conferindo doca 2", etc.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 3 — [Nível: Intermediário]
# Dada a lista de status: statuses = ["Em separação", "Faturado", "Em trânsito", "Entregue"]
# Faça um 'for' pela lista. Se o status for "Faturado", imprima "Ação: Imprimir DANFE".
# Senão, imprima o próprio status.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 4 — [Nível: Intermediário]
# Utilize um 'while' para simular o carregamento de caixas de 20kg.
# O caminhão tem capacidade de 100kg. Inicie current_load = 0.
# Enquanto a carga atual for menor que 100, adicione 20 e imprima a carga atual.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 5 — [Nível: Desafio]
# Dada uma lista de CEPs: zip_codes = ["01000-000", "13000-000", "", "22000-000"]
# Faça um 'for' loop.
# Se o CEP for vazio "", use 'break' para interromper o processo informando erro.
# Se começar com "0" (ex: zip_code[0] == "0"), imprima "Região SP Capital".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:




# ======================================
# GABARITO COMENTADO
# ======================================
# Exercício 1
cargo_weight = 2100
# if cargo_weight > 2000:
#     print("Bloqueado por excesso")
# else:
#     print("Aprovado")

# Exercício 2
# for dock_number in range(1, 6):
#     print(f"Conferindo doca {dock_number}")

# Exercício 3
statuses = ["Em separação", "Faturado", "Em trânsito", "Entregue"]
# for status in statuses:
#     if status == "Faturado":
#         print("Ação: Imprimir DANFE")
#     else:
#         print(f"Status atual: {status}")

# Exercício 4
capacity = 100
current_load = 0

# while current_load < capacity:
#     current_load += 20
#     print(f"Carga atualizada: {current_load}kg")

# Exercício 5
zip_codes = ["01000-000", "13000-000", "", "22000-000"]

# for zip_code in zip_codes:
#     if zip_code == "":
#         print("Erro: CEP em branco encontrado. Interrompendo roteirização.")
#         break
        
#     if zip_code[0] == "0":
#         print(f"CEP {zip_code}: Região SP Capital")
#     else:
#         print(f"CEP {zip_code}: Outras Regiões")





# ==============================================================================
# GABARITO (Tente antes de olhar!)
# ==============================================================================
# Exemplo de Solução:
# def main():
#     # ==============================================================================
# 🛑 REGRA DE OURO PARA O APRENDIZADO DE LOGÍSTICA:
# 1. Tente resolver cada exercício SOZINHO primeiro.
# 2. Se travar, use a dica do exercício ou peça ajuda ao Antigravity (IA copiloto)
#    usando os prompts de dica sugeridos (sem pedir a resposta direta!).
# 3. O GABARITO DETALHADO E COMENTADO está no final deste arquivo.
#    Consulte o gabarito APENAS se tiver tentado de verdade e continuar travado!
# ==============================================================================



# Contexto: Você precisa classificar e roteirizar cargas na expedição.

# Exercício 1 — [Nível: Básico]
# Crie uma variável cargo_weight = 2100.
# Faça um 'if' que verifique se a carga pesa mais que 2000. 
# Se sim, imprima "Bloqueado por excesso", senão, "Aprovado".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 2 — [Nível: Básico]
# Utilize um loop 'for' e a função range() para simular a conferência de 5 docas.
# Imprima: "Conferindo doca 1", "Conferindo doca 2", etc.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 3 — [Nível: Intermediário]
# Dada a lista de status: statuses = ["Em separação", "Faturado", "Em trânsito", "Entregue"]
# Faça um 'for' pela lista. Se o status for "Faturado", imprima "Ação: Imprimir DANFE".
# Senão, imprima o próprio status.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 4 — [Nível: Intermediário]
# Utilize um 'while' para simular o carregamento de caixas de 20kg.
# O caminhão tem capacidade de 100kg. Inicie current_load = 0.
# Enquanto a carga atual for menor que 100, adicione 20 e imprima a carga atual.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 5 — [Nível: Desafio]
# Dada uma lista de CEPs: zip_codes = ["01000-000", "13000-000", "", "22000-000"]
# Faça um 'for' loop.
# Se o CEP for vazio "", use 'break' para interromper o processo informando erro.
# Se começar com "0" (ex: zip_code[0] == "0"), imprima "Região SP Capital".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:




# ======================================
# GABARITO COMENTADO
# ======================================
# Exercício 1
cargo_weight = 2100
# if cargo_weight > 2000:
#     print("Bloqueado por excesso")
# else:
#     print("Aprovado")

# Exercício 2
# for dock_number in range(1, 6):
#     print(f"Conferindo doca {dock_number}")

# Exercício 3
statuses = ["Em separação", "Faturado", "Em trânsito", "Entregue"]
# for status in statuses:
#     if status == "Faturado":
#         print("Ação: Imprimir DANFE")
#     else:
#         print(f"Status atual: {status}")

# Exercício 4
capacity = 100
current_load = 0

# while current_load < capacity:
#     current_load += 20
#     print(f"Carga atualizada: {current_load}kg")

# Exercício 5
zip_codes = ["01000-000", "13000-000", "", "22000-000"]

# for zip_code in zip_codes:
#     if zip_code == "":
#         print("Erro: CEP em branco encontrado. Interrompendo roteirização.")
#         break
        
#     if zip_code[0] == "0":
#         print(f"CEP {zip_code}: Região SP Capital")
#     else:
#         print(f"CEP {zip_code}: Outras Regiões")