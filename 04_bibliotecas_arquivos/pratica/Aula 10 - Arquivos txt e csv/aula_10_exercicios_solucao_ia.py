"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — AULA 10
Manipulação de Arquivos TXT, CSV e Pathlib
Issue #10
"""

import csv
from pathlib import Path
from typing import List, Dict

def ler_csv_entregas(filepath: Path) -> List[Dict[str, str]]:
    """
    Lê um arquivo CSV utilizando DictReader.
    """
    if not filepath.exists():
        return []
    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def escrever_relatorio_txt(filepath: Path, linhas: List[str]):
    """
    Escreve linhas formatadas em um arquivo TXT.
    """
    with open(filepath, mode="w", encoding="utf-8") as f:
        for l in linhas:
            f.write(l + "
")

if __name__ == "__main__":
    p = Path("temp_test.txt")
    escrever_relatorio_txt(p, ["Linha 1", "Linha 2"])
    if p.exists():
        p.unlink()
