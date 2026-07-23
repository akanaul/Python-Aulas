"""
Instruções de como rodar: python -m unittest discover testes

Testes unitários para o Mini-Projeto 3 - Relatório KPI de Entregas.
"""
import unittest

# Simulando funções do módulo principal
def calculate_on_time_percentage(deliveries):
    if not deliveries:
        return 0.0
    on_time = sum(1 for d in deliveries if d.get('delay_minutes', 0) <= 0)
    return (on_time / len(deliveries)) * 100

def calculate_average_delay(deliveries):
    delayed = [d['delay_minutes'] for d in deliveries if d.get('delay_minutes', 0) > 0]
    if not delayed:
        return 0.0
    return sum(delayed) / len(delayed)

def generate_metrics(deliveries):
    return {
        'on_time_pct': calculate_on_time_percentage(deliveries),
        'avg_delay': calculate_average_delay(deliveries)
    }

class TestRelatorioKPI(unittest.TestCase):
    def setUp(self):
        self.deliveries = [
            {'id': 'D1', 'delay_minutes': 0},
            {'id': 'D2', 'delay_minutes': 15},
            {'id': 'D3', 'delay_minutes': 0},
            {'id': 'D4', 'delay_minutes': 45}
        ]

    def test_calculate_on_time_percentage(self):
        """Testa o cálculo de porcentagem de entregas no prazo."""
        pct = calculate_on_time_percentage(self.deliveries)
        self.assertEqual(pct, 50.0)

    def test_calculate_average_delay(self):
        """Testa o cálculo da média de tempo de atraso."""
        avg = calculate_average_delay(self.deliveries)
        self.assertEqual(avg, 30.0)

    def test_generate_metrics(self):
        """Testa a geração de métricas consolidadas."""
        metrics = generate_metrics(self.deliveries)
        self.assertEqual(metrics['on_time_pct'], 50.0)
        self.assertEqual(metrics['avg_delay'], 30.0)

if __name__ == '__main__':
    unittest.main()
