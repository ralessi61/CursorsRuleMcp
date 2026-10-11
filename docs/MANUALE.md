# Manuale d'uso passo passo

Guida per principianti a **tutti** gli esempi del repository. Segui le sezioni nell'ordine del [percorso consigliato](#percorso-di-apprendimento-consigliato).

> Convenzione: i comandi per **macOS/Linux** usano `python3` e `.venv/bin/...`; su **Windows** (PowerShell) usa `python` e `.venv\Scripts\...`.

---

## 0. Prerequisiti

| Strumento | A cosa serve | Come verificare |
|-----------|--------------|-----------------|
| **Python 3.10+** | eseguire tutti gli esempi | `python3 --version` (Windows: `python --version`) |
| **Git** | scaricare il repository | `git --version` |
| **Cursor** | l'editor con AI, Rules e MCP | apri l'app |
| **Node.js** (solo per l'esempio principale) | avviare i server MCP GitHub e Postgres, che partono con `npx` | `node --version` |

Node.js **non** serve per gli esempi in `examples/`.

## 1. Scaricare il repository

```bash
git clone https://github.com/ralessi61/CursorsRuleMcp.git
cd CursorsRuleMcp
```

Struttura:
```
.cursor/            regole e config MCP dell'esempio principale
src/utils.py        codice di esempio
tests/              test pytest
pyproject.toml      configurazione progetto Python
docs/               documentazione in italiano (questo manuale incluso)
examples/
  rules-avanzate/           i 4 tipi di regole
  mcp-server-python/        server MCP personalizzato (FastMCP)
  paradigmi-agentici/       ReAct, Plan and Execute, Reflection
  rag-documenti-aziendali/  regola + MCP con citazioni
```

## 2. Creare un ambiente virtuale (venv)

Un **venv** è una cartella (`.venv`) con un Python isolato per il progetto: le librerie installate lì non "sporcano" il sistema. Ogni esempio che ha dipendenze ha il suo venv.

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
Quando è attivo, il prompt mostra `(.venv)`. Per uscire: `deactivate`.

> Su Windows, se PowerShell blocca lo script di attivazione: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## 3. Come aprire una cartella in Cursor (importante!)

Cursor legge `.cursor/rules` e `.cursor/mcp.json` **solo nella radice della cartella aperta** (il *workspace*). Quindi:
- per l'esempio principale apri la cartella `CursorsRuleMcp`;
- per ogni esempio in `examples/` apri **quella sottocartella** (*File → Open Folder*), ad esempio `CursorsRuleMcp/examples/rules-avanzate`.

Per vedere i server MCP: **Cursor Settings > MCP**. Ogni server mostra il suo stato (attivo/errore) e l'elenco dei tool. Dopo aver modificato `mcp.json` può servire disattivare/riattivare il server o riavviare Cursor.

---

## Esempio A – Esempio principale (radice)

**Obiettivo:** vedere una regola sempre attiva (stile), una regola legata ai file di test e una regola che dice quando usare un tool MCP.

**File:** `src/utils.py`, `tests/test_utils.py`, `.cursor/rules/style.mdc`, `tests.mdc`, `database.mdc`, `.cursor/mcp.json`.

### Passi
1. Dalla radice del repo crea e attiva il venv (sezione 2).
2. Installa il progetto con le dipendenze di sviluppo:
   ```bash
   pip install -e ".[dev]"
   ```
3. Esegui i test:
   ```bash
   pytest
   ```
   Risultato atteso: `3 passed`.
4. Apri la cartella radice `CursorsRuleMcp` in Cursor.
5. (Facoltativo, MCP GitHub) crea un token GitHub *fine-grained* con permessi minimi e impostalo **prima** di avviare Cursor:
   - macOS/Linux: `export GITHUB_PERSONAL_ACCESS_TOKEN=il_tuo_token`
   - Windows: `$env:GITHUB_PERSONAL_ACCESS_TOKEN="il_tuo_token"`
   
   Poi avvia Cursor dallo stesso terminale (es. `cursor .`, se hai installato il comando da shell).
6. (Facoltativo, MCP Postgres) serve un database PostgreSQL locale su `postgresql://localhost/mydb`; altrimenti modifica l'URL in `.cursor/mcp.json`.
7. Apri **Cursor Settings > MCP** e controlla `github` e `postgres`.

### Prompt da provare
- `write tests for src/utils.py` → si attiva `tests.mdc`: test pytest, con il caso di errore (`pytest.raises`), rete simulata.
- `aggiungi una funzione multiply in src/utils.py` → `style.mdc`: type hint, PEP 8, commenti in inglese.
- `Summarise open issues labelled bug in <owner>/<repo>` → usa il tool MCP GitHub (Cursor chiede conferma prima di eseguirlo).
- `aggiungi una colonna email alla tabella users` → `database.mdc`: prima ispeziona le tabelle con il tool postgres, e chiede conferma prima di DELETE/DROP.

### Problemi comuni
- **`pip install -e` fallisce**: aggiorna pip (`python -m pip install --upgrade pip`) e verifica Python ≥ 3.10.
- **Server `github` in errore**: token non impostato nell'ambiente da cui è partito Cursor, oppure Node.js mancante (`node --version`).
- **Server `postgres` in errore**: database non raggiungibile; per imparare puoi ignorarlo.
- **Mai** scrivere il token in `mcp.json` o in un file del repo.

---

## Esempio B – `examples/rules-avanzate`

**Obiettivo:** capire i 4 tipi di regole: Always, Auto Attached (glob), Agent Requested, Manual.

### Passi
1. ```bash
   cd examples/rules-avanzate
   ```
2. Crea e attiva un venv (sezione 2), poi:
   ```bash
   pip install pytest
   pytest
   ```
   Risultato atteso: `4 passed`.
3. Apri **la cartella `examples/rules-avanzate`** in Cursor (non la radice!).

### Prompt da provare e risultato atteso
| Prompt | Regola | Cosa aspettarsi |
|--------|--------|-----------------|
| `Scrivi una funzione che somma due numeri` | `sempre-italiano.mdc` (Always) | risposta in italiano, Python con type hint |
| apri `tests/test_prezzi.py`, poi `Aggiungi un test per prezzo negativo` | `test-pytest.mdc` (glob `tests/**/*.py`) | funzione `test_...` pytest, niente `unittest` |
| `Come dovrei gestire gli errori in una funzione che legge un file?` | `gestione-errori.mdc` (Agent Requested) | niente `except: pass`, eccezioni specifiche |
| `@checklist-release prepara la release 1.1.0` | `checklist-release.mdc` (Manual) | segue la checklist, propone il tag senza eseguirlo |

### Problemi comuni
- **Le regole non si attivano**: hai aperto la radice del repo invece della sottocartella.
- **La regola glob non parte**: il file di test deve essere nel contesto (aperto o allegato alla chat).
- **`ModuleNotFoundError: prezzi`**: lancia `pytest` dalla cartella `examples/rules-avanzate` (lì c'è `pytest.ini`).

---

## Esempio C – `examples/mcp-server-python`

**Obiettivo:** creare e usare un **server MCP** in Python con il tool `cerca_documenti` e la resource `doc://{nome}`.

### Passi
1. ```bash
   cd examples/mcp-server-python
   ```
2. Crea e attiva il venv **in questa cartella** (deve chiamarsi `.venv`, perché `.cursor/mcp.json` usa `.venv/bin/python`), poi:
   ```bash
   pip install -r requirements.txt
   ```
3. (Facoltativo) test senza Cursor con l'Inspector (richiede Node.js):
   ```bash
   pip install "mcp[cli]<2"
   mcp dev server.py
   ```
4. Apri **la cartella `examples/mcp-server-python`** in Cursor.
5. **Cursor Settings > MCP**: deve comparire `documenti-aziendali-py` attivo con il tool `cerca_documenti`.

### Prompt da provare
- `Quanti giorni di ferie ho?` → chiama `cerca_documenti`; risposta: 26 giorni, fonte `policy-ferie.md`.
- `Qual è il rimborso massimo per un pasto?` → 30 euro (`rimborsi-spese.md`).
- `Posso lavorare da remoto?` → fino a 2 giorni a settimana (`smart-working.md`).
- `Qual è il dress code?` → il tool risponde "non trovato nei documenti".

### Problemi comuni
- **Server in errore / non trovato**: il venv non esiste o non si chiama `.venv`. **Su Windows** modifica `.cursor/mcp.json` con `".venv\\Scripts\\python.exe"`. Se il percorso relativo non funziona, usa percorsi assoluti.
- **`No module named 'mcp.server.fastmcp'`**: hai installato `mcp` 2.x; usa `pip install -r requirements.txt` (che fissa `mcp<2`).
- **Lanciando `python server.py` "non succede nulla"**: è normale, il server attende messaggi su stdin. Interrompi con Ctrl+C.

---

## Esempio D – `examples/paradigmi-agentici`

**Obiettivo:** vedere il flusso di ReAct, Plan and Execute e Reflection con un LLM **simulato** (niente API key, niente installazioni).

### Passi
1. ```bash
   cd examples/paradigmi-agentici
   ```
2. Esegui gli script (macOS/Linux `python3`, Windows `python`):
   ```bash
   python3 react_loop.py
   python3 plan_and_execute.py
   python3 reflection.py
   ```
3. (Facoltativo) apri la cartella in Cursor e chiedi: `Spiegami react_loop.py passo per passo`.

### Risultato atteso
- `react_loop.py`: 3 passi Pensiero/Azione/Osservazione, finale "In 2 anni hai 52 giorni di ferie [fonte: policy-ferie.md]".
- `plan_and_execute.py`: piano di 4 passi, poi un "RIEPILOGO ONBOARDING" con 3 fonti.
- `reflection.py`: Bozza 1 bocciata (manca la fonte, numero 30 inventato), Bozza 2 approvata.

### Problemi comuni
- **`SyntaxError` su `str | None`**: Python troppo vecchio, serve 3.10+.
- **`ModuleNotFoundError: strumenti`**: lancia gli script dalla cartella `examples/paradigmi-agentici`.

Teoria: [03-paradigmi-agentici.md](03-paradigmi-agentici.md).

---

## Esempio E – `examples/rag-documenti-aziendali`

**Obiettivo:** combinare **Rule + MCP**: l'agente deve cercare nei documenti, citare la fonte e dire "non trovato nei documenti" quando l'informazione manca.

### Passi
1. Prepara il server dell'Esempio C (venv `.venv` in `examples/mcp-server-python` con `pip install -r requirements.txt`). Da questa cartella non serve altro: `.cursor/mcp.json` punta a `../mcp-server-python/.venv/bin/python` e `../mcp-server-python/server.py`.
2. Apri **la cartella `examples/rag-documenti-aziendali`** in Cursor.
3. **Cursor Settings > MCP**: deve comparire `documenti-aziendali` attivo.

### Prompt da provare e risultato atteso
| Prompt | Risposta attesa |
|--------|-----------------|
| `Quanti giorni di ferie ho all'anno?` | 26 giorni `[fonte: policy-ferie.md]` |
| `Qual è il rimborso massimo per un pasto?` | 30 euro `[fonte: rimborsi-spese.md]` |
| `Qual è il dress code aziendale?` | "non trovato nei documenti" |

### Problemi comuni
- **Server in errore**: manca il venv dell'Esempio C; su Windows usa `../mcp-server-python/.venv/Scripts/python.exe`; se i percorsi relativi non funzionano, usa percorsi assoluti.
- **Risposta senza citazioni**: la regola è *Agent Requested*; se l'agente non la carica, citala nel prompt: `@risposte-con-citazioni Quanti giorni di ferie ho?`.
- **Aggiungere documenti**: metti nuovi `.md` in `examples/mcp-server-python/documenti/`.

---

## Percorso di apprendimento consigliato

1. Leggi [01-cursor-rules.md](01-cursor-rules.md) → fai l'**Esempio A** (solo la parte rules) e l'**Esempio B**.
2. Leggi [02-mcp.md](02-mcp.md) → fai l'**Esempio C**, poi la parte MCP dell'**Esempio A** (facoltativa).
3. Leggi [03-paradigmi-agentici.md](03-paradigmi-agentici.md) → fai l'**Esempio D** e gli esercizi del suo README.
4. Leggi [04-rules-e-mcp-insieme.md](04-rules-e-mcp-insieme.md) → fai l'**Esempio E**.

## Checklist finale

- [ ] Python ≥ 3.10, Git e Cursor installati (Node.js solo per GitHub/Postgres)
- [ ] Repository clonato
- [ ] Radice: `pip install -e ".[dev]"` e `pytest` → 3 passed
- [ ] `rules-avanzate`: `pytest` → 4 passed; provate le 4 regole aprendo la sottocartella in Cursor
- [ ] `mcp-server-python`: venv `.venv` creato, `pip install -r requirements.txt`, server attivo in Cursor Settings > MCP
- [ ] `paradigmi-agentici`: eseguiti i 3 script
- [ ] `rag-documenti-aziendali`: risposte con `[fonte: ...]` e "non trovato nei documenti" per il dress code
- [ ] Nessun token scritto nei file: solo variabili d'ambiente
