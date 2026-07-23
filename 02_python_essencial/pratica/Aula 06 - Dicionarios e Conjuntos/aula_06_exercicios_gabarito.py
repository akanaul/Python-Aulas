# -*- coding: utf-8 -*-
"""
Gabarito Oficial de Referência - aula_06_exercicios_gabarito
Curso: Python + IA para Automação em Logística
"""

# ======================================
# GABARITO MANUAL COMENTADO PASSO A PASSO
# ======================================

# Exercício 1
# nf = {
#     "chave_acesso": "35230112345678901234550010001234561012345678",
#     "valor": 4500.50,
#     "data": "2023-10-25",
#     "fornecedor": "Industria ABC"
# }
print(nf["valor"])

# Exercício 2
transportadora = nf.get("transportadora", "Rodoviário Padrão")
print(transportadora)

# Exercício 3
cidades_visitadas_lista = ["SP", "RJ", "SP", "MG", "RJ", "PR"]
cidades_unicas = set(cidades_visitadas_lista)
print(cidades_unicas)

# Exercício 4
status_entregas = {"BR01": "Entregue", "BR02": "Em rota", "BR03": "Pendente"}
# for pacote, status in status_entregas.items():
#     print(f"O pacote {pacote} está com status {status}")

# Exercício 5
motoristas_seg = {"João", "Maria", "Pedro"}
motoristas_ter = {"Maria", "José", "Pedro"}

ambos_dias = motoristas_seg.intersection(motoristas_ter)
apenas_seg = motoristas_seg.difference(motoristas_ter)

print(f"Trabalharam ambos os dias: {ambos_dias}")
print(f"Trabalharam apenas na segunda: {apenas_seg}")

# o a # ==============================================================================
# 🛑 REGRA DE OURO PARA O APRENDIZADO DE LOGÍSTICA:
# 1. Tente resolver cada exercício SOZINHO primeiro.
# 2. Se travar, use a dica do exercício ou peça ajuda ao Antigravity (IA copiloto)
#    usando os prompts de dica sugeridos (sem pedir a resposta direta!).
# 3. O GABARITO DETALHADO E COMENTADO está no final deste arquivo.
#    Consulte o gabarito APENAS se tiver tentado de verdade e continuar travado!
# ==============================================================================



# Contexto logístico: Mapear atributos de rotas e lidar com ocorrências únicas em transportes.

# Exercício 1 — [Nível: Básico]
# Crie um dicionário representando uma nota fiscal com as chaves: "chave_acesso", "valor", "data" e "fornecedor".
# Exiba o valor da nota acessando a chave diretamente.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Usando o dicionário do exercício 1, utilize o método .get() para tentar acessar a chave "transportadora".
# Caso não exista, retorne "Rodoviário Padrão". Imprima o resultado.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Você tem uma lista de cidades onde as entregas de hoje passaram.
# Converta essa lista para um conjunto (set) para descobrir as cidades únicas visitadas e imprima o set.
cidades_visitadas_lista = ["SP", "RJ", "SP", "MG", "RJ", "PR"]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Dado o dicionário de status de entregas abaixo, use um loop for com o método .items()
# para imprimir a frase: "O pacote [CHAVE] está com status [VALOR]".
status_entregas = {"BR01": "Entregue", "BR02": "Em rota", "BR03": "Pendente"}
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Crie dois conjuntos de motoristas que trabalharam na segunda e na terça.
# Use operações de conjunto (intersection, difference) para descobrir:
# a) Quem trabalhou nos dois dias (segunda E terça)?
# b) Quem trabalhou apenas na segunda?
motoristas_seg = {"João", "Maria", "Pedro"}
motoristas_ter = {"Maria", "José", "Pedro"}
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


# GABARITO:

# Exercício 1
# nf = {
#     "chave_acesso": "35230112345678901234550010001234561012345678",
#     "valor": 4500.50,
#     "data": "2023-10-25",
#     "fornecedor": "Industria ABC"
# }
print(nf["valor"])

# Exercício 2
transportadora = nf.get("transportadora", "Rodoviário Padrão")
print(transportadora)

# Exercício 3
cidades_visitadas_lista = ["SP", "RJ", "SP", "MG", "RJ", "PR"]
cidades_unicas = set(cidades_visitadas_lista)
print(cidades_unicas)

# Exercício 4
status_entregas = {"BR01": "Entregue", "BR02": "Em rota", "BR03": "Pendente"}
# for pacote, status in status_entregas.items():
#     print(f"O pacote {pacote} está com status {status}")

# Exercício 5
motoristas_seg = {"João", "Maria", "Pedro"}
motoristas_ter = {"Maria", "José", "Pedro"}

ambos_dias = motoristas_seg.intersection(motoristas_ter)
apenas_seg = motoristas_seg.difference(motoristas_ter)

print(f"Trabalharam ambos os dias: {ambos_dias}")
print(f"Trabalharam apenas na segunda: {apenas_seg}")

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



# Contexto logístico: Mapear atributos de rotas e lidar com ocorrências únicas em transportes.

# Exercício 1 — [Nível: Básico]
# Crie um dicionário representando uma nota fiscal com as chaves: "chave_acesso", "valor", "data" e "fornecedor".
# Exiba o valor da nota acessando a chave diretamente.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Usando o dicionário do exercício 1, utilize o método .get() para tentar acessar a chave "transportadora".
# Caso não exista, retorne "Rodoviário Padrão". Imprima o resultado.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Você tem uma lista de cidades onde as entregas de hoje passaram.
# Converta essa lista para um conjunto (set) para descobrir as cidades únicas visitadas e imprima o set.
cidades_visitadas_lista = ["SP", "RJ", "SP", "MG", "RJ", "PR"]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Dado o dicionário de status de entregas abaixo, use um loop for com o método .items()
# para imprimir a frase: "O pacote [CHAVE] está com status [VALOR]".
status_entregas = {"BR01": "Entregue", "BR02": "Em rota", "BR03": "Pendente"}
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Crie dois conjuntos de motoristas que trabalharam na segunda e na terça.
# Use operações de conjunto (intersection, difference) para descobrir:
# a) Quem trabalhou nos dois dias (segunda E terça)?
# b) Quem trabalhou apenas na segunda?
motoristas_seg = {"João", "Maria", "Pedro"}
motoristas_ter = {"Maria", "José", "Pedro"}
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


# GABARITO:

# Exercício 1
# nf = {
#     "chave_acesso": "35230112345678901234550010001234561012345678",
#     "valor": 4500.50,
#     "data": "2023-10-25",
#     "fornecedor": "Industria ABC"
# }
print(nf["valor"])

# Exercício 2
transportadora = nf.get("transportadora", "Rodoviário Padrão")
print(transportadora)

# Exercício 3
cidades_visitadas_lista = ["SP", "RJ", "SP", "MG", "RJ", "PR"]
cidades_unicas = set(cidades_visitadas_lista)
print(cidades_unicas)

# Exercício 4
status_entregas = {"BR01": "Entregue", "BR02": "Em rota", "BR03": "Pendente"}
# for pacote, status in status_entregas.items():
#     print(f"O pacote {pacote} está com status {status}")

# Exercício 5
motoristas_seg = {"João", "Maria", "Pedro"}
motoristas_ter = {"Maria", "José", "Pedro"}

ambos_dias = motoristas_seg.intersection(motoristas_ter)
apenas_seg = motoristas_seg.difference(motoristas_ter)

print(f"Trabalharam ambos os dias: {ambos_dias}")
print(f"Trabalharam apenas na segunda: {apenas_seg}")





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



# Contexto logístico: Mapear atributos de rotas e lidar com ocorrências únicas em transportes.

# Exercício 1 — [Nível: Básico]
# Crie um dicionário representando uma nota fiscal com as chaves: "chave_acesso", "valor", "data" e "fornecedor".
# Exiba o valor da nota acessando a chave diretamente.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Usando o dicionário do exercício 1, utilize o método .get() para tentar acessar a chave "transportadora".
# Caso não exista, retorne "Rodoviário Padrão". Imprima o resultado.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Você tem uma lista de cidades onde as entregas de hoje passaram.
# Converta essa lista para um conjunto (set) para descobrir as cidades únicas visitadas e imprima o set.
cidades_visitadas_lista = ["SP", "RJ", "SP", "MG", "RJ", "PR"]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Dado o dicionário de status de entregas abaixo, use um loop for com o método .items()
# para imprimir a frase: "O pacote [CHAVE] está com status [VALOR]".
status_entregas = {"BR01": "Entregue", "BR02": "Em rota", "BR03": "Pendente"}
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Crie dois conjuntos de motoristas que trabalharam na segunda e na terça.
# Use operações de conjunto (intersection, difference) para descobrir:
# a) Quem trabalhou nos dois dias (segunda E terça)?
# b) Quem trabalhou apenas na segunda?
motoristas_seg = {"João", "Maria", "Pedro"}
motoristas_ter = {"Maria", "José", "Pedro"}
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


# GABARITO:

# Exercício 1
# nf = {
#     "chave_acesso": "35230112345678901234550010001234561012345678",
#     "valor": 4500.50,
#     "data": "2023-10-25",
#     "fornecedor": "Industria ABC"
# }
print(nf["valor"])

# Exercício 2
transportadora = nf.get("transportadora", "Rodoviário Padrão")
print(transportadora)

# Exercício 3
cidades_visitadas_lista = ["SP", "RJ", "SP", "MG", "RJ", "PR"]
cidades_unicas = set(cidades_visitadas_lista)
print(cidades_unicas)

# Exercício 4
status_entregas = {"BR01": "Entregue", "BR02": "Em rota", "BR03": "Pendente"}
# for pacote, status in status_entregas.items():
#     print(f"O pacote {pacote} está com status {status}")

# Exercício 5
motoristas_seg = {"João", "Maria", "Pedro"}
motoristas_ter = {"Maria", "José", "Pedro"}

ambos_dias = motoristas_seg.intersection(motoristas_ter)
apenas_seg = motoristas_seg.difference(motoristas_ter)

print(f"Trabalharam ambos os dias: {ambos_dias}")
print(f"Trabalharam apenas na segunda: {apenas_seg}")