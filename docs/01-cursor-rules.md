# Cursor Rules

## Cosa sono
Le **Cursor Rules** sono istruzioni persistenti, scritte in Markdown, che Cursor inserisce nel contesto dell'agente AI. Servono a "insegnare" al modello le convenzioni del progetto una volta sola, invece di ripeterle in ogni prompt.

Si salvano in `.cursor/rules/*.mdc` (nella **radice** del workspace). Ogni file ha un'intestazione YAML (frontmatter) e un corpo:

```markdown
---
description: Convenzioni per le query SQL
globs: app/db/**/*.py
alwaysApply: false
---
- Usa sempre query parametrizzate, mai concatenazione di stringhe.
```

## Quali problemi risolvono
- **Ripetizione**: non devi riscrivere "usa Python con type hint, segui PEP 8" in ogni chat.
- **Incoerenza**: tutto il team (e l'AI) segue le stesse convenzioni.
- **Contesto mancante**: l'AI non conosce architettura, librerie scelte, regole di sicurezza: le regole gliele dicono.
- **Spreco di contesto**: con glob e description le regole si caricano solo quando servono.

## I quattro tipi di regole

| Tipo | Frontmatter | Quando viene applicata |
|------|-------------|------------------------|
| **Always** | `alwaysApply: true` | In ogni richiesta |
| **Auto Attached** (glob) | `globs: ...`, `alwaysApply: false` | Quando nel contesto c'è un file che corrisponde al glob |
| **Agent Requested** | solo `description`, `alwaysApply: false` | L'agente legge la description e decide se gli serve |
| **Manual** | niente description/globs, `alwaysApply: false` | Solo se la citi esplicitamente con `@nome-regola` |

### 1. Always
```markdown
---
alwaysApply: true
---
Rispondi in italiano. Codice Python 3.10+ con type hint.
```
Uso: convenzioni generali, brevi. Attenzione: costano token in *ogni* richiesta.

### 2. Auto Attached (globs)
```markdown
---
globs: tests/**/*.py
alwaysApply: false
---
Test con pytest: funzioni `test_...`, `@pytest.mark.parametrize` per più casi.
```
Uso: regole specifiche per una parte del codice (test, modelli, migrazioni).

### 3. Agent Requested (description)
```markdown
---
description: Come scrivere e gestire migrazioni del database
alwaysApply: false
---
Ogni migrazione deve avere up e down...
```
Uso: conoscenza "su richiesta". La **description** deve essere chiara: è l'unica cosa che l'agente vede per decidere.

### 4. Manual
```markdown
---
alwaysApply: false
---
Checklist di release: ...
```
Uso: procedure occasionali. Nel prompt scrivi: `@release-checklist prepara la release 1.2`.

## Buone pratiche
- Regole brevi e concrete (meglio elenchi puntati con esempi).
- Una regola = un argomento.
- Preferisci glob/description a `alwaysApply` quando possibile.
- Versiona `.cursor/rules` con git: le regole sono parte del progetto.

## Esempi nel repo
- Radice: `.cursor/rules/style.mdc`, `tests.mdc`, `database.mdc`
- Esempi estesi: [examples/rules-avanzate](../examples/rules-avanzate/README.md)
