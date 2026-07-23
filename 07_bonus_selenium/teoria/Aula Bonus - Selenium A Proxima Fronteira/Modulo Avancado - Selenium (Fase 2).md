--
aliases: ["Módulo Avançado — Selenium (Fase 2)"
tags: [modulo-2, selenium, web-scraping, curso
--
`
# 🚀 Módulo Avançado: Automação Web Profissional com Selenium (Fase 2

> [!TUTOR] 🚀 Guia Prático de Estudo da Aula (Ciclo de 4 Passos em 1-Clique)
> 1. 📖 **Conceito:** Leia as explicações e tire dúvidas com a IA no **Modo Tutor**.
> 2. 👨‍💻 **Código:** Edite e desenvolva sua solução no arquivo `*_manual.py`.
> 3. ⚡ **Testar no Obsidian (1-Clique):** Clique em **Run** no bloco abaixo para validar:
> > [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #devtools)
> 📌 **Exercício Avaliado:** Issue #devtools — Selenium & Chrome DevTools MCP
> 📁 **Arquivo de Trabalho na IDE:** `07_bonus_selenium/pratica/Aula Bonus - Selenium A Proxima Fronteira/devtools_mcp_manual.py`
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
print("📌 [AVALIAÇÃO 1-CLIQUE] Testando Exercício da Issue #devtools...")
print("📁 Arquivo Alvo na IDE: 07_bonus_selenium/pratica/Aula Bonus - Selenium A Proxima Fronteira/devtools_mcp_manual.py")
res = subprocess.run([sys.executable, script_path, "--issue", "devtools"], cwd=vault_root, capture_output=True, text=True, encoding="utf-8", errors="replace")
print(res.stdout or res.stderr)
```
> 4. 🔀 **Enviar PR:** Se aprovado pela IA, envie o Pull Request no GitHub para o Tutor (@akanaul)!

`
> *Você já dominou o Python básico, o Excel, o OS e o PyAutoGUI. Agora é hora de levar suas automações para a nuvem e para os sistemas web complexos!
`
## 📦 O que é a Fase 2
A Fase 2 é o próximo passo natural do seu aprendizado. Vamos abandonar as limitações de interagir apenas com a "tela" (PyAutoGUI) e passar a interagir diretamente com o "código" dos sites (Selenium)
`
Seja para extrair dados da Secretaria da Fazenda, lançar CT-es em um TMS web, cotar fretes online em vários portais, ou consultar rastreamentos em massa: **O Selenium é a ferramenta definitiva.*
`
--
`
## 📋 Sumário de Tópico
Serão mais de 10 aulas focadas 100% na Web
`
1. **Setup Profissional:** ChromeDriver, EdgeDriver e Webdriver-Manage
2. **Caçando Elementos:** Masterclass de XPath e CSS Selectors (achar qualquer coisa em qualquer site
3. **Interações Avançadas:** Dropdowns, Checkboxes, Uploads e Downloads automático
4. **Esperas Inteligentes:** Adeus `time.sleep`! Olá `WebDriverWait` (o robô espera o site carregar
5. **Web Scraping:** Raspando tabelas de dados inteiras (ex: cotação de moedas/frete) e jogando pro Pandas/Exce
6. **Lidando com Obstáculos:** Como contornar iFrames, múltiplas abas, pop-ups e alertas do sistem
7. **Arquitetura de Projeto Web:** Page Object Model (POM) para robôs complexo
8. **Evolução do AutoMDFText:** Criando a emissão de CIOT direto no site da operadora (Projeto Real)
`
--
`
## ✅ Pré-requisito
- Conclusão da Fase 1 (Python + IA para Automação em Logística
- Entendimento sólido de funções (`def`), listas e dicionário
- Vontade de aprender um pouco de estrutura web (HTML básico, que ensinaremos do zero!
`
--
`
## 🛠️ O que você vai conseguir construir
Ao final desta fase, você será capaz de criar robôs que operam sozinhos "em segundo plano" (Headless Mode), logando em sistemas ERP da sua empresa, baixando relatórios e alimentando os dashboards sem precisar bloquear o seu mouse e teclado
`
--
`
## 📞 Call to Actio
> **Ficou interessado em se tornar um programador de automação logística completo?*
> Fale com o instrutor para garantir sua vaga e acessar os materiais da Fase 2! 
`
--
#modulo-2 #selenium #web-scraping #curs
`

---

## 🔀 Aprendizado Ativo de Git, Issue & Pull Request

> 📌 **Issue Oficial no GitHub:** # Issue #devtools
> 🔀 **Branch de Desenvolvimento:** git checkout -b feature/issue-devtools-devtools-mcp
> 📁 **Arquivo de Trabalho (Manual):** devtools_mcp_manual.py
> 🧪 **Teste Automatizado & Pré-Aprovação IA:** python avaliar_exercicio.py --issue devtools
> 🚀 **Envio de Pull Request (PR):** git push origin feature/issue-devtools-devtools-mcp e abra o PR no GitHub para a revisão final do Tutor (@akanaul)!

---

## 📝 Anotações Pessoais do Aluno sobre esta Aula

> [!TIP] **Criar Nota de Estudo Relacionada**
> Quer guardar resumos ou anotações próprias sobre esta aula?
> Pressione Alt + N no Templater e selecione **Template de Anotação do Aluno** para salvar automaticamente em [[meu_caderno_aluno/anotacoes_aulas/anotacoes_aulas|meu_caderno_aluno/anotacoes_aulas/]]!