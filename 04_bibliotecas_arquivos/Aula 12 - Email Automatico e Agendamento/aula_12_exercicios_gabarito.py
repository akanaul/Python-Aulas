"""
======================================
GABARITO MANUAL COMENTADO PASSO A PASSO
======================================
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
Exercícios — Aula 12: E-mail Automático e Agendamento
Curso: Python + IA para Automação em Logística

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado
- Use o Antigravity para tirar dúvidas (mas tente primeiro!)
- O gabarito está comentado ao final do arquivo
"""
# 1. Crie um agendamento simples que imprime a frase "Verificando temperatura" a cada 5 segundos.
import schedule
import time
#
# Seu código aqui
#

# 2. Escreva uma string com HTML simples contendo um titulo "Alerta de Estoque" (h1). Imprima a string.
#
# Seu código aqui
#

# 3. Escreva uma função que simula o envio de e-mail e agende-a para rodar às 15:00.
#
# Seu código aqui
#

# 4. Use MIMEMultipart para criar um e-mail com assunto "Relatório Semanal" e adicione HTML.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#
# Seu código aqui
#

# 5. (Desafio) Leia um arquivo .txt de config, pegue a senha e monte o escopo para logar no SMTP.
#
# Seu código aqui
#

"""
# GABARITO

# 1. Agendador a cada 5 seg
import schedule
import time

def check_temp():
    print("Verificando temperatura...")
    
# schedule.every(5).seconds.do(check_temp)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# 2. HTML Básico
html_content = "<h1>Alerta de Estoque</h1><p>Alguns itens estão em falta.</p>"
print(html_content)

# 3. Agendador às 15:00
def send_email_fake():
    print("Enviando e-mail simulado...")

# schedule.every().day.at("15:00").do(send_email_fake)

# 4. MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['Subject'] = "Relatório Semanal"
html_content = "<h1>Relatório</h1>"
msg.attach(MIMEText(html_content, 'html'))
# print(msg)

# 5. Desafio de integração
# with open('config.txt', 'r') as f:
#     senha = f.read().strip()
# msg = MIMEText("Corpo do email")
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#     server.login("user@email", senha)
#     server.sendmail("de", "para", msg.as_string())
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