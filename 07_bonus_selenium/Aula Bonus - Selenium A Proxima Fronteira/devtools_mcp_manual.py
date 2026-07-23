# -*- coding: utf-8 -*-
"""
Exercícios - devtools_mcp_manual
Curso: Python + IA para Automação em Logística

INSTRUÇÕES:
- Resolva cada exercício no espaço indicado.
- Use a IA Antigravity no MODO TUTOR (pedindo dicas de lógica).
"""

# -*- coding: utf-8 -*-


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Issue #07-B — Automação Web Avançada com Chrome DevTools MCP (Modo Tutor)

# Este arquivo é um exercício guiado para praticar a inspeção e extração de dados
# de páginas web utilizando o Chrome DevTools MCP e seletores CSS/XPATH.

# Regras do Modo Tutor:
# - Escreva sua lógica passo a passo nos locais indicados.
# - Teste com: python avaliar_exercicio.py --issue 07

from typing import Dict, Any

# def extract_record_data(html_content: str) -> Dict[str, Any]:
#     Função para extrair o código ID e o status da primeira linha da tabela HTML.
    
#     Parâmetros:
#         html_content (str): String contendo o HTML da página web_playground.html.
        
#     Retorna:
#         Dict[str, Any]: Dicionário no formato {'id': 'REG-001', 'status': 'Concluído'}
    # 💡 Dica do Mentor:
    # 1. Utilize a biblioteca BeautifulSoup (ou regex simples) para encontrar a tag <table>.
    # 2. Localize a primeira tag <tr> da tabela dentro do <tbody>.
    # 3. Extraia o texto do primeiro <td> (ID) e o texto da <span> dentro do último <td> (Status).

#     record_data = {
#         "id": "",
#         "status": ""
#     }

    # TODO: Escreva sua lógica de extração aqui:

#     return record_data


# if __name__ == "__main__":
#     sample_html = """
#     <table>
#         <tbody>
#             <tr>
#                 <td>REG-001</td>
#                 <td>Relatório Financeiro</td>
#                 <td>SP -> RJ</td>
#                 <td><span class="badge status-ok">Concluído</span></td>
#             </tr>
#         </tbody>
#     </table>
#     result = extract_record_data(sample_html)
#     print("Resultado da Extração Manual:", result)