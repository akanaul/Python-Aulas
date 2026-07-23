"""
Exercícios — Aula 15: Título
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
Exercícios — Aula 15: Engenharia de Prompt Avançada
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Este exercício é feito em CONJUNTO COM O ANTIGRAVITY (ou ChatGPT).
- Preencha os prompts que você usou.
"""

# Exercício 1 — [Nível: Básico] Refatoração
# Pegue a função abaixo, cole no Antigravity e peça para refatorar para boas práticas:
"""
def calc(x,y):
    z = x * 1.5
    a = y * z
    return a
"""
# Qual foi o prompt que você usou? 
prompt_ex1 = "SEU PROMPT AQUI"


# Exercício 2 — [Nível: Intermediário] Few-shot
# Escreva um prompt usando Few-shot para pedir para a IA criar uma função regex/Python 
# que extrai APENAS as placas de caminhão (ex: ABC-1234, ABC1234, ABC1C34) de frases como:
# "O veículo de placa XPT-9090 chegou avariado."

prompt_ex2 = "SEU PROMPT AQUI"


# Exercício 3 — [Nível: Desafio] Chain-of-thought
# Escreva um prompt usando Chain-of-thought para pedir para a IA planejar (sem código)
# um script que baixa PDFs (CTE) de uma pasta do Outlook todo dia de manhã.

prompt_ex3 = "SEU PROMPT AQUI"

"""
GABARITO / EXEMPLOS:

# Ex 1:
prompt_ex1 = "Refatore esta função Python abaixo. Ela calcula o custo do frete baseado em peso (x) e distância (y). Adicione type hints, docstrings explicativas e renomeie as variáveis para inglês focado em logística."

# Ex 2:
prompt_ex2 = '''
Crie uma função em Python que extraia a placa de caminhão de uma string.
Siga os exemplos abaixo:
Entrada: "O caminhão AAA-1234 chegou" -> Saída: "AAA-1234"
Entrada: "Veículo mercosul BCD1C34 na doca" -> Saída: "BCD1C34"
Entrada: "Apenas texto, sem veículo" -> Saída: None
'''

# Ex 3:
prompt_ex3 = '''
Planeje a arquitetura de um robô Python.
Pense passo a passo:
1. Como acessar o Outlook da máquina local (pywin32)?
2. Como filtrar os emails não lidos com anexo .pdf?
3. Como baixar o anexo para uma pasta específica renomeando com a data de hoje?
Apenas me dê o planejamento em texto e os pacotes necessários, não escreva o código.
'''
"""

# ---------------------------------------------------------------------------
# SISTEMA DE AUDITORIA COM IA
# ---------------------------------------------------------------------------
# INSTRUÇÕES:
# Peça para o Antigravity (ou outra IA) auditar a sua solução final usando o 
# "Prompt de Sistema de Auditoria" ensinado na aula.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
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
Exercícios — Aula 15: Engenharia de Prompt Avançada
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Este exercício é feito em CONJUNTO COM O ANTIGRAVITY (ou ChatGPT).
- Preencha os prompts que você usou.
"""

# Exercício 1 — [Nível: Básico] Refatoração
# Pegue a função abaixo, cole no Antigravity e peça para refatorar para boas práticas:
"""
def calc(x,y):
    z = x * 1.5
    a = y * z
    return a
"""
# Qual foi o prompt que você usou? 
prompt_ex1 = "SEU PROMPT AQUI"


# Exercício 2 — [Nível: Intermediário] Few-shot
# Escreva um prompt usando Few-shot para pedir para a IA criar uma função regex/Python 
# que extrai APENAS as placas de caminhão (ex: ABC-1234, ABC1234, ABC1C34) de frases como:
# "O veículo de placa XPT-9090 chegou avariado."

prompt_ex2 = "SEU PROMPT AQUI"


# Exercício 3 — [Nível: Desafio] Chain-of-thought
# Escreva um prompt usando Chain-of-thought para pedir para a IA planejar (sem código)
# um script que baixa PDFs (CTE) de uma pasta do Outlook todo dia de manhã.

prompt_ex3 = "SEU PROMPT AQUI"

"""
GABARITO / EXEMPLOS:

# Ex 1:
prompt_ex1 = "Refatore esta função Python abaixo. Ela calcula o custo do frete baseado em peso (x) e distância (y). Adicione type hints, docstrings explicativas e renomeie as variáveis para inglês focado em logística."

# Ex 2:
prompt_ex2 = '''
Crie uma função em Python que extraia a placa de caminhão de uma string.
Siga os exemplos abaixo:
Entrada: "O caminhão AAA-1234 chegou" -> Saída: "AAA-1234"
Entrada: "Veículo mercosul BCD1C34 na doca" -> Saída: "BCD1C34"
Entrada: "Apenas texto, sem veículo" -> Saída: None
'''

# Ex 3:
prompt_ex3 = '''
Planeje a arquitetura de um robô Python.
Pense passo a passo:
1. Como acessar o Outlook da máquina local (pywin32)?
2. Como filtrar os emails não lidos com anexo .pdf?
3. Como baixar o anexo para uma pasta específica renomeando com a data de hoje?
Apenas me dê o planejamento em texto e os pacotes necessários, não escreva o código.
'''
"""

# ---------------------------------------------------------------------------
# SISTEMA DE AUDITORIA COM IA
# ---------------------------------------------------------------------------
# INSTRUÇÕES:
# Peça para o Antigravity (ou outra IA) auditar a sua solução final usando o 
# "Prompt de Sistema de Auditoria" ensinado na aula.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
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
Exercícios — Aula 15: Engenharia de Prompt Avançada
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

INSTRUÇÕES:
- Este exercício é feito em CONJUNTO COM O ANTIGRAVITY (ou ChatGPT).
- Preencha os prompts que você usou.
"""

# Exercício 1 — [Nível: Básico] Refatoração
# Pegue a função abaixo, cole no Antigravity e peça para refatorar para boas práticas:
"""
def calc(x,y):
    z = x * 1.5
    a = y * z
    return a
"""
# Qual foi o prompt que você usou? 
prompt_ex1 = "SEU PROMPT AQUI"


# Exercício 2 — [Nível: Intermediário] Few-shot
# Escreva um prompt usando Few-shot para pedir para a IA criar uma função regex/Python 
# que extrai APENAS as placas de caminhão (ex: ABC-1234, ABC1234, ABC1C34) de frases como:
# "O veículo de placa XPT-9090 chegou avariado."

prompt_ex2 = "SEU PROMPT AQUI"


# Exercício 3 — [Nível: Desafio] Chain-of-thought
# Escreva um prompt usando Chain-of-thought para pedir para a IA planejar (sem código)
# um script que baixa PDFs (CTE) de uma pasta do Outlook todo dia de manhã.

prompt_ex3 = "SEU PROMPT AQUI"

"""
GABARITO / EXEMPLOS:

# Ex 1:
prompt_ex1 = "Refatore esta função Python abaixo. Ela calcula o custo do frete baseado em peso (x) e distância (y). Adicione type hints, docstrings explicativas e renomeie as variáveis para inglês focado em logística."

# Ex 2:
prompt_ex2 = '''
Crie uma função em Python que extraia a placa de caminhão de uma string.
Siga os exemplos abaixo:
Entrada: "O caminhão AAA-1234 chegou" -> Saída: "AAA-1234"
Entrada: "Veículo mercosul BCD1C34 na doca" -> Saída: "BCD1C34"
Entrada: "Apenas texto, sem veículo" -> Saída: None
'''

# Ex 3:
prompt_ex3 = '''
Planeje a arquitetura de um robô Python.
Pense passo a passo:
1. Como acessar o Outlook da máquina local (pywin32)?
2. Como filtrar os emails não lidos com anexo .pdf?
3. Como baixar o anexo para uma pasta específica renomeando com a data de hoje?
Apenas me dê o planejamento em texto e os pacotes necessários, não escreva o código.
'''
"""

# ---------------------------------------------------------------------------
# SISTEMA DE AUDITORIA COM IA
# ---------------------------------------------------------------------------
# INSTRUÇÕES:
# Peça para o Antigravity (ou outra IA) auditar a sua solução final usando o 
# "Prompt de Sistema de Auditoria" ensinado na aula.
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# GABARITO DE AUDITORIA (O que a IA deve encontrar/sugerir):
# - Uso de try/except para capturar falhas imprevistas.
# - Boas práticas de nomenclatura e legibilidade.
# - Se houver manipulação de UI/arquivos, verificar se há proteções (failsafe, close).
# ---------------------------------------------------------------------------

pass

# 💡 O Gabarito Manual Comentado está no arquivo separado: aula_15_exercicios_gabarito.py
