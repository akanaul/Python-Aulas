---
tags: [python312, automacao, pyautogui, desktop, gui]
---
# 🤖 Referência Técnica — Automação GUI com PyAutoGUI

## 📌 1. Configurações de Segurança Obrigatórias
```python
import pyautogui

# Habilitar FAILSAFE (mover o mouse para o canto superior esquerdo (0,0) cancela a execução)
pyautogui.FAILSAFE = True

# Pausa de 0.5 segundos entre cada comando para simular digitação humana
pyautogui.PAUSE = 0.5
```

---

## 📌 2. Controle de Mouse & Resolução de Tela
```python
# Obter resolução da tela atual
largura, altura = pyautogui.size()
print(f"Resolução: {largura}x{altura}")

# Mover mouse suavemente para posição (X=500, Y=300) em 1.5 segundos
pyautogui.moveTo(500, 300, duration=1.5)

# Clique com botão esquerdo e duplo clique
pyautogui.click(500, 300)
pyautogui.doubleClick()
pyautogui.rightClick()
```

---

## 📌 3. Reconhecimento de Imagens na Tela (PyScreeze)
```python
# Localizar um botão na tela usando uma imagem de referência em PNG
try:
    posicao = pyautogui.locateOnScreen("assets/botao_confirmar.png", confidence=0.8)
    if posicao:
        centro_x, centro_y = pyautogui.center(posicao)
        pyautogui.click(centro_x, centro_y)
        print("✅ Botão localizado e clicado!")
except pyautogui.ImageNotFoundException:
    print("❌ Botão não localizado na tela.")
```
