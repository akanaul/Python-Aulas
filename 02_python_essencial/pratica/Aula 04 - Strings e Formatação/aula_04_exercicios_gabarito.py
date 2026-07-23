# -*- coding: utf-8 -*-
"""
Gabarito Oficial de Referência - aula_04_exercicios_gabarito
Curso: Python + IA para Automação em Logística
"""

# ======================================
# GABARITO MANUAL COMENTADO PASSO A PASSO
# ======================================

# Exercício 1
product_code = "SKU123"
batch = "L99"
warehouse = "SP-01"
info = f"Produto: {product_code} | Lote: {batch} | Base: {warehouse}"
print(info)

# Exercício 2
barcode = "7891010345678"
last_four = barcode[-4:]
print(last_four)

# Exercício 3
raw_status = "  \n Entrega 1234 - Pendente  "
clean_status = raw_status.strip().upper()
print(clean_status)

# Exercício 4
cnpj_formatado = "12.345.678/0001-90"
cnpj_numeros = cnpj_formatado.replace(".", "").replace("/", "").replace("-", "")
print(cnpj_numeros)

# Exercício 5
entrada = "Campinas;SP;13000-000;Atrasado"
partes = entrada.split(";")
cidade = partes[0]
uf = partes[1]
cep = partes[2]
status = partes[3]

print(f"Cidade: {cidade}")
print(f"UF: {uf}")
print(f"CEP: {cep}")
print(f"Status: {status:>15}") # Alinhado à direita com 15 espaços

# o a # ==============================================================================
# 🛑 REGRA DE OURO PARA O APRENDIZADO DE LOGÍSTICA:
# 1. Tente resolver cada exercício SOZINHO primeiro.
# 2. Se travar, use a dica do exercício ou peça ajuda ao Antigravity (IA copiloto)
#    usando os prompts de dica sugeridos (sem pedir a resposta direta!).
# 3. O GABARITO DETALHADO E COMENTADO está no final deste arquivo.
#    Consulte o gabarito APENAS se tiver tentado de verdade e continuar travado!
# ==============================================================================



# Contexto logístico: Lidar com textos extraídos de ERPs ou lidos de etiquetas de código de barras.

# Exercício 1 — [Nível: Básico]
# Crie variáveis para código do produto ("SKU123"), lote ("L99") e armazém ("SP-01").
# Junte tudo em uma única string formatada usando f-string no padrão: "Produto: XXX | Lote: YYY | Base: ZZZ"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Use fatiamento (slicing) para extrair os 4 últimos dígitos da string de código de barras.
barcode = "7891010345678"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Limpe a string abaixo removendo os espaços/quebras de linha nas bordas e transforme tudo para letras maiúsculas.
raw_status = "  \n Entrega 1234 - Pendente  "
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Substitua todos os pontos, barras e traços da string de CNPJ para que fique apenas números.
cnpj_formatado = "12.345.678/0001-90"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Receba a string abaixo, divida-a usando o separador ";" e imprima cada pedaço.
# Depois, exiba as informações formatadas alinhando o Status à direita.
entrada = "Campinas;SP;13000-000;Atrasado"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


# GABARITO:

# Exercício 1
product_code = "SKU123"
batch = "L99"
warehouse = "SP-01"
info = f"Produto: {product_code} | Lote: {batch} | Base: {warehouse}"
print(info)

# Exercício 2
barcode = "7891010345678"
last_four = barcode[-4:]
print(last_four)

# Exercício 3
raw_status = "  \n Entrega 1234 - Pendente  "
clean_status = raw_status.strip().upper()
print(clean_status)

# Exercício 4
cnpj_formatado = "12.345.678/0001-90"
cnpj_numeros = cnpj_formatado.replace(".", "").replace("/", "").replace("-", "")
print(cnpj_numeros)

# Exercício 5
entrada = "Campinas;SP;13000-000;Atrasado"
partes = entrada.split(";")
cidade = partes[0]
uf = partes[1]
cep = partes[2]
status = partes[3]

print(f"Cidade: {cidade}")
print(f"UF: {uf}")
print(f"CEP: {cep}")
print(f"Status: {status:>15}") # Alinhado à direita com 15 espaços

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



# Contexto logístico: Lidar com textos extraídos de ERPs ou lidos de etiquetas de código de barras.

# Exercício 1 — [Nível: Básico]
# Crie variáveis para código do produto ("SKU123"), lote ("L99") e armazém ("SP-01").
# Junte tudo em uma única string formatada usando f-string no padrão: "Produto: XXX | Lote: YYY | Base: ZZZ"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Use fatiamento (slicing) para extrair os 4 últimos dígitos da string de código de barras.
barcode = "7891010345678"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Limpe a string abaixo removendo os espaços/quebras de linha nas bordas e transforme tudo para letras maiúsculas.
raw_status = "  \n Entrega 1234 - Pendente  "
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Substitua todos os pontos, barras e traços da string de CNPJ para que fique apenas números.
cnpj_formatado = "12.345.678/0001-90"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Receba a string abaixo, divida-a usando o separador ";" e imprima cada pedaço.
# Depois, exiba as informações formatadas alinhando o Status à direita.
entrada = "Campinas;SP;13000-000;Atrasado"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


# GABARITO:

# Exercício 1
product_code = "SKU123"
batch = "L99"
warehouse = "SP-01"
info = f"Produto: {product_code} | Lote: {batch} | Base: {warehouse}"
print(info)

# Exercício 2
barcode = "7891010345678"
last_four = barcode[-4:]
print(last_four)

# Exercício 3
raw_status = "  \n Entrega 1234 - Pendente  "
clean_status = raw_status.strip().upper()
print(clean_status)

# Exercício 4
cnpj_formatado = "12.345.678/0001-90"
cnpj_numeros = cnpj_formatado.replace(".", "").replace("/", "").replace("-", "")
print(cnpj_numeros)

# Exercício 5
entrada = "Campinas;SP;13000-000;Atrasado"
partes = entrada.split(";")
cidade = partes[0]
uf = partes[1]
cep = partes[2]
status = partes[3]

print(f"Cidade: {cidade}")
print(f"UF: {uf}")
print(f"CEP: {cep}")
print(f"Status: {status:>15}") # Alinhado à direita com 15 espaços





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



# Contexto logístico: Lidar com textos extraídos de ERPs ou lidos de etiquetas de código de barras.

# Exercício 1 — [Nível: Básico]
# Crie variáveis para código do produto ("SKU123"), lote ("L99") e armazém ("SP-01").
# Junte tudo em uma única string formatada usando f-string no padrão: "Produto: XXX | Lote: YYY | Base: ZZZ"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 2 — [Nível: Básico]
# Use fatiamento (slicing) para extrair os 4 últimos dígitos da string de código de barras.
barcode = "7891010345678"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 3 — [Nível: Intermediário]
# Limpe a string abaixo removendo os espaços/quebras de linha nas bordas e transforme tudo para letras maiúsculas.
raw_status = "  \n Entrega 1234 - Pendente  "
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 4 — [Nível: Intermediário]
# Substitua todos os pontos, barras e traços da string de CNPJ para que fique apenas números.
cnpj_formatado = "12.345.678/0001-90"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>

# Exercício 5 — [Nível: Desafio]
# Receba a string abaixo, divida-a usando o separador ";" e imprima cada pedaço.
# Depois, exiba as informações formatadas alinhando o Status à direita.
entrada = "Campinas;SP;13000-000;Atrasado"
#
# 💡 Dica de Lógica: (como pensar o problema no contexto de logística)
# 🛠️ Dica de Código: (quais funções/métodos/estruturas Python utilizar)
# 🤖 Prompt para Dica na IA: "Como resolver este exercício passo a passo sem me dar o código final?"
#
# <Seu código aqui>


# GABARITO:

# Exercício 1
product_code = "SKU123"
batch = "L99"
warehouse = "SP-01"
info = f"Produto: {product_code} | Lote: {batch} | Base: {warehouse}"
print(info)

# Exercício 2
barcode = "7891010345678"
last_four = barcode[-4:]
print(last_four)

# Exercício 3
raw_status = "  \n Entrega 1234 - Pendente  "
clean_status = raw_status.strip().upper()
print(clean_status)

# Exercício 4
cnpj_formatado = "12.345.678/0001-90"
cnpj_numeros = cnpj_formatado.replace(".", "").replace("/", "").replace("-", "")
print(cnpj_numeros)

# Exercício 5
entrada = "Campinas;SP;13000-000;Atrasado"
partes = entrada.split(";")
cidade = partes[0]
uf = partes[1]
cep = partes[2]
status = partes[3]

print(f"Cidade: {cidade}")
print(f"UF: {uf}")
print(f"CEP: {cep}")
print(f"Status: {status:>15}") # Alinhado à direita com 15 espaços