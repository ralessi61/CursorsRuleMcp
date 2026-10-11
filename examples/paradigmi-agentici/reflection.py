"""Reflection: bozza -> critica -> revisione, per al massimo N iterazioni."""
import re

from strumenti import cerca_documenti

contesto = cerca_documenti("ferie")


def autore(prompt: str) -> str:
    """Autore simulato: la prima bozza "inventa" e non cita la fonte."""
    if "CRITICA:" in prompt:
        return "Hai diritto a 26 giorni di ferie all'anno [fonte: policy-ferie.md]."
    return "Hai diritto a 30 giorni di ferie e puoi prenderli quando vuoi."


def critico(bozza: str) -> str | None:
    """Controlla fonte e numeri. Restituisce None se la bozza è approvata."""
    problemi = []
    if "[fonte:" not in bozza:
        problemi.append("manca la citazione della fonte")
    for n in re.findall(r"\d+", bozza):
        if n not in contesto:
            problemi.append(f"il numero {n} non è nei documenti")
    return "; ".join(problemi) or None


domanda = "Quanti giorni di ferie ho?"
bozza = autore(f"Domanda: {domanda}\nContesto: {contesto}")
for i in range(1, 4):
    print(f"Bozza {i}: {bozza}")
    critica = critico(bozza)
    if critica is None:
        print("Critico: ✅ approvata")
        break
    print(f"Critico: ❌ {critica}")
    bozza = autore(f"Domanda: {domanda}\nBozza: {bozza}\nCRITICA: {critica}")
