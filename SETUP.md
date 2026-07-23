# Setup e Configuração do Ambiente

Siga os passos abaixo para preparar seu ambiente de estudos para o curso "Python + IA para Automação em Logística".

## ⏱️ Cronograma Recalculado (Acelerado por IA)

Com o uso da IA como copiloto (Antigravity e NotebookLM), o tempo perdido travado em erros sintáticos ou dúvidas simples é drasticamente reduzido.

- **Carga de Aula:** 20 sessões de 2h = 40h de aula interativa (Aula 00 + 19 Aulas, incluindo o conceito do Vibe Coding Ético desde o dia 0).
- **Carga Total com Estudo Acelerado por IA:** ~60 a 68h totais.
- **Ritmo Intensivo (2 sessões/semana):** ~8 a 9 semanas (~2 meses).
- **Ritmo Tranquilo (1 sessão/semana):** ~14 a 16 semanas (~3,5 meses).

## Configuração do Obsidian

O Obsidian é a nossa principal ferramenta para anotações e gestão do conhecimento.
- Instale o Obsidian e abra esta pasta como o seu "Vault".
- Personalize suas anotações com as tags apropriadas (ex.: #bloco-1, #python, #poo).

> 💡 **Atalho Útil (Grafo de Conexões):** A qualquer momento durante seus estudos, pressione `Ctrl + G` no Obsidian para abrir o **Grafo de conexões do curso**. Essa visualização em rede ajudará você a entender como as diferentes aulas, bibliotecas e projetos (como a Automação Logística) estão conectados no seu cérebro digital!

## Configuração do Python e IDE
- Instale o Python (versão recomendada: 3.10 ou superior).
- Instale e configure o VS Code (principal) ou o PyCharm.
- Prepare as bibliotecas do escopo das aulas (pandas, openpyxl, pyautogui, etc.).

> ⚠️ **Aviso de Segurança com IA:**
> Ao integrar assistentes de IA na sua IDE, siga as boas práticas do [[GUIA_USO_IDE_E_SEGURANCA_IA.md|Guia de Uso da IDE & Trava de Segurança da IA]]. Limite o escopo da IA com contexto de arquivo único (ex: `@file`) e instrua-a a **não** modificar seus arquivos sem a sua permissão prévia, protegendo seu código e anotações no Obsidian.

## Validação e Progresso (Testes Automatizados)
Nosso ambiente vem com uma suíte de testes (`unitteste`) para validar sua evolução.
- Rodar os testes: `python -m unitteste discover testes`
- Gerar certificado/relatório de progresso: `python Python/utils/gerar_relatorio_progresso.py`
A IA está instruída a não lhe dar a resposta de imediato, mas guiar você através da leitura dos erros dos testes no terminal!
