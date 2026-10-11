# Documentazione (in italiano)

Indice dei materiali aggiunti per il corso di *Agentic AI*.

- 📘 [Manuale d'uso passo passo](MANUALE.md) – come eseguire tutti gli esempi

## Guide
1. [Cursor Rules](01-cursor-rules.md) – cosa sono, i tipi, esempi
2. [MCP – Model Context Protocol](02-mcp.md) – client/server, tool, configurazione
3. [Paradigmi agentici](03-paradigmi-agentici.md) – ReAct, Plan and Execute, Reflection
4. [Rules e MCP insieme](04-rules-e-mcp-insieme.md) – guidare l'uso dei tool con le regole

## Esempi pratici
- [examples/rules-avanzate](../examples/rules-avanzate/README.md) – i quattro tipi di regole `.mdc` (su un progetto Python)
- [examples/mcp-server-python](../examples/mcp-server-python/README.md) – un server MCP in Python con FastMCP (`cerca_documenti`)
- [examples/paradigmi-agentici](../examples/paradigmi-agentici/README.md) – ReAct, Plan and Execute, Reflection con LLM simulato (Python, solo libreria standard)
- [examples/rag-documenti-aziendali](../examples/rag-documenti-aziendali/README.md) – regola + MCP per risposte con citazioni

## Esempi già presenti nella radice del repo
- `.cursor/rules/*.mdc` – regole di base (stile, test, database)
- `.cursor/mcp.json` – configurazione MCP con server GitHub e Postgres
