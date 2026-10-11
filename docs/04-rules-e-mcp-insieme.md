# Rules e MCP insieme

**MCP** dà all'agente le *capacità* (i tool). Le **Rules** gli dicono *quando* e *come* usarle. Insieme rendono l'agente utile **e** prevedibile.

## Problemi che risolve la combinazione
- L'agente **non usa** un tool quando dovrebbe (risponde "a memoria").
- L'agente **usa troppo** i tool, o quelli sbagliati (costi, lentezza).
- L'agente compie **azioni rischiose** senza conferma (es. scrivere sul DB di produzione).
- L'output non ha un **formato** coerente (es. manca la fonte).

## Esempi di regole

### Forzare l'uso di un tool
```markdown
---
description: Domande su policy, procedure o regolamenti aziendali
alwaysApply: false
---
- Prima di rispondere chiama SEMPRE il tool MCP `cerca_documenti`.
- Non rispondere usando conoscenze generali.
```

### Limitare l'uso di un tool rischioso
```markdown
---
globs: src/db/**
alwaysApply: false
---
- Con il server MCP `postgres` esegui solo query SELECT.
- Per INSERT/UPDATE/DELETE mostra la query e chiedi conferma all'utente.
```

### Definire il formato dell'output
```markdown
---
alwaysApply: true
---
Quando usi informazioni ottenute da un tool MCP, indica la fonte tra parentesi quadre.
```

## Come provarlo
Vedi [examples/rag-documenti-aziendali](../examples/rag-documenti-aziendali/README.md): una regola + la configurazione del server MCP [mcp-server-custom](../examples/mcp-server-custom/README.md).
