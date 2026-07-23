# -*- coding: utf-8 -*-
"""
Gabarito Oficial de Referência - aula_14_exercicios_gabarito
Curso: Python + IA para Automação em Logística
"""

# ======================================
# GABARITO MANUAL COMENTADO PASSO A PASSO
# ======================================

# Ex 1:
# logging.basicConfig(filename='operacao.log', level=logging.INFO, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Iniciando turno")
logging.error("Falha na conexão com ERP")

# Ex 2:
# def buscar_imagem():
#     try:
#         logging.info("Buscando imagem...")
#         img = pyautogui.locateOnScreen("imagem_que_nao_existe.png")
#         if img is None:
#             raise Exception("Imagem não encontrada")
#         print("Encontrada!")
#     except Exception as e:
#         logging.error(f"Erro na busca: {e}")
#         print(f"Erro capturado: {e}")

buscar_imagem()

# Ex 3:
# nfes = [
#     {"numero": "1001", "valor": 500},
#     {"numero": "1002", "valor": 800},
#     {"numero": "1003", "valor": 1200}
# ]

# for nfe in nfes:
#     print(f"Processando NFE {nfe['numero']}...")
#     time.sleep(1)
#     logging.info(f"NFE {nfe['numero']} de valor R${nfe['valor']} processada com sucesso.")

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



import pyautogui
import time
import logging

pyautogui.FAILSAFE = True

# Exercício 1 — [Nível: Básico]
# Configure o módulo logging para escrever num arquivo chamado 'operacao.log'. 
# Registre uma mensagem de INFO "Iniciando turno" e um ERROR "Falha na conexão com ERP".

print("--- Exercicio 1 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass


# Exercício 2 — [Nível: Intermediário]
# Escreva uma função que tente achar uma imagem na tela (ex: "imagem_teste.png") com locateOnScreen. 
# Coloque em um bloco try/except. Se der erro, registre no log e avise no print.

print("--- Exercicio 2 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass


# Exercício 3 — [Nível: Desafio]
# Crie uma lista de dicionários com 3 NFEs (numero e valor). 
# Faça um loop que "processa" (apenas prints e time.sleep de 1s) e salva cada sucesso no arquivo de log.

print("--- Exercicio 3 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

# GABARITO:

# Ex 1:
# logging.basicConfig(filename='operacao.log', level=logging.INFO, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Iniciando turno")
logging.error("Falha na conexão com ERP")

# Ex 2:
# def buscar_imagem():
#     try:
#         logging.info("Buscando imagem...")
#         img = pyautogui.locateOnScreen("imagem_que_nao_existe.png")
#         if img is None:
#             raise Exception("Imagem não encontrada")
#         print("Encontrada!")
#     except Exception as e:
#         logging.error(f"Erro na busca: {e}")
#         print(f"Erro capturado: {e}")

buscar_imagem()

# Ex 3:
# nfes = [
#     {"numero": "1001", "valor": 500},
#     {"numero": "1002", "valor": 800},
#     {"numero": "1003", "valor": 1200}
# ]

# for nfe in nfes:
#     print(f"Processando NFE {nfe['numero']}...")
#     time.sleep(1)
#     logging.info(f"NFE {nfe['numero']} de valor R${nfe['valor']} processada com sucesso.")

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



import pyautogui
import time
import logging

pyautogui.FAILSAFE = True

# Exercício 1 — [Nível: Básico]
# Configure o módulo logging para escrever num arquivo chamado 'operacao.log'. 
# Registre uma mensagem de INFO "Iniciando turno" e um ERROR "Falha na conexão com ERP".

print("--- Exercicio 1 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass


# Exercício 2 — [Nível: Intermediário]
# Escreva uma função que tente achar uma imagem na tela (ex: "imagem_teste.png") com locateOnScreen. 
# Coloque em um bloco try/except. Se der erro, registre no log e avise no print.

print("--- Exercicio 2 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass


# Exercício 3 — [Nível: Desafio]
# Crie uma lista de dicionários com 3 NFEs (numero e valor). 
# Faça um loop que "processa" (apenas prints e time.sleep de 1s) e salva cada sucesso no arquivo de log.

print("--- Exercicio 3 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

# GABARITO:

# Ex 1:
# logging.basicConfig(filename='operacao.log', level=logging.INFO, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Iniciando turno")
logging.error("Falha na conexão com ERP")

# Ex 2:
# def buscar_imagem():
#     try:
#         logging.info("Buscando imagem...")
#         img = pyautogui.locateOnScreen("imagem_que_nao_existe.png")
#         if img is None:
#             raise Exception("Imagem não encontrada")
#         print("Encontrada!")
#     except Exception as e:
#         logging.error(f"Erro na busca: {e}")
#         print(f"Erro capturado: {e}")

buscar_imagem()

# Ex 3:
# nfes = [
#     {"numero": "1001", "valor": 500},
#     {"numero": "1002", "valor": 800},
#     {"numero": "1003", "valor": 1200}
# ]

# for nfe in nfes:
#     print(f"Processando NFE {nfe['numero']}...")
#     time.sleep(1)
#     logging.info(f"NFE {nfe['numero']} de valor R${nfe['valor']} processada com sucesso.")

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



import pyautogui
import time
import logging

pyautogui.FAILSAFE = True

# Exercício 1 — [Nível: Básico]
# Configure o módulo logging para escrever num arquivo chamado 'operacao.log'. 
# Registre uma mensagem de INFO "Iniciando turno" e um ERROR "Falha na conexão com ERP".

print("--- Exercicio 1 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass


# Exercício 2 — [Nível: Intermediário]
# Escreva uma função que tente achar uma imagem na tela (ex: "imagem_teste.png") com locateOnScreen. 
# Coloque em um bloco try/except. Se der erro, registre no log e avise no print.

print("--- Exercicio 2 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass


# Exercício 3 — [Nível: Desafio]
# Crie uma lista de dicionários com 3 NFEs (numero e valor). 
# Faça um loop que "processa" (apenas prints e time.sleep de 1s) e salva cada sucesso no arquivo de log.

print("--- Exercicio 3 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

# GABARITO:

# Ex 1:
# logging.basicConfig(filename='operacao.log', level=logging.INFO, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Iniciando turno")
logging.error("Falha na conexão com ERP")

# Ex 2:
# def buscar_imagem():
#     try:
#         logging.info("Buscando imagem...")
#         img = pyautogui.locateOnScreen("imagem_que_nao_existe.png")
#         if img is None:
#             raise Exception("Imagem não encontrada")
#         print("Encontrada!")
#     except Exception as e:
#         logging.error(f"Erro na busca: {e}")
#         print(f"Erro capturado: {e}")

buscar_imagem()

# Ex 3:
# nfes = [
#     {"numero": "1001", "valor": 500},
#     {"numero": "1002", "valor": 800},
#     {"numero": "1003", "valor": 1200}
# ]

# for nfe in nfes:
#     print(f"Processando NFE {nfe['numero']}...")
#     time.sleep(1)
#     logging.info(f"NFE {nfe['numero']} de valor R${nfe['valor']} processada com sucesso.")

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