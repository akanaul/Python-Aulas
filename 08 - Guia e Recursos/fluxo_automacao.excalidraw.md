---
excalidraw-plugin: parsed
tags: [excalidraw, diagrama, arquitetura]
---
# Fluxo de Automação e Aprendizado

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "node1",
      "type": "rectangle",
      "x": 100,
      "y": 100,
      "width": 200,
      "height": 80,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "#a5d8ff",
      "fillStyle": "hachure",
      "strokeWidth": 2,
      "text": "1. Estudo da Aula\n(Obsidian Vault)"
    },
    {
      "id": "node2",
      "type": "rectangle",
      "x": 350,
      "y": 100,
      "width": 200,
      "height": 80,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "#ffd8a8",
      "fillStyle": "hachure",
      "strokeWidth": 2,
      "text": "2. Exercício Manual\n(*_manual.py)"
    },
    {
      "id": "node3",
      "type": "rectangle",
      "x": 600,
      "y": 100,
      "width": 200,
      "height": 80,
      "strokeColor": "#1e1e1e",
      "backgroundColor": "#b2f2bb",
      "fillStyle": "hachure",
      "strokeWidth": 2,
      "text": "3. Avaliador Git\n(avaliar_exercicio.py)"
    }
  ],
  "appState": {
    "viewBackgroundColor": "#ffffff"
  }
}
```

## 🗺️ Descrição do Fluxo
1. **Estudo da Aula:** Aluno lê a nota no Obsidian com a IA no Modo Tutor.
2. **Exercício Manual:** Aluno desenvolve o script `*_manual.py` na sua IDE (Cursor/VSCode).
3. **Avaliador Git:** Aluno roda `python avaliar_exercicio.py --issue XX` e faz o merge da branch aprovada.
