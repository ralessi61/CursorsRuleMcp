# Esempio: paradigmi agentici (con LLM simulato)

Tre script Python (solo libreria standard, Python 3.10+) che mostrano il **flusso** dei principali paradigmi. L'LLM è finto (risposte scritte a mano), quindi **non servono API key** né installazioni: l'obiettivo è capire la struttura del ciclo. Teoria: [docs/03-paradigmi-agentici.md](../../docs/03-paradigmi-agentici.md).

| File | Paradigma | Cosa mostra |
|------|-----------|-------------|
| `react_loop.py` | ReAct | ciclo Pensiero → Azione → Osservazione con limite di passi |
| `plan_and_execute.py` | Plan and Execute | un piano creato all'inizio, poi eseguito passo per passo |
| `reflection.py` | Reflection | una bozza sbagliata corretta da un critico (fonte e numeri) |
| `strumenti.py` | – | tool simulati (`cerca_documenti`, `calcola`) |

## Esecuzione
```bash
cd examples/paradigmi-agentici
python react_loop.py
python plan_and_execute.py
python reflection.py
```

## Esercizi
- Sostituisci `llm_finto` con una vera chiamata a un modello (leggi la chiave da una variabile d'ambiente con `os.environ`, mai nel codice).
- In ReAct, abbassa `MAX_PASSI` a 1: cosa succede?
- Nel critico di Reflection aggiungi un controllo: la risposta non deve superare 200 caratteri.
