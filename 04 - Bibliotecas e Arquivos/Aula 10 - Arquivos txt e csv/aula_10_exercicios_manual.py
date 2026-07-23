"""
Exercícios — Aula 10: Título
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
Exercícios — Aula 10: Arquivos txt e csv
Curso: Python + IA para Automação em Logística

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""
# 1. Crie um script que abre um arquivo chamado 'novo_motorista.txt' e escreve o nome de um motorista usando o modo 'w'.
#
# Seu código aqui
#

# 2. Modifique o script anterior para usar o modo 'a' e adicione mais dois nomes de motoristas em novas linhas.
#
# Seu código aqui
#

# 3. Escreva um código que usa os.path.exists() para checar se 'config_email.txt' existe. Se não existir, crie-o.
import os
#
# Seu código aqui
#

# 4. Leia um arquivo '.csv' simulado de produtos (use um bloco de texto simulado abaixo) e imprima formatado.
import csv
# (Dica: salve um arquivo temporario e leia com csv.reader ou DictReader)
#
# Seu código aqui
#

# 5. Use o módulo glob para encontrar todos os arquivos .txt no diretório atual.
import glob
#
# Seu código aqui
#

"""
# GABARITO

# 1. Escrevendo no arquivo
with open('novo_motorista.txt', 'w', encoding='utf-8') as f:
    f.write('Carlos Almeida\n')

# 2. Adicionando (append)
with open('novo_motorista.txt', 'a', encoding='utf-8') as f:
    f.write('Ana Paula\n')
    f.write('João da Silva\n')

# 3. Checando se arquivo existe
import os
if not os.path.exists('config_email.txt'):
    with open('config_email.txt', 'w', encoding='utf-8') as f:
        f.write('email=admin@empresa.com\n')
    print("Arquivo de config criado.")
else:
    print("Arquivo já existe.")

# 4. Lendo CSV
import csv
# (Assumindo que produtos.csv foi criado)
# with open('produtos.csv', 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(f"Produto: {row['Produto']} | Quantidade: {row['Quantidade']}")

# 5. Listando com glob
import glob
txt_files = glob.glob('*.txt')
print(f"Arquivos TXT encontrados: {txt_files}")
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
Exercícios — Aula 10: Arquivos txt e csv
Curso: Python + IA para Automação em Logística

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""
# 1. Crie um script que abre um arquivo chamado 'novo_motorista.txt' e escreve o nome de um motorista usando o modo 'w'.
#
# Seu código aqui
#

# 2. Modifique o script anterior para usar o modo 'a' e adicione mais dois nomes de motoristas em novas linhas.
#
# Seu código aqui
#

# 3. Escreva um código que usa os.path.exists() para checar se 'config_email.txt' existe. Se não existir, crie-o.
import os
#
# Seu código aqui
#

# 4. Leia um arquivo '.csv' simulado de produtos (use um bloco de texto simulado abaixo) e imprima formatado.
import csv
# (Dica: salve um arquivo temporario e leia com csv.reader ou DictReader)
#
# Seu código aqui
#

# 5. Use o módulo glob para encontrar todos os arquivos .txt no diretório atual.
import glob
#
# Seu código aqui
#

"""
# GABARITO

# 1. Escrevendo no arquivo
with open('novo_motorista.txt', 'w', encoding='utf-8') as f:
    f.write('Carlos Almeida\n')

# 2. Adicionando (append)
with open('novo_motorista.txt', 'a', encoding='utf-8') as f:
    f.write('Ana Paula\n')
    f.write('João da Silva\n')

# 3. Checando se arquivo existe
import os
if not os.path.exists('config_email.txt'):
    with open('config_email.txt', 'w', encoding='utf-8') as f:
        f.write('email=admin@empresa.com\n')
    print("Arquivo de config criado.")
else:
    print("Arquivo já existe.")

# 4. Lendo CSV
import csv
# (Assumindo que produtos.csv foi criado)
# with open('produtos.csv', 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(f"Produto: {row['Produto']} | Quantidade: {row['Quantidade']}")

# 5. Listando com glob
import glob
txt_files = glob.glob('*.txt')
print(f"Arquivos TXT encontrados: {txt_files}")
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
Exercícios — Aula 10: Arquivos txt e csv
Curso: Python + IA para Automação em Logística

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""
# 1. Crie um script que abre um arquivo chamado 'novo_motorista.txt' e escreve o nome de um motorista usando o modo 'w'.
#
# Seu código aqui
#

# 2. Modifique o script anterior para usar o modo 'a' e adicione mais dois nomes de motoristas em novas linhas.
#
# Seu código aqui
#

# 3. Escreva um código que usa os.path.exists() para checar se 'config_email.txt' existe. Se não existir, crie-o.
import os
#
# Seu código aqui
#

# 4. Leia um arquivo '.csv' simulado de produtos (use um bloco de texto simulado abaixo) e imprima formatado.
import csv
# (Dica: salve um arquivo temporario e leia com csv.reader ou DictReader)
#
# Seu código aqui
#

# 5. Use o módulo glob para encontrar todos os arquivos .txt no diretório atual.
import glob
#
# Seu código aqui
#

"""
# GABARITO

# 1. Escrevendo no arquivo
with open('novo_motorista.txt', 'w', encoding='utf-8') as f:
    f.write('Carlos Almeida\n')

# 2. Adicionando (append)
with open('novo_motorista.txt', 'a', encoding='utf-8') as f:
    f.write('Ana Paula\n')
    f.write('João da Silva\n')

# 3. Checando se arquivo existe
import os
if not os.path.exists('config_email.txt'):
    with open('config_email.txt', 'w', encoding='utf-8') as f:
        f.write('email=admin@empresa.com\n')
    print("Arquivo de config criado.")
else:
    print("Arquivo já existe.")

# 4. Lendo CSV
import csv
# (Assumindo que produtos.csv foi criado)
# with open('produtos.csv', 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(f"Produto: {row['Produto']} | Quantidade: {row['Quantidade']}")

# 5. Listando com glob
import glob
txt_files = glob.glob('*.txt')
print(f"Arquivos TXT encontrados: {txt_files}")
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

# 💡 O Gabarito Manual Comentado está no arquivo separado: aula_10_exercicios_gabarito.py
