---
tags: [python312, automacao, selenium, webdriver, scraping]
---
# 🌐 Referência Técnica — Automação Web com Selenium WebDriver

## 📌 1. Inicialização com ChromeOptions & Headless Mode
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# Rodar sem abrir janela física do navegador (ideal para servidores de CI/CD)
# options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
```

---

## 📌 2. Espera Explícita Otimizada (`WebDriverWait` & `EC`)

> [!CAUTION]
> **Nunca use `time.sleep()` fixo.** Sempre prefira `WebDriverWait` com `expected_conditions` para aguardar elementos dinâmicos na DOM!

```python
driver.get("https://example.com/login")

# Aguardar até 10 segundos para o elemento estar clicável
wait = WebDriverWait(driver, 10)
campo_usuario = wait.until(EC.element_to_be_clickable((By.ID, "username")))
campo_usuario.send_keys("aluno_python")

campo_senha = driver.find_element(By.ID, "password")
campo_senha.send_keys("senha_segura123")

botão_login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
botão_login.click()

# Fechar driver ao finalizar
driver.quit()
```


---

## ⚡ Avaliação 1-Clique dos Exercícios da IDE

> [!EXERCICIO] 🧪 Avaliação 1-Clique dos Exercícios da IDE (Issue #devtools)
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
