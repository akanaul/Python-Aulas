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
