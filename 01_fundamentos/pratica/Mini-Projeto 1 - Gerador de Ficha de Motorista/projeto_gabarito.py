"""
=============================================================================
🌟 MINI-PROJETO 4: Robô de Preenchimento de Formulário (Gabarito)
=============================================================================
Curso: Python + IA para Automação em Logística
Instrutor: [Nome]

GABARITO:
- Solução passo a passo resolvida pelo instrutor.
=============================================================================
"""

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
    pyautogui.FAILSAFE = True

def open_notepad() -> None:
    """Abre o bloco de notas usando atalhos do Windows."""
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('notepad')
    pyautogui.press('enter')
    time.sleep(2)

def read_data(filename: str) -> List[str]:
    """Lê o arquivo txt e retorna a lista de linhas."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()

def process_typing(lines: List[str]) -> None:
    """Itera nas linhas e digita no app."""
    for line in lines:
        clean_line = line.strip()
        pyperclip.copy(clean_line)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(0.5)


if __name__ == "__main__":
    create_dummy_txt()
    
    setup_failsafe()
    print("Iniciando automação em 3 segundos...")
    time.sleep(3)
    open_notepad()
    data_lines = read_data("entregas.txt")
    process_typing(data_lines)
    print("Finalizado!")
