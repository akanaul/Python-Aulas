# -*- coding: utf-8 -*-
"""
Exercícios - aula_09a_exercicios_manual
Curso: Python + IA para Automação em Logística

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado.
- Use a IA Antigravity no MODO TUTOR (pedindo dicas de lógica).
"""

# -*- coding: utf-8 -*-
# Exercícios - aula_09a_exercicios_manual
# Curso: Python + IA para Automação

# INSTRUÇÕES:


# INSTRUÇÕES:
# - Resolva cada exercício no espaço indicado
# - O gabarito está comentado ao final do arquivo

# EXERCÍCIO 1 — [Nível: Básico]
# O setor logístico precisa calcular o prazo final de uma devolução.
# Importe o módulo `datetime` e adicione 7 dias (usando timedelta) à data de hoje.
# Imprima o resultado.
print("--- Exercício 1 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 2 — [Nível: Básico]
# Crie uma classe `Person` com um construtor (__init__) que receba `name` e `cpf`.
# Depois, crie uma instância (objeto) sua e imprima o nome.
print("\n--- Exercício 2 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 3 — [Nível: Intermediário]
# Crie uma classe `Driver` que HERDE de `Person` (do exercício 2).
# No construtor de `Driver`, além de name e cpf, adicione `plate` (placa) e `route` (rota).
# Não esqueça do super().__init__().
print("\n--- Exercício 3 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 4 — [Nível: Intermediário]
# Na classe `Driver` criada acima, adicione um método chamado `update_route(new_route)`
# que atualize o atributo `route` e dê um print avisando que a rota mudou.
# Instancie o motorista e teste o método.
print("\n--- Exercício 4 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 5 — [Nível: Desafio]
# Na mesma classe, adicione o método mágico `__str__` para retornar uma string formatada:
# "Motorista: <nome> | CPF: <cpf> | Placa: <plate> | Rota: <route>"
# Imprima o objeto instanciado.
print("\n--- Exercício 5 ---")
# SEU CÓDIGO AQUI




###################### GABARITO ######################

# 1. 
from datetime import date, timedelta
today_date = date.today()
return_deadline = today_date + timedelta(days=7)
print(f"Prazo de devolução: {return_deadline}")

# 2.
# class Person:
#     def __init__(self, name, cpf):
#         self.name = name
#         self.cpf = cpf

my_person = Person("João", "111.111.111-11")
print(my_person.name)

# 3, 4 e 5:
# class Driver(Person):
#     def __init__(self, name, cpf, plate, route):
#         super().__init__(name, cpf)
#         self.plate = plate
#         self.route = route
        
#     def update_route(self, new_route):
#         self.route = new_route
#         print(f"A rota de {self.name} foi atualizada para {self.route}")
        
#     def __str__(self):
#         return f"Motorista: {self.name} | CPF: {self.cpf} | Placa: {self.plate} | Rota: {self.route}"

driver_maria = Driver("Maria", "222.222.222-22", "XYZ-9876", "SP-RJ")
driver_maria.update_route("SP-MG")
print(driver_maria)

# ---------------------------------------------------------------------------
# SISTEMA DE AUDITORIA COM IA
# ---------------------------------------------------------------------------
# INSTRUÇÕES:
# Peça para o Antigravity (ou outra IA) auditar a sua solução final usando o 
# "Prompt de Sistema de Auditoria" ensinado na aula.
# 
# GABARITO DE AUDITORIA (O que a IA deve encontrar/sugerir):
# - Uso de try/except para capturar falhas imprevistas.
# - Boas práticas de nomenclatura e legibilidade.
# - Se houver manipulação de UI/arquivos, verificar se há proteções (failsafe, close).
# ---------------------------------------------------------------------------

# passo a # ==============================================================================
# 🛑 REGRA DE OURO PARA O APRENDIZADO DE LOGÍSTICA:
# 1. Tente resolver cada exercício SOZINHO primeiro.
# 2. Se travar, use a dica do exercício ou peça ajuda ao Antigravity (IA copiloto)
#    usando os prompts de dica sugeridos (sem pedir a resposta direta!).
# 3. O GABARITO DETALHADO E COMENTADO está no final deste arquivo.
#    Consulte o gabarito APENAS se tiver tentado de verdade e continuar travado!
# ==============================================================================

# INSTRUÇÕES:
# - Resolva cada exercício no espaço indicado
# - O gabarito está comentado ao final do arquivo

# EXERCÍCIO 1 — [Nível: Básico]
# O setor logístico precisa calcular o prazo final de uma devolução.
# Importe o módulo `datetime` e adicione 7 dias (usando timedelta) à data de hoje.
# Imprima o resultado.
print("--- Exercício 1 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 2 — [Nível: Básico]
# Crie uma classe `Person` com um construtor (__init__) que receba `name` e `cpf`.
# Depois, crie uma instância (objeto) sua e imprima o nome.
print("\n--- Exercício 2 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 3 — [Nível: Intermediário]
# Crie uma classe `Driver` que HERDE de `Person` (do exercício 2).
# No construtor de `Driver`, além de name e cpf, adicione `plate` (placa) e `route` (rota).
# Não esqueça do super().__init__().
print("\n--- Exercício 3 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 4 — [Nível: Intermediário]
# Na classe `Driver` criada acima, adicione um método chamado `update_route(new_route)`
# que atualize o atributo `route` e dê um print avisando que a rota mudou.
# Instancie o motorista e teste o método.
print("\n--- Exercício 4 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 5 — [Nível: Desafio]
# Na mesma classe, adicione o método mágico `__str__` para retornar uma string formatada:
# "Motorista: <nome> | CPF: <cpf> | Placa: <plate> | Rota: <route>"
# Imprima o objeto instanciado.
print("\n--- Exercício 5 ---")
# SEU CÓDIGO AQUI




###################### GABARITO ######################

# 1. 
from datetime import date, timedelta
today_date = date.today()
return_deadline = today_date + timedelta(days=7)
print(f"Prazo de devolução: {return_deadline}")

# 2.
# class Person:
#     def __init__(self, name, cpf):
#         self.name = name
#         self.cpf = cpf

my_person = Person("João", "111.111.111-11")
print(my_person.name)

# 3, 4 e 5:
# class Driver(Person):
#     def __init__(self, name, cpf, plate, route):
#         super().__init__(name, cpf)
#         self.plate = plate
#         self.route = route
        
#     def update_route(self, new_route):
#         self.route = new_route
#         print(f"A rota de {self.name} foi atualizada para {self.route}")
        
#     def __str__(self):
#         return f"Motorista: {self.name} | CPF: {self.cpf} | Placa: {self.plate} | Rota: {self.route}"

driver_maria = Driver("Maria", "222.222.222-22", "XYZ-9876", "SP-RJ")
driver_maria.update_route("SP-MG")
print(driver_maria)

# ---------------------------------------------------------------------------
# SISTEMA DE AUDITORIA COM IA
# ---------------------------------------------------------------------------
# INSTRUÇÕES:
# Peça para o Antigravity (ou outra IA) auditar a sua solução final usando o 
# "Prompt de Sistema de Auditoria" ensinado na aula.
# 
# GABARITO DE AUDITORIA (O que a IA deve encontrar/sugerir):
# - Uso de try/except para capturar falhas imprevistas.
# - Boas práticas de nomenclatura e legibilidade.
# - Se houver manipulação de UI/arquivos, verificar se há proteções (failsafe, close).
# ---------------------------------------------------------------------------

# passo como você faria no Excel ou no papel.
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

# INSTRUÇÕES:
# - Resolva cada exercício no espaço indicado
# - O gabarito está comentado ao final do arquivo

# EXERCÍCIO 1 — [Nível: Básico]
# O setor logístico precisa calcular o prazo final de uma devolução.
# Importe o módulo `datetime` e adicione 7 dias (usando timedelta) à data de hoje.
# Imprima o resultado.
print("--- Exercício 1 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 2 — [Nível: Básico]
# Crie uma classe `Person` com um construtor (__init__) que receba `name` e `cpf`.
# Depois, crie uma instância (objeto) sua e imprima o nome.
print("\n--- Exercício 2 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 3 — [Nível: Intermediário]
# Crie uma classe `Driver` que HERDE de `Person` (do exercício 2).
# No construtor de `Driver`, além de name e cpf, adicione `plate` (placa) e `route` (rota).
# Não esqueça do super().__init__().
print("\n--- Exercício 3 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 4 — [Nível: Intermediário]
# Na classe `Driver` criada acima, adicione um método chamado `update_route(new_route)`
# que atualize o atributo `route` e dê um print avisando que a rota mudou.
# Instancie o motorista e teste o método.
print("\n--- Exercício 4 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 5 — [Nível: Desafio]
# Na mesma classe, adicione o método mágico `__str__` para retornar uma string formatada:
# "Motorista: <nome> | CPF: <cpf> | Placa: <plate> | Rota: <route>"
# Imprima o objeto instanciado.
print("\n--- Exercício 5 ---")
# SEU CÓDIGO AQUI




###################### GABARITO ######################

# 1. 
from datetime import date, timedelta
today_date = date.today()
return_deadline = today_date + timedelta(days=7)
print(f"Prazo de devolução: {return_deadline}")

# 2.
# class Person:
#     def __init__(self, name, cpf):
#         self.name = name
#         self.cpf = cpf

my_person = Person("João", "111.111.111-11")
print(my_person.name)

# 3, 4 e 5:
# class Driver(Person):
#     def __init__(self, name, cpf, plate, route):
#         super().__init__(name, cpf)
#         self.plate = plate
#         self.route = route
        
#     def update_route(self, new_route):
#         self.route = new_route
#         print(f"A rota de {self.name} foi atualizada para {self.route}")
        
#     def __str__(self):
#         return f"Motorista: {self.name} | CPF: {self.cpf} | Placa: {self.plate} | Rota: {self.route}"

driver_maria = Driver("Maria", "222.222.222-22", "XYZ-9876", "SP-RJ")
driver_maria.update_route("SP-MG")
print(driver_maria)

# ---------------------------------------------------------------------------
# SISTEMA DE AUDITORIA COM IA
# ---------------------------------------------------------------------------
# INSTRUÇÕES:
# Peça para o Antigravity (ou outra IA) auditar a sua solução final usando o 
# "Prompt de Sistema de Auditoria" ensinado na aula.
# 
# GABARITO DE AUDITORIA (O que a IA deve encontrar/sugerir):
# - Uso de try/except para capturar falhas imprevistas.
# - Boas práticas de nomenclatura e legibilidade.
# - Se houver manipulação de UI/arquivos, verificar se há proteções (failsafe, close).
# ---------------------------------------------------------------------------

pass

# 💡 O Gabarito Manual Comentado está no arquivo separado: aula_09a_exercicios_gabarito.py