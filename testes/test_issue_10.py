# -*- coding: utf-8 -*-
import unittest
import os

class TestStudentExercise_10(unittest.TestCase):
    """Suíte de Testes Automatizados para a Issue #10."""

    def setUp(self):
        self.curr_dir = os.path.dirname(os.path.abspath(__file__))
        self.root_dir = os.path.join(self.curr_dir, "..")
        self.file_path = os.path.normpath(os.path.join(self.root_dir, r"04_bibliotecas_arquivos\Aula 10 - Arquivos txt e csv\aula_10_exercicios_manual.py"))

    def test_file_exists(self):
        """Garante que o arquivo de exercício do aluno existe."""
        self.assertTrue(os.path.exists(self.file_path), f"Arquivo {self.file_path} não encontrado.")

    def test_file_syntax(self):
        """Valida que o arquivo do aluno não possui erros de sintaxe Python."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read()
            try:
                compile(content, self.file_path, "exec")
            except SyntaxError as e:
                self.fail(f"Erro de sintaxe Python no arquivo do aluno: {e}")

if __name__ == "__main__":
    unittest.main()
