# Paradigmi agentici

Un **agente** è un LLM che, in un ciclo, decide quali azioni compiere (chiamare tool, leggere dati) per raggiungere un obiettivo. Esistono diversi schemi ("paradigmi") per organizzare questo ciclo.

## 1. Single-shot tool use
Il modello riceve la domanda, chiama **un** tool (o nessuno) e risponde.
- ✅ Veloce, economico, prevedibile.
- ❌ Non gestisce compiti a più passi.
- Quando: domande semplici ("che tempo fa a Roma?", "cerca il documento X").

## 2. ReAct (Reason + Act)
Ciclo **Pensiero → Azione → Osservazione**, ripetuto finché il modello decide di rispondere.
```
Pensiero: devo trovare la policy ferie
Azione: cerca_documenti("ferie")
Osservazione: trovato policy-ferie.md ...
Pensiero: ho abbastanza informazioni
Risposta: ...
```
- ✅ Flessibile, si adatta a ciò che scopre.
- ❌ Più chiamate = più costo e latenza; può girare a vuoto (serve un limite di passi).
- Quando: ricerca esplorativa, debugging, domande dove non sai in anticipo cosa serve.

## 3. Plan and Execute
Prima un **pianificatore** scrive l'elenco dei passi, poi un **esecutore** li svolge uno per uno.
- ✅ Struttura chiara, piano ispezionabile (anche da un umano), passi eseguibili da un modello più economico.
- ❌ Se il piano è sbagliato serve ri-pianificare; meno reattivo.
- Quando: compiti lunghi e prevedibili (migrazioni, report in più sezioni).

## 4. Reflection
Il modello produce una bozza, poi un **critico** (lo stesso o un altro modello) la valuta e si corregge, per N iterazioni.
- ✅ Qualità più alta, meno errori.
- ❌ Raddoppia/triplica costi e latenza.
- Quando: output dove la qualità conta molto (codice, testi importanti, risposte con citazioni).

## Trade-off

| Paradigma | Qualità | Costo | Latenza | Rischio (azioni non volute / loop) |
|-----------|---------|-------|---------|-----------------------------------|
| Single-shot | bassa-media | basso | bassa | basso |
| ReAct | media-alta | medio-alto | variabile | medio (serve max passi) |
| Plan and Execute | alta su compiti lunghi | medio | medio-alta | basso-medio (piano verificabile) |
| Reflection | alta | alto | alta | basso |

Regola pratica: **parti dal paradigma più semplice** che risolve il problema e aggiungi complessità solo se misuri un beneficio.

## Esempio: assistente sui documenti aziendali (priorità: affidabilità)
Obiettivo: rispondere ai dipendenti usando solo i documenti interni, **con citazioni**, senza inventare.

Design consigliato:
1. **ReAct leggero** con tool `cerca_documenti` (via MCP), massimo 3-4 passi.
2. **Reflection** finale: un controllo verifica che ogni frase sia supportata da un documento citato; se no la rimuove.
3. **Regola** (Cursor Rule) che impone: cita la fonte `[fonte: nome-file.md]`; se l'informazione non c'è rispondi **"non trovato nei documenti"**.

Perché non solo single-shot? Le domande possono richiedere più documenti. Perché non Plan and Execute? Le domande sono brevi e imprevedibili, un piano rigido aggiunge latenza senza vantaggi. La Reflection costa di più ma riduce le allucinazioni, che qui sono il rischio principale.

Vedi: [examples/paradigmi-agentici](../examples/paradigmi-agentici/README.md) e [examples/rag-documenti-aziendali](../examples/rag-documenti-aziendali/README.md).
