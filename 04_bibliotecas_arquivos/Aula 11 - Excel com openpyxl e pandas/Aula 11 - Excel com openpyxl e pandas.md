---
aliases: ["Aula 11 — Excel com openpyxl e pandas"]
tags: [aula, bloco-4, python, excel, pandas, openpyxl]
---
# Aula 11 — Excel com openpyxl e pandas
> 💡 **O que você vai aprender:** Automação de planilhas `.xlsx`! Ler, formatar e criar relatórios logísticos.
> ⏱️ **Duração estimada:** 2h | 📅 **Bloco:** 4

---

## 🎯 Objetivos da Aula
- Dominar o `openpyxl` para formatar e interagir célula por célula.
- Usar o `pandas` (básico) para operações brutas de análise de dados.
- Tratar dados de data/hora vindos do Excel usando `datetime` com `zoneinfo`.

---

## 📊 Diagrama Visual (Mermaid)
```mermaid
graph TD
    A[Excel Bruto] -->|Pandas| B(Filtros e Cálculos)
    B -->|OpenPyXL| C[Excel Formatado (Cores, Fórmulas)]
```

---

## 📖 Prosa de 2h (Conceito e Explicação)
O Excel é a tela de pintura da logística. Porém, fazer relatórios VLOOKUP manuais todo dia às 7h da manhã drena a energia.
Com `openpyxl` e `pandas`, fazemos em segundos. E uma dor clássica do Excel é o fuso horário: os servidores do ERP (UTC) salvam planilhas que aqui em SP estão erradas. É aqui que entra o módulo `datetime` e o moderníssimo `zoneinfo` no Python 3.9+, ajustando fusos com perfeição para prazos de entrega precisos (SLA)!

---

## 🔗 Conexão com os Projetos Reais
> 💼 **AutoMDFText:** Exporta os totais extraídos para um relatório em Excel formatado.
> 📊 **AutoPickingPy:** Lê as guias do WMS (Warehouse Management System) em `.xlsx` e gera o relatório final com `pandas`.

---

## 💻 Tríade Dev+IA (Exemplos)

### Exemplo 1 — Lendo Data Certa
```python
from datetime import datetime
from zoneinfo import ZoneInfo
import pandas as pd

# Quando você lê datas do ERP, elas podem vir em UTC
dt_erp = datetime(2023, 10, 1, 12, 0, tzinfo=ZoneInfo("UTC"))
dt_sp = dt_erp.astimezone(ZoneInfo("America/Sao_Paulo"))

print(f"Horário real da entrega BR: {dt_sp}")
```

### Exemplo 2 — Pintando Células (openpyxl)
```python
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

wb = load_workbook('relatorio_estoque.xlsx')
ws = wb.active

green_fill = PatternFill(start_color='00FF00', end_color='00FF00', fill_type='solid')
ws['A1'].fill = green_fill # Destaca o estoque crítico

wb.save('relatorio_estoque_formatado.xlsx')
```

### Exemplo 3 — Com IA (Antigravity)
> 🤖 **Prompt sugerido:**
> "Crie um código usando pandas para carregar `picking.xlsx`, filtrar os que têm a coluna 'Status' igual a 'Pendente', e salvar em um novo arquivo."

---

## 🔗 Links de Código e Prática
> 📁 Arquivo de prática: `exercicios/aula_11_exercicios.py`

**Exercício 1:** Calcule o SLA de entrega usando datetime e timedelta.
**Exercício 2:** Pinte a célula de vermelho se o prazo venceu, usando openpyxl.

---

## 👣 Rodapé / Conexão com a Próxima Aula
Agora que o relatório está pronto, precisamos enviá-lo. Na próxima aula: Automação de Emails e Agendamento.
#aula #bloco-4 #python #excel


---

## 🔀 Aprendizado Ativo de Git, Issue & Pull Request

> 📌 **Issue Oficial no GitHub:** # Issue #11
> 🔀 **Branch de Desenvolvimento:** git checkout -b feature/issue-11-excel-pandas
> 📁 **Arquivo de Trabalho (Manual):** aula_11_exercicios_manual.py
> 🧪 **Teste Automatizado & Pré-Aprovação IA:** python avaliar_exercicio.py --issue 11
> 🚀 **Envio de Pull Request (PR):** git push origin feature/issue-11-excel-pandas e abra o PR no GitHub para a revisão final do Tutor (@akanaul)!
