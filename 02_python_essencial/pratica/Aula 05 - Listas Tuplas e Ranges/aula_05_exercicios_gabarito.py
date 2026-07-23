# -*- coding: utf-8 -*-
"""
Gabarito Oficial de Referência - aula_05_exercicios_gabarito
Curso: Python + IA para Automação em Logística
"""

# ======================================
# GABARITO MANUAL COMENTADO PASSO A PASSO
# ======================================

# Exercício 1
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte", "Porto Alegre"]
cidades.append("Salvador")
cidades.remove("Rio de Janeiro") # Ou cidades.pop(1)
cidades.sort()
print(cidades)

# Exercício 2
cd_coords = (-23.5505, -46.6333)
lat, lon = cd_coords
print(f"Latitude: {lat}, Longitude: {lon}")

# Exercício 3
notas_fiscais = list(range(100, 111))
print(notas_fiscais)

# Exercício 4
# frotas = [
#     ["ABC-1234", 12],
#     ["XYZ-9876", 24],
#     ["QWE-5555", 8]
# ]
capacidade_segundo = frotas[1][1]
print(f"Capacidade do 2º veículo: {capacidade_segundo} ton")

# Exercício 5
distancias_km = [12, 45, 89, 150, 30, 205]
longas_distancias = [d for d in distancias_km if d > 50]
soma_longas = sum(longas_distancias)
print(f"Distâncias longas: {longas_distancias}")
print(f"Soma total: {soma_longas} km")

# o a # ==============================================================================
# 🛑 REGRA DE OURO PARA O APRENDIZADO DE LOGÍSTICA:
# 1. Tente resolver cada exercício SOZINHO primeiro.
# 2. Se travar, use a dica do exercício ou peça ajuda ao Antigravity (IA copiloto)
#    usando os prompts de dica sugeridos (sem pedir a resposta direta!).
# 3. O GABARITO DETALHADO E COMENTADO está no final deste arquivo.
#    Consulte o gabarito APENAS se tiver tentado de verdade e continuar travado!
# ==============================================================================



# Contexto logístico: Lidar com múltiplas rotas, veículos e sequências de documentos.

# Exercício 1 — [Nível: Básico]
# Crie uma lista com 5 códigos de cidades. Adicione uma nova cidade ao final.
# Remova a segunda cidade da lista e depois exiba a lista ordenada em ordem alfabética.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Crie uma tupla com as coordenadas (latitude, longitude) do seu Centro de Distribuição (ex: -23.5505, -46.6333).
# Desempacote essa tupla em duas variáveis (lat, lon) e imprima.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Usando a função range(), gere uma lista de números de nota fiscal sequenciais de 100 até 110 (inclusive).
# Dica: lembre-se de converter o range para list().
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Dada uma lista de listas contendo [placa_veiculo, capacidade_toneladas].
# Acesse e imprima a capacidade do segundo veículo (frotas[1]).
# frotas = [
#     ["ABC-1234", 12],
#     ["XYZ-9876", 24],
#     ["QWE-5555", 8]
# ]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Dada uma lista de distâncias em km.
# Use *list comprehension* para criar uma nova lista apenas com as distâncias superiores a 50 km.
# Calcule a soma (sum()) dessas longas distâncias.
distancias_km = [12, 45, 89, 150, 30, 205]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


# GABARITO:

# Exercício 1
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte", "Porto Alegre"]
cidades.append("Salvador")
cidades.remove("Rio de Janeiro") # Ou cidades.pop(1)
cidades.sort()
print(cidades)

# Exercício 2
cd_coords = (-23.5505, -46.6333)
lat, lon = cd_coords
print(f"Latitude: {lat}, Longitude: {lon}")

# Exercício 3
notas_fiscais = list(range(100, 111))
print(notas_fiscais)

# Exercício 4
# frotas = [
#     ["ABC-1234", 12],
#     ["XYZ-9876", 24],
#     ["QWE-5555", 8]
# ]
capacidade_segundo = frotas[1][1]
print(f"Capacidade do 2º veículo: {capacidade_segundo} ton")

# Exercício 5
distancias_km = [12, 45, 89, 150, 30, 205]
longas_distancias = [d for d in distancias_km if d > 50]
soma_longas = sum(longas_distancias)
print(f"Distâncias longas: {longas_distancias}")
print(f"Soma total: {soma_longas} km")

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



# Contexto logístico: Lidar com múltiplas rotas, veículos e sequências de documentos.

# Exercício 1 — [Nível: Básico]
# Crie uma lista com 5 códigos de cidades. Adicione uma nova cidade ao final.
# Remova a segunda cidade da lista e depois exiba a lista ordenada em ordem alfabética.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Crie uma tupla com as coordenadas (latitude, longitude) do seu Centro de Distribuição (ex: -23.5505, -46.6333).
# Desempacote essa tupla em duas variáveis (lat, lon) e imprima.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Usando a função range(), gere uma lista de números de nota fiscal sequenciais de 100 até 110 (inclusive).
# Dica: lembre-se de converter o range para list().
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Dada uma lista de listas contendo [placa_veiculo, capacidade_toneladas].
# Acesse e imprima a capacidade do segundo veículo (frotas[1]).
# frotas = [
#     ["ABC-1234", 12],
#     ["XYZ-9876", 24],
#     ["QWE-5555", 8]
# ]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Dada uma lista de distâncias em km.
# Use *list comprehension* para criar uma nova lista apenas com as distâncias superiores a 50 km.
# Calcule a soma (sum()) dessas longas distâncias.
distancias_km = [12, 45, 89, 150, 30, 205]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


# GABARITO:

# Exercício 1
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte", "Porto Alegre"]
cidades.append("Salvador")
cidades.remove("Rio de Janeiro") # Ou cidades.pop(1)
cidades.sort()
print(cidades)

# Exercício 2
cd_coords = (-23.5505, -46.6333)
lat, lon = cd_coords
print(f"Latitude: {lat}, Longitude: {lon}")

# Exercício 3
notas_fiscais = list(range(100, 111))
print(notas_fiscais)

# Exercício 4
# frotas = [
#     ["ABC-1234", 12],
#     ["XYZ-9876", 24],
#     ["QWE-5555", 8]
# ]
capacidade_segundo = frotas[1][1]
print(f"Capacidade do 2º veículo: {capacidade_segundo} ton")

# Exercício 5
distancias_km = [12, 45, 89, 150, 30, 205]
longas_distancias = [d for d in distancias_km if d > 50]
soma_longas = sum(longas_distancias)
print(f"Distâncias longas: {longas_distancias}")
print(f"Soma total: {soma_longas} km")





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



# Contexto logístico: Lidar com múltiplas rotas, veículos e sequências de documentos.

# Exercício 1 — [Nível: Básico]
# Crie uma lista com 5 códigos de cidades. Adicione uma nova cidade ao final.
# Remova a segunda cidade da lista e depois exiba a lista ordenada em ordem alfabética.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Crie uma tupla com as coordenadas (latitude, longitude) do seu Centro de Distribuição (ex: -23.5505, -46.6333).
# Desempacote essa tupla em duas variáveis (lat, lon) e imprima.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Usando a função range(), gere uma lista de números de nota fiscal sequenciais de 100 até 110 (inclusive).
# Dica: lembre-se de converter o range para list().
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Dada uma lista de listas contendo [placa_veiculo, capacidade_toneladas].
# Acesse e imprima a capacidade do segundo veículo (frotas[1]).
# frotas = [
#     ["ABC-1234", 12],
#     ["XYZ-9876", 24],
#     ["QWE-5555", 8]
# ]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Dada uma lista de distâncias em km.
# Use *list comprehension* para criar uma nova lista apenas com as distâncias superiores a 50 km.
# Calcule a soma (sum()) dessas longas distâncias.
distancias_km = [12, 45, 89, 150, 30, 205]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


# GABARITO:

# Exercício 1
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte", "Porto Alegre"]
cidades.append("Salvador")
cidades.remove("Rio de Janeiro") # Ou cidades.pop(1)
cidades.sort()
print(cidades)

# Exercício 2
cd_coords = (-23.5505, -46.6333)
lat, lon = cd_coords
print(f"Latitude: {lat}, Longitude: {lon}")

# Exercício 3
notas_fiscais = list(range(100, 111))
print(notas_fiscais)

# Exercício 4
# frotas = [
#     ["ABC-1234", 12],
#     ["XYZ-9876", 24],
#     ["QWE-5555", 8]
# ]
capacidade_segundo = frotas[1][1]
print(f"Capacidade do 2º veículo: {capacidade_segundo} ton")

# Exercício 5
distancias_km = [12, 45, 89, 150, 30, 205]
longas_distancias = [d for d in distancias_km if d > 50]
soma_longas = sum(longas_distancias)
print(f"Distâncias longas: {longas_distancias}")
print(f"Soma total: {soma_longas} km")