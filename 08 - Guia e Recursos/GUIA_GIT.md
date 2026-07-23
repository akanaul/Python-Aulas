# 🔀 Guia Prático de Git, Forks e Exercícios

Bem-vindo(a) ao **Guia Prático de Git e Resolução de Exercícios por Issues**! Neste curso, você aprende Python e automação enquanto domina o controle de versão com Git de forma prática e descomplicada.

---

## 💡 Por que usar Git no Aprendizado?

Assim como no trabalho organizamos pastas, versões de relatórios e revisões de arquivos, o **Git** nos permite:
1. **Trabalhar com Segurança (Branches):** Testar novos códigos em "ramificações" sem quebrar o projeto principal.
2. **Acompanhar Progresso (Commits):** Registrar marcos de avanço a cada exercício concluído.
3. **Validar Soluções (Merge Gatekeeper):** Submeter exercícios para avaliação automatizada antes de incorporar a solução.

---

## 🔄 Fluxo de Trabalho do Aluno (Passo a Passo)

### 1. Criar um Fork do Repositório
No GitHub, clique no botão **Fork** no canto superior direito para criar sua própria cópia de estudos do repositório.

### 2. Clonar seu Fork Localmente
No seu terminal (PowerShell ou Bash):
```bash
git clone https://github.com/SEU_USUARIO/curso-python-ia-automacao.git
cd curso-python-ia-automacao
```

### 3. Escolher uma Issue de Exercício
Consulte as issues disponíveis ou a lista no [[00 - Plano de Estudos e Tarefas.md|📋 Plano de Estudos]].

### 4. Criar uma Branch para o Exercício
Sempre crie uma ramificação (branch) isolada antes de modificar os arquivos:
```bash
git checkout -b feature/issue-07-selenium
```

### 5. Resolver o Exercício (`*_manual.py`)
Escreva sua lógica no arquivo `*_manual.py` com o apoio do **Modo Tutor** da IA.

### 6. Executar o Avaliador Automatizado
Rode o script de avaliação para testar sua solução:
```bash
python avaliar_exercicio.py --issue 07
```

- **Se o teste retornar ❌ SOLUÇÃO RECUSADA:** Leia as dicas diagnósticas, ajuste o código e tente novamente.
- **Se o teste retornar ✅ SOLUÇÃO ACEITA:** Parabéns! Avance para o commit.

### 7. Commit e Merge da Solução
Com o teste aprovado, registre sua conquista:
```bash
git add .
git commit -m "fix(issue-07): solucao aceita em automacao web"
git checkout main
git merge feature/issue-07-selenium
```

---

## 🛠️ Comandos Rápidos de Sobrevivência Git

| Comando | Para que serve? |
| :--- | :--- |
| `git status` | Verifica o estado atual dos seus arquivos modificados |
| `git branch` | Lista todas as branches locais |
| `git checkout main` | Volta para a branch principal |
| `python avaliar_exercicio.py --all` | Executa o avaliador em todos os testes do curso |

---

> [!TIP] Dica de Aprendizado
> Não tenha medo de errar nas branches! O avaliador automatizado está aqui para te dar feedback amigável e seguro em cada etapa.
