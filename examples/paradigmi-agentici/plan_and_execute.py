"""Plan and Execute: prima si crea il piano, poi si eseguono i passi."""
from strumenti import cerca_documenti


def pianificatore(obiettivo: str) -> str:
    """Pianificatore simulato: restituisce un elenco di passi (uno per riga)."""
    return "\n".join(["cerca: ferie", "cerca: smart working", "cerca: rimborso", "riassumi"])


def esegui(passo: str, risultati: list[str]) -> str:
    """Esecutore: svolge un singolo passo (qui senza LLM, solo tool)."""
    if passo.startswith("cerca: "):
        return cerca_documenti(passo.removeprefix("cerca: "))
    if passo == "riassumi":
        return "RIEPILOGO ONBOARDING:\n" + "\n".join(risultati)
    return "passo sconosciuto"


obiettivo = "Prepara un riepilogo per un nuovo assunto su ferie, smart working e rimborsi"
print(f"Obiettivo: {obiettivo}\n")

# 1. Pianificazione (una sola chiamata al modello "grande")
piano = pianificatore(obiettivo).split("\n")
print("Piano:")
for i, p in enumerate(piano, 1):
    print(f"  {i}. {p}")
print()

# 2. Esecuzione passo per passo
risultati: list[str] = []
for passo in piano:
    r = esegui(passo, risultati)
    print(f"> {passo}\n{r}\n")
    risultati.append(r)
