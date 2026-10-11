"""Server MCP minimale in Python (SDK ufficiale `mcp`, FastMCP).

Espone:
- il tool `cerca_documenti(query)` sui file Markdown della cartella ./documenti
- la resource `doc://{nome}` con il contenuto completo di un documento
"""
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Cartella dei documenti, relativa a questo file
CARTELLA_DOCUMENTI = Path(__file__).parent / "documenti"

# 1. Creiamo il server con un nome
mcp = FastMCP("documenti-aziendali")


def carica_documenti() -> list[tuple[str, str]]:
    """Restituisce una lista di (nome_file, testo) per ogni .md."""
    return [(p.name, p.read_text(encoding="utf-8")) for p in sorted(CARTELLA_DOCUMENTI.glob("*.md"))]


# 2. TOOL: FastMCP ricava nome, descrizione (docstring) e schema (type hint)
@mcp.tool()
def cerca_documenti(query: str) -> str:
    """Cerca una parola o frase nei documenti aziendali e restituisce le righe trovate con il nome del file sorgente."""
    parole = [p for p in query.lower().split() if p]
    risultati = []
    for nome, testo in carica_documenti():
        # Teniamo le righe che contengono almeno una parola cercata
        righe = [r for r in testo.splitlines() if any(p in r.lower() for p in parole)]
        if righe:
            risultati.append(f"[fonte: {nome}]\n" + "\n".join(righe))
    return "\n\n".join(risultati) if risultati else "Nessun risultato: non trovato nei documenti."


# 3. RESOURCE: ogni documento leggibile con URI doc://<nome>
@mcp.resource("doc://{nome}")
def leggi_documento(nome: str) -> str:
    """Contenuto completo di un documento aziendale."""
    percorso = (CARTELLA_DOCUMENTI / nome).resolve()
    # Sicurezza: impediamo di uscire dalla cartella documenti (es. ../../segreti)
    if percorso.parent != CARTELLA_DOCUMENTI.resolve():
        raise ValueError("Documento non valido")
    return percorso.read_text(encoding="utf-8")


# 4. Avvio su stdio: Cursor lancia questo script come processo figlio.
#    Attenzione: con stdio non usare print() (sporcherebbe il protocollo).
if __name__ == "__main__":
    mcp.run(transport="stdio")
