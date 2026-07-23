# -*- coding: utf-8 -*-
"""
Gabarito Oficial de Referência - aula_09b_exercicios_gabarito
Curso: Python + IA para Automação em Logística
"""

# ======================================
# GABARITO MANUAL COMENTADO PASSO A PASSO
# ======================================

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




###################### GABARITO ######################

# 1. 
# class Vehicle:
#     def __init__(self, model, plate):
#         self.model = model
#         self.plate = plate

# class Driver:
#     def __init__(self, name, vehicle):
#         self.name = name
#         self.vehicle = vehicle

my_truck = Vehicle("Scania", "ABC-9999")
my_driver = Driver("Pedro", my_truck)

print(f"O motorista {my_driver.name} dirige um {my_driver.vehicle.model}")

# 2.
# class Driver:
#     def __init__(self, name, vehicle):
#         self.name = name
#         self.vehicle = vehicle
        
#     def to_dict(self):
#         return {
#             "name": self.name,
#             "vehicle": {
#                 "model": self.vehicle.model,
#                 "plate": self.vehicle.plate
#             }
#         }

my_truck = Vehicle("Scania", "ABC-9999")
my_driver = Driver("Pedro", my_truck)
driver_dict = my_driver.to_dict()
print(driver_dict)

# 3.
import json

# Salvando
# with open("dados_motorista.json", "w") as file:
#     json.dump(driver_dict, file, indent=4)
    
# Carregando
# with open("dados_motorista.json", "r") as file:
#     loaded_data = json.load(file)

print("Dados lidos do arquivo JSON:")
print(loaded_data)

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