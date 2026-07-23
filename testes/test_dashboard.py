#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testes unitários automatizados para o gerador de relatórios e avaliador.
"""

import unittest
import os
import importlib.util

class TestDashboardUtils(unittest.TestCase):
    """Testes de validação dos utilitários de progresso."""

    def setUp(self):
        self.curr_dir = os.path.dirname(os.path.abspath(__file__))
        self.script_path = os.path.join(self.curr_dir, "..", "gerar_relatorio_progresso.py")

    def test_progress_script_importable(self):
        """Garante que o script gerar_relatorio_progresso.py carrega sem erros de sintaxe."""
        spec = importlib.util.spec_from_file_location("gerar_relatorio", self.script_path)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            self.assertTrue(hasattr(module, "main") or hasattr(module, "calcular_progresso"))
        except Exception as e:
            self.fail(f"Falha ao carregar gerar_relatorio_progresso.py: {e}")

if __name__ == "__main__":
    unittest.main()
