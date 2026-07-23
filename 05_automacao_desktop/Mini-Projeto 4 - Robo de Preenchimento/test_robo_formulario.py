"""
Instruções de como rodar: python -m unittest discover testes

Testes unitários para o Mini-Projeto 4 - Robô de Preenchimento.
"""
import unittest

# Simulando funções do módulo principal
def format_data_line(line):
    # Supondo linha no formato "Nome,Idade,Setor"
    parts = [p.strip() for p in line.split(',')]
    if len(parts) >= 3:
        return {
            'name': parts[0],
            'age': parts[1],
            'department': parts[2]
        }
    return None

class TestRoboFormulario(unittest.TestCase):
    def test_format_data_line_valid(self):
        """Testa a formatação de uma linha de dados válida."""
        line = "Maria, 30, Logística "
        result = format_data_line(line)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'Maria')
        self.assertEqual(result['age'], '30')
        self.assertEqual(result['department'], 'Logística')

    def test_format_data_line_invalid(self):
        """Testa a formatação de uma linha de dados inválida/incompleta."""
        line = "João, 25"
        result = format_data_line(line)
        self.assertIsNone(result)

    def test_format_data_line_empty(self):
        """Testa a formatação de uma linha vazia."""
        line = ""
        result = format_data_line(line)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
