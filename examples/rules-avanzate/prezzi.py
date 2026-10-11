"""Modulo di esempio da testare."""


def applica_sconto(prezzo: float, percentuale: float) -> float:
    """Applica uno sconto percentuale (0-100) al prezzo."""
    if not 0 <= percentuale <= 100:
        raise ValueError("la percentuale deve essere tra 0 e 100")
    return round(prezzo * (1 - percentuale / 100), 2)
