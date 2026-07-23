"""
Exercícios — Aula 09b: Título
Curso: Python + IA para Automação em Logística

⭐ REGRA DE OURO ⭐
Resolva este exercício MANUALMENTE.
Use a IA **apenas** no MODO TUTOR (pedindo dicas, não a resposta).

Dica de Lógica: Pense # ==============================================================================
# 🛑 REGRA DE OURO PARA O APRENDIZADO DE LOGÍSTICA:
# 1. Tente resolver cada exercício SOZINHO primeiro.
# 2. Se travar, use a dica do exercício ou peça ajuda ao Antigravity (IA copiloto)
#    usando os prompts de dica sugeridos (sem pedir a resposta direta!).
# 3. O GABARITO DETALHADO E COMENTADO está no final deste arquivo.
#    Consulte o gabarito APENAS se tiver tentado de verdade e continuar travado!
# ==============================================================================

"""
Exercícios — Aula 9B: POO Prático, Composição e Persistência
Curso: Python + IA para Automação em Logística
Instrutor: Seu Nome

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

import json

# EXERCÍCIO 1 — [Nível: Básico]
# Composição: Crie uma classe `Vehicle` com `model` e `plate`.
# Depois, crie uma classe `Driver` com `name` e que receba um objeto `Vehicle` no construtor.
# Imprima o nome do motorista e o modelo do veículo acessando pela composição.
print("--- Exercício 1 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 2 — [Nível: Intermediário]
# Na classe `Driver` (do ex 1), crie o método `to_dict()` para converter 
# o motorista e o seu veículo em um dicionário de dicionários (aninhado).
# Exemplo do retorno: {'name': 'Pedro', 'vehicle': {'model': 'Fiorino', 'plate': 'ABC-123'}}
print("\n--- Exercício 2 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 3 — [Nível: Desafio]
# Persistência: Pegue o dicionário gerado no exercício 2 e salve-o em um arquivo 
# chamado `dados_motorista.json` usando `json.dump()`. 
# Depois, abra o arquivo com `json.load()` e imprima o conteúdo na tela.
print("\n--- Exercício 3 ---")
# SEU CÓDIGO AQUI




"""
###################### GABARITO ######################

# 1. 
class Vehicle:
    def __init__(self, model, plate):
        self.model = model
        self.plate = plate

class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

my_truck = Vehicle("Scania", "ABC-9999")
my_driver = Driver("Pedro", my_truck)

print(f"O motorista {my_driver.name} dirige um {my_driver.vehicle.model}")

# 2.
class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle
        
    def to_dict(self):
        return {
            "name": self.name,
            "vehicle": {
                "model": self.vehicle.model,
                "plate": self.vehicle.plate
            }
        }

my_truck = Vehicle("Scania", "ABC-9999")
my_driver = Driver("Pedro", my_truck)
driver_dict = my_driver.to_dict()
print(driver_dict)

# 3.
import json

# Salvando
with open("dados_motorista.json", "w") as file:
    json.dump(driver_dict, file, indent=4)
    
# Carregando
with open("dados_motorista.json", "r") as file:
    loaded_data = json.load(file)

print("Dados lidos do arquivo JSON:")
print(loaded_data)
"""

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

passo a # ==============================================================================
# 🛑 REGRA DE OURO PARA O APRENDIZADO DE LOGÍSTICA:
# 1. Tente resolver cada exercício SOZINHO primeiro.
# 2. Se travar, use a dica do exercício ou peça ajuda ao Antigravity (IA copiloto)
#    usando os prompts de dica sugeridos (sem pedir a resposta direta!).
# 3. O GABARITO DETALHADO E COMENTADO está no final deste arquivo.
#    Consulte o gabarito APENAS se tiver tentado de verdade e continuar travado!
# ==============================================================================

"""
Exercícios — Aula 9B: POO Prático, Composição e Persistência
Curso: Python + IA para Automação em Logística
Instrutor: Seu Nome

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

import json

# EXERCÍCIO 1 — [Nível: Básico]
# Composição: Crie uma classe `Vehicle` com `model` e `plate`.
# Depois, crie uma classe `Driver` com `name` e que receba um objeto `Vehicle` no construtor.
# Imprima o nome do motorista e o modelo do veículo acessando pela composição.
print("--- Exercício 1 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 2 — [Nível: Intermediário]
# Na classe `Driver` (do ex 1), crie o método `to_dict()` para converter 
# o motorista e o seu veículo em um dicionário de dicionários (aninhado).
# Exemplo do retorno: {'name': 'Pedro', 'vehicle': {'model': 'Fiorino', 'plate': 'ABC-123'}}
print("\n--- Exercício 2 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 3 — [Nível: Desafio]
# Persistência: Pegue o dicionário gerado no exercício 2 e salve-o em um arquivo 
# chamado `dados_motorista.json` usando `json.dump()`. 
# Depois, abra o arquivo com `json.load()` e imprima o conteúdo na tela.
print("\n--- Exercício 3 ---")
# SEU CÓDIGO AQUI




"""
###################### GABARITO ######################

# 1. 
class Vehicle:
    def __init__(self, model, plate):
        self.model = model
        self.plate = plate

class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

my_truck = Vehicle("Scania", "ABC-9999")
my_driver = Driver("Pedro", my_truck)

print(f"O motorista {my_driver.name} dirige um {my_driver.vehicle.model}")

# 2.
class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle
        
    def to_dict(self):
        return {
            "name": self.name,
            "vehicle": {
                "model": self.vehicle.model,
                "plate": self.vehicle.plate
            }
        }

my_truck = Vehicle("Scania", "ABC-9999")
my_driver = Driver("Pedro", my_truck)
driver_dict = my_driver.to_dict()
print(driver_dict)

# 3.
import json

# Salvando
with open("dados_motorista.json", "w") as file:
    json.dump(driver_dict, file, indent=4)
    
# Carregando
with open("dados_motorista.json", "r") as file:
    loaded_data = json.load(file)

print("Dados lidos do arquivo JSON:")
print(loaded_data)
"""

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

passo como você faria no Excel ou no papel.
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
Exercícios — Aula 9B: POO Prático, Composição e Persistência
Curso: Python + IA para Automação em Logística
Instrutor: Seu Nome

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

import json

# EXERCÍCIO 1 — [Nível: Básico]
# Composição: Crie uma classe `Vehicle` com `model` e `plate`.
# Depois, crie uma classe `Driver` com `name` e que receba um objeto `Vehicle` no construtor.
# Imprima o nome do motorista e o modelo do veículo acessando pela composição.
print("--- Exercício 1 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 2 — [Nível: Intermediário]
# Na classe `Driver` (do ex 1), crie o método `to_dict()` para converter 
# o motorista e o seu veículo em um dicionário de dicionários (aninhado).
# Exemplo do retorno: {'name': 'Pedro', 'vehicle': {'model': 'Fiorino', 'plate': 'ABC-123'}}
print("\n--- Exercício 2 ---")
# SEU CÓDIGO AQUI


# EXERCÍCIO 3 — [Nível: Desafio]
# Persistência: Pegue o dicionário gerado no exercício 2 e salve-o em um arquivo 
# chamado `dados_motorista.json` usando `json.dump()`. 
# Depois, abra o arquivo com `json.load()` e imprima o conteúdo na tela.
print("\n--- Exercício 3 ---")
# SEU CÓDIGO AQUI




"""
###################### GABARITO ######################

# 1. 
class Vehicle:
    def __init__(self, model, plate):
        self.model = model
        self.plate = plate

class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

my_truck = Vehicle("Scania", "ABC-9999")
my_driver = Driver("Pedro", my_truck)

print(f"O motorista {my_driver.name} dirige um {my_driver.vehicle.model}")

# 2.
class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle
        
    def to_dict(self):
        return {
            "name": self.name,
            "vehicle": {
                "model": self.vehicle.model,
                "plate": self.vehicle.plate
            }
        }

my_truck = Vehicle("Scania", "ABC-9999")
my_driver = Driver("Pedro", my_truck)
driver_dict = my_driver.to_dict()
print(driver_dict)

# 3.
import json

# Salvando
with open("dados_motorista.json", "w") as file:
    json.dump(driver_dict, file, indent=4)
    
# Carregando
with open("dados_motorista.json", "r") as file:
    loaded_data = json.load(file)

print("Dados lidos do arquivo JSON:")
print(loaded_data)
"""

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

# 💡 O Gabarito Manual Comentado está no arquivo separado: aula_09b_exercicios_gabarito.py
