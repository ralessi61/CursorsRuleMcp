# Esempio: paradigmi agentici (con LLM simulato)

Tre script TypeScript che mostrano il **flusso** dei principali paradigmi. L'LLM è finto (risposte scritte a mano), quindi **non servono API key**: l'obiettivo è capire la struttura del ciclo. Teoria: [docs/03-paradigmi-agentici.md](../../docs/03-paradigmi-agentici.md).

| File | Paradigma | Cosa mostra |
|------|-----------|-------------|
| `src/react-loop.ts` | ReAct | ciclo Pensiero → Azione → Osservazione con limite di passi |
| `src/plan-and-execute.ts` | Plan and Execute | un piano creato all'inizio, poi eseguito passo per passo |
| `src/reflection.ts` | Reflection | una bozza sbagliata corretta da un critico (fonte e numeri) |
| `src/strumenti.ts` | – | tool simulati (`cercaDocumenti`, `calcola`) |

## Esecuzione
```bash
cd examples/paradigmi-agentici
npx tsx src/react-loop.ts
npx tsx src/plan-and-execute.ts
npx tsx src/reflection.ts
```
(oppure `npm install` e poi `npm run react`, `npm run plan`, `npm run reflection`)

## Esercizi
- Sostituisci `llmFinto` con una vera chiamata a un modello (usa una variabile d'ambiente per la chiave, mai nel codice).
- In ReAct, abbassa `MAX_PASSI` a 1: cosa succede?
- Nel critico di Reflection aggiungi un controllo: la risposta non deve superare 200 caratteri.
