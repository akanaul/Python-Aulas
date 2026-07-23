"""
======================================
GABARITO MANUAL COMENTADO PASSO A PASSO
======================================
"""

# Exercício 1
carrier_name = "Expresso Log"
total_invoices = 150
total_freight_cost = 4500.50

print(type(carrier_name))
print(type(total_invoices))
print(type(total_freight_cost))

# Exercício 2
vehicle_plate = input("Informe a placa do veículo: ")
print(f"Bem-vindo(a)! Veículo {vehicle_plate} autorizado na portaria.")

# Exercício 3
length = 0.5
width = 0.4
height = 0.3
cubage_factor = 300

cubed_weight = (length * width * height) * cubage_factor
print(f"O peso cubado da caixa é: {cubed_weight} kg")

# Exercício 4
is_driver_licensed = True
is_fueled = True

is_cleared = is_driver_licensed and is_fueled
print(f"O caminhão está liberado para viagem? {is_cleared}")

# Exercício 5
distance_km = float(input("Digite a distância da rota em KM: "))
fuel_efficiency = 3.5
liters_needed = distance_km / fuel_efficiency

print(f"Para a rota de {distance_km}km, serão necessários {liters_needed} litros de diesel.")
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
Exercícios — Aula 2: Variáveis e Operadores
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

# Contexto: Seu sistema logístico precisa calcular algumas métricas da operação do dia.

# Exercício 1 — [Nível: Básico]
# Crie variáveis para: nome da transportadora, quantidade de notas fiscais (NF) e valor total do frete.
# Imprima o tipo de cada variável usando a função type().
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 2 — [Nível: Básico]
# Receba via input() a placa do veículo que acabou de chegar na portaria.
# Imprima uma mensagem de boas-vindas informando a placa utilizando f-strings.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 3 — [Nível: Intermediário]
# Calcule o peso cubado de uma caixa de papelão.
# Crie as variáveis: length (comprimento) = 0.5m, width (largura) = 0.4m, height (altura) = 0.3m.
# A fórmula é: volume (length * width * height) vezes o fator de cubagem (300).
# Imprima o resultado.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 4 — [Nível: Intermediário]
# Verifique se o veículo está apto para viagem (liberação de pátio).
# Crie duas variáveis booleanas: is_driver_licensed (tem CNH válida) e is_fueled (tem combustível).
# Defina as duas como True. O caminhão é liberado (is_cleared) se ambas forem verdadeiras.
# Imprima o resultado booleano da liberação.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 5 — [Nível: Desafio]
# Um caminhão faz 3.5 km/l de diesel. 
# Peça ao usuário (via input) a distância total da rota em km (lembre de converter para float).
# Calcule os litros necessários (distância / rendimento) e imprima o resultado com f-string.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:




"""
======================================
GABARITO COMENTADO
======================================
# Exercício 1
carrier_name = "Expresso Log"
total_invoices = 150
total_freight_cost = 4500.50

print(type(carrier_name))
print(type(total_invoices))
print(type(total_freight_cost))

# Exercício 2
vehicle_plate = input("Informe a placa do veículo: ")
print(f"Bem-vindo(a)! Veículo {vehicle_plate} autorizado na portaria.")

# Exercício 3
length = 0.5
width = 0.4
height = 0.3
cubage_factor = 300

cubed_weight = (length * width * height) * cubage_factor
print(f"O peso cubado da caixa é: {cubed_weight} kg")

# Exercício 4
is_driver_licensed = True
is_fueled = True

is_cleared = is_driver_licensed and is_fueled
print(f"O caminhão está liberado para viagem? {is_cleared}")

# Exercício 5
distance_km = float(input("Digite a distância da rota em KM: "))
fuel_efficiency = 3.5
liters_needed = distance_km / fuel_efficiency

print(f"Para a rota de {distance_km}km, serão necessários {liters_needed} litros de diesel.")
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
Exercícios — Aula 2: Variáveis e Operadores
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

# Contexto: Seu sistema logístico precisa calcular algumas métricas da operação do dia.

# Exercício 1 — [Nível: Básico]
# Crie variáveis para: nome da transportadora, quantidade de notas fiscais (NF) e valor total do frete.
# Imprima o tipo de cada variável usando a função type().
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 2 — [Nível: Básico]
# Receba via input() a placa do veículo que acabou de chegar na portaria.
# Imprima uma mensagem de boas-vindas informando a placa utilizando f-strings.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 3 — [Nível: Intermediário]
# Calcule o peso cubado de uma caixa de papelão.
# Crie as variáveis: length (comprimento) = 0.5m, width (largura) = 0.4m, height (altura) = 0.3m.
# A fórmula é: volume (length * width * height) vezes o fator de cubagem (300).
# Imprima o resultado.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 4 — [Nível: Intermediário]
# Verifique se o veículo está apto para viagem (liberação de pátio).
# Crie duas variáveis booleanas: is_driver_licensed (tem CNH válida) e is_fueled (tem combustível).
# Defina as duas como True. O caminhão é liberado (is_cleared) se ambas forem verdadeiras.
# Imprima o resultado booleano da liberação.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 5 — [Nível: Desafio]
# Um caminhão faz 3.5 km/l de diesel. 
# Peça ao usuário (via input) a distância total da rota em km (lembre de converter para float).
# Calcule os litros necessários (distância / rendimento) e imprima o resultado com f-string.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:




"""
======================================
GABARITO COMENTADO
======================================
# Exercício 1
carrier_name = "Expresso Log"
total_invoices = 150
total_freight_cost = 4500.50

print(type(carrier_name))
print(type(total_invoices))
print(type(total_freight_cost))

# Exercício 2
vehicle_plate = input("Informe a placa do veículo: ")
print(f"Bem-vindo(a)! Veículo {vehicle_plate} autorizado na portaria.")

# Exercício 3
length = 0.5
width = 0.4
height = 0.3
cubage_factor = 300

cubed_weight = (length * width * height) * cubage_factor
print(f"O peso cubado da caixa é: {cubed_weight} kg")

# Exercício 4
is_driver_licensed = True
is_fueled = True

is_cleared = is_driver_licensed and is_fueled
print(f"O caminhão está liberado para viagem? {is_cleared}")

# Exercício 5
distance_km = float(input("Digite a distância da rota em KM: "))
fuel_efficiency = 3.5
liters_needed = distance_km / fuel_efficiency

print(f"Para a rota de {distance_km}km, serão necessários {liters_needed} litros de diesel.")
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
Exercícios — Aula 2: Variáveis e Operadores
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

# Contexto: Seu sistema logístico precisa calcular algumas métricas da operação do dia.

# Exercício 1 — [Nível: Básico]
# Crie variáveis para: nome da transportadora, quantidade de notas fiscais (NF) e valor total do frete.
# Imprima o tipo de cada variável usando a função type().
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 2 — [Nível: Básico]
# Receba via input() a placa do veículo que acabou de chegar na portaria.
# Imprima uma mensagem de boas-vindas informando a placa utilizando f-strings.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 3 — [Nível: Intermediário]
# Calcule o peso cubado de uma caixa de papelão.
# Crie as variáveis: length (comprimento) = 0.5m, width (largura) = 0.4m, height (altura) = 0.3m.
# A fórmula é: volume (length * width * height) vezes o fator de cubagem (300).
# Imprima o resultado.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 4 — [Nível: Intermediário]
# Verifique se o veículo está apto para viagem (liberação de pátio).
# Crie duas variáveis booleanas: is_driver_licensed (tem CNH válida) e is_fueled (tem combustível).
# Defina as duas como True. O caminhão é liberado (is_cleared) se ambas forem verdadeiras.
# Imprima o resultado booleano da liberação.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:


# Exercício 5 — [Nível: Desafio]
# Um caminhão faz 3.5 km/l de diesel. 
# Peça ao usuário (via input) a distância total da rota em km (lembre de converter para float).
# Calcule os litros necessários (distância / rendimento) e imprima o resultado com f-string.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui:




"""
======================================
GABARITO COMENTADO
======================================
# Exercício 1
carrier_name = "Expresso Log"
total_invoices = 150
total_freight_cost = 4500.50

print(type(carrier_name))
print(type(total_invoices))
print(type(total_freight_cost))

# Exercício 2
vehicle_plate = input("Informe a placa do veículo: ")
print(f"Bem-vindo(a)! Veículo {vehicle_plate} autorizado na portaria.")

# Exercício 3
length = 0.5
width = 0.4
height = 0.3
cubage_factor = 300

cubed_weight = (length * width * height) * cubage_factor
print(f"O peso cubado da caixa é: {cubed_weight} kg")

# Exercício 4
is_driver_licensed = True
is_fueled = True

is_cleared = is_driver_licensed and is_fueled
print(f"O caminhão está liberado para viagem? {is_cleared}")

# Exercício 5
distance_km = float(input("Digite a distância da rota em KM: "))
fuel_efficiency = 3.5
liters_needed = distance_km / fuel_efficiency

print(f"Para a rota de {distance_km}km, serão necessários {liters_needed} litros de diesel.")