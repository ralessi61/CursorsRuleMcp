"""ReAct = Reason + Act: ciclo Pensiero -> Azione -> Osservazione."""
import re

from strumenti import calcola, cerca_documenti


def llm_finto(storico: str) -> str:
    """LLM simulato: guarda lo storico e decide il prossimo passo."""
    if "Osservazione:" not in storico:
        return "Pensiero: devo sapere quanti giorni di ferie ci sono.\nAzione: cerca_documenti[ferie]"
    if "Azione: calcola" not in storico:
        return "Pensiero: 26 giorni all'anno, la domanda chiede i giorni in 2 anni.\nAzione: calcola[26 * 2]"
    return "Pensiero: ho tutto.\nRisposta finale: In 2 anni hai 52 giorni di ferie [fonte: policy-ferie.md]."


TOOLS = {"cerca_documenti": cerca_documenti, "calcola": calcola}
MAX_PASSI = 5  # limite di sicurezza contro i loop infiniti

domanda = "Quanti giorni di ferie maturo in 2 anni?"
storico = f"Domanda: {domanda}\n"

for passo in range(1, MAX_PASSI + 1):
    output = llm_finto(storico)
    print(f"--- Passo {passo} ---\n{output}")
    storico += output + "\n"

    if "Risposta finale:" in output:  # il modello ha finito
        break

    # Estrae l'azione richiesta, es. "cerca_documenti[ferie]"
    m = re.search(r"Azione: (\w+)\[(.*)\]", output)
    if not m or m.group(1) not in TOOLS:
        break
    osservazione = TOOLS[m.group(1)](m.group(2))
    print(f"Osservazione: {osservazione}")
    storico += f"Osservazione: {osservazione}\n"
