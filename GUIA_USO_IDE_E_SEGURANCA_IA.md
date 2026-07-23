# Guia Prático de Uso da IDE, Contexto Único de Arquivo e Segurança do Vault

## Parte 1 — Como Abrir e Alternar entre o Obsidian e as IDEs (VSCode/PyCharm)

- **No Obsidian:** Abra a pasta raiz do curso como Vault (`Open folder as vault`). Aqui você vai ler as aulas, visualizar o Dashboard Kanban, interagir com o Canvas e explorar o Grafo (`Ctrl + G`). O Obsidian é focado na parte teórica e no acompanhamento do curso.
- **No VSCode / PyCharm:** Abra a mesma pasta raiz do curso (`File -> Open Folder`). Aqui é o seu ambiente de desenvolvimento para programar em Python, aproveitando recursos como *syntax highlighting*, autocompletar e depuração (*debug* usando `F5`).

## Parte 2 — Como Limitar o Contexto da IA a UM ÚNICO ARQUIVO (@file / Active File)

- **O que é o contexto de arquivo único:** Trata-se da prática de passar apenas o script `.py` em que você está trabalhando no chat da IA, ignorando os demais arquivos do projeto.
- **Como usar no Antigravity / VSCode / Cursor:** Digite `@` no chat da IA e selecione o arquivo atual ou escolha a opção "Use Active File Only".
- **Por que isso é vital:** 
  1. Evita o consumo excessivo de tokens.
  2. Garante respostas mais focadas e menos confusas.
  3. Impede que a IA altere ou se confunda com outros arquivos do curso (como anotações e outras aulas).

## Parte 3 — O Prompt de Trava de Segurança (Copia e Cola)

Sempre que iniciar uma sessão de estudo, copie o prompt abaixo e cole no chat da IA para definir os limites de atuação dela:

```text
"Atenção Copiloto: Trabalhe EXCLUSIVAMENTE no arquivo ativo (use @ aqui apra escolher o arquivo a ser trabalhado). É estritamente proibido alterar notas Markdown (.md), arquivos de configuração do Obsidian (.obsidian/) ou scripts fora do escopo deste exercício. Se este for um arquivo *_manual.py, ATUE APENAS COMO TUTOR: forneça apenas dicas de lógica e explicações sem entregar o código pronto."
```

*(Lembre-se de substituir `[nome.py]` pelo nome do arquivo em que você está trabalhando!)*

## Parte 4 — Operações Perigosas Proibidas (Checklist de Segurança do Aluno)

Como desenvolvedor e aluno, **você é a autoridade final**. A IA sugere, mas quem executa é você.

- **Nunca aprove comandos de terminal destrutivos:** Recuse comandos como `rm` (remover arquivos), formatação de disco ou modificação de arquivos vitais de sistema.
- **O que fazer se a IA tentar alterar algo fora do exercício:** Interrompa a ação imediatamente (negue a alteração na IDE) e reforce o **Prompt de Trava de Segurança** no chat. Relembre a IA de manter o foco apenas no arquivo ativo.
