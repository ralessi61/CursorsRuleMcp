"""Strumenti e LLM SIMULATI: nessuna API key necessaria (solo libreria standard)."""
import ast
import operator
from typing import Callable

# Piccolo "archivio documenti" in memoria
DOCUMENTI: dict[str, str] = {
    "policy-ferie.md": "Ogni dipendente ha diritto a 26 giorni di ferie all'anno.",
    "smart-working.md": "Smart working fino a 2 giorni a settimana.",
    "rimborsi-spese.md": "Rimborso massimo per un pasto in trasferta: 30 euro.",
}


def cerca_documenti(query: str) -> str:
    """Tool: cerca una parola nei documenti e restituisce '[fonte] testo'."""
    trovati = [f"[fonte: {nome}] {testo}" for nome, testo in DOCUMENTI.items()
               if query.lower() in testo.lower()]
    return "\n".join(trovati) if trovati else "non trovato nei documenti"


# Operatori ammessi dalla calcolatrice (niente eval: è più sicuro)
_OPERATORI = {ast.Add: operator.add, ast.Sub: operator.sub,
              ast.Mult: operator.mul, ast.Div: operator.truediv}


def calcola(espressione: str) -> str:
    """Tool: calcolatrice semplice (numeri e + - * /)."""
    def valuta(nodo: ast.AST) -> float:
        if isinstance(nodo, ast.Constant) and isinstance(nodo.value, (int, float)):
            return nodo.value
        if isinstance(nodo, ast.BinOp) and type(nodo.op) in _OPERATORI:
            return _OPERATORI[type(nodo.op)](valuta(nodo.left), valuta(nodo.right))
        raise ValueError("espressione non valida")
    try:
        return str(valuta(ast.parse(espressione, mode="eval").body))
    except (ValueError, SyntaxError):
        return "espressione non valida"


# Un "LLM" è semplicemente una funzione: prompt (str) -> risposta (str).
# Negli esempi è finta e risponde in base a parole chiave.
LLM = Callable[[str], str]
