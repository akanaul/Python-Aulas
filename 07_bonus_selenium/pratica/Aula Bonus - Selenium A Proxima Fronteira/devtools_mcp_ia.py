#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# Issue #07-B — Automação Web Otimizada (Abordagem IA One-Shot)

Solução 100% otimizada utilizando BeautifulSoup com type hints e docstrings completos
para extração resiliente de dados de páginas web.
"""

from typing import Dict, Any
from bs4 import BeautifulSoup

def extract_record_data(html_content: str) -> Dict[str, Any]:
    """
    Extrai o código ID e o status da primeira linha da tabela HTML utilizando BeautifulSoup.

    Args:
        html_content (str): Conteúdo HTML a ser parseado.

    Returns:
        Dict[str, Any]: Dicionário com os dados extraídos ou valores padrão se não encontrado.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    row = soup.find("tr")
    
    if not row:
        return {"id": "", "status": ""}
        
    cols = row.find_all("td")
    if len(cols) < 4:
        return {"id": "", "status": ""}
        
    record_id = cols[0].get_text(strip=True)
    status = cols[3].get_text(strip=True)
    
    return {
        "id": record_id,
        "status": status
    }

if __name__ == "__main__":
    sample_html = """
    <table>
        <tbody>
            <tr>
                <td>REG-001</td>
                <td>Relatório Financeiro</td>
                <td>SP -> RJ</td>
                <td><span class="badge status-ok">Concluído</span></td>
            </tr>
        </tbody>
    </table>
    """
    print("Resultado Otimizado IA:", extract_record_data(sample_html))
