"""
======================================
GABARITO MANUAL COMENTADO PASSO A PASSO
======================================
"""

# Exercício 1
def soma_pesos(p1, p2):
    return p1 + p2
print(soma_pesos(15.5, 20.0))

# Exercício 2
def verificar_caminhao(placa):
    if placa == "":
        return "Placa inválida"
    return f"Placa registrada: {placa}"
print(verificar_caminhao("ABC-1234"))

# Exercício 3
def calcular_eta(distancia_km, velocidade_media=60):
    return distancia_km / velocidade_media
print(f"Tempo de viagem: {calcular_eta(120)} horas")

# Exercício 4
def min_max_pesos(pesos):
    return (min(pesos), max(pesos))
menor, maior = min_max_pesos([10, 50, 5, 120, 30])
print(f"Menor: {menor}kg | Maior: {maior}kg")

# Exercício 5
def formatar_motoristas(*args):
    \"\"\"
    Recebe um número variável de nomes de motoristas e os retorna em maiúsculas.
    \"\"\"
    return [motorista.upper() for motorista in args]

lista_formatada = formatar_motoristas("João", "Maria", "Pedro", "Ana")
print(lista_formatada)
"""

o a # ==============================================================================
# 🛑 REGRA DE OURO PARA O APRENDIZADO DE LOGÍSTICA:
# 1. Tente resolver cada exercício SOZINHO primeiro.
# 2. Se travar, use a dica do exercício ou peça ajuda ao Antigravity (IA copiloto)
#    usando os prompts de dica sugeridos (sem pedir a resposta direta!).
# 3. O GABARITO DETALHADO E COMENTADO está no final deste arquivo.
#    Consulte o gabarito APENAS se tiver tentado de verdade e continuar travado!
# ==============================================================================

"""
Exercícios — Aula 7: Funções
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

# Contexto logístico: Modularizar lógicas de cálculo, verificação de dados e geração de relatórios.

# Exercício 1 — [Nível: Básico]
# Crie uma função chamada `soma_pesos` que recebe o peso de dois pacotes e retorna a soma deles.
# Chame a função passando 15.5 e 20.0 e imprima o resultado.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Crie uma função `verificar_caminhao` que recebe uma `placa`. 
# Se a placa for uma string vazia (""), retorne "Placa inválida".
# Senão retorne "Placa registrada: [placa]".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Escreva uma função `calcular_eta` (Estimated Time of Arrival) que aceita `distancia_km` e `velocidade_media`.
# Configure `velocidade_media` para ter o valor padrão de 60.
# A função deve retornar o tempo de viagem (distancia / velocidade). Teste chamando com apenas a distância.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Crie uma função chamada `min_max_pesos` que recebe uma lista de pesos.
# Ela deve retornar o peso mínimo e o máximo juntos (uma tupla). Use min() e max().
# Teste com a lista: [10, 50, 5, 120, 30]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Crie uma função chamada `formatar_motoristas` que receba `*args` (uma quantidade variável de nomes).
# Adicione uma docstring explicando o que a função faz.
# A função deve iterar pelos argumentos e retornar uma lista com todos os nomes em letras maiúsculas.
# Chame a função passando: "João", "Maria", "Pedro", "Ana".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


"""
GABARITO:

# Exercício 1
def soma_pesos(p1, p2):
    return p1 + p2
print(soma_pesos(15.5, 20.0))

# Exercício 2
def verificar_caminhao(placa):
    if placa == "":
        return "Placa inválida"
    return f"Placa registrada: {placa}"
print(verificar_caminhao("ABC-1234"))

# Exercício 3
def calcular_eta(distancia_km, velocidade_media=60):
    return distancia_km / velocidade_media
print(f"Tempo de viagem: {calcular_eta(120)} horas")

# Exercício 4
def min_max_pesos(pesos):
    return (min(pesos), max(pesos))
menor, maior = min_max_pesos([10, 50, 5, 120, 30])
print(f"Menor: {menor}kg | Maior: {maior}kg")

# Exercício 5
def formatar_motoristas(*args):
    \"\"\"
    Recebe um número variável de nomes de motoristas e os retorna em maiúsculas.
    \"\"\"
    return [motorista.upper() for motorista in args]

lista_formatada = formatar_motoristas("João", "Maria", "Pedro", "Ana")
print(lista_formatada)
"""

o como você faria no Excel ou no papel.
Dica de Código: Lembre-se da sintaxe vista na aula.

🤖 PROMPT TUTOR PARA A IA (Copie e cole se travar):
"Atue como meu tutor de Python. Estou tentando resolver um exercício sobre [TEMA]. 
Meu código até agora é este: [COLE AQUI]. 
Não me dê a resposta direta. Aponte o erro e me dê uma dica de como consertar."
"""

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

"""
Exercícios — Aula 7: Funções
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

# Contexto logístico: Modularizar lógicas de cálculo, verificação de dados e geração de relatórios.

# Exercício 1 — [Nível: Básico]
# Crie uma função chamada `soma_pesos` que recebe o peso de dois pacotes e retorna a soma deles.
# Chame a função passando 15.5 e 20.0 e imprima o resultado.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Crie uma função `verificar_caminhao` que recebe uma `placa`. 
# Se a placa for uma string vazia (""), retorne "Placa inválida".
# Senão retorne "Placa registrada: [placa]".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Escreva uma função `calcular_eta` (Estimated Time of Arrival) que aceita `distancia_km` e `velocidade_media`.
# Configure `velocidade_media` para ter o valor padrão de 60.
# A função deve retornar o tempo de viagem (distancia / velocidade). Teste chamando com apenas a distância.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Crie uma função chamada `min_max_pesos` que recebe uma lista de pesos.
# Ela deve retornar o peso mínimo e o máximo juntos (uma tupla). Use min() e max().
# Teste com a lista: [10, 50, 5, 120, 30]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Crie uma função chamada `formatar_motoristas` que receba `*args` (uma quantidade variável de nomes).
# Adicione uma docstring explicando o que a função faz.
# A função deve iterar pelos argumentos e retornar uma lista com todos os nomes em letras maiúsculas.
# Chame a função passando: "João", "Maria", "Pedro", "Ana".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


"""
GABARITO:

# Exercício 1
def soma_pesos(p1, p2):
    return p1 + p2
print(soma_pesos(15.5, 20.0))

# Exercício 2
def verificar_caminhao(placa):
    if placa == "":
        return "Placa inválida"
    return f"Placa registrada: {placa}"
print(verificar_caminhao("ABC-1234"))

# Exercício 3
def calcular_eta(distancia_km, velocidade_media=60):
    return distancia_km / velocidade_media
print(f"Tempo de viagem: {calcular_eta(120)} horas")

# Exercício 4
def min_max_pesos(pesos):
    return (min(pesos), max(pesos))
menor, maior = min_max_pesos([10, 50, 5, 120, 30])
print(f"Menor: {menor}kg | Maior: {maior}kg")

# Exercício 5
def formatar_motoristas(*args):
    \"\"\"
    Recebe um número variável de nomes de motoristas e os retorna em maiúsculas.
    \"\"\"
    return [motorista.upper() for motorista in args]

lista_formatada = formatar_motoristas("João", "Maria", "Pedro", "Ana")
print(lista_formatada)
"""





# ==============================================================================
# GABARITO (Tente antes de olhar!)
# ==============================================================================
"""
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

"""
Exercícios — Aula 7: Funções
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

# Contexto logístico: Modularizar lógicas de cálculo, verificação de dados e geração de relatórios.

# Exercício 1 — [Nível: Básico]
# Crie uma função chamada `soma_pesos` que recebe o peso de dois pacotes e retorna a soma deles.
# Chame a função passando 15.5 e 20.0 e imprima o resultado.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Crie uma função `verificar_caminhao` que recebe uma `placa`. 
# Se a placa for uma string vazia (""), retorne "Placa inválida".
# Senão retorne "Placa registrada: [placa]".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Escreva uma função `calcular_eta` (Estimated Time of Arrival) que aceita `distancia_km` e `velocidade_media`.
# Configure `velocidade_media` para ter o valor padrão de 60.
# A função deve retornar o tempo de viagem (distancia / velocidade). Teste chamando com apenas a distância.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Crie uma função chamada `min_max_pesos` que recebe uma lista de pesos.
# Ela deve retornar o peso mínimo e o máximo juntos (uma tupla). Use min() e max().
# Teste com a lista: [10, 50, 5, 120, 30]
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Crie uma função chamada `formatar_motoristas` que receba `*args` (uma quantidade variável de nomes).
# Adicione uma docstring explicando o que a função faz.
# A função deve iterar pelos argumentos e retornar uma lista com todos os nomes em letras maiúsculas.
# Chame a função passando: "João", "Maria", "Pedro", "Ana".
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


"""
GABARITO:

# Exercício 1
def soma_pesos(p1, p2):
    return p1 + p2
print(soma_pesos(15.5, 20.0))

# Exercício 2
def verificar_caminhao(placa):
    if placa == "":
        return "Placa inválida"
    return f"Placa registrada: {placa}"
print(verificar_caminhao("ABC-1234"))

# Exercício 3
def calcular_eta(distancia_km, velocidade_media=60):
    return distancia_km / velocidade_media
print(f"Tempo de viagem: {calcular_eta(120)} horas")

# Exercício 4
def min_max_pesos(pesos):
    return (min(pesos), max(pesos))
menor, maior = min_max_pesos([10, 50, 5, 120, 30])
print(f"Menor: {menor}kg | Maior: {maior}kg")

# Exercício 5
def formatar_motoristas(*args):
    \"\"\"
    Recebe um número variável de nomes de motoristas e os retorna em maiúsculas.
    \"\"\"
    return [motorista.upper() for motorista in args]

lista_formatada = formatar_motoristas("João", "Maria", "Pedro", "Ana")
print(lista_formatada)