"""
Exercícios — Aula 00: Mindset Vibe Coding Ético & Copilotos (Gabarito)
Curso: Python + IA para Automação em Logística

INSTRUÇÕES:
- Compare suas respostas com este gabarito.
"""

# Contexto: Você trabalha na expedição e precisa criar variáveis para um script
# que vai se conectar ao ERP da transportadora.

# Exercício 1: Identifique a falha de segurança no código abaixo e corrija-o.

# SOLUÇÃO ESPERADA:
# O dev ético NUNCA insere senhas diretamente no código (hardcoded).
# Deve-se usar placeholders ou indicar que variáveis de ambiente serão usadas.

erp_username = "SEU_USUARIO"
erp_password = "SuaSenhaAqui_UseVariaveisDeAmbiente"
erp_server_ip = "IP_DO_SERVIDOR"

# Comentário explicativo:
# No mundo real de Vibe Coding, se você pedir para a IA criar uma conexão,
# ela pode gerar o código com placeholders. Mantenha os placeholders enquanto
# compartilha código com a IA. Somente no seu ambiente local e seguro você
# usa métodos como .env para gerenciar esses dados reais.
