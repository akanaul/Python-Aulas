#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testes unitários automatizados para os exercícios do Módulo 07 (Automação Web).
"""

import unittest
import importlib.util
import os

class TestWebAutomation(unittest.TestCase):
    """Suíte de teste para validar o extrator de dados web."""

    def setUp(self):
        self.sample_html = """
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
        # Caminho absoluto para a implementação de referência da IA
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        self.ia_script_path = os.path.join(
            curr_dir,
            "..",
            "07_bonus_selenium",
            "pratica",
            "Aula Bonus - Selenium A Proxima Fronteira",
            "devtools_mcp_ia.py"
        )

    def test_ia_extraction_logic(self):
        """Valida se a função de extração da IA retorna os campos ID e Status corretamente."""
        spec = importlib.util.spec_from_file_location("devtools_mcp_ia", self.ia_script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        result = module.extract_record_data(self.sample_html)
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get("id"), "REG-001")
        self.assertEqual(result.get("status"), "Concluído")

if __name__ == "__main__":
    unittest.main()
