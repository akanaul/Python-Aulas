# 🤖 Diretriz do Agente: Curadoria Ativa do Vault, Proteção de Testes, Git Flow, Solicitação de Contexto e Progresso do Aluno

> **Regra de Projeto Rígida — Antigravity / IA Assistant**  
> Esta diretriz define o comportamento automático do agente durante as interações com o aluno e o codebase.

---

## 1. 🛡️ Proteção Rígida dos Scripts de Avaliação e Código do Aluno
- **PROIBIÇÃO ESTRITA nos Testes:** O agente **JAMAIS** deve alterar, modificar ou excluir o script `avaliar_exercicio.py` ou os arquivos de teste na pasta `testes/`.
- **PROIBIÇÃO ESTRITA nos Arquivos Manuais:** O agente **JAMAIS** deve sobrescrever o arquivo de trabalho manual do aluno (`*_manual.py`, ex: `aula_01_exercicios_manual.py`). Este arquivo pertence exclusivamente à escrita do aluno.
- **USO LIBERADO DE SOLUÇÃO IA (`*_solucao_ia.py`):** Quando o aluno solicitar a solução demonstrativa ou gabarito da IA, o agente pode escrever a solução completa no arquivo de referência `*_solucao_ia.py` (ex: `aula_01_exercicios_solucao_ia.py`) na pasta de prática ou em `meu_caderno_aluno/anotacoes_aulas/`, para o aluno comparar e aprender.

---

## 2. ❓ Solicitação Ativa de Contexto em Dúvidas Ambíguas
- Se o aluno fizer uma pergunta vaga ou pedir ajuda sem especificar a aula, Issue, arquivo `.py` ou mensagem de erro:
  - **NÃO ADIVINHAR:** O agente não deve assumir arquivos ou códigos cegamente.
  - **SOLICITAR CONTEXTO:** O agente deve perguntar educadamente:
    > *"Para que eu possa te orientar com precisão, qual é a Issue ou Aula que você está estudando? Poderia informar o caminho do arquivo `*_manual.py` e colar a mensagem de erro/traceback do terminal?"*

---

## 3. 🔀 Gestão do Git Flow, Instrução no Terminal e Automação de Commits/PRs
- Sempre que uma solução for aprovada nos testes automatizados (`🎉 PRÉ-APROVADO 100% OK`), o agente deve:
  1. **Exibir o Tutorial Passo a Passo dos Comandos no Terminal:**
     ```bash
     git checkout -b feature/issue-XX
     git add <caminho_do_arquivo>
     git commit -m "fix(issue-XX): resolucao dos exercicios aprovados nos testes #XX"
     git push origin feature/issue-XX
     ```
  2. **Incentivar o Aprendizado no Terminal:** Explicar o propósito de cada comando e incentivar o aluno a rodá-los manualmente no terminal para não esquecer os comandos essenciais.
  3. **Oferecer Automação Conveniente:** Informar ao aluno: *"Se desejar que eu execute a sequência do Git por você (criar branch, add, commit e push), basta me pedir no chat!"*

---

## 4. ⚡ Verificação, Atualização Automática de Progresso e Checklists
- Sempre que o agente responder a uma dúvida de código ou analisar uma solução, ele executa `python avaliar_exercicio.py --issue XX` em segundo plano.
- **Em caso de Sucesso (Pré-Aprovado 100% OK):**
  - O agente registra **AUTOMATICAMENTE** a nota de conclusão em `meu_caderno_aluno/progresso/progresso_issue_XX.md`.
  - **Atualização Automática de Checklists:** O agente/avaliador varre os arquivos de plano de estudos (`00_central/plano_de_estudos.md`), `00 - Dashboard.md` e notas de aulas, alterando os marcadores da Issue de pendente (`- [ ]`) para concluído (`- [x]`).

---

## 5. ✍️ Sugestão Prévia de Notas de Estudos / Dúvidas
- Antes de criar notas em `meu_caderno_aluno/anotacoes_aulas/` ou `meu_caderno_aluno/duvidas/`, o agente sugere previamente ao aluno:
  - *"Gostaria que eu registrasse essa explicação/dúvida no seu caderno de estudos em 'meu_caderno_aluno/anotacoes_aulas/' usando o template oficial?"*

---

## 6. 🗂️ Estrutura de Pastas do Caderno do Aluno (`meu_caderno_aluno/`)
- `meu_caderno_aluno/anotacoes_aulas/` ➔ Resumos e reflexões teóricas sugeridas ao aluno.
- `meu_caderno_aluno/diagnostico_erros/` ➔ Registros de falhas com dicas do mentor e flashcards.
- `meu_caderno_aluno/duvidas/` ➔ Dúvidas registradas para revisão espaçada.
- `meu_caderno_aluno/progresso/` ➔ Registros automáticos de aprovação de exercícios e tarefas.
