# MCP – Model Context Protocol

## Cosa è
**MCP** è un protocollo aperto che standardizza il modo in cui un'applicazione AI (es. Cursor) si collega a strumenti e dati esterni. È spesso descritto come "la porta USB-C delle applicazioni AI": scrivi un server una volta e funziona con qualunque client compatibile.

## Architettura: client e server
- **Host / Client**: l'app che usa l'LLM (Cursor, Claude Desktop, ...). Avvia i server e passa al modello l'elenco degli strumenti disponibili.
- **Server**: un piccolo programma che espone capacità. Può girare in locale (trasporto **stdio**) o in remoto (trasporto **HTTP**).

```
[ LLM ] <-> [ Cursor (client MCP) ] <-stdio/HTTP-> [ Server MCP ] <-> [ GitHub / DB / file ... ]
```

## Cosa espone un server
- **Tools**: funzioni che il modello può *invocare* (es. `cerca_documenti`, `create_issue`). Hanno un nome, una descrizione e uno schema degli input.
- **Resources**: dati *leggibili* identificati da un URI (es. `doc://manuale.md`), utili come contesto.
- **Prompts**: modelli di prompt riutilizzabili.

## Quali problemi risolve
- **Integrazioni N×M**: senza standard ogni app deve integrare ogni servizio a mano. Con MCP: N client + M server.
- **Dati aggiornati**: il modello accede a dati reali (DB, ticket, documenti) invece di inventarli.
- **Azioni**: l'agente può *fare* cose (aprire una PR, eseguire una query), non solo scrivere testo.
- **Separazione e sicurezza**: le credenziali restano nel server, i permessi sono controllati e Cursor chiede conferma prima di eseguire i tool.

## Configurazione in Cursor
Due posizioni possibili:

| File | Ambito |
|------|--------|
| `.cursor/mcp.json` (nel progetto) | Solo quel progetto, condivisibile col team via git |
| `~/.cursor/mcp.json` (nella home) | Tutti i progetti, personale |

Esempio (server locale via stdio):
```json
{
  "mcpServers": {
    "documenti": {
      "command": "examples/mcp-server-python/.venv/bin/python",
      "args": ["examples/mcp-server-python/server.py"]
    }
  }
}
```

## Segreti: usa le variabili d'ambiente
Non scrivere mai token nel file (finirebbero su git). Usa l'interpolazione:
```json
{
  "mcpServers": {
    "mio-server": {
      "command": ".venv/bin/python",
      "args": ["server.py"],
      "env": { "API_KEY": "${env:API_KEY}" }
    }
  }
}
```
e imposta la variabile nella shell (`export API_KEY=...`) prima di avviare Cursor. Nel codice Python del server la leggi con:
```python
import os
api_key = os.environ["API_KEY"]  # mai scritta nel codice
```
(Lo stesso schema è usato per il server GitHub nel `.cursor/mcp.json` della radice.)

## Esempi d'uso (prompt in Cursor)
- "Elenca le issue aperte con label bug" → tool del server GitHub.
- "Quante righe ha la tabella users?" → tool `query` del server Postgres.
- "Cerca nei documenti la policy sulle ferie" → tool `cerca_documenti` del nostro server custom.

## Esempi nel repo
- Radice: `.cursor/mcp.json` (GitHub + Postgres; questi server ufficiali si avviano con `npx`, quindi richiedono Node.js)
- Server personalizzato in Python (FastMCP): [examples/mcp-server-python](../examples/mcp-server-python/README.md)
