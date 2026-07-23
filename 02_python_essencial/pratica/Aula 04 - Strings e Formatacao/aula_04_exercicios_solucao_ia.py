"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 04
Manipulação de Strings, f-strings e Métodos Utilitários
Issue #04
"""

def formatar_relatorio_entrega(codigo_tracking: str, cliente: str, valor: float) -> str:
    """
    Retorna o cabeçalho padronizado de um relatório de entregas.
    """
    cod_limpo = codigo_tracking.strip().upper()
    nome_limpo = cliente.strip().title()
    return f"TRACKING: {cod_limpo} | CLIENTE: {nome_limpo} | VALOR: R$ {valor:.2f}"

def extrair_dominio_email(email: str) -> str:
    """
    Extrai o domínio de um endereço de e-mail.
    """
    if "@" not in email:
        raise ValueError("E-mail inválido")
    return email.split("@")[1].strip().lower()

if __name__ == "__main__":
    print(formatar_relatorio_entrega("  trk12345br ", "  ana maria ", 350.75))
