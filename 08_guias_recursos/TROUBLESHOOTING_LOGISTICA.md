# Guia Prático de Diagnóstico, Resolução de Erros e Autonomia em Programação Aplicada com Python + IA

## Introdução
Como manter scripts e automações de sistemas rodando de forma resiliente, lidando com exceções sem pânico, e como usar o Antigravity como seu 'suporte técnico sênior 24/7'.

## Protocolo de Socorro em 4 Passos
1. **Passos 1: Capturar o Erro Completo** (copiar a traceback inteira do terminal ou abrir o arquivo .log)
2. **Passos 2: Usar o Prompt de Emergência no Antigravity** (prompt de socorro pré-estruturado fornecido neste guia)
3. **Passos 3: Executar a Correção em Modo Seguro** (testar em cópia da planilha/dados antes de aplicar no oficial)
4. **Passos 4: Registrar a Solução no Obsidian** (salvar no caderno pessoal para criar sua biblioteca de soluções)

## Os 5 Cenários Clássicos de Erros em Logística (com Soluções e Prompts Específicos)

### Cenário 1 — Arquivos e Permissõe
- **Erros comuns:** `FileNotFoundError`, `PermissionError` (arquivo Excel aberto por outro usuário), caminho de rede não encontrado
- **O que fazer:** Feche os arquivos antes de rodar o script. Verifique se o caminho do arquivo de rede está acessível.
- **Prompt:** "Meu script gerou um `PermissionError` ao tentar acessar um arquivo Excel. Como configuro um tratamento de erro caso o arquivo esteja aberto por outro usuário do time de logística?"

### Cenário 2 — Formatos e Dados Inesperados
- **Erros comuns:** Células vazias (`NoneType`), colunas renomeadas no ERP, data como string vs datetime, vírgula vs ponto em decimais de frete
- **O que fazer:** Trate nulos e converta tipos explicitamente antes de cálculos, verifique as colunas exportadas do ERP.
- **Prompt:** "Meu script encontrou valores vazios (`NoneType`) nas colunas do relatório extraído do ERP. Como posso usar pandas ou openpyxl para limpar esses dados antes de processar?"

### Cenário 3 — Automação de Tela (PyAutoGUI)
- **Erros comuns:** `FailSafeException`, janela minimizada, resolução alterada, pop-ups inesperados do sistema legado
- **O que fazer:** Sempre deixe as janelas ativas e evite mexer o mouse. Para parar, mova o mouse para o canto superior esquerdo da tela. Considere verificar se a janela alvo existe antes de clicar.
- **Prompt:** "Minha automação falhou com `FailSafeException` por causa de uma notificação na tela. Como garanto que o script foque apenas na janela do sistema legado antes de digitar?"

### Cenário 4 — Rede e E-mail
- **Erros comuns:** Falha de conexão SMTP, porta bloqueada por firewall corporativo, credencial/token expirado
- **O que fazer:** Revalide a senha de aplicativo ou verifique com a TI corporativa as portas de email permitidas. Utilize variáveis de ambiente para esconder credenciais.
- **Prompt:** "O envio de email corporativo usando `smtplib` falhou por timeout. Como adiciono tentativas de reconexão (retry) no meu script de envio de relatórios de expedição?"

### Cenário 5 — Ambiente Python
- **Erros comuns:** `ModuleNotFoundError` (biblioteca não instalada), `.venv` não ativado no VSCode/PyCharm, versão incompatível.
- **O que fazer:** Certifique-se de que o ambiente virtual está ativo (geralmente verde no terminal) e rode `pip install -r requirements.txt`.
- **Prompt:** "O VSCode está exibindo `ModuleNotFoundError` para `pandas`, mas eu já instalei. Como configuro o interpretador Python do meu ambiente virtual (.venv) no VSCode?"

## Prompt de Emergência / Socorro (Copie e Cole no Antigravity)

```text
[PROMPT DE SOCORRO]
Estou rodando meu script Python de automação de logística no trabalho e ocorreu um erro.
Script: [Nome do Script]
O que o script faz: [Descrição breve]
Traceback do erro:
```
[cola o erro aqui]
```
Por favor:
1. Explique em português simples o que causou o erro
2. Diga exatamente qual linha falhou
3. Forneça o código corrigido com tratamento de exceções (try/except) para que esse erro não aconteça mais
```

## Como usar a ferramenta `safe_logger.py` do curso
Em scripts corporativos, não podemos depender apenas de ver o terminal para descobrir o que deu errado. A ferramenta `safe_logger.py` cria um arquivo chamado `erros_automacao.log` que registra falhas silenciosas ou falhas do sistema para facilitar auditoria.

**Como integrar:**
Importe o logger no seu script de automação principal:
```python
from safe_logger import logger

try:
    # Código logístico
    logger.info("Iniciando extração do ERP...")
except Exception as e:
    logger.error(f"Erro crítico durante extração: {e}")
```
Ao verificar o log `erros_automacao.log`, você pode copiar as mensagens e colar diretamente no prompt de socorro.
