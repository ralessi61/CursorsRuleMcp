# Esempio: assistente RAG sui documenti aziendali (Rule + MCP)

Combina i due concetti:
- **MCP** (`.cursor/mcp.json`): registra il server `documenti-aziendali` di [mcp-server-python](../mcp-server-python/README.md), che fornisce il tool `cerca_documenti`.
- **Rule** (`.cursor/rules/risposte-con-citazioni.mdc`, tipo Agent Requested): obbliga l'agente a cercare nei documenti, **citare la fonte** e rispondere **"non trovato nei documenti"** se l'informazione manca.

## Che problema risolve
Un assistente aziendale deve essere **affidabile**: niente risposte inventate (allucinazioni) e possibilità di verificare ogni risposta. Il tool dà i dati, la regola impone il comportamento. Approfondimento: [docs/04-rules-e-mcp-insieme.md](../../docs/04-rules-e-mcp-insieme.md) e [docs/03-paradigmi-agentici.md](../../docs/03-paradigmi-agentici.md).

## Preparazione
```bash
cd examples/mcp-server-python
python -m venv .venv
.venv/bin/pip install -r requirements.txt   # Windows: .venv\Scripts\pip
```
Poi apri `examples/rag-documenti-aziendali` come **workspace** in Cursor (Cursor legge `.cursor` solo nella radice del workspace). I percorsi `../mcp-server-python/.venv/bin/python` e `../mcp-server-python/server.py` sono relativi a questa cartella; se Cursor non lo risolve, usa un percorso assoluto (su Windows: `.venv\Scripts\python.exe`).

## Prompt da provare e risultato atteso
| Prompt | Risposta attesa |
|--------|-----------------|
| "Quanti giorni di ferie ho all'anno?" | "26 giorni [fonte: policy-ferie.md]" |
| "Qual è il rimborso massimo per un pasto?" | "30 euro [fonte: rimborsi-spese.md]" |
| "Qual è il dress code aziendale?" | "non trovato nei documenti" |

## Aggiungere documenti
Metti nuovi file `.md` in `examples/mcp-server-python/documenti/`: il server li legge a ogni ricerca.
