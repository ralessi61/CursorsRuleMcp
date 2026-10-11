# Esempio: Rules avanzate

Quattro regole in `.cursor/rules/`, una per ogni tipo:

| File | Tipo | Si attiva... |
|------|------|--------------|
| `sempre-italiano.mdc` | Always | sempre |
| `componenti-react.mdc` | Auto Attached (glob `src/components/**/*.tsx`) | quando nel contesto c'è un componente React |
| `gestione-errori.mdc` | Agent Requested | quando l'agente ritiene utile la description |
| `checklist-release.mdc` | Manual | solo se scrivi `@checklist-release` |

## ⚠️ Importante: apri questa cartella come workspace
Cursor legge solo la cartella `.cursor` nella **radice del workspace**. Per provare queste regole:
**File → Open Folder → `examples/rules-avanzate`** (aprila come progetto a sé).

## Prompt da provare
1. **Always** – "Scrivi una funzione che somma due numeri" → risposta in italiano, TypeScript strict.
2. **Auto Attached** – apri `src/components/Saluto.tsx` e chiedi "Crea un componente `Pulsante` simile" → props con interfaccia `PulsanteProps`, niente classi.
3. **Agent Requested** – "Come dovrei gestire gli errori in una funzione che legge un file?" → l'agente dovrebbe caricare `gestione-errori.mdc`.
4. **Manual** – "@checklist-release prepara la release 1.1.0" → segue la checklist e non esegue il tag.

Suggerimento: nel pannello della chat Cursor mostra quali regole sono state applicate.
