---
sticker: "📇"
tags: [flashcards, srs, estudo, python]
---
# 📇 Central de Flashcards — Repetição Espaçada (Spaced Repetition)

> [!TUTOR] Como Usar este Deck de Memorização
> Pressione `Ctrl + P` (ou `Cmd + P` no Mac) e digite **Spaced Repetition: Review Flashcards**.
> O Obsidian abrirá a interface interativa com cartões divididos por subdecks!

---

## 🐍 Subdeck: Fundamentos de Python & PEP 8
#flashcards/fundamentos

Como se declara a codificação UTF-8 no topo de um script Python em sistemas Windows? :: `# -*- coding: utf-8 -*-` ou configurando `getattr(sys.stdout, "reconfigure", None)`.

Qual é a regra da PEP 8 para nomenclatura de variáveis e funções em Python? :: Usar `snake_case` com letras minúsculas separadas por underline (ex: `calcular_desconto()`).

Qual é a regra da PEP 8 para nomenclatura de Classes em Python? :: Usar `PascalCase` com iniciais maiúsculas sem underline (ex: `ProcessadorDeDados`).

Como converter com segurança uma string `"150"` para inteiro e flutuante? :: `int("150")` para número inteiro e `float("150")` para número decimal.

No Python 3.12+, qual a grande vantagem das f-strings aprimoradas? :: Permitem aspas aninhadas e reutilização de aspas duplas internas dentro da expressão `{dados["chave"]}`.

---

## 📦 Subdeck: Estruturas de Dados & Operadores
#flashcards/sintaxe

Qual é a diferença entre uma Lista `[]` e uma Tupla `()` em Python? :: Listas são mutáveis (podem ser alteradas), enquanto Tuplas são imutáveis (fixas).

Como remover duplicatas de uma lista mantendo apenas elementos únicos? :: Convertendo a lista para um conjunto `set()` (ex: `list(set(lista_com_duplicatas))`).

O que faz o método `.get()` de um Dicionário em Python? :: Busca o valor de uma chave com segurança. Se a chave não existir, retorna `None` ou um valor padrão em vez de estourar `KeyError`.

Como funciona uma List Comprehension simples para filtrar números pares? :: `[x for x in lista if x % 2 == 0]`

Como combinar duas listas em pares dentro de um loop `for`? :: Usando a função integrada `zip(lista_a, lista_b)`.

Como obter tanto o índice numérico quanto o valor de uma lista num loop `for`? :: Usando a função integrada `enumerate(lista, start=1)`.

---

## 🧩 Subdeck: Programação Orientada a Objetos (POO) & Dataclasses
#flashcards/poo

O que é o método especial `__init__` em uma classe Python? :: É o construtor da classe, executado automaticamente quando um novo objeto é instanciado.

O que o parâmetro `self` representa dentro dos métodos de uma classe? :: Representa a própria instância atual do objeto sendo manipulado.

Para que serve o decorator `@dataclass` do módulo `dataclasses`? :: Elimina o código repetitivo (*boilerplate*) gerando automaticamente `__init__`, `__repr__` e `__eq__`.

No Python 3.10+, qual o benefício de usar `@dataclass(slots=True)`? :: Otimiza o consumo de memória RAM criando slots fixos para os atributos da classe.

Como indicar um atributo como protegido por convenção em Python? :: Adicionando um sublinhado prefixado no nome do atributo (ex: `self._saldo`).

---

## 🛣️ Subdeck: Manipulação de Arquivos & `pathlib`
#flashcards/pathlib

Qual é a Regra de Ouro para definir caminhos de arquivos seguros no Python? :: Usar `Path(__file__).resolve().parent` para criar caminhos absolutos relativos ao próprio script.

Por que NUNCA devemos escrever caminhos fixos como `C:\Users\...` no código? :: Porque o código quebrará ao ser executado em outro computador, servidor ou sistema (Linux/macOS).

Como ler o conteúdo de um arquivo TXT em UTF-8 em 1 linha com `pathlib`? :: `conteudo = Path("arquivo.txt").read_text(encoding="utf-8")`

Como verificar se um arquivo ou pasta existe antes de abrir usando `pathlib`? :: `Path("caminho").exists()` ou `Path("caminho").is_file()`

Como criar uma pasta caso ela ainda não exista usando `pathlib`? :: `Path("minha_pasta").mkdir(exist_ok=True)`

---

## 🤖 Subdeck: Automação Desktop (PyAutoGUI) & Web (Selenium)
#flashcards/automacao

Para que serve a instrução `pyautogui.FAILSAFE = True`? :: É uma trava de segurança que cancela a automação do mouse ao movê-lo para o canto superior esquerdo `(0,0)`.

Por que NUNCA devemos usar `time.sleep()` fixo no Selenium WebDriver? :: Porque o tempo de carregamento da rede varia. Devemos usar `WebDriverWait` com `expected_conditions`.

No Selenium, qual é a diferença entre `By.ID` e `By.CSS_SELECTOR`? :: `By.ID` localiza por atributo id único, enquanto `By.CSS_SELECTOR` usa seletores CSS flexíveis.

Como rodar o navegador Chrome no Selenium em segundo plano sem janela física? :: Adicionando `options.add_argument("--headless=new")` ao `chrome_options`.

O que o comando `pyautogui.locateOnScreen("imagem.png", confidence=0.8)` faz? :: Localiza a posição de uma imagem de referência na tela do computador com 80% de precisão.

---

## 🔀 Subdeck: Aprendizado Ativo de Git & Revisão Dupla (IA + Tutor)
#flashcards/git

Como criar uma nova branch Git isolada para um exercício do curso? :: `git checkout -b feature/issue-XX-exercicio`

Qual é o primeiro passo para avaliar um exercício localmente antes de enviar o PR? :: Rodar no terminal: `python avaliar_exercicio.py --issue XX`.

O que significa quando o avaliador retorna `🎉 ✅ PRÉ-APROVADO PELA IA!`? :: Significa que o código passou em 100% dos testes unitários automatizados locais.

Qual é o papel do Professor/Tutor (@akanaul) na revisão dupla? :: Revisar o Pull Request (PR) submetido pelo aluno no GitHub e fazer o Merge oficial.

Como enviar sua branch para o seu fork no GitHub? :: `git push origin feature/nome-da-branch`


---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #all)
> 📌 **Exercício Avaliado:** Issue #all — Suíte Geral de Testes do Vault
> 📁 **Arquivo de Trabalho na IDE:** `avaliar_exercicio.py --all`
> ⚡ Clique no botão **Run** no canto superior direito do bloco abaixo para testar sua solução:

```python run
import sys, os, subprocess

def find_vault_root():
    curr = os.path.abspath(os.getcwd())
    while curr:
        if os.path.exists(os.path.join(curr, "avaliar_exercicio.py")):
            return curr
        parent = os.path.dirname(curr)
        if parent == curr:
            break
        curr = parent
    user_home = os.path.expanduser("~")
    for root, dirs, files in os.walk(user_home):
        if "avaliar_exercicio.py" in files:
            return root
        if root.count(os.sep) - user_home.count(os.sep) >= 4:
            dirs.clear()
    return os.path.abspath(".")

vault_root = find_vault_root()
script_path = os.path.join(vault_root, "avaliar_exercicio.py")
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #all...")
print("📁 Arquivo Alvo na IDE: avaliar_exercicio.py --all")
res = subprocess.run([sys.executable, script_path, "--issue", "all"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```
