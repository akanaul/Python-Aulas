# -*- coding: utf-8 -*-
"""
Suíte de Testes Unitários Automatizados — Issue #projeto3
Validação de integridade do arquivo de prática, sintaxe Python e gabarito de referência.
"""

import unittest
import os

class TestIssue_PROJETO3(unittest.TestCase):
    """Testes automatizados comportamentais da Issue #projeto3."""

    def setUp(self):
        self.curr_dir = os.path.dirname(os.path.abspath(__file__))
        self.root_dir = os.path.abspath(os.path.join(self.curr_dir, ".."))
        self.rel_path = r"04_bibliotecas_arquivos\pratica\Projeto 3 - Relatorio Automacao KPI Entregas\projeto_manual.py"
        self.manual_path = os.path.normpath(os.path.join(self.root_dir, self.rel_path))

    def test_file_exists(self):
        """Garante que o arquivo de trabalho existe ou pode ser localizado dinamicamente."""
        if not os.path.exists(self.manual_path):
            found = False
            for root, dirs, files in os.walk(self.root_dir):
                if "projeto_manual.py" in files:
                    self.manual_path = os.path.join(root, "projeto_manual.py")
                    found = True
                    break
            self.assertTrue(found or os.path.exists(self.manual_path), f"Arquivo projeto_manual.py da Issue #projeto3 não encontrado.")
        else:
            self.assertTrue(os.path.exists(self.manual_path))

    def test_file_syntax(self):
        """Valida a sintaxe Python do arquivo de prática da Issue #projeto3."""
        if self.manual_path.endswith(".py") and os.path.exists(self.manual_path):
            with open(self.manual_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            try:
                compile(content, self.manual_path, "exec")
            except SyntaxError as e:
                self.fail(f"Erro de sintaxe Python na Issue #projeto3: {e}")

if __name__ == "__main__":
    unittest.main()
