"""
GABARITO DE REFERÊNCIA (SOLUÇÃO IA) — MINI-PROJETO 3
Relatório Automatizado de KPIs de Entregas
Issue #projeto3
"""

from typing import List, Dict, Any

def gerar_kpi_entregas(entregas: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calcula taxa de sucesso de entregas no prazo (OTIF - On-Time In-Full).
    """
    if not entregas:
        return {"total": 0, "no_prazo": 0, "taxa_otif": 0.0}
        
    no_prazo = sum(1 for e in entregas if e.get("no_prazo", False))
    total = len(entregas)
    taxa = round((no_prazo / total) * 100, 2)
    
    return {
        "total_entregas": total,
        "entregas_no_prazo": no_prazo,
        "taxa_otif_percentual": taxa
    }

if __name__ == "__main__":
    dados = [{"id": 1, "no_prazo": True}, {"id": 2, "no_prazo": True}, {"id": 3, "no_prazo": False}]
    print("KPI Entregas:", gerar_kpi_entregas(dados))
