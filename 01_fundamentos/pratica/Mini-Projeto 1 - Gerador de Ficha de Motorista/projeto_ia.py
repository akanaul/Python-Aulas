"""
=============================================================================
🌟 MINI-PROJETO 4: Robô de Preenchimento (Solução IA)
=============================================================================
Este arquivo contém a solução completa gerada por IA.

🤖 PROMPT ONE-SHOT:
"Crie um script Python usando pyautogui e time. Ele deve iterar sobre uma lista de dicionários 
(representando dados logísticos: ID, Carga, Destino). Para cada item:
1. Pausar 1 segundo.
2. Digitar o ID, apertar TAB.
3. Digitar Carga, TAB.
4. Digitar Destino, ENTER.
Inclua um aviso de segurança (time.sleep inicial de 3s) e pyautogui.FAILSAFE = True."
=============================================================================
"""

import pyautogui
import time

# Configuração de Segurança (MUITO IMPORTANTE)
pyautogui.FAILSAFE = True  # Jogue o mouse para o canto da tela para abortar!
pyautogui.PAUSE = 0.5      # Pausa de meio segundo entre comandos do pyautogui

def run_bot(data_list: list) -> None:
    print("🤖 Robô iniciando em 5 segundos! Mude para a janela do formulário AGORA.")
    time.sleep(5)
    
    print("▶️ Iniciando preenchimento...")
    for item in data_list:
        # Digita ID
        pyautogui.write(str(item['id']))
        pyautogui.press('tab')
        
        # Digita Carga
        pyautogui.write(item['carga'])
        pyautogui.press('tab')
        
        # Digita Destino
        pyautogui.write(item['destino'])
        pyautogui.press('enter')
        
        print(f"✅ Cadastro {item['id']} processado.")
        time.sleep(1) # Pausa entre registros

    print("🏁 Automação concluída!")

if __name__ == "__main__":
    # Dados fictícios para automação
    logistics_data = [
        {"id": "1001", "carga": "Eletrônicos", "destino": "São Paulo"},
        {"id": "1002", "carga": "Alimentos", "destino": "Rio de Janeiro"},
        {"id": "1003", "carga": "Vestuário", "destino": "Belo Horizonte"}
    ]
    
    run_bot(logistics_data)
