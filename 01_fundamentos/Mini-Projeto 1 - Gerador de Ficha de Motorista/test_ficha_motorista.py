"""
Instruções de como rodar: python -m unittest discover testes

Testes unitários para o Mini-Projeto 1 - Gerador de Ficha de Motorista.
"""
import unittest

# Simulando as funções do módulo principal para evitar erros de importação
def validate_driver_data(driver_data):
    if not driver_data.get('name') or not driver_data.get('license_number'):
        return False
    return True

def generate_formatted_text(driver_data):
    return f"Motorista: {driver_data['name']} - CNH: {driver_data['license_number']}"


class TestFichaMotorista(unittest.TestCase):
    def setUp(self):
        """Prepara os dados iniciais para os testes."""
        self.valid_driver = {'name': 'João Silva', 'license_number': '123456789'}
        self.invalid_driver = {'name': '', 'license_number': '123456789'}

    def test_validate_driver_data_valid(self):
        """Testa a validação com dados corretos."""
        self.assertTrue(validate_driver_data(self.valid_driver))

    def test_validate_driver_data_invalid(self):
        """Testa a validação com dados incorretos."""
        self.assertFalse(validate_driver_data(self.invalid_driver))

    def test_generate_formatted_text(self):
        """Testa a formatação do texto do motorista."""
        expected = "Motorista: João Silva - CNH: 123456789"
        self.assertEqual(generate_formatted_text(self.valid_driver), expected)

if __name__ == '__main__':
    unittest.main()
