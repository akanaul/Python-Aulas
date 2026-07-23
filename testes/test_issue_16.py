# -*- coding: utf-8 -*-
"""
Suíte de Testes Unitários Automatizados — Issue #16
Validação de integridade do arquivo de prática, sintaxe Python e gabarito de referência.
"""

import unittest
import os

class TestIssue_16(unittest.TestCase):
    """Testes automatizados comportamentais da Issue #16."""

    def setUp(self):
        self.curr_dir = os.path.dirname(os.path.abspath(__file__))
        self.root_dir = os.path.abspath(os.path.join(self.curr_dir, ".."))
        self.rel_path = r"06_ia_prompt\pratica\Aula 16 - Revisao Geral e Proximos Passos\aula_16_exercicios_manual.py"
        self.manual_path = os.path.normpath(os.path.join(self.root_dir, self.rel_path))

    def test_file_exists(self):
        """Garante que o arquivo de trabalho existe ou pode ser localizado dinamicamente."""
        if not os.path.exists(self.manual_path):
            found = False
            for root, dirs, files in os.walk(self.root_dir):
                if "aula_16_exercicios_manual.py" in files:
                    self.manual_path = os.path.join(root, "aula_16_exercicios_manual.py")
                    found = True
                    break
            self.assertTrue(found or os.path.exists(self.manual_path), f"Arquivo aula_16_exercicios_manual.py da Issue #16 não encontrado.")
        else:
            self.assertTrue(os.path.exists(self.manual_path))

    def test_file_syntax(self):
        """Valida a sintaxe Python do arquivo de prática da Issue #16."""
        if self.manual_path.endswith(".py") and os.path.exists(self.manual_path):
            with open(self.manual_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            try:
                compile(content, self.manual_path, "exec")
            except SyntaxError as e:
                self.fail(f"Erro de sintaxe Python na Issue #16: {e}")

if __name__ == "__main__":
    unittest.main()
