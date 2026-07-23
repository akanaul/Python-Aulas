"""
Instruções de como rodar: python -m unittest discover testes

Testes unitários para o Mini-Projeto 2 - Analisador de Rotas.
"""
import unittest

# Simulando funções do módulo principal
def filter_delayed_routes(routes):
    return [r for r in routes if r.get('status') == 'delayed']

def calculate_total_distance(routes):
    return sum(r.get('distance', 0) for r in routes)

def find_longest_route(routes):
    if not routes:
        return None
    return max(routes, key=lambda r: r.get('distance', 0))


class TestAnalisadorRotas(unittest.TestCase):
    def setUp(self):
        self.routes = [
            {'id': 1, 'distance': 150, 'status': 'on_time'},
            {'id': 2, 'distance': 300, 'status': 'delayed'},
            {'id': 3, 'distance': 50, 'status': 'delayed'},
            {'id': 4, 'distance': 500, 'status': 'on_time'}
        ]

    def test_filter_delayed_routes(self):
        """Testa a filtragem de rotas atrasadas."""
        delayed = filter_delayed_routes(self.routes)
        self.assertEqual(len(delayed), 2)
        self.assertTrue(all(r['status'] == 'delayed' for r in delayed))

    def test_calculate_total_distance(self):
        """Testa o cálculo da distância total das rotas."""
        total = calculate_total_distance(self.routes)
        self.assertEqual(total, 1000)

    def test_find_longest_route(self):
        """Testa a identificação da rota mais longa."""
        longest = find_longest_route(self.routes)
        self.assertEqual(longest['id'], 4)

if __name__ == '__main__':
    unittest.main()
