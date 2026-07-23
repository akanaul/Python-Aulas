---
aliases: ["Aula 7 — Funções, Decoradores e Geradores"]
tags: [aula, bloco-2, python]
---

> 💡 **O que você vai aprender:** Como encapsular código reutilizável em funções, aplicar metaprogramação com Decoradores (`@wraps`) e construir processadores de dados eficientes com Geradores (`yield`).
> ⏱️ **Duração estimada:** 2h | 📅 **Bloco:** 2

---

## 🎯 Objetivos da Aula
- Criar funções com parâmetros e retornos (`def`, `return`).
- Entender escopos globais e locais.
- Criar **Decoradores** para injetar comportamentos (ex: logs de auditoria).
- Usar **Geradores** (`yield`) para processamento sob demanda (Lazy Evaluation).

---

## 🔗 Conexão com os Projetos Reais
> 💼 **AutoMDFText:** A função `click_and_type(x, y, text)` encapsula múltiplas ações de teclado/mouse numa única chamada, limpando o código.
> 📊 **AutoPickingPy:** Funções organizam passos como "ler_planilha", "processar_linha" e "enviar_email".

---

## 📖 Conceito
Funções são os **SOPs (Standard Operating Procedures - Procedimentos Operacionais Padrão)**. Em vez de explicar toda vez como amarrar a carga, você simplesmente diz: "Execute o SOP de Amarração".
Decoradores (`@`) são os **Fiscais (Auditoria)** que ficam na porta das funções, anotando quem entrou, a hora e se tudo ocorreu bem, sem alterar o SOP em si.
Geradores (`yield`) são como a **Esteira Síncrona**: em vez de entregar 10.000 caixas de uma vez (sobrecarregando o receptor), ela entrega uma (yield), pausa, e só entrega a próxima quando o operador pedir (`next()`).

---

## 💻 Exemplos

### Exemplo 1 — Básico (Funções)

```python
def calculate_freight(weight, distance_km):
    base_rate = 1.5
    return weight * distance_km * base_rate

total = calculate_freight(100, 50)
print(f"Frete: R$ {total:.2f}")
```

### Exemplo 2 — Aplicado à Logística (Decoradores e Geradores)

```python
from functools import wraps
import time

# Decorador de Auditoria e Tempo

> [!TUTOR] 🚀 Guia Prático de Estudo da Aula (Ciclo de 4 Passos em 1-Clique)
> 1. 📖 **Conceito:** Leia as explicações e tire dúvidas com a IA no **Modo Tutor**.
> 2. 👨‍💻 **Código:** Edite e desenvolva sua solução no arquivo `*_manual.py`.
> 3. ⚡ **Testar no Obsidian (1-Clique):** Clique em **Run** no bloco abaixo para validar:
> ```python run
> import subprocess
> res = subprocess.run(["python", "avaliar_exercicio.py", "--issue", "01"], capture_output=True, text=True)
> print(res.stdout)
> ```
> 4. 🔀 **Enviar PR:** Se aprovado pela IA, envie o Pull Request no GitHub para o Tutor (@akanaul)!

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"[AUDIT] Iniciando {func.__name__}...")
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"[AUDIT] Finalizado em {duration:.4f}s")
        return result
    return wrapper

@log_execution
def process_shipment():
    time.sleep(1) # Simula processamento
    return "Expedição Concluída"

# Gerador para leitura infinita (yield)
def read_heavy_inventory_logs():
    for line_number in range(1, 1000000):
        # Em vez de return e acabar, yield pausa a função e entrega 1 por vez
        yield f"Linha de log {line_number} processada."

print(process_shipment())

log_stream = read_heavy_inventory_logs()
print(next(log_stream)) # Linha 1
print(next(log_stream)) # Linha 2
```

### Exemplo 3 — Com IA (Antigravity)
> 🤖 **Prompt sugerido:**
> "Como criar um decorador Python usando `@wraps` que tente rodar uma função falha até 3 vezes (retry decorator) simulando conexão com sistema SEFAZ/ERP lento?"

---

## 📋 Referência Rápida
| Estrutura | Sintaxe | Uso principal |
|---|---|---|
| Função | `def func(args):` | Encapsular lógica |
| Decorador | `@meu_decorador` | Modificar funções sem alterá-las internamente |
| Yield | `yield valor` | Criar geradores econômicos em memória |
| Wraps | `from functools import wraps`| Manter documentação e nome original da função decorada |

---

## ⚠️ Erros Comuns
| Erro | Causa | Solução |
|---|---|---|
| Return None | Esquecer o `return` no final | Coloque `return resultado` |
| Gerador Exausto | Chamar next() após o gerador finalizar | Capture a exceção `StopIteration` ou itere com `for` |

---

## 🏋️ Exercícios
> 📁 Arquivo de prática: `exercicios/aula_07_exercicios.py`

**Exercício 1 — [Nível: Básico]**
Crie uma função `cubagem(altura, largura, comprimento)` que retorne o volume de uma caixa.

**Exercício 2 — [Nível: Intermediário]**
Escreva uma função geradora (usando `yield`) que emita os números pares de um inventário (0, 2, 4, 6...) e teste chamando `next()` 3 vezes.

**Exercício 3 — [Nível: Desafio]**
Crie um decorador simples chamado `@verificar_login` que imprima "Verificando token de acesso..." ANTES de executar uma função chamada `acessar_painel_wms()`.

---

## 🎯 Conexão com a Próxima Aula
Agora que dominamos a base de Python moderna e avançada, estamos prontos para sair da telinha preta e ir para o mundo real: Interação com Arquivos e Automações Básicas (PyAutoGUI, openpyxl). O jogo vai começar!

---
#aula #bloco-2 #python


---

## 🔀 Aprendizado Ativo de Git, Issue & Pull Request

> 📌 **Issue Oficial no GitHub:** # Issue #07
> 🔀 **Branch de Desenvolvimento:** git checkout -b feature/issue-07-funcoes-pep8
> 📁 **Arquivo de Trabalho (Manual):** aula_07_exercicios_manual.py
> 🧪 **Teste Automatizado & Pré-Aprovação IA:** python avaliar_exercicio.py --issue 07
> 🚀 **Envio de Pull Request (PR):** git push origin feature/issue-07-funcoes-pep8 e abra o PR no GitHub para a revisão final do Tutor (@akanaul)!

---

## 📝 Anotações Pessoais do Aluno sobre esta Aula

> [!TIP] **Criar Nota de Estudo Relacionada**
> Quer guardar resumos ou anotações próprias sobre esta aula?
> Pressione Alt + N no Templater e selecione **Template de Anotação do Aluno** para salvar automaticamente em [[meu_caderno_aluno/anotacoes_aulas/anotacoes_aulas|meu_caderno_aluno/anotacoes_aulas/]]!