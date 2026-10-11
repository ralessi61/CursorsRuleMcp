// ReAct = Reason + Act: ciclo Pensiero -> Azione -> Osservazione
import { cercaDocumenti, calcola, LLM } from "./strumenti.js";

// LLM simulato: guarda lo storico e decide il prossimo passo
const llmFinto: LLM = (storico) => {
  if (!storico.includes("Osservazione:"))
    return "Pensiero: devo sapere quanti giorni di ferie ci sono.\nAzione: cerca_documenti[ferie]";
  if (!storico.includes("Azione: calcola"))
    return "Pensiero: 26 giorni all'anno, la domanda chiede i giorni in 2 anni.\nAzione: calcola[26 * 2]";
  return "Pensiero: ho tutto.\nRisposta finale: In 2 anni hai 52 giorni di ferie [fonte: policy-ferie.md].";
};

const domanda = "Quanti giorni di ferie maturo in 2 anni?";
let storico = `Domanda: ${domanda}\n`;
const MAX_PASSI = 5; // limite di sicurezza contro i loop infiniti

for (let passo = 1; passo <= MAX_PASSI; passo++) {
  const output = llmFinto(storico);
  console.log(`--- Passo ${passo} ---\n${output}`);
  storico += output + "\n";

  if (output.includes("Risposta finale:")) break; // il modello ha finito

  // Estrae l'azione richiesta, es. "cerca_documenti[ferie]"
  const m = output.match(/Azione: (\w+)\[(.*)\]/);
  if (!m) break;
  const [, tool, arg] = m;
  const osservazione = tool === "cerca_documenti" ? cercaDocumenti(arg) : calcola(arg);
  console.log(`Osservazione: ${osservazione}`);
  storico += `Osservazione: ${osservazione}\n`;
}
