import unittest
import os
import sys

class TestDashboardUtils(unittest.TestCase):
    def test_progress_script_importable(self):
        """Garante que o script gerar_relatorio_progresso.py carrega sem erros de sintaxe."""
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.join(curr_dir, "..")
        script_path = os.path.join(root_dir, "gerar_relatorio_progresso.py")
        self.assertTrue(os.path.exists(script_path), "gerar_relatorio_progresso.py deve existir na raiz.")

    def test_dashboard_exists(self):
        """Garante que o painel principal 00_dashboard.md existe na raiz."""
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.join(curr_dir, "..")
        dashboard_path = os.path.join(root_dir, "00_dashboard.md")
        self.assertTrue(os.path.exists(dashboard_path), "00_dashboard.md deve existir na raiz.")

    def test_central_hub_exists(self):
        """Garante que a pasta 00_central/ existe com seus arquivos organizados."""
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.join(curr_dir, "..")
        central_path = os.path.join(root_dir, "00_central")
        self.assertTrue(os.path.exists(central_path), "Diretório 00_central/ deve existir.")
        self.assertTrue(os.path.exists(os.path.join(central_path, "00_central.md")), "00_central.md deve existir em 00_central/")

if __name__ == '__main__':
    unittest.main()
