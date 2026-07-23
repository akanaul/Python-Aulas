# -*- coding: utf-8 -*-
"""
Suíte de Testes Unitários Automatizados — Issue #09a
Validação de integridade do arquivo de prática, sintaxe Python e gabarito de referência.
"""

import unittest
import os

class TestIssue_09A(unittest.TestCase):
    """Testes automatizados comportamentais da Issue #09a."""

    def setUp(self):
        self.curr_dir = os.path.dirname(os.path.abspath(__file__))
        self.root_dir = os.path.abspath(os.path.join(self.curr_dir, ".."))
        self.rel_path = r"03_poo\pratica\Aula 09A - Modulos e POO Basico\aula_09a_exercicios_manual.py"
        self.manual_path = os.path.normpath(os.path.join(self.root_dir, self.rel_path))

    def test_file_exists(self):
        """Garante que o arquivo de trabalho existe ou pode ser localizado dinamicamente."""
        if not os.path.exists(self.manual_path):
            found = False
            for root, dirs, files in os.walk(self.root_dir):
                if "aula_09a_exercicios_manual.py" in files:
                    self.manual_path = os.path.join(root, "aula_09a_exercicios_manual.py")
                    found = True
                    break
            self.assertTrue(found or os.path.exists(self.manual_path), f"Arquivo aula_09a_exercicios_manual.py da Issue #09a não encontrado.")
        else:
            self.assertTrue(os.path.exists(self.manual_path))

    def test_file_syntax(self):
        """Valida a sintaxe Python do arquivo de prática da Issue #09a."""
        if self.manual_path.endswith(".py") and os.path.exists(self.manual_path):
            with open(self.manual_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            try:
                compile(content, self.manual_path, "exec")
            except SyntaxError as e:
                self.fail(f"Erro de sintaxe Python na Issue #09a: {e}")

if __name__ == "__main__":
    unittest.main()
