# Esempio: Rules avanzate

Quattro regole in `.cursor/rules/`, una per ogni tipo:

| File | Tipo | Si attiva... |
|------|------|--------------|
| `sempre-italiano.mdc` | Always | sempre |
| `test-pytest.mdc` | Auto Attached (glob `tests/**/*.py`) | quando nel contesto c'è un file di test |
| `gestione-errori.mdc` | Agent Requested | quando l'agente ritiene utile la description |
| `checklist-release.mdc` | Manual | solo se scrivi `@checklist-release` |

File di esempio: `prezzi.py` (codice) e `tests/test_prezzi.py` (test pytest; per eseguirli: `pip install pytest && pytest`).

## ⚠️ Importante: apri questa cartella come workspace
Cursor legge solo la cartella `.cursor` nella **radice del workspace**. Per provare queste regole:
**File → Open Folder → `examples/rules-avanzate`** (aprila come progetto a sé).

## Prompt da provare
1. **Always** – "Scrivi una funzione che somma due numeri" → risposta in italiano, Python con type hint.
2. **Auto Attached** – apri `tests/test_prezzi.py` e chiedi "Aggiungi un test per prezzo negativo" → funzione `test_...` pytest, con `parametrize`/`pytest.raises`, niente `unittest`.
3. **Agent Requested** – "Come dovrei gestire gli errori in una funzione che legge un file?" → l'agente dovrebbe caricare `gestione-errori.mdc`.
4. **Manual** – "@checklist-release prepara la release 1.1.0" → segue la checklist e non esegue il tag.

Suggerimento: nel pannello della chat Cursor mostra quali regole sono state applicate.
