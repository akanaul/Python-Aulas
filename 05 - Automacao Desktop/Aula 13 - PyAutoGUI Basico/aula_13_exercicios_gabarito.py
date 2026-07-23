"""
======================================
GABARITO MANUAL COMENTADO PASSO A PASSO
======================================
"""

# Ex 1:
print(pyautogui.size())
time.sleep(2) # Dar tempo de botar o mouse em algum lugar
print(pyautogui.position())

# Ex 2:
time.sleep(3)
pyautogui.press('win')
time.sleep(1)
pyautogui.write('bloco de notas')
time.sleep(1)
pyautogui.press('enter')

# Ex 3:
time.sleep(4) # Espera o bloco abrir
texto = "Avaria confirmada! Carga recusada na portaria 2."
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('recusa_nfe.txt')
time.sleep(1)
pyautogui.press('enter')
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
Exercícios — Aula 13: PyAutoGUI Básico
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

import pyautogui
import time
import pyperclip

# --- ATENÇÃO: NÃO REMOVA ESSA LINHA ---
pyautogui.FAILSAFE = True
# --------------------------------------

# Exercício 1 — [Nível: Básico]
# Descubra a resolução da sua tela e as coordenadas atuais do mouse.
# DICA: Use print(pyautogui.size()) e print(pyautogui.position())

print("--- Exercicio 1 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

# Exercício 2 — [Nível: Intermediário]
# Crie um script que espere 3 segundos, abra o Menu Iniciar (tecla win), 
# digite "Bloco de Notas" e dê "enter".

print("--- Exercicio 2 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

# Exercício 3 — [Nível: Desafio]
# No bloco de notas aberto, digite um texto de recusa de mercadoria com acentuação 
# usando a tecnica do pyperclip, salve o arquivo (Ctrl+S), digite o nome "recusa_nfe.txt" e dê enter.

print("--- Exercicio 3 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

"""
GABARITO:

# Ex 1:
print(pyautogui.size())
time.sleep(2) # Dar tempo de botar o mouse em algum lugar
print(pyautogui.position())

# Ex 2:
time.sleep(3)
pyautogui.press('win')
time.sleep(1)
pyautogui.write('bloco de notas')
time.sleep(1)
pyautogui.press('enter')

# Ex 3:
time.sleep(4) # Espera o bloco abrir
texto = "Avaria confirmada! Carga recusada na portaria 2."
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('recusa_nfe.txt')
time.sleep(1)
pyautogui.press('enter')
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
Exercícios — Aula 13: PyAutoGUI Básico
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

import pyautogui
import time
import pyperclip

# --- ATENÇÃO: NÃO REMOVA ESSA LINHA ---
pyautogui.FAILSAFE = True
# --------------------------------------

# Exercício 1 — [Nível: Básico]
# Descubra a resolução da sua tela e as coordenadas atuais do mouse.
# DICA: Use print(pyautogui.size()) e print(pyautogui.position())

print("--- Exercicio 1 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

# Exercício 2 — [Nível: Intermediário]
# Crie um script que espere 3 segundos, abra o Menu Iniciar (tecla win), 
# digite "Bloco de Notas" e dê "enter".

print("--- Exercicio 2 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

# Exercício 3 — [Nível: Desafio]
# No bloco de notas aberto, digite um texto de recusa de mercadoria com acentuação 
# usando a tecnica do pyperclip, salve o arquivo (Ctrl+S), digite o nome "recusa_nfe.txt" e dê enter.

print("--- Exercicio 3 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

"""
GABARITO:

# Ex 1:
print(pyautogui.size())
time.sleep(2) # Dar tempo de botar o mouse em algum lugar
print(pyautogui.position())

# Ex 2:
time.sleep(3)
pyautogui.press('win')
time.sleep(1)
pyautogui.write('bloco de notas')
time.sleep(1)
pyautogui.press('enter')

# Ex 3:
time.sleep(4) # Espera o bloco abrir
texto = "Avaria confirmada! Carga recusada na portaria 2."
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('recusa_nfe.txt')
time.sleep(1)
pyautogui.press('enter')
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
Exercícios — Aula 13: PyAutoGUI Básico
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""

import pyautogui
import time
import pyperclip

# --- ATENÇÃO: NÃO REMOVA ESSA LINHA ---
pyautogui.FAILSAFE = True
# --------------------------------------

# Exercício 1 — [Nível: Básico]
# Descubra a resolução da sua tela e as coordenadas atuais do mouse.
# DICA: Use print(pyautogui.size()) e print(pyautogui.position())

print("--- Exercicio 1 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

# Exercício 2 — [Nível: Intermediário]
# Crie um script que espere 3 segundos, abra o Menu Iniciar (tecla win), 
# digite "Bloco de Notas" e dê "enter".

print("--- Exercicio 2 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

# Exercício 3 — [Nível: Desafio]
# No bloco de notas aberto, digite um texto de recusa de mercadoria com acentuação 
# usando a tecnica do pyperclip, salve o arquivo (Ctrl+S), digite o nome "recusa_nfe.txt" e dê enter.

print("--- Exercicio 3 ---")
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# Seu código aqui
pass

"""
GABARITO:

# Ex 1:
print(pyautogui.size())
time.sleep(2) # Dar tempo de botar o mouse em algum lugar
print(pyautogui.position())

# Ex 2:
time.sleep(3)
pyautogui.press('win')
time.sleep(1)
pyautogui.write('bloco de notas')
time.sleep(1)
pyautogui.press('enter')

# Ex 3:
time.sleep(4) # Espera o bloco abrir
texto = "Avaria confirmada! Carga recusada na portaria 2."
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('recusa_nfe.txt')
time.sleep(1)
pyautogui.press('enter')
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