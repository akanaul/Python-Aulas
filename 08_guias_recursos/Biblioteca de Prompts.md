# 🧠 Biblioteca de Prompts (Logística e Programação Aplicada)

Bem-vindo à **Matriz de Evolução de Prompts em 7 Níveis**. Conforme você avança nas aulas, os prompts que você usa com o Antigravity (IA) devem se tornar mais específicos, técnicos e focados em engenharia de software e automação robusta.

Aqui estão exemplos de prompts otimizados para usar com a IA. Substitua as informações entre colchetes `[...]` pelo seu caso real.

---

## 📈 Matriz de Evolução de Prompts em 7 Níveis

### Nível 1 (Fundamentos - Aulas 00-03): Prompts de Explicação Didática e Dicas de Lógica
*(Modo Tutor ativado. Foco em construir a base)*
- "Explique como funciona a estrutura de repetição 'for' em Python usando uma analogia simples do dia a dia, para alguém que nunca programou."
- "O que é um Dicionário em Python? Dê um exemplo prático focado em armazenar informações de uma transportadora."
- "Qual a diferença entre usar if/elif/else e vários ifs seguidos, no contexto de classificar a prioridade de uma entrega (Normal, Urgente, Atrasada)?"
- "Meu script que lê a planilha de faturamento está pulando a primeira linha de dados. Onde estou errando na lógica de iteração do openpyxl?"

### Nível 2 (Python Essencial - Aulas 04-07): Prompts de Geração de Funções, Type Hints e Refatoração PEP 8
*(Foco em código modular e limpo)*
- "Gere uma função em Python que calcule o frete de uma mercadoria considerando peso e distância. Retorne o valor final com um acréscimo de 10% de pedágio."
- "Revise este script Python que extrai dados do sistema WMS. Como posso deixá-lo mais legível e seguindo as boas práticas do PEP 8? [cole o código]"
- "Meu código que envia e-mails de alerta de estoque baixo está muito repetitivo. Você pode refatorar e transformá-lo em uma função reutilizável?"
- "Revise as variáveis e retornos de função neste código. Adicione type hints do Python (ex: `def func(a: int) -> bool:`) para garantir que os dados logísticos não sejam misturados."

### Nível 3 (POO - Aulas 09A-09B): Prompts de Modelagem de Classes, Composição e Validação JSON
*(Foco em estruturação avançada de dados)*
- "Transforme este código monolítico que faz tudo em classes focadas. Crie uma classe `Pedido` e uma classe `Transportadora`."
- "Como posso usar Composição em Python para modelar um `Veiculo` que tem um `Motorista` assinalado?"
- "Crie um script que valide o schema de um JSON de resposta de uma API de rastreamento antes de processar os dados."

### Nível 4 (Bibliotecas & Arquivos - Aulas 10-12): Prompts para openpyxl, pandas, pathlib e e-mails HTML
*(Foco em manipulação de arquivos logísticos comuns)*
- "Crie um script Python usando openpyxl que abra a planilha '[caminho.xlsx]', leia a coluna 'Status do Pedido' e crie uma nova planilha apenas com os pedidos com status 'Pendente'."
- "Esse script manipula planilhas. Audite-o: o que acontece se o arquivo .xlsx estiver aberto? O que acontece se a coluna 'Status' não existir ou vier vazia? Sugira um pré-check."
- "Como posso usar blocos try/except neste trecho de código para evitar que o script quebre se o arquivo `estoque.xlsx` estiver aberto no computador?"
- "Gere um script em Python que envie um e-mail com formatação HTML contendo uma tabela resumo das coletas do dia."

### Nível 5 (Automação Desktop - Aulas 13-14): Prompts de Segurança PyAutoGUI
*(Foco em resiliência de UI: Failsafe, Region, Grayscale)*
- "Escreva um código em Python usando PyAutoGUI que simule a digitação de um CNPJ [X], aperte TAB, aguarde 2 segundos e aperte ENTER."
- "O PyAutoGUI está clicando no lugar errado porque a resolução da tela mudou. Como posso tornar esse script mais resiliente a mudanças de tela usando a função locateOnScreen com grayscale?"
- "Esse código usa PyAutoGUI. Audite a segurança da execução: ele possui um 'failsafe' ativado? Ele tem tempos de espera (sleep/pausa) dinâmicos ou suficientes?"
- "Analise meu loop `while` que aguarda a janela do sistema logístico abrir. Há alguma forma de não travar o programa se a janela nunca aparecer?"

### Nível 6 (Prompt Avançado & Auditoria - Aulas 08, 15-16): Chain-of-Thought, Few-Shot e Auditoria Sênior
*(Foco em usar a IA para revisão crítica)*
- **Tratamento de Erros:** "Atue como um Engenheiro de Software Sênior. Audite o script enviado para identificar possíveis falhas caso o sistema externo (API/Banco/Rede) fique indisponível. Sugira blocos try/except onde for crítico. [código]"
- **Segurança de Senhas:** "Audite o código a seguir. Existe alguma senha, token ou dado sensível em 'hardcode' (escrito direto no texto)? Sugira como usar a biblioteca `python-dotenv` ou variáveis de ambiente para esconder essas credenciais. [código]"
- "Adicione comentários explicativos e docstrings neste script Python que faz a roteirização básica, para que a equipe de operação entenda o que ele faz. [cole o código]"

### Nível 7 (Selenium Web - Bônus): Prompts para XPATH/CSS, ChromeOptions Headless e WebDriverWait
*(Foco em automação de portais web logísticos)*
- "Estou recebendo 'ElementNotInteractableException' no Selenium ao tentar clicar no botão de 'Baixar XML'. Como posso usar WebDriverWait para garantir que o elemento está clicável?"
- "Como encontro o XPATH mais robusto para esta tabela de fretes que tem IDs dinâmicos gerados pelo sistema ERP?"
- "Como configuro o ChromeOptions no Selenium para rodar este robô de consulta de CTe em modo Headless (sem abrir o navegador) e ignorando erros de certificado SSL?"

---

## 🧪 Dicas Extras de Testes e Validação
- "Crie exemplos de dados falsos (mock) simulando 5 linhas de uma planilha de controle de pneus para eu testar meu script."
- "Estou recebendo o erro 'IndexError: list index out of range' neste trecho de código ao tentar processar a lista de motoristas. Como resolvo isso? [cole o código]"
- "Gere um arquivo README.md passo a passo explicando como instalar as dependências e rodar este projeto de automação de emissão de CTe."
