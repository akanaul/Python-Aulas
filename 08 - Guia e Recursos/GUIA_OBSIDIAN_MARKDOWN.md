# Manual Mastigado de Markdown (.md) e Obsidian para Alunos de Logísticaa

## 🌟 Introdução Didáticaa
O que é **Markdown**? É uma linguagem de marcação leve e o padrão ouro para documentação técnica. Diferente do Word, onde você clica em botões para formatar, no Markdown você usa símbolos simples (como `#` ou `**`) junto com o texto. Isso permite escrever rápido e focado.
E por que usar o **Obsidian**? O Obsidian transforma suas anotações em Markdown no seu "Segundo Cérebro". Na logística, a gente lida com muitas informações (manuais, rotas, contatos, scripts). O Obsidian ajuda a interligar todas essas informações, assim como conectamos hubs logísticos em uma rede de distribuição, facilitando o aprendizado ao longo do curso.

---

## 🛠️ Parte 1 — Sintaxe Markdown Mastigada (Exemplo Visual + Código))

### Títulos e Hierarquia
Para criar títulos, use o símbolo `#` (cerquilha). A quantidade de `#` define o nível do título.
```markdown
# Título Principal (H1)
## Subtítulo (H2)
### Tópico (H3)
```

### Formatação de Texto
```markdown
**negrito** (Use para destacar pontos fortes)
*itálico* (Use para ênfase)
`código inline` (Use para nomes de variáveis ou comandos, ex: `python`)
~~riscado~~ (Use para tarefas canceladas ou conceitos substituídos)
```

### Listas Simples, Numeradas e Checklist
```markdown
- Lista simples (ex: Carga A)
- Lista simples (ex: Carga B)

1. Passos 1 (ex: Separar itens)
2. Passos 2 (ex: Expedir itens)

- [ ] Tarefa pendente (ex: Revisar rota)
- [x] Tarefa concluída (ex: Caminhão liberado)
```

### Blocos de Código Python com Syntax Highlighting
Use 3 crases (```) seguidas do nome da linguagem para criar um bloco de código formatado.
```markdown
```python
def log_delivery(driver, route):
    print(f"Motorista {driver} iniciou a rota {route}")
```
```

### Links Externos, Links Internos de Arquivos e Imagens
```markdown
[Site do Python](https://python.org) - Link Externo
[[Aula 2 - Variáveis e Operadores]] - Link Interno do Obsidian (Wikilink)
![Fluxo Logístico](caminho/para/imagem.png) - Imagem (Adicione um `!` antes do link)
```

### Tabelas Formatadas
```markdown
| ID Rota | Destino | Status |
|---|---|---|
| R-01 | São Paulo | Concluída |
| R-02 | Campinas | Em trânsito |
```

### Callouts Estilizados do Obsidian
Callouts são blocos coloridos excelentes para destacar alertas ou dicas.
```markdown
> [!NOTE]
> Nota: Informação útil de background

> [!TIP]
> Dica: Sugestão de melhoria ou atalho

> [!IMPORTANT]
> Importante: Regra que não pode ser esquecida (ex: conferir os dados antes do script!)

> [!WARNING]
> Aviso: Algo que pode dar errado

> [!SUCCESS]
> Sucesso: Tarefa ou script executado com sucesso
```

----

## 🧠 Parte 2 — Como Usar o Obsidian no Dia a Dia do Curso

### Como abrir o Vault do Curso
1. Abra o Obsidian.
2. Clique em **"Open folder as vault"** (Abrir pasta como vault).
3. Selecione a **pasta raiz** do curso (onde estão todos os arquivos). Todo o repositório é configurado como seu cérebro digital!

### Conectar ideias com Wikilinks `[[Nome da Nota]]`
Sempre que estiver escrevendo e quiser referenciar outro conceito, digite `[[` e comece a digitar o nome da nota. O Obsidian vai sugerir as notas existentes. Isso cria uma rede de conhecimento.

### Como usar o `00 - Dashboard.md` (Kanban + Dataview)
- O **Dashboard** é sua torre de controle.
- Se houver um quadro **Kanban**, use para mover as aulas entre "A Fazer", "Em Andamento" e "Concluído".
- O **Dataview** (quando configurado) listará automaticamente suas anotações com base nas `#tags` que você colocar.

### Como criar notas usando os Templates (`Alt + N` / Templater
O vault possui templates pré-prontos para economizar tempo.
1. Pressione `Alt + N` (ou o atalho configurado no Templater)
2. Escolha entre:
   - `template_aula.md`: Para fazer anotações teóricas
   - `template_exercicio.md`: Para colar e comentar resoluções de exercícios
   - `template_prompt.md`: Para guardar prompts valiosos que você enviou à IA
   - `template_erro.md`: Para documentar erros difíceis que você já resolveu (seu futuro "eu" agradece)

### Usando os plugins instalados
- **Dataview:** Funciona como um banco de dados para suas notas (cria tabelas automáticas)
- **Calendar:** Mostra um calendário na lateral direita. Ótimo para notas diárias.
- **Kanban:** Transforma uma nota em um quadro estilo Trello.
- **Excalidraw:** Permite desenhar fluxogramas de processos logísticos direto na nota.
- **Advanced Tables:** Ajuda a formatar tabelas Markdown magicamente pressionando `Tab`

### Como salvar as notas com Git
Mantenha um backup do seu cérebro na nuvem (GitHub)
Abra o terminal na pasta do Vault e digite:
```bash
git add .
git commit -m "feat: atualiza anotações de python"
git push
```

----

## ⏱️ Parte 3 — Roteiro de 10 Minutos para o Instrutor Usar na Aula

**Objetivo:** Mostrar o valor do Obsidian sem sobrecarregar o aluno iniciante.

- **Minuto 1-2:** O que é o Obsidian? Explique que não é só bloco de notas, é o "caderno de bordo" inteligente do curso, conectando tudo.
- **Minuto 3-4:** Mostre a interface básica. Abra o vault do curso e apresente o arquivo `00 - Dashboard.md` rapidamente.
- **Minuto 5-6:** Sintaxe Básica de Markdown. Mostre na prática: Títulos (`#`), Negrito (`**`) e Listas. Mostre que é rápido escrever assim.
- **Minuto 7-8:** Apresente os Wikilinks (`[[ ]]`). Crie um link entre duas notas demonstrando como as ideias (aulas) se conectam.
- **Minuto 9-10:** Mostre os Templates. Pressione o atalho (`Alt + N`), crie uma "Nota de Erro" ou "Nota de Aula" usando template. Encerre dizendo: "Se algo der erro no Python, crie uma nota no Obsidian pra nunca mais esquecer a solução!"
