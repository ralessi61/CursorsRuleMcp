# Esempio: server MCP in Python (FastMCP)

Equivalente Python di [mcp-server-custom](../mcp-server-custom/README.md): stesso tool `cerca_documenti(query)` e stessa resource `doc://{nome}` sugli stessi documenti di esempio (`documenti/`). Usa l'SDK ufficiale [`mcp`](https://pypi.org/project/mcp/) con **FastMCP** e trasporto **stdio**.

## Che problema risolve
L'LLM non conosce i documenti interni dell'azienda: questo server permette a Cursor di cercarli su richiesta e di citare la fonte (`[fonte: file.md]`), invece di inventare.

## Setup
Con `venv` e `pip`:
```bash
cd examples/mcp-server-python
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
Oppure con [`uv`](https://docs.astral.sh/uv/):
```bash
uv venv && uv pip install -r requirements.txt
# oppure, senza creare il venv a mano:
uv run --with "mcp<2" server.py
```

## Registrazione in Cursor
`.cursor/mcp.json` di questa cartella (aprila come workspace: Cursor legge `.cursor` solo nella radice):
```json
{
  "mcpServers": {
    "documenti-aziendali-py": { "command": ".venv/bin/python", "args": ["server.py"] }
  }
}
```
Su Windows usa `.venv\\Scripts\\python.exe`. Se il percorso relativo non viene risolto, oppure in `~/.cursor/mcp.json`, usa percorsi assoluti. Alternativa con uv:
```json
{ "mcpServers": { "documenti-aziendali-py": { "command": "uv", "args": ["run", "--with", "mcp<2", "/percorso/assoluto/server.py"] } } }
```

## Confronto con la versione TypeScript
| Aspetto | TypeScript (`mcp-server-custom`) | Python (questo esempio) |
|---------|----------------------------------|-------------------------|
| SDK | `@modelcontextprotocol/sdk` | `mcp` (FastMCP) |
| Definizione tool | `server.registerTool(nome, {inputSchema: zod}, handler)` | decoratore `@mcp.tool()` |
| Schema input | esplicito con **zod** | dedotto dai **type hint** (`query: str`) |
| Descrizione | campo `description` | docstring della funzione |
| Resource | `new ResourceTemplate("doc://{nome}")` | `@mcp.resource("doc://{nome}")` |
| Build | serve `tsc` (o `tsx`) | nessuna, si esegue direttamente |
| Avvio | `node dist/server.js` | `python server.py` |

Stesso protocollo: per Cursor i due server sono intercambiabili.

## Prompt da provare
- "Quanti giorni di ferie ho?" → `cerca_documenti("ferie")`
- "Qual è il rimborso massimo per un pasto?"
- "Posso lavorare da remoto il venerdì?"
- "Qual è il dress code?" → "non trovato nei documenti"

## Test senza Cursor
`npx @modelcontextprotocol/inspector .venv/bin/python server.py`

## Nota sulle versioni
`requirements.txt` fissa `mcp<2`: nella versione 2.x dell'SDK `FastMCP` è stato rinominato `MCPServer` (`from mcp.server.mcpserver import MCPServer`). Questo esempio usa l'API 1.x con `FastMCP`, la più diffusa nei tutorial; per migrare vedi la [guida ufficiale](https://py.sdk.modelcontextprotocol.io/v2/migration/).
