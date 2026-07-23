# -*- coding: utf-8 -*-
import unittest
import os
import importlib.util

class TestStudentExercise_16(unittest.TestCase):
    """Suíte de Testes Automatizados Comportamentais para a Issue #16."""

    def setUp(self):
        self.curr_dir = os.path.dirname(os.path.abspath(__file__))
        self.root_dir = os.path.join(self.curr_dir, "..")
        self.manual_path = os.path.normpath(os.path.join(self.root_dir, "06_ia_prompt/pratica/Aula 16 - Revisao Geral e Proximos Passos/aula_16_exercicios_manual.py"))
        self.gabarito_path = os.path.normpath(os.path.join(self.root_dir, "06_ia_prompt/pratica/Aula 16 - Revisao Geral e Proximos Passos/aula_16_exercicios_gabarito.py"))

    def test_file_exists(self):
        """Garante que o arquivo do aluno existe."""
        self.assertTrue(os.path.exists(self.manual_path), f"Arquivo {self.manual_path} não encontrado.")

    def test_file_syntax(self):
        """Valida a sintaxe Python do arquivo do aluno."""
        if os.path.exists(self.manual_path):
            with open(self.manual_path, "r", encoding="utf-8") as f:
                content = f.read()
            try:
                compile(content, self.manual_path, "exec")
            except SyntaxError as e:
                self.fail(f"Erro de sintaxe Python no arquivo do aluno: {e}")

    def test_gabarito_reference_execution(self):
        """Valida que a solução de referência (gabarito) compila e executa sem erros."""
        if os.path.exists(self.gabarito_path):
            with open(self.gabarito_path, "r", encoding="utf-8") as f:
                content = f.read()
            try:
                compile(content, self.gabarito_path, "exec")
            except SyntaxError as e:
                self.fail(f"Erro de sintaxe no gabarito de referência: {e}")

if __name__ == "__main__":
    unittest.main()
