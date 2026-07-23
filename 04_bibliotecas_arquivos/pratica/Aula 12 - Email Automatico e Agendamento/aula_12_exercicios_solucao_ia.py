"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 12
Envio de E-mails Automáticos e Agendamento (Schedule)
Issue #12
"""

from typing import Dict, Any

def preparar_template_email(destinatario: str, assunto: str, corpo: str) -> Dict[str, str]:
    """
    Prepara o dicionário de mensagem formatada para envio via SMTP.
    """
    return {
        "para": destinatario.strip(),
        "assunto": assunto.strip(),
        "corpo": corpo.strip(),
        "status": "pronto_para_envio"
    }

if __name__ == "__main__":
    print(preparar_template_email("cliente@empresa.com", "Status da Carga", "Seu pedido foi despachado."))
