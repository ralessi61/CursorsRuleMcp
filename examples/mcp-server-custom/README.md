# Esempio: server MCP personalizzato

Un server MCP in TypeScript (SDK ufficiale `@modelcontextprotocol/sdk`) che espone:
- il **tool** `cerca_documenti(query)`: cerca nei file di `documenti/` e restituisce le righe trovate con `[fonte: file.md]`;
- la **resource** `doc://{nome}`: il contenuto completo di un documento.

## Che problema risolve
L'LLM non conosce i documenti interni della tua azienda. Con questo server Cursor può cercarli su richiesta, invece di inventare la risposta.

## Avvio
```bash
cd examples/mcp-server-custom
npm install
npm run build      # compila in dist/
```

## Registrazione in Cursor
Il file `.cursor/mcp.json` di questa cartella registra il server (percorso relativo alla cartella):
```json
{ "mcpServers": { "documenti-aziendali": { "command": "node", "args": ["dist/server.js"] } } }
```
Apri `examples/mcp-server-custom` come workspace in Cursor (Cursor legge `.cursor` solo nella radice), poi in **Settings → MCP** verifica che il server sia attivo.

In alternativa, aggiungilo a `~/.cursor/mcp.json` con un percorso assoluto:
```json
{ "mcpServers": { "documenti-aziendali": { "command": "node", "args": ["/percorso/assoluto/examples/mcp-server-custom/dist/server.js"] } } }
```

## Prompt da provare
- "Quanti giorni di ferie ho?" → chiama `cerca_documenti("ferie")`.
- "Qual è il rimborso massimo per un pasto?"
- "Posso lavorare da remoto il venerdì?"

## Test senza Cursor
Puoi usare l'inspector ufficiale: `npx @modelcontextprotocol/inspector node dist/server.js`.

Nota: nessun segreto è necessario. Se un tuo server ne avesse bisogno, passalo con `"env": { "API_KEY": "${env:API_KEY}" }`.
