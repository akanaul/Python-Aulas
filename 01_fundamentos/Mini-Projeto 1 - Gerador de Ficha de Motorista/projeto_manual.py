# -*- coding: utf-8 -*-
"""
Exercícios - projeto_manual
Curso: Python + IA para Automação em Logística

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado.
- Use a IA Antigravity no MODO TUTOR (pedindo dicas de lógica).
"""

# -*- coding: utf-8 -*-



import pyautogui
import time
import pyperclip
from pathlib import Path
from typing import List

def create_dummy_txt(filename: str = "entregas.txt") -> None:
    """Cria um arquivo .txt de testes com algumas entregas falsas."""
    content = "NF-1001;Cliente A\nNF-1002;Cliente B\nNF-1003;Cliente C"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def setup_failsafe() -> None:
    """Configura o mecanismo de segurança do PyAutoGUI."""
    # TODO: Passo 1 - Ative o FAILSAFE do pyautogui
    # pyautogui.FAILSAFE = True
    pass

def open_notepad() -> None:
    """Abre o bloco de notas usando atalhos do Windows."""
    # TODO: Passo 2 - Use pyautogui para:
    # 1. Pressionar a tecla 'win'
    # 2. Aguardar 1 segundo
    # 3. Digitar 'notepad'
    # 4. Pressionar 'enter'
    # 5. Aguardar 2 segundos pro app abrir
    pass

def read_data(filename: str) -> List[str]:
    """Lê o arquivo txt e retorna a lista de linhas."""
    # TODO: Passo 3 - Leia o arquivo com 'with open(...)' e retorne um .readlines()
    pass
    # return []

def process_typing(lines: List[str]) -> None:
    """Itera nas linhas e digita no app."""
    # TODO: Passo 4 - Para cada linha na lista:
    # 1. Limpe a quebra de linha com .strip()
    # 2. Copie para a área de transferência usando pyperclip.copy()
    # 3. Cole com pyautogui.hotkey('ctrl', 'v')
    # 4. Dê um pyautogui.press('enter')
    # 5. Espere 0.5 seg com time.sleep()
    pass


if __name__ == "__main__":
    # Teste rápido de ambiente
    create_dummy_txt()
    
    # TODO: Quando implementar as funções, descomente a rotina:
    # setup_failsafe()
    # print("Iniciando automação em 3 segundos...")
    # time.sleep(3)
    # open_notepad()
    # data_lines = read_data("entregas.txt")
    # process_typing(data_lines)
    # print("Finalizado!")
